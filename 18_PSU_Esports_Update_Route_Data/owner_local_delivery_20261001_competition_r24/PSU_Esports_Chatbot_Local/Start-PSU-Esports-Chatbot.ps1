param(
    [int]$Port = 8090,
    [switch]$OpenBrowser
)

$ErrorActionPreference = "Stop"
$projectRoot = $PSScriptRoot
Set-Location -LiteralPath $projectRoot

if ($Port -lt 1024 -or $Port -gt 65535) {
    throw "Port must be between 1024 and 65535."
}

$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
    $codexPython = Join-Path $env:USERPROFILE ".cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
    if (Test-Path -LiteralPath $codexPython) {
        $python = [pscustomobject]@{ Source = $codexPython }
    }
}
if (-not $python) {
    throw "Python was not found. Install Python 3.11 or newer, then run this file again."
}

try {
    $models = (Invoke-RestMethod -Uri "http://127.0.0.1:11434/api/tags" -TimeoutSec 3).models.name
} catch {
    throw "Ollama API is not running at 127.0.0.1:11434. Open Ollama first, then start the chatbot again."
}

$requiredModels = @("scb10x/typhoon2.5-qwen3-4b", "psu-bge-m3:q8_0")
# Ollama reports a default tag as `:latest`; the runtime is allowed to use
# either the explicit name or that equivalent default-tag form.
$installedModelBases = @($models | ForEach-Object { ([string]$_) -replace ':latest$', '' })
$missingModels = @($requiredModels | Where-Object { $_ -notin $installedModelBases })
if ($missingModels.Count -gt 0) {
    throw "Missing local model(s): $($missingModels -join ', '). Run Setup-Local-Models.cmd once while connected to the internet."
}

$env:PSU_RUNTIME_PROFILE = "owner-local-rag-assist"
$env:PSU_RUNTIME_VERSION = "2026.10.01-competition-r24"
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
$env:PSU_PIPELINE_WORKERS = "1"
$env:PSU_PIPELINE_WORKER_RECYCLE_REQUESTS = "250"
$env:PSU_PIPELINE_WORKER_WARMUP_EMBEDDING = "1"
$env:PSU_PIPELINE_WORKER_WARMUP_LLM = "1"
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

if ($OpenBrowser) {
    Start-Process $url
}

& $python.Source -m app.web_api.server --host 127.0.0.1 --port $Port

