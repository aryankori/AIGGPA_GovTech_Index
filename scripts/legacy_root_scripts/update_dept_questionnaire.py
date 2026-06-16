"""
AIGGPA Department Questionnaire v2
- Core functions per department
- Cadre hierarchy with designations and digital responsibilities
- Cadre-specific questions (Q60-Q67)
- Indicator explainer appendix
"""

# We'll write the cadre tables and new questions directly into a fresh .tex file
# by extending the existing generator's output

import os

# Read the existing generated tex
with open('AIGGPA_Dept_Questionnaire.tex', 'r', encoding='utf-8') as f:
    tex = f.read()

# ── INSERT 1: Cadre tables after each department's Core Functions table ──
# We insert BEFORE the "Key Digital Tools:" line for each department

cadre_tables = {
    "Revenue": r"""
\textbf{Cadre Structure \& Digital Responsibilities:}

\begin{table}[H]\centering\small
\begin{tabularx}{\textwidth}{L{1.2cm} L{3.5cm} L{4.5cm} X}
\toprule
\textbf{Class} & \textbf{Designations} & \textbf{Core Work} & \textbf{Digital Role} \\
\midrule
\textbf{I} & Collector, Additional Collector, Commissioner (Land Records) & District-level policy, appellate authority, disaster relief coordination, supervision of all revenue operations & Dashboard review, MIS monitoring, approval workflows in SAARA/RCMS; rarely direct data entry \\[4pt]
\textbf{II} & SDM (Sub-Divisional Magistrate), Deputy Collector, Dy. Director (Land Records) & Sub-divisional case adjudication, land acquisition, election duty, magisterial functions & RCMS case disposal, Bhulekh verification for land acquisition, e-Court hearings; moderate data entry \\[4pt]
\textbf{III} & Tehsildar, Naib Tehsildar, Revenue Inspector (RI), Patwari, Computer Operator & Land record maintenance, mutation, demarcation, revenue collection, Khasra/B-1 updates, data entry & Primary users of Bhulekh/WebGIS (Patwari), RCMS (Tehsildar), SAMPADA (registration staff); heaviest digital workload \\[4pt]
\textbf{IV} & Peon, Office Assistant, Process Server, Mali, Chowkidar & File movement, court summons delivery, office upkeep, record room management & Minimal direct use; may assist with scanning, photocopying, or carrying files to digital entry points \\
\bottomrule
\end{tabularx}
\end{table}
""",
    "Rural Development": r"""
\textbf{Cadre Structure \& Digital Responsibilities:}

\begin{table}[H]\centering\small
\begin{tabularx}{\textwidth}{L{1.2cm} L{3.5cm} L{4.5cm} X}
\toprule
\textbf{Class} & \textbf{Designations} & \textbf{Core Work} & \textbf{Digital Role} \\
\midrule
\textbf{I} & CEO (Zila Panchayat), Project Director (DRDA), Joint Director & District-level planning, scheme monitoring, fund allocation, convergence across schemes & Dashboard review on e-Gram Swaraj, PFMS fund release approvals, MIS reporting to state; supervisory digital role \\[4pt]
\textbf{II} & BDO/CEO (Janpad Panchayat), Asst. Project Officer, Dy. CEO & Block-level scheme implementation, staff supervision, expenditure monitoring, inspection & NREGASoft work approval, PMAY-G beneficiary sanctioning, e-Gram Swaraj GPDP uploads; regular portal use \\[4pt]
\textbf{III} & Gram Panchayat Secretary, Gram Rozgar Sahayak (GRS), Accountant, Data Entry Operator, Gram Sevak & Muster roll maintenance, wage list preparation, beneficiary registration, village-level record keeping & Heaviest users --- NREGASoft data entry, NMMS attendance uploads, PMAY-G geo-tagging, SBM-G reporting; daily multi-portal operations \\[4pt]
\textbf{IV} & Peon, Office Assistant, Chowkidar & File movement, office maintenance, physical delivery of notices & Minimal direct use; may carry printed MIS reports or assist with hardware maintenance \\
\bottomrule
\end{tabularx}
\end{table}
""",
    "Forest": r"""
\textbf{Cadre Structure \& Digital Responsibilities:}

\begin{table}[H]\centering\small
\begin{tabularx}{\textwidth}{L{1.2cm} L{3.5cm} L{4.5cm} X}
\toprule
\textbf{Class} & \textbf{Designations} & \textbf{Core Work} & \textbf{Digital Role} \\
\midrule
\textbf{I} & CCF (Chief Conservator), CF (Conservator), DFO/DCF (Divisional Forest Officer) --- IFS cadre & Division/circle management, CAMPA fund utilisation, wildlife protection policy, working plan approval & e-Green Watch dashboard, AI alert system monitoring, GIS-based planning; approval and review role \\[4pt]
\textbf{II} & ACF (Assistant Conservator), Sub-Divisional Forest Officer (SDFO) --- SFS cadre & Sub-division supervision, offence prosecution, nursery inspection, plantation monitoring & Forest Offence MIS entries, e-Green Watch geo-tagging verification, GIS map review; moderate digital use \\[4pt]
\textbf{III} & Range Officer (RFO/Ranger), Deputy Ranger, Forester & Range-level patrolling, offence detection, fire management, plantation execution, wildlife census fieldwork & AI alert response (field verification with GPS photos), GIS data collection, Forest Offence MIS first entry; field-heavy digital use \\[4pt]
\textbf{IV} & Forest Guard, Van Rakshak, Peon, Mali & Beat-level patrolling, fire line maintenance, nursery labour, camp duty, physical boundary marking & Frontline alert responders; use smartphones for GPS-tagged photos/voice notes; lowest formal training but highest field exposure \\
\bottomrule
\end{tabularx}
\end{table}
""",
    "Health": r"""
\textbf{Cadre Structure \& Digital Responsibilities:}

\begin{table}[H]\centering\small
\begin{tabularx}{\textwidth}{L{1.2cm} L{3.5cm} L{4.5cm} X}
\toprule
\textbf{Class} & \textbf{Designations} & \textbf{Core Work} & \textbf{Digital Role} \\
\midrule
\textbf{I} & CMHO (Chief Medical \& Health Officer), Civil Surgeon, Joint/Deputy Director, Senior Specialist & District health administration, programme monitoring, hospital management, policy compliance & HMIS dashboard review, Nikshay district-level monitoring, Ayushman Bharat claim oversight; supervisory digital role \\[4pt]
\textbf{II} & Block Medical Officer (BMO), Medical Officer (MO), District Programme Manager (NHM) & PHC/CHC clinical duties, block-level programme implementation, data review and reporting & HMIS data validation, Nikshay case notifications, IHIP disease reporting, ANMOL supervision; regular portal use \\[4pt]
\textbf{III} & Staff Nurse, ANM (Auxiliary Nurse Midwife), Lab Technician, Pharmacist, Health Worker, Data Entry Operator & Patient care, immunisation delivery, ANC registration, cold chain maintenance, sample collection, data entry & ANMOL MP primary users (ANMs), eVIN temperature logging, HMIS facility-level data entry; heaviest routine digital workload \\[4pt]
\textbf{IV} & Ward Boy/Attendant, Peon, Sweeper, Security Guard, Ambulance Helper & Patient handling, hospital sanitation, equipment movement, security, ambulance support & Minimal formal digital role; may interact with biometric attendance systems or assist with patient registration \\
\bottomrule
\end{tabularx}
\end{table}
""",
}

