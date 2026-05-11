"""Generate bilingual (EN/HI) printable schedule using xelatex."""
import subprocess, os, shutil
from hi import H, Q, ROLE, PERSONAL

def hi(text):
    return r"{\hindifont\small\itshape\color{black!70} " + text + "}"

def bilingual_q(qnum, en, hn, scale_en, scale_hi=""):
    """One question: English line, Hindi line below, then response options."""
    row = f"{qnum} & {en} & {scale_en} \\\\\n"
    row += f" & {hi(hn)} & {hi(scale_hi) if scale_hi else ''} \\\\[3pt]\n"
    return row

PREAMBLE = r"""\documentclass[10pt,a4paper]{article}
\usepackage[margin=0.8cm]{geometry}\usepackage{fontspec}\usepackage{tabularx}
\usepackage{array}\usepackage{booktabs}\usepackage{fancyhdr}\usepackage{setspace}
\usepackage{amssymb}\usepackage{xcolor}
\setmainfont{Times New Roman}
\newfontfamily\hindifont{Nirmala UI}
\pagestyle{fancy}\fancyhf{}
\fancyhead[L]{\small\textbf{AIGGPA Research Schedule}}
\fancyhead[R]{\small Respondent ID: \_\_\_\_\_\_\_\_}
\fancyfoot[C]{\small Page \thepage}\renewcommand{\headrulewidth}{0.5pt}
\setlength{\headheight}{14pt}\setstretch{1.05}
\newcolumntype{L}[1]{>{\raggedright\arraybackslash}p{#1}}
\newcommand{\likert}{{\Large$\square$}\,1\quad{\Large$\square$}\,2\quad{\Large$\square$}\,3\quad{\Large$\square$}\,4\quad{\Large$\square$}\,5}
\newcommand{\ymark}{{\Large$\square$}\,Yes/{\hindifont\itshape हाँ}\quad{\Large$\square$}\,No/{\hindifont\itshape नहीं}}
\newcommand{\blank}{\rule{7cm}{0.4pt}}
\begin{document}
"""

COVER = r"""
\begin{center}
{\Large\bfseries AIGGPA FIELD RESEARCH SCHEDULE}\\[1pt]
{\large\hindifont\itshape\color{black!70} AIGGPA \textnormal{क्षेत्र अनुसंधान अनुसूची}}\\[6pt]
{\small Assessment of Digital Tool Usage Among Government Employees}\\[1pt]
{\small\hindifont\itshape\color{black!70} सरकारी कर्मचारियों में डिजिटल उपकरण उपयोग का मूल्यांकन}\\[4pt]
{\small AIGGPA Bhopal \quad$\bullet$\quad 2026}
\end{center}
\vspace{4pt}\noindent\rule{\textwidth}{1pt}\vspace{4pt}

\noindent\begin{tabularx}{\textwidth}{@{}L{9.5cm} X@{}}
\textbf{Respondent ID:} \blank & \textbf{Date:} \_\_\_/\_\_\_/2026 \\[6pt]
\textbf{Department:} {\Large$\square$} Revenue {\Large$\square$} Rural Dev {\Large$\square$} Forest {\Large$\square$} Health & \textbf{Office:} {\Large$\square$} HO {\Large$\square$} District \\[6pt]
\textbf{Interviewer:} \blank & \textbf{Time:} \_\_:\_\_\quad to \quad\_\_:\_\_ \\
\end{tabularx}
\vspace{4pt}\noindent\rule{\textwidth}{0.5pt}\vspace{4pt}
"""

def sec_header(letter, en, hn):
    if hn:
        return f"\\noindent\\rule{{\\textwidth}}{{0.3pt}}\\vspace{{3pt}}\n\\noindent{{\\large\\bfseries Section {letter}: {en}}}\\\\\n{{\\hindifont\\itshape\\color{{black!70}} {hn}}}\\vspace{{3pt}}\n\n"
    return f"\\noindent\\rule{{\\textwidth}}{{0.3pt}}\\vspace{{3pt}}\n\\noindent{{\\large\\bfseries Section {letter}: {en}}}\\vspace{{3pt}}\n\n"

