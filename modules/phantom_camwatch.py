#!/usr/bin/env python3
"""
PhantomDisk - Kamera Takipçisi (CamWatch)
Geliştirici: burakcanbalta | 2025
Amaç: Kamera aktif hale gelirse RAM ortamını anında yok etmek.
"""

import cv2
import time
import subprocess
import os

DESTROYER = "phantom_destroyer.py"
CHECK_INTERVAL = 5  # saniye

def is_camera_active():
    try:
        cap = cv2.VideoCapture(0)
        if cap is None or not cap.isOpened():
            return False
        ret, frame = cap.read()
        cap.release()
        return ret and frame is not None
    except Exception:
        return False

def monitor_camera():
    print("=== PhantomCamWatch Başlatıldı ===")
    while True:
        if is_camera_active():
            print("[!] Kamera ALGILANDI! RAM ortamı yok ediliyor...")
            subprocess.call(["python3", DESTROYER])
            break
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    try:
        monitor_camera()
    except KeyboardInterrupt:
        print("[*] CamWatch sonlandırıldı.")
