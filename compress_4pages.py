import os
import subprocess

def compress_to_4_pages():
    files = ["gen_printable_schedule.py", "gen_dept_schedules.py"]
    for f_name in files:
        with open(f_name, "r", encoding="utf-8") as f:
            content = f.read()

        # 1. Decrease base font size from 11pt to 10pt
        content = content.replace(r"\documentclass[11pt,a4paper]{article}", r"\documentclass[10pt,a4paper]{article}")
        
        # 2. Decrease margins even further
        content = content.replace("margin=1.1cm", "margin=0.8cm")
        content = content.replace("margin=1.8cm", "margin=0.8cm")
        
        # 3. Reduce vertical spacing slightly between sections
        content = content.replace(r"\vspace{10pt}", r"\vspace{4pt}")
        content = content.replace(r"\vspace{14pt}", r"\vspace{6pt}")
        content = content.replace(r"\vspace{16pt}", r"\vspace{6pt}")
        content = content.replace(r"\vspace{8pt}", r"\vspace{4pt}")
        content = content.replace(r"\vspace{6pt}", r"\vspace{3pt}")

        # Reduce table row spacing slightly
        content = content.replace(r"[6pt]", r"[3pt]")
        content = content.replace(r"[5pt]", r"[3pt]")
        content = content.replace(r"[4pt]", r"[2pt]")

        with open(f_name, "w", encoding="utf-8") as f:
            f.write(content)

    print("Tweaked LaTeX generators for 4 pages. Recompiling PDFs...")
    subprocess.run(["python", "gen_printable_schedule.py"])
    subprocess.run(["python", "gen_dept_schedules.py"])
    subprocess.run(["pdflatex", "-interaction=nonstopmode", "AIGGPA_Printable_Schedule.tex"])
    
    # Copy master to downloads
    import shutil
    shutil.copy2("AIGGPA_Printable_Schedule.pdf", r"c:\Users\aryan\Downloads\AIGGPA_Printable_Schedule.pdf")
    
    print("Running pdf2docx conversion...")
    subprocess.run(["python", "convert_pdf2docx.py"])
    print("Done!")

if __name__ == "__main__":
    compress_to_4_pages()
