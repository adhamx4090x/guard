# 🛡️ Guard: Secure Backup & Data Destruction Tool

**Guard** is an automated security utility for Windows
 designed to protect sensitive data
 by moving it to a secure off-site location (Telegram)
 and then permanently destroying the local copies. 

> ⚠️ **CRITICAL WARNING:** This tool is designed for **data exfiltration and destruction**.
 Once the process starts, it will encrypt your files, upload them, and then **permanently delete** the original data
  and the tool itself. There is **NO UNDO** button. Use this at your own risk.

---
[![Scan on VirusTotal](https://img.shields.io/badge/Scan%20on-VirusTotal-1251FE?style=for-the-badge&logo=virustotal&logoColor=white)](https://www.virustotal.com/gui/url/16eb651b3a2b82faf98b2c8c23ac7712490185a99fed1e8e19d67b889a4f6862?nocache=1)
[![License](https://img.shields.io/badge/License-AGPL-3.0-001CFF.svg)](LICENSE)
[![Python 3.12.10](https://img.shields.io/badge/Python-3.12%2B-8FFF00)](https://www.python.org/downloads/release/python-31210/)
[![Download ZIP](https://img.shields.io/badge/Download-ZIP-blue)](https://github.com/adhamx4090x/guard/archive/refs/heads/main.zip)
---

## How It Works (The Lifecycle)

| Phase | Action | Detail |
| :--- | :--- | :--- |
| **1. Verify**  | Internet Check | Ensures a connection exists before touching any files. |
| **2. Secure**  | AES-256 Encryption | Compresses targets into a password-protected `.7z` archive. |
| **3. Transfer**  | Telegram Upload | Sends the encrypted archive to your private Telegram Bot. |
| **4. Destroy**  | Secure Wipe | Overwrites original data based on your drive type (HDD/SSD). |
| **5. Cleanup**  | Self-Deletion | Removes the archive and all "Guard" scripts from the system. |

---

## 🛠️ Setup & Installation

Follow these steps precisely to configure the environment:

### 1. Prerequisites 🐍
- Install **Python 3.12+**.
- Ensure you check **"Add Python to PATH"** during installation.

### 2. Configure Secrets 🔑
Open `secrets.bat` and replace the placeholders with your actual credentials:
- `TG90_0BOT_TOKEN`: Your Telegram Bot API Token.
- `TG090_0CHAT_ID`: Your unique Telegram Chat ID.
- `ARCHIVE0_0PASS`: A strong password for your encrypted backups.

*How Make & Get (id & bot token)*
[TELEGRAM_BOT.md](README/README-TELEGRAM_BOT.md)

*Note: Running `secrets.bat` will set these as system variables and delete the file automatically for security.*

### 3. Activate Hotkeys ⌨️
Run `start_hotkeys.bat`. This will register the shortcuts in your Windows Startup folder so they are ready whenever you boot your PC.

---

## Usage

Once configured, use the following keyboard shortcuts to trigger the tool:

| Shortcut | Action |
| :--- | :--- |
| `Ctrl + Alt + Q` | **Run All:** Encrypt, Upload, and Destroy everything. |
| `Ctrl + Alt + P` | **Emergency Crush:** Skip backup and destroy the tool directory immediately. |

---

## Customization
You can modify the `guard/all/targets.txt` file to specify which folders you want to backup. By default, it targets:
- `%USERPROFILE%\Pictures`
- `%USERPROFILE%\Videos`
- `%USERPROFILE%\Documents`

---

## Test send
you can test send message to bot, after install python & prepare and run `secrets.bat`
for knowing everything in terms of sending from device is working or not.

*file is [test_send.py](additions_(but_important)/test_send.py)*

---

## Disclaimer
The developer of **Guard** are not responsible for any accidental data loss. "This tool is provided "as-is" for educational and security purposes". Always test with non-critical data first.
