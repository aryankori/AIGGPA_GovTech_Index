"""Generate 4 separate printable schedules, one per department, with expanded dept questions."""
import subprocess, os

DEPTS = {
"Revenue": {
    "tools": "MP Bhulekh / WebGIS 2.0, RCMS, SAARA, SAMPADA 2.0, e-Court / e-Filing",
    "cadre": [
        ("I", "Collector, Addl. Collector, Commissioner (LR)", "Policy, appellate authority, disaster relief, supervision of all revenue ops", "Dashboard review, MIS monitoring, SAARA/RCMS approvals"),
        ("II", "SDM, Deputy Collector, Dy. Director (LR)", "Sub-divisional case adjudication, land acquisition, magisterial functions", "RCMS case disposal, Bhulekh verification, e-Court hearings"),
        ("III", "Tehsildar, Naib Tehsildar, RI, Patwari, Computer Operator", "Land record maintenance, mutation, demarcation, Khasra/B-1 updates, data entry", "Primary Bhulekh/WebGIS users (Patwari), RCMS (Tehsildar), SAMPADA (registration) --- heaviest digital load"),
        ("IV", "Peon, Office Asst., Process Server, Chowkidar", "File movement, court summons, office upkeep, record room", "Minimal --- scanning, photocopying, carrying files to digital entry points"),
    ],
    "questions": [
        ("Q40", "Which Revenue digital tools are you aware of?",
         r"{\Large$\square$} Bhulekh/WebGIS {\Large$\square$} RCMS {\Large$\square$} SAARA {\Large$\square$} SAMPADA 2.0 {\Large$\square$} e-Court/e-Filing {\Large$\square$} None"),
        ("Q41", "Has Bhulekh/WebGIS improved speed and accuracy of land record verification in your office?",
         r"\likert"),
        ("Q42", "How difficult is RCMS to use for tracking revenue cases?",
         r"\likert{} {\scriptsize(1=Very Easy, 5=Very Difficult)}"),
        ("Q43", "What percentage of land records or revenue cases in your office still need physical paper files?",
         r"{\Large$\square$} 0--20\% {\Large$\square$} 21--40\% {\Large$\square$} 41--60\% {\Large$\square$} 61--80\% {\Large$\square$} 81--100\%"),
        ("Q44", "How often do citizens visit expecting services through digital tools (e.g., online land record, e-stamp)?",
         r"\likert{} {\scriptsize(1=Never, 5=Multiple times daily)}"),
        ("Q45", "When you process a mutation (dakhil-kharij) case, which steps do you complete digitally and which on paper?",
         r"Digitally: \rule{6cm}{0.4pt}\\[2pt] && On paper: \rule{6cm}{0.4pt}"),
        ("Q46", "Has SAMPADA 2.0 reduced the time for property registration compared to the earlier manual process?",
         r"{\Large$\square$} Much faster {\Large$\square$} Somewhat faster {\Large$\square$} No change {\Large$\square$} Slower now {\Large$\square$} Don't use it"),
        ("Q47", "How often does the Bhulekh/WebGIS portal show errors, timeouts, or incorrect map data?",
         r"{\Large$\square$} Never {\Large$\square$} Rarely {\Large$\square$} Sometimes {\Large$\square$} Often {\Large$\square$} Almost always"),
        ("Q48", "As a Patwari/RI/Tehsildar, what is the biggest obstacle to completing Khasra/B-1 updates digitally?",
         r"\rule{\linewidth}{0.4pt}\\[2pt] && \rule{\linewidth}{0.4pt}"),
        ("Q49", "Do you receive different digital tasks based on your post (e.g., Patwari does data entry, Tehsildar does approval)?",
         r"{\Large$\square$} Yes, clearly separated {\Large$\square$} Somewhat {\Large$\square$} No, everyone does the same {\Large$\square$} Don't know"),
    ],
},
"Rural Development": {
    "tools": "NREGASoft / NMMS App, e-Gram Swaraj, PMAY-G Portal, SBM-G Portal, Panchayat Darpan, PFMS",
    "cadre": [
        ("I", "CEO (Zila Panchayat), Project Director (DRDA), Joint Director", "District planning, scheme monitoring, fund allocation, convergence", "Dashboard review, PFMS fund release, e-Gram Swaraj GPDP oversight"),
        ("II", "BDO / CEO (Janpad), Asst. Project Officer, Dy. CEO", "Block-level scheme execution, staff supervision, expenditure monitoring", "NREGASoft work approval, PMAY-G sanctioning, e-Gram Swaraj uploads"),
        ("III", "GP Secretary, GRS, Accountant, DEO, Gram Sevak", "Muster rolls, wage lists, beneficiary registration, village records", "NREGASoft data entry, NMMS attendance, PMAY-G geo-tagging, SBM-G --- heaviest multi-portal load"),
        ("IV", "Peon, Office Asst., Chowkidar", "File movement, office maintenance, notice delivery", "Minimal --- may carry printed MIS reports"),
    ],
    "questions": [
        ("Q40", "Which Rural Development tools are you aware of?",
         r"{\Large$\square$} NREGASoft/NMMS {\Large$\square$} e-Gram Swaraj {\Large$\square$} PMAY-G {\Large$\square$} SBM-G {\Large$\square$} Panchayat Darpan {\Large$\square$} PFMS {\Large$\square$} None"),
        ("Q41", "How difficult is managing and updating data across multiple portals (NREGASoft, e-Gram Swaraj, PMAY-G) at the same time?",
         r"\likert{} {\scriptsize(1=Very Easy, 5=Very Difficult)}"),
        ("Q42", "Rate internet connectivity at block-level or panchayat-level offices for uploading data:",
         r"\likert{} {\scriptsize(1=No connectivity, 5=Excellent)}"),
        ("Q43", "Has the NMMS app improved accuracy of MGNREGA attendance and worksite verification?",
         r"\likert"),
        ("Q44", "How much of your working day is spent entering data into portals?",
         r"{\Large$\square$} Less than 1 hr {\Large$\square$} 1--2 hrs {\Large$\square$} 2--4 hrs {\Large$\square$} 4+ hrs {\Large$\square$} Almost the entire day"),
        ("Q45", "When preparing MGNREGA muster rolls and wage lists, which steps are digital and which are on paper?",
         r"Digitally: \rule{6cm}{0.4pt}\\[2pt] && On paper: \rule{6cm}{0.4pt}"),
        ("Q46", "Have you personally used geo-tagging (GPS photo) for PMAY-G house verification or MGNREGA worksite?",
         r"{\Large$\square$} Yes, regularly {\Large$\square$} Yes, a few times {\Large$\square$} No, someone else does it {\Large$\square$} No, never"),
        ("Q47", "When e-Gram Swaraj or NREGASoft is down or slow, what do you do?",
         r"{\Large$\square$} Wait and retry {\Large$\square$} Record on paper, upload later {\Large$\square$} Go to block office {\Large$\square$} Ask someone else {\Large$\square$} Skip the entry"),
        ("Q48", "As a GRS / Panchayat Secretary, what is the single biggest problem with portal-based reporting?",
         r"\rule{\linewidth}{0.4pt}\\[2pt] && \rule{\linewidth}{0.4pt}"),
        ("Q49", "Does the BDO / CEO review the data you upload, or is it only checked at district level?",
         r"{\Large$\square$} BDO reviews regularly {\Large$\square$} BDO checks sometimes {\Large$\square$} Only district reviews {\Large$\square$} Nobody reviews {\Large$\square$} Don't know"),
    ],
},
"Forest": {
    "tools": "e-Green Watch (CAMPA), AI Forest Alert System, GIS/Remote Sensing, Forest Offence MIS, Nursery MIS",
    "cadre": [
        ("I", "CCF, CF, DFO/DCF (IFS cadre)", "Division/circle management, CAMPA utilisation, wildlife protection policy", "e-Green Watch dashboard, AI alert monitoring, GIS planning --- review role"),
        ("II", "ACF, SDFO (SFS cadre)", "Sub-division supervision, offence prosecution, plantation monitoring", "Forest Offence MIS, e-Green Watch verification, GIS review"),
        ("III", "Range Officer (RFO), Deputy Ranger, Forester", "Patrolling, offence detection, fire management, plantation, wildlife census", "AI alert field verification with GPS, GIS data collection, Offence MIS first entry"),
        ("IV", "Forest Guard, Van Rakshak, Peon, Mali", "Beat patrolling, fire lines, nursery labour, boundary marking", "Smartphones for GPS photos/voice notes --- lowest training, highest field exposure"),
    ],
    "questions": [
        ("Q40", "Which Forest department digital tools are you aware of?",
         r"{\Large$\square$} e-Green Watch {\Large$\square$} AI Alert System {\Large$\square$} GIS/Remote Sensing {\Large$\square$} Forest Offence MIS {\Large$\square$} Nursery MIS {\Large$\square$} None"),
        ("Q41", "If your division uses the AI-based alert system, has it improved detection of illegal activity vs. manual patrolling?",
         r"\likert{}\quad{\Large$\square$} Not applicable"),
        ("Q42", "How difficult do you find GIS tools (mapping boundaries, satellite imagery, geo-tagging reports)?",
         r"\likert{} {\scriptsize(1=Very Easy, 5=Very Difficult)}"),
        ("Q43", "Do you have a GPS-enabled device for field verification and geo-tagging?",
         r"{\Large$\square$} Yes, department-issued {\Large$\square$} Yes, my personal phone {\Large$\square$} No device available"),
        ("Q44", "How often does poor network in forest areas prevent you from using digital tools during field duty?",
         r"\likert{} {\scriptsize(1=Never, 5=Always)}"),
        ("Q45", "When you receive an AI forest alert, what do you do step by step?",
         r"\rule{\linewidth}{0.4pt}\\[2pt] && \rule{\linewidth}{0.4pt}"),
        ("Q46", "When filing a Forest Offence report, which parts are done digitally and which on paper?",
         r"Digitally: \rule{6cm}{0.4pt}\\[2pt] && On paper: \rule{6cm}{0.4pt}"),
        ("Q47", "Have you received any training on using GIS, GPS devices, or the AI alert system?",
         r"{\Large$\square$} Yes, formal training {\Large$\square$} Yes, learned from colleague {\Large$\square$} Self-taught {\Large$\square$} No training at all"),
        ("Q48", "As a Forest Guard / Range Officer, what is the biggest challenge in using digital tools in the field?",
         r"\rule{\linewidth}{0.4pt}\\[2pt] && \rule{\linewidth}{0.4pt}"),
        ("Q49", "Does your DFO / ACF personally review alerts and GIS data, or is it delegated to subordinates?",
         r"{\Large$\square$} Reviews personally {\Large$\square$} Mostly delegates {\Large$\square$} Mixed {\Large$\square$} Don't know"),
    ],
},
"Health": {
    "tools": "ANMOL MP, HMIS, Nikshay (TB), eVIN (Vaccine), IHIP (Surveillance), Ayushman Bharat/ABHA, MPCDSR",
    "cadre": [
        ("I", "CMHO, Civil Surgeon, Joint/Dy. Director, Sr. Specialist", "District health admin, programme monitoring, hospital management", "HMIS dashboard, Nikshay district monitoring, Ayushman claim oversight"),
        ("II", "BMO, Medical Officer, Dist. Programme Mgr (NHM)", "PHC/CHC clinical duties, block programme implementation, data review", "HMIS validation, Nikshay notifications, IHIP reporting, ANMOL supervision"),
        ("III", "Staff Nurse, ANM, Lab Tech, Pharmacist, Health Worker, DEO", "Patient care, immunisation, ANC registration, cold chain, sample collection", "ANMOL primary users (ANMs), eVIN logging, HMIS facility entry --- heaviest routine digital load"),
        ("IV", "Ward Boy, Peon, Sweeper, Security, Ambulance Helper", "Patient handling, sanitation, equipment movement, security", "Minimal --- biometric attendance, assist with patient registration"),
    ],
    "questions": [
        ("Q40", "Which Health department digital tools are you aware of?",
         r"{\Large$\square$} ANMOL {\Large$\square$} HMIS {\Large$\square$} Nikshay {\Large$\square$} eVIN {\Large$\square$} IHIP {\Large$\square$} ABHA {\Large$\square$} MPCDSR {\Large$\square$} None"),
        ("Q41", "Has ANMOL MP or ABHA Health IDs improved your ability to track patients across visits?",
         r"\likert"),
        ("Q42", "How often do you enter the SAME data in both paper registers AND digital systems (HMIS, ANMOL)?",
         r"\likert{} {\scriptsize(1=Never, 5=Always)}"),
        ("Q43", "How reliably does eVIN reflect actual vaccine stock and cold chain temperature at your facility?",
         r"\likert{} {\scriptsize(1=Very Unreliable, 5=Very Reliable)}"),
        ("Q44", "How much does mandatory IHIP disease reporting add to your daily workload?",
         r"\likert{} {\scriptsize(1=No burden, 5=Significant burden)}"),
        ("Q45", "When registering a new pregnant woman for ANC, which steps are on ANMOL and which on paper?",
         r"On ANMOL: \rule{6cm}{0.4pt}\\[2pt] && On paper: \rule{6cm}{0.4pt}"),
        ("Q46", "For Nikshay (TB portal): do you enter case notifications yourself or does someone else do it?",
         r"{\Large$\square$} I enter myself {\Large$\square$} DEO enters {\Large$\square$} Someone at district {\Large$\square$} Don't use Nikshay {\Large$\square$} Not applicable"),
        ("Q47", "When there is a disease outbreak (malaria, dengue), how do you report it?",
         r"{\Large$\square$} IHIP portal immediately {\Large$\square$} Phone call to BMO first {\Large$\square$} Paper form to CMHO {\Large$\square$} WhatsApp message {\Large$\square$} Multiple methods"),
        ("Q48", "As an ANM / Staff Nurse / MO, what is the single biggest problem with health portals?",
         r"\rule{\linewidth}{0.4pt}\\[2pt] && \rule{\linewidth}{0.4pt}"),
        ("Q49", "Does the BMO / CMHO review the data you upload on HMIS / ANMOL?",
         r"{\Large$\square$} Reviews regularly {\Large$\square$} Checks sometimes {\Large$\square$} Only during inspections {\Large$\square$} Never {\Large$\square$} Don't know"),
    ],
},
}

