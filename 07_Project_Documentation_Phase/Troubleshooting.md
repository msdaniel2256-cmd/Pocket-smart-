# Troubleshooting & Diagnostic Guide

This guide addresses common questions, diagnostic commands, and error resolutions for **PocketSmart AI**.

---

## 1. Common Issues & Solutions

### Issue 1: `ModuleNotFoundError: No module named 'jose'` or `'bcrypt'`
- **Symptom**: Python exits on startup with module import errors.
- **Cause**: Packages were installed in a different Python environment or outside the active virtual environment.
- **Resolution**:
  ```powershell
  python -m pip install -r requirements.txt
  ```

---

### Issue 2: `Error: Address already in use (Port 8000)`
- **Symptom**: `OSError: [Errno 10048] error while attempting to bind on address ('0.0.0.0', 8000)`
- **Cause**: An existing instance of Uvicorn or another local service is holding port 8000.
- **Resolution**:
  - Run on another port:
    ```bash
    uvicorn backend.app:app --port 8080
    ```
  - Or terminate the blocking process on Windows:
    ```powershell
    netstat -ano | findstr :8000
    taskkill /PID <PID> /F
    ```

---

### Issue 3: Google Gemini API Rate Limit or Invalid Key
- **Symptom**: Console logs show `[Gemini API fallback] Error: 429 ResourceExhausted` or `API_KEY_INVALID`.
- **Behavior in PocketSmart AI**: The application **automatically and gracefully** switches to its deterministic local Indian pricing engine without crashing.
- **Resolution**: Verify that `GOOGLE_API_KEY` in `.env` has active billing credits and quota enabled. If you prefer to test purely offline, simply leave `GOOGLE_API_KEY=` blank in `.env`.

---

### Issue 4: `401 Unauthorized` on Protected Pages
- **Symptom**: Navigating to `/dashboard`, `/home-planner`, or `/history` immediately redirects to `/login`.
- **Cause**: The 60-minute JWT session token has expired or the browser cookie was deleted.
- **Resolution**: Visit `http://localhost:8000/login` and log in again with credentials (`sai` / `password123`).

---

### Issue 5: Uploaded Image Does Not Appear or Fails Analysis
- **Symptom**: Image upload returns generic styling advice.
- **Cause**: File format is unsupported (must be JPEG, PNG, or WebP) or file exceeds size limits.
- **Resolution**: Ensure the uploaded image is under 10MB in standard JPEG or PNG format. Ensure the `static/uploads/` directory has write permissions.

---

## 2. Health & Diagnostic Checklist

Run these quick one-liner tests in your terminal:

```bash
# 1. Test Server HTTP Status
python -c "import urllib.request; print('Server Status:', urllib.request.urlopen('http://127.0.0.1:8000/').getcode())"

# 2. Run Comprehensive Automated Test Suite
python 06_Project_Testing_Phase/test_suite.py
```
