param(
    [string]$OutputRoot = "owner_local_package",
    [string]$RuntimeVersion = "2026.10.10-common-r58.2",
    [string]$PythonRuntimeRoot = "",
    [switch]$CreateZip
)

$ErrorActionPreference = "Stop"
$projectRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$outputRootPath = if ([System.IO.Path]::IsPathRooted($OutputRoot)) { $OutputRoot } else { Join-Path $projectRoot $OutputRoot }
$packageName = "PSU_Esports_Chatbot_Local"
$packageRoot = Join-Path $outputRootPath $packageName
$templateRoot = Join-Path $projectRoot "deployment_templates"

if (Test-Path $packageRoot) {
    throw "Package folder already exists: $packageRoot. Choose a new -OutputRoot or remove that package folder first."
}

function Copy-RuntimeTree {
    param([Parameter(Mandatory = $true)][string]$RelativePath)

    $source = Join-Path $projectRoot $RelativePath
    $destination = Join-Path $packageRoot $RelativePath
    if (-not (Test-Path $source)) {
        throw "Missing runtime path: $source"
    }

    New-Item -ItemType Directory -Force -Path $destination | Out-Null
    & robocopy $source $destination /E /XD __pycache__ /XF *.pyc | Out-Null
    if ($LASTEXITCODE -gt 7) {
        throw "Copy failed for $RelativePath (robocopy exit code $LASTEXITCODE)."
    }
}

New-Item -ItemType Directory -Force -Path $packageRoot | Out-Null

Copy-RuntimeTree "app"
Copy-RuntimeTree "web_chat"
Copy-RuntimeTree "booking_dashboard"

# Common-content packages include a pinned CPython 3.12 x64 runtime.
if (-not $PythonRuntimeRoot) { $PythonRuntimeRoot = Join-Path $projectRoot "runtime\python" }
$runtimePython = Join-Path $PythonRuntimeRoot "python.exe"
if (-not (Test-Path -LiteralPath $runtimePython -PathType Leaf)) { throw "Pass -PythonRuntimeRoot with a verified Python 3.12 x64 runtime directory." }
$identity = & $runtimePython -B -c "import sys,struct; print(str(sys.version_info.major)+'.'+str(sys.version_info.minor)+':'+str(struct.calcsize('P')*8))"
if ($LASTEXITCODE -ne 0 -or $identity -ne '3.12:64') { throw 'Common-content runtime must be Python 3.12 x64.' }
$runtimeTarget = Join-Path $packageRoot "runtime\python"
New-Item -ItemType Directory -Force -Path $runtimeTarget | Out-Null
& robocopy $PythonRuntimeRoot $runtimeTarget /E /XD __pycache__ /XF *.pyc | Out-Null
if ($LASTEXITCODE -gt 7) { throw 'Bundled Python copy failed.' }
$knowledgePath = Join-Path $projectRoot "data\knowledge\approved.sqlite"
if (Test-Path -LiteralPath $knowledgePath) {
    $knowledgeTarget = Join-Path $packageRoot "data\knowledge\approved.sqlite"
    New-Item -ItemType Directory -Force -Path (Split-Path -Parent $knowledgeTarget) | Out-Null
    # backup() includes committed WAL data; capability/session files are excluded.
    $backupCode = "import sqlite3,sys; a=sqlite3.connect(sys.argv[1]); demo=a.execute('SELECT value FROM cc_meta WHERE key=?',('demo',)).fetchone(); assert demo and demo[0]=='0','Only production knowledge databases may be packaged'; b=sqlite3.connect(sys.argv[2]); a.backup(b); b.close(); a.close()"
    & $runtimePython -B -c $backupCode $knowledgePath $knowledgeTarget
    if ($LASTEXITCODE -ne 0) { throw 'Knowledge database backup failed.' }
}
$ownerDocsSource = Join-Path $projectRoot "docs\common_content_r58"
$ownerDocsTarget = Join-Path $packageRoot "owner_content_docs"
New-Item -ItemType Directory -Force -Path $ownerDocsTarget | Out-Null
& robocopy $ownerDocsSource $ownerDocsTarget /E | Out-Null
if ($LASTEXITCODE -gt 7) { throw 'Owner docs copy failed.' }

