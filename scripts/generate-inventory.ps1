$ErrorActionPreference = "Stop"

$RepoRoot = Split-Path -Parent $PSScriptRoot
$CodexHome = Join-Path $env:USERPROFILE ".codex"
$GeneratedAt = "2026-05-04"
$TimeZone = "America/Sao_Paulo"

$SessionAvailableSkillIds = @(
  "imagegen",
  "openai-docs",
  "plugin-creator",
  "skill-creator",
  "skill-installer",
  "browser-use:browser",
  "company-jobs",
  "curadoria-eventos",
  "figma:figma-code-connect",
  "figma:figma-create-design-system-rules",
  "figma:figma-generate-design",
  "figma:figma-generate-library",
  "figma:figma-implement-design",
  "figma:figma-use",
  "gemini-interview-prep-prompt",
  "github:gh-address-comments",
  "github:gh-fix-ci",
  "github:github",
  "github:yeet",
  "job-fit-evaluator",
  "pessoa-due-diligence",
  "prd-to-codex-prompt",
  "tailor-cv-to-job",
  "vercel:agent-browser",
  "vercel:agent-browser-verify",
  "vercel:ai-elements",
  "vercel:ai-gateway",
  "vercel:ai-generation-persistence",
  "vercel:ai-sdk",
  "vercel:auth",
  "vercel:bootstrap",
  "vercel:chat-sdk",
  "vercel:cms",
  "vercel:cron-jobs",
  "vercel:deployments-cicd",
  "vercel:email",
  "vercel:env-vars",
  "vercel:geist",
  "vercel:geistdocs",
  "vercel:investigation-mode",
  "vercel:json-render",
  "vercel:marketplace",
  "vercel:micro",
  "vercel:ncc",
  "vercel:next-forge",
  "vercel:nextjs",
  "vercel:observability",
  "vercel:payments",
  "vercel:react-best-practices",
  "vercel:routing-middleware",
  "vercel:runtime-cache",
  "vercel:satori",
  "vercel:shadcn",
  "vercel:sign-in-with-vercel",
  "vercel:swr",
  "vercel:turbopack",
  "vercel:turborepo",
  "vercel:v0-dev",
  "vercel:vercel-agent",
  "vercel:vercel-api",
  "vercel:vercel-cli",
  "vercel:vercel-firewall",
  "vercel:vercel-flags",
  "vercel:vercel-functions",
  "vercel:vercel-queues",
  "vercel:vercel-sandbox",
  "vercel:vercel-services",
  "vercel:vercel-storage",
  "vercel:verification",
  "vercel:workflow"
)

$SkillRoots = @(
  [pscustomobject]@{
    Alias = "r1"
    Label = "System"
    Group = "system"
    Plugin = $null
    Prefix = $null
    Root = Join-Path $CodexHome "skills\.system"
  },
  [pscustomobject]@{
    Alias = "r0"
    Label = "Personal"
    Group = "personal"
    Plugin = $null
    Prefix = $null
    Root = Join-Path $CodexHome "skills"
  },
  [pscustomobject]@{
    Alias = "r2"
    Label = "Browser Use"
    Group = "plugin"
    Plugin = "browser-use"
    Prefix = "browser-use"
    Root = Join-Path $CodexHome "plugins\cache\openai-bundled"
  },
  [pscustomobject]@{
    Alias = "r3"
    Label = "Figma"
    Group = "plugin"
    Plugin = "figma"
    Prefix = "figma"
    Root = Join-Path $CodexHome "plugins\cache\openai-curated\figma\f951c6ef\skills"
  },
  [pscustomobject]@{
    Alias = "r4"
    Label = "GitHub"
    Group = "plugin"
    Plugin = "github"
    Prefix = "github"
    Root = Join-Path $CodexHome "plugins\cache\openai-curated\github\f951c6ef\skills"
  },
  [pscustomobject]@{
    Alias = "r6"
    Label = "Gmail"
    Group = "plugin"
    Plugin = "gmail"
    Prefix = "gmail"
    Root = Join-Path $CodexHome "plugins\cache\openai-curated\gmail\f951c6ef\skills"
  },
  [pscustomobject]@{
    Alias = "r5"
    Label = "Vercel"
    Group = "plugin"
    Plugin = "vercel"
    Prefix = "vercel"
    Root = Join-Path $CodexHome "plugins\cache\openai-curated\vercel\f951c6ef\skills"
  }
)

