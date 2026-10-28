@echo off
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0Open-Migrated-Drafts.ps1" %*
pause
