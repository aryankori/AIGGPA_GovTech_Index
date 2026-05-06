"""
Builds a Methodology and Scope Options PDF.
Provides Level 1 (Simple), Level 2 (Moderate), and Level 3 (Complex) options
for data collection, sampling, and sorting/analysis algorithms.
No em dashes, 'government employees' used throughout.
"""
import fitz
import os, textwrap

BASE = os.path.dirname(__file__)
OUT  = os.path.join(BASE, 'Methodology_Scope_Options.pdf')

W, H = 595.28, 841.89
ML, MR, MT, MB = 55, 55, 55, 55
TW = W - ML - MR

HELV  = "helv"
HELVB = "hebo"
HELVI = "helv"
BLACK = (0, 0, 0)
DGRAY = (0.25, 0.25, 0.25)
MGRAY = (0.44, 0.44, 0.44)
LGRAY = (0.7, 0.7, 0.7)

doc = fitz.open()

def new_page():
    page = doc.new_page(width=W, height=H)
    page.draw_rect(fitz.Rect(28, 28, W-28, H-28), color=BLACK, width=0.5)
    return page

def add_footer(page, num):
    page.insert_text(fitz.Point(W - MR - 100, H - 38),
        f"AIGGPA Bhopal  |  Page {num}", fontname=HELV, fontsize=7, color=LGRAY)

def wrap_write(page, y, text, fontsize=9.5, bold=False, color=BLACK, indent=0):
    fn = HELVB if bold else HELV
    chars = int((TW - indent) / (fontsize * 0.52))
    for para in text.split('\n'):
        if para.strip() == '':
            y += fontsize * 0.8
            continue
        for line in textwrap.wrap(para, width=chars):
            if y > H - MB - 20:
                break
            page.insert_text(fitz.Point(ML + indent, y), line, fontname=fn, fontsize=fontsize, color=color)
            y += fontsize * 1.55
    return y

def draw_hline(page, y):
    page.draw_line(fitz.Point(ML, y), fitz.Point(W - MR, y), color=BLACK, width=1.0)
    return y + 6

# ═══════════════════════════════════════════════════════════
#  PAGE 1: Cover & Intro
# ═══════════════════════════════════════════════════════════
page = new_page()
page.draw_rect(fitz.Rect(28, 28, W-28, 36), color=BLACK, fill=BLACK)

y = 120
page.insert_text(fitz.Point(ML, y), "Scope and Methodology", fontname=HELVB, fontsize=32, color=BLACK)
y += 38
page.insert_text(fitz.Point(ML, y), "Options Proposal", fontname=HELVB, fontsize=32, color=BLACK)
y += 20
page.draw_line(fitz.Point(ML, y), fitz.Point(ML + 120, y), color=BLACK, width=2)
y += 25
page.insert_text(fitz.Point(ML, y), "Digital Assessment of Government Employees", fontname=HELV, fontsize=11, color=MGRAY)

y += 50
y = wrap_write(page, y, "PURPOSE OF THIS DOCUMENT", fontsize=10, bold=True, color=MGRAY)
intro = (
    "This document outlines three different levels of scope for the research project, ranging "
    "from a simple, fast approach to a highly complex, algorithmic approach. It details the "
    "Tools, Processes, Data Collection Methods, Sampling Techniques, and Sorting/Analysis "
    "Algorithms for each level.\n\n"
    "This will help management decide the final commitment level, required resources, "
    "and timeline for the study."
)
y = wrap_write(page, y, intro, fontsize=9.5)
y += 20

# LEVEL 1 Box
page.draw_rect(fitz.Rect(ML, y, W-MR, y+45), color=LGRAY, fill=(0.96, 0.96, 0.96))
y += 18
page.insert_text(fitz.Point(ML+15, y), "OPTION 1: BASIC SCOPE (Qualitative Focus)", fontname=HELVB, fontsize=11, color=BLACK)
y += 14
page.insert_text(fitz.Point(ML+15, y), "Fast, low cost, interview-based. (Current Proposal Level)", fontname=HELV, fontsize=9, color=DGRAY)
y += 35

# LEVEL 2 Box
page.draw_rect(fitz.Rect(ML, y, W-MR, y+45), color=LGRAY, fill=(0.96, 0.96, 0.96))
y += 18
page.insert_text(fitz.Point(ML+15, y), "OPTION 2: MODERATE SCOPE (Quantitative Focus)", fontname=HELVB, fontsize=11, color=BLACK)
y += 14
page.insert_text(fitz.Point(ML+15, y), "Survey-based, statistically significant, uses basic algorithms.", fontname=HELV, fontsize=9, color=DGRAY)
y += 35

