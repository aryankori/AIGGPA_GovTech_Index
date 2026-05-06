---
name: aiggpa_soul
description: Core context and parameters for the AIGGPA Research Project. Use this skill to recall the project's entire background, methodology, structural rules, and tone requirements without the user needing to repeat them.
---

# AIGGPA Research Project: "Soul" Context

This skill acts as the master reference guide for the user's internship research project at the Atal Bihari Vajpayee Institute of Good Governance and Policy Analysis (AIGGPA).

Whenever you are working on this project, you must adhere strictly to the rules, context, and methodologies outlined below.

## 1. Project Overview
**Title:** Assessment of Digital Tool Adoption and Its Impact on Efficiency in MP Government Departments.
**Objective:** To systematically evaluate how digital tools are being adopted by government employees across different levels, identify bottlenecks, and recommend actionable policy changes to improve service delivery in Madhya Pradesh.

## 2. Scope and Target Demographics
The research targets four specific government departments across four staff hierarchies (cadres).
**Target Departments:**
1. Revenue
2. Rural Development
3. Forest
4. Health

**Target Cadres (Hierarchies):**
- **Class I:** High-level officials (e.g., Collector, CEO Zila Panchayat, DFO, CMHO).
- **Class II:** Mid-level management (e.g., SDM, BDO, ACF, BMO).
- **Class III:** Field/Operational staff (e.g., Tehsildar, Patwari, GRS, Range Officer, ANM).
- **Class IV:** Support staff (e.g., Peon, Forest Guard, Ward Boy).

## 3. Core Objectives & Indicators
1. **Digital Infrastructure & Awareness:** Assessing device availability, internet quality, and frequency of portal usage.
2. **Capacity Building & Training:** Evaluating the frequency and quality of formal/informal IT training and technical support.
3. **Bottlenecks & Challenges:** Identifying hardware issues, software bugs, poor UI, and attitudinal resistance.
4. **Recommendations:** Formulating data-driven policy actions, infrastructure upgrades, and training modifications.

## 4. Methodology
- **Mixed Methods:** Combining quantitative data (survey scores, device counts) with qualitative insights (field observations, semi-structured interviews, FGDs).
- **Frameworks:** Grounded in TAM (Technology Acceptance Model) and UTAUT (Unified Theory of Acceptance and Use of Technology).
- **Measurement:** 5-point Likert scales for difficulty, satisfaction, and impact. Thematic analysis for interview transcripts.

## 5. Technical Infrastructure
- **Google Workspace (gog CLI):** The project relies entirely on Google Workspace for fieldwork data collection and storage. The `gog` CLI is installed locally. The workspace contains a master Google Sheet tracker, a Google Form for surveys, and a Google Drive vault for audio/scans.
- **Python:** Used for data validation (`validate_tracker.py`), automated transcriptions (via Whisper API), and directory generation.
- **LaTeX:** Used for generating highly professional, institutional-grade PDFs (schedules, questionnaires, research proposals).

## 6. Strict Tone & Formatting Rules
- **Humanizer Mandatory:** You must actively suppress AI writing quirks. Do NOT use words like "delve", "leverage", "testament", "tapestry", "seamless", "crucial", or "vital". Use simple, direct, authoritative English.
- **No Hallucinations:** Do not invent data, fake government programs, or make assumptions about Madhya Pradesh departments that are not verified.
- **Minimalist & Professional:** Documents, LaTeX designs, and reports must look clean, modern, and "Wall-Street/Apple" style. Avoid clutter. Use data to drive the narrative.
- **Institutional Perspective:** Write from the perspective of an objective, data-driven researcher reporting to government leadership, not a casual observer.

## 7. How to Use This Context
Whenever the user asks you to "draft a report", "make a chart", or "plan a field visit", silently reference these parameters. You know exactly who we are interviewing, what we are asking them, and what tools we are using to store the data. Proceed with absolute confidence.

## 8. Deep Data Points & Quantitative Targets
- **Sample Size:** 320 respondents total (80 per department).
- **Stratification:** 10 respondents per Cadre Class per Office Type (Head Office vs. District Office). Segmented by age (30-45 and 46-60).
- **Timeline:** Fieldwork spans May 2026 through July 2026. Final report submission deadline is July 15, 2026.
- **Evaluation Benchmarks:**
  - Device Ratio: >= 1 device per employee.
  - Internet Score: Median Likert >= 3.
  - Tool Awareness: >= 70% aware of core tools.
  - Daily Usage: >= 50% use tools daily.
  - Training Coverage: >= 60% trained in last 2 years.
  - Reliability: Cronbach's Alpha >= 0.70 per construct.

## 9. Academic Frameworks & Analysis Toolkit
- **Research Design:** Convergent Parallel Mixed-Methods Design (Creswell, 2014).
- **Theoretical Base:** 
  - Technology Acceptance Model (TAM) - Davis (1989) (Focus: Facilitating Conditions, Performance Expectancy).
  - UTAUT - Venkatesh (2003) (Focus: Effort Expectancy, Social Influence).
- **Quantitative Tools:** 
  - Descriptive statistics (SPSS v26+ / Excel).
  - Cronbach's Alpha (Reliability).
  - Mann-Whitney U Test (Ordinal comparison: HO vs District).
  - Kruskal-Wallis H Test (Ordinal comparison across 4 departments).
- **Qualitative Tools:** 
  - Reflexive Thematic Analysis (Braun & Clarke, 2006) - 6 phases.
  - Hybrid inductive-deductive coding (mapping quotes to TAM/UTAUT).
- **Policy Benchmarks:**
  - UN e-Government Development Index (EGDI) 2024.
  - OECD Digital Government Policy Framework (2014).

## 10. Department-Specific Digital Portals (The Tech Stack)
To accurately assess adoption, the research looks at these specific portals for each department:
- **Revenue:** MP Bhulekh / WebGIS 2.0, RCMS (Revenue Case Management System), SAARA, SAMPADA 2.0, e-Court / e-Filing.
- **Rural Development:** NREGASoft MIS, NMMS App (MGNREGA), e-Gram Swaraj, PMAY-G Portal, SBM-G Portal, Panchayat Darpan, PFMS.
- **Forest:** e-Green Watch (CAMPA), AI-Based Forest Alert System, GIS/Remote Sensing platforms, Forest Offence Tracking MIS, Nursery Management System.
- **Health:** ANMOL MP (ANM Online), HMIS, Nikshay (TB Portal), eVIN (Vaccine Cold Chain), IHIP (Disease Surveillance), Ayushman Bharat/ABHA, MPCDSR.

## 11. Custom Questionnaire Additions
- **Q60-Q67:** These refer to department-specific and cadre-specific questions appended to the main 59-question standard schedule. They target exact workflow issues (like dual-documentation burdens in Health, or GIS proficiency in Forest).
