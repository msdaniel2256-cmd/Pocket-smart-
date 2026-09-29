# Production Deployment Guide

This guide details best practices for deploying **PocketSmart AI** to a production Linux/Cloud server (e.g., Ubuntu 22.04 LTS, AWS EC2, DigitalOcean, or Render).

---

## 1. System Architecture in Production

```mermaid
flowchart LR
    ClientBrowser[Client Browser] -->|HTTPS :443| NginxProxy[Nginx Reverse Proxy & SSL]
    NginxProxy -->|HTTP :8000| UvicornProcess[Uvicorn ASGI Process Manager]
    UvicornProcess --> FastAPIApp[FastAPI Application]
    FastAPIApp --> JSONData[(database.json Persistence)]
```

---

## 2. Server Provisioning & Setup (Ubuntu 22.04 LTS)

### Step 2.1: Update Server Packages
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip python3-venv git nginx certbot python3-certbot-nginx -y
```

### Step 2.2: Clone Project & Configure Virtual Environment
```bash
sudo mkdir -p /var/www/pocketsmart
sudo chown -R $USER:$USER /var/www/pocketsmart
git clone https://github.com/your-username/pocketsmart-ai.git /var/www/pocketsmart
cd /var/www/pocketsmart

python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 2.3: Production Environment Variables
Create `/var/www/pocketsmart/.env`:
```env
GOOGLE_API_KEY=your_production_gemini_key
SECRET_KEY=generate_a_cryptographically_secure_random_hex_string_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
HOST=127.0.0.1
PORT=8000
```

---

## 3. Configuring Systemd Service Manager
Create a systemd unit file at `/etc/systemd/system/pocketsmart.service`:

```ini
[Unit]
Description=PocketSmart AI FastAPI Application
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/var/www/pocketsmart
Environment="PATH=/var/www/pocketsmart/venv/bin"
ExecStart=/var/www/pocketsmart/venv/bin/uvicorn backend.app:app --host 127.0.0.1 --port 8000 --workers 4

Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

Enable and start the service:
```bash
sudo systemctl daemon-reload
sudo systemctl enable pocketsmart
sudo systemctl start pocketsmart
sudo systemctl status pocketsmart
```

---

## 4. Configuring Nginx Reverse Proxy & SSL (HTTPS)

Create `/etc/nginx/sites-available/pocketsmart`:

```nginx
server {
    server_name yourdomain.com www.yourdomain.com;

    client_max_body_size 20M;

    location /static/ {
        alias /var/www/pocketsmart/frontend/static/;
        expires 30d;
        add_header Cache-Control "public, no-transform";
    }

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Enable the site and obtain a free Let's Encrypt SSL certificate:
```bash
sudo ln -s /etc/nginx/sites-available/pocketsmart /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
```

---

## 5. Docker Containerization (Optional)

```dockerfile
# Multi-stage lightweight Python container
FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc libffi-dev && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "backend.app:app", "--host", "0.0.0.0", "--port", "8000"]
```
