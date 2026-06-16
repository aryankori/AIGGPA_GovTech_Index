"""
Build a Presentation Pitch Guide PDF.
Sections: Timed pitch script, Q&A prep, full glossary.
No em dashes. Simple language. Government employees throughout.
"""
import fitz
import os, textwrap

BASE = os.path.dirname(__file__)
OUT  = os.path.join(BASE, 'Pitch_Guide.pdf')

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
WHITE = (1, 1, 1)

doc = fitz.open()
page_num = [0]

def new_page():
    page_num[0] += 1
    page = doc.new_page(width=W, height=H)
    page.draw_rect(fitz.Rect(28, 28, W-28, H-28), color=BLACK, width=0.5)
    page.insert_text(fitz.Point(W - MR - 100, H - 38),
        f"Pitch Guide  |  Page {page_num[0]}", fontname=HELV, fontsize=7, color=LGRAY)
    return page

def draw_hline(page, y, thick=False):
    page.draw_line(fitz.Point(ML, y), fitz.Point(W - MR, y),
                   color=BLACK, width=1.5 if thick else 0.5)
    return y + 4

def wrap_write(page, y, text, fontsize=9, bold=False, italic=False, indent=0, color=BLACK):
    if bold:
        fn = HELVB
    elif italic:
        fn = HELVI
    else:
        fn = HELV
    chars = int((TW - indent) / (fontsize * 0.52))
    for para in text.split('\n'):
        if para.strip() == '':
            y += fontsize * 0.8
            continue
        for line in textwrap.wrap(para, width=chars):
            if y > H - MB - 20:
                page_num[0] += 1
                page2 = doc.new_page(width=W, height=H)
                page2.draw_rect(fitz.Rect(28, 28, W-28, H-28), color=BLACK, width=0.5)
                page2.insert_text(fitz.Point(W - MR - 100, H - 38),
                    f"Pitch Guide  |  Page {page_num[0]}", fontname=HELV, fontsize=7, color=LGRAY)
                page = page2
                y = MT + 15
            page.insert_text(fitz.Point(ML + indent, y), line, fontname=fn, fontsize=fontsize, color=color)
            y += fontsize * 1.55
    return page, y

def section_title(page, y, text):
    y += 6
    page.insert_text(fitz.Point(ML, y), text.upper(), fontname=HELVB, fontsize=12, color=BLACK)
    y += 6
    y = draw_hline(page, y, thick=True)
    y += 6
    return y

def sub_title(page, y, text, fontsize=10):
    y += 4
    page.insert_text(fitz.Point(ML, y), text, fontname=HELVB, fontsize=fontsize, color=BLACK)
    y += fontsize * 1.4
    return y

# ═══════════════════════════════════════════════════════════
#  COVER
# ═══════════════════════════════════════════════════════════
page = new_page()
page.draw_rect(fitz.Rect(28, 28, W-28, 36), color=BLACK, fill=BLACK)

y = 200
page.insert_text(fitz.Point(ML, y), "Presentation", fontname=HELVB, fontsize=36, color=BLACK)
y += 48
page.insert_text(fitz.Point(ML, y), "Pitch Guide", fontname=HELVB, fontsize=36, color=BLACK)
y += 30
page.draw_line(fitz.Point(ML, y), fitz.Point(ML + 100, y), color=BLACK, width=2)
y += 25
page.insert_text(fitz.Point(ML, y), "Digital Assessment of Government Employees", fontname=HELV, fontsize=10, color=MGRAY)
y += 16
page.insert_text(fitz.Point(ML, y), "5-10 Minute Pitch Script + Q&A Preparation + Full Glossary", fontname=HELV, fontsize=9, color=MGRAY)

y += 50
# Contents box
page.draw_rect(fitz.Rect(ML, y, W - MR, y + 120), color=LGRAY, width=0.5)
y += 18
page.insert_text(fitz.Point(ML + 15, y), "WHAT IS IN THIS DOCUMENT", fontname=HELVB, fontsize=8.5, color=MGRAY)
y += 18
items = [
    "Part 1: Full pitch script with timing for each section (pages 2-5)",
    "Part 2: 15 likely questions with prepared answers (pages 5-8)",
    "Part 3: Complete glossary of every term used (pages 8-10)",
]
for item in items:
    page.insert_text(fitz.Point(ML + 20, y), item, fontname=HELV, fontsize=8.5, color=BLACK)
    y += 16

