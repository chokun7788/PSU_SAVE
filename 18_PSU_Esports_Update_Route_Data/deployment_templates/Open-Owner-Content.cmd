@echo off
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0Open-Owner-Content.ps1" %*
if errorlevel 1 pause
