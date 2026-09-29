# Phase 01: Brainstorming & Ideation Phase

## Overview
This phase encapsulates the conceptual foundation, initial creative discovery, market necessity, problem identification, and strategic ideation behind **PocketSmart AI: Your Smart Budget & Recommendation Assistant**.

---

## Directory Contents
- **[Problem_Statement.md](Problem_Statement.md)**: Details the financial, logistical, and stylistic friction faced by everyday consumers when planning budgets for home interiors, events, and jewelry.
- **[Idea_Description.md](Idea_Description.md)**: Comprehensive description of PocketSmart AI as an intelligent, GenAI-powered personalized budgeting and product sourcing companion.
- **[Proposed_Solution.md](Proposed_Solution.md)**: Technical and functional architecture of the proposed solution, including dynamic allocation algorithms, multimodal vision matching, and vendor routing.
- **[Brainstorming_Notes.md](Brainstorming_Notes.md)**: Raw ideation logs, feature trade-offs, architecture decisions, and platform evaluation notes from the initial design meetings.

---

## Key Ideation Milestones
1. **Identified Core Domains**: Narrowed focus to three high-variance expenditure categories: Home Interior Furnishing, Party/Event Management, and Occasion Jewelry Matching.
2. **Indian Market Context**: Prioritized deep localization for Indian consumers with pricing in INR (₹) and direct query routing to prominent Indian platforms (Amazon India, Flipkart, IKEA India, Swiggy, Zomato, BookMyShow, Tanishq, CaratLane).
3. **Resilience Principle**: Mandated that the system must never fail even if external AI APIs (Google Gemini) are throttled, offline, or unconfigured—leading to the dual-engine architecture (Gemini 1.5 Flash + Intelligent Rule-Based Fallback).
