param(
    [string]$BaseModel = "bge-m3",
    [string]$Q8Model = "psu-bge-m3:q8_0",
    [string]$Q4Model = "psu-bge-m3:q4_k_m",
    [switch]$AlsoQ4
)

$ErrorActionPreference = "Stop"
Set-Location -LiteralPath (Split-Path -Parent $PSScriptRoot)

$ollama = (Get-Command ollama -ErrorAction SilentlyContinue).Source
if (-not $ollama) {
    $candidate = Join-Path $env:LOCALAPPDATA "Programs\Ollama\ollama.exe"
    if (Test-Path -LiteralPath $candidate) {
        $ollama = $candidate
    }
}
if (-not $ollama) {
    throw "ไม่พบ ollama.exe กรุณาติดตั้งหรือเพิ่ม Ollama ใน PATH"
}

& $ollama pull $BaseModel
& $ollama create $Q8Model --quantize q8_0 -f "models\Modelfile.bge-m3-1024"
if ($AlsoQ4) {
    & $ollama create $Q4Model --quantize q4_k_m -f "models\Modelfile.bge-m3-1024"
}

& $ollama list
