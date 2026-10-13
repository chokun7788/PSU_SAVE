# Model service belongs to this package and this Windows account.
# Environment changes are confined to this PowerShell process and its children.
function Initialize-PSUModels([string]$PackageRoot) {
    $bundled = Join-Path $PackageRoot 'runtime\ollama\ollama.exe'
    if (-not (Test-Path -LiteralPath $bundled)) {
        $command = Get-Command ollama -CommandType Application -ErrorAction SilentlyContinue | Select-Object -First 1
        if (-not $command) { throw 'Missing bundled runtime/ollama/ollama.exe. Use a complete delivery package.' }
        $script:PSUOllamaExe = $command.Source
        $env:OLLAMA_HOST = '127.0.0.1:11434'
        $env:OLLAMA_URL = 'http://127.0.0.1:11434'
        $env:PSU_EMBEDDING_OLLAMA_URL = $env:OLLAMA_URL
        try { Invoke-RestMethod "$env:OLLAMA_URL/api/tags" -TimeoutSec 2 | Out-Null; return } catch {}
        Start-Process -FilePath $script:PSUOllamaExe -ArgumentList 'serve' -WindowStyle Hidden | Out-Null
        for ($a=0; $a -lt 30; $a++) {
            try { Invoke-RestMethod "$env:OLLAMA_URL/api/tags" -TimeoutSec 2 | Out-Null; return } catch { Start-Sleep -Milliseconds 500 }
        }
        throw 'Installed Ollama could not start.'
    }
    $script:PSUOllamaExe = [IO.Path]::GetFullPath($bundled)
    $modelRoot = Join-Path $PackageRoot 'models\ollama'
    $runRoot = Join-Path $PackageRoot 'data\runtime'
    New-Item -ItemType Directory -Force -Path $modelRoot,$runRoot | Out-Null
    $sessionFile = Join-Path $runRoot 'model-service.json'
    $sha=[Security.Cryptography.SHA256]::Create()
    try { $key=([BitConverter]::ToString($sha.ComputeHash([Text.Encoding]::UTF8.GetBytes($script:PSUOllamaExe.ToLowerInvariant())))).Replace('-','') } finally { $sha.Dispose() }
    $mutex=[Threading.Mutex]::new($false, ('Local\PSUModels'+$key))
    $locked=$false
    try {
        try { $locked=$mutex.WaitOne(30000) } catch [Threading.AbandonedMutexException] { $locked=$true }
        if (-not $locked) { throw 'Another package launch is still starting its model service; retry shortly.' }
        $chosen=$null
        if (Test-Path -LiteralPath $sessionFile) {
            try {
                $session=Get-Content -LiteralPath $sessionFile -Raw | ConvertFrom-Json
                $proc=Get-CimInstance Win32_Process -Filter ('ProcessId='+[int]$session.pid)
                if ($proc -and $proc.ExecutablePath -eq $script:PSUOllamaExe -and
                    $proc.CreationDate.ToUniversalTime().Ticks -eq ([DateTime]$session.created_at).ToUniversalTime().Ticks -and
                    $session.model_root -eq $modelRoot -and $proc.CommandLine -match '\bserve\b') {
                    Invoke-RestMethod ($session.url+'/api/tags') -TimeoutSec 2 | Out-Null
                    $chosen=[int]$session.port
                }
            } catch {}
        }
        if ($null -eq $chosen) {
            foreach ($port in 11436..11455) {
                $listener=[Net.Sockets.TcpListener]::new([Net.IPAddress]::Loopback,$port)
                try { $listener.Start(); $chosen=$port; break } catch {} finally { $listener.Stop() }
            }
            if ($null -eq $chosen) { throw 'No free package model port (11436..11455).' }
            $env:OLLAMA_MODELS=$modelRoot
            $env:OLLAMA_HOST="127.0.0.1:$chosen"
            $env:OLLAMA_URL="http://127.0.0.1:$chosen"
            $env:PSU_EMBEDDING_OLLAMA_URL=$env:OLLAMA_URL
            $stamp=[guid]::NewGuid().ToString('N')
            $child=Start-Process -FilePath $script:PSUOllamaExe -ArgumentList 'serve' -WorkingDirectory $PackageRoot -WindowStyle Hidden -PassThru -RedirectStandardOutput (Join-Path $runRoot ($stamp+'.out.log')) -RedirectStandardError (Join-Path $runRoot ($stamp+'.err.log'))
            $ready=$false
            for ($a=0; $a -lt 40; $a++) {
                if ($child.HasExited) { break }
                try { Invoke-RestMethod "$env:OLLAMA_URL/api/tags" -TimeoutSec 2 | Out-Null; $ready=$true; break } catch { Start-Sleep -Milliseconds 500 }
            }
            if (-not $ready) { throw "Bundled model service failed to start. Read $runRoot." }
            $proc=Get-CimInstance Win32_Process -Filter ('ProcessId='+$child.Id)
            @{pid=$child.Id;created_at=$proc.CreationDate.ToUniversalTime().ToString('o');port=$chosen;url=$env:OLLAMA_URL;executable=$script:PSUOllamaExe;model_root=$modelRoot} | ConvertTo-Json | Set-Content -LiteralPath $sessionFile -Encoding UTF8
        }
        $env:OLLAMA_MODELS=$modelRoot
        $env:OLLAMA_HOST="127.0.0.1:$chosen"
        $env:OLLAMA_URL="http://127.0.0.1:$chosen"
        $env:PSU_EMBEDDING_OLLAMA_URL=$env:OLLAMA_URL
    } finally { if ($locked) { $mutex.ReleaseMutex() }; $mutex.Dispose() }
}

