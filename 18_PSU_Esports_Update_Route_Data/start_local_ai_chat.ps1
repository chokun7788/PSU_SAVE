param(
    [string]$Model = "scb10x/typhoon2.5-qwen3-4b",
    [double]$Timeout = 8,
    [double]$GlobalTimeout = 9,
    [int]$NumPredict = 128,
    [int]$NumCtx = 2048,
    [int]$FactsNumCtx = 3072,
    [switch]$NoLlm,
    [switch]$NoToolRouter,
    [switch]$NoComposer,
    [switch]$Composer,
    [switch]$IntentFirst,
    [switch]$NoIntentFirst,
    [string]$IntentModel = "",
    [double]$IntentTimeout = 8,
    [int]$IntentPredict = 50,
    [switch]$EntityReranker,
    [string]$EntityRerankerModel = "BAAI/bge-reranker-v2-m3",
    [string]$EntityRerankerCacheDir = "D:\AIModels\huggingface",
    [switch]$SemanticRag,
    [string]$EmbeddingModel = "psu-bge-m3:q8_0",
    [int]$EmbeddingNumCtx = 1024,
    [string]$EmbeddingKeepAlive = "10m",
    [switch]$DocumentReranker,
    [switch]$NoRagFallback,
    [switch]$Debug,
    [switch]$NoLog,
    [string]$Once = ""
)

$ErrorActionPreference = "Stop"
Set-Location -LiteralPath $PSScriptRoot

$env:PSU_CHATBOT_OLLAMA_MODEL = $Model
$env:PSU_GENERAL_LLM_TIMEOUT_SEC = [string]$Timeout
$env:PSU_PIPELINE_GLOBAL_TIMEOUT_SEC = [string]$GlobalTimeout
$env:PSU_GENERAL_LLM_NUM_PREDICT = [string]$NumPredict
$env:PSU_GENERAL_LLM_NUM_CTX = [string]$NumCtx
$env:PSU_INTENT_LLM_NUM_CTX = [string]([Math]::Min($NumCtx, 2048))
$env:PSU_TOOL_ROUTER_NUM_CTX = [string]([Math]::Min($NumCtx, 2048))
$env:PSU_QUERY_PLANNER_NUM_CTX = [string]([Math]::Min($NumCtx, 2048))
$env:PSU_FACTS_LLM_NUM_CTX = [string]$FactsNumCtx
$env:PSU_FACTS_LLM_TIMEOUT_SEC = "5.0"
$env:PSU_FACTS_LLM_NUM_PREDICT = "192"
$env:PSU_MODEL_FIRST_MIN_REMAINING_SEC = "6.0"
$env:PSU_OLLAMA_THINK = "false"
$env:PSU_LLM_TOOL_ROUTER = $(if ($NoToolRouter -or $NoLlm) { "0" } else { "1" })
$env:PSU_FACTS_LLM_COMPOSER = $(if ($Composer -and -not $NoComposer -and -not $NoLlm) { "1" } else { "0" })
$env:PSU_UNIVERSAL_INTENT_LLM = $(if ($NoLlm) { "0" } else { "1" })
$env:PSU_QUERY_PLANNER = $(if ($NoLlm) { "0" } else { "1" })
$env:PSU_QUERY_PLANNER_TIMEOUT_SEC = "8"
$env:PSU_QUERY_PLANNER_NUM_PREDICT = "128"
$env:PSU_LLM_MAX_CALLS = "2"
$env:PSU_LLM_MAX_CONCURRENCY = "1"
$env:PSU_LLM_CONCURRENCY_WAIT_SEC = "0.20"
$env:PSU_COMPOUND_MAX_WORKERS = "2"
$env:PSU_QUERY_PLANNER_ON_CLEAR_SPLIT = "0"
$env:PSU_UNIVERSAL_INTENT_LLM_FIRST = $(if ($NoIntentFirst -or $NoLlm) { "0" } else { "1" })
$env:PSU_INTENT_LLM_FIRST_ONLY_WEAK = "1"
$env:PSU_INTENT_LLM_TIMEOUT_SEC = [string]$IntentTimeout
$env:PSU_INTENT_LLM_NUM_PREDICT = [string]$IntentPredict
$env:PSU_ENTITY_RERANKER = $(if ($EntityReranker) { "1" } else { "0" })
$env:PSU_ENTITY_RERANKER_MODEL = $EntityRerankerModel
$env:PSU_ENTITY_RERANKER_CACHE_DIR = $EntityRerankerCacheDir
$env:PSU_SEMANTIC_RETRIEVAL = $(if ($SemanticRag) { "1" } else { "0" })
$env:PSU_EMBEDDING_MODEL = $EmbeddingModel
$env:PSU_EMBEDDING_NUM_CTX = [string]$EmbeddingNumCtx
$env:PSU_EMBEDDING_KEEP_ALIVE = $EmbeddingKeepAlive
$env:PSU_MODEL_FIRST_FLOW = $(if ($SemanticRag -and -not $NoLlm) { "1" } else { "0" })
$env:PSU_RAG_LLM_COMPOSER = $(if ($SemanticRag -and -not $NoLlm) { "1" } else { "0" })
$env:PSU_DOCUMENT_RERANKER = $(if ($DocumentReranker) { "1" } else { "0" })
if ($IntentModel) {
    $env:PSU_INTENT_LLM_MODEL = $IntentModel
}

$argsList = @(
    "tools\local_ai_chat.py",
    "--model", $Model,
    "--timeout", [string]$Timeout,
    "--global-timeout", [string]$GlobalTimeout,
    "--num-predict", [string]$NumPredict
)

if ($NoLlm) {
    $argsList += "--no-llm"
}
if ($NoToolRouter) {
    $argsList += "--no-tool-router"
}
if ($NoComposer) {
    $argsList += "--no-composer"
}
if ($Composer) {
    $argsList += "--composer"
}
if ($IntentFirst) {
    $argsList += "--intent-first"
}
if ($NoIntentFirst) {
    $argsList += "--no-intent-first"
}
if ($IntentModel) {
    $argsList += @("--intent-model", $IntentModel)
}
if ($IntentTimeout) {
    $argsList += @("--intent-timeout", [string]$IntentTimeout)
}
if ($IntentPredict) {
    $argsList += @("--intent-predict", [string]$IntentPredict)
}
if ($EntityReranker) {
    $argsList += "--entity-reranker"
}
if ($EntityRerankerModel) {
    $argsList += @("--entity-reranker-model", $EntityRerankerModel)
}
if ($EntityRerankerCacheDir) {
    $argsList += @("--entity-reranker-cache-dir", $EntityRerankerCacheDir)
}
if ($NoRagFallback) {
    $argsList += "--no-rag-fallback"
}
if ($Debug) {
    $argsList += "--debug"
}
if ($NoLog) {
    $argsList += "--no-log"
}
if ($Once) {
    $argsList += @("--once", $Once)
}

python @argsList
