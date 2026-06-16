# AETHER_CLINICAL — Technical Architecture
> Secure Clinical Research Utilities & Psychometric Dashboard

This document provides a technical walkthrough of the **AETHER_CLINICAL** prototype system, mapping the TypeScript schemas, processing pipelines, and React component states.

---

## 1. Data Model (TypeScript Schemas)
The psychometric scoring logic, de-identification buffers, and export schemas are strongly typed in [`prototype/clinical_utils.ts`](file:///c:/Users/aryan/OneDrive/Documents/Visual%20Studio%202022/AIGGPA_Report/prototype/clinical_utils.ts).

```mermaid
classClass Diagram
classDef type font-family:var(--font-mono),fill:#1b2a4a,stroke:#c49a2a,stroke-width:1px,color:#fff;
classDef interface font-family:var(--font-mono),fill:#00695c,stroke:#00695c,stroke-width:1px,color:#fff;

class PHQ9Result {
    <<interface>>
    +number score
    +PHQ9Severity severity
    +string colorCode
}

class GAD7Result {
    <<interface>>
    +number score
    +GAD7Severity severity
    +string colorCode
}

class AnonymizedExportRecord {
    <<interface>>
    +string participantHash
    +string ageCohort
    +string studyCohort
    +number baselinePHQ9
    +number baselineGAD7
    +number activePHQ9
    +number activeGAD7
    +number adherencePercentage
    +number sleepAverageHours
}

class PHQ9Severity {
    <<type>>
    'Minimal' | 'Mild' | 'Moderate' | 'Moderately Severe' | 'Severe'
}

class GAD7Severity {
    <<type>>
    'Minimal' | 'Mild' | 'Moderate' | 'Severe'
}

PHQ9Result --> PHQ9Severity
GAD7Result --> GAD7Severity
```

---

## 2. Ingestion & scoring pipeline (Data Flow)
The workflow follows a **Zero-Knowledge / Zero PHI** protocol. Personal Health Information (PHI) is hashed on the client side before any clinical scoring or aggregation occur.

```mermaid
graph TD
    %% Define Styles
    classDef input fill:#2e7d32,color:#fff,stroke:#333,stroke-width:1px;
    classDef process fill:#1b2a4a,color:#fff,stroke:#333,stroke-width:1px;
    classDef output fill:#c49a2a,color:#fff,stroke:#333,stroke-width:1px;

    %% Data Inputs
    SubID[Raw Patient ID]:::input
    Salt[Local Secure Site Salt]:::input
    PHQ9_Q[9x Likert Answers 0-3]:::input
    GAD7_Q[7x Likert Answers 0-3]:::input

    %% Processing Functions
    HashFunc["generateParticipantHash(patientId, siteSalt)"]:::process
    PHQFunc["scorePHQ9(answers)"]:::process
    GADFunc["scoreGAD7(answers)"]:::process

    %% Data Mapping
    SubID & Salt --> HashFunc
    PHQ9_Q --> PHQFunc
    GAD7_Q --> GADFunc

    %% Interface Mappings
    HashFunc -->|SHA-256 Digest| Hash[participantHash]:::output
    PHQFunc -->|Score & Severity| PHQ_Res[PHQ9Result]:::output
    GADFunc -->|Score & Severity| GAD_Res[GAD7Result]:::output

    %% Excel/SPSS Export
    Hash & PHQ_Res & GAD_Res --> MapRecord[Map to AnonymizedExportRecord]:::process
    MapRecord --> ExportCSV["exportClinicalCSV(records)"]:::process
    ExportCSV -->|CSV Matrix Stream| CSVFile[clinical_export.csv]:::output
```

---

## 3. Client-Side Cryptographic Anonymization (Sequence)
To prevent dictionary attacks on de-identified database records, client nodes use the asynchronous browser WebCrypto API to salt and hash participant identities.

```mermaid
sequenceDiagram
    autonumber
    actor User as Researcher Client
    participant TS as clinical_utils.ts
    participant WC as WebCrypto API (SHA-256)
    
    User->>TS: generateParticipantHash(patientId, siteSalt)
    Note over TS: String concatenation & normalization:<br/>"salt:patient_id" (trimmed & lowercase)
    TS->>WC: crypto.subtle.digest('SHA-256', UTF8Buffer)
    activate WC
    WC-->>TS: ArrayBuffer (32-byte binary digest)
    deactivate WC
    Note over TS: Convert byte buffer to hex string:<br/>Array.map(b.toString(16).padStart(2, '0'))
    TS-->>User: SHA-256 Hex String (64 chars)
```

---

## 4. UI Rendering & Component State (React)
The main dashboard [`prototype/ClinicalDashboard.tsx`](file:///c:/Users/aryan/OneDrive/Documents/Visual%20Studio%202022/AIGGPA_Report/prototype/ClinicalDashboard.tsx) coordinates active tabs and filters using standard React hooks.

```mermaid
graph TD
    classDef state fill:#6a1b9a,color:#fff,stroke:#333;
    classDef render fill:#1b2a4a,color:#fff,stroke:#333;

    %% React State Variables
    State_Tab[useState: activeTab]:::state
    State_Cohort[useState: selectedCohort]:::state

    %% UI Actions
    Nav[Sidebar Navigation Bar] -->|onClick| ChangeTab[setActiveTab]:::render
    Selector[Cohort Dropdown Option] -->|onChange| ChangeCohort[setSelectedCohort]:::render

    ChangeTab --> State_Tab
    ChangeCohort --> State_Cohort

    %% Conditional Renders
    State_Tab -->|'summary'| PanelSummary[Longitudinal Outcomes & OCEAN Baselines Panel]:::render
    State_Tab -->|'psychometrics'| PanelPsych[Circadian & Somatic Correlation Graphs]:::render
    State_Tab -->|'registry'| PanelRegistry[Anonymized Participant Registry Table]:::render
    State_Tab -->|'audit'| PanelAudit[WebCrypto Secure Log Ledger]:::render

    %% Filters
    State_Cohort -->|Computes| CohortMetrics[Get Cohort Metrics: N, Adherence, Symptom Ratio]:::render
    CohortMetrics --> PanelSummary & PanelPsych & PanelRegistry
```
