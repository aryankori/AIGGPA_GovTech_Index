import os
import re

def escape_latex(text):
    # Escape special LaTeX characters
    text = text.replace('\\', '\\textbackslash ')
    text = text.replace('&', '\\&')
    text = text.replace('%', '\\%')
    text = text.replace('$', '\\$')
    text = text.replace('#', '\\#')
    text = text.replace('_', '\\_')
    text = text.replace('{', '\\{')
    text = text.replace('}', '\\}')
    text = text.replace('~', '\\textasciitilde ')
    text = text.replace('^', '\\textasciicircum ')
    return text

def generate_tex():
    with open('temp_docx_dump.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    tex_content = r"""\documentclass[11pt,a4paper]{article}
\usepackage{fontspec}
\setmainfont{Nirmala UI}
\usepackage{geometry}
\geometry{a4paper, margin=0.8in, headheight=14pt}
\usepackage{amssymb} % For square and circle
\usepackage{color}
\usepackage{fancyhdr}
\usepackage{titlesec}
\usepackage{tcolorbox}
\usepackage{enumitem}

\definecolor{primary}{rgb}{0.1, 0.3, 0.6}
\titleformat{\section}{\large\bfseries\color{primary}}{}{0em}{}[\titlerule]

\pagestyle{fancy}
\fancyhf{}
\rhead{\textcolor{gray}{AIGGPA Research Fieldwork}}
\lhead{\textcolor{gray}{Survey Schedule}}
\rfoot{\thepage}

\setlength{\parindent}{0pt}
\newcounter{qcounter}

\begin{document}

\begin{center}
    {\LARGE \bfseries \color{primary} AIGGPA Fieldwork Schedule} \\ \vspace{0.2cm}
    {\Large \bfseries Assessment of Digital Tool Adoption \& Efficiency} \\ \vspace{0.2cm}
    \textit{Please fill out this form clearly. All responses are confidential.}
\end{center}
\vspace{0.5cm}

"""

    for line in lines:
        line = line.strip()
        if not line: continue
        
        if line.startswith("AIGGPA Questionnaire"):
            continue

        if line.startswith("Section"):
            # Section 1: Personal Information / ...
            safe_line = escape_latex(line)
            tex_content += f"\n\\section*{{{safe_line}}}\n\\vspace{{0.2cm}}\n"
        
        elif line.startswith("Q:"):
            # Extract question text, type, and options
            match = re.search(r"Q: (.*?)\s+Type: (.*?)(?:\s+Options: (.*))?$", line)
            if not match:
                print(f"Failed to parse line: {line}")
                continue
                
            q_text = escape_latex(match.group(1))
            q_type = match.group(2).strip()
            options_str = match.group(3)
            
            tex_content += "\\stepcounter{qcounter}\n"
            tex_content += f"\\textbf{{\\arabic{{qcounter}}. {q_text}}}\n\\vspace{{0.1cm}}\n"
            
            if q_type == "Short Answer":
                tex_content += "\\vspace{0.2cm}\n\\hrulefill\n\\vspace{0.4cm}\n\n"
                
            elif q_type == "Paragraph":
                tex_content += "\\vspace{0.2cm}\n\\hrulefill\\par\\vspace{0.6cm}\\hrulefill\\par\\vspace{0.6cm}\\hrulefill\n\\vspace{0.4cm}\n\n"
                
            elif q_type == "Scale (1 to 5)":
                tex_content += "\\vspace{0.1cm}\n"
                tex_content += "1 $\\bigcirc$ \\hspace{1cm} 2 $\\bigcirc$ \\hspace{1cm} 3 $\\bigcirc$ \\hspace{1cm} 4 $\\bigcirc$ \\hspace{1cm} 5 $\\bigcirc$\n"
                tex_content += "\\vspace{0.4cm}\n\n"
                
            elif q_type in ["RADIO", "CHECKBOX"]:
                symbol = r"$\bigcirc$" if q_type == "RADIO" else r"$\square$"
                tex_content += "\\begin{itemize}[label=, itemsep=0.1cm, leftmargin=0.5cm]\n"
                if options_str:
                    options = [o.strip() for o in options_str.split(" - ") if o.strip()]
                    if options and options_str.startswith("-"):
                        options = [o for o in options if o]
                    
                    for opt in options:
                        if opt.startswith("-"): opt = opt[1:].strip()
                        safe_opt = escape_latex(opt)
                        tex_content += f"    \\item {symbol} {safe_opt}\n"
                tex_content += "\\end{itemize}\n\\vspace{0.2cm}\n\n"

    tex_content += "\\end{document}\n"

    os.makedirs('schedules/tex', exist_ok=True)
    with open('schedules/tex/AIGGPA_Fieldwork_Schedule.tex', 'w', encoding='utf-8') as f:
        f.write(tex_content)
    print("LaTeX schedule generated at schedules/tex/AIGGPA_Fieldwork_Schedule.tex")

if __name__ == '__main__':
    generate_tex()
