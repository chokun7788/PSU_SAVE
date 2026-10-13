# Shared by all launchers. No global PATH changes and no process termination.
function Get-ChatbotPython([string]$PackageRoot, [string]$PythonPath = '') {
    $binding = $null
    $manifest = Join-Path $PackageRoot 'package_manifest.json'
    if (Test-Path -LiteralPath $manifest) {
        $binding = (Get-Content -LiteralPath $manifest -Raw | ConvertFrom-Json).python_runtime
    }
    $origin = 'explicit'
    if (-not $PythonPath) { $PythonPath = $env:PSU_PYTHON_EXE; $origin = 'environment' }
    if (-not $PythonPath) {
        $bundled = Join-Path $PackageRoot 'runtime\python\python.exe'
        if (Test-Path -LiteralPath $bundled) { $PythonPath = $bundled; $origin = 'bundled' }
        elseif ($binding.path) { $PythonPath = [string]$binding.path; $origin = 'manifest' }
        else {
            $command = Get-Command python -CommandType Application -ErrorAction SilentlyContinue | Select-Object -First 1
            if ($command) { $PythonPath = $command.Source; $origin = 'path' }
            else { $PythonPath = Join-Path $env:USERPROFILE '.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'; $origin = 'fallback' }
        }
    }
    if (-not [System.IO.Path]::IsPathRooted($PythonPath)) { $PythonPath = Join-Path $PackageRoot $PythonPath }
    if (-not (Test-Path -LiteralPath $PythonPath -PathType Leaf)) { throw "Selected Python does not exist ($origin): $PythonPath. No silent fallback was used." }
    # Single quoted Python literals survive native argument forwarding in both
    # Windows PowerShell 5.1 and PowerShell 7 (5.1 strips embedded double quotes).
    $code = 'import sys,os,struct,json,hashlib;print(json.dumps(dict(path=sys.executable,version=list(sys.version_info[:3]),bits=struct.calcsize(''P'')*8,executable_id=hashlib.sha256(os.path.normcase(os.path.realpath(sys.executable)).encode(''utf-8'')).hexdigest()[:16])))'
    $raw = & $PythonPath -B -c $code
    if ($LASTEXITCODE -ne 0) { throw "Selected Python could not run: $PythonPath" }
    $identity = $raw | ConvertFrom-Json
    if ($identity.version[0] -ne 3 -or $identity.version[1] -lt 11 -or $identity.bits -ne 64) { throw 'Chatbot requires 64-bit Python 3.11 or newer.' }
    return [pscustomobject]@{ Path = $identity.path; Identity = $identity; Origin = $origin }
}

function Get-ChatbotInstallationId([string]$PackageRoot) {
    $hasher = [System.Security.Cryptography.SHA256]::Create()
    try {
        $bytes = [System.Text.Encoding]::UTF8.GetBytes(([System.IO.Path]::GetFullPath($PackageRoot)).TrimEnd('\').ToLowerInvariant())
        return ([System.BitConverter]::ToString($hasher.ComputeHash($bytes))).Replace('-','').ToLowerInvariant().Substring(0,16)
    } finally { $hasher.Dispose() }
}

function Test-ChatbotHealth($Health, [string]$Version, [string]$InstallationId, $PythonIdentity) {
    $reasons = @()
    if ($env:PSU_EXPECTED_SOURCE_SHA256 -and $Health.common_loaded_build.loaded_source_sha256 -ne $env:PSU_EXPECTED_SOURCE_SHA256) { $reasons += 'loaded_source_stale' }
    if ($Health.ok -ne $true -or $Health.service -ne 'psu-esports-chat-web') { $reasons += 'health_service' }
    if ($Health.runtime.version -ne $Version -or $Health.runtime.installation_id -ne $InstallationId) { $reasons += 'package_identity' }
    if ($Health.runtime.python.executable_id -ne $PythonIdentity.executable_id -or
        ($Health.runtime.python.version -join '.') -ne ($PythonIdentity.version -join '.') -or
        $Health.runtime.python.bits -ne $PythonIdentity.bits) { $reasons += 'python_identity' }
    if ($Health.warmup.ok -ne $true) { $reasons += 'warmup_failed_or_missing' }
    if ($Health.runtime.local_llm.enabled -ne $true -or $Health.llm_preflight.ok -ne $true) { $reasons += 'llm_preflight_failed_or_missing' }
    $workers = @($Health.pipeline_workers.workers)
    if ($Health.pipeline_workers.enabled -ne $true -or $Health.pipeline_workers.started -ne $true -or
        $workers.Count -lt 1 -or @($workers | Where-Object { $_.alive -ne $true -or $_.ready -ne $true }).Count -gt 0) { $reasons += 'worker_not_ready' }
    return [pscustomobject]@{ Ready = ($reasons.Count -eq 0); Reasons = $reasons }
}

function Test-ChatbotAnswer($Response) {
    $reasons = @()
    if ($Response.ok -ne $true -or $Response.timed_out -eq $true -or $Response.error) { $reasons += 'request_failed' }
    # A successful transport can contain a timeout or a wrong answer. Validate this
    # static source oracle only; it is not a live occupancy or whole-corpus gate.
    if ($Response.validation_ok -ne $true -or $Response.route_category -ne 'reservation' -or $Response.route_intent -ne 'booking_advance_time' -or
        $Response.mode -ne 'pipeline:rule_en' -or $Response.answer -notmatch '\bat least 1 hour\b' -or
        $Response.answer -notmatch 'https://esports\.computing\.psu\.ac\.th/') { $reasons += 'answer_oracle' }
    return [pscustomobject]@{ Ready = ($reasons.Count -eq 0); Reasons = $reasons }
}

function Invoke-ChatbotReadiness([string]$BaseUrl, [string]$Version, [string]$InstallationId, $PythonIdentity) {
    $started = [System.Diagnostics.Stopwatch]::StartNew()
    try {
        $health = Invoke-RestMethod -Uri "$BaseUrl/health" -TimeoutSec 3
        $gate = Test-ChatbotHealth $health $Version $InstallationId $PythonIdentity
        if (-not $gate.Ready) { return [pscustomobject]@{ Ready=$false; Stage='health'; Reasons=$gate.Reasons; Health=$health } }
        # Isolated synthetic session; this audit exchange is kept in local logs.
        $body = @{ question='How far ahead must I book?'; locale='en'; debug=$false;
            client_session_id=('startup-probe-'+[guid]::NewGuid().ToString('N')); client_turn_id='readiness-1' } | ConvertTo-Json
        $response = Invoke-RestMethod -Uri "$BaseUrl/api/chat" -Method Post -ContentType 'application/json; charset=utf-8' `
            -Body ([System.Text.Encoding]::UTF8.GetBytes($body)) -TimeoutSec 25
        $gate = Test-ChatbotAnswer $response
        return [pscustomobject]@{ Ready=$gate.Ready; Stage='answer'; Reasons=$gate.Reasons; Health=$health;
            Response=$response; ElapsedMs=$started.ElapsedMilliseconds }
    } catch {
        return [pscustomobject]@{ Ready=$false; Stage='transport'; Reasons=@($_.Exception.Message); ElapsedMs=$started.ElapsedMilliseconds }
    }
}
