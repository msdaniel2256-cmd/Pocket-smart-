# Non-Functional Requirements Specification (NFRS)

## 1. Performance & Latency (NFR-01 to NFR-03)

### NFR-01: Response Latency
- **Offline / Fallback Calculations**: Must respond within **< 150 ms** for budget calculation and platform search link generation.
- **Gemini API Calculations**: Must stream or return responses within **< 3.5 seconds** under normal cloud conditions.
- **Image Processing**: Color extraction and formality heuristics on uploaded images must execute in **< 300 ms** locally.

### NFR-02: Page Load Times
- Landing page (`/`), Dashboard (`/dashboard`), and Planner pages must load in **< 1.0 second** on local ASGI server.
- Static assets (CSS, images) must be efficiently cached by the browser.

### NFR-03: Concurrency & ASGI Async Performance
- Backend built on FastAPI and Uvicorn utilizing Python `asyncio` to handle concurrent user requests without thread starvation.

---

## 2. Reliability & Availability (NFR-04 to NFR-06)

### NFR-04: Graceful Degradation (100% Service Availability)
- If the `GOOGLE_API_KEY` is missing, expired, throttled (HTTP 429), or network fails, the system must **never** return an uncaught 500 error.
- The dual-engine architecture must silently switch to the local rule-based engine and return valid calculations.

### NFR-05: Data Consistency
- Atomic read/write operations on the JSON database (`data/database.json`) to prevent data corruption during simultaneous user writes.

### NFR-06: Error Handling & Form Feedback
- User input errors (e.g., negative budget, non-numeric values, password mismatch) must produce human-readable UI alerts without crashing the server.

---

## 3. Security & Privacy (NFR-07 to NFR-10)

### NFR-07: Password Hashing
- Passwords must be hashed using `bcrypt` with automatic salt generation. Plaintext passwords must never be stored or logged.

### NFR-08: Token Security
- JWT tokens signed with HMAC-SHA256 (`HS256`).
- Secret key configurable via `.env`.
- Tokens expire in 60 minutes (`ACCESS_TOKEN_EXPIRE_MINUTES`).
- Session cookies marked with `HttpOnly` and `SameSite=Lax`.

### NFR-09: Token Blacklisting on Logout
- Logged-out tokens are stored in an in-memory blacklist set to prevent replay attacks during their remaining validity window.

### NFR-10: Upload Sanitization
- Uploaded outfit images must be assigned collision-free timestamped filenames (`YYYYMMDDHHMMSS_filename.ext`) and saved within `static/uploads/`.

---

## 4. Usability & UI/UX (NFR-11 to NFR-13)

### NFR-11: Responsive Layout
- Fully responsive across desktop (1920x1080, 1440x900), tablet (768px), and mobile (375px - 414px) viewport widths using CSS Flexbox and Grid.

### NFR-12: Visual Aesthetics & Theme
- Dark mode theme utilizing curated slate-blue backgrounds (`#0f172a`, `#1e293b`), vibrant accent gradients (purple, cyan, amber), glassmorphism cards, and modern typography (Inter / Outfit / system sans-serif).

### NFR-13: Accessibility & Feedback
- Interactive button states, clear loading spinners during calculation, and legible color contrast adhering to WCAG 2.1 AA standards.
