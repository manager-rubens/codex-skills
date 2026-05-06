param(
  [string]$RepoUrl = "https://github.com/manager-rubens/codex-skills.git",
  [string]$Branch = "main",
  [string]$WorkDir = (Join-Path (Get-Location).Path "codex-skills"),
  [string]$PersonalSkillsRoot = "",
  [switch]$Publish,
  [switch]$AllowRemovals,
  [switch]$SkipValidation,
  [string]$CommitMessage = "Update personal Codex skills catalog"
)

$ErrorActionPreference = "Stop"
$GeneratedAt = Get-Date -Format "yyyy-MM-dd"
$TimeZone = "America/Sao_Paulo"

function Invoke-Checked {
  param(
    [string]$FilePath,
    [string[]]$Arguments,
    [string]$WorkingDirectory = (Get-Location).Path
  )

  $previous = (Get-Location).Path
  try {
    Set-Location $WorkingDirectory
    & $FilePath @Arguments
    if ($LASTEXITCODE -ne 0) {
      throw "Command failed: $FilePath $($Arguments -join ' ')"
    }
  }
  finally {
    Set-Location $previous
  }
}

function Get-GitOutput {
  param(
    [string[]]$Arguments,
    [string]$WorkingDirectory
  )

  $previous = (Get-Location).Path
  try {
    Set-Location $WorkingDirectory
    $output = & git @Arguments
    if ($LASTEXITCODE -ne 0) {
      throw "Git command failed: git $($Arguments -join ' ')"
    }
    return $output
  }
  finally {
    Set-Location $previous
  }
}

function Write-Utf8NoBom {
  param(
    [string]$Path,
    [string]$Content
  )

  $encoding = New-Object System.Text.UTF8Encoding($false)
  [IO.File]::WriteAllText($Path, $Content, $encoding)
}

