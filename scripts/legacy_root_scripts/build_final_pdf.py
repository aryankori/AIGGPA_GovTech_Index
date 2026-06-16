"""
Build the final formatted proposal as a PDF.
Black & white minimalist style inspired by the Canva template.
Content: exact words from the approved proposal — NO changes.
"""
import fitz  # PyMuPDF
import os, textwrap

OUT = os.path.join(os.path.dirname(__file__), 'Final_Proposal_Formatted.pdf')
W, H = 595.28, 841.89  # A4

doc = fitz.open()

# ── Fonts ────────────────────────────────────────────────────
TITLE_FONT = "helv"   # Helvetica
BODY_FONT  = "cobo"   # Courier Bold for monospace headers
BODY_REG   = "cour"   # Courier for body (monospace feel)
HELV       = "helv"
HELVB      = "hebo"   # Helvetica Bold
HELVBI     = "hebi"
HELVI      = "heli"

# ── Colors ───────────────────────────────────────────────────
BLACK = fitz.pdfcolor["black"]
GRAY  = (0.4, 0.4, 0.4)
LGRAY = (0.85, 0.85, 0.85)
WHITE = (1, 1, 1)

# ── Margins ──────────────────────────────────────────────────
ML, MR, MT, MB = 60, 60, 60, 60
TW = W - ML - MR  # text width

def new_page():
    page = doc.new_page(width=W, height=H)
    # page border
    r = fitz.Rect(30, 30, W-30, H-30)
    page.draw_rect(r, color=BLACK, width=0.5)
    return page

def add_footer(page, num, total):
    page.insert_text(
        fitz.Point(W - MR - 100, H - 40),
        f"AIGGPA Bhopal  |  Page {num}",
        fontname=HELV, fontsize=7, color=GRAY
    )

def draw_hline(page, y, x1=None, x2=None):
    if x1 is None: x1 = ML
    if x2 is None: x2 = W - MR
    page.draw_line(fitz.Point(x1, y), fitz.Point(x2, y), color=BLACK, width=0.8)
    return y + 4

def section_heading(page, y, text):
    """Bold uppercase heading"""
    y += 8
    page.insert_text(fitz.Point(ML, y), text.upper(), fontname=HELVB, fontsize=12, color=BLACK)
    y += 6
    return y

def sub_heading(page, y, text):
    y += 4
    page.insert_text(fitz.Point(ML, y), text, fontname=HELVB, fontsize=9.5, color=BLACK)
    y += 4
    return y

def body_text(page, y, text, indent=0, fontsize=9, maxlines=100):
    """Insert word-wrapped body text. Returns new y."""
    chars_per_line = int((TW - indent) / (fontsize * 0.52))
    lines = []
    for paragraph in text.split('\n'):
        if paragraph.strip() == '':
            lines.append('')
        else:
            wrapped = textwrap.wrap(paragraph, width=chars_per_line)
            lines.extend(wrapped)
    
    count = 0
    for line in lines:
        if count >= maxlines:
            break
        if line == '':
            y += fontsize * 0.8
            continue
        if y > H - MB - 20:
            break
        page.insert_text(fitz.Point(ML + indent, y), line, fontname=HELV, fontsize=fontsize, color=BLACK)
        y += fontsize * 1.55
        count += 1
    return y

def numbered_item(page, y, num, text, fontsize=9):
    """Numbered list item"""
    chars_per_line = int((TW - 25) / (fontsize * 0.52))
    wrapped = textwrap.wrap(text, width=chars_per_line)
    prefix = f"{num}."
    page.insert_text(fitz.Point(ML + 5, y), prefix, fontname=HELVB, fontsize=fontsize, color=BLACK)
    for i, line in enumerate(wrapped):
        page.insert_text(fitz.Point(ML + 25, y), line, fontname=HELV, fontsize=fontsize, color=BLACK)
        y += fontsize * 1.55
    y += 2
    return y

def bullet_item(page, y, text, fontsize=9):
    chars_per_line = int((TW - 25) / (fontsize * 0.52))
    wrapped = textwrap.wrap(text, width=chars_per_line)
    page.insert_text(fitz.Point(ML + 8, y), "\u00b7", fontname=HELV, fontsize=fontsize, color=BLACK)
    for i, line in enumerate(wrapped):
        page.insert_text(fitz.Point(ML + 25, y), line, fontname=HELV, fontsize=fontsize, color=BLACK)
        y += fontsize * 1.55
    y += 2
    return y

