#!/usr/bin/env python3
"""
PhantomDisk - Fallback (Acil Durum Yok Edici)
Geliştirici: burakcanbalta | 2025
Amaç: Destroyer devreye giremezse son çare olarak RAM ortamını zorla kapatmak.
"""

import os
import time
import subprocess
import psutil

PHANTOM_PATH = "/mnt/phantomdisk"
DESTROYER = "phantom_destroyer.py"
SHELL_LOG = os.path.join(PHANTOM_PATH, "phantom_shell.log")
CHECK_INTERVAL = 10  # saniyede bir kontrol

def destroy_ram():
    print("[!!!] Fallback devrede! RAM ortamı zorla yok ediliyor...")
    try:
        subprocess.call(["python3", DESTROYER])
    except Exception:
        print("[X] Destroyer hata verdi. Fallback unmount aktif.")
        subprocess.call(["umount", PHANTOM_PATH])
    print("[✔] RAM ortamı silindi.")
    os.system("sync")  # RAM flush
    time.sleep(1)
    os.system("shutdown -h now")  # Son çare: sistemi durdur

def check_log_activity():
    try:
        last_mod = os.path.getmtime(SHELL_LOG)
        if time.time() - last_mod > 120:
            return False
        return True
    except:
        return False

def check_mount_status():
    mounts = subprocess.check_output("mount", shell=True).decode()
    return PHANTOM_PATH in mounts and "tmpfs" in mounts

def monitor():
    print("=== PhantomFallback Gözcü Başladı ===")
    while True:
        if not check_mount_status():
            print("[!] Mount noktası geçersiz.")
            destroy_ram()
        elif not check_log_activity():
            print("[!] Shell logu aktif değil.")
            destroy_ram()
        elif psutil.virtual_memory().percent > 95:
            print("[!] RAM kullanımı %95’i geçti!")
            destroy_ram()
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    try:
        monitor()
    except KeyboardInterrupt:
        print("[*] Fallback sonlandırıldı.")
