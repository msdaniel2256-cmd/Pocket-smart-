# Brainstorming Notes & Discussion Log

## 1. Initial Brainstorming Discussions

### Topic 1: Scope of Categories
- *Initial Idea*: Cover all consumer purchases including electronics, grocery shopping, travel, weddings, and interior design.
- *Decision*: Too broad for high precision. Focused on three high-friction, high-value domains:
  1. Home Interior Furnishing (complex balance of electricals vs. furniture).
  2. Event/Party Management (high risk of catering/venue budget blowouts).
  3. Occasion Jewelry (strong visual/outfit pairing requirements).

### Topic 2: AI Dependency vs. Reliability
- *Discussion*: Should the application rely 100% on external LLM calls (e.g., OpenAI or Gemini)?
- *Resolution*: No. Relying purely on cloud APIs introduces latency, rate limiting, and potential failure when keys are missing or invalid.
- *Architecture Decision*: Implement a **dual-engine system**. The app must function seamlessly with realistic Indian pricing and smart algorithms even with zero API credits or no internet connectivity.

### Topic 3: E-Commerce Integration Strategy
- *Discussion*: Should we integrate real-time merchant affiliate APIs (Amazon Product Advertising API, Flipkart API)?
- *Resolution*: Official affiliate APIs require corporate approvals, token rotations, and have strict query quotas. Instead, build a **Dynamic Search Query Formatter** that generates pre-filled search URLs directly to Amazon India, Flipkart, IKEA India, Swiggy, Zomato, BookMyShow, and Tanishq. This ensures 100% availability, zero cost, and immediate shopping utility.

### Topic 4: Image Analysis for Jewelry Matching
- *Discussion*: How can a user get jewelry recommendations that match what they are wearing?
- *Resolution*:
  - Add an outfit image upload field.
  - When Gemini Vision API is accessible, feed prompt + image for deep stylistic matching.
  - Provide a local Python Pillow (PIL) RGB color histogram analyzer as fallback to detect dominant colors (e.g., Crimson Red, Emerald Green, Royal Blue, Gold) and categorize outfit formality.

### Topic 5: Session & Storage Architecture
- *Discussion*: Is a full relational database (PostgreSQL/MySQL) needed for the MVP?
- *Resolution*: A lightweight, atomic JSON persistence file (`database.json`) combined with in-memory caching provides instant zero-configuration deployment, portability across operating systems, and rapid startup without database server dependencies.

---

## 2. Feature Prioritization Matrix

| Feature | Impact | Feasibility | Phase 1 Status |
|---|---|---|---|
| Home Interior Budget Planner | High | High | Core Feature |
| Party / Event Budget Planner | High | High | Core Feature |
| Multimodal Jewelry Outfit Matcher | High | Medium | Core Feature |
| JWT Authentication & Session Tracking | Medium | High | Core Feature |
| Interactive History & Category Filter | Medium | High | Core Feature |
| Direct Indian Retail Search Links | High | High | Core Feature |
| Auto Session Expiry Cleaner (30 mins) | Low | High | Background Service |
