import json, os

Q = [
# === SECTION A: DEMOGRAPHIC PROFILE ===
{"construct":"Respondent Profile","dimension":"Administrative Identity","indicator":"Department of posting","item":"Which department are you currently posted in?","scale":"Categorical (Revenue / Rural Development / Forest / Health)","justification":"Stratification variable; enables cross-departmental comparison of digital adoption patterns as required by the study's multi-department design."},
{"construct":"Respondent Profile","dimension":"Administrative Identity","indicator":"Office type classification","item":"What is your current office type?","scale":"Categorical (Head Office / District Office)","justification":"Core stratification variable; the study hypothesises significant infrastructure and adoption gaps between HO and DO levels (Heeks, 2003)."},
{"construct":"Respondent Profile","dimension":"Administrative Identity","indicator":"Service cadre classification","item":"What is your current service class/cadre?","scale":"Categorical (Class I / Class II / Class III / Class IV)","justification":"Cadre determines role complexity and digital tool exposure; essential for testing whether adoption barriers vary by hierarchical position (Venkatesh et al., 2003)."},
{"construct":"Respondent Profile","dimension":"Demographics","indicator":"Age cohort membership","item":"What is your age group?","scale":"Categorical (30-45 years / 46-60 years)","justification":"Age is a moderating variable in UTAUT; older employees may exhibit lower behavioural intention due to higher effort expectancy (Venkatesh et al., 2003)."},
{"construct":"Respondent Profile","dimension":"Demographics","indicator":"Gender identity","item":"What is your gender?","scale":"Categorical (Male / Female / Other)","justification":"Gender is a moderating variable in UTAUT; enables analysis of gendered differences in technology acceptance (Venkatesh et al., 2003)."},
{"construct":"Respondent Profile","dimension":"Service Tenure","indicator":"Years of government service","item":"How many years have you been in government service?","scale":"Numeric (Ratio data, in years)","justification":"Experience is a UTAUT moderator; longer-tenured employees may have entrenched workflows resistant to digital change (Venkatesh et al., 2012)."},

# === SECTION B: FACILITATING CONDITIONS ===
{"construct":"Facilitating Conditions (FC)","dimension":"Hardware Infrastructure","indicator":"Availability of dedicated digital devices at workstation","item":"What digital devices are available at your personal workstation? (Select all that apply)","scale":"Multi-select Checklist (Desktop / Laptop / Tablet / Smartphone / None)","justification":"FC requires that organisational infrastructure exists to support system use; device availability is the most direct measure of hardware FC (Venkatesh et al., 2003)."},
{"construct":"Facilitating Conditions (FC)","dimension":"Hardware Infrastructure","indicator":"Device sharing ratio","item":"Do you share your primary digital device with other colleagues?","scale":"Categorical (No, it is assigned to me / Yes, shared with 1-2 others / Yes, shared with 3+ others)","justification":"Shared devices reduce effective FC by limiting access time; captures the gap between stated device counts and actual per-employee availability."},
{"construct":"Facilitating Conditions (FC)","dimension":"Network Infrastructure","indicator":"Perceived quality of internet connectivity","item":"How would you rate the internet connectivity at your office?","scale":"5-point Likert (1=Very Poor to 5=Excellent)","justification":"Bandwidth and reliability are core FC determinants; poor connectivity is the most commonly cited barrier in developing-country e-government studies (Heeks, 2006; World Bank, 2016)."},
{"construct":"Facilitating Conditions (FC)","dimension":"Network Infrastructure","indicator":"Frequency of connectivity disruptions","item":"How often do you experience internet outages or severe slowdowns during working hours?","scale":"5-point Frequency (1=Never to 5=Multiple times daily)","justification":"Complements the perception-based connectivity question with a behavioural frequency measure; high disruption frequency directly undermines FC (OECD, 2014)."},
{"construct":"Facilitating Conditions (FC)","dimension":"Technical Support","indicator":"Availability of IT helpdesk or support personnel","item":"Is there a dedicated IT helpdesk or technical support person available in your office?","scale":"Categorical (Yes, full-time / Yes, but part-time or shared / No)","justification":"UTAUT defines FC as including the belief that technical infrastructure exists to support use; helpdesk availability is the human dimension of this construct (Venkatesh et al., 2003)."},
{"construct":"Facilitating Conditions (FC)","dimension":"Technical Support","indicator":"Responsiveness of IT support","item":"When you report a technical issue, how quickly is it typically resolved?","scale":"Categorical (Same day / Within 2-3 days / Within a week / More than a week / Issue remains unresolved)","justification":"FC is not just about existence but effectiveness of support; slow resolution degrades perceived FC and discourages future digital engagement (Heeks, 2003)."},

# === SECTION C: PERFORMANCE EXPECTANCY ===
{"construct":"Performance Expectancy (PE)","dimension":"Perceived Usefulness","indicator":"Belief that digital tools improve work speed","item":"To what extent do you agree: Digital tools help me complete my work faster than manual/paper-based methods.","scale":"5-point Likert (1=Strongly Disagree to 5=Strongly Agree)","justification":"PE is the strongest predictor of behavioural intention in both TAM and UTAUT; this item directly operationalises Davis's (1989) perceived usefulness construct."},
{"construct":"Performance Expectancy (PE)","dimension":"Perceived Usefulness","indicator":"Belief that digital tools improve work quality","item":"To what extent do you agree: Using digital tools improves the accuracy and quality of my work output.","scale":"5-point Likert (1=Strongly Disagree to 5=Strongly Agree)","justification":"PE encompasses both speed and quality dimensions; capturing quality separately prevents conflation and allows finer diagnostic analysis (Davis, 1989)."},
{"construct":"Performance Expectancy (PE)","dimension":"Productivity Impact","indicator":"Perceived overall productivity gain","item":"Overall, how much has the use of digital tools improved your personal work productivity?","scale":"5-point Improvement Scale (1=No improvement to 5=Greatly improved)","justification":"Provides a summative PE measure that can be correlated with specific FC and EE items to test the full UTAUT causal path."},
{"construct":"Performance Expectancy (PE)","dimension":"Task-Technology Fit","indicator":"Relevance of available tools to actual job tasks","item":"How well do the digital tools provided to you match the actual requirements of your daily tasks?","scale":"5-point Likert (1=Not at all to 5=Perfectly matched)","justification":"PE is moderated by task-technology fit; a tool may be powerful but irrelevant to the user's role, producing low PE despite high capability (Venkatesh et al., 2003)."},

# === SECTION D: EFFORT EXPECTANCY ===
{"construct":"Effort Expectancy (EE)","dimension":"Perceived Ease of Use","indicator":"Subjective difficulty of using current digital tools","item":"How difficult do you find the digital tools currently used in your office?","scale":"5-point Likert (1=Very Easy to 5=Very Difficult)","justification":"EE directly measures the degree of ease associated with system use; high EE (difficulty) reduces behavioural intention, especially for older and less experienced users (Venkatesh et al., 2003)."},
{"construct":"Effort Expectancy (EE)","dimension":"Perceived Ease of Use","indicator":"Self-assessed digital literacy level","item":"How would you rate your own ability to use computers and digital tools?","scale":"5-point Likert (1=Very Low to 5=Very High)","justification":"Self-efficacy mediates EE; employees who perceive themselves as digitally literate report lower effort expectancy for the same tools (Davis, 1989; Venkatesh et al., 2012)."},
{"construct":"Effort Expectancy (EE)","dimension":"Learning Curve","indicator":"Time required to become proficient with new tools","item":"When a new digital tool or software is introduced, how long does it typically take you to use it comfortably?","scale":"Categorical (Less than 1 week / 1-2 weeks / 1 month / More than 1 month / I usually need ongoing help)","justification":"Operationalises the learning dimension of EE; prolonged learning curves indicate high EE barriers that require targeted training interventions."},
{"construct":"Effort Expectancy (EE)","dimension":"Interface Complexity","indicator":"Perception of software interface design quality","item":"To what extent do you agree: The interfaces of the digital tools I use are clear, intuitive, and easy to navigate.","scale":"5-point Likert (1=Strongly Disagree to 5=Strongly Agree)","justification":"Interface design directly affects perceived ease of use (Davis, 1989); poor UI/UX is a modifiable barrier that can be addressed through software redesign recommendations."},

# === SECTION E: SOCIAL INFLUENCE ===
{"construct":"Social Influence (SI)","dimension":"Superior Influence","indicator":"Degree to which senior officers encourage digital tool usage","item":"To what extent do your senior officers/supervisors actively encourage you to use digital tools?","scale":"5-point Likert (1=Not at all to 5=Very actively)","justification":"SI posits that an individual's behaviour is influenced by how important others believe they should use the system; in hierarchical government structures, superior influence is the dominant SI channel (Venkatesh et al., 2003)."},
{"construct":"Social Influence (SI)","dimension":"Peer Influence","indicator":"Extent of peer adoption and encouragement","item":"Do your colleagues in the same office regularly use digital tools for their work?","scale":"5-point Likert (1=None of them to 5=All of them)","justification":"Peer usage normalises digital adoption and creates social pressure; low peer adoption indicates a systemic culture barrier beyond individual resistance (Venkatesh et al., 2003)."},
{"construct":"Social Influence (SI)","dimension":"Organisational Mandate","indicator":"Existence of formal policy mandating digital tool usage","item":"Has your department issued any formal order or circular making the use of specific digital tools mandatory?","scale":"Categorical (Yes, and it is enforced / Yes, but not enforced / No such order exists / I am not aware)","justification":"Mandatory use shifts adoption from voluntary to compliance-based; UTAUT shows SI is strongest under mandatory conditions, making policy mandates a critical lever (Venkatesh et al., 2003)."},

# === SECTION F: DIGITAL TOOL AWARENESS & USAGE ===
{"construct":"Facilitating Conditions (FC)","dimension":"Tool Awareness","indicator":"Awareness of specific government digital platforms","item":"Which of the following digital tools/platforms are you aware of? (Select all that apply)","scale":"Multi-select Checklist (e-Office / CPGRAMS / NIC Email / CM Helpline / Departmental MIS Portal / PFMS / GeM / iGOT-Karmayogi / Other)","justification":"Awareness is a precondition for adoption; you cannot use what you do not know exists. Low awareness rates indicate systemic communication failures in digital rollout (Ndou, 2004)."},
{"construct":"Facilitating Conditions (FC)","dimension":"Tool Usage Behaviour","indicator":"Frequency of digital tool usage in daily work","item":"How frequently do you use digital tools (computer, email, portals) in your daily office work?","scale":"5-point Frequency (1=Never to 5=Multiple times daily)","justification":"Usage frequency is the behavioural outcome variable in UTAUT; it is the dependent variable against which all constructs (PE, EE, SI, FC) are tested."},
{"construct":"Facilitating Conditions (FC)","dimension":"Tool Usage Behaviour","indicator":"Proportion of work completed digitally vs. manually","item":"What percentage of your daily office work is currently done using digital tools rather than paper-based methods?","scale":"Categorical (0-20% / 21-40% / 41-60% / 61-80% / 81-100%)","justification":"Captures the depth of digital integration beyond mere frequency; an employee may use email daily but still do 80% of work on paper, indicating shallow adoption."},

# === SECTION G: CAPACITY BUILDING & TRAINING ===
{"construct":"Facilitating Conditions (FC)","dimension":"Training Provision","indicator":"Receipt of formal IT/digital training","item":"Have you received any formal training on digital tools from your department in the last 2 years?","scale":"Categorical (Yes / No)","justification":"Training is a core FC enabler; its absence indicates an organisational failure to support technology use, directly reducing FC scores (Government of India, 2020; Venkatesh et al., 2003)."},
{"construct":"Facilitating Conditions (FC)","dimension":"Training Provision","indicator":"Volume of training received","item":"If yes, how many training sessions have you attended in the last 2 years?","scale":"Numeric (Ratio data)","justification":"Training volume can be correlated with PE and EE scores to test the hypothesis that more training reduces effort expectancy and increases performance expectancy."},
{"construct":"Facilitating Conditions (FC)","dimension":"Training Quality","indicator":"Perceived quality and relevance of training","item":"How would you rate the overall quality and relevance of the digital training you received?","scale":"5-point Likert (1=Very Poor to 5=Excellent)","justification":"Training quality, not just quantity, determines its impact on FC; irrelevant or poorly delivered training may not reduce EE at all (Bhatnagar, 2004)."},
{"construct":"Facilitating Conditions (FC)","dimension":"Training Quality","indicator":"Perceived sufficiency of training for job needs","item":"To what extent do you agree: The training I received was sufficient to confidently use the digital tools required for my job.","scale":"5-point Likert (1=Strongly Disagree to 5=Strongly Agree)","justification":"Directly tests whether training translates into actual capability; a gap here indicates training-needs mismatch that the recommendation phase must address."},
{"construct":"Facilitating Conditions (FC)","dimension":"Training Gaps","indicator":"Unmet training needs identification","item":"In which areas do you feel you need additional training? (Select all that apply)","scale":"Multi-select Checklist (Basic computer skills / Email and communication / e-Office / Data entry and MIS / Internet and cybersecurity / Advanced software / None)","justification":"Identifies specific training gaps by topic area; directly feeds into Objective 4 recommendations for cadre-specific, role-based training programme design."},

# === SECTION H: CHALLENGES & BOTTLENECKS ===
{"construct":"Effort Expectancy (EE)","dimension":"Technical Barriers","indicator":"Types of technical issues encountered","item":"What are the most common technical problems you face when using digital tools? (Select all that apply)","scale":"Multi-select Checklist (Slow internet / Frequent system crashes / Power outages / Outdated hardware / Software errors / Complex passwords/logins / Lack of local language support / Other)","justification":"Categorises bottlenecks into actionable types; each category maps to a different FC or EE dimension, enabling targeted recommendations rather than generic ones (Heeks, 2006)."},
{"construct":"Effort Expectancy (EE)","dimension":"Technical Barriers","indicator":"Frequency of technical disruptions","item":"How often do you experience technical problems that disrupt your work?","scale":"5-point Frequency (1=Never to 5=Daily)","justification":"Quantifies the severity of technical barriers; high-frequency disruptions indicate systemic infrastructure failure (FC) rather than isolated incidents."},
{"construct":"Effort Expectancy (EE)","dimension":"Attitudinal Barriers","indicator":"Comfort level with transition from paper to digital","item":"To what extent do you agree: I feel comfortable transitioning from paper-based to digital methods of working.","scale":"5-point Likert (1=Strongly Disagree to 5=Strongly Agree)","justification":"Captures attitudinal resistance to change, a known moderator of EE; employees who are uncomfortable report higher perceived difficulty even with objectively simple tools (Alrawabdeh, 2014)."},
{"construct":"Effort Expectancy (EE)","dimension":"Adequacy of Support","indicator":"Perceived adequacy of support during difficulties","item":"Do you feel adequately supported when you face technical problems at work?","scale":"Categorical (Yes, always / Somewhat / No, rarely / No support exists)","justification":"Tests the subjective FC perception; even if support exists, if employees perceive it as inadequate, the effective FC is low (Venkatesh et al., 2003)."},
{"construct":"Social Influence (SI)","dimension":"Systemic Barriers","indicator":"Perceived organisational commitment to digital adoption","item":"To what extent do you agree: My department is genuinely committed to supporting digital transformation, not just issuing orders.","scale":"5-point Likert (1=Strongly Disagree to 5=Strongly Agree)","justification":"Tests the gap between formal SI (mandates) and substantive SI (genuine organisational commitment); a large gap indicates performative digitalisation without real support (Cordella & Bonina, 2012)."},

# === SECTION I: RECOMMENDATIONS & IMPROVEMENT ===
{"construct":"Performance Expectancy (PE)","dimension":"Improvement Priorities","indicator":"Employee-identified priority areas for improvement","item":"If ONE area could be improved to help you use digital tools more effectively, which would you choose?","scale":"Categorical (Better internet / Better hardware / More training / Simpler software / More IT support / Clearer policy directives)","justification":"Forces rank-ordering of priorities; the modal response directly identifies the highest-impact intervention area, feeding Objective 4's evidence-based recommendations."},
{"construct":"Performance Expectancy (PE)","dimension":"Improvement Priorities","indicator":"Specific improvement suggestions (open-ended)","item":"In your own words, what specific changes or improvements would help you use digital tools more effectively in your daily work?","scale":"Open-ended (Qualitative text)","justification":"Captures insights beyond pre-defined categories; open-ended responses undergo thematic analysis (Braun & Clarke, 2006) and may reveal unanticipated barriers or solutions."},
{"construct":"Performance Expectancy (PE)","dimension":"Future Outlook","indicator":"Perceived impact of improved digital tools on service delivery","item":"If the digital tools and support in your office were significantly improved, how much do you think it would improve citizen service delivery?","scale":"5-point Improvement Scale (1=No improvement to 5=Greatly improved)","justification":"Tests the theoretical endpoint of the UTAUT model: does the employee believe that better technology adoption leads to better governance outcomes? Validates the study's core premise linking PE to service efficiency (World Bank, 2016; United Nations, 2024)."},
]

