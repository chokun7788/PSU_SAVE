param(
    [string]$ModelDir = "D:\OllamaModels",
    [string]$HostUrl = "http://127.0.0.1:11435",
    [string]$ConfigPath = "data\eval\model_benchmark_models_under_10b.json",
    [switch]$SkipPull
)

$ErrorActionPreference = "Stop"
$ProjectRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
$FullConfigPath = Resolve-Path (Join-Path $ProjectRoot $ConfigPath)

New-Item -ItemType Directory -Path $ModelDir -Force | Out-Null

$env:OLLAMA_MODELS = $ModelDir
$env:OLLAMA_HOST = $HostUrl

function Test-Ollama {
    try {
        Invoke-RestMethod -Uri "$HostUrl/api/tags" -Method Get -TimeoutSec 2 | Out-Null
        return $true
    } catch {
        return $false
    }
}

if (-not (Test-Ollama)) {
    Write-Host "Starting Ollama on $HostUrl with OLLAMA_MODELS=$ModelDir"
    Start-Process -FilePath "ollama" -ArgumentList "serve" -WindowStyle Hidden -WorkingDirectory $ProjectRoot | Out-Null
    $ready = $false
    for ($i = 0; $i -lt 30; $i++) {
        Start-Sleep -Seconds 1
        if (Test-Ollama) {
            $ready = $true
            break
        }
    }
    if (-not $ready) {
        throw "Ollama did not become ready at $HostUrl"
    }
}

Write-Host "Ollama ready at $HostUrl"

if ($SkipPull) {
    ollama list
    exit 0
}

$config = Get-Content -Path $FullConfigPath -Raw -Encoding UTF8 | ConvertFrom-Json
foreach ($model in $config.models) {
    $name = [string]$model.name
    Write-Host ""
    Write-Host "Pulling $name"
    ollama pull $name
}

Write-Host ""
Write-Host "Installed models on $ModelDir"
ollama list
