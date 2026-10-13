$ErrorActionPreference='Stop'
$dbPath=if($env:PSU_KNOWLEDGE_DB){$env:PSU_KNOWLEDGE_DB}else{Join-Path $PSScriptRoot 'data\knowledge\approved.sqlite'}
$sessionPath=Join-Path (Split-Path -Parent $dbPath) 'owner-session.json'
if(-not(Test-Path -LiteralPath $sessionPath)){Write-Host 'No owner editor session for this database.';return}
$session=Get-Content -LiteralPath $sessionPath -Raw | ConvertFrom-Json
$proc=Get-CimInstance Win32_Process -Filter ('ProcessId='+$session.pid) -ErrorAction SilentlyContinue
if($proc -and $proc.CommandLine.Contains('app.knowledge.common.owner_server') -and $proc.CommandLine.Contains($dbPath)){
    Stop-Process -Id $session.pid
    Write-Host 'Stopped this database owner editor.'
}else{throw 'Session process identity does not match. No process was stopped.'}
