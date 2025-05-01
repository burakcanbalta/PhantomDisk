#!/usr/bin/env python3
"""
PhantomDisk - Kamera Açıldığında Sahte Ekran (CamPhish)
Geliştirici: burakcanbalta | 2025
Amaç: Kamera aktif olduğunda sistemi kullanıyor gibi gösteren bir ekran simülasyonu oluşturmak.
"""

import cv2
import time
import tkinter as tk
import threading

def fake_display():
    root = tk.Tk()
    root.title("Sistem Güvenlik Paneli")
    root.geometry("600x300")
    root.configure(bg="black")
    msg = "GÜVENLİK DURUMU: Sistem izleniyor.\nİzinsiz müdahale tespit edildi.\nYönetici ile iletişime geçin."
    label = tk.Label(root, text=msg, fg="lime", bg="black", font=("Courier", 14), justify="center")
    label.pack(expand=True)
    root.mainloop()

def camera_detector():
    while True:
        try:
            cap = cv2.VideoCapture(0)
            if cap is None or not cap.isOpened():
                time.sleep(5)
                continue
            ret, frame = cap.read()
            cap.release()
            if ret:
                print("[!] Kamera ALGILANDI → sahte ekran aktif.")
                t = threading.Thread(target=fake_display)
                t.start()
                break
        except:
            pass
        time.sleep(5)

if __name__ == "__main__":
    print("=== PhantomCamPhish Başladı ===")
    camera_detector()