def tab_start():
    return r"\noindent\begin{tabularx}{\textwidth}{@{}L{0.8cm} X L{5.2cm}@{}}" + "\n"

def tab_end():
    return r"\end{tabularx}" + "\n"

# Build the full LaTeX
tex = PREAMBLE + COVER

# Section A: Demographics
tex += sec_header("A", "Respondent Profile", H["sec_a"])
tex += r"\noindent\begin{tabularx}{\textwidth}{@{}L{0.8cm} L{7.7cm} X@{}}" + "\n"
for i in range(6):  # Q1-Q6
    qn, en, hn = Q[i]
    if qn == "Q3":
        opts = r"{\Large$\square$} Below 30/{\hindifont 30 से कम}\quad{\Large$\square$} 30--45\quad{\Large$\square$} 46--60"
    elif qn == "Q4":
        opts = r"{\Large$\square$} Male/{\hindifont पुरुष}\quad{\Large$\square$} Female/{\hindifont महिला}\quad{\Large$\square$} Other/{\hindifont अन्य}"
    elif qn == "Q5":
        opts = r"{\Large$\square$} 0--5\quad{\Large$\square$} 6--10\quad{\Large$\square$} 11--20\quad{\Large$\square$} 21+"
    elif qn == "Q6":
        opts = r"{\Large$\square$} " + f"Up to 12th/{hi(H['upto12'])}" + r"\quad{\Large$\square$} " + f"Grad/{hi(H['grad'])}" + r"\quad{\Large$\square$} " + f"PG/{hi(H['pg'])}" + r"\quad{\Large$\square$} " + f"Prof/{hi(H['prof'])}"
    else:
        opts = r"\blank"
    tex += f"{qn} & {en} / {hi(hn)} & {opts} \\\\[3pt]\n"
tex += tab_end()

# Likert scale note
tex += r"\vspace{4pt}" + "\n"
tex += sec_header("B", "Infrastructure & Facilitating Conditions", H["sec_b"])
tex += r"\small\textit{Likert: 1=Strongly Disagree \quad 2=Disagree \quad 3=Neutral \quad 4=Agree \quad 5=Strongly Agree}" + "\n"
tex += r"\\" + "\n"
tex += r"{\hindifont\small\textit{लिकर्ट: 1=पूर्णतः असहमत \quad 2=असहमत \quad 3=तटस्थ \quad 4=सहमत \quad 5=पूर्णतः सहमत}}" + r"\vspace{3pt}" + "\n\n"

# Section B: Q7-Q12
tex += tab_start()
b_scales = [
    r"{\Large$\square$} Desktop {\Large$\square$} Laptop {\Large$\square$} Tablet {\Large$\square$} Phone {\Large$\square$} None/{\hindifont कोई नहीं}",
    r"{\Large$\square$} Yes, always/{\hindifont हमेशा} {\Large$\square$} Sometimes/{\hindifont कभी-कभी} {\Large$\square$} No, dedicated/{\hindifont नहीं}",
    r"\likert", r"{\Large$\square$} Never {\Large$\square$} 1--2 {\Large$\square$} 3--5 {\Large$\square$} Daily/{\hindifont प्रतिदिन}",
    r"\ymark",
    r"{\Large$\square$} Same day/{\hindifont उसी दिन} {\Large$\square$} 2--3 days {\Large$\square$} 1 week+ {\Large$\square$} Never/{\hindifont कभी नहीं}",
]
for i in range(6, 12):
    qn, en, hn = Q[i]
    tex += f"{qn} & {en} & {b_scales[i-6]} \\\\\n & {hi(hn)} & \\\\[3pt]\n"
tex += tab_end()

# Section C: Q13-Q16
tex += r"\vspace{4pt}" + "\n"
tex += sec_header("C", "Performance Expectancy", H["sec_c"])
tex += tab_start()
for i in range(12, 16):
    qn, en, hn = Q[i]
    tex += f"{qn} & {en} & \\likert \\\\\n & {hi(hn)} & \\\\[3pt]\n"
tex += tab_end()

