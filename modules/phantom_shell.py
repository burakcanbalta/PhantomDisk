#!/usr/bin/env python3
"""
PhantomDisk - RAM Terminali
Geliştirici: burakcanbalta | 2025
Amaç: RAM disk içerisinde çalışan, iz bırakmayan geçici terminal ortamı sağlamak.
"""

import os
import subprocess
import sys
import time

# Phantom ortam yolu (phantom_init.py'de oluşturulmuştu)
PHANTOM_PATH = "/mnt/phantomdisk"
LOG_FILE = os.path.join(PHANTOM_PATH, "phantom_shell.log")

def verify_phantom_env():
    if not os.path.ismount(PHANTOM_PATH):
        print("[X] Phantom ortamı bulunamadı. Lütfen önce 'phantom_init.py' dosyasını çalıştırın.")
        sys.exit(1)

def execute_command(cmd):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        output = result.stdout + result.stderr
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        
        with open(LOG_FILE, "a") as log:
            log.write(f"[{timestamp}] $ {cmd}\n")
            log.write(output + "\n")

        print(output.strip())

    except Exception as e:
        print(f"[!] Komut çalıştırılırken hata oluştu: {str(e)}")

def interactive_shell():
    print("=== PhantomShell Başlatıldı (RAM Terminali) ===")
    print("Çıkmak için 'exit' veya 'quit' yazın.")
    while True:
        try:
            cmd = input("phantom> ").strip()
            if cmd.lower() in ["exit", "quit"]:
                print("[*] PhantomShell sonlandırılıyor...")
                break
            if cmd == "":
                continue
            execute_command(cmd)
        except KeyboardInterrupt:
            print("\n[!] Ctrl+C algılandı. Çıkmak için 'exit' yaz.")
        except EOFError:
            break

def main():
    verify_phantom_env()
    interactive_shell()

if __name__ == "__main__":
    main()
