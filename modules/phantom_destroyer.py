#!/usr/bin/env python3
"""
PhantomDisk - RAM Ortamını Güvenli Şekilde Sonlandırıcı
Geliştirici: burakcanbalta | 2025
Amaç: RAM ortamındaki tüm izleri yok eder, mount'u kaldırır, güvenli biçimde çıkış sağlar.
"""

import os
import shutil
import subprocess
import sys
import time

PHANTOM_PATH = "/mnt/phantomdisk"

def verify_env():
    if not os.path.ismount(PHANTOM_PATH):
        print("[X] Phantom ortamı zaten etkin değil. Unmount işlemi gereksiz.")
        sys.exit(0)

def wipe_ram_disk():
    print("[*] RAM ortamı içindeki dosyalar temizleniyor...")
    try:
        for item in os.listdir(PHANTOM_PATH):
            item_path = os.path.join(PHANTOM_PATH, item)
            if os.path.isfile(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
        print("[+] RAM içeriği silindi.")
    except Exception as e:
        print(f"[!] RAM içeriği silinemedi: {str(e)}")

def unmount_ram_disk():
    print("[*] PhantomDisk RAM ortamı kaldırılıyor...")
    try:
        subprocess.check_call(["umount", PHANTOM_PATH])
        print("[+] PhantomDisk başarıyla kaldırıldı.")
    except subprocess.CalledProcessError as e:
        print(f"[X] Unmount başarısız: {e}")

def main():
    print("=== PhantomDestroyer Başlatılıyor ===")
    verify_env()
    wipe_ram_disk()
    time.sleep(1)
    unmount_ram_disk()
    print("[✔] PhantomDisk ortamı başarıyla yok edildi. Sistem artık temiz.")

if __name__ == "__main__":
    main()