function Assert-PSUModels([string]$PackageRoot, [switch]$DownloadMissing) {
    Initialize-PSUModels $PackageRoot
    $names=@((Invoke-RestMethod "$env:OLLAMA_URL/api/tags" -TimeoutSec 5).models.name | ForEach-Object { ([string]$_) -replace ':latest$','' })
    $missing=@(@('scb10x/typhoon2.5-qwen3-4b','psu-bge-m3:q8_0') | Where-Object { $_ -notin $names })
    if ($missing.Count -and $DownloadMissing) {
        & (Join-Path $PackageRoot 'Setup-Local-Models.ps1')
        $names=@((Invoke-RestMethod "$env:OLLAMA_URL/api/tags" -TimeoutSec 5).models.name | ForEach-Object { ([string]$_) -replace ':latest$','' })
        $missing=@(@('scb10x/typhoon2.5-qwen3-4b','psu-bge-m3:q8_0') | Where-Object { $_ -notin $names })
    }
    if ($missing.Count) { throw "Missing models: $($missing -join ', '). Run Setup-Local-Models.cmd with internet access." }
    if ((Test-Path -LiteralPath (Join-Path $PackageRoot 'runtime\ollama\ollama.exe')) -and (Test-Path -LiteralPath (Join-Path $PackageRoot 'models\expected_manifests.json'))) {
        & (Join-Path $PackageRoot 'runtime\python\python.exe') -B (Join-Path $PackageRoot 'Model-Manifest-Check.py')
        if ($LASTEXITCODE -ne 0) { throw 'Model identity verification failed; chatbot startup stopped.' }
    }
}

function Warm-PSUChatModel {
    # Exercise one token before accepting chat requests. First CUDA execution
    # can take much longer than a normal question on a new installation.
    Write-Host 'Preparing the local chat model. First startup may take a few minutes.'
    $payload=@{model='scb10x/typhoon2.5-qwen3-4b';prompt='Say OK';stream=$false;think=$false;keep_alive='30m';options=@{num_ctx=3072;num_predict=1}} | ConvertTo-Json -Depth 5
    $warm=Invoke-RestMethod "$env:OLLAMA_URL/api/generate" -Method Post -ContentType 'application/json' -Body $payload -TimeoutSec 180
    if ($warm.done -ne $true) { throw 'Local model warmup did not finish. Read data/runtime or retry the launcher.' }
}