function ConvertTo-PlainAscii {
  param([string]$Value)

  if ($null -eq $Value) {
    return ""
  }

  $text = $Value.Trim()
  $text = $text -replace [string][char]0x2018, "'"
  $text = $text -replace [string][char]0x2019, "'"
  $text = $text -replace [string][char]0x201C, '"'
  $text = $text -replace [string][char]0x201D, '"'
  $text = $text -replace [string][char]0x2013, "-"
  $text = $text -replace [string][char]0x2014, "-"
  $text = $text -replace [string][char]0x2192, "->"
  $text = $text -replace [string][char]0x00D7, "x"

  $normalized = $text.Normalize([Text.NormalizationForm]::FormD)
  $builder = New-Object System.Text.StringBuilder
  foreach ($char in $normalized.ToCharArray()) {
    $category = [Globalization.CharUnicodeInfo]::GetUnicodeCategory($char)
    if ($category -eq [Globalization.UnicodeCategory]::NonSpacingMark) {
      continue
    }
    if ([int][char]$char -le 127) {
      [void]$builder.Append($char)
    } else {
      [void]$builder.Append("?")
    }
  }

  return (($builder.ToString() -replace "\s+", " ").Trim())
}

function Read-FrontmatterField {
  param(
    [string]$Content,
    [string]$Field
  )

  $frontmatter = $Content
  $match = [regex]::Match($Content, "(?ms)^---\s*(.*?)\s*---")
  if ($match.Success) {
    $frontmatter = $match.Groups[1].Value
  }

  $line = ($frontmatter -split "`r?`n" | Where-Object { $_ -match "^\s*$Field\s*:" } | Select-Object -First 1)
  if (-not $line) {
    return ""
  }

  $value = $line -replace "^\s*$Field\s*:\s*", ""
  $value = $value.Trim()
  if (($value.StartsWith('"') -and $value.EndsWith('"')) -or ($value.StartsWith("'") -and $value.EndsWith("'"))) {
    $value = $value.Substring(1, $value.Length - 2)
  }

  return ConvertTo-PlainAscii $value
}

