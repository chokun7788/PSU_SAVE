$ErrorActionPreference = "Stop"
$packageRoot = $PSScriptRoot
. (Join-Path $packageRoot "Booking-Dashboard-Probe.ps1")
$ownerDashboardAt8080 = Test-BookingDashboardIdentity -BaseUrl "http://127.0.0.1:8080"
$chatbotPort = 8094
$chatbotUrl = "http://127.0.0.1:$chatbotPort/"

function Test-LocalPortInUse([int]$ListenPort) {
    $client = [System.Net.Sockets.TcpClient]::new()
    try {
        $client.Connect("127.0.0.1", $ListenPort)
        return $true
    } catch {
        return $false
    } finally {
        $client.Dispose()
    }
}

if (Test-LocalPortInUse $chatbotPort) {
    try {
        $health = Invoke-RestMethod -Uri "http://127.0.0.1:$chatbotPort/health" -TimeoutSec 2
        if ($health.service -eq "psu-esports-chat-web") {
            Write-Host "Chatbot is already running: $chatbotUrl"
            Start-Process $chatbotUrl
            return
        }
    } catch { }
    throw "Chatbot port $chatbotPort is already in use by another service."
}

$logs = Join-Path $packageRoot "data\logs\launcher"
New-Item -ItemType Directory -Force -Path $logs | Out-Null
$runId = (Get-Date -Format "yyyyMMdd_HHmmss_fff") + "_" + [guid]::NewGuid().ToString("N").Substring(0, 8)
$scriptPath = Join-Path $packageRoot "Open-PSU-Esports-Chatbot.ps1"
if (-not (Test-Path -LiteralPath $scriptPath)) {
    throw "Missing package launcher: $scriptPath"
}
$child = Start-Process -FilePath "PowerShell.exe" `
    -ArgumentList @("-NoProfile", "-ExecutionPolicy", "Bypass", "-File", ('"' + $scriptPath + '"'), "-Port", "$chatbotPort") `
    -WorkingDirectory $packageRoot -WindowStyle Hidden -PassThru `
    -RedirectStandardOutput (Join-Path $logs "chatbot_$runId.out.log") `
    -RedirectStandardError (Join-Path $logs "chatbot_$runId.err.log")
Write-Host "Starting Chatbot in the background (process $($child.Id))."
Write-Host "Chatbot: $chatbotUrl"
Write-Host "Dashboard: http://127.0.0.1:$(if ($ownerDashboardAt8080) { 8080 } else { 8091 })/"
Write-Host "Startup logs: $logs"
Write-Host "The window can now close. The computer must remain on for local answers."