y = H - 145
page.insert_text(fitz.Point(ML, y), "Investigator: Aryan Kori", fontname=HELV, fontsize=9, color=BLACK)
y += 14
page.insert_text(fitz.Point(ML, y), "AIGGPA, Bhopal", fontname=HELV, fontsize=9, color=MGRAY)
y += 14
page.insert_text(fitz.Point(ML, y), "April 2026", fontname=HELV, fontsize=9, color=MGRAY)

page.draw_rect(fitz.Rect(28, H-36, W-28, H-28), color=BLACK, fill=BLACK)

# ═══════════════════════════════════════════════════════════
#  PART 1: PITCH SCRIPT
# ═══════════════════════════════════════════════════════════
page = new_page()
y = MT + 15

y = section_title(page, y, "Part 1: Pitch Script (5-10 Minutes)")

# Tip box
page.draw_rect(fitz.Rect(ML, y, W - MR, y + 45), color=BLACK, fill=(0.96, 0.96, 0.96))
y += 14
page.insert_text(fitz.Point(ML + 10, y), "TIPS: Speak slowly and clearly. Make eye contact. Refer to your Charts Appendix when", fontname=HELVI, fontsize=8, color=DGRAY)
y += 12
page.insert_text(fitz.Point(ML + 10, y), "mentioning data. Pause after each section to let the audience absorb. Do not rush.", fontname=HELVI, fontsize=8, color=DGRAY)
y += 25

# SECTION 1
y = sub_title(page, y, "SECTION 1: Opening (30 seconds)")
page, y = wrap_write(page, y,
    '"Good morning/afternoon everyone. My name is Aryan Kori and I am working with '
    'AIGGPA, Bhopal. Today I will present my research proposal titled Digital Assessment '
    'of Government Employees."\n\n'
    '"In simple words, I want to find out: do government employees in Madhya Pradesh '
    'actually use the digital tools that the government has given them? And if not, why not?"',
    fontsize=9, italic=True)
y += 8

# SECTION 2
y = sub_title(page, y, "SECTION 2: The Problem (1-2 minutes)")
page, y = wrap_write(page, y,
    '"India has made big progress in digital governance. Under the Digital India programme, '
    'many websites, apps, and systems have been built for government offices. For example, '
    'e-Office, SPARROW, iGOT Karmayogi, and many more."\n\n'
    '"But here is the problem: these tools exist, but many government employees still do not '
    'use them. In many offices I have visited, people still keep paper files, write in registers, '
    'and use WhatsApp to share official documents instead of using the proper government portal."\n\n'
    '"Let me show you some numbers." [Open Charts Appendix]\n\n'
    '"India has moved from rank 118 to rank 97 in the UN E-Government Index over 10 years '
    '(Figure 1). Internet users in India have gone from 30 crore to 95 crore (Figure 2). '
    'At the Central Secretariat in Delhi, 94 percent of files are now digital (Figure 4). '
    'But at the state level, especially in Madhya Pradesh, we do not see this level of '
    'usage. That is the gap I want to study."',
    fontsize=9, italic=True)
y += 8

# SECTION 3
y = sub_title(page, y, "SECTION 3: What I Want To Do (1-2 minutes)")
page, y = wrap_write(page, y,
    '"My research has five main goals:"\n\n'
    '"First, I want to check how much government employees know about the digital tools '
    'available to them."\n\n'
    '"Second, I want to find what stops them from using these tools. Is it old computers? '
    'Lack of training? No internet? Or is it that their seniors do not ask them to use it?"\n\n'
    '"Third, I want to see what role the IT department plays. Do they provide help and '
    'training?"\n\n'
    '"Fourth, I want to check whether government employees who use digital tools feel '
    'that their work has become faster and better."\n\n'
    '"And finally, I will write a report showing the gap between what tools are available '
    'and what is actually being used, with practical suggestions for improvement."',
    fontsize=9, italic=True)
y += 8

