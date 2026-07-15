param(
    [string]$Model = "qwen2.5:3b",
    [double]$Timeout = 20,
    [int]$NumPredict = 256,
    [switch]$NoLlm,
    [switch]$NoRagFallback,
    [switch]$Debug,
    [switch]$NoLog,
    [string]$Once = ""
)

$ErrorActionPreference = "Stop"
Set-Location -LiteralPath $PSScriptRoot

$env:PSU_CHATBOT_OLLAMA_MODEL = $Model
$env:PSU_GENERAL_LLM_TIMEOUT_SEC = [string]$Timeout
$env:PSU_GENERAL_LLM_NUM_PREDICT = [string]$NumPredict

$argsList = @(
    "tools\local_ai_chat.py",
    "--model", $Model,
    "--timeout", [string]$Timeout,
    "--num-predict", [string]$NumPredict
)

if ($NoLlm) {
    $argsList += "--no-llm"
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