# Insert cadre tables after "Core Functions:" blocks
for dept, cadre_tex in cadre_tables.items():
    # Find the tools line for this department
    if dept == "Rural Development":
        search_key = "Rural\\_Development" if "Rural\\_Development" in tex else "Rural Development"
    else:
        search_key = dept
    
    # Find "Key Digital Tools:" that follows the department section
    # We insert BEFORE the tools line
    dept_tools_markers = {
        "Revenue": r"\textbf{Key Digital Tools:} MP Bhulekh",
        "Rural Development": r"\textbf{Key Digital Tools:} NREGASoft",
        "Forest": r"\textbf{Key Digital Tools:} e-Green Watch",
        "Health": r"\textbf{Key Digital Tools:} ANMOL MP",
    }
    marker = dept_tools_markers[dept]
    if marker in tex:
        tex = tex.replace(marker, cadre_tex + "\n" + marker, 1)
        print(f"  Inserted cadre table for {dept}")
    else:
        print(f"  WARNING: Could not find marker for {dept}")

# ── INSERT 2: Cadre-specific questions (Q60-Q67) ──
# Insert before the "Pre-Fieldwork: Questions for Your Manager" section

cadre_questions = r"""
\newpage
\section{Cadre-Specific Questions (All Departments)}

These 8 questions (Q60--Q67) are administered to \textbf{every respondent} regardless of department. They capture cadre-specific digital experiences that vary by seniority and role type.

\subsection*{Q60. What is your primary interaction with digital tools in your role?}
\qcard{Facilitating Conditions (FC)}{Role-Based Digital Access}{Nature of digital tool interaction by cadre}{In your current role, what is your primary interaction with digital tools?}{Single-select (I enter/create data in portals / I review dashboards and approve / I use tools for field verification / I do not directly use digital tools / Other)}{Different cadres interact with technology at fundamentally different levels --- data entry (Class III), supervisory review (Class I-II), field use (Class III-IV), or no interaction (Class IV). Capturing this prevents treating all ``users'' as equivalent (Venkatesh et al., 2003).}{sb}{navy}

\subsection*{Q61. Has anyone in your office been assigned ``digital duty'' --- doing portal w...}
\qcard{Facilitating Conditions (FC)}{Informal Digital Labour Division}{Whether digital work is concentrated on specific individuals}{In your office, is there a specific person (e.g., a Computer Operator or junior staff member) who does most of the digital/portal work on behalf of others?}{Categorical (Yes, one designated person / Yes, a few people share it / No, everyone does their own / Not applicable)}{In many offices, a single Class III employee handles all digital work for the unit, creating a single point of failure. This ``proxy use'' pattern means official adoption numbers overstate actual individual capability (Heeks, 2003).}{sb}{navy}

\subsection*{Q62. Do you feel that employees at your level receive sufficient training co...}
\qcard{Training \& Capacity Building}{Cadre-Appropriate Training}{Perceived adequacy of training for respondent's specific cadre}{Do you feel that the digital skills training provided is appropriate for the work expected at your level (Class I/II/III/IV)?}{5-point Likert (1=Not at all appropriate to 5=Highly appropriate)}{A Class IV Forest Guard needs GPS/photo skills; a Class I Collector needs dashboard literacy. Generic ``computer training'' fails both. This item tests whether training is calibrated to actual role needs (Government of India, 2020).}{sb}{navy}

\subsection*{Q63. If a digital system breaks down or produces an error, what do you typi...}
\qcard{Facilitating Conditions (FC)}{Error Recovery by Cadre}{Coping strategy when digital systems fail}{When a digital tool or portal produces an error or stops working during your task, what do you typically do?}{Single-select (Wait for IT support / Ask a colleague for help / Switch to paper/manual process / Try to fix it myself / Escalate to supervisor / Abandon the task)}{Error recovery behaviour varies dramatically by cadre: Class I officers escalate, Class III staff switch to paper, Class IV staff abandon. This reveals the real-world FC gap between infrastructure availability and usability (Venkatesh et al., 2003).}{sb}{navy}

\subsection*{Q64. In your experience, do senior officers (Class I/II) use digital tools ...}
\qcard{Social Influence (SI)}{Leadership Digital Modelling}{Whether senior officers visibly use digital tools themselves}{In your observation, do senior officers (Class I/II) in your department actively use digital tools themselves, or do they rely on subordinates to operate portals on their behalf?}{Categorical (They use tools themselves / They mostly rely on subordinates / Mixed --- depends on the officer / I don't know)}{SI theory predicts that visible technology use by superiors accelerates adoption among subordinates. If Class I-II officers delegate all digital work, it signals that technology is ``clerical work,'' undermining adoption motivation for all cadres (Venkatesh et al., 2003).}{sb}{navy}

\subsection*{Q65. Has the introduction of digital tools changed the kind of work expecte...}
\qcard{Performance Expectancy (PE)}{Role Evolution}{Whether digital tools have changed job role expectations}{Has the introduction of digital tools changed the nature of work expected from employees at your level?}{5-point Likert (1=No change at all to 5=Completely changed my role) + Follow-up: How? (Open-ended)}{Digitisation often adds portal management to existing duties without reducing old tasks. For Class III staff (Patwaris, ANMs, GRS), this can mean doing the same field work PLUS hours of data entry --- a net negative PE outcome (Heeks, 2006).}{sb}{navy}

\subsection*{Q66. Are there tasks that your cadre is expected to do digitally but you fe...}
\qcard{Effort Expectancy (EE)}{Cadre-Skill Mismatch}{Tasks expected digitally but perceived as beyond current skill level}{Are there any digital tasks you are expected to perform as part of your duties that you feel are beyond your current skill level?}{Categorical (Yes / No) + If yes: Which tasks? (Open-ended)}{This directly measures the EE gap between institutional expectations and individual capability at each cadre level. High ``Yes'' rates in specific cadres pinpoint where targeted upskilling is needed (Venkatesh et al., 2003).}{sb}{navy}

\subsection*{Q67. In your opinion, should digital training be different for different lev...}
\qcard{Training \& Capacity Building}{Training Differentiation}{Opinion on whether training should be cadre-differentiated}{Do you think digital skills training should be designed differently for different levels of employees (Class I/II vs. III vs. IV)?}{Categorical (Yes, definitely / Somewhat / No, same training for all) + Why? (Open-ended)}{Captures ground-level demand for cadre-differentiated training design. If respondents across cadres overwhelmingly say ``yes,'' it provides direct evidence for recommending tiered training programmes in the policy brief.}{sb}{navy}

"""

