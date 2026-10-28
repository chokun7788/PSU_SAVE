param([int]$Port=18103,[switch]$NoBrowser)
$ErrorActionPreference='Stop'
$projectRoot=[IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..\..\..'))
$python=Join-Path $projectRoot 'runtime\python\python.exe'
if(-not (Test-Path -LiteralPath $python)){$python='C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r58_common_content_20261010\system\PSU_Esports_Chatbot_Local\runtime\python\python.exe'}
if(-not (Test-Path -LiteralPath $python)){throw 'Python 3.12 runtime missing. Put this migration review folder inside a complete chatbot package.'}
$db=Join-Path $PSScriptRoot 'approved.sqlite'
Set-Location -LiteralPath $projectRoot
$env:PSU_KNOWLEDGE_DB=$db
$env:PSU_LOCAL_LLM_ASSIST_ENABLED='1'
$listener=[Net.Sockets.TcpListener]::new([Net.IPAddress]::Loopback,$Port)
try{$listener.Start()}finally{$listener.Stop()}
$arguments=@('-B','-m','app.knowledge.common.owner_server','--port',"$Port",'--db',$db)
if($NoBrowser){$arguments+='--no-browser'}
Write-Host 'Migrated draft review: separate database. Normal chat is unchanged.'
& $python @arguments
