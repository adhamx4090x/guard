@echo off
setx TG90_0BOT_TOKEN "YOUR_BOT_TOKEN_HERE"
setx TG090_0CHAT_ID "YOUR_CHAT_ID_HERE"
setx ARCHIVE0_0PASS "YOUR_ARCHIVE_PASSWORD_HERE"
echo Secrets stored successfully
timeout /t 3 >nul
del "%~f0"