# ═════════════════════════════════════════════════════════════
#  PAGE 1 — COVER
# ═════════════════════════════════════════════════════════════
page = new_page()

# Thick top line
page.draw_rect(fitz.Rect(30, 30, W-30, 38), color=BLACK, fill=BLACK)

# Title
y = 250
page.insert_text(fitz.Point(ML, y), "Digital Assessment", fontname=HELVB, fontsize=36, color=BLACK)
y += 48
page.insert_text(fitz.Point(ML, y), "of Government", fontname=HELVB, fontsize=36, color=BLACK)
y += 48
page.insert_text(fitz.Point(ML, y), "Employees", fontname=HELVB, fontsize=36, color=BLACK)

# Subtitle line
y += 30
page.draw_line(fitz.Point(ML, y), fitz.Point(ML + 120, y), color=BLACK, width=2)

y += 30
page.insert_text(fitz.Point(ML, y), "Research Proposal", fontname=HELV, fontsize=11, color=GRAY)

# Bottom info
y = H - 160
page.insert_text(fitz.Point(ML, y), "Prepared By:", fontname=HELVB, fontsize=8, color=GRAY)
y += 14
page.insert_text(fitz.Point(ML, y), "Aryan Kori", fontname=HELV, fontsize=9, color=BLACK)

y += 22
page.insert_text(fitz.Point(ML, y), "Institution:", fontname=HELVB, fontsize=8, color=GRAY)
y += 14
page.insert_text(fitz.Point(ML, y), "AIGGPA, Bhopal", fontname=HELV, fontsize=9, color=BLACK)

# right side
y2 = H - 160
page.insert_text(fitz.Point(W/2 + 30, y2), "Departments:", fontname=HELVB, fontsize=8, color=GRAY)
y2 += 14
page.insert_text(fitz.Point(W/2 + 30, y2), "School Education, Health, Forest", fontname=HELV, fontsize=9, color=BLACK)
y2 += 12
page.insert_text(fitz.Point(W/2 + 30, y2), "(Govt. of Madhya Pradesh)", fontname=HELV, fontsize=8, color=GRAY)

y2 += 22
page.insert_text(fitz.Point(W/2 + 30, y2), "Date:", fontname=HELVB, fontsize=8, color=GRAY)
y2 += 14
page.insert_text(fitz.Point(W/2 + 30, y2), "April 2026", fontname=HELV, fontsize=9, color=BLACK)

# bottom bar
page.draw_rect(fitz.Rect(30, H-38, W-30, H-30), color=BLACK, fill=BLACK)

add_footer(page, 1, 10)

# ═════════════════════════════════════════════════════════════
#  PAGE 2 — TABLE OF CONTENTS
# ═════════════════════════════════════════════════════════════
page = new_page()
y = MT + 20

y = section_heading(page, y, "Table of Contents")
y += 10
y = draw_hline(page, y)
y += 8

toc_items = [
    ("1.  Introduction and The Digital Gap", "3"),
    ("2.  Research Objectives", "3"),
    ("3.  Hypothesis", "3"),
    ("4.  Research Questions", "4"),
    ("5.  Framework", "4"),
    ("6.  Scope", "5"),
    ("7.  Methodology", "5"),
    ("8.  Timeline", "6"),
    ("9.  Budget", "6"),
    ("10. Expected Contribution", "7"),
    ("11. Limitations", "7"),
    ("12. Acronyms and Key Terms", "7"),
    ("13. References", "8"),
]

for title, pg in toc_items:
    page.insert_text(fitz.Point(ML + 10, y), title, fontname=HELV, fontsize=9, color=BLACK)
    page.insert_text(fitz.Point(W - MR - 15, y), pg, fontname=HELV, fontsize=9, color=GRAY)
    y += 18
    y = draw_hline(page, y)
    y += 6

add_footer(page, 2, 10)

# ═════════════════════════════════════════════════════════════
#  PAGE 3 — Introduction + Objectives + Hypothesis
# ═════════════════════════════════════════════════════════════
page = new_page()
y = MT + 20

y = section_heading(page, y, "1. Introduction and The Digital Gap")
y += 4
y = draw_hline(page, y)
y += 8