# SECTION 4
y = sub_title(page, y, "SECTION 4: How I Will Do It (1-2 minutes)")
page, y = wrap_write(page, y,
    '"I will use a well-known research model called UTAUT." [Show Figure 7]\n\n'
    '"UTAUT stands for Unified Theory of Acceptance and Use of Technology. It was created '
    'by Venkatesh and others in 2003, and it is used worldwide to study why people accept '
    'or reject technology. It looks at four things:"\n\n'
    '"1. Performance Expectancy: Does the government employee think the tool makes '
    'work faster?"\n'
    '"2. Effort Expectancy: Is the tool easy to use, or is paper easier?"\n'
    '"3. Social Influence: Do seniors and coworkers push for digital tool use?"\n'
    '"4. Facilitating Conditions: Is the computer working? Is there internet? Is there '
    'tech support?"\n\n'
    '"For data collection, I will use two methods:"\n'
    '"Secondary data: I will review existing IT records and reports from departments."\n'
    '"Primary data: I will personally interview 45 to 60 government employees and IT '
    'personnel from three departments: School Education, Health, and Forest. I will '
    'also visit offices to check equipment."\n\n'
    '"I will study offices in Bhopal and nearby districts. The study will take 2 to 3 months."',
    fontsize=9, italic=True)
y += 8

# SECTION 5
y = sub_title(page, y, "SECTION 5: Why This Matters (1 minute)")
page, y = wrap_write(page, y,
    '"Let me show you the MP-specific data." [Show Figure 5]\n\n'
    '"In Madhya Pradesh, 9.37 lakh government employees have signed up on iGOT Karmayogi, '
    'and there are 42.79 lakh course enrolments. That is 4.6 courses per person on average. '
    'So they are registering and taking courses. But are they actually using IT tools '
    'in their daily work? That is what we do not know yet."\n\n'
    '"At the central level, file processing layers have dropped from 7.19 to 4.19 '
    '(Figure 6). That means decisions are getting faster because of digital tools. '
    'Can this happen in MP too? My study will find out."',
    fontsize=9, italic=True)
y += 8

# SECTION 6
y = sub_title(page, y, "SECTION 6: Budget and Timeline (30 seconds)")
page, y = wrap_write(page, y,
    '"The total budget is 60,000 rupees. This covers literature review, travel for '
    'interviews, software for analysis, and printing the final report."\n\n'
    '"The project will take 8 weeks: 2 weeks for preparation, 3 weeks for field visits '
    'and interviews, 2 weeks for analysis, and 1 week for the final report."',
    fontsize=9, italic=True)
y += 8

# SECTION 7
y = sub_title(page, y, "SECTION 7: Closing (30 seconds)")
page, y = wrap_write(page, y,
    '"To summarize: the government has built many digital tools, but government employees '
    'are not using them fully. I want to find out why, using a proven research model, '
    'and give practical suggestions that can actually be used to fix the problem."\n\n'
    '"Thank you for your time. I am happy to take any questions."',
    fontsize=9, italic=True)
y += 12

# ═══════════════════════════════════════════════════════════
#  PART 2: Q&A
# ═══════════════════════════════════════════════════════════
y = section_title(page, y, "Part 2: Likely Questions and Answers")

