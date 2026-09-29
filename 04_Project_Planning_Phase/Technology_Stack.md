# Technology Stack & Technical Rationale

## 1. Stack Summary Table

| Category | Technology | Version | Key Justification |
|---|---|---|---|
| **Backend Framework** | FastAPI | `>=0.110.0` | Asynchronous speed, automatic OpenAPI docs, Pydantic type safety |
| **ASGI Web Server** | Uvicorn | `>=0.28.0` | Ultra-fast ASGI implementation powered by `uvloop` / `asyncio` |
| **Language** | Python | `3.11.x` | Modern async syntax, rich AI SDK ecosystem, rapid development |
| **AI / LLM Engine** | Google Gemini 1.5 Flash | `google-generativeai>=0.4.0` | Low latency, multimodal vision support, cost efficiency |
| **Templating Engine** | Jinja2 | `>=3.1.3` | Clean separation of Python controllers from HTML views |
| **Client-Side Styling** | Vanilla CSS3 | Custom | Zero build step, bespoke dark mode theme, fast rendering |
| **Client-Side Logic** | Vanilla JavaScript | ES6+ | Lightweight asynchronous `fetch` without framework bloat |
| **Image Processing** | Pillow (PIL) | `>=10.0.0` | Fast RGB color histogram extraction and image resizing |
| **Authentication** | `python-jose` & `bcrypt` | `>=3.3.0`, `>=4.0.0` | Industry-standard JWT signing and salted password hashing |
| **Persistence Store** | JSON-backed Storage | Native Python `json` | Zero external database dependencies, instant local setup |

---

## 2. Technical Evaluation & Rationale

### 2.1 Backend: FastAPI vs. Flask vs. Django
- **FastAPI Selected**: Offers native Python async support, high concurrency for background workers, automated request validation using Pydantic, and native OpenAPI generation.
- **Why Flask Was Rejected**: Synchronous by default; requires external libraries for async request handling and Pydantic-level schema validation.
- **Why Django Was Rejected**: Excessive architectural overhead (ORM, migrations, admin panel) for an AI-first application with a lightweight document model.

### 2.2 AI Engine: Google Gemini 1.5 Flash vs. Alternatives
- **Gemini 1.5 Flash Selected**: Designed specifically for low-latency production applications, native multimodal image ingestion (critical for the jewelry planner), and high output token rates.
- **Dual-Engine Architecture**: Integrated with a deterministic fallback engine to ensure 100% application uptime regardless of cloud API availability.

### 2.3 Frontend: Server-Rendered Jinja2 + Vanilla CSS vs. Heavy SPA (React/Next.js)
- **Jinja2 + Vanilla CSS/JS Selected**: Eliminates `npm` build toolchain complexity, avoids heavy client-side hydration delays, and ensures immediate, reliable local execution on any machine.
- **Dark Mode CSS Architecture**: Crafted with CSS custom properties (variables), Flexbox, and CSS Grid to deliver a responsive, visual experience.

### 2.4 Persistence: JSON File Store vs. Relational DBMS (PostgreSQL/MySQL)
- **JSON File Store Selected**: Eliminates the need to install, configure, migrate, or manage background database daemons, making the project portable across operating systems while remaining inspectable.
