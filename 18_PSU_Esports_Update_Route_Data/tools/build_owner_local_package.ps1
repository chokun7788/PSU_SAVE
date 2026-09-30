param(
    [string]$OutputRoot = "owner_local_package",
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

New-Item -ItemType Directory -Force -Path (Join-Path $packageRoot "tools") | Out-Null
Copy-Item -LiteralPath (Join-Path $projectRoot "tools\export_local_chat_logs.py") -Destination (Join-Path $packageRoot "tools\export_local_chat_logs.py")

@{
    package_name = $packageName
    built_at = (Get-Date).ToUniversalTime().ToString("o")
    runtime_version = "2026.09.29-multi-error-recovery-r15"
    included_data_directories = $runtimeDataDirectories
    local_runtime_features = @("per_page_anonymous_sessions", "sqlite_transcript", "append_only_daily_jsonl_log", "owner_html_log_report", "loopback_only_server", "live_booking_status_aggregate_only")
    excluded = @("reports", "tests", "tools except export_local_chat_logs.py", "notebooks", "data/eval", "data/ground_truth", "data/human_review", "data/logs", "Ollama model weights")
    required_local_models = @("scb10x/typhoon2.5-qwen3-4b", "psu-bge-m3:q8_0")
} | ConvertTo-Json -Depth 4 | Set-Content -LiteralPath (Join-Path $packageRoot "package_manifest.json") -Encoding UTF8

if ($CreateZip) {
    $zipPath = Join-Path $outputRootPath ($packageName + ".zip")
    Compress-Archive -LiteralPath $packageRoot -DestinationPath $zipPath -CompressionLevel Optimal
    Write-Host "Created zip: $zipPath"
}

Write-Host "Owner package created: $packageRoot"
