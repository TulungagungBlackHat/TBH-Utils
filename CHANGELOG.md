# Changelog

## Unreleased

- Ecosystem standardization: SECURITY.md, CONTRIBUTING.md, requirements, CI smoke checks.

## 1.0.0 (2026-09-18)

- Initial stable single-tool release (educational, authorized-use only).

## [3.0.0] - 2026-10-10
### Added
- JWT inspection (alg=none & expiry flags, no signature verify)
- hex encode/decode, rot13, HMAC-SHA256
- stdin support (-t -), graceful decode errors
- Unified TBH v3 CLI: --version, --json, --no-color
- Exit codes for pipelines (0 ok, 1 finding, 2 error)
- Consistent JSON report schema
- Proper exception handling, honest versioning
