# Development Notes & Technical Log

## 1. Architectural Implementation Overview
PocketSmart AI was developed to deliver an interactive, resilient budgeting and recommendation engine. The codebase is organized into cleanly decoupled layers:
- `backend/app.py`: Main FastAPI ASGI controller, route definitions, authentication middleware, and session lifecycle manager.
- `backend/services/gemini_service.py`: AI and algorithmic engine, regex JSON extractor, multimodal vision color quantizer, and Indian retail platform link synthesizer.
- `backend/models/schemas.py`: Pydantic input models and domain entity objects.
- `frontend/`: Jinja2 templates and vanilla CSS/JS assets.
- `database/`: Atomic JSON persistence store.

---

## 2. Key Engineering Solutions & Implementation Details

### 2.1 Resilient Dual-Engine AI Architecture
- **Challenge**: Relying strictly on Google Gemini 1.5 Flash introduces vulnerabilities: network timeouts, quota limits (HTTP 429), or missing API keys during evaluation.
- **Solution**: Implemented an automatic detection and fallback mechanism in `gemini_service.py`:
  ```python
  if gemini_available and gemini_model:
      try:
          response = gemini_model.generate_content(prompt)
          result = extract_json_from_response(response.text)
      except Exception as e:
          print(f"[Gemini API fallback] Error: {e}")
          result = None

  if not result or "budget_breakdown" not in result:
      result = generate_fallback_home_recommendations(budget_input)
  ```
- **Result**: The application guarantees 100% operational availability in offline or unconfigured environments with realistic Indian rupee (INR) estimates.

### 2.2 Local Multimodal Vision Processing
- **Challenge**: The jewelry planner requires matching jewelry to outfit colors, but cloud vision APIs may not always be reachable.
- **Solution**: Developed `analyze_image_colors_fallback(image_path)` using Python Pillow (`PIL.Image`). The routine downsizes uploaded images to a 50x50 RGB thumbnail, computes color histograms, filters top RGB centroids, maps them to human-readable color descriptions (e.g., Crimson Red, Emerald Green, Royal Blue, Golden Ochre), and assigns an outfit formality classification.

### 2.3 Direct Indian Market Sourcing Link Generation
- **Challenge**: Third-party retail APIs require commercial approval and rate quotas.
- **Solution**: Built deterministic search query generators (`get_home_shopping_links`, `get_party_shopping_links`, `get_jewelry_shopping_links`) that format and URL-encode targeted search queries directly to Amazon India, Flipkart, IKEA India, Swiggy, Zomato, BookMyShow, and Tanishq.

### 2.4 State Management & Background Garbage Collection
- **In-Memory Active Sessions**: Maintained in `active_sessions` dictionary for rapid session lookups.
- **Background Worker**: Configured via `@app.on_event("startup")` using `asyncio.create_task`. Every 5 minutes (300 seconds), it checks session timestamps and purges any session where `(current_time - last_activity) > 1800` seconds (30 minutes).

### 2.5 Atomic JSON Persistence
- Data persistence is implemented in `database.json`.
- Uses dictionary models serialized with `indent=2` for human readability, ease of audit, and zero database server dependencies.

---

## 3. Bug Fixes & Refinements During Development
1. **Passlib & Cryptography Compatibility**: Standard passlib bcrypt configurations had compatibility friction with modern 2026 bcrypt libraries. Implemented a custom `PasswordContext` wrapping `bcrypt.hashpw` and `bcrypt.checkpw` directly with safe 72-byte password truncation.
2. **Markdown Block JSON Stripping**: LLM responses often wrap JSON inside ````json ... ```` blocks. Implemented `extract_json_from_response` with regex extraction to guarantee parsing success.
3. **Cookie and Header Dual-Authentication**: Configured auth middleware to inspect both `Authorization: Bearer <token>` HTTP headers and `access_token` cookies, enabling seamless API usage and browser navigation.
