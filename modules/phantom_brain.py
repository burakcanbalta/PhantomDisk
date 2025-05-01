#!/usr/bin/env python3
"""
PhantomDisk - AI Tabanlı Tepki Motoru (PhantomBrain)
Geliştirici: burakcanbalta | 2025
Amaç: Kullanıcı davranışlarını, RAM kullanımını ve AI skorunu izleyerek sistemi gerektiğinde otomatik yönlendirmek.
"""

import os
import time
import subprocess
import json
import psutil
from phantom_config_loader import load_config

config = load_config()
PHANTOM_PATH = config.get("mount_point", "/mnt/phantomdisk")
SHELL_LOG = os.path.join(PHANTOM_PATH, config.get("shell_log", "phantom_shell.log"))
AI_THRESHOLD = config.get("ai_threshold", {"suspicious": 50, "attack": 75})
DESTROYER_PATH = "modules/phantom_destroyer.py"
SAFEVAULT_PATH = "modules/phantom_safevault.py"
CHECK_INTERVAL = 15  # saniye

def get_command_count():
    try:
        with open(SHELL_LOG, "r") as f:
            return len([line for line in f if "] $" in line])
    except:
        return 0

def get_ai_score():
    report_path = os.path.join(PHANTOM_PATH, "ai_anomaly_report.txt")
    try:
        with open(report_path, "r") as f:
            for line in f:
                if "Risk Skoru" in line:
                    score = int(line.strip().split(":")[1].split("/")[0])
                    return score
    except:
        return 0
    return 0

def phantom_react():
    while True:
        score = get_ai_score()
        cmd_count = get_command_count()
        ram_percent = psutil.virtual_memory().percent

        print(f"[*] AI Skor: {score} | Komut: {cmd_count} | RAM: {ram_percent}%")

        if score >= AI_THRESHOLD["attack"]:
            print("[!] AI seviyesi çok yüksek! Ortam yok ediliyor.")
            subprocess.call(["python3", DESTROYER_PATH])
            break
        elif score >= AI_THRESHOLD["suspicious"] or ram_percent > 90:
            print("[!] Tehlike algılandı! Güvenli yedekleme başlatılıyor.")
            subprocess.call(["python3", SAFEVAULT_PATH])

        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    print("=== PhantomBrain Başlatıldı ===")
    phantom_react()
