$ErrorActionPreference = "Stop"

$RepoRoot = Split-Path -Parent $PSScriptRoot
$CodexHome = Join-Path $env:USERPROFILE ".codex"
$PersonalSkillsRoot = Join-Path $CodexHome "skills"
$SystemSkillsRoot = (Join-Path $PersonalSkillsRoot ".system").TrimEnd("\")
$GeneratedAt = "2026-05-04"
$TimeZone = "America/Sao_Paulo"

function Assert-InRepo {
  param([string]$Path)

  $resolvedRepo = [IO.Path]::GetFullPath($RepoRoot).TrimEnd("\")
  $resolvedPath = [IO.Path]::GetFullPath($Path).TrimEnd("\")
  if (-not $resolvedPath.StartsWith($resolvedRepo, [StringComparison]::OrdinalIgnoreCase)) {
    throw "Refusing to touch path outside repository: $resolvedPath"
  }
}

function Reset-GeneratedPath {
  param([string]$RelativePath)

  $target = Join-Path $RepoRoot $RelativePath
  Assert-InRepo $target
  if (Test-Path $target) {
    Remove-Item -LiteralPath $target -Recurse -Force
  }
  New-Item -ItemType Directory -Path $target | Out-Null
}

function Write-Utf8NoBom {
  param(
    [string]$Path,
    [string]$Content
  )

  Assert-InRepo $Path
  $directory = Split-Path -Parent $Path
  if (-not (Test-Path $directory)) {
    New-Item -ItemType Directory -Path $directory | Out-Null
  }

  $encoding = New-Object System.Text.UTF8Encoding($false)
  [IO.File]::WriteAllText($Path, $Content, $encoding)
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

if (-not (Test-Path $PersonalSkillsRoot)) {
  throw "Personal skills root not found: $PersonalSkillsRoot"
}

Reset-GeneratedPath "data"
Reset-GeneratedPath "docs"
Reset-GeneratedPath "skills"

$skillFiles = Get-ChildItem -Path $PersonalSkillsRoot -Recurse -Force -Filter "SKILL.md" -File |
  Where-Object { -not $_.FullName.StartsWith($SystemSkillsRoot, [StringComparison]::OrdinalIgnoreCase) } |
  Sort-Object FullName

$skills = New-Object System.Collections.Generic.List[object]

foreach ($file in $skillFiles) {
  $content = Get-Content -Raw -Encoding UTF8 -Path $file.FullName
  $name = Read-FrontmatterField -Content $content -Field "name"
  if (-not $name) {
    $name = $file.Directory.Name
  }

  $description = Read-FrontmatterField -Content $content -Field "description"
  $repoPath = "skills/$name/SKILL.md"
  $sourcePath = ('$CODEX_HOME/skills/' + $name + '/SKILL.md')

  Write-Utf8NoBom -Path (Join-Path $RepoRoot $repoPath) -Content $content

  $skills.Add([pscustomobject][ordered]@{
    name = $name
    description = $description
    source_path = $sourcePath
    repository_path = $repoPath
    sha256 = Get-Sha256 $content
    content = $content
  }) | Out-Null
}

$skills = $skills | Sort-Object name
$total = @($skills).Count

$metadataSkills = $skills | ForEach-Object {
  [pscustomobject][ordered]@{
    name = $_.name
    description = $_.description
    source_path = $_.source_path
    repository_path = $_.repository_path
    sha256 = $_.sha256
  }
}

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
Write-Utf8NoBom -Path (Join-Path $RepoRoot "data/skills.json") -Content ($json + "`n")

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
Write-Utf8NoBom -Path (Join-Path $RepoRoot "data/skills.csv") -Content (($csvLines -join "`n") + "`n")

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
Write-Utf8NoBom -Path (Join-Path $RepoRoot "docs/skills.md") -Content ($docs.ToString() + "`n")

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
[void]$readme.AppendLine("- ``skills/<nome>/SKILL.md``: conteudo completo de cada skill pessoal.")
[void]$readme.AppendLine("- ``docs/skills.md``: catalogo legivel com os conteudos completos reunidos.")
[void]$readme.AppendLine("- ``data/skills.json``: inventario estruturado com metadados e checksums.")
[void]$readme.AppendLine("- ``data/skills.csv``: exportacao tabular com metadados.")
[void]$readme.AppendLine("- ``scripts/generate-personal-skills.ps1``: script para atualizar este catalogo.")
Write-Utf8NoBom -Path (Join-Path $RepoRoot "README.md") -Content ($readme.ToString().TrimEnd() + "`n")

Write-Host "Generated $total user-created skills."