qa_pairs = [
    (
        "Why did you pick this topic?",
        "Because the government has spent a lot of money building digital tools, but we do not "
        "know if government employees are actually using them. Without checking, we cannot "
        "improve. This study will give real answers based on real interviews, not guesswork."
    ),
    (
        "What is UTAUT? Why are you using it?",
        "UTAUT stands for Unified Theory of Acceptance and Use of Technology. It is a research "
        "model created in 2003 by Venkatesh and others. It has been used in over 5000 studies "
        "worldwide. It checks four things: whether the tool is useful, whether it is easy to use, "
        "whether seniors and coworkers support it, and whether the right equipment is available. "
        "I am using it because it is the most accepted model for this type of research."
    ),
    (
        "Why only three departments?",
        "School Education, Health, and Forest are three of the largest departments in the "
        "Government of Madhya Pradesh. Each one has different types of work and different levels "
        "of digital tools. By comparing them, we can see if the problems are the same everywhere "
        "or different in each department."
    ),
    (
        "Is 60 people enough for a study?",
        "Yes. This is a qualitative study, not a survey of thousands. In qualitative research, "
        "45 to 60 in-depth interviews give rich, detailed information. We are not counting numbers. "
        "We are understanding reasons, feelings, and experiences. This is the standard sample size "
        "for this type of research as recommended by Braun and Clarke (2006)."
    ),
    (
        "What if government employees do not give honest answers?",
        "That is a valid concern. To handle this, I will use two methods together. First, I will "
        "interview them. Second, I will personally visit their offices and check the computers, "
        "internet, and systems. This way, I can compare what they say with what I actually see. "
        "This is called triangulation."
    ),
    (
        "What is the expected outcome?",
        "The final output is a report that shows: (1) How much government employees know about "
        "digital tools, (2) How often they use them, (3) What stops them from using them, (4) "
        "What the IT department is doing, and (5) Practical steps to improve usage. This report "
        "can be used by AIGGPA and the state government to plan better training and support."
    ),
    (
        "How is this different from other studies?",
        "Most existing studies look at digital services for citizens, like passport or tax portals. "
        "Very few studies look at how government employees themselves use internal office tools. "
        "This study fills that gap. Also, most studies are about central government offices. This "
        "one focuses on Madhya Pradesh state offices, which have not been studied before."
    ),
    (
        "What is the Digital India programme?",
        "Digital India is a programme launched by the Government of India in 2015 to make "
        "government services available digitally. It includes building internet infrastructure, "
        "creating online portals, and training government employees to use digital tools."
    ),
    (
        "What is e-Office?",
        "e-Office is a software platform created by the National Informatics Centre (NIC). It "
        "allows government offices to handle files, letters, and approvals digitally instead of "
        "using paper. It has been very successful at the Central Secretariat in Delhi where 94 "
        "percent of files are now digital."
    ),
    (
        "What is iGOT Karmayogi?",
        "iGOT Karmayogi is a digital training platform for government employees, launched "
        "under Mission Karmayogi in 2022. It offers online courses on various topics. As of "
        "March 2026, it has 1.53 crore users nationally and 9.37 lakh users in Madhya Pradesh."
    ),
    (
        "What is your budget breakdown?",
        "Total budget is 60,000 rupees. Design and literature review: 32,000. Data collection "
        "and travel: 15,500. Software for analysis: 8,000. Writing and printing: 4,500."
    ),
    (
        "What do you mean by digital gap?",
        "Digital gap means the difference between what digital tools are available and how much "
        "they are actually used. For example, a department may have e-Office installed, but if "
        "government employees still use paper files, that is a digital gap."
    ),
    (
        "How will you analyze the data?",
        "I will use thematic analysis. That means I will read all my interview notes, find "
        "common patterns and group them into themes based on the UTAUT model. For example, "
        "if many people say the internet is slow, that goes under Facilitating Conditions. "
        "If many say their seniors do not encourage digital tools, that goes under Social Influence."
    ),
    (
        "What is qualitative research?",
        "Qualitative research focuses on understanding reasons and experiences through interviews "
        "and observations. It does not use surveys with numbers. Instead, it collects detailed "
        "stories and explanations from participants. It answers the question 'why' rather than "
        "'how many'."
    ),
    (
        "Can this study actually change anything?",
        "Yes. The report will have specific, practical suggestions. For example, if we find that "
        "the main problem is lack of training, we can recommend more training programmes. If the "
        "problem is old computers, we can recommend hardware upgrades. The findings will be "
        "shared with AIGGPA and the departments so they can take real action."
    ),
]

for i, (q, a) in enumerate(qa_pairs, 1):
    y = sub_title(page, y, f"Q{i}: {q}")
    page, y = wrap_write(page, y, a, fontsize=8.5, indent=5)
    y += 10

# ═══════════════════════════════════════════════════════════
#  PART 3: GLOSSARY
# ═══════════════════════════════════════════════════════════
y = section_title(page, y, "Part 3: Complete Glossary")

page, y = wrap_write(page, y,
    "Every technical term used in the proposal and this pitch, explained in plain language.",
    fontsize=8.5, color=MGRAY)
y += 8