# Common sections (shared across all 4 files)
def common_header(dept_name):
    return r"""\documentclass[10pt,a4paper]{article}
\usepackage[utf8]{inputenc}\usepackage[T1]{fontenc}\usepackage{mathptmx}
\usepackage[margin=0.8cm]{geometry}\usepackage{enumitem}\usepackage{tabularx}
\usepackage{array}\usepackage{booktabs}\usepackage{fancyhdr}\usepackage{setspace}
\usepackage{amssymb}
\pagestyle{fancy}\fancyhf{}
\fancyhead[L]{\small\textbf{AIGGPA --- """ + dept_name + r""" Department}}\fancyhead[R]{\small ID: \_\_\_\_\_\_\_\_}
\fancyfoot[C]{\small Page \thepage}\renewcommand{\headrulewidth}{0.5pt}
\setlength{\headheight}{14pt}\setstretch{1.1}
\newcolumntype{L}[1]{>{\raggedright\arraybackslash}p{#1}}
\newcommand{\likert}{{\Large$\square$}\,1\quad{\Large$\square$}\,2\quad{\Large$\square$}\,3\quad{\Large$\square$}\,4\quad{\Large$\square$}\,5}
\newcommand{\yesno}{{\Large$\square$}\,Yes\quad{\Large$\square$}\,No}
\newcommand{\blank}{\rule{8cm}{0.4pt}}
\begin{document}
"""

