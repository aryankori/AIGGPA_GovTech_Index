import textwrap

Q = {
"Revenue": {
    "tools": "MP Bhulekh / WebGIS 2.0, RCMS (Revenue Case Management System), SAARA (Smart Application for Revenue Administration), SAMPADA 2.0 (Registration \\& Stamps), e-Court / e-Filing",
    "items": [
        {"construct":"Facilitating Conditions (FC)","dimension":"Department-Specific Tool Awareness","indicator":"Awareness of Revenue-specific digital platforms","item":"Which of the following Revenue department digital tools are you aware of? (Select all that apply)","scale":"Multi-select Checklist (MP Bhulekh/WebGIS 2.0 / RCMS / SAARA / SAMPADA 2.0 / e-Court/e-Filing / None)","justification":"Revenue department operates a distinct digital ecosystem for land records, case management, and registration. Awareness must be measured at the department-specific tool level, not just generic tools, to identify precise FC gaps (Ndou, 2004)."},
        {"construct":"Performance Expectancy (PE)","dimension":"Task-Technology Fit (Land Records)","indicator":"Perceived usefulness of Bhulekh/WebGIS for land record management","item":"To what extent has the MP Bhulekh/WebGIS 2.0 portal improved the speed and accuracy of land record verification in your office?","scale":"5-point Improvement Scale (1=No improvement to 5=Greatly improved)","justification":"Land record digitisation is the flagship digital intervention in Revenue; measuring its perceived impact directly tests PE for the department's core workflow (Davis, 1989)."},
        {"construct":"Effort Expectancy (EE)","dimension":"System Complexity (RCMS)","indicator":"Perceived difficulty of using RCMS for case tracking","item":"How difficult do you find the Revenue Case Management System (RCMS) to use for tracking and managing revenue cases?","scale":"5-point Likert (1=Very Easy to 5=Very Difficult)","justification":"RCMS is a complex workflow system requiring multi-step data entry; high EE here indicates need for role-specific RCMS training rather than generic IT training (Venkatesh et al., 2003)."},
        {"construct":"Facilitating Conditions (FC)","dimension":"Data Migration Challenges","indicator":"Extent of legacy paper records still requiring manual processing","item":"What percentage of revenue cases or land records in your office still require reference to physical (paper) files that have not been digitised?","scale":"Categorical (0-20 percent / 21-40 percent / 41-60 percent / 61-80 percent / 81-100 percent)","justification":"Incomplete digitisation of legacy records is a Revenue-specific FC barrier; even with functional digital tools, employees are forced into hybrid workflows if historical data remains on paper (Heeks, 2006)."},
        {"construct":"Social Influence (SI)","dimension":"Citizen-Facing Pressure","indicator":"Frequency of citizen enquiries that require digital tool usage","item":"How often do citizens or applicants visit your office expecting services that require you to use digital tools (e.g., online land record verification, e-stamp)?","scale":"5-point Frequency (1=Never to 5=Multiple times daily)","justification":"Revenue is a high-volume citizen-facing department; external demand for digital services creates SI pressure that may accelerate adoption independently of internal mandates (Cordella \\& Bonina, 2012)."},
    ]
},
"Rural Development": {
    "tools": "NREGASoft MIS / NMMS App (MGNREGA), e-Gram Swaraj, PMAY-G Portal, SBM-G Portal, Panchayat Darpan, PFMS",
    "items": [
        {"construct":"Facilitating Conditions (FC)","dimension":"Department-Specific Tool Awareness","indicator":"Awareness of Rural Development digital platforms","item":"Which of the following Rural Development department digital tools are you aware of? (Select all that apply)","scale":"Multi-select Checklist (NREGASoft/NMMS App / e-Gram Swaraj / PMAY-G Portal / SBM-G Portal / Panchayat Darpan / PFMS / None)","justification":"Rural Development operates the highest number of scheme-specific MIS portals; awareness fragmentation across multiple platforms is a unique FC challenge for this department."},
        {"construct":"Effort Expectancy (EE)","dimension":"Multi-Portal Burden","indicator":"Perceived difficulty of managing multiple scheme portals simultaneously","item":"How difficult do you find it to manage and update data across multiple portals (e.g., NREGASoft, e-Gram Swaraj, PMAY-G) simultaneously?","scale":"5-point Likert (1=Very Easy to 5=Very Difficult)","justification":"Unlike other departments, Rural Development staff must operate 4-6 separate MIS platforms daily; this multi-portal burden is a department-specific EE barrier not captured by generic difficulty questions (Venkatesh et al., 2003)."},
        {"construct":"Facilitating Conditions (FC)","dimension":"Field-Level Connectivity","indicator":"Reliability of internet access at block/panchayat level offices","item":"When working at block-level or panchayat-level offices, how would you rate the internet connectivity available for uploading data to portals?","scale":"5-point Likert (1=No connectivity to 5=Excellent)","justification":"Rural Development uniquely operates at the panchayat/block level where connectivity is significantly worse than district HQs; this tests FC at the actual operational level rather than the office level (World Bank, 2016)."},
        {"construct":"Performance Expectancy (PE)","dimension":"Geo-Tagging \\& Mobile Monitoring","indicator":"Perceived usefulness of NMMS app for field verification","item":"To what extent has the NMMS (National Mobile Monitoring System) app improved the accuracy of attendance and worksite verification under MGNREGA?","scale":"5-point Improvement Scale (1=No improvement to 5=Greatly improved)","justification":"NMMS mandates real-time geo-tagged attendance; testing its perceived impact measures PE for mobile-first field monitoring tools specific to rural schemes (Government of India, 2020)."},
        {"construct":"Effort Expectancy (EE)","dimension":"Data Entry Burden","indicator":"Time spent on digital data entry vs. fieldwork","item":"On average, what proportion of your working day is spent on entering data into various portals and MIS systems?","scale":"Categorical (Less than 1 hour / 1-2 hours / 2-4 hours / More than 4 hours / Almost the entire day)","justification":"A known complaint in Rural Development is that portal compliance consumes time meant for field implementation; quantifying this tests whether digital tools enhance or impede actual service delivery (Heeks, 2003)."},
    ]
},
"Forest": {
    "tools": "e-Green Watch (CAMPA), AI-Based Forest Alert System, GIS/Remote Sensing platforms, Forest Offence Tracking MIS, Nursery Management System",
    "items": [
        {"construct":"Facilitating Conditions (FC)","dimension":"Department-Specific Tool Awareness","indicator":"Awareness of Forest department digital platforms","item":"Which of the following Forest department digital tools are you aware of? (Select all that apply)","scale":"Multi-select Checklist (e-Green Watch / AI Forest Alert System / GIS/Remote Sensing tools / Forest Offence MIS / Nursery Management System / None)","justification":"Forest department has a unique tech stack combining GIS, AI-based monitoring, and field verification apps; awareness must be measured at this specialised tool level to identify FC gaps."},
        {"construct":"Performance Expectancy (PE)","dimension":"AI \\& Satellite Monitoring","indicator":"Perceived usefulness of AI-based alert system for forest protection","item":"If your division uses the AI-based forest alert system, to what extent has it improved your ability to detect illegal activities (encroachment, felling) compared to manual patrolling?","scale":"5-point Improvement Scale (1=No improvement to 5=Greatly improved) + Not applicable option","justification":"MP is the first state to pilot AI-based forest alerts; measuring PE for this cutting-edge tool provides evidence on whether advanced technology translates to field-level impact (Davis, 1989)."},
        {"construct":"Effort Expectancy (EE)","dimension":"GIS Proficiency","indicator":"Perceived difficulty of using GIS and remote sensing tools","item":"How difficult do you find it to use GIS-based tools (e.g., mapping forest boundaries, interpreting satellite imagery, geo-tagging field reports)?","scale":"5-point Likert (1=Very Easy to 5=Very Difficult)","justification":"GIS requires specialised skills not covered by generic IT training; high EE for GIS indicates need for domain-specific technical capacity building unique to the Forest department (Venkatesh et al., 2003)."},
        {"construct":"Facilitating Conditions (FC)","dimension":"Field Equipment","indicator":"Availability of GPS-enabled devices and field equipment","item":"Do you have access to GPS-enabled devices (smartphones, handheld GPS units) required for field verification, geo-tagging, and alert response?","scale":"Categorical (Yes, department-issued / Yes, I use my personal device / No, not available)","justification":"Forest field operations require GPS-enabled hardware for alert verification and geo-tagged reporting; unlike office-based departments, FC here includes rugged field equipment, not just desktop computers (Venkatesh et al., 2003)."},
        {"construct":"Effort Expectancy (EE)","dimension":"Remote Area Operations","indicator":"Challenges of using digital tools in forest/remote terrain","item":"How often does poor network coverage in forest areas prevent you from using digital tools (uploading reports, responding to alerts, accessing portals) during field duty?","scale":"5-point Frequency (1=Never to 5=Always)","justification":"Forest staff operate in terrain with minimal cellular coverage; this department-specific EE barrier cannot be captured by office-centric connectivity questions and requires offline-capable tool recommendations (Heeks, 2006)."},
    ]
},
"Health": {
    "tools": "ANMOL MP (ANM Online), HMIS, Nikshay (TB Portal), eVIN (Vaccine Cold Chain), IHIP (Disease Surveillance), Ayushman Bharat/ABHA, MPCDSR",
    "items": [
        {"construct":"Facilitating Conditions (FC)","dimension":"Department-Specific Tool Awareness","indicator":"Awareness of Health department digital platforms","item":"Which of the following Health department digital tools are you aware of? (Select all that apply)","scale":"Multi-select Checklist (ANMOL MP / HMIS / Nikshay / eVIN / IHIP / Ayushman Bharat-ABHA / MPCDSR / None)","justification":"Health operates the most disease- and programme-specific portals; each serves a distinct public health function, and awareness gaps in any single tool can have patient safety implications."},
        {"construct":"Performance Expectancy (PE)","dimension":"Patient Tracking \\& Continuity","indicator":"Perceived usefulness of ANMOL/ABHA for patient record management","item":"To what extent has the use of ANMOL MP or ABHA Health IDs improved your ability to track and follow up with patients (pregnant women, infants, TB patients) across visits?","scale":"5-point Improvement Scale (1=No improvement to 5=Greatly improved)","justification":"Continuity of care is the core PE outcome for Health; digital patient tracking should reduce loss-to-follow-up, and measuring this tests whether PE translates to actual health service improvement (Davis, 1989)."},
        {"construct":"Effort Expectancy (EE)","dimension":"Dual Documentation Burden","indicator":"Extent of duplicate data entry across paper registers and digital systems","item":"How often are you required to enter the same patient or programme data in both paper registers AND digital systems (e.g., HMIS, ANMOL)?","scale":"5-point Frequency (1=Never to 5=Always)","justification":"Health workers frequently maintain parallel paper and digital records due to incomplete digital trust; this dual burden is a Health-specific EE barrier that increases workload without proportional benefit (Heeks, 2003)."},
        {"construct":"Facilitating Conditions (FC)","dimension":"Cold Chain \\& Supply Monitoring","indicator":"Usage and reliability of eVIN for vaccine stock management","item":"How reliably does the eVIN system reflect the actual vaccine stock and cold chain temperature status at your facility?","scale":"5-point Likert (1=Very Unreliable to 5=Very Reliable)","justification":"eVIN accuracy directly affects vaccine wastage and availability; unreliable data in eVIN indicates FC failure in a system where inaccuracy has direct patient health consequences (United Nations, 2024)."},
        {"construct":"Social Influence (SI)","dimension":"Real-Time Surveillance Pressure","indicator":"Impact of IHIP disease surveillance reporting requirements on workflow","item":"To what extent do mandatory real-time disease reporting requirements (through IHIP) add to your daily workload?","scale":"5-point Likert (1=No additional burden to 5=Significant additional burden)","justification":"IHIP mandates real-time outbreak reporting, creating compliance-driven SI; testing whether this is perceived as productive surveillance or bureaucratic burden reveals whether SI enhances or undermines adoption (Venkatesh et al., 2003)."},
    ]
},
}

