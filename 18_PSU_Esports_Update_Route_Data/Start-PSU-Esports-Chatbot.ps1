param(
    [int]$Port = 8090,
    [switch]$OpenBrowser,
    [string]$PythonPath = ''
)

$ErrorActionPreference = "Stop"
$projectRoot = $PSScriptRoot
Set-Location -LiteralPath $projectRoot

if ($Port -lt 1024 -or $Port -gt 65535) {
    throw "Port must be between 1024 and 65535."
}

. (Join-Path $projectRoot 'Runtime-Readiness.ps1')
$python = Get-ChatbotPython $projectRoot $PythonPath
if ($OpenBrowser) {
    & (Join-Path $projectRoot 'Open-PSU-Esports-Background.ps1') -Port $Port -PythonPath $python.Path
    return
}

. (Join-Path $projectRoot 'Portable-Models.ps1')
Assert-PSUModels $projectRoot
Warm-PSUChatModel

$env:PSU_RUNTIME_PROFILE = "owner-local-rag-assist"
$manifestPath = Join-Path $projectRoot 'package_manifest.json'
$env:PSU_RUNTIME_VERSION = if (Test-Path -LiteralPath $manifestPath) {
    (Get-Content -LiteralPath $manifestPath -Raw | ConvertFrom-Json).runtime_version
} else { "2026.10.06-targeted-flow-r40.3" }
if (-not $env:PSU_RUNTIME_VERSION) { throw 'Missing runtime_version in package_manifest.json.' }
$env:PSU_BILINGUAL_EN_ENABLED = "1"
$env:PSU_LOCAL_LLM_ASSIST_ENABLED = "1"
$env:PSU_PRODUCT_BACKEND_TIMEOUT_SEC = "20"
$env:PSU_PIPELINE_GLOBAL_TIMEOUT_SEC = "19"
$env:PSU_INTENT_LLM_TIMEOUT_SEC = "14"
$env:PSU_INTENT_LLM_NUM_PREDICT = "18"
$env:PSU_INTENT_LLM_NUM_CTX = "1536"
$env:PSU_OLLAMA_KEEP_ALIVE = "30m"
$env:PSU_EMBEDDING_KEEP_ALIVE = "30m"
$env:PSU_PIPELINE_WARMUP = "1"
$env:PSU_PIPELINE_WARMUP_EMBEDDING = "1"
$env:PSU_LLM_PREFLIGHT = "1"
$env:PSU_PIPELINE_WORKER_SUPERVISOR = "1"
$env:PSU_CHAT_JOBS_ENABLED = "1"
$env:PSU_LLM_MAX_CONCURRENCY = "1"
$env:PSU_PIPELINE_WORKERS = "2"
$env:PSU_PIPELINE_WORKER_RECYCLE_REQUESTS = "250"
$env:PSU_PIPELINE_WORKER_WARMUP_EMBEDDING = "1"
$env:PSU_PIPELINE_WORKER_WARMUP_LLM = "0"
$env:PSU_PIPELINE_WORKER_STARTUP_TIMEOUT_SEC = "45"
$env:PSU_PIPELINE_WORKER_QUEUE_WAIT_SEC = "3.0"
$env:PSU_INPUT_QUALITY_GUARD_MODE = "enforce"
$env:PSU_INPUT_QUALITY_REPEAT_POLICY = "warn_and_continue"
$env:PSU_SEMANTIC_RETRIEVAL = "1"
$env:PSU_MODEL_FIRST_FLOW = "1"
$env:PSU_RAG_LLM_COMPOSER = "1"
$env:PSU_MODEL_FIRST_PREFLIGHT_CONFIDENCE = "0.99"
$env:PSU_INTENT_LLM_FIRST_ONLY_WEAK = "0"
$env:PSU_INTENT_STRONG_ROUTE_SKIP_LLM_CONFIDENCE = "0.99"
$env:PSU_INTENT_STRONG_HEURISTIC_SKIP_LLM_CONFIDENCE = "0.99"
$env:PSU_CHAT_LOG_LOCAL_JSONL = "1"
$env:PSU_CHAT_LOG_SQLITE = "1"
$env:PSU_CHAT_LOG_DIR = Join-Path $projectRoot "data\logs"
$env:PSU_CHAT_LOG_SQLITE_PATH = Join-Path $projectRoot "data\logs\chat_history.sqlite3"

$bookingDashboardRoot = Join-Path $projectRoot "booking_dashboard"
. (Join-Path $projectRoot "Booking-Dashboard-Probe.ps1")

function Test-LocalPortInUse([int]$ListenPort) {
    $client = [System.Net.Sockets.TcpClient]::new()
    try {
        $client.Connect("127.0.0.1", $ListenPort)
        return $true
    } catch {
        return $false
    } finally {
        $client.Dispose()
    }
}

if (Test-LocalPortInUse $Port) {
    throw "Chatbot port $Port is already in use. Close the existing Chatbot or choose another port with -Port."
}

$ownerDashboardAt8080 = $Port -ne 8080 -and (Test-BookingDashboardIdentity -BaseUrl "http://127.0.0.1:8080")
# The standalone Chatbot fetches the WordPress exports on demand. An
# already-running owner Dashboard remains authoritative for its own calendar.
$env:PSU_LIVE_BOOKING_FETCH_MODE = if ($ownerDashboardAt8080) { "dashboard" } else { "wordpress" }
$env:PSU_LIVE_BOOKING_ENABLED = "1"
$env:PSU_LIVE_BOOKING_STATUS_URL = if ($ownerDashboardAt8080) { "http://127.0.0.1:8080/api/chatbot-status" } else { "http://127.0.0.1:8091/api/chatbot-status" }
$env:PSU_LIVE_BOOKING_TIMEOUT_SEC = "5"
$env:PSU_LIVE_BOOKING_CACHE_SEC = "0"

$url = "http://127.0.0.1:$Port/"
Write-Host "Starting PSU Esports Chatbot"
Write-Host $(if ($ownerDashboardAt8080) { "Booking: read owner Dashboard at port 8080 on each status question" } else { "Booking: fetch WordPress directly on each status question; no separate Dashboard process required" })
Write-Host "Open: $url"
Write-Host "Keep this window open while the chatbot is in use."

& $python.Path -m app.web_api.server --host 127.0.0.1 --port $Port