def cover(dept_name, tools, cadre):
    cadre_rows = ""
    for cls, desig, work, digital in cadre:
        cadre_rows += f"\\textbf{{Class {cls}}} & {desig} & {work} & {digital} \\\\[2pt]\n"
    return r"""
\begin{center}
{\Large\bfseries AIGGPA FIELD RESEARCH SCHEDULE}\\[3pt]
{\large\bfseries """ + dept_name + r""" Department}\\[3pt]
{\small Assessment of Digital Tool Usage Among Government Employees}\\[2pt]
{\small AIGGPA Bhopal \quad$\bullet$\quad 2026}
\end{center}
\vspace{4pt}\noindent\rule{\textwidth}{1pt}\vspace{4pt}
\noindent\begin{tabularx}{\textwidth}{@{}L{7cm} L{7cm}@{}}
\textbf{Respondent ID:} \blank & \textbf{Date:} \_\_\_/\_\_\_/2026 \\[3pt]
\textbf{Office:} {\Large$\square$} Head Office\quad{\Large$\square$} District Office & \textbf{Start:} \_\_:\_\_\quad\textbf{End:} \_\_:\_\_ \\[3pt]
\textbf{Interviewer:} \blank & \\
\end{tabularx}
\vspace{4pt}\noindent\rule{\textwidth}{0.5pt}\vspace{4pt}

\noindent\textbf{Key Digital Tools:} """ + tools + r"""

\vspace{3pt}

\vspace{4pt}\noindent\rule{\textwidth}{0.5pt}
"""

