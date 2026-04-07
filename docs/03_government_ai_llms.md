# Government AI, Local LLMs & Workspace Tools — Landscape

> **Institutional Branding Note:** The Atal Bihari Vajpayee Institute of Good Governance and Policy Analysis (AIGGPA) typically uses a primary color palette of dark blue and gold/yellow in its official branding and logo.
> ### Official Brand Colors
> Based on the institute's official visual identity, the primary hex codes are:
> - **AIGGPA Blue:** `#1B3B6F` (Approximate)
> - **AIGGPA Gold/Yellow:** `#FFC107` (Approximate)
> ### Supplemental Secondary Colors
> While the blue and gold are the most prominent, the following colors are often used for text and accents in digital reports:
> - **White:** `#FFFFFF` (Backgrounds and negative space)
> - **Dark Gray:** `#333333` (Standard body text)
> 
> **Note:** Do not confuse AIGGPA with the multinational insurance company AIG, whose primary brand color is Spanish Sky Blue (`#00A3E7`).

> **Purpose:** Map the Indian government's AI/LLM ecosystem so you know what exists, what's usable, and how it connects to your GovTech Adoption Index project.

---

## 1. Government LLM Initiatives

### Bhashini (Digital India Bhashini Division)
| Parameter | Detail |
|-----------|--------|
| **Owner** | MeitY, Government of India |
| **Type** | Public Digital Infrastructure (not a single LLM) |
| **Function** | Translation, speech-to-text, text-to-speech, transliteration |
| **Scale** | 35+ languages, 1,600+ AI models (mid-2025) |
| **Integrations** | IRCTC, NPCI (UPI), police documentation |
| **Relevance to you** | Could translate your Hindi survey responses to English for analysis, or vice versa |
| **Access** | Public API — `bhashini.gov.in` |

### BharatGPT (CoRover.ai — Private)
| Parameter | Detail |
|-----------|--------|
| **Owner** | CoRover.ai (startup), in collaboration with NHLT (under MeitY) |
| **Type** | Enterprise conversational AI platform |
| **Languages** | 14-22+ Indian languages |
| **Key Product** | BharatGPT Mini — a Small Language Model (SLM) that runs OFFLINE on local servers, phones, IoT |
| **Data Sovereignty** | All data stays within India — key selling point for government |
| **Relevance to you** | This is the "local LLM" angle — government departments could run BharatGPT Mini on-premise for document processing |

### BharatGen (Government-Funded)
| Parameter | Detail |
|-----------|--------|
| **Owner** | Government of India (IndiaAI Mission) |
| **Type** | Sovereign multilingual, multimodal foundational model |
| **Launch** | 2025 |
| **Goal** | India-specific foundational models trained on Indian datasets, languages, contexts |
| **Status** | Under development via research institutions and startups |

### IndiaAI Mission (Umbrella Framework)
| Parameter | Detail |
|-----------|--------|
| **Approved** | March 2024 |
| **Components** | IndiaAI Compute Portal (GPU access), AI Kosha (datasets), foundational model development |
| **Budget** | ₹10,372 crore over 5 years |
| **Relevance** | Provides the POLICY CONTEXT for why your research on IT adoption matters — if employees can't use e-Office, they certainly can't use AI |

---

## 2. Comparative Model Map

```
                    Government AI Stack — India (2026)

    ┌─────────────────────────────────────────────────────┐
    │                    APPLICATION LAYER                 │
    │  CPGRAMS (AI grievance)  │  Bhashini (translation)  │
    │  iGOT (AI recommendations) │ BharatGPT (conv. AI)   │
    └─────────────────────────────────────────────────────┘
                            ▲
    ┌─────────────────────────────────────────────────────┐
    │                    MODEL LAYER                       │
    │  BharatGen (sovereign)  │  BharatGPT Mini (local)   │
    │  Bhashini models (1600+)│  Gemini/GPT (cloud, ext.) │
    └─────────────────────────────────────────────────────┘
                            ▲
    ┌─────────────────────────────────────────────────────┐
    │                 INFRASTRUCTURE LAYER                  │
    │  IndiaAI Compute Portal  │  NIC Data Centres         │
    │  MeitY GPU clusters      │  State Cloud (MeghRaj)    │
    └─────────────────────────────────────────────────────┘
                            ▲
    ┌─────────────────────────────────────────────────────┐
    │                    DATA LAYER                        │
    │  AI Kosha (datasets)  │  eSankhyiki MCP (MoSPI)     │
    │  Open Data (data.gov.in) │  Dept-level databases     │
    └─────────────────────────────────────────────────────┘
```

