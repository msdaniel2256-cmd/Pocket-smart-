# Idea Description

## 1. Executive Summary
**PocketSmart AI: Your Smart Budget & Recommendation Assistant** is an intelligent web application designed to bridge the gap between financial budget constraints and real-world consumer lifestyle planning. Powered by **Google Gemini 1.5 Flash**, **FastAPI**, and an Indian e-commerce search routing engine, PocketSmart AI serves as an interactive financial co-pilot across three key lifestyle domains:

1. **Home Interior Planning** (`/home-planner`)
2. **AI-Based Party & Event Budgeting** (`/party-planner`)
3. **Multimodal Occasion Jewelry Matching** (`/jewelry-planner`)

---

## 2. Core Pillars of the Idea

### 2.1 Dynamic Algorithmic Budget Allocation
Instead of generic advice, PocketSmart AI calculates precise percentage-based and quantity-sensitive allocations:
- In Home Planning: Automatically balances funds across lighting fixtures, ceiling fans, furniture pieces, and dining tables, taking room counts into account.
- In Party Planning: Intelligently proportions funds between catering, venue booking, theme decoration, entertainment, and safety buffers based on guest counts and event types.
- In Jewelry Planning: Allocates budgets across neckwear, earrings, rings, and bangles/bracelets tailored to occasion formality.

### 2.2 Direct-to-Commerce Indian Market Routing
For every generated recommendation, PocketSmart AI automatically constructs targeted, URL-encoded search links to leading Indian commerce and service platforms:
- **Home Decor**: IKEA India, Amazon.in, Flipkart, Myntra, Ajio
- **Event Planning**: Swiggy, Zomato, BigBasket, BookMyShow, OYO, Booking.com, MakeMyTrip
- **Jewelry**: Tanishq, CaratLane, BlueStone, Melorra, Meesho

### 2.3 Multimodal Computer Vision Integration
Using Google Gemini 1.5 Flash Vision capabilities alongside a local Pillow-based RGB color histogram analyzer, users can upload photos of their event outfits. PocketSmart AI detects:
- Dominant and accent color palettes (e.g., Emerald Green, Golden Ochre, Crimson Red, Royal Blue)
- Formality classification (Formal, Semi-Formal, Traditional, Casual)
- Harmonious metal and gemstone recommendations (e.g., Kundan, Polki, Rose Gold, Solitaire, Oxidized Silver)

### 2.4 User Session & History Management
Users can create secure accounts, log in, track active session duration, view previously generated budget plans, filter historical plans by planner category, and inspect detailed cost calculation breakdowns.

### 2.5 Resilient Dual-Engine Architecture
The application is built to guarantee 100% uptime:
- When a valid Google Gemini API key is present: Generates dynamic, context-aware GenAI suggestions.
- When offline or running without an API key: Automatically activates the deterministic Indian market rule engine, maintaining realistic INR item estimates and platform links.