intro = (
    "India is moving from paper records to digital systems to improve public offices. "
    "In Madhya Pradesh, departments for education, health, and forests now have websites "
    "and apps for daily tasks. However, many government employees still do not use these tools. "
    "Instead, they use paper books or personal apps like WhatsApp. This study looks at why "
    "this gap exists. Common problems include old computers, lack of training, and old habits. "
    "We will talk to government employees in Bhopal and nearby areas to find the exact physical "
    "and personal issues that slow down digital work."
)
y = body_text(page, y, intro)
y += 8

y = section_heading(page, y, "2. Research Objectives")
y += 4
y = draw_hline(page, y)
y += 8

objectives = [
    "Check how much government employees know about and use digital tools in their daily work.",
    "Identify barriers like bad equipment, lack of training, or office culture.",
    "Review how the IT department helps government employees and tracks tool usage.",
    "See if government employees feel faster and more accurate when using digital tools.",
    "Write a report on the gap between available tools and actual use, with tips for improvement.",
]
for i, obj in enumerate(objectives, 1):
    y = numbered_item(page, y, i, obj)

y += 6

y = section_heading(page, y, "3. Hypothesis")
y += 4
y = draw_hline(page, y)
y += 8

hypotheses = [
    "Government employees who know about digital tools are more likely to use them.",
    "Poor training and old computers are the main reasons government employees avoid digital tools.",
    "Government employees use digital tools more when their seniors tell them to.",
    "Users of digital tools believe they work better than those using paper.",
    "Offices with better IT support have more people using digital tools.",
]
for i, h in enumerate(hypotheses, 1):
    y = numbered_item(page, y, i, h)

add_footer(page, 3, 10)

# ═════════════════════════════════════════════════════════════
#  PAGE 4 — Research Questions + Framework
# ═════════════════════════════════════════════════════════════
page = new_page()
y = MT + 20

y = section_heading(page, y, "4. Research Questions")
y += 4
y = draw_hline(page, y)
y += 8

questions = [
    "What are the main tasks for government employees and what tools do they use?",
    "Do government employees know which IT tools are available to them?",
    "How often do government employees use these tools every day?",
    "What are the reasons for not using the tools?",
    "Is the main issue training, equipment, or lack of orders from seniors?",
    "Has the IT department's help been effective?",
    "What data is tracked regarding tool usage?",
    "Do government employees feel their work improves with these tools?",
    "What specific changes would encourage more digital work?",
]
for i, q in enumerate(questions, 1):
    y = numbered_item(page, y, i, q)

y += 8

y = section_heading(page, y, "5. Framework")
y += 4
y = draw_hline(page, y)
y += 8

framework = (
    "This study uses a standard model called UTAUT to understand why people use technology. "
    "It looks at four areas: if the tool helps work, if it is easy to use, if coworkers use it, "
    "and if the right equipment is available. This model helps us see if problems are personal "
    "or organizational."
)
y = body_text(page, y, framework)
y += 4

flow = "The study follows this flow: Available Tools > Factors Affecting Use > Level of Use > Impact on Work."
y = body_text(page, y, flow)
y += 8

utaut_items = [
    "Expected Benefit: Does the government employee think the tool makes work faster?",
    "Ease of Use: Is the system harder than using paper?",
    "Social Pressure: Do bosses and coworkers encourage usage?",
    "Support: Is there a working computer, internet, and tech help?",
]
for i, item in enumerate(utaut_items, 1):
    y = numbered_item(page, y, i, item)

add_footer(page, 4, 10)

# ═════════════════════════════════════════════════════════════
#  PAGE 5 — Scope + Methodology
# ═════════════════════════════════════════════════════════════
page = new_page()
y = MT + 20

y = section_heading(page, y, "6. Scope")
y += 4
y = draw_hline(page, y)
y += 8

scope_intro = "This study focuses on how government employees in Madhya Pradesh use IT tools for internal work."
y = body_text(page, y, scope_intro)
y += 4

scope_items = [
    "Location: Offices in Bhopal and nearby districts.",
    "Participants: Government employees at all levels and IT personnel.",
    "Focus: Internal office tools only, not public services.",
    "Duration: 2 to 3 months.",
]
for item in scope_items:
    y = bullet_item(page, y, item)

y += 8

y = section_heading(page, y, "7. Methodology")
y += 4
y = draw_hline(page, y)
y += 8

meth_intro = "The study will use two types of data:"
y = body_text(page, y, meth_intro)
y += 4

