cd /d "%~dp0"
@echo off
ping -n 1 8.8.8.8 >nul
if errorlevel 1 exit /b 1
exit /b 0