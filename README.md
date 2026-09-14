# TBH-Utils - Tools Berguna untuk Semua Orang

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Useful-Untuk%20Semua-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Safe-100%25-orange?style=for-the-badge">
</p>

> **Bukan cuma untuk hacker** - QR, Base64, URL Encode, Hash, Hitung kata - berguna untuk pelajar, admin, semua orang.

Oleh **uchil404 | Tulungagung Black Hat**

## ✨ Features
- 📱 **QR Generator** - `qr` bikin QR code jadi `qrcode.png`
- 🔐 **Base64** - `b64e`/`b64d` encode/decode
- 🔗 **URL Encode** - `urle`/`urld`
- #️⃣ **Hash** - `hash` MD5 + SHA256
- 🔢 **Count** - `count` hitung char/word/line

## 📦 Install
```bash
git clone https://github.com/TulungagungBlackHat/TBH-Utils
cd TBH-Utils
pip install qrcode[pil]
```

## 🚀 Usage
```bash
python3 utils.py qr -t "https://tulungagungblackhat.github.io"
python3 utils.py b64e -t "halo dunia"
python3 utils.py b64d -t "aGFsbyBkdW5pYQ=="
python3 utils.py hash -t "password123"
python3 utils.py count -t "Halo dunia dari Tulungagung"
python3 utils.py urle -t "https://example.com/a b"
```

## 👥 TBH
Tulungagung Black Hat - Always Smile :)

## 📄 License
MIT