# Section D: Q17-Q20
tex += r"\vspace{4pt}" + "\n"
tex += sec_header("D", "Effort Expectancy", H["sec_d"])
tex += tab_start()
d_scales = [
    r"\likert{} {\scriptsize(1=Very Easy, 5=Very Difficult)}",
    r"\likert",
    r"{\Large$\square$} <1 day {\Large$\square$} Few days {\Large$\square$} 1--2 weeks {\Large$\square$} >2 weeks",
    r"\likert",
]
for idx, i in enumerate(range(16, 20)):
    qn, en, hn = Q[i]
    tex += f"{qn} & {en} & {d_scales[idx]} \\\\\n & {hi(hn)} & \\\\[3pt]\n"
tex += tab_end()

# Section E: Q21-Q23
tex += r"\vspace{4pt}" + "\n"
tex += sec_header("E", "Social Influence", H["sec_e"])
tex += tab_start()
e_scales = [r"\likert", r"\likert",
    r"{\Large$\square$} Yes/{\hindifont हाँ} {\Large$\square$} No/{\hindifont नहीं} {\Large$\square$} Don't know/{\hindifont पता नहीं}"]
for idx, i in enumerate(range(20, 23)):
    qn, en, hn = Q[i]
    tex += f"{qn} & {en} & {e_scales[idx]} \\\\\n & {hi(hn)} & \\\\[3pt]\n"
tex += tab_end()

# Section F: Q24-Q26
tex += r"\vspace{4pt}" + "\n"
tex += sec_header("F", "Awareness \\& Usage", H["sec_f"])
tex += tab_start()
f_scales = [
    r"{\Large$\square$} e-Office {\Large$\square$} CM Helpline {\Large$\square$} PFMS {\Large$\square$} SPARROW {\Large$\square$} iGOT {\Large$\square$} MP eDistrict",
    r"{\Large$\square$} Daily/{\hindifont प्रतिदिन} {\Large$\square$} Weekly/{\hindifont साप्ताहिक} {\Large$\square$} Monthly/{\hindifont मासिक} {\Large$\square$} Rarely/{\hindifont कभी-कभी} {\Large$\square$} Never/{\hindifont कभी नहीं}",
    r"{\Large$\square$} 0--20\% {\Large$\square$} 21--40\% {\Large$\square$} 41--60\% {\Large$\square$} 61--80\% {\Large$\square$} 81--100\%",
]
for idx, i in enumerate(range(23, 26)):
    qn, en, hn = Q[i]
    tex += f"{qn} & {en} & {f_scales[idx]} \\\\\n & {hi(hn)} & \\\\[3pt]\n"
tex += tab_end()

tex += r"\newpage" + "\n"

# Section G: Q27-Q31
tex += sec_header("G", "Training \\& Capacity Building", H["sec_g"])
tex += tab_start()
g_scales = [
    r"\ymark",
    r"{\Large$\square$} 1 {\Large$\square$} 2--3 {\Large$\square$} 4--5 {\Large$\square$} More than 5",
    r"\likert", r"\likert",
    r"\rule{\linewidth}{0.4pt}\\[2pt] & & \rule{\linewidth}{0.4pt}",
]
for idx, i in enumerate(range(26, 31)):
    qn, en, hn = Q[i]
    tex += f"{qn} & {en} & {g_scales[idx]} \\\\\n & {hi(hn)} & \\\\[3pt]\n"
tex += tab_end()

# Section H: Q32-Q36
tex += r"\vspace{4pt}" + "\n"
tex += sec_header("H", "Challenges \\& Barriers", H["sec_h"])
tex += tab_start()
h_scales = [
    r"{\Large$\square$} Slow internet {\Large$\square$} Crashes {\Large$\square$} No device {\Large$\square$} Complex UI {\Large$\square$} No training {\Large$\square$} No support {\Large$\square$} Power cuts",
    r"{\Large$\square$} Daily {\Large$\square$} Weekly {\Large$\square$} Monthly {\Large$\square$} Rarely {\Large$\square$} Never",
    r"\likert", r"\likert", r"\likert",
]
for idx, i in enumerate(range(31, 36)):
    qn, en, hn = Q[i]
    tex += f"{qn} & {en} & {h_scales[idx]} \\\\\n & {hi(hn)} & \\\\[3pt]\n"
tex += tab_end()

