#!/usr/bin/env python3
"""
PhantomDisk - AI Davranış Monitörü
Geliştirici: burakcanbalta | 2025
Amaç: Shell komut geçmişine göre kullanıcı davranışlarını analiz ederek risk puanı üretmek.
"""

import os
import sys
import pandas as pd
from datetime import datetime
from collections import Counter
from sklearn.ensemble import IsolationForest

PHANTOM_PATH = "/mnt/phantomdisk"
LOG_FILE = os.path.join(PHANTOM_PATH, "phantom_shell.log")
REPORT_FILE = os.path.join(PHANTOM_PATH, "ai_anomaly_report.txt")

def parse_log():
    if not os.path.exists(LOG_FILE):
        print("[!] Shell logu bulunamadı.")
        sys.exit(1)

    timestamps = []
    commands = []
    with open(LOG_FILE, "r") as f:
        for line in f:
            if line.startswith("["):
                try:
                    ts, cmd = line.split("] $ ")
                    ts = ts.strip("[")
                    timestamps.append(datetime.strptime(ts, "%Y-%m-%d %H:%M:%S"))
                    commands.append(cmd.strip())
                except:
                    continue

    return pd.DataFrame({
        "timestamp": timestamps,
        "command": commands
    })

def extract_features(df):
    df = df.sort_values("timestamp")
    df["delta"] = df["timestamp"].diff().dt.total_seconds().fillna(0)
    df["is_repeat"] = df.duplicated("command").astype(int)
    return df

def score_behavior(df):
    # Basit özellikler
    avg_delta = df["delta"].mean()
    repeat_ratio = df["is_repeat"].mean()
    unique_cmds = df["command"].nunique()
    total_cmds = len(df)

    score = 0
    if avg_delta < 2:
        score += 40
    if repeat_ratio > 0.5:
        score += 30
    if total_cmds > 25:
        score += 20
    if unique_cmds < 5:
        score += 10

    verdict = "NORMAL"
    if score >= 50:
        verdict = "ŞÜPHELİ DAVRANIŞ"
    if score >= 75:
        verdict = "MUHTEMEL SALDIRGANLIK"

    return score, verdict

def save_report(score, verdict, df):
    with open(REPORT_FILE, "w") as f:
        f.write("=== Phantom AI Anomali Raporu ===\n")
        f.write(f"Toplam Komut: {len(df)}\n")
        f.write(f"Ortalama Süre: {df['delta'].mean():.2f} sn\n")
        f.write(f"Tekrar Oranı: {df['is_repeat'].mean():.2f}\n")
        f.write(f"Risk Skoru: {score} / 100\n")
        f.write(f"Sonuç: {verdict}\n")
    print(f"[+] AI davranış raporu oluşturuldu: {REPORT_FILE}")

def main():
    print("=== Phantom AI Monitor Başlatılıyor ===")
    df = parse_log()
    df = extract_features(df)
    score, verdict = score_behavior(df)
    save_report(score, verdict, df)

if __name__ == "__main__":
    main()
