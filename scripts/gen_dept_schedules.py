"""Generate 4 bilingual dept schedules using xelatex + hi.py translations."""
import subprocess, os, shutil
from hi import H, Q, ROLE, PERSONAL, DEPT_REVENUE, DEPT_RD, DEPT_FOREST, DEPT_HEALTH

def hi(t): return r"{\hindifont\small\itshape\color{black!70} " + t + "}"

DEPTS = {
"Revenue": {"hi": "राजस्व", "tools": "MP Bhulekh / WebGIS 2.0, RCMS, SAARA, SAMPADA 2.0, e-Court",
 "qs": DEPT_REVENUE, "scales": [
    r"{\Large$\square$} Bhulekh/WebGIS {\Large$\square$} RCMS {\Large$\square$} SAARA {\Large$\square$} SAMPADA 2.0 {\Large$\square$} e-Court {\Large$\square$} None",
    r"\likert", r"\likert{} {\scriptsize(1=Easy, 5=Difficult)}",
    r"{\Large$\square$} 0--20\% {\Large$\square$} 21--40\% {\Large$\square$} 41--60\% {\Large$\square$} 61--80\% {\Large$\square$} 81--100\%",
    r"\likert{} {\scriptsize(1=Never, 5=Daily)}",
    r"Digital: \rule{5cm}{0.4pt}\\[2pt] && Paper: \rule{5cm}{0.4pt}",
    r"{\Large$\square$} Much faster {\Large$\square$} Somewhat {\Large$\square$} No change {\Large$\square$} Slower {\Large$\square$} Don't use",
    r"{\Large$\square$} Never {\Large$\square$} Rarely {\Large$\square$} Sometimes {\Large$\square$} Often {\Large$\square$} Always",
    r"\rule{\linewidth}{0.4pt}\\[2pt] && \rule{\linewidth}{0.4pt}",
    r"{\Large$\square$} Yes, separated {\Large$\square$} Somewhat {\Large$\square$} No, same {\Large$\square$} Don't know",
]},
"Rural Development": {"hi": "ग्रामीण विकास", "tools": "NREGASoft / NMMS, e-Gram Swaraj, PMAY-G, SBM-G, Panchayat Darpan, PFMS",
 "qs": DEPT_RD, "scales": [
    r"{\Large$\square$} NREGASoft/NMMS {\Large$\square$} e-Gram Swaraj {\Large$\square$} PMAY-G {\Large$\square$} SBM-G {\Large$\square$} Panchayat Darpan {\Large$\square$} PFMS {\Large$\square$} None",
    r"\likert{} {\scriptsize(1=Easy, 5=Difficult)}", r"\likert", r"\likert",
    r"{\Large$\square$} <1hr {\Large$\square$} 1--2hr {\Large$\square$} 2--4hr {\Large$\square$} 4+hr {\Large$\square$} Almost all day",
    r"Digital: \rule{5cm}{0.4pt}\\[2pt] && Paper: \rule{5cm}{0.4pt}",
    r"{\Large$\square$} Yes, regularly {\Large$\square$} A few times {\Large$\square$} Someone else {\Large$\square$} Never",
    r"{\Large$\square$} Wait/retry {\Large$\square$} Paper, upload later {\Large$\square$} Block office {\Large$\square$} Ask someone {\Large$\square$} Skip",
    r"\rule{\linewidth}{0.4pt}\\[2pt] && \rule{\linewidth}{0.4pt}",
    r"{\Large$\square$} Reviews regularly {\Large$\square$} Sometimes {\Large$\square$} Only district {\Large$\square$} Nobody {\Large$\square$} Don't know",
]},
"Forest": {"hi": "वन", "tools": "e-Green Watch (CAMPA), AI Forest Alert, GIS/Remote Sensing, Forest Offence MIS, Nursery MIS",
 "qs": DEPT_FOREST, "scales": [
    r"{\Large$\square$} e-Green Watch {\Large$\square$} AI Alert {\Large$\square$} GIS/Remote Sensing {\Large$\square$} Offence MIS {\Large$\square$} Nursery MIS {\Large$\square$} None",
    r"\likert{}\quad{\Large$\square$} N/A", r"\likert{} {\scriptsize(1=Easy, 5=Difficult)}",
    r"{\Large$\square$} Dept-issued {\Large$\square$} Personal phone {\Large$\square$} Not available",
    r"\likert{} {\scriptsize(1=Never, 5=Always)}",
    r"\rule{\linewidth}{0.4pt}\\[2pt] && \rule{\linewidth}{0.4pt}",
    r"Digital: \rule{5cm}{0.4pt}\\[2pt] && Paper: \rule{5cm}{0.4pt}",
    r"{\Large$\square$} Formal training {\Large$\square$} From colleague {\Large$\square$} Self-taught {\Large$\square$} No training",
    r"\rule{\linewidth}{0.4pt}\\[2pt] && \rule{\linewidth}{0.4pt}",
    r"{\Large$\square$} Reviews personally {\Large$\square$} Delegates {\Large$\square$} Mixed {\Large$\square$} Don't know",
]},
"Health": {"hi": "स्वास्थ्य", "tools": "ANMOL MP, HMIS, Nikshay, eVIN, IHIP, Ayushman/ABHA, MPCDSR",
 "qs": DEPT_HEALTH, "scales": [
    r"{\Large$\square$} ANMOL {\Large$\square$} HMIS {\Large$\square$} Nikshay {\Large$\square$} eVIN {\Large$\square$} IHIP {\Large$\square$} ABHA {\Large$\square$} MPCDSR {\Large$\square$} None",
    r"\likert", r"\likert{} {\scriptsize(1=Never, 5=Always)}",
    r"\likert{} {\scriptsize(1=Unreliable, 5=Reliable)}",
    r"\likert{} {\scriptsize(1=None, 5=Significant)}",
    r"ANMOL: \rule{5cm}{0.4pt}\\[2pt] && Paper: \rule{5cm}{0.4pt}",
    r"{\Large$\square$} I enter {\Large$\square$} DEO {\Large$\square$} District {\Large$\square$} Don't use {\Large$\square$} N/A",
    r"{\Large$\square$} IHIP immediately {\Large$\square$} Phone BMO {\Large$\square$} Paper to CMHO {\Large$\square$} WhatsApp {\Large$\square$} Multiple",
    r"\rule{\linewidth}{0.4pt}\\[2pt] && \rule{\linewidth}{0.4pt}",
    r"{\Large$\square$} Reviews regularly {\Large$\square$} Sometimes {\Large$\square$} Only inspections {\Large$\square$} Never {\Large$\square$} Don't know",
]},
}

