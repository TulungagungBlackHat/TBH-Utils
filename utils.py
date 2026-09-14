#!/usr/bin/env python3
# TBH-Utils - Tools Berguna untuk Semua Orang
# Tulungagung Black Hat - uchil404 | 100% Aman & Berguna

import base64, urllib.parse, hashlib, re, argparse, sys, json
try:
    import qrcode
    HAS_QR = True
except:
    HAS_QR = False

BANNER = """\033[96m╔════════════════════════════════════╗
\033[96m║ \033[97mTBH-Utils \033[96m- Berguna Untuk Semua      \033[96m║
\033[96m║ \033[90mTulungagung Black Hat | uchil404 \033[96m║
\033[96m╚════════════════════════════════════╝\033[0m"""

def qr(text):
    if not HAS_QR:
        print("\033[91m[!] Butuh: pip install qrcode[pil]\033[0m"); return
    img = qrcode.make(text)
    img.save("qrcode.png")
    print(f"\033[92m[✓] QR saved: qrcode.png untuk '{text[:30]}'\033[0m")

def b64e(t): print(f"\033[92mBase64 Encode: {base64.b64encode(t.encode()).decode()}\033[0m")
def b64d(t): 
    try: print(f"\033[92mBase64 Decode: {base64.b64decode(t).decode()}\033[0m")
    except: print("\033[91m[!] Base64 invalid\033[0m")
def url_e(t): print(f"\033[92mURL Encode: {urllib.parse.quote(t)}\033[0m")
def url_d(t): print(f"\033[92mURL Decode: {urllib.parse.unquote(t)}\033[0m")
def hashit(t): 
    print(f"\033[92mMD5: {hashlib.md5(t.encode()).hexdigest()}\033[0m")
    print(f"\033[92mSHA256: {hashlib.sha256(t.encode()).hexdigest()}\033[0m")
def count(t):
    print(f"\033[96mChars: {len(t)} | Words: {len(t.split())} | Lines: {t.count(chr(10))+1}\033[0m")

def main():
    print(BANNER)
    parser = argparse.ArgumentParser(description="TBH-Utils - Berguna Untuk Semua")
    parser.add_argument("action", choices=["qr","b64e","b64d","urle","urld","hash","count"], help="qr/b64e/b64d/urle/urld/hash/count")
    parser.add_argument("-t","--text", required=True, help="Text")
    args = parser.parse_args()
    if args.action == "qr": qr(args.text)
    elif args.action == "b64e": b64e(args.text)
    elif args.action == "b64d": b64d(args.text)
    elif args.action == "urle": url_e(args.text)
    elif args.action == "urld": url_d(args.text)
    elif args.action == "hash": hashit(args.text)
    elif args.action == "count": count(args.text)

if __name__ == "__main__":
    main()
