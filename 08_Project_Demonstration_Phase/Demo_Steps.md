# Step-by-Step Live Demonstration Script

Follow this exact sequence to demonstrate the complete functionality of **PocketSmart AI**:

---

## Step 1: Pre-Demo Preparation & Launch
1. Ensure dependencies are installed and the application server is active:
   ```bash
   python main.py
   ```
2. Open your web browser and navigate to: **`http://localhost:8000`**

---

## Step 2: Showcase Landing Page & Value Proposition
1. Highlight the header navigation: Brand logo, Home, Login, Register.
2. Scroll through the feature cards:
   - **Smart Home Interior Planning**
   - **Party & Event Celebration Budgeting**
   - **Occasion Jewelry Matching with Image AI**
3. Point out the supported Indian retail integrations: Amazon India, Flipkart, IKEA, Swiggy, Zomato, BookMyShow, Tanishq, CaratLane.

---

## Step 3: Authenticate & Explore User Dashboard
1. Click **Login** in the top navbar.
2. Enter the demo credentials:
   - **Username**: `sai`
   - **Password**: `password123`
3. Click **Sign In**.
4. Observe redirection to `/dashboard`.
5. Explain the **Active Session Duration** and recent recommendation cards.

---

## Step 4: Demonstrate Home Interior Budget Planner
1. Click **Home Planner** in the navbar.
2. Enter:
   - **Total Budget**: `50000`
   - **Lights**: `4`
   - **Ceiling Fans**: `2`
   - **Furniture Sets**: `1`
   - **Rooms**: Select *Living Room* and *Kitchen*
3. Click **Generate Home Budget Plan**.
4. Show the **Calculation Breakdown Table** with percentage shares and costs in INR.
5. Click on an **IKEA** or **Amazon** search button to demonstrate the pre-filled URL query.

---

## Step 5: Demonstrate Party & Event Budget Planner
1. Click **Party Planner** in the navbar.
2. Enter:
   - **Total Budget**: `80000`
   - **Guest Count**: `35`
   - **Party Type**: `Birthday Celebration`
   - **Venue**: `Cafe / Lounge`
   - Check *Catering*, *Decoration*, and *Entertainment*.
3. Click **Generate Party Budget Plan**.
4. Show how funds are proportioned across food, venue, and decor. Highlight the **Safety Buffer**.
5. Click on a **Swiggy / Zomato** or **BookMyShow** button to show direct vendor routing.

---

## Step 6: Demonstrate Occasion Jewelry Planner with Image AI
1. Click **Jewelry Planner** in the navbar.
2. Enter:
   - **Total Budget**: `25000`
   - **Occasion**: `Wedding Celebration`
   - **Preferences**: `Traditional gold and emerald accents`
3. Click **Upload Outfit Photo** and select `frontend/static/uploads/sample_outfit.jpg`.
4. Click **Generate Jewelry Recommendations**.
5. Show the **Detected Outfit Colors** (e.g., Emerald Green, Golden Ochre) and styling suggestions.
6. Click on a **Tanishq** or **CaratLane** link.

---

## Step 7: Demonstrate History & Details Modal
1. Click **History** in the navbar.
2. Click the **Home**, **Party**, and **Jewelry** filter tabs.
3. Click **View Details** on any recommendation to open the popup modal.
4. Show the full nested JSON breakdown.
5. Click **Logout** to demonstrate token blacklisting and session termination.
