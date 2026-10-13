param([switch]$NoBrowser, [string]$PythonPath = '', [int]$Port = 0)
$ErrorActionPreference = "Stop"
if ($Port -ne 0 -and ($Port -lt 1024 -or $Port -gt 65535)) { throw 'Port must be between 1024 and 65535.' }
$packageRoot = $PSScriptRoot
. (Join-Path $packageRoot 'Runtime-Readiness.ps1')
$python = Get-ChatbotPython $packageRoot $PythonPath
. (Join-Path $packageRoot "Booking-Dashboard-Probe.ps1")
$ownerDashboardAt8080 = Test-BookingDashboardIdentity -BaseUrl "http://127.0.0.1:8080"
$manifestPath = Join-Path $packageRoot 'package_manifest.json'
if (-not (Test-Path -LiteralPath $manifestPath)) { throw 'Missing package_manifest.json. Use a complete Chatbot package.' }
$expectedVersion = (Get-Content -LiteralPath $manifestPath -Raw | ConvertFrom-Json).runtime_version
$expectedInstallation = Get-ChatbotInstallationId $packageRoot
$logs = Join-Path $packageRoot 'data\logs\launcher'
New-Item -ItemType Directory -Force -Path $logs | Out-Null
$runId = [DateTime]::UtcNow.ToString('yyyyMMdd_HHmmss_fff', [Globalization.CultureInfo]::InvariantCulture) + '_' + [guid]::NewGuid().ToString('N').Substring(0,8)
$diagnosticPath = Join-Path $logs "readiness_$runId.json"
function Save-Readiness($Result, [string]$Action) {
    @{ action=$Action; python=$python; url=$chatbotUrl; checked_at=[DateTime]::UtcNow.ToString('o'); result=$Result } |
        ConvertTo-Json -Depth 16 | Set-Content -LiteralPath $diagnosticPath -Encoding UTF8
}

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

function Test-ThisPackage($Health) {
    return ($Health.service -eq 'psu-esports-chat-web' -and $Health.runtime.version -eq $expectedVersion -and $Health.runtime.installation_id -eq $expectedInstallation)
}
$chatbotPort = $null
$candidatePorts = if ($Port) { @($Port) } else { 8090..8099 }
foreach ($candidatePort in $candidatePorts) {
    if (Test-LocalPortInUse $candidatePort) {
        try {
            $health = Invoke-RestMethod -Uri "http://127.0.0.1:$candidatePort/health" -TimeoutSec 1
        } catch { $health = $null }
        if ($health -and (Test-ThisPackage $health)) {
            $chatbotUrl = "http://127.0.0.1:$candidatePort/"
            $readiness = Invoke-ChatbotReadiness $chatbotUrl.TrimEnd('/') $expectedVersion $expectedInstallation $python.Identity
            Save-Readiness $readiness 'reuse'
            if (-not $readiness.Ready) { throw "This package is running but not ready: $($readiness.Reasons -join ', '). Read $diagnosticPath. Existing processes were preserved; retry after resolving the recorded failure." }
            Write-Host "This Chatbot package is already running and answered the readiness question: $chatbotUrl"
            if (-not $NoBrowser) { Start-Process $chatbotUrl }
            return
        }
    } elseif ($null -eq $chatbotPort) {
        $chatbotPort = $candidatePort
    }
}
if ($null -eq $chatbotPort) { throw 'Ports 8090..8099 are in use. Close an unused Chatbot instance first.' }
$chatbotUrl = "http://127.0.0.1:$chatbotPort/"

$scriptPath = Join-Path $packageRoot "Open-PSU-Esports-Chatbot.ps1"
if (-not (Test-Path -LiteralPath $scriptPath)) {
    throw "Missing package launcher: $scriptPath"
}
$child = Start-Process -FilePath "PowerShell.exe" `
    -ArgumentList @("-NoProfile", "-ExecutionPolicy", "Bypass", "-File", ('"' + $scriptPath + '"'), "-Port", "$chatbotPort", "-NoBrowser", "-PythonPath", ('"' + $python.Path + '"')) `
    -WorkingDirectory $packageRoot -WindowStyle Hidden -PassThru `
    -RedirectStandardOutput (Join-Path $logs "chatbot_$runId.out.log") `
    -RedirectStandardError (Join-Path $logs "chatbot_$runId.err.log")
Write-Host "Starting Chatbot in the background (process $($child.Id))."
Write-Host "Chatbot: $chatbotUrl"
if ($ownerDashboardAt8080) {
    Write-Host "Booking source: owner Dashboard at http://127.0.0.1:8080/"
} else {
    Write-Host "Booking source: WordPress (read-only, fetched when a status question is asked)."
}
Write-Host "Startup logs: $logs"
Write-Host "Checking readiness before opening the browser. Python: $($python.Path)"
for ($attempt = 0; $attempt -lt 90; $attempt++) {
    if ($child.HasExited) {
        Save-Readiness @{Ready=$false;Stage='process';Reasons=@('launcher_exited');ExitCode=$child.ExitCode} 'startup'
        throw "Chatbot stopped during startup. Read the startup logs in $logs."
    }
    try {
        $health = Invoke-RestMethod -Uri "http://127.0.0.1:$chatbotPort/health" -TimeoutSec 1
    } catch { $health = $null }
    if ($health -and (Test-ThisPackage $health)) {
        $readiness = Invoke-ChatbotReadiness $chatbotUrl.TrimEnd('/') $expectedVersion $expectedInstallation $python.Identity
        Save-Readiness $readiness 'startup'
        if (-not $readiness.Ready) { throw "Chatbot is not ready: $($readiness.Reasons -join ', '). Read $diagnosticPath and startup logs. The browser was not opened." }
        Write-Host "Chatbot answered the readiness question. The computer must remain on for local answers."
        if (-not $NoBrowser) { Start-Process $chatbotUrl }
        return
    }
    Start-Sleep -Seconds 1
}
Save-Readiness @{Ready=$false;Stage='startup_timeout';Reasons=@('health_not_ready')} 'startup'
throw "Chatbot did not become ready within the startup wait. Read $diagnosticPath and startup logs in $logs."
