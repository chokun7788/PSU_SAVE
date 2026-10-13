param([int]$Port=8097,[string]$PythonPath='', [switch]$NoBrowser)
$ErrorActionPreference='Stop'
$packageRoot=$PSScriptRoot
. (Join-Path $packageRoot 'Runtime-Readiness.ps1')
$python=Get-ChatbotPython $packageRoot $PythonPath
if($python.Identity.version[1] -ne 12){throw 'The bundled common-content validator requires 64-bit Python 3.12. Use the bundled runtime or pass -PythonPath.'}
$dbPath=if($env:PSU_KNOWLEDGE_DB){$env:PSU_KNOWLEDGE_DB}else{Join-Path $packageRoot 'data\knowledge\approved.sqlite'}
$sessionPath=Join-Path (Split-Path -Parent $dbPath) 'owner-session.json'
if(Test-Path -LiteralPath $sessionPath){
    $existing=Get-Content -LiteralPath $sessionPath -Raw | ConvertFrom-Json
    $proc=Get-CimInstance Win32_Process -Filter ('ProcessId='+$existing.pid) -ErrorAction SilentlyContinue
    if($proc -and $proc.CommandLine.Contains('app.knowledge.common.owner_server') -and $proc.CommandLine.Contains($dbPath)){
        if(-not $NoBrowser){Start-Process $existing.url}
        Write-Host 'Reopened the existing local owner editor.'
        return
    }
}
$runId=Get-Date -Format 'yyyyMMdd_HHmmss_ffff'
$logs=Join-Path $packageRoot 'data\logs\owner_content'
New-Item -ItemType Directory -Force -Path $logs | Out-Null
$args=@('-B','-m','app.knowledge.common.owner_server','--port',"$Port",'--db',('"'+$dbPath+'"'))
if($NoBrowser){$args+='--no-browser'}
$child=Start-Process -FilePath $python.Path -ArgumentList $args -WorkingDirectory $packageRoot -WindowStyle Hidden -PassThru -RedirectStandardOutput (Join-Path $logs ($runId+'.out.log')) -RedirectStandardError (Join-Path $logs ($runId+'.err.log'))
Write-Host "Starting local owner editor (PID $($child.Id)) on port $Port."
Write-Host 'If the port is occupied, choose another with -Port. Existing applications are preserved.'
