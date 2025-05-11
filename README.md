
# 🧠 PhantomDisk | RAM-Only Stealth Operating Layer
**Geliştirici:** burakcanbalta  
**Yıl:** 2025  
**Kategori:** Red Team, RAM-Based OS Layer, AI-Driven Defense

---

## 🚀 Proje Hakkında
PhantomDisk; yalnızca RAM üzerinde çalışan, hiçbir iz bırakmadan işlem yapan, AI destekli, modüler ve uzaktan yönetilebilir bir "RAM tabanlı operasyon katmanıdır".  
Amaç; sistemde disk kullanılmadan veri işlemek, olay müdahale senaryolarını test etmek, gerçek saldırı simülasyonlarını oluşturmak ve kurumların tehdit algısını artırmaktır.

---

## 🎯 Hedef Kitle

| Kurum/Kuruluş | Kullanım |
|---------------|----------|
| 🛡️ Milli Savunma Bakanlığı | RAM-only casusluk/sızma tespiti için simülasyon sistemi |
| 🔬 Tübitak / Siber Güvenlik Enstitüsü | Akademik araştırma & TEKNOFEST proje sunumu |
| 🏢 Kurumsal Red Team / SOC birimleri | RAM saldırı analiz eğitimi ve güvenlik testi |
| 🧪 Üniversiteler / Siber Güvenlik Bölümleri | Öğrencilere gerçek tehdit modellemesi |
| 🧑‍💻 Penetrasyon Test Uzmanları | Eğitim amaçlı RAM içi exploit senaryoları |

---

## 📦 Kullanım

```bash
pip install -r requirements.txt
sudo python3 PhantomDisk_Final.py
```

> Ctrl+C ile çıkıldığında RAM ortamı tamamen yok edilir.

---

## ⚙️ Modüller ve İşlevleri

### 1. `phantom_init.py`
RAM üzerinde tmpfs ile sanal dosya sistemi oluşturur. Tüm sistem bu alanda çalışır.  
📁 `/mnt/phantomdisk`

### 2. `phantom_shell.py`
RAM ortamı üzerinde çalışan etkileşimli terminal. Logları RAM’e yazar.

### 3. `phantom_sniffer.py`
RAM'de çalışan ağ trafiği dinleyici. Tüm veriyi `capture.pcap` dosyasına kaydeder.

### 4. `phantom_reporter.py`
Sistemdeki loglardan PDF formatında rapor üretir. Raporlar sadece RAM'de tutulur.

### 5. `phantom_destroyer.py`
RAM ortamını güvenli şekilde unmount ederek tüm izleri temizler.

### 6. `phantom_guardian.py`
USB çıkarıldığında, süre dolduğunda veya kullanıcı inaktif kaldığında ortamı otomatik siler.

### 7. `phantom_safevault.py`
RAM ortamını periyodik olarak şifreli yedekleyip disk dışı alana taşır (örn. /tmp).

### 8. `phantom_ai_monitor.py`
Kullanıcı komutlarını analiz eder, şüpheli durumları AI ile tespit eder.

### 9. `phantom_mutation.py`
Sistemdeki modülleri otomatik olarak yeniden adlandırır ve içeriklerini rastgele değiştirerek tespit edilmesini engeller.

### 10. `phantom_fallback.py`
Tüm sistem çökerse bile RAM ortamını zorla unmount eden son çare güvenlik katmanıdır.

### 11. `phantom_camwatch.py`
Kamera aktif hale gelirse ortamı otomatik yok eder (anti-surveillance modu).

### 12. `phantom_tunnel.py`
RAM üzerinden çalışan reverse shell bağlantısı kurar. Tamamen izsiz çalışır.

### 13. `phantom_gui.py`
Tüm modülleri bir arada yönetebileceğiniz görsel kullanıcı arayüzüdür.

### 14. `phantom_config.json`
Tüm sistem ayarları buradan alınır: RAM boyutu, reverse portu, AI eşiği, log dosyaları…

### 15. `phantom_config_loader.py`
Config dosyasını tüm modüllere JSON olarak çeken yardımcı modüldür.

### 16. `phantom_ghostlogin.py`
Sahte sistem giriş ekranı. Kullanıcıdan alınan bilgiler RAM’e kaydedilir (phishing simülasyonu).

### 17. `phantom_brain.py`
AI skorlarına ve RAM kullanımına göre ortamı yedekler veya yok eder. Otomatik içsel tepki sistemidir.

### 18. `phantom_antiav.py`
Sistemin sandbox, VM, AV veya güvenlik yazılımları altında çalışıp çalışmadığını analiz eder. Tespit edilirse ortamı kapatır.

### 19. `phantom_autopayload.py`
RAM üzerinde reverse shell payload’ı üretir: .py, base64, AES-şifreli versiyonlarıyla.

### 20. `phantom_c2sync.py`
Mini Flask tabanlı web paneli: komut gönder, log al, ortamı sil gibi işlemler yapılabilir.

### 21. `phantom_camphish.py`
Kamera açıldığında, ekran yerine sahte bir güvenlik paneli gösterir. Arka planda sistem çalışmaya devam eder.

---

## 🔐 Güvenlik ve Geliştirme Önerileri

- 🔄 RAM snapshot modülü eklenebilir (belge hash'leri vs.)
- 🔥 Process hollowing, LD_PRELOAD, memory loader gibi APT teknikleriyle genişletilebilir
- 🕵️ OSINT entegrasyonu ile hedefe göre davranış farklılığı uygulanabilir
- 📦 Discord bot veya Telegram C2 ile hibrit kontrol geliştirilebilir
- 🧬 AI modeli daha karmaşık hale getirilerek kullanıcı profili çıkarımı yapılabilir

---

## 🧪 PhantomDisk Nerelerde Kullanılır?

| Saha | Amaç |
|------|------|
| Savunma Sanayii | İz bırakmayan eğitim/demo/karantina ortamı |
| Siber Güvenlik Akademileri | Öğrencilere iz bırakmayan sistem analizi eğitimi |
| Kurum içi Red Team/SOC | Gerçek saldırı simülasyonu ve farkındalık oluşturma |

---

## 📄 Lisans & Yasal Uyarı

Bu sistem eğitim ve yetkili güvenlik testleri için tasarlanmıştır.  
Yetkisiz sistemlerde kullanılması yasaktır ve suç teşkil eder.

**© 2025 - burakcanbalta | PhantomDisk**

---
