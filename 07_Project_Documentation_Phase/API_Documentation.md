# REST API Documentation

PocketSmart AI provides a set of RESTful endpoints for authentication, session querying, budget planning, and history inspection.

---

## 1. Authentication Endpoints

### 1.1 Obtain OAuth2 Access Token
- **Endpoint**: `POST /token`
- **Content-Type**: `application/x-www-form-urlencoded`
- **Request Body**:
  | Parameter | Type | Required | Description |
  |---|---|---|---|
  | `username` | String | Yes | Account username (e.g., `sai`) |
  | `password` | String | Yes | Account password (e.g., `password123`) |

- **Response (200 OK)**:
  ```json
  {
    "access_token": "eyJhbGciOiJIUzI1NiIsIn...",
    "token_type": "bearer"
  }
  ```

---

## 2. Session Management Endpoints

### 2.1 Get Current Session Information
- **Endpoint**: `GET /session-info`
- **Headers**: `Authorization: Bearer <access_token>` or `Cookie: access_token=Bearer <access_token>`
- **Response (200 OK)**:
  ```json
  {
    "username": "sai",
    "login_time": "2026-09-28T05:32:00.123456+00:00",
    "last_activity": "2026-09-28T05:33:15.987654+00:00",
    "session_duration_minutes": 1,
    "user_data": {
      "last_home_budget": { ... }
    }
  }
  ```

---

## 3. Budget Recommendation Endpoints

### 3.1 Home Interior Budget Planner
- **Endpoint**: `POST /home-budget` (or `POST /generate-home`)
- **Content-Type**: `application/json`
- **Request Body**:
  ```json
  {
    "total_budget": 50000.0,
    "num_lights": 6,
    "num_fans": 3,
    "num_furniture": 2,
    "num_dining_tables": 1,
    "has_living_room": true,
    "has_kitchen": true,
    "has_bedroom": false,
    "additional_requirements": "Warm minimalist styling"
  }
  ```
- **Response (200 OK)**:
  ```json
  {
    "total_budget": 50000.0,
    "budget_breakdown": [
      {
        "category": "Lighting",
        "allocation": 7500.0,
        "items": [
          {
            "name": "Philips / Crompton LED Warm White Lights",
            "description": "Energy-efficient ambient lighting",
            "estimated_price": 1250.0,
            "quantity": 6,
            "search_terms": "Warm White LED Ceiling Light fixture",
            "shopping_links": {
              "amazon": "https://www.amazon.in/s?k=...",
              "flipkart": "https://www.flipkart.com/search?q=...",
              "ikea": "https://www.ikea.com/in/en/search/?q=..."
            }
          }
        ]
      }
    ],
    "calculation_table_inr": [
      {
        "category": "Lighting",
        "items_count": 6,
        "total_cost": 7500.0,
        "percentage_of_budget": 15.0
      }
    ],
    "remaining_budget": 0.0
  }
  ```

### 3.2 Party & Event Budget Planner
- **Endpoint**: `POST /party-budget` (or `POST /generate-party`)
- **Content-Type**: `application/json`
- **Request Body**:
  ```json
  {
    "total_budget": 80000.0,
    "num_guests": 40,
    "party_type": "Wedding Reception",
    "venue_type": "Banquet Hall",
    "needs_catering": true,
    "needs_decoration": true,
    "needs_entertainment": true,
    "additional_requirements": "Buffet dinner setup"
  }
  ```

### 3.3 Occasion Jewelry Planner
- **Endpoint**: `POST /jewelry-budget` (or `POST /generate-jewelry`)
- **Content-Type**: `multipart/form-data`
- **Form Fields**:
  | Field | Type | Required | Description |
  |---|---|---|---|
  | `total_budget` | Float | Yes | Total spending budget in INR |
  | `occasion` | String | Yes | Wedding / Festive / Cocktail / Casual |
  | `preferences` | String | No | Style preferences (e.g., Gold & Emerald) |
  | `image` | File | No | JPEG/PNG/WebP image of event outfit |

---

## 4. History Endpoints

### 4.1 Get User Recommendation History
- **Endpoint**: `GET /recommendation-history`
- **Response (200 OK)**:
  ```json
  {
    "history": [
      {
        "id": "d4a5ac51",
        "timestamp": "Sep 26, 2026, 01:24 PM",
        "type": "home",
        "input": { "total_budget": 5000.0 },
        "summary": { "total_budget": 5000.0, "remaining_budget": 0.0, "categories_count": 4 }
      }
    ]
  }
  ```

### 4.2 Get Detailed Recommendation by ID
- **Endpoint**: `GET /recommendation-details/{recommendation_id}`
- **Response (200 OK)**: Full recommendation object with items, calculation tables, and shopping links.
