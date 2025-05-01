
#!/usr/bin/env python3
"""
PhantomDisk Final - Tüm Sistemi Yöneten Ana Script
Geliştirici: burakcanbalta | 2025
Amaç: PhantomDisk modüllerini tek merkezden çalıştırmak, RAM ortamı üzerinde iz bırakmadan işlem yapmak.
"""

import os
import threading
import subprocess
import time
import sys

# Ayar dosyasını yükle
try:
    from phantom_config_loader import load_config
    config = load_config()
except Exception as e:
    print(f"[X] Ayar dosyası yüklenemedi: {str(e)}")
    sys.exit(1)

# Genel ayarlar
MOUNT_POINT = config.get("mount_point", "/mnt/phantomdisk")
DESTROYER_PATH = "modules/phantom_destroyer.py"

# Modüller (modül adı → yol)
MODULES = {
    "phantom_shell": "modules/phantom_shell.py",
    "phantom_safevault": "modules/phantom_safevault.py",
    "phantom_guardian": "modules/phantom_guardian.py",
    "phantom_camwatch": "modules/phantom_camwatch.py",
    "phantom_ai_monitor": "modules/phantom_ai_monitor.py",
    "phantom_tunnel": "modules/phantom_tunnel.py",
    "phantom_fallback": "modules/phantom_fallback.py",
    "phantom_ghostlogin": "modules/phantom_ghostlogin.py",
    "phantom_brain": "modules/phantom_brain.py",
    "phantom_antiav": "modules/phantom_antiav.py",
    "phantom_autopayload": "modules/phantom_autopayload.py",
    "phantom_c2sync": "modules/phantom_c2sync.py",
    "phantom_camphish": "modules/phantom_camphish.py"
}

# Modül çalıştırıcı
def start_module(script_path):
    def run():
        try:
            subprocess.call(["python3", script_path])
        except Exception as e:
            print(f"[!] {script_path} çalıştırılamadı: {e}")
    t = threading.Thread(target=run)
    t.daemon = True
    t.start()

def main():
    print("=== PhantomDisk Final Başlatılıyor ===")
    print("[*] RAM ortamı hazırlanıyor...")

    # RAM ortamını başlat
    subprocess.call(["python3", "modules/phantom_init.py"])

    print("[*] Modüller başlatılıyor...")

    for name, path in MODULES.items():
        print(f"  → {name} başlatılıyor...")
        start_module(path)
        time.sleep(0.5)  # küçük gecikme

    print("[✔] Tüm sistem RAM ortamında aktif! Çıkmak için Ctrl+C")
    
    # Sonsuz bekleyiş (çıkış olursa yok et)
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[!] Çıkış algılandı. RAM ortamı yok ediliyor...")
        subprocess.call(["python3", DESTROYER_PATH])
        print("[✔] PhantomDisk Final kapatıldı.")

if __name__ == "__main__":
    main()
