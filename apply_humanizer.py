import os
import subprocess

def humanize_and_remove_cadre():
    # 1. Update gen_printable_schedule.py
    f1 = "gen_printable_schedule.py"
    with open(f1, "r", encoding="utf-8") as f:
        content1 = f.read()
    
    # Remove Q2 Cadre
    content1 = content1.replace(
        r"Q2 & Cadre: & $\square$ Class I\quad$\square$ Class II\quad$\square$ Class III\quad$\square$ Class IV \\[6pt]",
        r"Q2 & Job Role / Level: & \blank \\[6pt]"
    )
    # Rename Section N
    content1 = content1.replace(
        r"\noindent{\large\bfseries Section N: Cadre-Specific Questions (All Departments)}\vspace{6pt}",
        r"\noindent{\large\bfseries Section N: Role-Specific Questions}\vspace{6pt}"
    )
    # Humanize questions
    content1 = content1.replace("YOUR cadre level?", "your specific job role?")
    content1 = content1.replace("differ by cadre level?", "differ based on job level?")
    content1 = content1.replace("8 (cadre)", "8 (role-specific)")
    content1 = content1.replace("CADRE-SPECIFIC (ALL DEPTS)", "ROLE-SPECIFIC QUESTIONS")

    with open(f1, "w", encoding="utf-8") as f:
        f.write(content1)
        
    # 2. Update gen_dept_schedules.py
    f2 = "gen_dept_schedules.py"
    with open(f2, "r", encoding="utf-8") as f:
        content2 = f.read()

    # Remove Cadre Reference Table from cover
    cover_old = r"""\noindent\textbf{Cadre Reference --- Who Does What:}
\vspace{2pt}

{\small
\noindent\begin{tabularx}{\textwidth}{@{}L{1cm} L{3.8cm} L{4.5cm} X@{}}
\textbf{Class} & \textbf{Officers / Posts} & \textbf{Core Work} & \textbf{Digital Role} \\
\hline
""" + '""" + cadre_rows + r"""' + r"""\end{tabularx}
}"""
    
    content2 = content2.replace(cover_old, "")
    
    # Remove Q2 Cadre
    content2 = content2.replace(
        r"Q2 & Cadre: & $\square$ Class I\quad$\square$ Class II\quad$\square$ Class III\quad$\square$ Class IV \\[5pt]",
        r"Q2 & Job Role / Level: & \blank \\[5pt]"
    )
    
    # Rename Section J
    content2 = content2.replace(
        r"\noindent{\large\bfseries Section J: Cadre-Specific (All Departments)}\vspace{4pt}",
        r"\noindent{\large\bfseries Section J: Role-Specific Questions}\vspace{4pt}"
    )
    
    # Humanize questions
    content2 = content2.replace("YOUR cadre level?", "your specific job role?")
    content2 = content2.replace("differ by cadre level?", "differ based on your job level?")
    content2 = content2.replace("8 (cadre)", "8 (role)")
    
    with open(f2, "w", encoding="utf-8") as f:
        f.write(content2)

    print("Scripts updated. Now regenerating PDFs...")
    
    subprocess.run(["python", "gen_printable_schedule.py"], check=True)
    subprocess.run(["python", "gen_dept_schedules.py"], check=True)
    
    subprocess.run(["pdflatex", "AIGGPA_Printable_Schedule.tex"], check=True)
    subprocess.run(["powershell", "-Command", r'Copy-Item AIGGPA_Printable_Schedule.pdf "C:\Users\aryan\Downloads" -Force'])
    
    print("All PDFs successfully rebuilt and humanized!")

if __name__ == "__main__":
    humanize_and_remove_cadre()