# LEVEL 3 Box
page.draw_rect(fitz.Rect(ML, y, W-MR, y+45), color=LGRAY, fill=(0.96, 0.96, 0.96))
y += 18
page.insert_text(fitz.Point(ML+15, y), "OPTION 3: COMPLEX SCOPE (Mixed-Methods + ML)", fontname=HELVB, fontsize=11, color=BLACK)
y += 14
page.insert_text(fitz.Point(ML+15, y), "Massive scale, uses Structural Equation Modeling and Clustering.", fontname=HELV, fontsize=9, color=DGRAY)

add_footer(page, 1)

# ═══════════════════════════════════════════════════════════
#  PAGE 2: LEVEL 1 (BASIC)
# ═══════════════════════════════════════════════════════════
page = new_page()
y = MT + 20

page.insert_text(fitz.Point(ML, y), "OPTION 1: BASIC SCOPE", fontname=HELVB, fontsize=14, color=BLACK)
y += 10
y = draw_hline(page, y)

opts1 = [
    ("Summary", "This is the simplest approach. It focuses on talking to a small group of people to understand their problems deeply, rather than collecting numbers. This is the baseline proposed earlier."),
    ("Sampling Method", "Purposive & Convenience Sampling. We carefully select 45 to 60 government employees who represent different roles (clerks, managers, IT staff) in Bhopal. We do not use randomized formulas."),
    ("Collection Tools", "In-person, one-on-one structured interviews (30 minutes each). Notes and audio recordings are collected. A checklist is used to observe their physical workspace (computer condition)."),
    ("Sorting & Analysis Algorithm", "Thematic Analysis (Manual Coding). Data is transcribed into Excel/Word. We manually read the answers and sort them into four \"buckets\" or themes based on the UTAUT model (e.g., all answers about bad internet go into the 'Facilitating Conditions' bucket)."),
    ("Time & Commitment", "8 Weeks. Low software cost. Requires 1 researcher visiting offices heavily for 3 weeks."),
    ("Pros", "Very fast. Gives real, human stories and specific software complaints. Very low cost."),
    ("Cons", "Sample size is too small to say 'X percent of the whole state feels this way'. It is an exploratory study.")
]

for title, text in opts1:
    y = wrap_write(page, y, title.upper(), bold=True, fontsize=9)
    y = wrap_write(page, y, text, fontsize=9, color=DGRAY)
    y += 10

add_footer(page, 2)

# ═══════════════════════════════════════════════════════════
#  PAGE 3: LEVEL 2 (MODERATE)
# ═══════════════════════════════════════════════════════════
page = new_page()
y = MT + 20

page.insert_text(fitz.Point(ML, y), "OPTION 2: MODERATE SCOPE", fontname=HELVB, fontsize=14, color=BLACK)
y += 10
y = draw_hline(page, y)

opts2 = [
    ("Summary", "This approach uses numbers to prove a point. We ask hundreds of government employees to rate their digital experience on a 1 to 5 scale. This allows us to create graphs and calculate averages."),
    ("Sampling Method", "Stratified Random Sampling. We take the total population of government employees in 3 departments, divide them into groups (strata) based on their rank (e.g., senior, mid-level, junior), and randomly select 300 to 400 people across Bhopal and 2 other cities."),
    ("Collection Tools", "Online Likert-Scale Surveys (Google Forms or Qualtrics) sent via official email or WhatsApp groups. Paper surveys act as backups for those without internet. The survey asks them to agree/disagree with 20 statements."),
    ("Sorting & Analysis Algorithm", "Descriptive Statistics (SPSS or Python Pandas/SciPy). We use sorting algorithms to group data by age, department, and rank. We use algorithms like T-tests and ANOVA to check if there is a real mathematical difference between how young vs. older employees use tools."),
    ("Time & Commitment", "12 to 14 Weeks. Requires management to push out the survey link to hundreds of people. Requires basic statistical software licenses."),
    ("Pros", "Statistically significant. We can confidently say '75 percent of mid-level employees blame poor training'. Forms solid graphs."),
    ("Cons", "Surveys are dry. A person might answer '3 out of 5', but we will not know exactly 'why' they gave that score.")
]

for title, text in opts2:
    y = wrap_write(page, y, title.upper(), bold=True, fontsize=9)
    y = wrap_write(page, y, text, fontsize=9, color=DGRAY)
    y += 10

add_footer(page, 3)

# ═══════════════════════════════════════════════════════════
#  PAGE 4: LEVEL 3 (COMPLEX)
# ═══════════════════════════════════════════════════════════
page = new_page()
y = MT + 20

