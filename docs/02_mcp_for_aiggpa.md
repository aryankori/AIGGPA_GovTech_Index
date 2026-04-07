# Concept Note — MCP Server for AIGGPA

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

> **Strategic Vision:** This document outlines how AIGGPA can leverage the Model Context Protocol (MCP) to turn its research repositories into "AI-ready" data assets.
> **What is this?** A proposal to build a Model Context Protocol (MCP) server for AIGGPA that lets AI agents query the institute's research data, survey responses, and governance analytics in natural language.

---

## What is MCP?

**Model Context Protocol** is an open standard (by Anthropic) that lets AI assistants (Claude, ChatGPT, Cursor, etc.) connect to external data sources through a structured API. Think of it as a **USB port for AI** — plug in your data, and any AI can query it.

```
┌──────────────┐       MCP Protocol       ┌──────────────────┐
│  AI Assistant │ ◄─────────────────────► │  Your Data Server │
│  (Claude,     │    list → schema →      │  (AIGGPA MCP)     │
│   ChatGPT)    │    query → results      │                   │
└──────────────┘                          └──────────────────┘
```

---

## Two Government MCP Servers Already Exist

### 1. eSankhyiki MCP (Ministry of Statistics — MoSPI)
- **Repo:** [github.com/nso-india/esankhyiki-mcp](https://github.com/nso-india/esankhyiki-mcp)
- **What it does:** Exposes 19 statistical datasets (GDP, employment, inflation, education, health, trade, etc.) to AI agents
- **Tech:** FastMCP 3.0 + Python + Swagger validation + OpenTelemetry
- **Live server:** `https://mcp.mospi.gov.in/`
- **4-tool workflow:** `list_datasets → get_indicators → get_metadata → get_data`
- **116 stars**, MIT License, made by DIID (Data Innovation Lab) with Bharat Digital

### 2. Datalake MCP (NHAI — Your Friend Mayank's Project)
- **Repo:** [github.com/mayankthekumawat/datalake-mcp](https://github.com/mayankthekumawat/datalake-mcp)
- **What it does:** Structured analytics + document retrieval over NHAI operational data
- **Tech:** FastMCP 3.0 + DuckDB + Gemini File Search + S3
- **5-tool workflow:** `list_tables → get_table_schema → query_data` (analytics) + `list_document_stores → query_documents` (documents)
- **Key innovation:** Uses Gemini File Search for domain-scoped retrieval over circulars, acts, regulations

---

## Can You Use / Adapt These for AIGGPA?

### Short answer: **YES** — and you should.

| Question | Answer |
|----------|--------|
| Can I use the eSankhyiki MCP? | Yes — it's MIT licensed, open source, and the server at `mcp.mospi.gov.in` is publicly accessible. You can query national statistics directly. |
| Can I copy Mayank's datalake-mcp code? | You can use it as an **architectural reference**. Don't literally copy-paste — adapt the pattern for AIGGPA's data. Credit Mayank as inspiration. The code is public on GitHub. |
| Is this plagiarism? | No. Using open-source code as a template and adapting it for a different domain is standard practice. MoSPI explicitly encourages it (MIT License, CONTRIBUTING.md). |
| What makes AIGGPA's MCP different? | Different data (governance research vs highways vs statistics), different tools, different audience (policy researchers vs data analysts). |

---

## Proposed AIGGPA MCP Architecture

```
aiggpa-mcp/
├── aiggpa_server.py          # FastMCP server — tool definitions
├── aiggpa/
│   └── client.py             # Client for AIGGPA internal data APIs
├── db/
│   └── govtech_survey.duckdb # Survey response data (from your prototype)
├── documents/
│   └── policy_briefs/        # AIGGPA research documents for retrieval
├── swagger/
│   └── swagger_survey.yaml   # Parameter validation specs
├── observability/
│   └── telemetry.py          # OpenTelemetry tracing
├── tests/
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

### Proposed MCP Tools (6 tools)

| # | Tool | Purpose | Pattern From |
|---|------|---------|-------------|
| 1 | `list_datasets()` | Show available data categories (survey data, iGOT stats, e-Office logs) | eSankhyiki |
| 2 | `get_schema(dataset)` | Return column names, types, descriptions for a dataset | datalake-mcp |
| 3 | `query_data(sql)` | Run read-only DuckDB SQL on structured survey data | datalake-mcp |
| 4 | `compute_adoption_index(department, filters)` | Compute the GovTech Adoption Index for a department | **YOUR innovation** |
| 5 | `list_document_stores()` | List available policy document collections | datalake-mcp |
| 6 | `query_documents(question, store_keys)` | Natural language Q&A over AIGGPA policy documents | datalake-mcp |

### What Data Would It Serve?

| Dataset | Source | Type |
|---------|--------|------|
| GovTech Survey Responses | Your survey (120+ records) | Structured (DuckDB) |
| Adoption Index Scores | Computed from survey | Structured |
| Department Profiles | Desk audit | Structured |
| iGOT Completion Data | If accessible from dept IT cells | Structured |
| AIGGPA Policy Briefs | Institute publications | Documents (Gemini Search) |
| Government Circulars | Relevant GOs, office orders | Documents |

---

## Conceptual Metrics

```
AIGGPA MCP — Projected Impact

Data Points Queryable:     ~2,400 (120 respondents × 20 variables)
Document Collections:      4-6 stores (circulars, policy briefs, reports)
Query Response Time:       <2 seconds (DuckDB)
AI Agents Supported:       Claude, ChatGPT, Cursor, Antigravity
Deployment:                Docker → AIGGPA intranet or cloud

                    ┌─────────────────────────────┐
  Traditional       │  Manually open Excel → Pivot │  ~15 min/query
  Research Query    │  → Filter → Compute → Chart  │
                    └─────────────────────────────┘
                              vs.
                    ┌─────────────────────────────┐
  MCP-Powered       │  "What's the adoption index  │  ~5 seconds
  AI Query          │   for Health dept, Group C,  │
                    │   female employees over 40?" │
                    └─────────────────────────────┘

  Efficiency Gain: ~180x faster for ad-hoc research queries
```

---

## Implementation Roadmap (if approved as stretch goal)

| Phase | Week | Work |
|-------|------|------|
| 1. Setup | Week 9 | Fork datalake-mcp, replace NHAI schema with AIGGPA survey schema |
| 2. Data Ingest | Week 9 | Import survey CSV into DuckDB, define schema_meta.py |
| 3. Core Tools | Week 10 | Implement `list_datasets`, `get_schema`, `query_data` |
| 4. Custom Tool | Week 10 | Build `compute_adoption_index` tool |
| 5. Documents | Week 11 | Set up Gemini File Search with AIGGPA policy docs |
| 6. Deploy | Week 11 | Dockerize, test with Claude/Cursor |
| 7. Demo | Week 12 | Present working MCP to AIGGPA leadership |