# Section I: Recommendations Q37-Q39
tex += r"\vspace{4pt}" + "\n"
tex += sec_header("I", "Recommendations", H["sec_i"])
qn37, en37, hn37 = Q[36]
tex += f"\\noindent {qn37}. {en37} / {hi(hn37)}\\vspace{{3pt}}\n\n"
tex += r"\noindent\begin{tabularx}{\textwidth}{@{}L{0.8cm} X L{1.5cm}@{}}" + "\n"
ranks = [("Better internet", "बेहतर इंटरनेट"), ("More/better devices", "अधिक/बेहतर उपकरण"),
         ("More training", "अधिक प्रशिक्षण"), ("Simpler portals", "सरल पोर्टल"), ("Faster IT support", "तेज़ IT सहायता")]
for en_r, hi_r in ranks:
    tex += f" & {en_r} / {hi(hi_r)} & Rank: \\_\\_\\_ \\\\[3pt]\n"
tex += tab_end()

tex += r"\vspace{4pt}" + "\n"
qn38, en38, hn38 = Q[37]
tex += f"\\noindent {qn38}. {en38}\\\\\n{hi(hn38)}\\vspace{{3pt}}\n\n"
tex += r"\noindent\rule{\textwidth}{0.4pt}\vspace{4pt}" + "\n"
tex += r"\noindent\rule{\textwidth}{0.4pt}\vspace{4pt}" + "\n"

qn39, en39, hn39 = Q[38]
tex += f"\\noindent {qn39}. {en39}\\\\\n{hi(hn39)}\\vspace{{2pt}}\n\n"
tex += r"\noindent {\Large$\square$} Yes, significantly/{\hindifont हाँ, काफ़ी}\quad{\Large$\square$} Somewhat/{\hindifont कुछ हद तक}\quad{\Large$\square$} No change/{\hindifont कोई बदलाव नहीं}\quad{\Large$\square$} Worsened/{\hindifont बिगड़ा}\quad{\Large$\square$} Can't say/{\hindifont कह नहीं सकते}" + "\n\n"

tex += r"\vspace{4pt}\noindent\rule{\textwidth}{1pt}\vspace{2pt}" + "\n"
tex += r"\begin{center}\textit{--- End of Common Schedule (Q1--Q39) / {\hindifont सामान्य अनुसूची समाप्त} ---}\end{center}" + "\n"
tex += r"\rule{\textwidth}{0.5pt}" + "\n"

# ====== DEPARTMENT SPECIFIC (abbreviated for master schedule) ======
tex += r"\newpage" + "\n"

# Revenue Q40-Q44
tex += sec_header("J", "Department-Specific --- REVENUE / {\\hindifont राजस्व विभाग}", "")
tex += r"\small\textit{Administer ONLY to Revenue respondents / {\hindifont केवल राजस्व विभाग के उत्तरदाताओं के लिए}}\vspace{3pt}" + "\n\n"
tex += tab_start()
from hi import DEPT_REVENUE
rev_scales = [
    r"{\Large$\square$} Bhulekh/WebGIS {\Large$\square$} RCMS {\Large$\square$} SAARA {\Large$\square$} SAMPADA {\Large$\square$} e-Court {\Large$\square$} None/{\hindifont कोई नहीं}",
    r"\likert", r"\likert{} {\scriptsize(1=Easy, 5=Difficult)}",
    r"{\Large$\square$} 0--20\% {\Large$\square$} 21--40\% {\Large$\square$} 41--60\% {\Large$\square$} 61--80\% {\Large$\square$} 81--100\%",
    r"\likert{} {\scriptsize(1=Never, 5=Daily)}",
]
for idx in range(5):
    en, hn = DEPT_REVENUE[idx]
    tex += f"Q{40+idx} & {en} & {rev_scales[idx]} \\\\\n & {hi(hn)} & \\\\[3pt]\n"
tex += tab_end()