y = sub_heading(page, y, "Secondary Data")
y += 4
y = body_text(page, y, "Reviewing existing reports and usage records from IT departments.")
y += 6

y = sub_heading(page, y, "Primary Data")
y += 4
y = body_text(page, y, 
    "Interviews with 45 to 60 government employees and IT personnel to understand their daily "
    "challenges. We will also check office equipment in person.")
y += 6

meth_tools = [
    "Interview guides for government employees and IT personnel.",
    "Checklists to record details of computer and internet availability.",
]
for item in meth_tools:
    y = bullet_item(page, y, item)

y += 6
y = body_text(page, y,
    "All interview notes and recordings will be grouped into themes based on the UTAUT model. "
    "This data will be checked against IT records and office observations to ensure accuracy.")

add_footer(page, 5, 10)

# ═════════════════════════════════════════════════════════════
#  PAGE 6 — Timeline + Budget
# ═════════════════════════════════════════════════════════════
page = new_page()
y = MT + 20

y = section_heading(page, y, "8. Timeline")
y += 4
y = draw_hline(page, y)
y += 8

y = body_text(page, y, "The total project will take 8 weeks:")
y += 4

timeline = [
    "Weeks 1-2: Preparation and design.",
    "Weeks 3-5: Visits and interviews.",
    "Weeks 6-7: Analysis of findings.",
    "Week 8: Final report and presentation.",
]
for item in timeline:
    y = bullet_item(page, y, item)

y += 12

y = section_heading(page, y, "9. Budget")
y += 4
y = draw_hline(page, y)
y += 12

# Table header
y = sub_heading(page, y, "PROPOSED BUDGET")
y += 8
page.draw_line(fitz.Point(ML, y), fitz.Point(W-MR, y), color=BLACK, width=1.5)
y += 14

# header row
page.insert_text(fitz.Point(ML + 5, y), "Category", fontname=HELVB, fontsize=8.5, color=BLACK)
page.insert_text(fitz.Point(W - MR - 80, y), "Amount (Rs.)", fontname=HELVB, fontsize=8.5, color=BLACK)
y += 8
page.draw_line(fitz.Point(ML, y), fitz.Point(W-MR, y), color=BLACK, width=0.5)
y += 16

budget = [
    ("Design and Literature Review", "32,000"),
    ("Data Collection and Travel", "15,500"),
    ("Software and Analysis", "8,000"),
    ("Writing and Printing", "4,500"),
]

for cat, amt in budget:
    page.insert_text(fitz.Point(ML + 5, y), cat, fontname=HELV, fontsize=9, color=BLACK)
    page.insert_text(fitz.Point(W - MR - 55, y), amt, fontname=HELV, fontsize=9, color=BLACK)
    y += 8
    page.draw_line(fitz.Point(ML, y), fitz.Point(W-MR, y), color=LGRAY, width=0.3)
    y += 16

# Total row
page.draw_line(fitz.Point(ML, y-6), fitz.Point(W-MR, y-6), color=BLACK, width=1)
y += 4
page.insert_text(fitz.Point(ML + 5, y), "TOTAL", fontname=HELVB, fontsize=9.5, color=BLACK)
page.insert_text(fitz.Point(W - MR - 55, y), "60,000", fontname=HELVB, fontsize=9.5, color=BLACK)
y += 8
page.draw_line(fitz.Point(ML, y), fitz.Point(W-MR, y), color=BLACK, width=1)

add_footer(page, 6, 10)

# ═════════════════════════════════════════════════════════════
#  PAGE 7 — Expected Contribution + Limitations + Acronyms
# ═════════════════════════════════════════════════════════════
page = new_page()
y = MT + 20

y = section_heading(page, y, "10. Expected Contribution")
y += 4
y = draw_hline(page, y)
y += 8

y = body_text(page, y,
    "This study will show the real gap between available IT tools and actual use. "
    "It will identify specific problems and suggest practical steps to help government employees "
    "work digitally. The findings will help other offices improve their efficiency.")

y += 10

y = section_heading(page, y, "11. Limitations")
y += 4
y = draw_hline(page, y)
y += 8

y = body_text(page, y,
    "The study is limited to Bhopal and nearby areas. With a sample of 60 people, it gives "
    "a good overview of challenges but may not represent every office in the state. We rely on "
    "honest answers from government employees, but in-person checks will help confirm the details.")

