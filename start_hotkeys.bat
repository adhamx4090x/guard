@echo off
setlocal

set "base=%~dp0additions_(but_important)"
set "startup=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"

if not exist "%startup%\hotkey0_0.exe" (
    copy "%base%\hotkey0_0.exe" "%startup%" >nul
)

exit