sections = [
    ("Section A: Respondent Profile \\& Demographics", 0, 6),
    ("Section B: Facilitating Conditions --- Infrastructure \\& Support", 6, 12),
    ("Section C: Performance Expectancy", 12, 16),
    ("Section D: Effort Expectancy", 16, 20),
    ("Section E: Social Influence", 20, 23),
    ("Section F: Digital Tool Awareness \\& Usage Behaviour", 23, 26),
    ("Section G: Capacity Building \\& Training", 26, 31),
    ("Section H: Challenges \\& Bottlenecks", 31, 36),
    ("Section I: Recommendations \\& Improvement", 36, 39),
]

def esc(s):
    return s.replace('&','\\&').replace('%','\\%').replace('#','\\#').replace('_','\\_').replace('"','``').replace('"',"''").replace("'","'")

header = r"""\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{mathptmx}
\usepackage[margin=2.2cm]{geometry}
\usepackage{booktabs}
\usepackage{tabularx}
\usepackage{longtable}
\usepackage{array}
\usepackage{xcolor}
\usepackage{titlesec}
\usepackage{enumitem}
\usepackage{hyperref}
\usepackage{fancyhdr}
\usepackage{setspace}
\usepackage{parskip}
\usepackage{float}
\usepackage{colortbl}
\usepackage{multirow}

\definecolor{navy}{HTML}{1B2A4A}
\definecolor{gold}{HTML}{C49A2A}
\definecolor{dk}{HTML}{2D2D2D}
\definecolor{mg}{HTML}{4A4A4A}
\definecolor{lg}{HTML}{F0F0F0}
\definecolor{sb}{HTML}{D6E4F0}

\titleformat{\section}{\Large\bfseries\color{navy}}{\thesection}{1em}{}[\vspace{-4pt}{\color{gold}\rule{\textwidth}{1.5pt}}]
\titleformat{\subsection}{\large\bfseries\color{navy}}{\thesubsection}{1em}{}
\setlength{\headheight}{14pt}
\pagestyle{fancy}\fancyhf{}
\fancyhead[L]{\small\color{mg}\textit{AIGGPA --- Structured Schedule}}
\fancyhead[R]{\small\color{mg}\textit{April 2026}}
\fancyfoot[C]{\small\color{mg}\thepage}
\renewcommand{\headrulewidth}{0.4pt}
\hypersetup{colorlinks=true,linkcolor=navy,citecolor=navy,urlcolor=navy}
\setstretch{1.1}
\newcolumntype{L}[1]{>{\raggedright\arraybackslash}p{#1}}

\newcommand{\qcard}[7]{%
\noindent\begin{tabularx}{\textwidth}{@{}>{\columncolor{sb}\bfseries\small}L{3.2cm}|X@{}}
\arrayrulecolor{navy}\hline
Theoretical Construct & #1 \\
Dimension & #2 \\
Operational Indicator & #3 \\
\arrayrulecolor{gold}\hline
\rowcolor{white}\textbf{\color{navy}Survey Item} & \textbf{\color{navy}#4} \\
\arrayrulecolor{gold}\hline
Data Type \& Scale & #5 \\
Justification & \textit{#6} \\
\arrayrulecolor{navy}\hline
\end{tabularx}\vspace{10pt}
}

\begin{document}

\begin{titlepage}\centering
\vspace*{3cm}
{\color{gold}\rule{0.6\textwidth}{2pt}}\vspace{1cm}
{\Huge\bfseries\color{navy} STRUCTURED SCHEDULE\\[8pt] \& QUESTIONNAIRE DESIGN}\vspace{0.6cm}
{\Large\color{dk} Assessment of the Use of Digital Tools and Technologies\\[4pt]by Government Employees for Enhancing Workplace\\[4pt]Efficiency and Effectiveness}\vspace{1cm}
{\color{gold}\rule{0.6\textwidth}{2pt}}\vspace{2cm}
\begin{tabular}{r l}
\textbf{\color{navy}Framework:} & TAM (Davis, 1989) / UTAUT (Venkatesh et al., 2003) \\[6pt]
\textbf{\color{navy}Prepared By:} & Aryan Kori \\[6pt]
\textbf{\color{navy}Institution:} & AIGGPA, Bhopal \\[6pt]
\textbf{\color{navy}Date:} & April 2026 \\
\end{tabular}\vfill
{\small\color{mg}Each question is mapped to its theoretical construct, dimension, indicator, scale, and justification.}
\end{titlepage}

\tableofcontents\newpage

\section*{Reading This Document}
\addcontentsline{toc}{section}{Reading This Document}

Every question in this schedule is presented as a structured card containing six parameters:

\begin{table}[H]\centering\small
\begin{tabularx}{\textwidth}{L{3.5cm} X}
\toprule
\textbf{Parameter} & \textbf{Description} \\
\midrule
Theoretical Construct & The broad TAM/UTAUT construct this question measures \\[3pt]
Dimension & The specific facet of that construct being targeted \\[3pt]
Operational Indicator & The exact observable metric or behaviour being captured \\[3pt]
Survey Item & The actual question presented to the respondent \\[3pt]
Data Type \& Scale & The answer format (Likert, categorical, numeric, open-ended) \\[3pt]
Justification & Why this question is necessary within the theoretical model \\
\bottomrule
\end{tabularx}
\end{table}

\textbf{Framework Alignment:} All items are anchored to the Technology Acceptance Model (Davis, 1989) and Unified Theory of Acceptance and Use of Technology (Venkatesh et al., 2003, 2012), ensuring complete construct coverage across four pillars: \textbf{Performance Expectancy (PE)}, \textbf{Effort Expectancy (EE)}, \textbf{Social Influence (SI)}, and \textbf{Facilitating Conditions (FC)}.

\newpage
"""

