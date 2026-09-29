# Functional Requirements Specification (FRS)

## 1. User Management & Authentication (FR-01 to FR-06)

### FR-01: User Registration
- The system must provide a registration page at `/register`.
- Inputs required: `username`, `email`, `password`, and `confirm_password`.
- Validations:
  - `password` and `confirm_password` must match identically.
  - `username` must be unique in the system.
  - Passwords must be hashed using bcrypt before storage.
- Postcondition: Automatically generate a JWT session cookie and redirect user to `/dashboard`.

### FR-02: User Authentication & Login
- The system must provide a login page at `/login` accepting `username` and `password`.
- The system must provide an OAuth2 compliant token endpoint at `/token` accepting `application/x-www-form-urlencoded` credentials.
- On valid credentials:
  - Generate a signed JWT token containing `sub: <username>` with a 60-minute expiration.
  - Create an active user session in memory.
  - Set an `HttpOnly`, `SameSite=Lax` cookie named `access_token`.
  - Redirect the browser to `/dashboard`.

### FR-03: Session Tracking & Metadata
- The system must track user session creation time, last active timestamp, and duration.
- Endpoint `/session-info` must return the current user's session metadata in JSON.
- Endpoint `/session-data` must allow updating custom session state attributes.

### FR-04: Background Session Garbage Collection
- An asynchronous background worker must trigger every 300 seconds to detect sessions inactive for more than 1800 seconds (30 minutes) and purge them from memory.

### FR-05: User Logout & Token Invalidation
- Endpoint `/logout` (supporting both `GET` and `POST`) must add the active token to a blacklist, delete the in-memory session, clear the `access_token` cookie, and redirect to `/login`.

### FR-06: Pre-Configured Demo Account
- The system must initialize with a pre-configured demo user:
  - Username: `sai`
  - Password: `password123`
  - Pre-seeded with sample home, party, and jewelry recommendations.

---

## 2. Home Interior Budget Planner (FR-07 to FR-10)

### FR-07: Home Planning Input Form
- Form interface at `/home-planner` must accept:
  - `total_budget` (float, required, > 0)
  - `num_lights` (int, default 0)
  - `num_fans` (int, default 0)
  - `num_furniture` (int, default 0)
  - `num_dining_tables` (int, default 0)
  - Room selectors: Living Room (`has_living_room`), Kitchen (`has_kitchen`), Bedroom (`has_bedroom`)
  - `additional_requirements` (optional string)

### FR-08: Home Budget Proportional Allocation
- Post endpoints: `/home-budget` and `/generate-home`.
- Algorithmic distribution:
  - Lighting: ~15% of total budget
  - Ceiling Fans: ~20% of total budget
  - Furniture: ~35% of total budget
  - Dining Tables: ~20% of total budget
  - Contingency / Remainder: Automatically calculated and reported as `remaining_budget`.
- Total allocated funds must not exceed the provided `total_budget`.

### FR-09: E-Commerce Sourcing Generation (Home)
- For every suggested item, generate direct query links to:
  - Amazon India (`https://www.amazon.in/s?k=...`)
  - Flipkart (`https://www.flipkart.com/search?q=...`)
  - IKEA India (`https://www.ikea.com/in/en/search/?q=...`)
  - Myntra (`https://www.myntra.com/search?q=...`)
  - Ajio (`https://www.ajio.com/search/?text=...`)

### FR-10: Budget Calculation Summary Table
- Emits a calculation table with: `category`, `items_count`, `total_cost`, and `percentage_of_budget`.

---

## 3. Party & Event Budget Planner (FR-11 to FR-14)

### FR-11: Party Planning Input Form
- Form interface at `/party-planner` must accept:
  - `total_budget` (float, required, > 0)
  - `num_guests` (int, required, > 0)
  - `party_type` (string, e.g., Birthday, Wedding, Corporate, Anniversary)
  - `venue_type` (optional string, e.g., Banquet Hall, Cafe, Home, Resort)
  - Requirements toggles: `needs_catering`, `needs_decoration`, `needs_entertainment`
  - `additional_requirements` (optional string)

### FR-12: Party Budget Allocation Logic
- Post endpoints: `/party-budget` and `/generate-party`.
- Algorithmic distribution:
  - Catering: ~40% of total budget
  - Venue: ~25% of total budget
  - Decoration: ~15% of total budget
  - Entertainment: ~10% of total budget
  - Contingency Buffer: ~10% of total budget

### FR-13: Venue Suggestions with Capacity
- Suggest venues tailored to `num_guests` and `venue_type` with estimated cost and search links.

### FR-14: E-Commerce & Service Sourcing Generation (Party)
- Catering links: Swiggy, Zomato, BigBasket, Amazon
- Venue links: Booking.com, MakeMyTrip, OYO Rooms, NoBroker
- Decor & Entertainment: Amazon, Flipkart, BookMyShow

---

## 4. Occasion Jewelry Planner with Image Analysis (FR-15 to FR-18)

### FR-15: Jewelry Planning Input Form
- Form interface at `/jewelry-planner` must accept:
  - `total_budget` (float, required)
  - `occasion` (string, e.g., Wedding, Birthday, Festive, Cocktail, Casual)
  - `preferences` (optional string)
  - `image` (optional file upload: JPEG/PNG/WebP)

### FR-16: Multimodal Outfit Color & Style Extraction
- When an outfit image is uploaded:
  - Save to `static/uploads/` with a timestamped unique filename.
  - Offline mode: PIL quantizer extracts top RGB colors, maps them to human-readable names (Crimson Red, Emerald Green, Royal Blue, Golden Ochre, etc.), and classifies formality.
  - GenAI mode: Feeds image into Gemini 1.5 Flash Vision to evaluate silhouette, pattern, and color synergy.

### FR-17: Jewelry Recommendation & Pairing Tips
- Post endpoints: `/jewelry-budget` and `/generate-jewelry`.
- Suggests complementary items (Necklaces, Earrings, Rings, Bracelets/Bangles) with estimated prices and styling tips.

### FR-18: Jewelry Sourcing Links
- Generates links for: Tanishq, CaratLane, BlueStone, Melorra, Meesho, Amazon, Flipkart.

---

## 5. History & Audit Trail (FR-19 to FR-21)

### FR-19: Persistent Storage of Recommendations
- Automatically persist every generated recommendation to `database.json` linked to the authenticated user.
- Include unique 8-character ID, ISO timestamp, type, input summary, full result, and summary metrics.

### FR-20: History View & Dynamic Category Filter
- Page `/history` displays all past recommendations.
- Interactive filter buttons: "All", "Home", "Party", "Jewelry".

### FR-21: Recommendation Details Modal
- Endpoint `/recommendation-details/{id}` returns the full JSON result.
- Frontend displays an interactive modal with complete breakdown tables and shopping links.
