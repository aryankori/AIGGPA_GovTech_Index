import os
import re
import subprocess

# Set directories
script_dir = os.path.dirname(os.path.abspath(__file__))
workspace_dir = os.path.abspath(os.path.join(script_dir, ".."))
last30_dir = os.path.join(workspace_dir, "last30")
latex_path = os.path.join(workspace_dir, "schedules", "tex", "AIGGPA_Indus_Valley_Report.tex")

print(f"[+] last30 directory: {last30_dir}")
print(f"[+] LaTeX report path: {latex_path}")

# Regex to parse the stats from the last30 files
reddit_re = re.compile(r'Reddit:\s*(\d+)\s*thread')
x_re = re.compile(r'X:\s*(\d+)\s*post')
youtube_re = re.compile(r'YouTube:\s*(\d+)\s*video')
github_re = re.compile(r'GitHub:\s*(\d+)\s*item')
digg_re = re.compile(r'Digg:\s*(\d+)\s*cluster')
jobs_re = re.compile(r'Jobs:\s*(\d+)\s*role')
web_re = re.compile(r'Web:\s*(\d+)\s*page')
voices_re = re.compile(r'Top voices:\s*(.*)')

# 1. Parse all last30 files
parsed_data = []
files = sorted([f for f in os.listdir(last30_dir) if f.endswith(".md")])

for f in files:
    file_path = os.path.join(last30_dir, f)
    with open(file_path, "r", encoding="utf-8") as file_content:
        content = file_content.read()
    
    # Extract keyword name from title line
    title_match = re.search(r'^# last30days v\d+\.\d+\.\d+:\s*(.*)$', content, re.MULTILINE)
    term = title_match.group(1).strip() if title_match else f.replace(".md", "").split("_", 1)[-1].replace("_", " ")
    
    # Extract details
    reddit = reddit_re.search(content)
    x = x_re.search(content)
    youtube = youtube_re.search(content)
    github = github_re.search(content)
    digg = digg_re.search(content)
    jobs = jobs_re.search(content)
    web = web_re.search(content)
    voices = voices_re.search(content)
    
    coverage_parts = []
    if reddit: coverage_parts.append(f"{reddit.group(1)} Reddit threads")
    if x: coverage_parts.append(f"{x.group(1)} X posts")
    if youtube: coverage_parts.append(f"{youtube.group(1)} YouTube videos")
    if github: coverage_parts.append(f"{github.group(1)} GitHub items")
    if digg: coverage_parts.append(f"{digg.group(1)} Digg clusters")
    if jobs: coverage_parts.append(f"{jobs.group(1)} Job postings")
    if web: coverage_parts.append(f"{web.group(1)} Web sources")
    
    coverage = ", ".join(coverage_parts) if coverage_parts else "No direct matches"
    top_voices = voices.group(1).strip() if voices else "N/A"
    
    # Remove directory paths or references from voices to keep it clean
    top_voices = re.sub(r'└─ 📎.*', '', top_voices).strip()
    top_voices = top_voices.replace("_", "\\_").replace("&", "\\&").replace("%", "\\%")
    term = term.replace("_", "\\_").replace("&", "\\&").replace("%", "\\%")
    coverage = coverage.replace("_", "\\_").replace("&", "\\&").replace("%", "\\%")

    parsed_data.append((term, coverage, top_voices))

# 2. Build the LaTeX Appendix content
latex_table_rows = []
for idx, (term, coverage, top_voices) in enumerate(parsed_data, 1):
    latex_table_rows.append(f"{idx} & \\textbf{{{term}}} & {coverage} & {top_voices} \\\\ \\hline")

table_content = "\n".join(latex_table_rows)

appendix_latex = f"""
\\newpage
\\section{{Appendix: last30days Social \\& Web Intel Summary}}
This appendix compiles live and mock social intelligence data collected across Reddit, X, YouTube, GitHub, and the web over the last 30 days for each project-specific keyword:

\\renewcommand{{\\arraystretch}}{{1.25}}
\\begin{{longtable}}{{c p{{5.8cm}} p{{5.5cm}} p{{4.2cm}}}}
\\caption{{\\textbf{{last30days Keyword Index and Social Activity Summary}}}} \\\\
\\toprule
\\rowcolor{{navyblue}}
\\textcolor{{white}}{{\\textbf{{\\#}}}} & \\textcolor{{white}}{{\\textbf{{Keyword}}}} & \\textcolor{{white}}{{\\textbf{{Social/Web Coverage}}}} & \\textcolor{{white}}{{\\textbf{{Top Voices}}}} \\\\
\\midrule
\\endfirsthead
\\multicolumn{{4}}{{c}}{{\\bfseries \\color{{accentteal}} Table \\thetable\\ (Continued)}} \\\\
\\toprule
\\rowcolor{{navyblue}}
\\textcolor{{white}}{{\\textbf{{\\#}}}} & \\textcolor{{white}}{{\\textbf{{Keyword}}}} & \\textcolor{{white}}{{\\textbf{{Social/Web Coverage}}}} & \\textcolor{{white}}{{\\textbf{{Top Voices}}}} \\\\
\\midrule
\\endhead
\\bottomrule
\\endfoot
{table_content}
\\end{{longtable}}
"""

# 3. Read AIGGPA_Indus_Valley_Report.tex
with open(latex_path, "r", encoding="utf-8") as f:
    latex_content = f.read()

# Add \usepackage{longtable} to preamble if not present
if "\\usepackage{longtable}" not in latex_content:
    latex_content = latex_content.replace("\\usepackage{tikz}", "\\usepackage{tikz}\n\\usepackage{longtable}")

# Inject appendix before \end{document}
if "Appendix: last30days" not in latex_content:
    latex_content = latex_content.replace("\\end{document}", appendix_latex + "\n\\end{document}")
else:
    # Overwrite old appendix if running again
    print("[+] Old appendix found. Overwriting...")
    pattern = r"\\newpage\s*\\section\{Appendix: last30days.*?(?=\\end\{document\})"
    latex_content = re.sub(pattern, lambda m: appendix_latex + "\n", latex_content, flags=re.DOTALL)

with open(latex_path, "w", encoding="utf-8") as f:
    f.write(latex_content)

print("[✓] Successfully injected last30days summary table into LaTeX report.")

# 4. Re-compile LaTeX
print("[+] Re-compiling report...")
compile_cmd = ["xelatex", "-interaction=nonstopmode", "AIGGPA_Indus_Valley_Report.tex"]
result = subprocess.run(compile_cmd, cwd=os.path.join(workspace_dir, "schedules", "tex"), capture_output=True, text=True)

if result.returncode == 0:
    print("[✓] Compiled successfully!")
    # Copy compiled PDF to Review folder
    dest_path = os.path.join(workspace_dir, "AIGGPA_Fieldwork_Review", "14_AIGGPA_Indus_Valley_Report.pdf")
    src_path = os.path.join(workspace_dir, "schedules", "tex", "AIGGPA_Indus_Valley_Report.pdf")
    import shutil
    shutil.copy2(src_path, dest_path)
    print(f"[✓] Copied to Review folder: {dest_path}")
else:
    print(f"[!] Compilation failed: {result.stderr}")
    # Print compilation logs
    log_path = os.path.join(workspace_dir, "schedules", "tex", "AIGGPA_Indus_Valley_Report.log")
    if os.path.exists(log_path):
        with open(log_path, "r", encoding="utf-8") as log_file:
            print("--- LOG FILE TAIL ---")
            lines = log_file.readlines()
            for line in lines[-50:]:
                print(line.strip())