def header(dept, dept_hi):
    return r"""\documentclass[10pt,a4paper]{article}
\usepackage[margin=0.8cm]{geometry}\usepackage{fontspec}\usepackage{tabularx}
\usepackage{array}\usepackage{booktabs}\usepackage{fancyhdr}\usepackage{setspace}\usepackage{amssymb}\usepackage{xcolor}
\setmainfont{Times New Roman}
\newfontfamily\hindifont{Nirmala UI}
\pagestyle{fancy}\fancyhf{}
\fancyhead[L]{\small\textbf{AIGGPA --- """ + dept + r"""}}
\fancyhead[R]{\small Respondent ID: \_\_\_\_\_\_\_\_}
\fancyfoot[C]{\small Page \thepage}\renewcommand{\headrulewidth}{0.5pt}
\setlength{\headheight}{14pt}\setstretch{1.05}
\newcolumntype{L}[1]{>{}\raggedright\arraybackslash}p{#1}}
\newcommand{\likert}{{\Large$\square$}\,1\quad{\Large$\square$}\,2\quad{\Large$\square$}\,3\quad{\Large$\square$}\,4\quad{\Large$\square$}\,5}
\newcommand{\ymark}{{\Large$\square$}\,Yes/{\hindifont\itshape हाँ}\quad{\Large$\square$}\,No/{\hindifont\itshape नहीं}}
\newcommand{\blank}{\rule{7cm}{0.4pt}}
\begin{document}
\begin{center}
{\Large\bfseries AIGGPA FIELD RESEARCH SCHEDULE}\\[1pt]
{\large\bfseries """ + dept + r""" Department}\\[1pt]
{\hindifont\itshape\color{black!70} """ + dept_hi + r""" विभाग}\\[4pt]
{\small Digital Tool Usage Assessment}\\[1pt]
{\small\hindifont\itshape\color{black!70} डिजिटल उपकरण उपयोग मूल्यांकन}\\[3pt]
{\small AIGGPA Bhopal \quad$\bullet$\quad 2026}
\end{center}
\vspace{4pt}\noindent\rule{\textwidth}{1pt}\vspace{4pt}
\noindent\begin{tabularx}{\textwidth}{@{}L{9.5cm} X@{}}
\textbf{ID:} \blank & \textbf{Date:} \_\_\_/\_\_\_/2026 \\[4pt]
\textbf{Office:} {\Large$\square$} HO\quad{\Large$\square$} District & \textbf{Time:} \_\_:\_\_\quad to\quad\_\_:\_\_ \\[4pt]
\textbf{Interviewer:} \blank & \\
\end{tabularx}
\vspace{4pt}\noindent\rule{\textwidth}{0.5pt}\vspace{4pt}
\noindent\textbf{Key Digital Tools:} """ + DEPTS[dept]["tools"] + r"""
\vspace{3pt}\noindent\rule{\textwidth}{0.5pt}
"""

