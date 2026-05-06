import os
import subprocess

def tweak_files():
    files = ["gen_printable_schedule.py", "gen_dept_schedules.py"]
    for f_name in files:
        with open(f_name, "r", encoding="utf-8") as f:
            content = f.read()

        # 1. Decrease margins to save space (compresses into 4 pages)
        content = content.replace("margin=1.8cm", "margin=1.1cm")
        
        # 2. Make checkboxes significantly larger
        content = content.replace(r"$\square$", r"{\Large$\square$}")
        
        # 3. Make blank lines longer
        content = content.replace(r"\newcommand{\blank}{\rule{5cm}{0.4pt}}", r"\newcommand{\blank}{\rule{8cm}{0.4pt}}")
        
        # 4. Add more space for write-in questions
        # Find occurrences of \rule{\linewidth}{0.4pt} and double them up to give two lines to write on
        content = content.replace(r"Why? & \rule{\linewidth}{0.4pt} \\", r"Why? & \rule{\linewidth}{0.4pt}\\[6pt] & \rule{\linewidth}{0.4pt} \\")
        content = content.replace(r"If yes, which? & \rule{\linewidth}{0.4pt} \\", r"If yes, which? & \rule{\linewidth}{0.4pt}\\[6pt] & \rule{\linewidth}{0.4pt} \\")
        content = content.replace(r"Topics needing more training: & \rule{\linewidth}{0.4pt} \\", r"Topics needing more training: & \rule{\linewidth}{0.4pt}\\[6pt] & \rule{\linewidth}{0.4pt} \\")
        
        # For Q38 open ended, add one more line
        content = content.replace(r"\noindent\rule{\textwidth}{0.4pt}\vspace{6pt}", r"\noindent\rule{\textwidth}{0.4pt}\vspace{8pt}\n\noindent\rule{\textwidth}{0.4pt}\vspace{6pt}")

        with open(f_name, "w", encoding="utf-8") as f:
            f.write(content)

    print("Tweaked LaTeX generators. Recompiling PDFs...")
    subprocess.run(["python", "gen_printable_schedule.py"])
    subprocess.run(["python", "gen_dept_schedules.py"])
    subprocess.run(["pdflatex", "-interaction=nonstopmode", "AIGGPA_Printable_Schedule.tex"])
    
    # Copy master to downloads
    import shutil
    shutil.copy2("AIGGPA_Printable_Schedule.pdf", r"c:\Users\aryan\Downloads\AIGGPA_Printable_Schedule.pdf")
    
    print("PDFs recompiled. Running pdf2docx conversion...")
    
    # Run the pdf2docx script to regenerate the DOCX files based on the newly tweaked PDFs
    subprocess.run(["python", "convert_pdf2docx.py"])
    print("Done!")

if __name__ == "__main__":
    tweak_files()
