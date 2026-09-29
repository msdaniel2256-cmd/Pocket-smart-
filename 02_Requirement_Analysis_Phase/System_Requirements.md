# System Requirements Specification

## 1. Software Environment Requirements

### 1.1 Backend Runtime
- **Python**: Version `3.10.x` or `3.11.x` (Recommended: Python 3.11 for optimal async performance).
- **ASGI Web Server**: `uvicorn>=0.28.0` with `fastapi>=0.110.0`.
- **Operating Systems**: 
  - Windows 10 / 11 (tested and verified on Windows AMD64)
  - Linux (Ubuntu 20.04+, Debian 11+, RHEL 8+)
  - macOS (Monterey 12.0+)

### 1.2 Python Dependencies (requirements.txt)
| Package | Version Range | Purpose |
|---|---|---|
| `fastapi` | `>=0.110.0` | Asynchronous web framework & API routing |
| `uvicorn` | `>=0.28.0` | High-performance ASGI production server |
| `pydantic` | `>=2.6.0` | Data modeling & request/response validation |
| `python-multipart` | `>=0.0.9` | Form data & image file upload handling |
| `jinja2` | `>=3.1.3` | Server-rendered HTML templating engine |
| `python-jose[cryptography]` | `>=3.3.0` | JWT token creation, signing, and verification |
| `passlib[bcrypt]` | `>=1.7.4` | Password hashing integration |
| `bcrypt` | `>=4.0.0` | Secure cryptographic password hashing |
| `pillow` | `>=10.0.0` | Image processing, resizing, and color quantizing |
| `google-generativeai` | `>=0.4.0` | Google Gemini 1.5 Flash SDK client |
| `python-dotenv` | `>=1.0.0` | Environment variable management from `.env` |
| `requests` | `>=2.31.0` | Synchronous HTTP calls for testing & utilities |
| `email-validator` | `>=2.0.0` | Robust RFC-compliant email address validation |

### 1.3 Client Browser Compatibility
- Google Chrome (v90+)
- Mozilla Firefox (v88+)
- Microsoft Edge (v90+)
- Apple Safari (v14+)
- Mobile Browsers: Chrome for Android, Safari for iOS

---

## 2. Hardware Requirements

### Minimum Specifications (Development & Local Hosting)
- **Processor**: Dual-Core x86_64 or ARM64 CPU (1.8 GHz+)
- **RAM**: 1 GB available RAM (FastAPI + Python runtime consumes ~65 MB)
- **Disk Storage**: 500 MB free disk space for application files, uploads, and dependencies
- **Network**: Standard broadband connection (for optional Gemini API calls and package installations; offline fallback works without internet)

### Recommended Production Specifications
- **Processor**: Quad-Core CPU (2.4 GHz+)
- **RAM**: 2 GB - 4 GB RAM
- **Disk Storage**: 5 GB SSD storage
- **Network**: Low-latency outbound HTTPS access to `generativelanguage.googleapis.com`

---

## 3. Configuration & Environment Variables

| Variable | Type | Default Value | Description |
|---|---|---|---|
| `GOOGLE_API_KEY` | String | `None` | Google Gemini 1.5 Flash API Key |
| `GEMINI_API_KEY` | String | `None` | Secondary alias for Google Gemini API key |
| `SECRET_KEY` | String | `pocketsmart_jwt_super_secret_key_2026_secure` | Secret string for HMAC-SHA256 JWT signing |
| `ALGORITHM` | String | `HS256` | JWT signature algorithm |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Integer | `60` | JWT token lifespan in minutes |
| `HOST` | String | `0.0.0.0` | Network binding interface |
| `PORT` | Integer | `8000` | Network port for HTTP web traffic |
