cd /d "%~dp0"
@echo off
setlocal enabledelayedexpansion

set "passwd=%ARCHIVE0_0PASS%"
if not defined passwd exit /b 1

set "temp_folder=%TEMP%\archive_temp_%RANDOM%"
mkdir "!temp_folder!" 2>nul

for /f "usebackq delims=" %%f in ("targets.txt") do (
    if exist "%%f" (
        xcopy "%%f" "!temp_folder!\" /E /I /Y /Q
    )
)

if not exist "!temp_folder!\*" (
    rmdir /s /q "!temp_folder!"
    exit /b 1
)

"%~dp0\..\7zr.exe" a -t7z -p"!passwd!" -mhe=on "%~dp0\..\protected0_0data.7z" "!temp_folder!" >nul
if errorlevel 1 (
    rmdir /s /q "!temp_folder!"
    exit /b 1
)

rmdir /s /q "!temp_folder!"

if not exist "%~dp0\..\protected0_0data.7z" exit /b 1