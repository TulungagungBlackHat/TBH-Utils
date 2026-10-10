# TBH-Utils

<p align="center">
  <a href="https://github.com/TulungagungBlackHat/TBH-Utils/actions/workflows/ci.yml"><img src="https://github.com/TulungagungBlackHat/TBH-Utils/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <img src="https://img.shields.io/badge/license-MIT-red.svg" alt="License">
  <img src="https://img.shields.io/badge/python-3.8%2B-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/type-utility-black.svg" alt="Utility">
</p>

Everyday encoders and hashes a hunter reaches for mid-engagement — QR, Base64, URL encoding, MD5/SHA-256, and string counting in one file.

Part of the [Tulungagung Black Hat](https://github.com/TulungagungBlackHat) toolset.

## Actions

| Action | What it does |
|--------|--------------|
| `qr` | Generate a QR code image from text (`qrcode[pil]` needed) |
| `b64e` | Base64 encode |
| `b64d` | Base64 decode |
| `urle` | URL percent-encode |
| `urld` | URL percent-decode |
| `hash` | MD5 + SHA-256 digests |
| `count` | Character / word / line count |

## Install

```bash
git clone https://github.com/TulungagungBlackHat/TBH-Utils
cd TBH-Utils
pip install -r requirements.txt
# optional, for QR codes:
pip install "qrcode[pil]"
```

## Usage

```
usage: utils.py [-h] -t TEXT [--json JSON] {qr,b64e,b64d,urle,urld,hash,count}
```

### Examples

```bash
python3 utils.py b64e -t "admin:password"
python3 utils.py b64d -t "YWRtaW46cGFzc3dvcmQ="
python3 utils.py hash -t "session-token" --json out.json
python3 utils.py urle -t "https://example.com/?q=hello world"
python3 utils.py qr -t "https://example.com"
```

## Sample Output

```
$ python3 utils.py hash -t "test"
MD5: 098f6bcd4621d373cade4e832627b4f6
SHA256: 9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08
[✓] JSON: out.json
```

## Authorized Use Only

Utility functions operate on text you provide — but what you decode or encode is your responsibility. Stay within authorized engagements. See [SECURITY.md](SECURITY.md).

## Related Tools

- [TBH-PassStrength](https://github.com/TulungagungBlackHat/TBH-PassStrength) — password strength analysis
- [TBH-JSLeak](https://github.com/TulungagungBlackHat/TBH-JSLeak) — secrets found in JS often need decoding

## License

[MIT](LICENSE) — Tulungagung Black Hat, East Java, Indonesia. Always Smile :)
