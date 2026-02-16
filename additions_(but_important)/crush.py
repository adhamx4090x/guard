import os
import sys
import subprocess
import secrets
import shutil

TARGET = os.path.join(os.environ["USERPROFILE"], "Documents", "guard")

if not os.path.isdir(TARGET):
    sys.exit("Target not found")


def get_disk_type():
    try:
        out = subprocess.check_output(
            'powershell "Get-PhysicalDisk | Select MediaType"',
            shell=True, text=True
        ).upper()
        if "SSD" in out:
            return "SSD"
        if "HDD" in out:
            return "HDD"
        if "SCM" in out:
            return "NVME"
    except (subprocess.CalledProcessError, FileNotFoundError):

        pass
    return "UNKNOWN"


disk = get_disk_type()
print("Disk type:", disk)


def shred_file(path, passes=5):
    size = os.path.getsize(path)
    with open(path, "r+b", buffering=0) as f:
        for _ in range(passes):
            f.seek(0)
            written = 0
            while written < size:
                chunk = min(65536, size - written)
                f.write(secrets.token_bytes(chunk))
                written += chunk
            f.flush()
            os.fsync(f.fileno())
        f.truncate(0)
    os.remove(path)


def crypto_wipe_folder(folder):

    for root, dirs, files in os.walk(folder):
        for name in files:
            p = os.path.join(root, name)
            with open(p, "rb") as f:
                data = f.read()
            key = secrets.token_bytes(len(data))
            enc = bytes(a ^ b for a, b in zip(data, key))
            with open(p, "wb") as f:
                f.write(enc)
    shutil.rmtree(folder)


def nvme_secure_erase():
    print("NVMe detected -> requires firmware secure erase")
    print("Use vendor tool (Samsung Magician / BIOS)")


if disk == "HDD":
    for root, dirs, files in os.walk(TARGET):
        for name in files:
            shred_file(os.path.join(root, name))
    shutil.rmtree(TARGET)

elif disk == "SSD":
    print("Using crypto-wipe strategy")
    crypto_wipe_folder(TARGET)

elif disk == "NVME":
    nvme_secure_erase()

else:
    print("Unknown storage -> fallback overwrite")
    for root, dirs, files in os.walk(TARGET):
        for name in files:
            shred_file(os.path.join(root, name))
    shutil.rmtree(TARGET)

p = os.path.abspath(sys.argv[0])
subprocess.Popen(
    f'cmd /c ping 127.0.0.1 -n 2 > nul & del /f /q "{p}"',
    shell=True,
    creationflags=0x08000000
)
