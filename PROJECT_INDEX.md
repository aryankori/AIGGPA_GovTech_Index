# PROJECT_INDEX.md
> AIGGPA_Report -- Repository Index
> **Generated:** 2026-06-08 | **Reorganized & Structured**
> **Staleness threshold:** 7 days

---

## Repository Overview

| Attribute | Value |
|---|---|
| **Repository Name** | AIGGPA_Report |
| **Primary Language** | Python, LaTeX (TeX), HTML, JavaScript, CSS |
| **Framework** | XeLaTeX (documents), Vanilla HTML/CSS/JS (prototypes), Matplotlib/Seaborn (charts) |
| **Purpose** | AIGGPA Internship -- HR-IT Integration field research in MP Government |
| **Reorganized Structure** | Consolidated root files into vault subfolders, archives, and prototype directory |
| **Total Source Files** | ~120 files across 7 primary directories |
| **Build System** | Python scripts (data entry & SPSS quant analysis), xelatex (schedules & guides) |

---

## Directory Tree

```
AIGGPA_Report/
├── AIGGPA_Fieldwork_Review/     # MEETING DESK: All 18 files needed for Monday 10:00 AM Review
│   ├── 01_AIGGPA_Fieldwork_Journal.xlsx
│   ├── 02_AIGGPA_Master_Tracker.xlsx
│   ├── 03_Rural_Development_Responses_Form.xlsx
│   ├── 04_AIGGPA_Forest_Coded_DataMatrix.xlsx
│   ├── 05_Forest_Descriptive_Statistics.xlsx
│   ├── 06_Forest_CrossTabs_CadreDivide.xlsx
│   ├── 07_Forest_Cadre_RadarChart.png
│   ├── 08_Forest_DigitalDivide_Heatmap.png
│   ├── 09_Forest_TrainingGap_BarChart.png
│   ├── 10_Forest_DeviceAvailability_Chart.png
│   ├── tomorrow_briefing.md/txt
│   ├── meeting_prep.md/txt
│   └── *.pdf (schedules templates)
│
├── AIGGPA_Fieldwork_Vault/      # DATA VAULT: Structured research center
│   ├── 01_Schedules_Raw/        # Survey templates & scanned schedules
│   ├── 04_Observation_Notes/    # Fieldwork Journal & observation files
│   ├── 07_Secondary_Data/       # Collected data from Forest & RD, framework templates
│   ├── 08_Data_Entry/           # Raw Excel, clean files, and SPSS-ready datasets
│   ├── 09_Analysis_Output/      # Quantitative results, descriptives, reliability, charts
│   ├── 10_Reports_Drafts/       # Proposals, plans, guides, and policy blueprints
│   ├── 11_Presentations/        # Pitch decks and stakeholder briefings
│   ├── 12_Backups/              # Weekly tracker backup archives
│   ├── AIGGPA_Master_Tracker.xlsx  # Live Command Tracker
│   └── *.py (data ingestion, validation & analysis scripts)
│
├── Organized_Archive/           # CLEANUP: Archived historical & compiled files
│   ├── 01_PDFs/                 # Compiled XeLaTeX PDFs
│   ├── 02_Build_Artifacts/      # LaTeX intermediate build logs (.aux, .log, etc.)
│   ├── 05_Word_Docs/            # Draft proposals and rationales (.docx)
│   └── index.md
│
├── prototype/                   # PROTOTYPE: Interactive web visuals & mobile survey
│   ├── index.html               # Main dashboard
│   ├── field_survey_entry.html  # Mobile survey mockup
│   ├── ClinicalDashboard.*      # Health prototypes (moved to subfolder)
│   └── *.html (visualisation mockups)
│
├── docs/                        # Supporting documentation
│   └── CLINICAL_ARCHITECTURE.md # TS/React architecture flow charts (Mermaid)
│
├── schedules/                   # SOURCES: Document compilation source codes
│   └── tex/                     # All 40+ .tex source files (main.tex, schedules, etc.)
│
├── scripts/                     # SCRIPTS: Python utility modules
│   └── legacy_root_scripts/     # Cleaned up legacy ad-hoc Python files from root
│
├── README.md                    # Repository description & build instructions
├── PROJECT_INDEX.md             # This file
└── PROJECT_INDEX.json           # Machine-readable directory index
```

