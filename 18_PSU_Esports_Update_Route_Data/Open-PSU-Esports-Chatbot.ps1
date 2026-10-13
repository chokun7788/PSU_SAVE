param(
    [int]$Port = 8090,
    [switch]$NoBrowser,
    [string]$PythonPath = ''
)

$ErrorActionPreference = "Stop"
$projectRoot = $PSScriptRoot
Set-Location -LiteralPath $projectRoot
. (Join-Path $projectRoot "Booking-Dashboard-Probe.ps1")

if ($Port -lt 1024 -or $Port -gt 65535) {
    throw "Port must be between 1024 and 65535."
}

. (Join-Path $projectRoot 'Runtime-Readiness.ps1')
$python = Get-ChatbotPython $projectRoot $PythonPath
Write-Host "Python: $($python.Path) ($($python.Identity.version -join '.'))"
if (-not $NoBrowser) {
    & (Join-Path $projectRoot 'Open-PSU-Esports-Background.ps1') -Port $Port -PythonPath $python.Path
    return
}

. (Join-Path $projectRoot 'Portable-Models.ps1')
Assert-PSUModels $projectRoot

& (Join-Path $projectRoot "Start-PSU-Esports-Chatbot.ps1") -Port $Port -PythonPath $python.Path -OpenBrowser:(!$NoBrowser)
