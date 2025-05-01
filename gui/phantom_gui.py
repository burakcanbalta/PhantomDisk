#!/usr/bin/env python3
"""
PhantomDisk - GUI Kontrol Paneli
Geliştirici: burakcanbalta | 2025
Amaç: PhantomDisk modüllerini görsel arayüz üzerinden başlatmak.
"""

import tkinter as tk
from tkinter import messagebox
import subprocess
import os

MODULES = {
    "🧠 Başlat - RAM Ortamı": "phantom_init.py",
    "💻 Shell (Terminal)": "phantom_shell.py",
    "📡 Sniffer": "phantom_sniffer.py",
    "📄 Rapor Oluştur": "phantom_reporter.py",
    "🔐 AI Anomali Analizi": "phantom_ai_monitor.py",
    "🔁 Mutasyon Motoru": "phantom_mutation.py",
    "💣 Destroyer (Manuel Yok Et)": "phantom_destroyer.py",
    "🧍 Guardian (USB/Süre Tetikleme)": "phantom_guardian.py",
    "📦 Güvenli Yedekleme (SafeVault)": "phantom_safevault.py",
    "🌍 PhantomTunnel (Reverse Shell)": "phantom_tunnel.py"
}

def run_script(script_name):
    try:
        subprocess.Popen(["python3", script_name])
        messagebox.showinfo("Çalıştırıldı", f"{script_name} başlatıldı.")
    except Exception as e:
        messagebox.showerror("Hata", f"Modül çalıştırılamadı: {e}")

def main():
    root = tk.Tk()
    root.title("PhantomDisk Kontrol Paneli")
    root.geometry("400x500")
    root.configure(bg="black")

    tk.Label(root, text="PhantomDisk", font=("Arial", 20, "bold"), fg="lime", bg="black").pack(pady=10)

    for label, script in MODULES.items():
        btn = tk.Button(root, text=label, font=("Arial", 12), fg="white", bg="#1e1e1e",
                        width=40, height=2, command=lambda s=script: run_script(s))
        btn.pack(pady=5)

    tk.Label(root, text="burakcanbalta | 2025", font=("Arial", 8), fg="gray", bg="black").pack(side="bottom", pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
