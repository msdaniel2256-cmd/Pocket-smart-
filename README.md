# PocketSmart AI: Your Smart Budget & Recommendation Assistant

[![Python 3.11](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688.svg)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Tests Passing](https://img.shields.io/badge/Tests-12%2F12%20Passed%20(100%25)-brightgreen.svg)](06_Project_Testing_Phase/Test_Results.md)
[![AI Engine](https://img.shields.io/badge/AI-Google%20Gemini%201.5%20Flash-orange.svg)](https://deepmind.google/technologies/gemini/)

**PocketSmart AI** is an intelligent, GenAI-driven budget allocation and lifestyle recommendation system engineered for Indian consumers. It provides personalized, mathematically proportioned budget breakdowns and direct product sourcing links for **Home Interior Furnishing**, **Event & Party Planning**, and **Multimodal Occasion Jewelry Matching**.

The application utilizes a **Dual-Engine Architecture**: combining **Google Gemini 1.5 Flash** for dynamic generative intelligence with a robust, deterministic **Indian Market Rule Engine** that guarantees 100% operational availability with realistic INR estimates even when offline or unconfigured.

---

## 📁 Repository Structure by Project Lifecycle Phase

This repository is organized phase-wise according to the full project engineering lifecycle:

| Phase Directory | Phase Name | Key Deliverables & Documentation |
|---|---|---|
| **[01_Brainstorming_and_Ideation_Phase/](01_Brainstorming_and_Ideation_Phase/)** | Brainstorming & Ideation | [Problem Statement](01_Brainstorming_and_Ideation_Phase/Problem_Statement.md), [Idea Description](01_Brainstorming_and_Ideation_Phase/Idea_Description.md), [Proposed Solution](01_Brainstorming_and_Ideation_Phase/Proposed_Solution.md), [Brainstorming Notes](01_Brainstorming_and_Ideation_Phase/Brainstorming_Notes.md) |
| **[02_Requirement_Analysis_Phase/](02_Requirement_Analysis_Phase/)** | Requirement Analysis | [Functional Requirements](02_Requirement_Analysis_Phase/Functional_Requirements.md), [Non-Functional Requirements](02_Requirement_Analysis_Phase/Non_Functional_Requirements.md), [User Requirements](02_Requirement_Analysis_Phase/User_Requirements.md), [System Requirements](02_Requirement_Analysis_Phase/System_Requirements.md), [Use Cases](02_Requirement_Analysis_Phase/Use_Cases.md) |
| **[03_Project_Design_Phase/](03_Project_Design_Phase/)** | Project Design | [System Architecture](03_Project_Design_Phase/System_Architecture.md), [Database Design](03_Project_Design_Phase/Database_Design.md), [UI/UX Design](03_Project_Design_Phase/UI_UX_Design.md), [Data Flow](03_Project_Design_Phase/Data_Flow.md), [Architecture Diagrams](03_Project_Design_Phase/Architecture_Diagrams/README.md) |
| **[04_Project_Planning_Phase/](04_Project_Planning_Phase/)** | Project Planning | [Development Plan](04_Project_Planning_Phase/Development_Plan.md), [Project Timeline](04_Project_Planning_Phase/Project_Timeline.md), [Task Breakdown (WBS)](04_Project_Planning_Phase/Task_Breakdown.md), [Technology Stack](04_Project_Planning_Phase/Technology_Stack.md) |
| **[05_Project_Development_Phase/](05_Project_Development_Phase/)** | Project Development | [Source Code](05_Project_Development_Phase/source/), [Frontend Assets](05_Project_Development_Phase/frontend/), [Backend Logic](05_Project_Development_Phase/backend/), [API Schemas](05_Project_Development_Phase/api/), [Database Store](05_Project_Development_Phase/database/), [Configuration](05_Project_Development_Phase/config/), [Development Notes](05_Project_Development_Phase/development_notes.md) |
| **[06_Project_Testing_Phase/](06_Project_Testing_Phase/)** | Project Testing | [Test Plan](06_Project_Testing_Phase/Test_Plan.md), [Test Cases](06_Project_Testing_Phase/Test_Cases.md), [Test Results (100% Pass)](06_Project_Testing_Phase/Test_Results.md), [Bug Reports](06_Project_Testing_Phase/Bug_Reports.md), [Automated Suite](06_Project_Testing_Phase/test_suite.py), [Screenshots](06_Project_Testing_Phase/screenshots/) |
| **[07_Project_Documentation_Phase/](07_Project_Documentation_Phase/)** | Project Documentation | [User Guide](07_Project_Documentation_Phase/User_Guide.md), [Installation Guide](07_Project_Documentation_Phase/Installation_Guide.md), [API Documentation](07_Project_Documentation_Phase/API_Documentation.md), [Deployment Guide](07_Project_Documentation_Phase/Deployment_Guide.md), [Troubleshooting](07_Project_Documentation_Phase/Troubleshooting.md) |
| **[08_Project_Demonstration_Phase/](08_Project_Demonstration_Phase/)** | Project Demonstration | [Project Demo Narrative](08_Project_Demonstration_Phase/Project_Demo.md), [Demo Steps Script](08_Project_Demonstration_Phase/Demo_Steps.md), [Visual Evidence](08_Project_Demonstration_Phase/Screenshots/), [Demo Video Link](08_Project_Demonstration_Phase/Demo_Video_Link.md) |

---

## 🌟 Key Application Features

1. **Home Interior Planning with Smart Allocation (`/home-planner`)**:
   - Dynamic budget allocation across lighting fixtures, ceiling fans, furniture pieces, and dining tables.
   - Room-specific recommendations (Living Room, Kitchen, Bedroom).
   - Direct shopping links with pre-filled search terms for **IKEA India, Amazon, Flipkart, Myntra, and Ajio**.
   - Allocation breakdown calculation table with percentages and smart cost-saving recommendations.

2. **AI-Based Party & Event Budget Planning (`/party-planner`)**:
   - Smart budget proportioning across catering, venue booking, theme decoration, entertainment, and safety contingency buffer.
   - Tailored to event types (Birthday, Wedding, Corporate, Anniversary) and guest counts.
   - Sourcing links for **Swiggy, Zomato, BigBasket, BookMyShow, OYO, Booking.com, MakeMyTrip, and Amazon**.

3. **Occasion Jewelry Recommendations with Outfit Vision (`/jewelry-planner`)**:
   - Context-aware recommendations for occasions (Wedding, Birthday, Festive, Cocktail, Casual).
   - **Multimodal Outfit Image Analysis**: Upload an outfit photo to automatically extract color palette, formality, and design style to match jewelry using Python Pillow or Gemini Vision.
   - Sourcing links for **Tanishq, CaratLane, BlueStone, Melorra, Amazon, and Flipkart**.
   - Personalized styling and pairing tips.

4. **User Dashboard & History Tracking (`/dashboard`, `/history`)**:
   - Secure user authentication with OAuth2 password flow, JWT tokens (`python-jose`), and salted `bcrypt` password hashing.
   - Full history of past recommendations with category filters and interactive details modal.
   - Pre-configured demo user (`sai` / `password123`) for instant evaluation.

---

## 🏗️ Architecture & Technology Stack

- **Backend**: FastAPI (Python 3.10+) with Uvicorn ASGI production server
- **AI Engine**: Google Gemini 1.5 Flash (`google-generativeai`) with intelligent offline rule-based fallback
- **Frontend**: Server-rendered Jinja2 Templates, Vanilla CSS3 (Custom Dark Mode), Vanilla JS
- **Security**: OAuth2 Password Flow, JWT tokens (`python-jose`), salted `bcrypt` password hashing, token blacklisting on logout
- **Storage**: Lightweight, zero-dependency JSON-backed persistence (`data/database.json`)

---

## 🚀 Quickstart & Installation

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Environment
Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```
*(Note: If no Google Gemini API key is provided, the application will automatically run in intelligent local fallback mode with realistic Indian pricing).*

### 3. Run Application Server
```bash
python main.py
```
Or with Uvicorn:
```bash
uvicorn backend.app:app --host 0.0.0.0 --port 8000 --reload
```

Open your browser at **[http://localhost:8000](http://localhost:8000)**.

### Demo Credentials
- **Username**: `sai`
- **Password**: `password123`
*(Or register a new account on `/register`)*

### 4. Run Automated Test Suite
```bash
python 06_Project_Testing_Phase/test_suite.py
```
*(All 12 automated unit and integration tests execute against the live server).*

---

## 📋 Core API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Marketing Landing page |
| `GET`/`POST` | `/login` | User login and session initiation |
| `GET`/`POST` | `/register` | User registration |
| `POST` | `/token` | OAuth2 JWT token endpoint |
| `GET` | `/dashboard` | User dashboard with planner links & recent activity |
| `GET` | `/home-planner` | Home Interior Planner UI |
| `POST` | `/home-budget` or `/generate-home` | Generate home interior recommendations |
| `GET` | `/party-planner` | Party Planner UI |
| `POST` | `/party-budget` or `/generate-party` | Generate party budget plan |
| `GET` | `/jewelry-planner` | Jewelry Planner UI (with outfit photo upload) |
| `POST` | `/jewelry-budget` or `/generate-jewelry` | Generate jewelry recommendations |
| `GET` | `/history` | History page of saved recommendations |
| `GET` | `/recommendation-history` | JSON history list |
| `GET` | `/recommendation-details/{id}` | Detailed recommendation JSON |
| `GET` | `/session-info` | Current user session metadata |
| `GET` | `/logout` | Blacklist token and clear session |
