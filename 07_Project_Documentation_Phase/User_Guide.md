# User Guide: PocketSmart AI

Welcome to **PocketSmart AI: Your Smart Budget & Recommendation Assistant**. This guide will walk you through the key capabilities of the application.

---

## 1. Getting Started & Logging In

### Accessing the Web Application
1. Open your web browser and navigate to: **`http://localhost:8000`**
2. You will see the **PocketSmart AI Landing Page**, highlighting features for Home Interior Planning, Event Budgeting, and Occasion Jewelry Matching.

### User Login
1. Click **Login** in the top navigation bar or go directly to `/login`.
2. Use the pre-configured demo account:
   - **Username**: `sai`
   - **Password**: `password123`
3. Click **Sign In**.
4. You will be redirected to your **Personal Dashboard** (`/dashboard`).

*(Alternatively, click **Register** (`/register`) to create a new personalized account).*

---

## 2. Navigating the Dashboard
Your Dashboard displays:
- **Active Session Timer**: Shows your login timestamp and session activity.
- **Quick Launch Tiles**: Direct buttons to launch the Home Planner, Party Planner, or Jewelry Planner.
- **Recent Recommendations**: A list of your latest budget plans with category badges and direct inspection links.

---

## 3. Using the Home Interior Planner (`/home-planner`)
1. Click **Home Planner** in the navigation bar.
2. Enter your **Total Budget (₹)** (e.g., `50000`).
3. Specify your required fixture quantities:
   - Number of LED Lights (e.g., `6`)
   - Number of Ceiling Fans (e.g., `3`)
   - Furniture Sets (e.g., `2`)
   - Dining Table count (e.g., `1`)
4. Check the rooms you are decorating: Living Room, Kitchen, Bedroom.
5. Click **Generate Home Budget Plan**.
6. **Reviewing the Results**:
   - The **Calculation Table** displays the exact percentage and INR allocation for Lighting, Fans, Furniture, and Dining.
   - Each item card shows unit prices and direct search links for **IKEA India, Amazon, Flipkart, Myntra, and Ajio**. Click any button to view matching products immediately.

---

## 4. Using the Party & Event Budget Planner (`/party-planner`)
1. Click **Party Planner** in the navigation bar.
2. Enter your **Total Budget (₹)** (e.g., `75000`) and **Guest Count** (e.g., `40`).
3. Select your **Event Type** (e.g., Birthday, Wedding Reception, Anniversary, Corporate Gathering).
4. Select your **Venue Style** (e.g., Banquet Hall, Cafe, Resort, Home).
5. Toggle your requirements: Catering, Theme Decoration, Entertainment (DJ/Music).
6. Click **Generate Party Budget Plan**.
7. **Reviewing the Results**:
   - The plan divides your budget safely across Catering (~40%), Venue (~25%), Decor (~15%), Entertainment (~10%), and reserves a **10% Contingency Buffer**.
   - Browse suggested venues with estimated costs and direct links to **Swiggy, Zomato, BookMyShow, Booking.com, and MakeMyTrip**.

---

## 5. Using the Occasion Jewelry Planner (`/jewelry-planner`)
1. Click **Jewelry Planner** in the navigation bar.
2. Enter your **Total Budget (₹)** (e.g., `20000`).
3. Select the **Occasion** (e.g., Wedding, Festive Diwali, Cocktail Party, Casual).
4. Specify your styling preferences (e.g., *"Traditional gold with pearl accents"*).
5. *(Optional but Recommended)*: Click **Upload Outfit Photo** to attach a photo of your dress or saree.
6. Click **Generate Jewelry Recommendations**.
7. **Reviewing the Results**:
   - If an outfit photo was provided, PocketSmart AI highlights your **Detected Color Palette** (e.g., Emerald Green, Golden Ochre) and formality class.
   - Recommended jewelry items (Necklaces, Earrings, Rings, Bracelets) are displayed with estimated prices, styling tips, and direct shopping links to **Tanishq, CaratLane, BlueStone, and Melorra**.

---

## 6. Reviewing History & Details (`/history`)
1. Click **History** in the top navigation bar.
2. Filter your past recommendations using the **All**, **Home**, **Party**, or **Jewelry** tabs.
3. Click **View Details** on any recommendation card to open the interactive modal with complete breakdown tables and shopping links.