glossary = [
    ("AIGGPA", "Atal Bihari Vajpayee Institute of Good Governance and Policy Analysis. A government institute in Bhopal, Madhya Pradesh that works on improving how the government runs."),
    ("Behavioural Intention", "A person's plan or willingness to do something. In this study, it means whether a government employee plans to use a digital tool."),
    ("Braun and Clarke (2006)", "Two researchers who wrote a well-known guide on thematic analysis (a method for analyzing interview data). Their paper is one of the most cited in social science."),
    ("Central Secretariat", "The main office complex of the Government of India in New Delhi where central government ministries work."),
    ("DARPG", "Department of Administrative Reforms and Public Grievances. A central government department that works on making government offices more efficient."),
    ("Data Collection", "The process of gathering information. In this study, it means conducting interviews and visiting offices."),
    ("Digital Gap", "The difference between what digital tools are available and how much they are actually used by government employees."),
    ("Digital India", "A programme launched by the Government of India in 2015 to make government services available online and improve digital infrastructure across the country."),
    ("e-File", "A digital file processed through e-Office software, replacing the traditional paper file system."),
    ("e-Office", "Software built by NIC (National Informatics Centre) for government offices to handle files, letters, and approvals digitally instead of on paper."),
    ("e-Receipt", "A digital receipt processed through e-Office, replacing paper-based receipt tracking."),
    ("EGDI", "E-Government Development Index. A score given by the United Nations to each country, measuring how well they use digital tools for governance. India's rank was 97 out of 193 countries in 2024."),
    ("Effort Expectancy", "One of the four UTAUT factors. It means how easy or hard the government employee thinks the digital tool is to use."),
    ("Facilitating Conditions", "One of the four UTAUT factors. It means whether the necessary support is available: working computer, internet connection, and technical help."),
    ("Field Research", "Research done by going to the actual location (offices in this case), rather than studying from a desk."),
    ("Govt. of MP", "Government of Madhya Pradesh."),
    ("Hypothesis", "An educated guess or prediction about what the study will find. For example: government employees who know about digital tools are more likely to use them."),
    ("ICT", "Information and Communication Technology. A broad term for digital tools, computers, internet, and related systems."),
    ("iGOT Karmayogi", "Integrated Government Online Training platform, launched under Mission Karmayogi in 2022. An online training and learning platform for government employees."),
    ("Methodology", "The plan or process for how the research will be done. It includes what data will be collected, from whom, where, and how it will be analyzed."),
    ("Mission Karmayogi", "A government programme launched in 2020 to improve the skills and capacity of government employees through digital training."),
    ("Moderator", "A factor that can change the strength of a relationship. In UTAUT, age, experience, and designation can change how much the four main factors affect tool usage."),
    ("NIC", "National Informatics Centre. A government organization that builds and manages IT systems for the government."),
    ("Performance Expectancy", "One of the four UTAUT factors. It means whether the government employee believes the digital tool will make their work faster or better."),
    ("PIB", "Press Information Bureau. The official media communication wing of the Government of India."),
    ("Primary Data", "New, original information collected directly by the researcher through interviews and observations."),
    ("Qualitative Research", "A type of research that focuses on understanding reasons, feelings, and experiences through interviews and observation, rather than collecting numbers through surveys."),
    ("Research Objective", "The specific goal or aim of the study. What the researcher is trying to find out."),
    ("Research Question", "A specific question that the study tries to answer. For example: How often do government employees use digital tools?"),
    ("Sample Size", "The number of people who will be interviewed or studied. In this study, it is 45 to 60 government employees."),
    ("Secondary Data", "Information that already exists, collected by someone else. In this study, it means existing IT reports and usage records from departments."),
    ("Social Influence", "One of the four UTAUT factors. It means whether seniors, bosses, or coworkers push or encourage the government employee to use digital tools."),
    ("SPARROW", "Smart Performance Appraisal Report Recording Online Window. An online system for government employee performance reviews."),
    ("Thematic Analysis", "A method of analyzing interview data by reading through notes, finding common patterns, and grouping them into themes or categories."),
    ("TRAI", "Telecom Regulatory Authority of India. The government body that regulates telecom and internet services in India."),
    ("Triangulation", "Using two or more methods to check the same finding. For example, comparing what a government employee says in an interview with what you observe in their office."),
    ("UN DESA", "United Nations Department of Economic and Social Affairs. The UN body that publishes the E-Government Survey every two years."),
    ("UTAUT", "Unified Theory of Acceptance and Use of Technology. A research model created by Venkatesh and others in 2003 that explains why people accept or reject new technology. It has four main factors: Performance Expectancy, Effort Expectancy, Social Influence, and Facilitating Conditions."),
    ("Venkatesh (2003)", "Viswanath Venkatesh, the lead author of the UTAUT model. His 2003 paper in MIS Quarterly has been cited over 50,000 times and is one of the most important papers in IT research."),
]

for term, defn in glossary:
    page.insert_text(fitz.Point(ML, y), term, fontname=HELVB, fontsize=8.5, color=BLACK)
    y += 12
    page, y = wrap_write(page, y, defn, fontsize=8, indent=10, color=DGRAY)
    y += 8
    if y > H - MB - 30:
        # Draw separator
        pass

# Save
doc.save(OUT)
doc.close()
print(f'Done: {OUT}')
print(f'Total pages: {page_num[0]}')
