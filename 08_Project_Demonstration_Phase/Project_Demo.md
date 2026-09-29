# Project Demonstration Narrative

## 1. Executive Summary & Value Proposition
**PocketSmart AI: Your Smart Budget & Recommendation Assistant** addresses the real-world challenge of budgeting for lifestyle milestones in India. During this demonstration, the audience is guided through an intuitive, dark-mode web application that seamlessly converts high-level monetary budgets into detailed, category-proportioned product recommendations with direct links to major Indian retailers.

---

## 2. Key Demonstration Scenarios

### Scenario 1: Seamless Authentication & Live Session Monitoring
- **Persona**: Returning homeowner "Sai Kumar".
- **Action**: Accesses `http://localhost:8000/login`, enters `sai` / `password123`, and reaches the dashboard.
- **Showcase**: Highlights the automatic JWT cookie issuance, active session duration counter, and historical budget items.

### Scenario 2: Home Interior Furnishing under ₹50,000 Budget
- **Action**: Enters ₹50,000 for a Living Room and Kitchen setup with 4 LED ceiling fixtures, 2 ceiling fans, and 1 modular armchair.
- **Showcase**:
  - Algorithmic budget division: Lighting (~₹7,500), Fans (~₹10,000), Furniture (~₹17,500).
  - Itemized cards with estimated unit prices.
  - Interactive shopping link buttons generating instant searches for **IKEA India, Amazon.in, and Flipkart**.

### Scenario 3: 50-Guest Wedding Reception Planning under ₹1,20,000 Budget
- **Action**: Inputs ₹1,20,000 budget for 50 attendees at a Banquet Hall with catering, decoration, and DJ entertainment enabled.
- **Showcase**:
  - Proportional division: Catering (₹48,000), Venue (₹30,000), Decor (₹18,000), Entertainment (₹12,000).
  - Automatic reservation of a **10% Contingency Safety Buffer** (₹12,000).
  - Instant venue options and deep links to **Swiggy, Zomato, BookMyShow, Booking.com, and MakeMyTrip**.

### Scenario 4: Multimodal Jewelry Matching with Outfit Photo
- **Action**: Uploads `sample_outfit.jpg` with a ₹25,000 budget for a Festive Diwali Celebration.
- **Showcase**:
  - Python Pillow / Gemini Vision extracts the dominant color palette (e.g., Emerald Green, Golden Ochre) and classifies formality.
  - Generates matching jewelry pieces (Kundan choker necklace, Polki earrings, cocktail ring).
  - Provides direct shopping links for **Tanishq, CaratLane, BlueStone, and Melorra**.

### Scenario 5: Audit Trail, Filtering & Details Modal
- **Action**: Navigates to `/history`, toggles filters (All, Home, Party, Jewelry), and clicks "View Details".
- **Showcase**: Instant popup modal displaying full JSON calculation structures, percentages, and platform queries.