def esc(s):
    return s.replace('%','\\%').replace('#','\\#').replace('_','\\_')

header = r"""\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{inputenc}\usepackage[T1]{fontenc}\usepackage{mathptmx}
\usepackage[margin=2.2cm]{geometry}\usepackage{booktabs}\usepackage{tabularx}
\usepackage{array}\usepackage{xcolor}\usepackage{titlesec}\usepackage{enumitem}
\usepackage{hyperref}\usepackage{fancyhdr}\usepackage{setspace}\usepackage{parskip}
\usepackage{float}\usepackage{colortbl}

\definecolor{navy}{HTML}{1B2A4A}\definecolor{gold}{HTML}{C49A2A}
\definecolor{dk}{HTML}{2D2D2D}\definecolor{mg}{HTML}{4A4A4A}
\definecolor{sb}{HTML}{D6E4F0}\definecolor{sg}{HTML}{DFF0D8}
\definecolor{so}{HTML}{FDEBD0}\definecolor{sp}{HTML}{E8DAEF}
\definecolor{sr}{HTML}{FADBD8}

\definecolor{revcol}{HTML}{2E5090}\definecolor{rdcol}{HTML}{2E7D32}
\definecolor{forcol}{HTML}{E65100}\definecolor{hlcol}{HTML}{6A1B9A}
\definecolor{revbg}{HTML}{D6E4F0}\definecolor{rdbg}{HTML}{DFF0D8}
\definecolor{forbg}{HTML}{FDEBD0}\definecolor{hlbg}{HTML}{E8DAEF}

\titleformat{\section}{\Large\bfseries\color{navy}}{\thesection}{1em}{}[\vspace{-4pt}{\color{gold}\rule{\textwidth}{1.5pt}}]
\titleformat{\subsection}{\large\bfseries\color{navy}}{\thesubsection}{1em}{}
\setlength{\headheight}{14pt}\pagestyle{fancy}\fancyhf{}
\fancyhead[L]{\small\color{mg}\textit{AIGGPA --- Department-Specific Schedule}}
\fancyhead[R]{\small\color{mg}\textit{April 2026}}
\fancyfoot[C]{\small\color{mg}\thepage}
\renewcommand{\headrulewidth}{0.4pt}
\hypersetup{colorlinks=true,linkcolor=navy,citecolor=navy,urlcolor=navy}
\setstretch{1.1}
\newcolumntype{L}[1]{>{\raggedright\arraybackslash}p{#1}}
\newcolumntype{C}[1]{>{\centering\arraybackslash}p{#1}}

\newcommand{\qcard}[8]{%
\noindent\begin{tabularx}{\textwidth}{@{}>{\columncolor{#7}\bfseries\small}L{3.2cm}|X@{}}
\arrayrulecolor{#8}\hline
Theoretical Construct & #1 \\
Dimension & #2 \\
Operational Indicator & #3 \\
\arrayrulecolor{gold}\hline
\rowcolor{white}\textbf{\color{#8}Survey Item} & \textbf{\color{#8}#4} \\
\arrayrulecolor{gold}\hline
Data Type \& Scale & #5 \\
Justification & \textit{#6} \\
\arrayrulecolor{#8}\hline
\end{tabularx}\vspace{10pt}
}

\begin{document}
\begin{titlepage}\centering
\vspace*{2.5cm}
{\color{gold}\rule{0.6\textwidth}{2pt}}\vspace{1cm}
{\Huge\bfseries\color{navy} DEPARTMENT-SPECIFIC\\[6pt] QUESTIONNAIRE SUPPLEMENT}\vspace{0.5cm}
{\Large\color{dk} Structured Schedule Items Tailored to\\[4pt] Revenue, Rural Development, Forest \& Health}\vspace{1cm}
{\color{gold}\rule{0.6\textwidth}{2pt}}\vspace{2cm}
{\large\color{mg} This document supplements the main questionnaire (39 items)\\[4pt] with 20 department-specific questions --- 5 per department ---\\[4pt] targeting the unique digital ecosystems of each department.}\vspace{2cm}
\begin{tabular}{r l}
\textbf{\color{navy}Prepared By:} & Aryan Kori \\[6pt]
\textbf{\color{navy}Institution:} & AIGGPA, Bhopal \\[6pt]
\textbf{\color{navy}Date:} & April 2026 \\
\end{tabular}
\vfill
{\small\color{mg} Administer only the section relevant to the respondent's department.}
\end{titlepage}
\tableofcontents\newpage

\section*{How to Use This Supplement}
\addcontentsline{toc}{section}{How to Use This Supplement}
This document contains \textbf{20 department-specific questions} (5 per department) designed to complement the 39-item main questionnaire. Each respondent receives \textbf{only the section matching their department}, resulting in a total instrument of 39~+~5~=~\textbf{44 questions per respondent}.

\begin{table}[H]\centering\small
\begin{tabularx}{\textwidth}{L{3.5cm} L{3cm} X}
\toprule
\textbf{Department} & \textbf{Questions} & \textbf{Key Digital Ecosystem} \\
\midrule
\textcolor{revcol}{\textbf{Revenue}} & Q40--Q44 & Bhulekh/WebGIS, RCMS, SAARA, SAMPADA \\[4pt]
\textcolor{rdcol}{\textbf{Rural Development}} & Q45--Q49 & NREGASoft/NMMS, e-Gram Swaraj, PMAY-G, SBM-G \\[4pt]
\textcolor{forcol}{\textbf{Forest}} & Q50--Q54 & e-Green Watch, AI Alert System, GIS/Remote Sensing \\[4pt]
\textcolor{hlcol}{\textbf{Health}} & Q55--Q59 & ANMOL MP, HMIS, Nikshay, eVIN, IHIP, ABHA \\
\bottomrule
\end{tabularx}
\end{table}
\newpage
"""

