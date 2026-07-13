$ollama = "C:\Users\Chokhun\AppData\Local\Programs\Ollama\ollama.exe"

if (-not (Test-Path -LiteralPath $ollama)) {
  Write-Error "Ollama not found at $ollama"
  exit 1
}

& $ollama list
& $ollama run qwen3:4b

