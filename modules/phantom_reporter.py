#!/usr/bin/env python3
"""
PhantomDisk - RAM Tabanlı Rapor Oluşturucu
Geliştirici: burakcanbalta | 2025
Amaç: Phantom ortamında yapılan işlemleri HTML/PDF formatında özetlemek.
"""

import os
import sys
import time
from datetime import datetime
from platform import platform, node
from fpdf import FPDF

# RAM ortamı ve log dosyaları
PHANTOM_PATH = "/mnt/phantomdisk"
SHELL_LOG = os.path.join(PHANTOM_PATH, "phantom_shell.log")
PCAP_FILE = os.path.join(PHANTOM_PATH, "capture.pcap")
REPORT_FILE = os.path.join(PHANTOM_PATH, "phantom_report.pdf")

class PhantomReport(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "PhantomDisk - Geçici RAM Raporu", ln=1, align="C")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Sayfa {self.page_no()}", align="C")

    def add_section(self, title, content):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, ln=1)
        self.set_font("Arial", "", 11)
        self.multi_cell(0, 8, content)
        self.ln(5)

def read_log_file(path):
    if os.path.exists(path):
        with open(path, "r") as file:
            return file.read()
    return "Dosya bulunamadı veya içerik yok."

def generate_report():
    pdf = PhantomReport()
    pdf.add_page()

    pdf.add_section("Rapor Zamanı", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    pdf.add_section("Sistem Bilgisi", f"Sistem: {platform()}\nMakine: {node()}")
    pdf.add_section("Komut Geçmişi", read_log_file(SHELL_LOG))
    pdf.add_section("Paket Yakalama (PCAP)", "Ağ trafiği başarıyla RAM ortamına kaydedildi." if os.path.exists(PCAP_FILE) else "PCAP dosyası bulunamadı.")
    
    pdf.output(REPORT_FILE)
    print(f"[+] Rapor oluşturuldu: {REPORT_FILE}")

def verify_env():
    if not os.path.ismount(PHANTOM_PATH):
        print("[X] Phantom ortamı bulunamadı. Lütfen önce 'phantom_init.py' çalıştırın.")
        sys.exit(1)

def main():
    print("=== PhantomReporter Başlatılıyor ===")
    verify_env()
    generate_report()

if __name__ == "__main__":
    main()
