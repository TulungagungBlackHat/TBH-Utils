#!/usr/bin/env python3
# TBH-Utils v2.0 Pro - JSON + Batch
import base64, urllib.parse, hashlib, argparse, sys, json
try:
    import qrcode
    HAS_QR=True
except: HAS_QR=False

BANNER = """\033[96m╔════════════════════════════════════╗
\033[96m║ \033[97mTBH-Utils v2.0 Pro \033[96m- JSON/Batch      \033[96m║
\033[96m║ \033[90mTulungagung Black Hat | uchil404 \033[96m║
\033[96m╚════════════════════════════════════╝\033[0m"""

def qr(text):
    if not HAS_QR: print("[!] pip install qrcode[pil]"); return
    img=qrcode.make(text); img.save("qrcode.png"); print(f"[✓] QR saved: qrcode.png")

def main():
    print(BANNER)
    parser=argparse.ArgumentParser(description="v2.0 Pro")
    parser.add_argument("action",choices=["qr","b64e","b64d","urle","urld","hash","count"])
    parser.add_argument("-t","--text",required=True,help="Text")
    parser.add_argument("--json",help="Save JSON")
    args=parser.parse_args()
    result={"action":args.action,"input":args.text}
    if args.action=="qr": qr(args.text); result["output"]="qrcode.png"
    elif args.action=="b64e": result["output"]=base64.b64encode(args.text.encode()).decode(); print(f"Encode: {result['output']}")
    elif args.action=="b64d": result["output"]=base64.b64decode(args.text).decode(); print(f"Decode: {result['output']}")
    elif args.action=="urle": result["output"]=urllib.parse.quote(args.text); print(f"URLE: {result['output']}")
    elif args.action=="urld": result["output"]=urllib.parse.unquote(args.text); print(f"URLD: {result['output']}")
    elif args.action=="hash": result["md5"]=hashlib.md5(args.text.encode()).hexdigest(); result["sha256"]=hashlib.sha256(args.text.encode()).hexdigest(); print(f"MD5: {result['md5']}\nSHA256: {result['sha256']}")
    elif args.action=="count": result["chars"]=len(args.text); result["words"]=len(args.text.split()); print(f"Chars: {result['chars']} Words: {result['words']}")
    if args.json:
        open(args.json,'w').write(json.dumps(result,indent=2)); print(f"[✓] JSON: {args.json}")

if __name__=="__main__": main()
