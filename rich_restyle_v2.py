import re

filepath = "concept_proposal_final_v3.tex"

with open(filepath, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Fix Undefined color 'lightsec' in chart background
text = text.replace("fill=lightsec", "fill=sectionbg")

# 2. Fix the alignment and spacing for \techsection again (ensure it's professional)
# The user said 1 page per heading is a bad idea, so I ensure clearpage is gone.
text = text.replace(r"\newcommand{\sectionbreak}{\clearpage}", "")
new_techsection_refined = r"""\newcommand{\techsection}[1]{%
  \vspace{0.6cm}\noindent
  {\fontsize{14}{17}\selectfont\bfseries\color{graphite}\MakeUppercase{#1}}%
  \\[-0.15cm]\rule{\textwidth}{1.2pt}\vspace{0.3cm}%
}"""
text = re.sub(r"\\newcommand\{\\techsection\}\[1\]\{.*?\}", lambda m: new_techsection_refined, text, flags=re.DOTALL)

# 3. Fix the tabularx errors In the UTAUT Gap Analysis Matrices
# The error "Misplaced \noalign" or "Extra alignment tab" often happens when \rowcolor 
# competes with \columncolor. I will strip \columncolor from the preamble 
# and use \rowcolor or \cellcolor for the headers/rows to be safer.

def fix_matrix(matrix_text):
    # Remove \columncolor from preamble to avoid clash with \rowcolor and fixing alignment issues
    matrix_text = re.sub(r">\{\\columncolor\{.*?\}\s*.*?\}", "", matrix_text)
    # Re-insert basic alignment
    matrix_text = matrix_text.replace(r"\begin{tabularx}{\textwidth}{", r"\begin{tabularx}{\textwidth}{C{2.6cm} C C C C}")
    return matrix_text

# Define a custom column type for centering in tabularx
if r"\newcolumntype{C}" not in text:
    text = text.replace(r"\usepackage{tabularx}", r"\usepackage{tabularx}" + "\n" + r"\newcolumntype{C}{>{\centering\arraybackslash}X}" + "\n" + r"\newcolumntype{L}[1]{>{\raggedright\arraybackslash}p{#1}}")

# Fix Matrix A
matrix_a_search = re.compile(r"Matrix A.*?\\begin\{tabularx\}\{\\textwidth\}.*?\\end\{tabularx\}", re.DOTALL)
def matrix_a_sub(m):
    obj = m.group(0)
    # Header row color
    obj = re.sub(r"Department &", r"\\rowcolor{graphite}\\color{white}Department &", obj)
    # Rows
    obj = obj.replace(r"\rowcolor{white}", r"\rowcolor{white}")
    obj = obj.replace(r"\rowcolor{lightgray}", r"\rowcolor{sectionbg}") # Use sectionbg for soft look
    return obj

# Actually I'll do a manual replace for the matrices to be 100% sure
new_matrix_a = r"""\noindent\small\textbf{Matrix A (Secretariat-Level Workflow Tools; e.g., e-Office, HRMIS)}
\renewcommand{\arraystretch}{1.6}
\begin{tabularx}{\textwidth}{l C C C C}
\rowcolor{graphite}
\textbf{\color{white}Department} & \textbf{\color{white}Perform. (PE)} & \textbf{\color{white}Effort (EE)} & \textbf{\color{white}Social (SI)} & \textbf{\color{white}Cond. (FC)} \\
\rowcolor{white}
School Edu. & & & & \\
\rowcolor{sectionbg}
Health & & & & \\
\rowcolor{white}
Forest & & & & \\
\end{tabularx}"""

text = re.sub(r"\\noindent\\small\\textbf\{Matrix A.*?\\end\{tabularx\}", lambda m: new_matrix_a, text, flags=re.DOTALL)

new_matrix_b = r"""\noindent\small\textbf{Matrix B (Territorial/Field Execution MIS; e.g., Education P3, CHETNA)}
\renewcommand{\arraystretch}{1.6}
\begin{tabularx}{\textwidth}{l C C C C}
\rowcolor{cyan}
\textbf{\color{white}Department} & \textbf{\color{white}Perform. (PE)} & \textbf{\color{white}Effort (EE)} & \textbf{\color{white}Social (SI)} & \textbf{\color{white}Cond. (FC)} \\
\rowcolor{white}
School Edu. & & & & \\
\rowcolor{sectionbg}
Health & & & & \\
\rowcolor{white}
Forest & & & & \\
\end{tabularx}"""

text = re.sub(r"\\noindent\\small\\textbf\{Matrix B.*?\\end\{tabularx\}", lambda m: new_matrix_b, text, flags=re.DOTALL)

# Fix the Work Plan table too, it might have similar issues
new_work_plan = r"""\renewcommand{\arraystretch}{1.8}
\begin{tabularx}{\textwidth}{L{2cm} L{4cm} X}
\rowcolor{graphite}
\textbf{\color{white}Phase} & \textbf{\color{white}Activity} & \textbf{\color{white}Deliverable / Milestone} \\
\rowcolor{white}
Week 1 to 2 & Literature review; finalise theoretical framework & Completed proposal; supervisor sign-off \\
\rowcolor{sectionbg}
Week 3 & Design and pilot-test interview guides and observation checklist & Revised instruments approved \\
\rowcolor{white}
Week 4 to 5 & School Education Department: interviews \& observations & 18 Stratified Case Studies \\
\rowcolor{sectionbg}
Week 6 to 7 & Health Department: interviews \& observations & 18 Stratified Case Studies \\
\rowcolor{white}
Week 8 & Forest Department: interviews \& observations & 18 Stratified Case Studies \\
\rowcolor{sectionbg}
Week 9 & Data coding, UTAUT classification, gap matrix construction & Draft gap analysis matrix \\
\rowcolor{white}
Week 10 & Write final report; prepare AIGGPA recommendations deck & Final report + presentation \\
\end{tabularx}"""

text = re.sub(r"\\section\{Work Plan\}.*?\\begin\{tabularx\}\{\\textwidth\}.*?\\end\{tabularx\}", lambda m: r"\section{Work Plan}\n\n\vspace{0.2cm}\n" + new_work_plan, text, flags=re.DOTALL)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(text)
