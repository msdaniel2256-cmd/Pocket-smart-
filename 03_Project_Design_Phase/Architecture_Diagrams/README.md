# Architecture Diagrams & Visualizations

This directory contains architectural blueprints and topology diagrams for **PocketSmart AI**.

---

## 1. System Component Architecture

```mermaid
graph TD
    subgraph Client["Client Tier"]
        UI["Jinja2 Web UI (HTML5, CSS3, JS)"]
    end

    subgraph Server["Application Server Tier (FastAPI / Uvicorn)"]
        Gateway["FastAPI Gateway"]
        AuthSvc["Auth & Security Service (JWT / Bcrypt)"]
        SessionMgr["In-Memory Session Manager & Cleaner"]
        StaticMnt["Static Assets Mount (/static)"]
        TemplateEng["Jinja2 Template Engine"]
        
        Gateway --> AuthSvc
        Gateway --> SessionMgr
        Gateway --> StaticMnt
        Gateway --> TemplateEng
    end

    subgraph CoreEngine["Recommendation & AI Tier"]
        Orchestrator["Gemini / Fallback Orchestrator"]
        VisionProc["Pillow Image / Vision Processor"]
        LinkEngine["Commerce Link Synthesizer"]
        
        Gateway --> Orchestrator
        Orchestrator --> VisionProc
        Orchestrator --> LinkEngine
    end

    subgraph DataTier["Persistence Tier"]
        JSONStore[("database.json (Users & Recs)")]
        FileStore[("Uploads Directory (/uploads)")]
        
        Gateway <--> JSONStore
        Gateway --> FileStore
    end

    subgraph ExternalServices["External Commerce & Cloud Tier"]
        GeminiCloud["Google Gemini 1.5 Flash Cloud API"]
        RetailWeb["Indian Retail Platforms (Amazon, Flipkart, IKEA, Swiggy, etc.)"]
        
        Orchestrator -.->|Optional GenAI API| GeminiCloud
        LinkEngine -.->|Pre-filled Search Queries| RetailWeb
    end

    UI <-->|HTTP / WebSocket / Cookie| Gateway
```

---

## 2. Authentication State Machine

```mermaid
stateDiagram-v2
    [*] --> Unauthenticated: Visit Site

    Unauthenticated --> LoggingIn: Submit Credentials
    LoggingIn --> Unauthenticated: Invalid Password / Username
    LoggingIn --> Authenticated: Password Verified & JWT Issued

    state Authenticated {
        [*] --> ActiveSession
        ActiveSession --> BrowsingPlanners: Navigate Pages
        BrowsingPlanners --> SubmittingBudget: Submit Form
        SubmittingBudget --> ActiveSession: Result Rendered
        ActiveSession --> Inactive: No user actions
        Inactive --> ActiveSession: User Activity Resumed
    }

    Authenticated --> Unauthenticated: Logout Clicked / Cookie Cleared
    Inactive --> Terminated: Inactive > 30 Mins (Worker Purge)
    Terminated --> [*]
```
