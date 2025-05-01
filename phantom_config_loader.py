#!/usr/bin/env python3
"""
PhantomDisk - Konfigürasyon Yükleyici
"""

import json
import os

CONFIG_PATH = "phantom_config.json"

def load_config():
    if not os.path.exists(CONFIG_PATH):
        raise FileNotFoundError("phantom_config.json bulunamadı!")
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)

# Kullanım örneği:
# config = load_config()
# print(config["ram_size"])