# Runtime data only. Test corpora, human-review samples, reports and debug logs
# deliberately stay out of the owner package.
$runtimeDataDirectories = @(
    "calendar",
    "competition_rules",
    "content",
    "control_game",
    "control_game_split",
    "curated",
    "intent",
    "knowledge_inbox",
    "locales",
    "manifests",
    "routing",
    "rules",
    "sources",
    "style",
    "vector"
)
foreach ($directory in $runtimeDataDirectories) {
    Copy-RuntimeTree (Join-Path "data" $directory)
}

New-Item -ItemType Directory -Force -Path (Join-Path $packageRoot "data\logs") | Out-Null
New-Item -ItemType File -Force -Path (Join-Path $packageRoot "data\logs\.gitkeep") | Out-Null
New-Item -ItemType Directory -Force -Path (Join-Path $packageRoot "models") | Out-Null
Copy-Item -LiteralPath (Join-Path $projectRoot "models\Modelfile.bge-m3-1024") -Destination (Join-Path $packageRoot "models\Modelfile.bge-m3-1024")

foreach ($template in @(
    "Runtime-Readiness.ps1",
    "OWNER_CONTENT_GUIDE_TH.md",
    "Open-Owner-Content.ps1",
    "Open-Owner-Content.cmd",
    "Stop-Owner-Content.ps1",
    "Stop-Owner-Content.cmd",
    "README_TH.md",
    "LOCAL_OPERATION_AND_DATA_POLICY_TH.md",
    "OWNER_HANDOFF_AND_SCOPE_TH.md",
    "SYSTEM_REQUIREMENTS_FROM_CODEX_TH.md",
    "Start-PSU-Esports-Chatbot.ps1",
    "Booking-Dashboard-Probe.ps1",
    "Start-PSU-Esports-Chatbot.cmd",
    "Open-PSU-Esports-Chatbot.ps1",
    "Open-PSU-Esports-Chatbot.cmd",
    "Open-PSU-Esports-Background.ps1",
    "Open-PSU-Esports-Background.cmd",
    "Setup-Local-Models.ps1",
    "Setup-Local-Models.cmd",
    "View-Chat-Logs.ps1",
    "View-Chat-Logs.cmd"
)) {
    $source = Join-Path $templateRoot $template
    if (-not (Test-Path $source)) {
        throw "Missing deployment template: $source"
    }
    Copy-Item -LiteralPath $source -Destination (Join-Path $packageRoot $template)
}

# Start launcher reads runtime_version from package_manifest.json.

New-Item -ItemType Directory -Force -Path (Join-Path $packageRoot "tools") | Out-Null
Copy-Item -LiteralPath (Join-Path $projectRoot "tools\export_local_chat_logs.py") -Destination (Join-Path $packageRoot "tools\export_local_chat_logs.py")

@{
    python_runtime = @{path="runtime/python/python.exe";scope="bundled-windows-x64";required="3.12"}
    common_content = @{version="studio-content-3.0";kinds=24;fields=155;database="data/knowledge/approved.sqlite"}
    package_name = $packageName
    built_at = (Get-Date).ToUniversalTime().ToString("o")
    runtime_version = $RuntimeVersion
    included_data_directories = $runtimeDataDirectories
    local_runtime_features = @("per_page_anonymous_sessions", "sqlite_transcript", "append_only_daily_jsonl_log", "owner_html_log_report", "loopback_only_server", "live_booking_status_aggregate_only", "bounded_intent_cue_recovery", "typed_price_conversation", "external_group_scoped_prices", "idempotent_client_turns", "acknowledged_full_rulebook_sections")
    excluded = @("reports", "tests", "tools except export_local_chat_logs.py", "notebooks", "data/eval", "data/ground_truth", "data/human_review", "data/logs", "Ollama model weights")
    required_local_models = @("scb10x/typhoon2.5-qwen3-4b", "psu-bge-m3:q8_0")
} | ConvertTo-Json -Depth 4 | Set-Content -LiteralPath (Join-Path $packageRoot "package_manifest.json") -Encoding UTF8

if ($CreateZip) {
    $zipPath = Join-Path $outputRootPath ($packageName + ".zip")
    Compress-Archive -LiteralPath $packageRoot -DestinationPath $zipPath -CompressionLevel Optimal
    Write-Host "Created zip: $zipPath"
}

Write-Host "Owner package created: $packageRoot"