---

## Entry Points

| Entry Point | File | Role |
|---|---|---|
| Meeting Shortcut Folder | [AIGGPA_Fieldwork_Review/](file:///c:/Users/aryan/OneDrive/Documents/Visual%20Studio%202022/AIGGPA_Report/AIGGPA_Fieldwork_Review) | Open files here during CEO presentation |
| CEO Briefing Plan | [tomorrow_briefing.md](file:///c:/Users/aryan/OneDrive/Documents/Visual%20Studio%202022/AIGGPA_Report/AIGGPA_Fieldwork_Review/tomorrow_briefing.md) | Action script and talking points for 10 AM |
| Master Progress Tracker | [AIGGPA_Master_Tracker.xlsx](file:///c:/Users/aryan/OneDrive/Documents/Visual%20Studio%202022/AIGGPA_Report/AIGGPA_Fieldwork_Vault/AIGGPA_Master_Tracker.xlsx) | Open first to review respondent counts (Forest N=40, RD N=19) |
| Quantitative Analysis Script | [build_analysis.py](file:///c:/Users/aryan/OneDrive/Documents/Visual%20Studio%202022/AIGGPA_Report/AIGGPA_Fieldwork_Vault/build_analysis.py) | Automates SPSS descriptives, Cronbach's Alpha, and chart visualisations |
| Main Research Report | `schedules/tex/main.tex` | Compile with `xelatex main.tex` (XeLaTeX font spec Nirmala UI) |
| Web Prototype | `prototype/index.html` | Open in browser |

---

## Module Map

### LaTeX Documents (Core Research)
All LaTeX sources reside under `schedules/tex/` to avoid root directory pollution.
- `main.tex`: Secondary research report on HR-IT in Indian Govt (~40 pages)
- `concept_proposal.tex`: Bilingual formal proposal (2 pages)
- `survey_instrument.tex`: Bilingual field questionnaire (2 pages)
- `proposal_prep_guide.tex`: Proposal prep & 20-Q checklist (7 pages)
- `Schedule_*.tex`: Department-specific field schedules (Forest, RD, Revenue, Health)

### Web Prototype Modules
Static web application mockups for testing design theories.
- `index.html`: Web dashboard
- `field_survey_entry.html`: Mobile field entry simulation
- Visualisations: `forest_dashboard.html`, `maturity_ladder.html`, `composite_scoring_model.html`

### Technical Documentation
- `docs/CLINICAL_ARCHITECTURE.md`: TypeScript/React architectural flow charts and de-identification sequence diagrams mapped via Mermaid.

### Fieldwork Data Vault
AIGGPA Fieldwork data tracking structure containing respondent logs, data entry sheets, reliability statistics, and charts.
- `04_Observation_Notes/AIGGPA_Fieldwork_Journal.xlsx`: Activity verification log (15 entries, May 4 - Jun 7)
- `08_Data_Entry/Raw_Excel/AIGGPA_Forest_DataEntry.xlsx`: Coded Likert data (40 rows x 68 variables)
- `09_Analysis_Output/Quantitative/forest_descriptives.xlsx`: Descriptive statistic tables
- `09_Analysis_Output/Quantitative/forest_reliability.xlsx`: Construct reliability alphas (PE, EE, SI, FC)
- `09_Analysis_Output/Visualisations/*.png`: Cadre Radar chart, Digital Divide heatmap, training gaps bar chart, and device availability counts

---

## Risk Flags & Maintenance

- ✅ **No Loose Files**: The root folder is completely cleaned of all temporary build artifacts, compiled PDFs, legacy Word drafts, and auxiliary Python scripts.
- ✅ **Code Safety**: All sensitive Google Sheets re-authentication tokens and workspace configurations are kept in `.tmp` files (ignored in `.gitignore`).
- ✅ **Path Validity**: Vault Python scripts (`ingest_forest_data.py`, `build_analysis.py`) execute perfectly from the vault root directory.