# Rural Dev Q45-Q49
tex += r"\vspace{3pt}" + "\n"
tex += sec_header("K", "Department-Specific --- RURAL DEVELOPMENT / {\\hindifont ग्रामीण विकास}", "")
tex += r"\small\textit{Administer ONLY to Rural Development respondents / {\hindifont केवल ग्रामीण विकास उत्तरदाताओं के लिए}}\vspace{3pt}" + "\n\n"
tex += tab_start()
from hi import DEPT_RD
rd_scales = [
    r"{\Large$\square$} NREGASoft/NMMS {\Large$\square$} e-Gram Swaraj {\Large$\square$} PMAY-G {\Large$\square$} SBM-G {\Large$\square$} Panchayat Darpan {\Large$\square$} PFMS {\Large$\square$} None",
    r"\likert{} {\scriptsize(1=Easy, 5=Difficult)}",
    r"\likert", r"\likert",
    r"{\Large$\square$} <1hr {\Large$\square$} 1--2hr {\Large$\square$} 2--4hr {\Large$\square$} 4+hr {\Large$\square$} Almost all day",
]
for idx in range(5):
    en, hn = DEPT_RD[idx]
    tex += f"Q{45+idx} & {en} & {rd_scales[idx]} \\\\\n & {hi(hn)} & \\\\[3pt]\n"
tex += tab_end()

# Forest Q50-Q54
tex += r"\vspace{3pt}" + "\n"
tex += sec_header("L", "Department-Specific --- FOREST / {\\hindifont वन विभाग}", "")
tex += r"\small\textit{Administer ONLY to Forest respondents / {\hindifont केवल वन विभाग उत्तरदाताओं के लिए}}\vspace{3pt}" + "\n\n"
tex += tab_start()
from hi import DEPT_FOREST
for_scales = [
    r"{\Large$\square$} e-Green Watch {\Large$\square$} AI Alert {\Large$\square$} GIS {\Large$\square$} Forest Offence MIS {\Large$\square$} Nursery MIS {\Large$\square$} None",
    r"\likert{}\quad{\Large$\square$} N/A",
    r"\likert{} {\scriptsize(1=Easy, 5=Difficult)}",
    r"{\Large$\square$} Dept-issued {\Large$\square$} Personal device {\Large$\square$} Not available/{\hindifont उपलब्ध नहीं}",
    r"\likert{} {\scriptsize(1=Never, 5=Always)}",
]
for idx in range(5):
    en, hn = DEPT_FOREST[idx]
    tex += f"Q{50+idx} & {en} & {for_scales[idx]} \\\\\n & {hi(hn)} & \\\\[3pt]\n"
tex += tab_end()

# Health Q55-Q59
tex += r"\vspace{3pt}" + "\n"
tex += sec_header("M", "Department-Specific --- HEALTH / {\\hindifont स्वास्थ्य विभाग}", "")
tex += r"\small\textit{Administer ONLY to Health respondents / {\hindifont केवल स्वास्थ्य विभाग उत्तरदाताओं के लिए}}\vspace{3pt}" + "\n\n"
tex += tab_start()
from hi import DEPT_HEALTH
hlth_scales = [
    r"{\Large$\square$} ANMOL {\Large$\square$} HMIS {\Large$\square$} Nikshay {\Large$\square$} eVIN {\Large$\square$} IHIP {\Large$\square$} ABHA {\Large$\square$} MPCDSR {\Large$\square$} None",
    r"\likert", r"\likert{} {\scriptsize(1=Never, 5=Always)}",
    r"\likert{} {\scriptsize(1=Unreliable, 5=Reliable)}",
    r"\likert{} {\scriptsize(1=None, 5=Significant)}",
]
for idx in range(5):
    en, hn = DEPT_HEALTH[idx]
    tex += f"Q{55+idx} & {en} & {hlth_scales[idx]} \\\\\n & {hi(hn)} & \\\\[3pt]\n"
tex += tab_end()

tex += r"\newpage" + "\n"

