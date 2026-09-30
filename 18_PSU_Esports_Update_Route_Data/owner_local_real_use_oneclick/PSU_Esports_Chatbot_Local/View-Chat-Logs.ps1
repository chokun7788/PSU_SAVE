param(
    [int]$SessionLimit = 100,
    [int]$MessageLimit = 1000
)

$ErrorActionPreference = "Stop"
Set-Location -LiteralPath $PSScriptRoot

$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
    throw "Python was not found. Install Python 3.11 or newer, then run this file again."
}

$database = Join-Path $PSScriptRoot "data\logs\chat_history.sqlite3"
if (-not (Test-Path $database)) {
    throw "No chat history has been created yet. Start the chatbot and ask at least one question first."
}

$output = Join-Path $PSScriptRoot "data\logs\chat_history_report.html"
& $python.Source "tools\export_local_chat_logs.py" --database $database --output $output --session-limit $SessionLimit --message-limit $MessageLimit
if ($LASTEXITCODE -ne 0) {
    throw "Could not create the chat log report."
}

Start-Process $output