def sec(letter, en, hn):
    if hn:
        return f"\\noindent\\rule{{\\textwidth}}{{0.3pt}}\\vspace{{3pt}}\n\\noindent{{\\large\\bfseries Section {letter}: {en}}}\\\\\n{{\\hindifont\\itshape\\color{{black!70}} {hn}}}\\vspace{{3pt}}\n\n"
    return f"\\noindent\\rule{{\\textwidth}}{{0.3pt}}\\vspace{{3pt}}\n\\noindent{{\\large\\bfseries Section {letter}: {en}}}\\vspace{{3pt}}\n\n"

TS = r"\noindent\begin{tabularx}{\textwidth}{@{}L{0.8cm} X L{5.2cm}@{}}" + "\n"
TE = r"\end{tabularx}" + "\n"

# Common section scales (same for all depts)
B_SC = [r"{\Large$\square$} Desktop {\Large$\square$} Laptop {\Large$\square$} Tablet {\Large$\square$} Phone {\Large$\square$} None",
    r"{\Large$\square$} Always {\Large$\square$} Sometimes {\Large$\square$} No, dedicated", r"\likert",
    r"{\Large$\square$} Never {\Large$\square$} 1--2 {\Large$\square$} 3--5 {\Large$\square$} Daily", r"\ymark",
    r"{\Large$\square$} Same day {\Large$\square$} 2--3 days {\Large$\square$} 1 week+ {\Large$\square$} Never"]
D_SC = [r"\likert{} {\scriptsize(1=Easy, 5=Difficult)}", r"\likert",
    r"{\Large$\square$} <1 day {\Large$\square$} Few days {\Large$\square$} 1--2 weeks {\Large$\square$} >2 weeks", r"\likert"]
E_SC = [r"\likert", r"\likert", r"\ymark\quad{\Large$\square$} Don't know",
    r"{\Large$\square$} e-Office {\Large$\square$} CM Helpline {\Large$\square$} PFMS {\Large$\square$} SPARROW {\Large$\square$} iGOT {\Large$\square$} eDistrict",
    r"{\Large$\square$} Daily {\Large$\square$} Weekly {\Large$\square$} Monthly {\Large$\square$} Rarely {\Large$\square$} Never",
    r"{\Large$\square$} 0--20\% {\Large$\square$} 21--40\% {\Large$\square$} 41--60\% {\Large$\square$} 61--80\% {\Large$\square$} 81--100\%"]
F_SC = [r"\ymark", r"{\Large$\square$} 1 {\Large$\square$} 2--3 {\Large$\square$} 4--5 {\Large$\square$} 5+",
    r"\likert", r"\likert", r"\rule{\linewidth}{0.4pt}\\[2pt] & & \rule{\linewidth}{0.4pt}"]
G_SC = [r"{\Large$\square$} Slow net {\Large$\square$} Crashes {\Large$\square$} No device {\Large$\square$} Complex UI {\Large$\square$} No training {\Large$\square$} Power cuts",
    r"{\Large$\square$} Daily {\Large$\square$} Weekly {\Large$\square$} Monthly {\Large$\square$} Rarely {\Large$\square$} Never",
    r"\likert", r"\likert", r"\likert"]
ROLE_SC = [
    r"{\Large$\square$} Data entry {\Large$\square$} Review {\Large$\square$} Field {\Large$\square$} Don't use {\Large$\square$} Other",
    r"{\Large$\square$} Yes, one {\Large$\square$} A few {\Large$\square$} Everyone {\Large$\square$} N/A",
    r"\likert",
    r"{\Large$\square$} Wait IT {\Large$\square$} Colleague {\Large$\square$} Paper {\Large$\square$} Fix myself {\Large$\square$} Supervisor {\Large$\square$} Abandon",
    r"{\Large$\square$} Yes {\Large$\square$} Subordinates {\Large$\square$} Mixed {\Large$\square$} Don't know",
    r"\likert{} {\scriptsize(1=No change, 5=Completely)}",
    r"\ymark\quad If yes: \rule{3cm}{0.4pt}",
    r"{\Large$\square$} Yes {\Large$\square$} Somewhat {\Large$\square$} No\quad Why: \rule{3cm}{0.4pt}"]
