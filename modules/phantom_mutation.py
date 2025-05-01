#!/usr/bin/env python3
"""
PhantomDisk - Polimorfik Modül Oluşturucu
Geliştirici: burakcanbalta | 2025
Amaç: Phantom modüllerinin adlarını ve bazı içeriklerini rastgele değiştirerek stealth davranış üretmek.
"""

import os
import shutil
import random
import string
from datetime import datetime

MODULES_PATH = "/mnt/phantomdisk/modules"
MUTATED_PATH = "/mnt/phantomdisk/mutated"
LOG_FILE = os.path.join(MUTATED_PATH, "mutation_log.txt")

def random_name(prefix="mod_", length=5):
    return prefix + ''.join(random.choices(string.ascii_letters + string.digits, k=length)) + ".py"

def mutate_file(original_path, mutated_path):
    with open(original_path, "r") as f:
        content = f.readlines()

    new_lines = []
    for line in content:
        # Random dummy comment ekle
        if random.random() < 0.2:
            new_lines.append(f"# {random.choice(['TODO', 'AUTO-GEN', 'FIXME'])} {random.randint(1,9999)}\n")
        new_lines.append(line)

    with open(mutated_path, "w") as f:
        f.writelines(new_lines)

def log_mutation(mapping):
    with open(LOG_FILE, "w") as f:
        f.write("=== PhantomDisk Mutasyon Logu ===\n")
        f.write(f"Tarih: {datetime.now()}\n\n")
        for orig, mutated in mapping.items():
            f.write(f"{orig} → {mutated}\n")

def main():
    print("=== PhantomMutation Başlatılıyor ===")

    if not os.path.exists(MUTATED_PATH):
        os.makedirs(MUTATED_PATH)

    module_files = [f for f in os.listdir(MODULES_PATH) if f.endswith(".py")]
    mapping = {}

    for file in module_files:
        orig_path = os.path.join(MODULES_PATH, file)
        new_name = random_name("pmod_")
        mutated_path = os.path.join(MUTATED_PATH, new_name)
        mutate_file(orig_path, mutated_path)
        mapping[file] = new_name

    log_mutation(mapping)
    print(f"[+] {len(mapping)} modül rastgele mutasyona uğratıldı.")
    print(f"[+] Mutasyon logu: {LOG_FILE}")

if __name__ == "__main__":
    main()
