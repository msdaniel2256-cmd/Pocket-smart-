# Phase 05: Project Development Phase

## Overview
This phase contains the complete, working source code, modules, templates, static assets, database, and configuration files for **PocketSmart AI**.

---

## Directory Organization

```
05_Project_Development_Phase/
├── README.md               # Development phase guide & architecture map
├── development_notes.md    # Technical logs, algorithmic solutions, bug fixes
├── source/                 # Main application launch scripts (main.py, app.py)
├── frontend/               # User interface assets
│   ├── templates/          # Jinja2 HTML templates
│   └── static/             # CSS stylesheets, static images, uploaded outfit photos
├── backend/                # Server application logic
│   ├── app.py              # FastAPI controller, routes, session worker
│   ├── models/             # Pydantic schemas (schemas.py)
│   ├── routes/             # Route modules & handlers
│   ├── services/           # AI services & link generators (gemini_service.py)
│   └── data/               # Persistent JSON database (database.json)
├── api/                    # API definitions & schema contracts
│   └── schemas.py          # Request and response models
├── database/               # Database files & storage
│   └── database.json       # JSON persistence store
└── config/                 # Environment configuration templates & loaders
    ├── config.py           # Configuration loader
    └── .env.example        # Environment variable template
```

---

## Running the Application from Development Phase

To run the application directly from the development phase or from the project root:

```bash
# From project root
python main.py

# Or via Uvicorn
uvicorn backend.app:app --host 0.0.0.0 --port 8000 --reload
```

Open your browser at **http://localhost:8000**.
Demo credentials:
- **Username**: `sai`
- **Password**: `password123`
