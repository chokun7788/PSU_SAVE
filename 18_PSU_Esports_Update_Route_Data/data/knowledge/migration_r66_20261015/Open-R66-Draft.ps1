param([int]$Port=8099,[string]$PythonPath='', [switch]$NoBrowser)
$ErrorActionPreference='Stop'
$r66ProjectRoot=(Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..\..\..')).Path
$r66Candidate=Join-Path $PSScriptRoot 'candidate.sqlite'
if(-not (Test-Path -LiteralPath $r66Candidate)){throw 'R66 candidate.sqlite is missing.'}
$r66PreviousDatabase=$env:PSU_KNOWLEDGE_DB
try {
    $env:PSU_KNOWLEDGE_DB=$r66Candidate
    & (Join-Path $r66ProjectRoot 'Open-Owner-Content.ps1') -Port $Port -PythonPath $PythonPath -NoBrowser:$NoBrowser
} finally {
    $env:PSU_KNOWLEDGE_DB=$r66PreviousDatabase
}
