@echo off

call all\archive_and_encrypt.bat
if errorlevel 1 exit /b 1

call all\send_via_telegram.py
if errorlevel 1 exit /b 1