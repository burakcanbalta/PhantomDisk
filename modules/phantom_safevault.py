#!/usr/bin/env python3
"""
PhantomDisk - Güvenli Yedekleme Modülü (SafeVault)
Geliştirici: burakcanbalta | 2025
Amaç: RAM ortamındaki kritik verileri şifreli olarak belirli aralıklarla yedeklemek.
"""

import os
import time
import shutil
from cryptography.fernet import Fernet

PHANTOM_PATH = "/mnt/phantomdisk"
VAULT_PATH = "/tmp/phantom_vault"
KEY_FILE = os.path.join(VAULT_PATH, "vault.key")
BACKUP_INTERVAL = 300  # 5 dakika = 300 saniye

FILES_TO_BACKUP = [
    "phantom_shell.log",
    "capture.pcap",
    "phantom_report.pdf"
]

def ensure_vault():
    if not os.path.exists(VAULT_PATH):
        os.makedirs(VAULT_PATH)

def load_or_create_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as f:
            return f.read()
    else:
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)
        return key

def encrypt_file(filepath, key):
    filename = os.path.basename(filepath)
    try:
        with open(filepath, "rb") as f:
            data = f.read()
        fernet = Fernet(key)
        encrypted = fernet.encrypt(data)
        with open(os.path.join(VAULT_PATH, filename + ".enc"), "wb") as enc_file:
            enc_file.write(encrypted)
        print(f"[+] {filename} dosyası şifreli olarak yedeklendi.")
    except Exception as e:
        print(f"[!] {filename} yedeklenemedi: {str(e)}")

def backup_files(key):
    for filename in FILES_TO_BACKUP:
        path = os.path.join(PHANTOM_PATH, filename)
        if os.path.exists(path):
            encrypt_file(path, key)

def main():
    print("=== PhantomSafeVault Başlatıldı ===")
    ensure_vault()
    key = load_or_create_key()

    try:
        while True:
            print("[*] 5 dakikalık güvenli yedekleme döngüsü başladı...")
            backup_files(key)
            time.sleep(BACKUP_INTERVAL)
    except KeyboardInterrupt:
        print("[*] Güvenli yedekleme durduruldu.")

if __name__ == "__main__":
    main()