y += 10

y = section_heading(page, y, "12. Acronyms and Key Terms")
y += 4
y = draw_hline(page, y)
y += 8

acronyms = [
    "AIGGPA: Atal Bihari Vajpayee Institute of Good Governance and Policy Analysis.",
    "Govt. of MP: Government of Madhya Pradesh.",
    "UTAUT (Unified Theory of Acceptance and Use of Technology): A standard research model used to understand why people choose to use new technologies, by looking at factors like how helpful or easy the tool is.",
    "Digital Gap: The difference between available digital tools (like websites and apps) and their actual use by employees.",
    "Primary Data: New information gathered directly from interviews and observations during this study.",
    "Secondary Data: Existing information and usage records reviewed from IT departments.",
    "Thematic analysis: A method for grouping interview notes and findings into themes to make sense of the results.",
]
for item in acronyms:
    y = bullet_item(page, y, item)

add_footer(page, 7, 10)

# ═════════════════════════════════════════════════════════════
#  PAGE 8 — References
# ═════════════════════════════════════════════════════════════
page = new_page()
y = MT + 20

y = section_heading(page, y, "13. References")
y += 4
y = draw_hline(page, y)
y += 10

refs = [
    'Alrawabdeh, W. (2014). Examining factors affecting digital platform adoption in Jordan. International Journal of Business and Social Science, 5(8), 232-241.',
    'Bhatnagar, S. (2004). E-Government: From Vision to Implementation - A Practical Guide with Case Studies. Sage Publications.',
    'Braun, V., & Clarke, V. (2006). Using thematic analysis in psychology. Qualitative Research in Psychology, 3(2), 77-101.',
    'Cordella, A., & Bonina, C. M. (2012). A public value perspective for ICT enabled public sector reforms. Government Information Quarterly, 29(4), 512-520.',
    'Davis, F. D. (1989). Perceived usefulness, perceived ease of use, and user acceptance of information technology. MIS Quarterly, 13(3), 319-340.',
    'Government of India, Department of Personnel & Training. (2020). National Programme for Civil Services Capacity Building (Mission Karmayogi).',
    'Government of India, Ministry of Electronics & Information Technology. (2015). Digital India. https://digitalindia.gov.in/',
    'Heeks, R. (2003). Most eGovernment-for-Development Projects Fail: How Can Risks Be Reduced? University of Manchester.',
    'Heeks, R. (2006). Implementing and Managing eGovernment. Sage Publications.',
    'Kumar, R., & Best, M. L. (2006). Impact and sustainability of e-government services in developing countries. The Information Society, 22(1), 1-12.',
    'Ndou, V. (2004). E-government for developing countries. The Electronic Journal of Information Systems in Developing Countries, 18(1), 1-24.',
    'OECD. (2014). Recommendation of the Council on Digital Government Strategies.',
    'United Nations. (2022). E-Government Survey 2022: The Future of Digital Government.',
    'United States GAO. (2019). Agencies Need to Develop Modernization Plans for Critical Legacy Systems (GAO-19-471).',
    'Venkatesh, V., Morris, M. G., Davis, G. B., & Davis, F. D. (2003). User acceptance of information technology: Toward a unified view. MIS Quarterly, 27(3), 425-478.',
    'Venkatesh, V., Thong, J. Y. L., & Xu, X. (2012). Consumer acceptance and use of information technology. MIS Quarterly, 36(1), 157-178.',
    'World Bank. (2016). World Development Report 2016: Digital Dividends.',
]

for ref in refs:
    if y > H - MB - 40:
        add_footer(page, 8, 10)
        page = new_page()
        y = MT + 30
        y = section_heading(page, y, "References (continued)")
        y += 4
        y = draw_hline(page, y)
        y += 10
    
    chars_per_line = int(TW / (8 * 0.52))
    wrapped = textwrap.wrap(ref, width=chars_per_line)
    for i, line in enumerate(wrapped):
        indent = 15 if i > 0 else 0
        page.insert_text(fitz.Point(ML + indent, y), line, fontname=HELV, fontsize=8, color=BLACK)
        y += 11
    y += 6

add_footer(page, 8, 10)

# ═════════════════════════════════════════════════════════════
#  SAVE
# ═════════════════════════════════════════════════════════════
doc.save(OUT)
doc.close()
print(f'✅ Final formatted proposal saved to:\n   {OUT}')