page.insert_text(fitz.Point(ML, y), "OPTION 3: COMPLEX SCOPE", fontname=HELVB, fontsize=14, color=BLACK)
y += 10
y = draw_hline(page, y)

opts3 = [
    ("Summary", "A state-wide, massive study using both massive surveys and direct IT server data. This creates an Academic-grade structural model that proves exactly which factor (e.g., training vs. hardware) causes usage to drop."),
    ("Sampling Method", "Multi-stage Cluster Sampling. We divide the entire state of Madhya Pradesh into zones, randomly pick districts from each zone, and survey over 1000+ government employees. We combine this with Focus Group Discussions (10 people in a room) to understand the data deeply."),
    ("Collection Tools", "Digital surveys, Focus Group recordings, PLUS secondary IT Server Logs (e.g., extracting login frequencies directly from the NIC/e-Office servers to see real usage, rather than relying on what people tell us)."),
    ("Sorting & Mathematical Algorithms", "1. Structural Equation Modeling (SEM) using SmartPLS software. This complex algorithm proves casualty. It maps exactly how much Social Pressure impacts Intention to Use.\n2. K-Means Clustering (Machine Learning): A Python-based sorting algorithm that groups the 1000+ employees into automated 'User Personas' (e.g., 'The Resistant Veteran', 'The Eager Beginner') based on their data patterns."),
    ("Time & Commitment", "5 to 6 Months. High cost. Requires high-level permissions to access IT login data. Requires an expert data analyst on the team."),
    ("Pros", "Absolute highest standard. Unbeatable evidence. Very impressive to senior leadership and policy makers."),
    ("Cons", "Very expensive. Requires massive coordination. If IT server data is denied due to privacy, the model breaks.")
]

for title, text in opts3:
    y = wrap_write(page, y, title.upper(), bold=True, fontsize=9)
    if '\n' in text:
        y -= 2
        for line in text.split('\n'):
            y = wrap_write(page, y, line, fontsize=9, color=DGRAY)
    else:
        y = wrap_write(page, y, text, fontsize=9, color=DGRAY)
    y += 10

add_footer(page, 4)

# ═══════════════════════════════════════════════════════════
#  PAGE 5: Comparison Summary
# ═══════════════════════════════════════════════════════════
page = new_page()
y = MT + 20

page.insert_text(fitz.Point(ML, y), "EXECUTIVE SUMMARY FOR APPROVAL", fontname=HELVB, fontsize=14, color=BLACK)
y += 10
y = draw_hline(page, y)

y = wrap_write(page, y, "Recommendation for the Manager:", fontsize=10, bold=True, color=BLACK)
y += 4
rec = (
    "For an 8-week internship or short-term project, OPTION 1 (Basic Scope) is the most "
    "realistic. It allows you to gather meaningful data quickly without requiring complex "
    "permissions or software. It is also what the current proposal is built around.\n\n"
    "If the department can securely send out an email to thousands of employees and you have "
    "an extra month, OPTION 2 (Moderate Scope) provides better visual graphs and stronger evidence.\n\n"
    "OPTION 3 is typically reserved for year-long government funded research projects or PhD theses."
)
y = wrap_write(page, y, rec, fontsize=9.5, color=DGRAY)
y += 20

# Table
col_x = [ML, ML + 110, ML + 220, ML + 330]
headers = ["Metric", "Option 1: Basic", "Option 2: Moderate", "Option 3: Complex"]

page.draw_rect(fitz.Rect(ML, y, W-MR, y+16), color=BLACK, fill=BLACK)
for i in range(4):
    page.insert_text(fitz.Point(col_x[i] + 5, y + 12), headers[i], fontname=HELVB, fontsize=8.5, color=(1,1,1))
y += 16

rows = [
    ("Primary Method", "Interviews", "Online Surveys", "Mixed + Server Logs"),
    ("Target Audience", "45 to 60", "300 to 400", "1000+ employees"),
    ("Algorithms Used", "Thematic Coding", "SPSS / T-Tests", "SEM & ML Clustering"),
    ("Sampling Type", "Convenience", "Stratified Random", "Multi-stage Cluster"),
    ("Timeline", "8 Weeks", "12-14 Weeks", "5-6 Months"),
    ("Cost & Access", "Very Low", "Medium", "Very High")
]

for row in rows:
    for i in range(4):
        fn = HELVB if i == 0 else HELV
        page.insert_text(fitz.Point(col_x[i] + 5, y + 14), row[i], fontname=fn, fontsize=8.5, color=BLACK)
    y += 22
    page.draw_line(fitz.Point(ML, y), fitz.Point(W-MR, y), color=LGRAY, width=0.5)

add_footer(page, 5)

doc.save(OUT)
doc.close()
print(f'Done: {OUT}')