function Get-ShortPath {
  param(
    [string]$FullPath,
    [object]$RootInfo
  )

  $root = $RootInfo.Root.TrimEnd("\")
  $relative = $FullPath.Substring($root.Length).TrimStart("\")
  return "$($RootInfo.Alias)/$($relative -replace "\\", "/")"
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

function Write-Utf8NoBom {
  param(
    [string]$Path,
    [string]$Content
  )

  $directory = Split-Path -Parent $Path
  if (-not (Test-Path $directory)) {
    New-Item -ItemType Directory -Path $directory | Out-Null
  }

  $encoding = New-Object System.Text.UTF8Encoding($false)
  [IO.File]::WriteAllText($Path, $Content, $encoding)
}

$systemRoot = (Join-Path $CodexHome "skills\.system").TrimEnd("\")
$skills = New-Object System.Collections.Generic.List[object]

foreach ($rootInfo in $SkillRoots) {
  if (-not (Test-Path $rootInfo.Root)) {
    continue
  }

  $files = Get-ChildItem -Path $rootInfo.Root -Recurse -Force -Filter "SKILL.md" -File
  foreach ($file in $files) {
    $fullPath = $file.FullName
    if ($rootInfo.Alias -eq "r0" -and $fullPath.StartsWith($systemRoot, [StringComparison]::OrdinalIgnoreCase)) {
      continue
    }

    $content = Get-Content -Raw -Encoding UTF8 -Path $fullPath
    $name = Read-FrontmatterField -Content $content -Field "name"
    if (-not $name) {
      $name = ConvertTo-PlainAscii $file.Directory.Name
    }

    $description = Read-FrontmatterField -Content $content -Field "description"
    $skillId = $name
    if ($rootInfo.Prefix) {
      $skillId = "$($rootInfo.Prefix):$name"
    }

    $status = "present_on_disk_only"
    if ($SessionAvailableSkillIds -contains $skillId) {
      $status = "available_in_session"
    }

    $skills.Add([pscustomobject][ordered]@{
      id = $skillId
      name = $name
      description = $description
      group = $rootInfo.Group
      source = $rootInfo.Label
      plugin = $rootInfo.Plugin
      status = $status
      path = Get-ShortPath -FullPath $fullPath -RootInfo $rootInfo
    }) | Out-Null
  }
}

$skills = $skills | Sort-Object source, id
$totalDiscovered = @($skills).Count
$totalAvailable = @($skills | Where-Object { $_.status -eq "available_in_session" }).Count
$totalDiskOnly = @($skills | Where-Object { $_.status -eq "present_on_disk_only" }).Count

$rootRows = $SkillRoots | ForEach-Object {
  [pscustomobject][ordered]@{
    alias = $_.Alias
    source = $_.Label
    root = ($_.Root -replace [regex]::Escape($CodexHome), '$CODEX_HOME') -replace "\\", "/"
  }
}

$payload = [ordered]@{
  generated_at = $GeneratedAt
  timezone = $TimeZone
  note = "Inventory of local Codex SKILL.md files. It lists metadata only, not full skill instructions."
  totals = [ordered]@{
    discovered_skill_files = $totalDiscovered
    available_in_current_session = $totalAvailable
    present_on_disk_only = $totalDiskOnly
  }
  roots = $rootRows
  skills = $skills
}

$json = $payload | ConvertTo-Json -Depth 8
Write-Utf8NoBom -Path (Join-Path $RepoRoot "data\skills.json") -Content ($json + "`n")

$csvLines = New-Object System.Collections.Generic.List[string]
$csvLines.Add("id,name,source,plugin,status,path,description") | Out-Null
foreach ($skill in $skills) {
  $csvLines.Add((
    @(
      Escape-CsvCell $skill.id
      Escape-CsvCell $skill.name
      Escape-CsvCell $skill.source
      Escape-CsvCell $(if ($skill.plugin) { $skill.plugin } else { "" })
      Escape-CsvCell $skill.status
      Escape-CsvCell $skill.path
      Escape-CsvCell $skill.description
    ) -join ","
  )) | Out-Null
}
Write-Utf8NoBom -Path (Join-Path $RepoRoot "data\skills.csv") -Content (($csvLines -join "`n") + "`n")

$docs = New-Object System.Text.StringBuilder
[void]$docs.AppendLine("# Codex Skills Inventory")
[void]$docs.AppendLine("")
[void]$docs.AppendLine("Generated on $GeneratedAt ($TimeZone).")
[void]$docs.AppendLine("")
[void]$docs.AppendLine("This catalog lists metadata from local Codex ``SKILL.md`` files. It does not publish the full internal instructions of each skill.")
[void]$docs.AppendLine("")
[void]$docs.AppendLine("## Totals")
[void]$docs.AppendLine("")
[void]$docs.AppendLine("| Metric | Count |")
[void]$docs.AppendLine("| --- | ---: |")
[void]$docs.AppendLine("| Discovered ``SKILL.md`` files | $totalDiscovered |")
[void]$docs.AppendLine("| Available in the current Codex session | $totalAvailable |")
[void]$docs.AppendLine("| Present on disk only | $totalDiskOnly |")
[void]$docs.AppendLine("")
[void]$docs.AppendLine("## Root aliases")
[void]$docs.AppendLine("")
[void]$docs.AppendLine("| Alias | Source | Root |")
[void]$docs.AppendLine("| --- | --- | --- |")
foreach ($root in $rootRows) {
  $aliasCell = Escape-MarkdownCell $root.alias
  $sourceCell = Escape-MarkdownCell $root.source
  $rootCell = Escape-MarkdownCell $root.root
  [void]$docs.AppendLine("| ``$aliasCell`` | $sourceCell | ``$rootCell`` |")
}

$groupOrder = @("System", "Personal", "Browser Use", "Figma", "GitHub", "Gmail", "Vercel")
foreach ($groupName in $groupOrder) {
  $groupSkills = @($skills | Where-Object { $_.source -eq $groupName })
  if ($groupSkills.Count -eq 0) {
    continue
  }

  [void]$docs.AppendLine("")
  [void]$docs.AppendLine("## $groupName")
  [void]$docs.AppendLine("")
  [void]$docs.AppendLine("| Skill ID | Status | Path | Description |")
  [void]$docs.AppendLine("| --- | --- | --- | --- |")
  foreach ($skill in $groupSkills) {
    $idCell = Escape-MarkdownCell $skill.id
    $statusCell = Escape-MarkdownCell $skill.status
    $pathCell = Escape-MarkdownCell $skill.path
    $descriptionCell = Escape-MarkdownCell $skill.description
    [void]$docs.AppendLine("| ``$idCell`` | ``$statusCell`` | ``$pathCell`` | $descriptionCell |")
  }
}
Write-Utf8NoBom -Path (Join-Path $RepoRoot "docs\skills.md") -Content ($docs.ToString() + "`n")

$readme = @"
# Codex Skills

Inventario organizado das skills encontradas neste ambiente local do Codex.

Generated on: $GeneratedAt ($TimeZone)

## Snapshot

| Metric | Count |
| --- | ---: |
| Discovered ``SKILL.md`` files | $totalDiscovered |
| Available in the current Codex session | $totalAvailable |
| Present on disk only | $totalDiskOnly |

## Files

- ``docs/skills.md``: human-readable catalog grouped by source/plugin.
- ``data/skills.json``: machine-readable inventory with roots, counts, and skill metadata.
- ``data/skills.csv``: spreadsheet-friendly export.
- ``scripts/generate-inventory.ps1``: repeatable generator for refreshing this repo.

## Notes

- This repository lists metadata only. It intentionally does not copy full ``SKILL.md`` instruction bodies.
- ``available_in_session`` means the skill was advertised as available to Codex in the current session.
- ``present_on_disk_only`` means the ``SKILL.md`` file exists locally but was not advertised in the current session list.

"@
Write-Utf8NoBom -Path (Join-Path $RepoRoot "README.md") -Content $readme

Write-Host "Generated $totalDiscovered skills ($totalAvailable available, $totalDiskOnly disk-only)."
