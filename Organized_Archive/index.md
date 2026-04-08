# AIGGPA_Report -- Archive Index
> Generated: 8 April 2026 | Project: AIGGPA Internship Field Research

This file maps everything in the repository. Source `.tex` files remain in the project root (required for LaTeX compilation). Everything else has been organized below.

---

## Repository Root (Active Source Files -- DO NOT MOVE)

| File | Purpose |
|------|---------|
| `main.tex` | Primary secondary research report (HR-IT in Indian Govt) |
| `concept_proposal.tex` | Formal bilingual concept proposal for manager approval |
| `notes_from_manager.tex` | Transcribed internship diary / manager meeting notes |
| `survey_instrument.tex` | Printable bilingual field survey questionnaire |
| `proposal_prep_guide.tex` | **NEW** -- Proposal structure guide + 20-question manager checklist |
| `manager_questions.tex` | Initial rough manager question notes |

---

## `Organized_Archive/`

### `01_PDFs/` -- All compiled output documents

| File | Contents |
|------|---------|
| `AIGGPA PRE REPORT.pdf` | Final compiled secondary research report |
| `concept_proposal.pdf` | Formal concept proposal (2 pages, bilingual) |
| `notes_from_manager.pdf` | Manager diary notes (8 pages) |
| `survey_instrument.pdf` | Field questionnaire (2 pages, printable) |
| `proposal_prep_guide.pdf` | Proposal prep guide with manager checklist (7 pages) |

### `02_Build_Artifacts/` -- LaTeX intermediate files (safe to delete/ignore)
`.aux`, `.log`, `.out`, `.toc` files from all LaTeX compilations. Not needed for reading -- only for incremental compilation.

### `03_Node_Scripts/` -- JavaScript utilities
| File | Purpose |
|------|---------|
| `capture_prototypes.js` | Puppeteer script to screenshot prototype HTML files |
| `package.json` | Node dependencies declaration |
| `package-lock.json` | Exact dependency lock file |

### `04_Prototype_Web_App/` -- Reference pointer
See `prototype/` folder in root for all web app files. Kept outside archive for web server compatibility.

---

## `prototype/` -- Field Survey Web Application

| File | Purpose |
|------|---------|
| `index.html` | Main dashboard / executive briefing |
| `field_survey_entry.html` | **Mobile data entry app for field surveys** |
| `executive_briefing.html` | Interactive research executive summary |
| `adoption_index_barchart.html` | Visual adoption index chart |
| `age_adoption_hypothesis.html` | Age vs. adoption hypothesis visual |
| `architecture_ledger.html` | Institutional architecture diagram |
| `comparison_report.html` | Cross-department comparison |
| `composite_scoring_model.html` | Composite adoption scoring model |
| `data_pipeline_flowchart.html` | Data pipeline flow diagram |
| `editorial_infographic.html` | Infographic for presentations |
| `gender_parity_index.html` | Gender parity analysis in IT adoption |
| `maturity_ladder.html` | Technology maturity ladder visual |
| `policy_ledger_matrix.html` | Policy impact matrix |
| `research_timeline.html` | Research project timeline |
| `scope_analysis.html` | Scope and limitations analysis |
| `style.css` | Shared CSS for all prototype pages |
| `app.js` | Shared JavaScript logic |

---

## `docs/` -- Supporting documentation
*(Contents to be confirmed)*

---

## Field Research Status

| Deliverable | Status |
|-------------|--------|
| Secondary Research Report (`main.pdf`) | ✅ Complete |
| Notes from Manager (`notes_from_manager.pdf`) | ✅ Complete |
| Concept Proposal (`concept_proposal.pdf`) | ✅ Complete |
| Survey Instrument (`survey_instrument.pdf`) | ✅ Complete |
| Proposal Prep Guide (`proposal_prep_guide.pdf`) | ✅ Complete |
| Field Data Collection (Primary Survey) | 🔲 Pending -- starts after manager approval |
| Department Intelligence Reports | ✅ Complete (see GitHub wiki / research notes) |

---

*LaTeX source files must remain in the root directory for compilation. Do not move `.tex` files.*
