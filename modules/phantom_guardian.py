#!/usr/bin/env python3
"""
PhantomDisk - RAM Ortamı Koruyucu ve Otomatik Yok Edici
Geliştirici: burakcanbalta | 2025
Amaç: USB çıkarma, süre dolması veya kullanıcı hareketsizliği gibi durumlarda RAM ortamını güvenli şekilde yok etmek.
"""

import os
import subprocess
import sys
import time
import psutil
from threading import Thread

# USB takip (pyudev)
try:
    import pyudev
    HAS_UDEV = True
except ImportError:
    HAS_UDEV = False

PHANTOM_PATH = "/mnt/phantomdisk"
DESTROYER_PATH = "phantom_destroyer.py"
AUTO_KILL_AFTER = 900  # 15 dakika (saniye)
IDLE_LIMIT = 180       # 3 dakika

def call_destroyer():
    print("[!] Tetikleyici algılandı! RAM ortamı yok ediliyor...")
    subprocess.call(["python3", DESTROYER_PATH])
    sys.exit(0)

def watch_usb(target_label="PhantomKey"):
    if not HAS_UDEV:
        return
    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)
    monitor.filter_by(subsystem='block')

    for device in iter(monitor.poll, None):
        if device.action == "remove" and target_label in str(device):
            call_destroyer()

def watch_idle_time():
    last_input_time = time.time()
    while True:
        idle = psutil.cpu_times().idle
        if idle > IDLE_LIMIT:
            call_destroyer()
        time.sleep(5)

def watch_timer():
    time.sleep(AUTO_KILL_AFTER)
    call_destroyer()

def verify_env():
    if not os.path.ismount(PHANTOM_PATH):
        print("[X] Phantom ortamı aktif değil.")
        sys.exit(0)

def main():
    print("=== PhantomGuardian Başlatıldı ===")
    verify_env()
    
    # Süre bazlı otomatik yok etme
    Thread(target=watch_timer, daemon=True).start()

    # USB izleme
    if HAS_UDEV:
        Thread(target=watch_usb, daemon=True).start()
    else:
        print("[!] pyudev bulunamadı, USB takibi devre dışı.")

    # Kullanıcı etkinliği izleme
    Thread(target=watch_idle_time, daemon=True).start()

    print("[*] Phantom ortamı korunuyor. Tetikleyici bekleniyor...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("[*] Kullanıcı tarafından sonlandırıldı.")
        sys.exit(0)

if __name__ == "__main__":
    main()