---

## 3. Google Workspace vs. Indigenous Alternatives

### The "Swadeshi" Shift

The government is **actively moving AWAY from Google Workspace** for core administrative work:

| Tool Category | Foreign Option | Indian Alternative (Preferred) | Status |
|--------------|---------------|-------------------------------|--------|
| Office Suite | Google Workspace | **Zoho Office Suite** | Min. of Education mandated Zoho (2025) |
| Email | Gmail | **NIC Email** (gov.in) | Already standard for all govt employees |
| Cloud | Google Cloud, AWS | **MeghRaj** (GI Cloud) | NIC-operated; empanelled clouds for overflow |
| SSO | Google Auth | **Parichay** (NIC SSO) | Mandatory for all govt apps |
| Video Conf | Google Meet | **NIC VC** platform | Used for inter-ministry coordination |
| AI Chat | Google Gemini | **BharatGPT / Bhashini** | Encouraged for data sovereignty |

### What This Means for Your Project

> **Don't pitch Google Workspace as the solution.** The government narrative is "Atmanirbhar" (self-reliant). Frame your tech stack around:
> - Zoho (office suite)
> - NIC infrastructure (hosting)
> - Bhashini (translation)
> - Indigenous tools wherever possible
> - Open-source (Python, PostgreSQL, DuckDB) over proprietary

---

## 4. AI Agents in Government — Current State

### What's Actually Deployed

| Agent/System | Department | Function | AI Type |
|-------------|-----------|----------|---------|
| CPGRAMS AI | DARPG | Auto-categorise and route citizen grievances | NLP classification |
| iGOT Recommendations | DoPT | Suggest courses based on role competency gaps | Recommendation engine |
| Bhashini Live | Multiple | Real-time translation in govt apps | Translation models |
| e-Office Smart Search | DARPG/NIC | Search across eFiles using NLP | Text search |
| GeM Bot | MoCI | Guided procurement queries | Rule-based + NLP |
| DigiLocker AI | MeitY | Document verification, OCR | Computer vision |

### What's Coming (2025-2027)

| Concept | Description |
|---------|-------------|
| MCP-powered data agents | AI assistants querying govt data (eSankhyiki is the pilot) |
| Autonomous file routing | e-Office files auto-routed based on content analysis |
| Predictive HR analytics | Forecast attrition, training needs from e-HRMS data |
| Sovereign chatbots | BharatGPT Mini deployed at district offices for citizen Q&A |

---

## 5. Conceptual Metric: AI Readiness Ladder

```
AI READINESS LADDER — Government Departments

Level 5 ┃ ██████████████████████████████████████ ┃ AI-Native
        ┃ AI agents query data autonomously;      ┃ (0% of depts)
        ┃ predictive analytics, auto-routing       ┃
        ┃                                          ┃
Level 4 ┃ ████████████████████████████             ┃ AI-Augmented
        ┃ NLP search, chatbots, auto-              ┃ (~5% of depts)
        ┃ categorisation active                    ┃
        ┃                                          ┃
Level 3 ┃ ██████████████████████                   ┃ Digital-First
        ┃ e-Office daily, e-HRMS active,           ┃ (~25% of depts)
        ┃ iGOT integrated, DSC mandatory           ┃
        ┃                                          ┃
Level 2 ┃ █████████████████                        ┃ Digitising
        ┃ Some tools adopted, parallel paper       ┃ (~45% of depts)
        ┃ processing, training underway            ┃
        ┃                                          ┃
Level 1 ┃ ████████████                             ┃ Paper-Based
        ┃ Manual files, no digital tools,          ┃ (~25% of depts)
        ┃ no training                              ┃

YOUR RESEARCH measures Level 1→3.
The MCP/AI layer is Level 4→5 — the FUTURE state.
Your GovTech Adoption Index tells departments WHERE they are on this ladder.
```

---

## 6. How This Connects to Your Project

| Your Project Component | AI/LLM Connection |
|-----------------------|-------------------|
| Survey data collection | Bhashini API could auto-translate Hindi responses |
| GovTech Adoption Index | Precursor metric — departments must reach Level 3 before AI (Level 4-5) is feasible |
| MCP server for AIGGPA | Direct application of eSankhyiki pattern to governance research data |
| Pitch to manager | "We're measuring the FOUNDATION that makes AI adoption possible" |
| Report visualisations | BharatGPT Mini could power a chatbot that answers questions about your report |