# Section N: Role-Specific Q60-Q67
tex += sec_header("N", "Role-Specific Questions", H["sec_n"])
tex += tab_start()
role_scales = [
    r"{\Large$\square$} Data entry {\Large$\square$} Review/approve {\Large$\square$} Field verification {\Large$\square$} Don't use {\Large$\square$} Other",
    r"{\Large$\square$} Yes, one person {\Large$\square$} A few share {\Large$\square$} Everyone does own {\Large$\square$} N/A",
    r"\likert",
    r"{\Large$\square$} Wait for IT {\Large$\square$} Ask colleague {\Large$\square$} Use paper {\Large$\square$} Fix myself {\Large$\square$} Tell supervisor {\Large$\square$} Abandon",
    r"{\Large$\square$} Yes/{\hindifont हाँ} {\Large$\square$} Rely on subordinates {\Large$\square$} Mixed {\Large$\square$} Don't know",
    r"\likert{} {\scriptsize(1=No change, 5=Completely)}",
    r"{\Large$\square$} Yes/{\hindifont हाँ} {\Large$\square$} No/{\hindifont नहीं}\quad If yes: \rule{4cm}{0.4pt}",
    r"{\Large$\square$} Yes {\Large$\square$} Somewhat {\Large$\square$} No\quad Why: \rule{3.5cm}{0.4pt}",
]
for idx, (en, hn) in enumerate(ROLE):
    tex += f"Q{60+idx} & {en} & {role_scales[idx]} \\\\\n & {hi(hn)} & \\\\[3pt]\n"
tex += tab_end()

# Section O: Personal Tools Q68-Q73
tex += r"\vspace{4pt}" + "\n"
tex += sec_header("O", "Personal \\& Non-Government Tools", H["sec_o"])
tex += tab_start()
pt_scales = [
    r"\ymark",
    r"{\Large$\square$} WhatsApp {\Large$\square$} Google Docs/Drive {\Large$\square$} ChatGPT/AI {\Large$\square$} YouTube {\Large$\square$} Personal email {\Large$\square$} MS Office {\Large$\square$} Google Translate {\Large$\square$} Other: \rule{2cm}{0.4pt}",
    r"{\Large$\square$} Drafting {\Large$\square$} Translating {\Large$\square$} Coordinating {\Large$\square$} Learning portals {\Large$\square$} Backup {\Large$\square$} Sharing files {\Large$\square$} Other: \rule{2cm}{0.4pt}",
    r"{\Large$\square$} Daily {\Large$\square$} Few times/week {\Large$\square$} Occasionally {\Large$\square$} Rarely {\Large$\square$} Never",
    r"\likert{} {\scriptsize(1=Not at all, 5=Absolutely)}",
    r"\rule{\linewidth}{0.4pt}\\[3pt] && \rule{\linewidth}{0.4pt}",
]
for idx, (en, hn) in enumerate(PERSONAL):
    tex += f"Q{68+idx} & {en} & {pt_scales[idx]} \\\\\n & {hi(hn)} & \\\\[3pt]\n"
tex += tab_end()

# END
tex += r"""
\vspace{3pt}\noindent\rule{\textwidth}{1pt}
\begin{center}
{\large\bfseries --- END OF SCHEDULE / {\hindifont अनुसूची समाप्त} ---}\\[3pt]
\textbf{Total Questions / {\hindifont कुल प्रश्न}:} 39 + 5 + 8 + 6 = \textbf{58}\\[8pt]
\textbf{Interviewer Notes / {\hindifont साक्षात्कारकर्ता नोट्स}:}\vspace{4pt}

\rule{\textwidth}{0.4pt}\vspace{4pt}
\rule{\textwidth}{0.4pt}\vspace{4pt}
\rule{\textwidth}{0.4pt}\vspace{12pt}

\textbf{Signature / {\hindifont हस्ताक्षर}:} \rule{5cm}{0.4pt}\qquad\textbf{Date / {\hindifont दिनांक}:} \_\_\_/\_\_\_/2026
\end{center}
\end{document}
"""

fname = "AIGGPA_Printable_Schedule.tex"
with open(fname, "w", encoding="utf-8") as f:
    f.write(tex)
print(f"Generated: {fname}")

# Compile with xelatex
for _ in range(2):
    subprocess.run(["xelatex", "-interaction=nonstopmode", fname], capture_output=True, cwd=os.getcwd())

pdf = fname.replace(".tex", ".pdf")
if os.path.exists(pdf):
    print(f"Compiled: {pdf}")
    shutil.copy2(pdf, os.path.join(r"c:\Users\aryan\Downloads", pdf))
    print("Copied to Downloads")
else:
    print("ERROR: PDF not found")
