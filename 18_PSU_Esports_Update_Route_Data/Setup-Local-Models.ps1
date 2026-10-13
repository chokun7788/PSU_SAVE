$ErrorActionPreference='Stop'
$projectRoot=$PSScriptRoot
. (Join-Path $projectRoot 'Portable-Models.ps1')
Initialize-PSUModels $projectRoot
Write-Host 'Downloading models into this package. Internet is needed only for setup and live booking.'
& $script:PSUOllamaExe pull 'scb10x/typhoon2.5-qwen3-4b'
if ($LASTEXITCODE -ne 0) { throw 'Typhoon download failed. Retry Setup-Local-Models.cmd.' }
& $script:PSUOllamaExe pull 'bge-m3'
if ($LASTEXITCODE -ne 0) { throw 'BGE-M3 download failed. Retry Setup-Local-Models.cmd.' }
& $script:PSUOllamaExe create 'psu-bge-m3:q8_0' -f (Join-Path $projectRoot 'models\Modelfile.bge-m3-1024')
if ($LASTEXITCODE -ne 0) { throw 'Creating embedding profile failed.' }
Write-Host 'Setup complete. Open Open-PSU-Esports-Background.cmd or Open-Owner-Content.cmd.'
