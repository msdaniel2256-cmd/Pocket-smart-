# Master Test Plan

## 1. Introduction & Objectives
The primary objective of testing PocketSmart AI is to verify that:
1. All API endpoints and web routes return appropriate HTTP status codes and valid schemas.
2. User authentication (OAuth2 / JWT / bcrypt) securely enforces access boundaries.
3. Budget allocation algorithms mathematically distribute funds accurately without exceeding top-line limits.
4. Multimodal image analysis correctly parses color histograms and produces style pairings.
5. Indian commerce search links are properly URL-encoded and functional.
6. The dual-engine architecture gracefully degrades to deterministic offline mode without 500 exceptions.

---

## 2. Scope of Testing

### In-Scope
- **Authentication & Authorization**: Registration, login, JWT token issuance, expired tokens, invalid passwords, token blacklisting.
- **Home Interior Budget Planner**: Budget distribution, fixture count allocations, room filters, IKEA/Amazon/Flipkart links.
- **Party Budget Planner**: Guest count scaling, catering/venue/decor/entertainment splits, safety buffer allocation.
- **Jewelry Planner**: Budget tiers, occasion filtering, outfit photo upload, dominant color extraction.
- **Session Management**: Session duration tracking, in-memory cache, background garbage collection.
- **Data Persistence**: Atomic writes and reads from `database.json`.

### Out-of-Scope
- Live third-party retail checkout flows (external merchant e-commerce platforms).
- Hardware stress testing beyond single-node server capability.

---

## 3. Test Environment Specifications
- **Operating System**: Windows 11 / x86_64
- **Runtime**: Python 3.11
- **Server**: Uvicorn ASGI Server on `http://127.0.0.1:8000`
- **Test Automation Framework**: Python `requests`, JSON assertions, Pytest compatible

---

## 4. Entry & Exit Criteria
- **Entry Criteria**: FastAPI server successfully initialized; all dependencies in `requirements.txt` installed; database seed present.
- **Exit Criteria**: 100% execution of automated integration test suite; 0 critical or high-severity blocking bugs; pass rate >= 95%.
