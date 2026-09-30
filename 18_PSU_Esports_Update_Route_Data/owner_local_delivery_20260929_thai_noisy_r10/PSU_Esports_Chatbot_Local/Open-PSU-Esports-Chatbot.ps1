param(
    [int]$Port = 8094
)

$ErrorActionPreference = "Stop"
$projectRoot = $PSScriptRoot
Set-Location -LiteralPath $projectRoot
. (Join-Path $projectRoot "Booking-Dashboard-Probe.ps1")

if ($Port -lt 1024 -or $Port -gt 65535) {
    throw "Port must be between 1024 and 65535."
}

$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
    throw "Python was not found. Install Python 3.11 or newer, select Add Python to PATH, then open this file again."
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
    $ollama = Get-Command ollama -ErrorAction SilentlyContinue
    if (-not $ollama) {
        throw "Ollama API is not running and the Ollama command was not found. Open Ollama or add it to PATH, then try again."
    }
    Write-Host "Starting Ollama..."
    Start-Process -FilePath $ollama.Source -ArgumentList "serve" -WindowStyle Hidden
    for ($attempt = 1; $attempt -le 30; $attempt++) {
        Start-Sleep -Seconds 1
        if (Test-OllamaReady) { break }
    }
}

if (-not (Test-OllamaReady)) {
    throw "Ollama did not start. Open the Ollama desktop application once, then try again."
}

$models = (Invoke-RestMethod -Uri "http://127.0.0.1:11434/api/tags" -TimeoutSec 3).models.name
$installedModelBases = @($models | ForEach-Object { ([string]$_) -replace ':latest$', '' })
$requiredModels = @("scb10x/typhoon2.5-qwen3-4b", "psu-bge-m3:q8_0")
$missingModels = @($requiredModels | Where-Object { $_ -notin $installedModelBases })

if ($missingModels.Count -gt 0) {
    if (-not (Get-Command ollama -ErrorAction SilentlyContinue)) {
        throw "Required models are missing. Add the Ollama command to PATH, then run Setup-Local-Models.cmd."
    }
    Write-Host "First-time setup: downloading the required local model(s)..."
    & (Join-Path $projectRoot "Setup-Local-Models.ps1")
    if ($LASTEXITCODE -ne 0) {
        throw "Local model setup did not complete. Check the message above and try again while connected to the internet."
    }
}

& (Join-Path $projectRoot "Start-PSU-Esports-Chatbot.ps1") -Port $Port -OpenBrowser