footer = r"""
\newpage
\section{Pre-Fieldwork: Questions for Your Manager}

Before beginning data collection, clarify the following with your supervisor/manager. These questions are organised by category and are designed to prevent scope misalignment, logistical delays, and institutional friction during your 3-month timeline.

\subsection{Scope \& Expectations}
\begin{table}[H]\centering\small
\begin{tabularx}{\textwidth}{C{0.8cm} X L{5cm}}
\toprule
\textbf{\#} & \textbf{Question} & \textbf{Why This Matters} \\
\midrule
1 & What is the exact scope of ``digital tools'' for this study --- only government-mandated platforms, or also informal tools (WhatsApp, personal email)? & Prevents scope creep; defines what counts as ``digital adoption'' \\[6pt]
2 & Are there any departments or offices that are off-limits or politically sensitive for data collection? & Avoids institutional friction early \\[6pt]
3 & What is the primary deliverable you expect --- a research report, a policy brief, a presentation, or all three? & Aligns output format with institutional expectations \\[6pt]
4 & Should findings be reported at department level, district level, or both? & Determines the level of disaggregation in analysis \\
\bottomrule
\end{tabularx}
\end{table}

\subsection{Access \& Permissions}
\begin{table}[H]\centering\small
\begin{tabularx}{\textwidth}{C{0.8cm} X L{5cm}}
\toprule
\textbf{\#} & \textbf{Question} & \textbf{Why This Matters} \\
\midrule
5 & Will AIGGPA provide an official letter of introduction / authorisation for me to visit department offices? & Government employees may not cooperate without formal institutional backing \\[6pt]
6 & Who is my point of contact in each department for scheduling interviews and office visits? & Prevents wasted time trying to navigate bureaucratic hierarchies independently \\[6pt]
7 & Do I need separate ethical clearance or IRB approval, or does the AIGGPA internship authorisation suffice? & Ensures data collection is institutionally legitimate \\
\bottomrule
\end{tabularx}
\end{table}

\subsection{Logistics \& Timeline}
\begin{table}[H]\centering\small
\begin{tabularx}{\textwidth}{C{0.8cm} X L{5cm}}
\toprule
\textbf{\#} & \textbf{Question} & \textbf{Why This Matters} \\
\midrule
8 & What is the realistic timeline for completing fieldwork --- is the full 3 months available, or are there institutional deadlines (reviews, presentations) that shorten it? & Allows backward-planning from hard deadlines \\[6pt]
9 & Is there a budget for travel to District Offices, or should data collection be limited to Bhopal-based offices? & Determines whether the HO vs.\ DO comparison is feasible \\[6pt]
10 & How frequently should I provide progress updates --- weekly, fortnightly, or milestone-based? & Sets reporting cadence and prevents surprise reviews \\[6pt]
11 & Can I audio-record interviews (with consent), or is there an institutional restriction? & Determines whether verbatim transcription is possible for thematic analysis \\
\bottomrule
\end{tabularx}
\end{table}

\subsection{Data \& Confidentiality}
\begin{table}[H]\centering\small
\begin{tabularx}{\textwidth}{C{0.8cm} X L{5cm}}
\toprule
\textbf{\#} & \textbf{Question} & \textbf{Why This Matters} \\
\midrule
12 & Should individual respondents be anonymised in the final report, or can designations be mentioned? & Determines the anonymisation protocol for qualitative quotes \\[6pt]
13 & Can I access any existing departmental data (IT inventory, training records, helpdesk logs) to supplement survey findings? & Secondary data strengthens triangulation without adding respondent burden \\[6pt]
14 & Who owns the final data and report --- AIGGPA, the intern, or shared? & Clarifies publication and reuse rights \\
\bottomrule
\end{tabularx}
\end{table}

\subsection{Recommendations \& Impact}
\begin{table}[H]\centering\small
\begin{tabularx}{\textwidth}{C{0.8cm} X L{5cm}}
\toprule
\textbf{\#} & \textbf{Question} & \textbf{Why This Matters} \\
\midrule
15 & How actionable should the recommendations be --- broad policy suggestions, or specific implementable steps with cost estimates? & Calibrates the depth of Objective 4 deliverables \\[6pt]
16 & Is there an existing departmental digital strategy or IT roadmap that my recommendations should align with? & Prevents recommending things already planned or rejected \\[6pt]
17 & Will there be an opportunity to present findings to department heads or senior officials? & Shapes the format and tone of the final deliverable \\
\bottomrule
\end{tabularx}
\end{table}

\newpage
\section*{References}
\addcontentsline{toc}{section}{References}
\begin{enumerate}[leftmargin=1.5em,itemsep=3pt,label={[\arabic*]}]
\item Cordella, A., \& Bonina, C. M. (2012). A public value perspective for ICT enabled public sector reforms. \textit{Government Information Quarterly}, 29(4), 512--520.
\item Davis, F. D. (1989). Perceived usefulness, perceived ease of use, and user acceptance of information technology. \textit{MIS Quarterly}, 13(3), 319--340.
\item Government of India, Dept.\ of Personnel \& Training. (2020). \textit{Mission Karmayogi}.
\item Heeks, R. (2003). Most eGovernment-for-Development Projects Fail. University of Manchester.
\item Heeks, R. (2006). \textit{Implementing and Managing eGovernment}. Sage Publications.
\item Ndou, V. (2004). E-government for developing countries. \textit{EJISDC}, 18(1), 1--24.
\item United Nations. (2024). \textit{E-Government Survey 2024}. UN DESA.
\item Venkatesh, V., Morris, M. G., Davis, G. B., \& Davis, F. D. (2003). User acceptance of information technology. \textit{MIS Quarterly}, 27(3), 425--478.
\item World Bank. (2016). \textit{World Development Report 2016: Digital Dividends}.
\end{enumerate}
\end{document}
"""

