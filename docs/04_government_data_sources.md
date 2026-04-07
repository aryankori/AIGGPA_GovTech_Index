# Government Data Sources — What You Can Access as an AIGGPA Intern

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

> **The question:** Does the government have special data sources not available to the public? **Yes, absolutely.** Here's what exists and how to request access.

---

## 1. Public Sources (Free, No Permission Needed)

These are available to anyone. Use them NOW for your desk audit.

| Source | URL | What's There | Useful For |
|--------|-----|-------------|-----------|
| **data.gov.in** | data.gov.in | 5 lakh+ datasets across all ministries | Department employee counts, scheme data |
| **eSankhyiki MCP** | mcp.mospi.gov.in | 19 statistical datasets via MCP API | GDP, employment, education, health stats |
| **PIB** | pib.gov.in | Press releases with official statistics | iGOT numbers, e-Office adoption stats |
| **iGOT Dashboard** | igotkarmayogi.gov.in | Training completion, registered users, courses | State-wise iGOT engagement data |
| **GeM Dashboard** | gem.gov.in | Procurement statistics, GMV | Department-wise digital procurement |
| **PFMS** | pfms.nic.in | Fund flow, DBT data | Financial digital adoption |
| **NeSDA Reports** | darpg.gov.in | E-service delivery assessment by state | MP's e-governance maturity ranking |
| **AEBAS Dashboard** | attendance.gov.in | Biometric attendance compliance | Digital attendance adoption |
| **Indiastat** | indiastat.com | Aggregated government statistics | Cross-reference employee data |
| **MP State Portal** | mp.gov.in | MP-specific governance data | State department listings, schemes |

---

## 2. Internal / Restricted Sources (Need Permission from Manager)

These exist but are NOT publicly queryable. As an AIGGPA intern, you can **request access** through your supervisor.

### Tier A: Likely Accessible (Ask your manager directly)

| Source | What's There | Who Controls It | How to Request |
|--------|-------------|----------------|----------------|
| **e-Office Admin Dashboard** | Login frequencies, file processing stats per department | NIC / Department IT cells | Ask manager to request from GAD (General Admin Dept) |
| **e-HRMS Department Data** | Employee roster with grade, age, posting — anonymised | DoPT (Central) / State GAD | Written request through AIGGPA director |
| **iGOT Department Reports** | Course completion rates by department, grade | DoPT / Karmayogi Bharat | Available through department nodal officers |
| **MAP_IT Data** | State IT infrastructure — SWAN connectivity, hardware inventories | MAP_IT Bhopal | AIGGPA has institutional relationship; request through director |
| **State HR Database** | MP state employee records (anonymised) | GAD / Public Service Management | Formal letter from AIGGPA |
| **Department IT Cell Records** | Hardware inventory, internet uptime logs, help desk tickets | Individual department IT cells | Direct request during field visits |

### Tier B: Harder to Get (Need formal approval)

| Source | What's There | Barrier |
|--------|-------------|---------|
| **NIC Usage Analytics** | Detailed platform metrics (time-on-app, feature usage) | NIC doesn't typically share granular user analytics |
| **SPARROW/APAR Data** | Performance appraisal patterns | Confidential — only aggregate statistics may be shared |
| **Payroll/GPF Systems** | Salary, grade, posting history | Financial data — highly restricted |
| **CPGRAMS Internal** | Grievance patterns by department | Available in aggregate on DARPG, not at individual level |

---

## 3. What to Actually Ask Your Manager For

### The Email/Letter Template

> **Subject:** Request for Data Access Guide — Sourcing Government Data for Research
>
> **Strategic Guide:** This document provides a framework for interns and researchers to access both public and non-public government data.
>
> Sir/Ma'am,
>
> For my internship research on IT adoption assessment across 4 government departments, I require access to the following data points. All data will be used in anonymised, aggregate form only and will not identify individual employees.
>
> **Priority 1 (Essential):**
> 1. **Employee roster** for Revenue, PWD, Health, and Education departments — fields: grade, age, gender, posting location (anonymised names acceptable)
> 2. **e-Office login frequency** — monthly active users per department (aggregate counts, not individual names)
> 3. **iGOT course completion rates** — department-wise summary for selected 4 departments
>
> **Priority 2 (If available):**
> 4. Hardware inventory of selected departments (computers per office)
> 5. SWAN connectivity reports for district offices
> 6. Any existing assessment reports on digital adoption in MP departments
>
> I can sign any data confidentiality undertaking required by the institute.
>
> Regards,
> [Your name]
> AIGGPA Summer Intern, April 2026

---

## 4. Data Source Accessibility Matrix

```
ACCESSIBILITY OF DATA SOURCES FOR AIGGPA INTERN

               Public │ Request │ Formal  │ Not
               Access │ Manager │ Approval│ Accessible
              ────────┼─────────┼─────────┼──────────
data.gov.in   ████████│         │         │
PIB stats     ████████│         │         │
iGOT portal   ████████│         │         │
GeM dashboard ████████│         │         │
NeSDA reports ████████│         │         │
eSankhyiki    ████████│         │         │
              ────────┼─────────┼─────────┼──────────
e-Office logs │        │█████████│         │
Employee      │        │█████████│         │
  rosters     │        │         │         │
iGOT dept     │        │█████████│         │
  reports     │        │         │         │
MAP_IT infra  │        │█████████│         │
              ────────┼─────────┼─────────┼──────────
NIC analytics │        │         │█████████│
SPARROW data  │        │         │█████████│
State HR DB   │        │         │█████████│
              ────────┼─────────┼─────────┼──────────
Payroll/GPF   │        │         │         │██████████
Individual    │        │         │         │██████████
  APARs       │        │         │         │██████████

YOUR SWEET SPOT: Public (desk audit) + Manager Request (survey supplement)
```

---

## 5. How to Use eSankhyiki MCP Right Now

You can connect to MoSPI's MCP server today — it's live and public:

```bash
# Test the connection
curl -s -X POST https://mcp.mospi.gov.in/ \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-03-26","capabilities":{},"clientInfo":{"name":"aiggpa-research","version":"0.1"}}}'
```

### Datasets Relevant to Your Research

| Dataset | Relevance |
|---------|-----------|
| Employment indicators | National employment data to compare with MP |
| Higher education statistics | Education department context |
| Health statistics | Health department context |
| Gender statistics | Gender parity analysis baseline |
| Economic census | Business/enterprise digitisation context |

You can query these through Claude, Cursor, or any MCP-compatible AI client by connecting to `https://mcp.mospi.gov.in/`.