# Find the pre-fieldwork section
prefieldwork_marker = r"\section{Pre-Fieldwork: Questions for Your Manager}"
if prefieldwork_marker in tex:
    tex = tex.replace(prefieldwork_marker, cadre_questions + "\n" + prefieldwork_marker)
    print("  Inserted cadre-specific questions (Q60-Q67)")

# ── INSERT 3: Indicators Explainer Appendix ──
# Insert before \end{document}

indicators_appendix = r"""
\newpage
\section*{Appendix: Understanding Operational Indicators}
\addcontentsline{toc}{section}{Appendix: Understanding Operational Indicators}

An \textbf{operational indicator} is the bridge between abstract theory and concrete measurement. It answers the question: \textit{``What specific, observable thing do I need to measure to assess this concept?''}

\subsection*{Why Indicators Matter}

\begin{table}[H]\centering\small
\begin{tabularx}{\textwidth}{L{3cm} X}
\toprule
\textbf{Without Indicators} & \textbf{With Indicators} \\
\midrule
``Measure digital adoption'' (vague --- what counts as adoption?) & ``Percentage of daily tasks completed using digital tools vs.\ paper'' (specific, countable) \\[4pt]
``Assess training quality'' (how?) & ``Respondent's self-rated confidence in using department-specific portals after training'' (measurable on a scale) \\[4pt]
``Check infrastructure'' (check what?) & ``Number of functioning, dedicated digital devices per employee at their workstation'' (observable, countable) \\
\bottomrule
\end{tabularx}
\end{table}

\subsection*{The Indicator Design Chain}

Every indicator in this questionnaire follows a four-step logic:

\begin{enumerate}[leftmargin=1.5em, itemsep=6pt]
    \item \textbf{Construct} (abstract): What theoretical concept are we testing? \\
    \textit{Example: Facilitating Conditions (FC)}
    \item \textbf{Dimension} (narrower): What specific aspect of the construct? \\
    \textit{Example: Hardware Infrastructure}
    \item \textbf{Indicator} (observable): What exact thing can we see, count, or ask about? \\
    \textit{Example: Number of dedicated digital devices available per employee}
    \item \textbf{Survey Item} (question): How do we ask the respondent about it? \\
    \textit{Example: ``What digital devices are available at your personal workstation?''}
\end{enumerate}

\subsection*{Types of Indicators Used in This Study}

\begin{table}[H]\centering\small
\begin{tabularx}{\textwidth}{L{2.5cm} L{3cm} X L{3cm}}
\toprule
\textbf{Indicator Type} & \textbf{What It Measures} & \textbf{Example from This Study} & \textbf{Data It Produces} \\
\midrule
\textbf{Awareness} & Whether the respondent knows a tool exists & ``Which digital tools are you aware of?'' & Checklist (nominal) \\[4pt]
\textbf{Usage Frequency} & How often a tool is actually used & ``How often do you use digital tools?'' & Likert / ordinal \\[4pt]
\textbf{Perception} & Subjective assessment of usefulness, difficulty, or quality & ``How difficult do you find RCMS?'' & Likert (1--5 scale) \\[4pt]
\textbf{Behaviour} & What the respondent actually does & ``What do you do when a portal produces an error?'' & Categorical \\[4pt]
\textbf{Count / Quantity} & Measurable numeric values & ``How many training sessions attended?'' & Numeric (ratio) \\[4pt]
\textbf{Ratio / Proportion} & Relative comparison & ``Percentage of tasks done digitally vs.\ paper'' & Categorical bands \\[4pt]
\textbf{Open-Ended} & Rich qualitative data & ``What would improve digital tool adoption?'' & Text (for thematic analysis) \\
\bottomrule
\end{tabularx}
\end{table}

\subsection*{Good Indicators vs.\ Bad Indicators}

\begin{table}[H]\centering\small
\begin{tabularx}{\textwidth}{C{0.8cm} L{5.5cm} L{5.5cm} L{3cm}}
\toprule
\textbf{\#} & \textbf{Bad Indicator} & \textbf{Good Indicator} & \textbf{Why} \\
\midrule
1 & ``Digital readiness of the department'' & ``Percentage of employees with a dedicated device at their desk'' & Observable, countable \\[4pt]
2 & ``Quality of internet'' & ``Frequency of internet outages per week lasting over 30 minutes'' & Specific, time-bound \\[4pt]
3 & ``Training effectiveness'' & ``Self-rated confidence in using [specific portal] before vs.\ after training'' & Measurable, comparable \\[4pt]
4 & ``Employee satisfaction with technology'' & ``Agreement that digital tools make my work faster (1--5 Likert)'' & Single-barrelled, scalable \\[4pt]
5 & ``Use of AI tools'' & ``Frequency of responding to AI-generated forest alerts per month'' & Specific action, countable \\
\bottomrule
\end{tabularx}
\end{table}

\subsection*{How Indicators Connect to Analysis}

\begin{table}[H]\centering\small
\begin{tabularx}{\textwidth}{L{3cm} L{3cm} X}
\toprule
\textbf{Indicator Type} & \textbf{Analysis Method} & \textbf{What You Can Conclude} \\
\midrule
Likert (ordinal) & Median, Mann-Whitney U, Kruskal-Wallis, Cronbach's $\alpha$ & Compare perceptions across groups (departments, cadres, age groups) \\[4pt]
Categorical (nominal) & Frequency tables, chi-square, cross-tabulation & Test associations (e.g., ``Is cadre associated with error recovery strategy?'') \\[4pt]
Numeric (ratio) & Mean, SD, t-test, ANOVA, correlation & Measure exact quantities and test differences \\[4pt]
Open-ended (text) & Thematic analysis (Braun \& Clarke, 2006) & Identify patterns, generate recommendations, contextualise quantitative findings \\
\bottomrule
\end{tabularx}
\end{table}
"""

end_doc = r"\end{document}"
if end_doc in tex:
    tex = tex.replace(end_doc, indicators_appendix + "\n" + end_doc)
    print("  Inserted indicators appendix")

# Write updated tex
with open('AIGGPA_Dept_Questionnaire.tex', 'w', encoding='utf-8') as f:
    f.write(tex)

print("\nDone: AIGGPA_Dept_Questionnaire.tex updated with cadre tables + Q60-Q67 + indicators appendix")