COMMON_SECTIONS = r"""
\vspace{3pt}
\noindent{\large\bfseries Section A: Respondent Profile}\vspace{4pt}

\noindent\begin{tabularx}{\textwidth}{@{}L{0.6cm} L{7.5cm} X@{}}
Q1 & Designation / Post: & \blank \\[3pt]
Q2 & Job Role / Level: & \blank \\[3pt]
Q3 & Age group: & {\Large$\square$} Below 30\quad{\Large$\square$} 30--45\quad{\Large$\square$} 46--60 \\[3pt]
Q4 & Gender: & {\Large$\square$} Male\quad{\Large$\square$} Female\quad{\Large$\square$} Other \\[3pt]
Q5 & Years of service: & {\Large$\square$} 0--5\quad{\Large$\square$} 6--10\quad{\Large$\square$} 11--20\quad{\Large$\square$} 21+ \\[3pt]
Q6 & Highest education: & {\Large$\square$} Up to 12th\quad{\Large$\square$} Graduate\quad{\Large$\square$} PG\quad{\Large$\square$} Professional \\
\end{tabularx}

\vspace{4pt}
\noindent{\large\bfseries Section B: Infrastructure}\vspace{2pt}

\small\textit{Likert: 1=Strongly Disagree/Very Poor \quad 2=Disagree/Poor \quad 3=Neutral \quad 4=Agree/Good \quad 5=Strongly Agree/Excellent}\normalsize\vspace{4pt}

\noindent\begin{tabularx}{\textwidth}{@{}L{0.6cm} X L{5.5cm}@{}}
Q7 & Devices at your workstation: & {\Large$\square$} Desktop {\Large$\square$} Laptop {\Large$\square$} Tablet {\Large$\square$} Phone {\Large$\square$} None \\[3pt]
Q8 & Share device with others? & {\Large$\square$} Yes, always {\Large$\square$} Sometimes {\Large$\square$} No, dedicated \\[3pt]
Q9 & Rate internet connectivity: & \likert \\[3pt]
Q10 & Internet outages per week: & {\Large$\square$} Never {\Large$\square$} 1--2 {\Large$\square$} 3--5 {\Large$\square$} Daily \\[3pt]
Q11 & IT support available? & \yesno \\[3pt]
Q12 & Issue resolution time: & {\Large$\square$} Same day {\Large$\square$} 2--3 days {\Large$\square$} 1 week+ {\Large$\square$} Never \\
\end{tabularx}

\vspace{4pt}
\noindent{\large\bfseries Section C: Performance Expectancy}\vspace{4pt}

\noindent\begin{tabularx}{\textwidth}{@{}L{0.6cm} X L{5.5cm}@{}}
Q13 & Digital tools help me complete tasks faster than paper. & \likert \\[3pt]
Q14 & Digital tools improve accuracy of my work. & \likert \\[3pt]
Q15 & Using digital tools increases my overall productivity. & \likert \\[3pt]
Q16 & Digital tools are well-suited to my actual job tasks. & \likert \\
\end{tabularx}

\vspace{4pt}
\noindent{\large\bfseries Section D: Effort Expectancy}\vspace{4pt}

\noindent\begin{tabularx}{\textwidth}{@{}L{0.6cm} X L{5.5cm}@{}}
Q17 & How difficult are digital tools to use? & \likert{} {\scriptsize(1=Easy, 5=Difficult)} \\[3pt]
Q18 & I am confident using digital tools for work. & \likert \\[3pt]
Q19 & Learning a new portal takes me: & {\Large$\square$} <1 day {\Large$\square$} Few days {\Large$\square$} 1--2 weeks {\Large$\square$} >2 weeks \\[3pt]
Q20 & Government portal interfaces are user-friendly. & \likert \\
\end{tabularx}

\vspace{4pt}
\noindent{\large\bfseries Section E: Social Influence \& Awareness}\vspace{4pt}

\noindent\begin{tabularx}{\textwidth}{@{}L{0.6cm} X L{5.5cm}@{}}
Q21 & Superiors encourage digital tool use. & \likert \\[3pt]
Q22 & Colleagues regularly use digital tools. & \likert \\[3pt]
Q23 & Formal mandate exists for digital tool use? & {\Large$\square$} Yes {\Large$\square$} No {\Large$\square$} Don't know \\[3pt]
Q24 & General tools you know: & {\Large$\square$} e-Office {\Large$\square$} CM Helpline {\Large$\square$} PFMS {\Large$\square$} SPARROW {\Large$\square$} iGOT {\Large$\square$} eDistrict \\[3pt]
Q25 & How often do you use digital tools? & {\Large$\square$} Daily {\Large$\square$} Weekly {\Large$\square$} Monthly {\Large$\square$} Rarely {\Large$\square$} Never \\[3pt]
Q26 & Percentage of work done digitally: & {\Large$\square$} 0--20\% {\Large$\square$} 21--40\% {\Large$\square$} 41--60\% {\Large$\square$} 61--80\% {\Large$\square$} 81--100\% \\
\end{tabularx}

\newpage
\noindent{\large\bfseries Section F: Training}\vspace{4pt}

\noindent\begin{tabularx}{\textwidth}{@{}L{0.6cm} X L{5.5cm}@{}}
Q27 & Digital training in last 2 years? & \yesno \\[3pt]
Q28 & If yes, how many sessions? & {\Large$\square$} 1 {\Large$\square$} 2--3 {\Large$\square$} 4--5 {\Large$\square$} 5+ \\[3pt]
Q29 & Rate training quality: & \likert \\[3pt]
Q30 & Training sufficient for your job? & \likert \\[3pt]
Q31 & Topics needing more training: & \rule{\linewidth}{0.4pt}\\[3pt] & \rule{\linewidth}{0.4pt} \\
\end{tabularx}

\vspace{4pt}
\noindent{\large\bfseries Section G: Challenges}\vspace{4pt}

\noindent\begin{tabularx}{\textwidth}{@{}L{0.6cm} X L{5.5cm}@{}}
Q32 & Issues faced (tick all): & {\Large$\square$} Slow net {\Large$\square$} Crashes {\Large$\square$} No device {\Large$\square$} Complex UI {\Large$\square$} No training {\Large$\square$} No support {\Large$\square$} Power cuts \\[3pt]
Q33 & How often do digital issues disrupt work? & {\Large$\square$} Daily {\Large$\square$} Weekly {\Large$\square$} Monthly {\Large$\square$} Rarely {\Large$\square$} Never \\[3pt]
Q34 & Comfortable asking for digital help? & \likert \\[3pt]
Q35 & Organisation supports digital tools adequately? & \likert \\[3pt]
Q36 & Department committed to digital transformation? & \likert \\
\end{tabularx}

\vspace{4pt}
\noindent{\large\bfseries Section H: Recommendations}\vspace{4pt}

\noindent Q37. Rank priorities (1=highest, 5=lowest):\vspace{3pt}

\noindent\begin{tabularx}{\textwidth}{@{}L{0.6cm} X L{1.5cm}@{}}
& Better internet & Rank: \_\_\_ \\[2pt]
& More/better devices & Rank: \_\_\_ \\[2pt]
& More training & Rank: \_\_\_ \\[2pt]
& Simpler portals & Rank: \_\_\_ \\[2pt]
& Faster IT support & Rank: \_\_\_ \\
\end{tabularx}

\vspace{3pt}
\noindent Q38. What one change would most improve your digital tool use?\vspace{3pt}

\noindent\rule{\textwidth}{0.4pt}\vspace{3pt}\rule{\textwidth}{0.4pt}\vspace{3pt}

\noindent Q39. Has digital adoption improved service delivery to citizens?\vspace{2pt}

\noindent {\Large$\square$} Yes, significantly\quad{\Large$\square$} Somewhat\quad{\Large$\square$} No change\quad{\Large$\square$} Worsened\quad{\Large$\square$} Can't say

\vspace{4pt}\noindent\rule{\textwidth}{1pt}\vspace{2pt}
\begin{center}\textit{--- End of Common Questions (Q1--Q39). Department-specific section follows. ---}\end{center}
\rule{\textwidth}{0.5pt}
"""