PT_SC = [r"\ymark",
    r"{\Large$\square$} WhatsApp {\Large$\square$} Google Docs {\Large$\square$} ChatGPT {\Large$\square$} YouTube {\Large$\square$} Email {\Large$\square$} MS Office {\Large$\square$} Translate {\Large$\square$} Other: \rule{2cm}{0.4pt}",
    r"{\Large$\square$} Drafting {\Large$\square$} Translating {\Large$\square$} Coordinating {\Large$\square$} Learning {\Large$\square$} Backup {\Large$\square$} Sharing {\Large$\square$} Other: \rule{2cm}{0.4pt}",
    r"{\Large$\square$} Daily {\Large$\square$} Few times/week {\Large$\square$} Occasionally {\Large$\square$} Rarely {\Large$\square$} Never",
    r"\likert{} {\scriptsize(1=Not at all, 5=Absolutely)}",
    r"\rule{\linewidth}{0.4pt}\\[2pt] && \rule{\linewidth}{0.4pt}"]

def bq(qn, en, hn, sc):
    return f"{qn} & {en} & {sc} \\\\\n & {hi(hn)} & \\\\[3pt]\n"

for dept_name, dd in DEPTS.items():
    safe = dept_name.replace(" ", "_")
    fname = f"Schedule_{safe}.tex"
    tex = header(dept_name, dd["hi"])

    # A: Q1-Q6
    tex += sec("A", "Respondent Profile", H["sec_a"])
    tex += r"\noindent\begin{tabularx}{\textwidth}{@{}L{0.8cm} L{7.2cm} X@{}}" + "\n"
    a_sc = [r"\blank", r"\blank",
        r"{\Large$\square$} <30 {\Large$\square$} 30--45 {\Large$\square$} 46--60",
        r"{\Large$\square$} M {\Large$\square$} F {\Large$\square$} Other",
        r"{\Large$\square$} 0--5 {\Large$\square$} 6--10 {\Large$\square$} 11--20 {\Large$\square$} 21+",
        r"{\Large$\square$} Up to 12th {\Large$\square$} Grad {\Large$\square$} PG {\Large$\square$} Prof"]
    for i in range(6):
        qn, en, hn = Q[i]
        tex += f"{qn} & {en} / {hi(hn)} & {a_sc[i]} \\\\[3pt]\n"
    tex += TE

    # B: Q7-12
    tex += r"\vspace{3pt}" + "\n"
    tex += sec("B", "Infrastructure", H["sec_b"])
    tex += r"\small\textit{Likert: 1=Strongly Disagree ... 5=Strongly Agree / {\hindifont 1=पूर्णतः असहमत ... 5=पूर्णतः सहमत}}\vspace{3pt}" + "\n\n"
    tex += TS
    for i in range(6,12): tex += bq(Q[i][0], Q[i][1], Q[i][2], B_SC[i-6])
    tex += TE

    # C: Q13-16
    tex += r"\vspace{3pt}" + "\n" + sec("C", "Performance Expectancy", H["sec_c"]) + TS
    for i in range(12,16): tex += bq(Q[i][0], Q[i][1], Q[i][2], r"\likert")
    tex += TE

    # D: Q17-20
    tex += r"\vspace{3pt}" + "\n" + sec("D", "Effort Expectancy", H["sec_d"]) + TS
    for i in range(16,20): tex += bq(Q[i][0], Q[i][1], Q[i][2], D_SC[i-16])
    tex += TE

    # E: Q21-26
    tex += r"\vspace{3pt}" + "\n" + sec("E", "Social Influence \\& Awareness", H["sec_e"]) + TS
    for i in range(20,26): tex += bq(Q[i][0], Q[i][1], Q[i][2], E_SC[i-20])
    tex += TE

    tex += r"\newpage" + "\n"

    # F: Q27-31
    tex += sec("F", "Training", H["sec_g"]) + TS
    for i in range(26,31): tex += bq(Q[i][0], Q[i][1], Q[i][2], F_SC[i-26])
    tex += TE

    # G: Q32-36
    tex += r"\vspace{3pt}" + "\n" + sec("G", "Challenges", H["sec_h"]) + TS
    for i in range(31,36): tex += bq(Q[i][0], Q[i][1], Q[i][2], G_SC[i-31])
    tex += TE

    # H: Q37-39
    tex += r"\vspace{3pt}" + "\n" + sec("H", "Recommendations", H["sec_i"])
    tex += f"\\noindent Q37. {Q[36][1]} / {hi(Q[36][2])}\\vspace{{3pt}}\n\n"
    tex += r"\noindent\begin{tabularx}{\textwidth}{@{}L{0.8cm} X L{1.5cm}@{}}" + "\n"
    for en_r, hi_r in [("Better internet","बेहतर इंटरनेट"),("More devices","अधिक उपकरण"),("More training","अधिक प्रशिक्षण"),("Simpler portals","सरल पोर्टल"),("Faster IT","तेज़ IT")]:
        tex += f" & {en_r} / {hi(hi_r)} & Rank: \\_\\_\\_ \\\\[2pt]\n"
    tex += TE
    tex += f"\\vspace{{3pt}}\\noindent Q38. {Q[37][1]} / {hi(Q[37][2])}\\vspace{{3pt}}\n\n"
    tex += r"\noindent\rule{\textwidth}{0.4pt}\vspace{3pt}\rule{\textwidth}{0.4pt}\vspace{3pt}" + "\n"
    tex += f"\\noindent Q39. {Q[38][1]} / {hi(Q[38][2])}\\vspace{{2pt}}\n\n"
    tex += r"\noindent {\Large$\square$} Yes, significantly\quad{\Large$\square$} Somewhat\quad{\Large$\square$} No change\quad{\Large$\square$} Worsened\quad{\Large$\square$} Can't say" + "\n"
    tex += r"\vspace{3pt}\noindent\rule{\textwidth}{1pt}\vspace{2pt}" + "\n"
    tex += r"\begin{center}\textit{--- Common Questions End (Q1--Q39) ---}\end{center}\rule{\textwidth}{0.5pt}" + "\n"

    # Dept-specific Q40-Q49
    tex += r"\newpage" + "\n"
    tex += sec("I", f"{dept_name} --- Specific / {{\\hindifont {dd['hi']} विभाग विशिष्ट}}", "")
    tex += TS
    for idx in range(10):
        en, hn = dd["qs"][idx]
        tex += bq(f"Q{40+idx}", en, hn, dd["scales"][idx])
    tex += TE

    # Role Q50-Q57
    tex += r"\vspace{3pt}" + "\n" + sec("J", "Role-Specific", H["sec_n"]) + TS
    for idx in range(8):
        en, hn = ROLE[idx]
        tex += bq(f"Q{50+idx}", en, hn, ROLE_SC[idx])
    tex += TE

    # Personal tools Q58-Q63
    tex += r"\vspace{3pt}" + "\n" + sec("K", "Personal \\& Non-Government Tools", H["sec_o"])
    tex += TS
    for idx in range(6):
        en, hn = PERSONAL[idx]
        tex += bq(f"Q{58+idx}", en, hn, PT_SC[idx])
    tex += TE

    # End
    tex += r"""
\vspace{3pt}\noindent\rule{\textwidth}{1pt}
\begin{center}
{\large\bfseries --- END / {\hindifont समाप्त} ---}\\[2pt]
\textbf{Total: 39 + 10 + 8 + 6 = 63}\\[6pt]
\textbf{Notes:}\vspace{3pt}
\rule{\textwidth}{0.4pt}\vspace{3pt}\rule{\textwidth}{0.4pt}\vspace{3pt}\rule{\textwidth}{0.4pt}\vspace{4pt}
\textbf{Signature:} \rule{5cm}{0.4pt}\qquad\textbf{Date:} \_\_\_/\_\_\_/2026
\end{center}
\end{document}
"""
    with open(fname, "w", encoding="utf-8") as f: f.write(tex)
    print(f"Created: {fname}")
    for _ in range(2):
        subprocess.run(["xelatex", "-interaction=nonstopmode", fname], capture_output=True, cwd=os.getcwd())
    pdf = fname.replace(".tex",".pdf")
    if os.path.exists(pdf):
        print(f"  Compiled: {pdf}")
        shutil.copy2(pdf, os.path.join(r"c:\Users\aryan\Downloads", pdf))
        print(f"  Copied to Downloads")
    else: print(f"  ERROR: {pdf} not found")

print("\nDone! 4 bilingual department schedules ready.")
