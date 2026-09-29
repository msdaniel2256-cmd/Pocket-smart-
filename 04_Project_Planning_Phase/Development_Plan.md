# Development Plan & Engineering Strategy

## 1. Engineering Methodology
PocketSmart AI was engineered using an **Agile/Iterative Vertical-Slice Methodology**, emphasizing rapid functional prototypes backed by solid foundational layers. Each feature cycle delivered an end-to-end working capability—from API endpoint and business logic down to user interface interaction and data persistence.

---

## 2. Iterative Development Sprints

### Sprint 1: Architectural Foundation & Security (Milestone 1)
- Scaffold project layout with clean separation of `backend/`, `frontend/`, and `data/`.
- Implement `PasswordContext` using salted `bcrypt` hashing.
- Configure OAuth2 Password Bearer flow and JWT token generation (`python-jose`).
- Build user session tracking in memory with automated background garbage collection task.
- Establish JSON-backed persistence store (`database.json`) with pre-seeded demo user (`sai`).

### Sprint 2: Core Domain Logic & Dual-Engine Fallback (Milestone 2)
- Formulate mathematical budget allocation models for Home Interior and Party Planning.
- Engineer `gemini_service.py` with dynamic Gemini 1.5 Flash client initialization.
- Implement resilient fallback routines returning standardized JSON structures.
- Develop dynamic URL synthesizer for Indian platforms (Amazon, Flipkart, IKEA, Swiggy, Zomato, BookMyShow, Tanishq).
- Build regex-based clean JSON extractor capable of parsing raw LLM responses.

### Sprint 3: Multimodal Vision & Image Processing (Milestone 3)
- Enable `multipart/form-data` image file upload handling with collision-resistant timestamped filenames.
- Build local RGB color quantizer using Python Pillow to extract dominant color palettes and map them to human-readable names.
- Connect vision outputs to jewelry recommendation prompts and fallback styling tips.

### Sprint 4: Frontend Templating & UI/UX Assembly (Milestone 4)
- Craft bespoke Dark Mode CSS design system (`styles.css`) using CSS Grid, Flexbox, and glassmorphism cards.
- Construct Jinja2 templates: Landing (`index.html`), Auth (`login.html`, `register.html`), Dashboard (`dashboard.html`), and Planners (`home_planner.html`, `party_planner.html`, `jewelry_planner.html`).
- Build interactive History page (`history.html`) with category tabs and detailed modal popup.

### Sprint 5: Testing, Hardening & Deployment Readiness (Milestone 5)
- Automated API test suite execution validating all status codes and JSON response schemas.
- Refactor project structure to conform with 8-phase standard repository layout.
- Finalize production documentation, installation manuals, and demonstration guides.
