#!/usr/bin/env python3
"""
PhantomDisk - RAM Ağ Trafiği Dinleyici
Geliştirici: burakcanbalta | 2025
Amaç: Sistem ağ trafiğini RAM ortamında sessizce kaydetmek (.pcap formatında).
Kullanım: Red Team, siber güvenlik eğitimi, anomali analizleri
"""

import os
import sys
import time
from scapy.all import sniff, wrpcap

# RAM ortamı ve pcap dosyası yolu
PHANTOM_PATH = "/mnt/phantomdisk"
PCAP_FILE = os.path.join(PHANTOM_PATH, "capture.pcap")
CAPTURE_DURATION = 60  # saniye (değiştirilebilir)

def verify_env():
    if not os.path.ismount(PHANTOM_PATH):
        print("[X] Phantom ortamı bulunamadı. Lütfen önce 'phantom_init.py' çalıştırın.")
        sys.exit(1)

def start_sniffer(interface="eth0", duration=CAPTURE_DURATION):
    print(f"[*] {interface} arayüzünde {duration} saniye boyunca paket dinleniyor...")
    try:
        packets = sniff(iface=interface, timeout=duration)
        wrpcap(PCAP_FILE, packets)
        print(f"[+] Yakalanan trafik RAM ortamına kaydedildi: {PCAP_FILE}")
        print(f"[+] Toplam paket sayısı: {len(packets)}")
    except PermissionError:
        print("[!] Root yetkisi gereklidir. 'sudo' ile çalıştırmayı deneyin.")
        sys.exit(1)
    except Exception as e:
        print(f"[X] Sniffer başlatılamadı: {str(e)}")
        sys.exit(2)

def main():
    print("=== PhantomSniffer Başlatılıyor ===")
    verify_env()
    interface = input("Dinlenecek ağ arayüzü (varsayılan: eth0): ").strip()
    if interface == "":
        interface = "eth0"
    duration = input("Dinleme süresi (saniye) [varsayılan: 60]: ").strip()
    try:
        duration = int(duration) if duration else CAPTURE_DURATION
    except ValueError:
        duration = CAPTURE_DURATION

    start_sniffer(interface, duration)

if __name__ == "__main__":
    main()
