#!/usr/bin/env python3
"""
PhantomDisk - RAM Tabanlı Geçici Çalışma Ortamı Başlatıcı
Geliştirici: burakcanbalta | 2025
Amaç: Bu script, sistemde iz bırakmayan, yalnızca RAM üzerinde çalışan geçici bir klasör oluşturur.
Kullanım: Eğitim, Red Team simülasyonu, forensics, hassas veri işleme
"""

import os
import subprocess
import tempfile
import shutil
import sys
import time

# Ortam ayarları
MOUNT_POINT = "/mnt/phantomdisk"
RAM_SIZE = "512M"  # Kullanılacak RAM alanı (değiştirilebilir)

def check_root():
    if os.geteuid() != 0:
        print("[!] Bu script root yetkisi gerektirir. Lütfen 'sudo' ile çalıştırın.")
        sys.exit(1)

def create_ram_disk():
    # Eğer mount noktası varsa, önceden unmount et
    if os.path.ismount(MOUNT_POINT):
        print(f"[*] Mevcut RAM ortamı bulundu: {MOUNT_POINT} - Unmount ediliyor...")
        subprocess.call(["umount", MOUNT_POINT])

    # Mount klasörü oluşturuluyor
    if not os.path.exists(MOUNT_POINT):
        os.makedirs(MOUNT_POINT)

    # tmpfs ile RAM ortamı mount edilir
    print(f"[*] {RAM_SIZE} boyutunda RAM ortamı oluşturuluyor: {MOUNT_POINT}")
    cmd = ["mount", "-t", "tmpfs", "-o", f"size={RAM_SIZE}", "tmpfs", MOUNT_POINT]
    result = subprocess.call(cmd)

    if result == 0:
        print(f"[+] PhantomDisk RAM ortamı başarıyla başlatıldı: {MOUNT_POINT}")
    else:
        print("[X] RAM ortamı oluşturulamadı. Yetki veya sistem hatası olabilir.")
        sys.exit(2)

def create_log_file():
    log_path = os.path.join(MOUNT_POINT, "phantom_init.log")
    with open(log_path, "w") as log:
        log.write(f"PhantomDisk başlatıldı - Zaman: {time.ctime()}\n")
        log.write(f"RAM ortamı boyutu: {RAM_SIZE}\n")
        log.write(f"Mount noktası: {MOUNT_POINT}\n")
    print(f"[+] Başlangıç log'u RAM içinde oluşturuldu: {log_path}")

def main():
    print("=== PhantomDisk Başlatıcı ===")
    check_root()
    create_ram_disk()
    create_log_file()
    print("[✔] RAM ortamı kullanıma hazır.")

if __name__ == "__main__":
    main()