dept_meta = {
    "Revenue": ("revcol","revbg","revcol"),
    "Rural Development": ("rdcol","rdbg","rdcol"),
    "Forest": ("forcol","forbg","forcol"),
    "Health": ("hlcol","hlbg","hlcol"),
}

dept_functions = {
    "Revenue": r"""
\begin{table}[H]\centering\small
\begin{tabularx}{\textwidth}{L{3cm} X}
\toprule
\textbf{Core Function} & \textbf{Description} \\
\midrule
Land Record Management & Maintenance, mutation, and verification of land ownership records (Khasra, B-1, land maps) \\[3pt]
Revenue Case Adjudication & Hearing and disposal of revenue disputes (demarcation, partition, succession) through Tehsil and SDM courts \\[3pt]
Registration \& Stamps & Registration of property sale/purchase deeds, lease agreements, and collection of stamp duty \\[3pt]
Revenue Collection & Collection of land revenue, cess, and other government dues at tehsil/district level \\[3pt]
Disaster \& Relief & Assessment and disbursement of crop damage compensation and disaster relief under SDRF/NDRF \\
\bottomrule
\end{tabularx}
\end{table}
""",
    "Rural Development": r"""
\begin{table}[H]\centering\small
\begin{tabularx}{\textwidth}{L{3cm} X}
\toprule
\textbf{Core Function} & \textbf{Description} \\
\midrule
Employment Guarantee & Implementation of MGNREGA --- job card issuance, work allocation, muster rolls, and wage disbursement \\[3pt]
Rural Housing & Beneficiary identification, sanctioning, fund transfer, and geo-tagged monitoring under PMAY-Gramin \\[3pt]
Panchayat Governance & Digital planning, accounting, and reporting for Gram Panchayats via e-Gram Swaraj and GPDP preparation \\[3pt]
Sanitation (SBM-G) & Tracking ODF Plus status, toilet construction, solid/liquid waste management at village level \\[3pt]
Rural Infrastructure & Planning and monitoring of roads, bridges, and public buildings through Rural Engineering Services \\
\bottomrule
\end{tabularx}
\end{table}
""",
    "Forest": r"""
\begin{table}[H]\centering\small
\begin{tabularx}{\textwidth}{L{3cm} X}
\toprule
\textbf{Core Function} & \textbf{Description} \\
\midrule
Forest Protection & Patrolling, detection and prosecution of illegal felling, encroachment, poaching, and forest fires \\[3pt]
Wildlife Conservation & Monitoring of tiger reserves, national parks, and wildlife corridors; anti-poaching operations \\[3pt]
Afforestation (CAMPA) & Planning, execution, and geo-tagged monitoring of compensatory afforestation and plantation drives \\[3pt]
Forest Inventory & Maintaining updated records of forest area, tree density, species distribution using GIS/remote sensing \\[3pt]
Community Forestry & Joint Forest Management (JFM), tribal rights under FRA, and eco-tourism management \\
\bottomrule
\end{tabularx}
\end{table}
""",
    "Health": r"""
\begin{table}[H]\centering\small
\begin{tabularx}{\textwidth}{L{3cm} X}
\toprule
\textbf{Core Function} & \textbf{Description} \\
\midrule
Maternal \& Child Health & Registration, tracking, and follow-up of pregnant women, newborns, and children for ANC, immunisation, and nutrition \\[3pt]
Disease Surveillance & Real-time monitoring, reporting, and response to outbreak-prone diseases (malaria, dengue, TB, COVID) via IHIP \\[3pt]
Immunisation \& Cold Chain & Vaccine procurement, storage temperature monitoring (eVIN), and session-wise immunisation tracking \\[3pt]
TB Elimination & Case notification, treatment monitoring, DBT support, and outcome tracking under the Nikshay portal \\[3pt]
Health Assurance & Ayushman Bharat PM-JAY card issuance, hospital empanelment, and cashless treatment claim processing \\
\bottomrule
\end{tabularx}
\end{table}
""",
}

qnum = 40
body = ""
for dept in ["Revenue","Rural Development","Forest","Health"]:
    col, bg, accent = dept_meta[dept]
    info = Q[dept]
    body += f"\n\\section{{\\textcolor{{{col}}}{{{dept} Department}}}}\n\n"
    body += f"\\textbf{{Core Functions:}}\n{dept_functions[dept]}\n"
    body += f"\\textbf{{Key Digital Tools:}} {info['tools']}\n\n"
    for q in info["items"]:
        short = q["item"][:85] + "..." if len(q["item"])>85 else q["item"]
        body += f"\\subsection*{{Q{qnum}. {esc(short)}}}\n"
        body += f"\\qcard{{{esc(q['construct'])}}}{{{esc(q['dimension'])}}}{{{esc(q['indicator'])}}}{{{esc(q['item'])}}}{{{esc(q['scale'])}}}{{{esc(q['justification'])}}}{{{bg}}}{{{accent}}}\n\n"
        qnum += 1

with open('AIGGPA_Dept_Questionnaire.tex','w',encoding='utf-8') as f:
    f.write(header + body + footer)

print(f"Done: AIGGPA_Dept_Questionnaire.tex ({qnum-40} questions, Q40-Q{qnum-1})")
