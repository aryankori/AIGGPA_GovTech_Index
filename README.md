# AIGGPA_Report

> **Atal Bihari Vajpayee Institute of Good Governance & Policy Analysis, Bhopal**
> Internship Research Package -- Summer 2026

Research deliverables for the field study on **HR-IT Integration and Technology Adoption** in Madhya Pradesh Government departments (Education, Health, Forest).

---

## Documents

| File | Description | Pages |
|------|-------------|-------|
| `main.tex` | Secondary research report -- HR-IT in Indian Govt | ~40 |
| `concept_proposal.tex` | Formal bilingual concept proposal for manager | 2 |
| `notes_from_manager.tex` | Transcribed manager meeting diary | 8 |
| `survey_instrument.tex` | Printable bilingual field survey questionnaire | 2 |
| `proposal_prep_guide.tex` | Proposal prep guide + 20-Q manager checklist | 7 |

## Compile Instructions

**Requirements:** MiKTeX (Windows) with XeLaTeX + `Nirmala UI` font (built into Windows 8+)

```powershell
# Compile any document
xelatex -interaction=nonstopmode schedules/tex/main.tex
xelatex -interaction=nonstopmode schedules/tex/concept_proposal.tex
xelatex -interaction=nonstopmode schedules/tex/survey_instrument.tex
xelatex -interaction=nonstopmode schedules/tex/proposal_prep_guide.tex
```

## Fieldwork Data Vault

Research progress and raw datasets are organized in [`AIGGPA_Fieldwork_Vault/`](AIGGPA_Fieldwork_Vault/).
Open the master tracker [`AIGGPA_Fieldwork_Vault/AIGGPA_Master_Tracker.xlsx`](AIGGPA_Fieldwork_Vault/AIGGPA_Master_Tracker.xlsx) to inspect survey counts andDaily Progress logs.

## Meeting Shortcuts

All files, charts, descriptive statistics, and briefs required for the Monday 10:00 AM CEO review meeting are organized in [`AIGGPA_Fieldwork_Review/`](AIGGPA_Fieldwork_Review/). Copies have also been placed on the Desktop for instant access during the presentation.

## Web Prototype

Open `prototype/index.html` in any browser for the interactive research dashboard.

**Mobile field survey app:** `prototype/field_survey_entry.html` (open on phone/tablet)

## Repository Structure

See [`PROJECT_INDEX.md`](PROJECT_INDEX.md) for the full file map.
See [`Organized_Archive/index.md`](Organized_Archive/index.md) for the archive navigation guide.

---

*Private repository -- AIGGPA Internal Use*