CADRE_SECTION = r"""
\vspace{4pt}
\noindent{\large\bfseries Section J: Role-Specific Questions}\vspace{4pt}

\noindent\begin{tabularx}{\textwidth}{@{}L{0.6cm} X L{5.5cm}@{}}
Q50 & Primary interaction with digital tools: & {\Large$\square$} Data entry {\Large$\square$} Review/approve {\Large$\square$} Field verification {\Large$\square$} Don't use {\Large$\square$} Other \\[3pt]
Q51 & One person does most portal work for others? & {\Large$\square$} Yes, one person {\Large$\square$} A few share {\Large$\square$} Everyone does own {\Large$\square$} N/A \\[3pt]
Q52 & Training appropriate for your specific job role? & \likert \\[3pt]
Q53 & When a portal errors out, you: & {\Large$\square$} Wait for IT {\Large$\square$} Ask colleague {\Large$\square$} Use paper {\Large$\square$} Fix myself {\Large$\square$} Tell supervisor {\Large$\square$} Abandon \\[3pt]
Q54 & Senior officers use digital tools themselves? & {\Large$\square$} Yes {\Large$\square$} Rely on subordinates {\Large$\square$} Mixed {\Large$\square$} Don't know \\[3pt]
Q55 & Digital tools changed work expected at your level? & \likert{} {\scriptsize(1=No change, 5=Completely)} \\[3pt]
Q56 & Digital tasks beyond your current skill? & {\Large$\square$} Yes {\Large$\square$} No\quad If yes: \rule{4cm}{0.4pt} \\[3pt]
Q57 & Training should differ based on your job level? & {\Large$\square$} Yes {\Large$\square$} Somewhat {\Large$\square$} No\quad Why: \rule{3.5cm}{0.4pt} \\
\end{tabularx}
"""

