param(
    [int]$Port = 8080,
    [string]$HostAddress = "127.0.0.1",
    [switch]$EnableSemanticRag,
    [switch]$PreviewEnglishDrafts
)

$ErrorActionPreference = "Stop"
Set-Location -LiteralPath $PSScriptRoot

if ($Port -lt 1024 -or $Port -gt 65535) {
    throw "Port must be between 1024 and 65535."
}

# This is the single local web profile. Later phases may turn on RAG through
# -EnableSemanticRag, but its state is always visible in the chat UI and /health.
$profileBase = if ($EnableSemanticRag) { "local-web-rag-assist" } else { "local-web-assist" }
$env:PSU_RUNTIME_PROFILE = $(if ($PreviewEnglishDrafts) { "$profileBase-draft-preview" } else { $profileBase })
$env:PSU_RUNTIME_VERSION = "2026.09.15-reliability-and-control-coverage"
$env:PSU_BILINGUAL_EN_ENABLED = "1"
$env:PSU_LOCAL_LLM_ASSIST_ENABLED = "1"
$env:PSU_PRODUCT_BACKEND_TIMEOUT_SEC = "20"
$env:PSU_PIPELINE_GLOBAL_TIMEOUT_SEC = "19"
$env:PSU_INTENT_LLM_TIMEOUT_SEC = "14"
$env:PSU_INTENT_LLM_NUM_PREDICT = "18"
$env:PSU_INTENT_LLM_NUM_CTX = "1536"
$env:PSU_OLLAMA_KEEP_ALIVE = "30m"
$env:PSU_EMBEDDING_KEEP_ALIVE = "30m"
$env:PSU_PIPELINE_WARMUP_EMBEDDING = "1"
$env:PSU_QUERY_PLANNER_TIMEOUT_SEC = "4"
$env:PSU_GENERAL_LLM_TIMEOUT_SEC = "8"
$env:PSU_EXPERIMENTAL_LLM_TIMEOUT_SEC = "6"
# This local evaluation profile gives the model more opportunity to resolve
# natural wording. It still selects a bounded intent only; verified tools/RAG
# remain the only fact-producing paths.
$env:PSU_MODEL_FIRST_PREFLIGHT_CONFIDENCE = "0.99"
$env:PSU_INTENT_LLM_FIRST_ONLY_WEAK = "0"
$env:PSU_INTENT_STRONG_ROUTE_SKIP_LLM_CONFIDENCE = "0.99"
$env:PSU_INTENT_STRONG_HEURISTIC_SKIP_LLM_CONFIDENCE = "0.99"
$env:PSU_PIPELINE_WARMUP = "1"
$env:PSU_LLM_PREFLIGHT = "1"
# Keep the web process responsive when an LLM, embedding, or native call does
# not return. One worker is deliberate for the local GPU profile; concurrency
# is handled by admission/fallback rather than competing model workers.
$env:PSU_PIPELINE_WORKER_SUPERVISOR = "1"
$env:PSU_PIPELINE_WORKERS = "1"
$env:PSU_PIPELINE_WORKER_RECYCLE_REQUESTS = "250"
$env:PSU_PIPELINE_WORKER_WARMUP_EMBEDDING = "1"
$env:PSU_PIPELINE_WORKER_WARMUP_LLM = "1"
$env:PSU_PIPELINE_WORKER_STARTUP_TIMEOUT_SEC = "45"
$env:PSU_PIPELINE_WORKER_QUEUE_WAIT_SEC = "3.0"
$env:PSU_INPUT_QUALITY_GUARD_MODE = "enforce"
$env:PSU_INPUT_QUALITY_REPEAT_POLICY = "warn_and_continue"
$env:PSU_SEMANTIC_RETRIEVAL = $(if ($EnableSemanticRag) { "1" } else { "0" })
$env:PSU_MODEL_FIRST_FLOW = $(if ($EnableSemanticRag) { "1" } else { "0" })
$env:PSU_RAG_LLM_COMPOSER = $(if ($EnableSemanticRag) { "1" } else { "0" })
# This is deliberately opt-in for local review only. Draft text is never used
# by the standard local profile or a production deployment.
$env:PSU_ENGLISH_LOCALIZATION_DRAFT_PREVIEW = $(if ($PreviewEnglishDrafts) { "1" } else { "0" })
$env:PSU_ENGLISH_LOCALIZATION_DRAFT_PREVIEW_PATH = $(if ($PreviewEnglishDrafts) { Join-Path $PSScriptRoot "data\locales\en\localization_review_drafts_machine_20260915_audited.jsonl" } else { "" })

$bookingDashboardRoot = Join-Path $PSScriptRoot "booking_dashboard"
$bookingDashboardUrl = "http://127.0.0.1:8091/api/chatbot-status"
function Test-BookingDashboard {
    try {
        (Invoke-WebRequest -UseBasicParsing -Uri "http://127.0.0.1:8091/" -TimeoutSec 2).StatusCode -eq 200
    } catch {
        $false
    }
}

if ((Test-Path $bookingDashboardRoot) -and -not (Test-BookingDashboard)) {
    $bookingLogDir = Join-Path $PSScriptRoot "data\logs"
    New-Item -ItemType Directory -Force -Path $bookingLogDir | Out-Null
    Start-Process -FilePath $python.Source -ArgumentList @("server.py", "--no-browser", "--port", "8091") `
        -WorkingDirectory $bookingDashboardRoot -WindowStyle Hidden `
        -RedirectStandardOutput (Join-Path $bookingLogDir "booking_dashboard_8091.out.log") `
        -RedirectStandardError (Join-Path $bookingLogDir "booking_dashboard_8091.err.log")
    for ($attempt = 1; $attempt -le 10 -and -not (Test-BookingDashboard); $attempt++) {
        Start-Sleep -Milliseconds 500
    }
}

$env:PSU_LIVE_BOOKING_ENABLED = $(if (Test-BookingDashboard) { "1" } else { "0" })
$env:PSU_LIVE_BOOKING_STATUS_URL = $bookingDashboardUrl
$env:PSU_LIVE_BOOKING_TIMEOUT_SEC = "5"
$env:PSU_LIVE_BOOKING_CACHE_SEC = "10"

Write-Host "PSU Esports Chatbot profile: $env:PSU_RUNTIME_PROFILE"
Write-Host $(if ($env:PSU_LIVE_BOOKING_ENABLED -eq "1") { "Live booking status: ready (Dashboard on port 8091)" } else { "Live booking status: unavailable; static schedule remains available" })
if ($PreviewEnglishDrafts) {
    Write-Host "English Draft Preview is ON (local review only; not an approved release)."
}
Write-Host "Open: http://$HostAddress`:$Port/"
py -m app.web_api.server --host $HostAddress --port $Port
