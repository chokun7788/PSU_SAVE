$ErrorActionPreference = "Stop"
$projectRoot = $PSScriptRoot
Set-Location -LiteralPath $projectRoot

$ollama = Get-Command ollama -ErrorAction SilentlyContinue
if (-not $ollama) {
    throw "Ollama was not found. Install it from https://ollama.com/download, then run this file again."
}

function Test-OllamaReady {
    try {
        Invoke-RestMethod -Uri "http://127.0.0.1:11434/api/tags" -TimeoutSec 3 | Out-Null
        return $true
    } catch {
        return $false
    }
}

if (-not (Test-OllamaReady)) {
    Write-Host "Starting Ollama..."
    Start-Process -FilePath $ollama.Source -ArgumentList "serve" -WindowStyle Hidden
    for ($attempt = 1; $attempt -le 30; $attempt++) {
        Start-Sleep -Seconds 1
        if (Test-OllamaReady) {
            break
        }
    }
}

if (-not (Test-OllamaReady)) {
    throw "Ollama did not start at http://127.0.0.1:11434. Open Ollama once and retry."
}

Write-Host "Downloading the local chat model. This is a one-time setup and needs internet access."
& $ollama.Source pull "scb10x/typhoon2.5-qwen3-4b"
if ($LASTEXITCODE -ne 0) {
    throw "Could not download the Typhoon local model."
}

Write-Host "Downloading the embedding model for semantic RAG."
& $ollama.Source pull "bge-m3"
if ($LASTEXITCODE -ne 0) {
    throw "Could not download the BGE-M3 embedding model."
}

Write-Host "Creating the PSU embedding profile."
& $ollama.Source create "psu-bge-m3:q8_0" -f (Join-Path $projectRoot "models\Modelfile.bge-m3-1024")
if ($LASTEXITCODE -ne 0) {
    throw "Could not create psu-bge-m3:q8_0."
}

Write-Host "Setup complete. You can now open Start-PSU-Esports-Chatbot.cmd."