footer = r"""
\newpage
\section*{References}
\addcontentsline{toc}{section}{References}
\begin{enumerate}[leftmargin=1.5em,itemsep=3pt,label={[\arabic*]}]
\item Alrawabdeh, W. (2014). Examining factors affecting digital platform adoption in Jordan. \textit{International Journal of Business and Social Science}, 5(8), 232--241.
\item Bhatnagar, S. (2004). \textit{E-Government: From Vision to Implementation}. Sage Publications.
\item Braun, V., \& Clarke, V. (2006). Using thematic analysis in psychology. \textit{Qualitative Research in Psychology}, 3(2), 77--101.
\item Cordella, A., \& Bonina, C. M. (2012). A public value perspective for ICT enabled public sector reforms. \textit{Government Information Quarterly}, 29(4), 512--520.
\item Davis, F. D. (1989). Perceived usefulness, perceived ease of use, and user acceptance of information technology. \textit{MIS Quarterly}, 13(3), 319--340.
\item Government of India, Dept.\ of Personnel \& Training. (2020). \textit{Mission Karmayogi}.
\item Heeks, R. (2003). Most eGovernment-for-Development Projects Fail. University of Manchester.
\item Heeks, R. (2006). \textit{Implementing and Managing eGovernment}. Sage Publications.
\item Ndou, V. (2004). E-government for developing countries. \textit{EJISDC}, 18(1), 1--24.
\item OECD. (2014). \textit{Recommendation of the Council on Digital Government Strategies}. OECD Publishing.
\item United Nations. (2024). \textit{E-Government Survey 2024}. UN DESA.
\item Venkatesh, V., Morris, M. G., Davis, G. B., \& Davis, F. D. (2003). User acceptance of information technology. \textit{MIS Quarterly}, 27(3), 425--478.
\item Venkatesh, V., Thong, J. Y. L., \& Xu, X. (2012). Consumer acceptance and use of information technology. \textit{MIS Quarterly}, 36(1), 157--178.
\item World Bank. (2016). \textit{World Development Report 2016: Digital Dividends}.
\end{enumerate}
\end{document}
"""

body = ""
qnum = 1
for sec_title, start, end in sections:
    body += f"\n\\section{{{sec_title}}}\n\n"
    for i in range(start, end):
        q = Q[i]
        body += f"\\subsection*{{Q{qnum}. {esc(q['item'][:90])}{'...' if len(q['item'])>90 else ''}}}\n"
        body += f"\\qcard{{{esc(q['construct'])}}}{{{esc(q['dimension'])}}}{{{esc(q['indicator'])}}}{{{esc(q['item'])}}}{{{esc(q['scale'])}}}{{{esc(q['justification'])}}}\n\n"
        qnum += 1

tex = header + body + footer

with open('AIGGPA_Questionnaire.tex', 'w', encoding='utf-8') as f:
    f.write(tex)

print(f"Done: AIGGPA_Questionnaire.tex ({len(Q)} questions, {len(tex):,} chars)")
