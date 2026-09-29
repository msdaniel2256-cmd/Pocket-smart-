# Installation & Setup Guide

This guide provides instructions for installing and running **PocketSmart AI** locally on Windows, Linux, or macOS.

---

## 1. Prerequisites
- **Python**: Version `3.10` or `3.11` (verify with `python --version`).
- **pip**: Python package manager (`python -m pip --version`).
- **Git**: (Optional, for cloning repository).

---

## 2. Step-by-Step Installation

### Step 2.1: Clone or Open the Repository
```bash
git clone https://github.com/your-username/pocketsmart-ai.git
cd pocketsmart-ai
```

### Step 2.2: Create a Virtual Environment (Recommended)
On Windows:
```powershell
python -m venv venv
.\venv\Scripts\activate
```

On Linux / macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 2.3: Install Dependencies
```bash
pip install -r requirements.txt
```

Verify that key packages are installed:
```bash
python -c "import fastapi, uvicorn, pydantic, jinja2, jose, bcrypt, PIL; print('All dependencies OK!')"
```

---

## 3. Environment Configuration

1. Copy `.env.example` to create your local `.env`:
   ```bash
   cp .env.example .env
   ```
   *(On Windows Command Prompt: `copy .env.example .env`)*

2. Open `.env` in an editor:
   ```env
   # Google Gemini API Key (Optional)
   # If left blank, PocketSmart AI runs automatically in intelligent offline fallback mode
   GOOGLE_API_KEY=your_gemini_api_key_here

   # Security & Sessions
   SECRET_KEY=pocketsmart_jwt_super_secret_key_2026_secure
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=60

   # Server Configuration
   HOST=0.0.0.0
   PORT=8000
   ```

---

## 4. Running the Application

### Option A: Using the Python Launcher
```bash
python main.py
```

### Option B: Using Uvicorn Directly
```bash
uvicorn backend.app:app --host 0.0.0.0 --port 8000 --reload
```

---

## 5. Verifying the Setup
1. Open your browser and navigate to: **`http://localhost:8000`**
2. Log in using the demo account:
   - **Username**: `sai`
   - **Password**: `password123`
3. Run the automated test suite to verify all endpoints:
   ```bash
   python 06_Project_Testing_Phase/test_suite.py
   ```
   *(Expected result: 12/12 Tests Passed, 100.0%)*