for dept_name, dept_data in DEPTS.items():
    safe = dept_name.replace(" ", "_")
    fname = f"Schedule_{safe}.tex"

    tex = common_header(dept_name)
    tex += cover(dept_name, dept_data["tools"], dept_data["cadre"])
    tex += COMMON_SECTIONS

    # Department-specific section
    tex += r"\newpage" + "\n"
    tex += r"\noindent{\large\bfseries Section I: " + dept_name + r" Department --- Specific Questions}\vspace{4pt}" + "\n\n"
    tex += r"\noindent\begin{tabularx}{\textwidth}{@{}L{0.6cm} X L{5.5cm}@{}}" + "\n"

    for qnum, qtext, qscale in dept_data["questions"]:
        tex += f"{qnum} & {qtext} & {qscale} \\\\[3pt]\n"

    tex += r"\end{tabularx}" + "\n"

    # Cadre section
    tex += CADRE_SECTION

    # End page
    tex += r"""
\vspace{3pt}\noindent\rule{\textwidth}{1pt}
\begin{center}
{\large\bfseries --- END OF SCHEDULE ---}\\[2pt]
\textbf{Total: 39 (common) + 10 (""" + dept_name + r""") + 8 (role) = 57 questions}\\[8pt]
\textbf{Notes:}\vspace{3pt}

\rule{\textwidth}{0.4pt}\vspace{3pt}
\rule{\textwidth}{0.4pt}\vspace{3pt}
\rule{\textwidth}{0.4pt}\vspace{3pt}
\rule{\textwidth}{0.4pt}\vspace{4pt}

\textbf{Interviewer:} \rule{5cm}{0.4pt}\qquad\textbf{Date:} \_\_\_/\_\_\_/2026
\end{center}
\end{document}
"""

    outpath = os.path.join(os.getcwd(), fname)
    with open(outpath, "w", encoding="utf-8") as f:
        f.write(tex)
    print(f"Created: {fname}")

    # Compile twice
    for _ in range(2):
        subprocess.run(["pdflatex", "-interaction=nonstopmode", fname],
                       capture_output=True, cwd=os.getcwd())

    pdf = fname.replace(".tex", ".pdf")
    if os.path.exists(pdf):
        print(f"  Compiled: {pdf}")
        # Copy to Downloads
        dl = os.path.join(r"c:\Users\aryan\Downloads", pdf)
        import shutil
        shutil.copy2(pdf, dl)
        print(f"  Copied to Downloads")
    else:
        print(f"  ERROR: {pdf} not found")

print("\nDone! 4 department schedules ready in Downloads.")
