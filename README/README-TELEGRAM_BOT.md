# Telegram Bot Setup Guide (Complete Step-by-Step)

This guide explains how to create a Telegram bot, get the bot token, change the token if needed, and obtain your chat ID.

---

## 1. Creating a Telegram Bot (Using BotFather)

Telegram provides an official bot called BotFather to manage bots.

### Steps:


1. Open Telegram.
2. Search for: @BotFather
3. Start the chat and type:
```
/start
```
4. Create a new bot:
```
/newbot
```
5. Choose:
- Bot name (any name, e.g. MyAutomationBot)
- Username (must end with bot, e.g. my_automation_bot)

BotFather will respond with something like:
```
Here is the token for bot repo @MyAutomationbot:

8084735010:AAFAI2PDwI0u5jJdELTjPjlwfE0OZbE6KnU
```

⚠️ This token is SECRET. Anyone who has it can control your bot.

---

## 2. What is the Bot Token?

The bot token is an API key that allows your script/program
to communicate with Telegram servers.

Example:
```
1234567890:AAFxxxxxxxxxxxxxxxxxxxx
```
You will use it in code like:
```
BOT_TOKEN = "1234567890:AAFxxxxxxxxxxxxxxxxxxxx"
```
Or in environment variables:
```
setx BOT_TOKEN "1234567890:AAFxxxxxxxxxxxxxxxxxxxx"
```

---

## 3. How to Change or Revoke the Bot Token

If your token is leaked or you want to regenerate it:

Steps:

1. Go to ```@BotFather```
2. Type:
```
/mybots
```

3. Select your bot
4. Click:
```
API Token
```
5. Choose:

```
Revoke
```
BotFather will generate a new token and the old one becomes invalid.


---

## 4. Getting Your Chat ID

The chat ID is required so the bot knows where to send messages.

### Method 1 (Using @userinfobot)

1. Search for:
```
@userinfobot
```
2. Start it.
3. It will reply with:
```
Your ID: 1234567890 [example]
```
That number is your chat ID.


---

### Method 2 (Using Your Own Bot)

1. Send any message to your bot.
2. Open this URL in browser (replace TOKEN):
```
https://api.telegram.org/bot<TOKEN>/getUpdates
```
Example:
```
https://api.telegram.org/8084735010:AAFAI2PDwI0u5jJdELTjPjlwfE0OZbE6KnU/getUpdates
```
You will see JSON like:
```
{
  "ok": true,
  "result": [
    {
      "update_id": 279427815,
      "message": {
        "message_id": 10,
        "from": {
          "id": 1234567890,
          "is_bot": false,
          "first_name": "X",
          "username": "admin",
          "language_code": "en"
        },
        "chat": {
          "id": 1234567890,
          "first_name": "X",
          "username": "admin",
          "type": "private"
        },
        "date": 1770453702,
        "text": "."
      }
    }
  ]
}
```
id = your chat ID.


---

## 5. Private Chat vs Group Chat ID

Private Chat
```
ID is positive:
1234567890
```
Group / Channel
```
ID is negative:
-1001234567890
```
To get group ID:

1. Add bot to group
2. Send message
3. Use getUpdates again


---

## 6. Storing Token & Chat ID Securely

Using Environment Variables (Windows)
```
setx TG_BOT_TOKEN "YOUR_TOKEN"
setx TG_CHAT_ID "YOUR_CHAT_ID"
```
In Python:
```
import os

TOKEN = os.getenv("TG_BOT_TOKEN")
CHAT_ID = os.getenv("TG_CHAT_ID")
```
This avoids hardcoding secrets in files.


---

## 7. Minimal Test Example (Python)
```
import requests

TOKEN = "YOUR_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

data = {
    "chat_id": CHAT_ID,
    "text": "Hello from my bot!"
}

requests.post(url, data=data)
```
If everything is correct, you’ll receive the message instantly.


---

## 8. Common Problems

Bot not responding?

- You didn’t start the bot (/start)
- Wrong token
- Bot blocked

Message not delivered?

- Wrong chat ID
- Bot not added to group
- Group privacy mode enabled

Disable privacy:

/setprivacy -> Disable


---

# Security Notes

- Never upload your token to GitHub.
- If leaked → immediately revoke.
- Use .env or environment variables.
- Treat token like a password.


---

# Summary
```
Item          | Purpose
BotFather     | Create & manage bots
Bot Token     | API authentication key
Chat ID       | Destination for messages
Revoke Token  | Regenerate if leaked
getUpdates    | Debug messages
```

