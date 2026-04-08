# PROJECT_INDEX.md
> AIGGPA_Report -- Repository Index
> **Generated:** 2026-04-08 | **Commit:** ec80fd2 | **Staleness threshold:** 7 days

---

## Repository Overview

| Attribute | Value |
|---|---|
| **Repository Name** | AIGGPA_Report |
| **Primary Language** | LaTeX (TeX), HTML, JavaScript |
| **Framework** | XeLaTeX (documents), Vanilla HTML/CSS/JS (prototypes) |
| **Purpose** | AIGGPA Internship -- HR-IT Integration field research in MP Government |
| **Total Source Files** | ~30 files across 3 directories |
| **Build System** | MiKTeX + xelatex (documents); Node.js + npm (web utilities) |

---

## Directory Tree

```
AIGGPA_Report/
├── *.tex                        # LaTeX source files (6 active)
├── Organized_Archive/
│   ├── 01_PDFs/                 # All compiled PDFs
│   ├── 02_Build_Artifacts/      # .aux .log .out .toc (safe to delete)
│   ├── 03_Node_Scripts/         # JS utilities + package manifests
│   ├── 04_Prototype_Web_App/    # Reference pointer to /prototype/
│   └── index.md                 # This archive's navigation guide
├── prototype/                   # Web application prototypes (18 HTML files)
│   ├── field_survey_entry.html  # PRIMARY: Mobile field survey app
│   ├── index.html               # Dashboard / executive briefing entry
│   ├── style.css                # Shared styles
│   └── app.js                   # Shared JS logic
├── docs/                        # Supporting documentation
├── node_modules/                # [EXCLUDED from index -- npm vendor]
├── package.json
└── PROJECT_INDEX.md             # This file
```

---

## Entry Points

| Entry Point | File | Role |
|---|---|---|
| Main Research Report | `main.tex` | Compile with `xelatex main.tex` |
| Concept Proposal | `concept_proposal.tex` | Compile with `xelatex concept_proposal.tex` |
| Survey Instrument | `survey_instrument.tex` | Compile with `xelatex survey_instrument.tex` |
| Proposal Prep Guide | `proposal_prep_guide.tex` | Compile with `xelatex proposal_prep_guide.tex` |
| Web Dashboard | `prototype/index.html` | Open in browser |
| Field Survey App | `prototype/field_survey_entry.html` | Open on mobile browser |

---

## Module Map

### LaTeX Documents (Core Research)
| File | Description | Pages | Status |
|---|---|---|---|
| `main.tex` | Secondary research report on HR-IT in Indian Govt | ~40 | ✅ |
| `concept_proposal.tex` | Bilingual formal proposal | 2 | ✅ |
| `notes_from_manager.tex` | Manager diary transcription | 8 | ✅ |
| `survey_instrument.tex` | Bilingual field questionnaire | 2 | ✅ |
| `proposal_prep_guide.tex` | Proposal prep + 20-Q manager checklist | 7 | ✅ |
| `manager_questions.tex` | Initial rough notes | 2 | Archive |

### Web Prototype Modules
| File | Visualisation Type |
|---|---|
| `field_survey_entry.html` | Mobile data entry form |
| `adoption_index_barchart.html` | Bar chart -- adoption by department |
| `age_adoption_hypothesis.html` | Scatter -- age vs. adoption rate |
| `architecture_ledger.html` | Institutional hierarchy diagram |
| `composite_scoring_model.html` | Weighted scoring model |
| `maturity_ladder.html` | Technology maturity levels |
| `policy_ledger_matrix.html` | Policy impact 2x2 matrix |
| `gender_parity_index.html` | Gender parity index |

---

## External Dependencies

### LaTeX (MiKTeX packages)
`fontspec`, `xcolor`, `tcolorbox`, `enumitem`, `booktabs`, `tabularx`, `fancyhdr`, `hyperref`, `titlesec`, `pgfplots`, `tikz`, `wasysym`, `geometry`, `amssymb`

### Node.js
See `Organized_Archive/03_Node_Scripts/package.json`. Primary dependency: `puppeteer` (for prototype screenshot capture).

---

## Change Hotspots (Git Analysis)

| Commit | Message | Impact |
|---|---|---|
| `ec80fd2` | Launch AIGGPA Project | Initial project setup |
| `da12df8` | Refactor: Sovereign Command Center dashboard | Prototype revamp |

*Note: Repository has 2 commits. Full hotspot analysis will be possible after sustained development.*

---

## Risk Flags

- ⚠️ `node_modules/` is present but in `.gitignore` -- verify `.gitignore` is committed
- ⚠️ PDF files in root were generated from `.tex` -- not tracked in git (added to `.gitignore`)
- ✅ No secrets or API keys found in any source file
- ✅ All `.tex` source files are self-contained and compile independently

---

## Freshness Metadata

```json
{
  "generated_at": "2026-04-08T06:45:00Z",
  "commit_hash": "ec80fd2",
  "files_indexed": 30,
  "staleness_threshold_days": 7,
  "freshness_score": 100,
  "next_reindex_recommended": "2026-04-15"
}
```