function Assert-UnderPath {
  param(
    [string]$Root,
    [string]$Path
  )

  $resolvedRoot = [IO.Path]::GetFullPath($Root).TrimEnd("\")
  $resolvedPath = [IO.Path]::GetFullPath($Path).TrimEnd("\")
  if (-not $resolvedPath.StartsWith($resolvedRoot, [StringComparison]::OrdinalIgnoreCase)) {
    throw "Refusing to touch path outside expected root: $resolvedPath"
  }
}

function Read-FrontmatterField {
  param(
    [string]$Content,
    [string]$Field
  )

  $match = [regex]::Match($Content, "(?ms)^---\s*(.*?)\s*---")
  if (-not $match.Success) {
    return ""
  }

  $line = ($match.Groups[1].Value -split "`r?`n" | Where-Object { $_ -match "^\s*$Field\s*:" } | Select-Object -First 1)
  if (-not $line) {
    return ""
  }

  $value = ($line -replace "^\s*$Field\s*:\s*", "").Trim()
  if (($value.StartsWith('"') -and $value.EndsWith('"')) -or ($value.StartsWith("'") -and $value.EndsWith("'"))) {
    $value = $value.Substring(1, $value.Length - 2)
  }
  return $value
}

function Escape-MarkdownCell {
  param([string]$Value)
  return (($Value -replace "\|", "\|") -replace "`r?`n", " ").Trim()
}

function Escape-CsvCell {
  param([string]$Value)
  $escaped = $Value -replace '"', '""'
  return '"' + $escaped + '"'
}

function Get-Sha256 {
  param([string]$Content)

  $sha = [Security.Cryptography.SHA256]::Create()
  $bytes = [Text.Encoding]::UTF8.GetBytes($Content)
  $hash = $sha.ComputeHash($bytes)
  return -join ($hash | ForEach-Object { $_.ToString("x2") })
}

function Test-RepoDirty {
  param([string]$RepoRoot)
  $status = @(Get-GitOutput -Arguments @("status", "--porcelain") -WorkingDirectory $RepoRoot)
  return $status.Count -gt 0
}

if (-not $PersonalSkillsRoot) {
  if ($env:CODEX_HOME) {
    $PersonalSkillsRoot = Join-Path $env:CODEX_HOME "skills"
  }
  else {
    $PersonalSkillsRoot = Join-Path $env:USERPROFILE ".codex\skills"
  }
}

if (-not (Test-Path $PersonalSkillsRoot)) {
  throw "Personal skills root not found: $PersonalSkillsRoot"
}

$WorkDir = [IO.Path]::GetFullPath($WorkDir)
$parent = Split-Path -Parent $WorkDir
if (-not (Test-Path $parent)) {
  New-Item -ItemType Directory -Path $parent | Out-Null
}

if (-not (Test-Path $WorkDir)) {
  Invoke-Checked -FilePath "git" -Arguments @("clone", $RepoUrl, $WorkDir) -WorkingDirectory $parent
}

if (-not (Test-Path (Join-Path $WorkDir ".git"))) {
  throw "WorkDir is not a git checkout: $WorkDir"
}

if (Test-RepoDirty -RepoRoot $WorkDir) {
  throw "Catalog checkout has local changes before sync. Commit, stash, or use a clean checkout: $WorkDir"
}

Invoke-Checked -FilePath "git" -Arguments @("fetch", "origin", $Branch) -WorkingDirectory $WorkDir
Invoke-Checked -FilePath "git" -Arguments @("checkout", $Branch) -WorkingDirectory $WorkDir
Invoke-Checked -FilePath "git" -Arguments @("pull", "--ff-only", "origin", $Branch) -WorkingDirectory $WorkDir

$repoSkillsRoot = Join-Path $WorkDir "skills"
if (-not (Test-Path $repoSkillsRoot)) {
  New-Item -ItemType Directory -Path $repoSkillsRoot | Out-Null
}

$systemRoot = (Join-Path $PersonalSkillsRoot ".system").TrimEnd("\")
$localSkillDirs = @(Get-ChildItem -Path $PersonalSkillsRoot -Directory -Force |
  Where-Object {
    -not $_.FullName.TrimEnd("\").Equals($systemRoot, [StringComparison]::OrdinalIgnoreCase) -and
    (Test-Path (Join-Path $_.FullName "SKILL.md"))
  } |
  Sort-Object Name)

$localNames = @($localSkillDirs | ForEach-Object { $_.Name })
$remoteSkillDirs = @(Get-ChildItem -Path $repoSkillsRoot -Directory -Force -ErrorAction SilentlyContinue |
  Where-Object { Test-Path (Join-Path $_.FullName "SKILL.md") } |
  Sort-Object Name)
$remoteNames = @($remoteSkillDirs | ForEach-Object { $_.Name })
$staleRemote = @($remoteNames | Where-Object { $localNames -notcontains $_ })

if ($staleRemote.Count -gt 0 -and -not $AllowRemovals) {
  Write-Host "Stale remote skills kept because -AllowRemovals was not supplied: $($staleRemote -join ', ')"
}

foreach ($dir in $localSkillDirs) {
  $target = Join-Path $repoSkillsRoot $dir.Name
  Assert-UnderPath -Root $repoSkillsRoot -Path $target
  if (Test-Path $target) {
    Remove-Item -LiteralPath $target -Recurse -Force
  }
  Copy-Item -LiteralPath $dir.FullName -Destination $target -Recurse -Force
}

if ($AllowRemovals) {
  foreach ($name in $staleRemote) {
    $target = Join-Path $repoSkillsRoot $name
    Assert-UnderPath -Root $repoSkillsRoot -Path $target
    Remove-Item -LiteralPath $target -Recurse -Force
  }
}

$skillDirs = @(Get-ChildItem -Path $repoSkillsRoot -Directory -Force |
  Where-Object { Test-Path (Join-Path $_.FullName "SKILL.md") } |
  Sort-Object Name)

$skills = New-Object System.Collections.Generic.List[object]
foreach ($dir in $skillDirs) {
  $skillFile = Join-Path $dir.FullName "SKILL.md"
  $content = Get-Content -Raw -Encoding UTF8 -Path $skillFile
  $name = Read-FrontmatterField -Content $content -Field "name"
  if (-not $name) {
    $name = $dir.Name
  }
  $description = Read-FrontmatterField -Content $content -Field "description"
  $repoPath = "skills/$name/SKILL.md"

  $skills.Add([pscustomobject][ordered]@{
    name = $name
    description = $description
    source_path = '$CODEX_HOME/skills/' + $name + '/SKILL.md'
    repository_path = $repoPath
    sha256 = Get-Sha256 $content
    content = $content
  }) | Out-Null
}

$total = $skills.Count
$metadataSkills = @($skills | ForEach-Object {
  [pscustomobject][ordered]@{
    name = $_.name
    description = $_.description
    source_path = $_.source_path
    repository_path = $_.repository_path
    sha256 = $_.sha256
  }
})

$payload = [ordered]@{
  generated_at = $GeneratedAt
  timezone = $TimeZone
  scope = 'Only user-created Codex skills from $CODEX_HOME/skills, excluding .system and plugin caches.'
  totals = [ordered]@{
    user_created_skills = $total
  }
  skills = $metadataSkills
}

$json = $payload | ConvertTo-Json -Depth 8
Write-Utf8NoBom -Path (Join-Path $WorkDir "data\skills.json") -Content ($json + "`n")

$csvLines = New-Object System.Collections.Generic.List[string]
$csvLines.Add("name,repository_path,source_path,sha256,description") | Out-Null
foreach ($skill in $skills) {
  $csvLines.Add((
    @(
      Escape-CsvCell $skill.name
      Escape-CsvCell $skill.repository_path
      Escape-CsvCell $skill.source_path
      Escape-CsvCell $skill.sha256
      Escape-CsvCell $skill.description
    ) -join ","
  )) | Out-Null
}
Write-Utf8NoBom -Path (Join-Path $WorkDir "data\skills.csv") -Content (($csvLines -join "`n") + "`n")

$docs = New-Object System.Text.StringBuilder
[void]$docs.AppendLine("# Skills pessoais do Codex")
[void]$docs.AppendLine("")
[void]$docs.AppendLine("Gerado em $GeneratedAt ($TimeZone).")
[void]$docs.AppendLine("")
[void]$docs.AppendLine('Escopo: somente skills criadas pelo usuario em `$CODEX_HOME/skills`. Foram excluidas as skills originais do Codex em `.system` e as skills vindas de plugins/cache.')
[void]$docs.AppendLine("")
[void]$docs.AppendLine("## Resumo")
[void]$docs.AppendLine("")
[void]$docs.AppendLine("| Metrica | Total |")
[void]$docs.AppendLine("| --- | ---: |")
[void]$docs.AppendLine("| Skills pessoais catalogadas | $total |")
[void]$docs.AppendLine("")
[void]$docs.AppendLine("## Catalogo")
[void]$docs.AppendLine("")
[void]$docs.AppendLine("| Skill | Arquivo | Descricao |")
[void]$docs.AppendLine("| --- | --- | --- |")
foreach ($skill in $skills) {
  $nameCell = Escape-MarkdownCell $skill.name
  $pathCell = Escape-MarkdownCell $skill.repository_path
  $descriptionCell = Escape-MarkdownCell $skill.description
  [void]$docs.AppendLine("| ``$nameCell`` | [$pathCell](../$pathCell) | $descriptionCell |")
}

[void]$docs.AppendLine("")
[void]$docs.AppendLine("## Conteudo completo")
foreach ($skill in $skills) {
  [void]$docs.AppendLine("")
  [void]$docs.AppendLine("### $($skill.name)")
  [void]$docs.AppendLine("")
  [void]$docs.AppendLine("Origem: ``$($skill.source_path)``")
  [void]$docs.AppendLine("")
  [void]$docs.AppendLine('````markdown')
  [void]$docs.AppendLine($skill.content.TrimEnd())
  [void]$docs.AppendLine('````')
}
Write-Utf8NoBom -Path (Join-Path $WorkDir "docs\skills.md") -Content ($docs.ToString().TrimEnd() + "`n")

$readme = New-Object System.Text.StringBuilder
[void]$readme.AppendLine("# Codex Skills")
[void]$readme.AppendLine("")
[void]$readme.AppendLine("Catalogo das skills pessoais criadas neste ambiente local do Codex.")
[void]$readme.AppendLine("")
[void]$readme.AppendLine("Gerado em: $GeneratedAt ($TimeZone)")
[void]$readme.AppendLine("")
[void]$readme.AppendLine("## Escopo")
[void]$readme.AppendLine("")
[void]$readme.AppendLine('Este repositorio contem somente skills criadas pelo usuario em `$CODEX_HOME/skills`.')
[void]$readme.AppendLine("")
[void]$readme.AppendLine("Nao inclui:")
[void]$readme.AppendLine("")
[void]$readme.AppendLine('- skills originais do Codex em `$CODEX_HOME/skills/.system`')
[void]$readme.AppendLine("- skills de plugins/cache, como Figma, GitHub, Vercel, Browser Use ou Gmail")
[void]$readme.AppendLine("")
[void]$readme.AppendLine("## Skills catalogadas")
[void]$readme.AppendLine("")
foreach ($skill in $skills) {
  [void]$readme.AppendLine("- [$($skill.name)]($($skill.repository_path))")
}
[void]$readme.AppendLine("")
[void]$readme.AppendLine("## Arquivos")
[void]$readme.AppendLine("")
[void]$readme.AppendLine("- `skills/<nome>/SKILL.md`: conteudo completo de cada skill pessoal.")
[void]$readme.AppendLine("- `docs/skills.md`: catalogo legivel com os conteudos completos reunidos.")
[void]$readme.AppendLine("- `data/skills.json`: inventario estruturado com metadados e checksums.")
[void]$readme.AppendLine("- `data/skills.csv`: exportacao tabular com metadados.")
[void]$readme.AppendLine("- `scripts/generate-personal-skills.ps1`: script para atualizar este catalogo.")
Write-Utf8NoBom -Path (Join-Path $WorkDir "README.md") -Content ($readme.ToString().TrimEnd() + "`n")

$null = Get-Content -Raw -Encoding UTF8 -Path (Join-Path $WorkDir "data\skills.json") | ConvertFrom-Json

if (-not $SkipValidation) {
  $validator = Join-Path $PersonalSkillsRoot ".system\skill-creator\scripts\quick_validate.py"
  if (Test-Path $validator) {
    foreach ($dir in $skillDirs) {
      Invoke-Checked -FilePath "python" -Arguments @($validator, $dir.FullName) -WorkingDirectory $WorkDir
    }
  }
  else {
    Write-Host "Validator not found, skipping quick_validate.py: $validator"
  }
}

Invoke-Checked -FilePath "git" -Arguments @("diff", "--check") -WorkingDirectory $WorkDir

$status = @(Get-GitOutput -Arguments @("status", "--short") -WorkingDirectory $WorkDir)
$diffStat = @(Get-GitOutput -Arguments @("diff", "--stat") -WorkingDirectory $WorkDir)

Write-Host "Local skills found: $($localNames -join ', ')"
if ($staleRemote.Count -gt 0) {
  Write-Host "Stale remote skills: $($staleRemote -join ', ')"
}
Write-Host "Catalog checkout: $WorkDir"
Write-Host "Branch: $Branch"
Write-Host "Status:"
if ($status.Count -gt 0) {
  $status | ForEach-Object { Write-Host $_ }
}
else {
  Write-Host "  clean"
}
Write-Host "Diff stat:"
if ($diffStat.Count -gt 0) {
  $diffStat | ForEach-Object { Write-Host $_ }
}
else {
  Write-Host "  no changes"
}

if ($status.Count -eq 0) {
  Write-Host "No changes to publish."
  exit 0
}

if ($Publish) {
  Invoke-Checked -FilePath "git" -Arguments @("add", "README.md", "docs/skills.md", "data/skills.json", "data/skills.csv", "skills") -WorkingDirectory $WorkDir
  Invoke-Checked -FilePath "git" -Arguments @("commit", "-m", $CommitMessage) -WorkingDirectory $WorkDir
  Invoke-Checked -FilePath "git" -Arguments @("push", "origin", $Branch) -WorkingDirectory $WorkDir
  $commit = Get-GitOutput -Arguments @("log", "-1", "--oneline") -WorkingDirectory $WorkDir
  Write-Host "Published: $commit"
}
else {
  Write-Host "Prepared local catalog changes only. Re-run with -Publish after reviewing the diff."
}
