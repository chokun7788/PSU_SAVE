param(
  [string]$DeployRoot = "C:\Users\Chokhun\Downloads\Learn-LLM\20_PSU_Esports_Vercel_Deploy"
)

$ErrorActionPreference = "Stop"

$SourceRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot "..")).Path
$DeployRoot = (Resolve-Path -LiteralPath $DeployRoot).Path

if (-not (Test-Path -LiteralPath (Join-Path $DeployRoot "app"))) {
  throw "DeployRoot does not look like the deploy project: $DeployRoot"
}

function Copy-RelativeFile {
  param([string]$RelativePath)
  $src = Join-Path $SourceRoot $RelativePath
  $dst = Join-Path $DeployRoot $RelativePath
  $dstDir = Split-Path -Parent $dst
  New-Item -ItemType Directory -Force -Path $dstDir | Out-Null
  Copy-Item -LiteralPath $src -Destination $dst -Force
  Write-Host "copied $RelativePath"
}

function Copy-RelativeFileAs {
  param([string]$SourceRelativePath, [string]$DeployRelativePath)
  $src = Join-Path $SourceRoot $SourceRelativePath
  $dst = Join-Path $DeployRoot $DeployRelativePath
  $dstDir = Split-Path -Parent $dst
  New-Item -ItemType Directory -Force -Path $dstDir | Out-Null
  Copy-Item -LiteralPath $src -Destination $dst -Force
  Write-Host "copied $SourceRelativePath -> $DeployRelativePath"
}

function Sync-RelativeDirectory {
  param([string]$RelativePath)
  $src = Join-Path $SourceRoot $RelativePath
  $dst = Join-Path $DeployRoot $RelativePath
  $resolvedParent = (Resolve-Path -LiteralPath (Split-Path -Parent $dst)).Path
  if (-not $resolvedParent.StartsWith($DeployRoot, [System.StringComparison]::OrdinalIgnoreCase)) {
    throw "Refusing to sync outside deploy root: $dst"
  }
  if (Test-Path -LiteralPath $dst) {
    $resolvedDst = (Resolve-Path -LiteralPath $dst).Path
    if (-not $resolvedDst.StartsWith($DeployRoot, [System.StringComparison]::OrdinalIgnoreCase)) {
      throw "Refusing to remove outside deploy root: $resolvedDst"
    }
    Remove-Item -LiteralPath $resolvedDst -Recurse -Force
  }
  New-Item -ItemType Directory -Force -Path (Split-Path -Parent $dst) | Out-Null
  Copy-Item -LiteralPath $src -Destination $dst -Recurse -Force
  Write-Host "synced $RelativePath"
}

Copy-RelativeFile "app\pipeline\vector_retrieval.py"
Copy-RelativeFile "app\pipeline\engine.py"
Copy-RelativeFile "app\pipeline\preprocess.py"
Copy-RelativeFile "app\pipeline\schemas.py"
Copy-RelativeFile "app\pipeline\formatter.py"
Copy-RelativeFile "app\core\normalization.py"
Copy-RelativeFile "app\runtime\fast_answer.py"
Copy-RelativeFile "app\web_api\server.py"
Copy-RelativeFile "app\session\__init__.py"
Copy-RelativeFile "app\session\chat_logger.py"
Copy-RelativeFile "app\session\context_resolver.py"
Copy-RelativeFile "web_chat\app.js"
Copy-RelativeFileAs "web_chat\app.js" "app.js"
Copy-RelativeFile "tools\build_game_control_facts.py"
Copy-RelativeFile "tools\audit_game_control_data.py"
Copy-RelativeFile "tools\audit_game_alias_collisions.py"
Copy-RelativeFile "tools\validate_game_controls.py"
Copy-RelativeFile "tools\summarize_chat_logs.py"
Copy-RelativeFile "tools\sync_game_controls_to_deploy.ps1"
Copy-RelativeFile "tests\smoke_test_game_controls.py"
Copy-RelativeFile "tests\smoke_test_answer_formatting.py"
Copy-RelativeFile "tests\smoke_test_genre_alias_formatting.py"
Copy-RelativeFile "tests\smoke_test_session_context.py"
Copy-RelativeFile "tests\smoke_test_game_catalog.py"
Copy-RelativeFile "tests\smoke_test_chat_logger_sqlite.py"
Copy-RelativeFile "tests\smoke_test_chat_logger_postgres.py"
Copy-RelativeFile "docs\30_neon_persistent_session_flow_20260713.md"
Copy-RelativeFile "data\curated\game_title_aliases.jsonl"
Copy-RelativeFile "data\curated\game_item_details.jsonl"
Copy-RelativeFile "data\curated\our_games_scraped_details.jsonl"
Copy-RelativeFile "data\curated\game_control_facts.jsonl"
Copy-RelativeFile "data\vector\psu_hybrid_vector_index.json"
Sync-RelativeDirectory "data\control_game_split\ps5"
Sync-RelativeDirectory "data\control_game_split\nintendo"

Write-Host "GAME CONTROL SYNC OK"
