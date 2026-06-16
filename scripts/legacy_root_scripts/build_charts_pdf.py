"""
Build a standalone Charts & Data Appendix PDF.
Each figure gets its own page with the chart image + a plain-English explanation.
No em dashes. Simple language. All data sourced.
"""
import fitz
import os, textwrap

BASE = os.path.dirname(__file__)
GFX  = os.path.join(BASE, 'Proposal_Graphics')
OUT  = os.path.join(BASE, 'Charts_Data_Appendix.pdf')

W, H = 595.28, 841.89  # A4
ML, MR, MT, MB = 55, 55, 55, 55
TW = W - ML - MR

HELV  = "helv"
HELVB = "hebo"
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
    page.insert_text(fitz.Point(W - MR - 130, H - 38),
        f"Charts & Data Appendix  |  Page {num}", fontname=HELV, fontsize=7, color=LGRAY)

def wrap_text(page, y, text, fontsize=9, indent=0, bold=False):
    fn = HELVB if bold else HELV
    chars = int((TW - indent) / (fontsize * 0.52))
    for para in text.split('\n'):
        if para.strip() == '':
            y += fontsize * 0.8
            continue
        for line in textwrap.wrap(para, width=chars):
            if y > H - MB - 20:
                break
            page.insert_text(fitz.Point(ML + indent, y), line, fontname=fn, fontsize=fontsize, color=BLACK)
            y += fontsize * 1.55
    return y

# ═════════════════════════════════════════════════════════════
#  COVER PAGE
# ═════════════════════════════════════════════════════════════
page = new_page()
page.draw_rect(fitz.Rect(28, 28, W-28, 36), color=BLACK, fill=BLACK)

y = 220
page.insert_text(fitz.Point(ML, y), "Charts & Data", fontname=HELVB, fontsize=34, color=BLACK)
y += 46
page.insert_text(fitz.Point(ML, y), "Appendix", fontname=HELVB, fontsize=34, color=BLACK)
y += 30
page.draw_line(fitz.Point(ML, y), fitz.Point(ML + 100, y), color=BLACK, width=2)
y += 25
page.insert_text(fitz.Point(ML, y), "Supporting Figures for the Research Proposal", fontname=HELV, fontsize=10, color=MGRAY)
y += 18
page.insert_text(fitz.Point(ML, y), "Digital Assessment of Government Employees", fontname=HELV, fontsize=10, color=MGRAY)

y = H - 155
page.insert_text(fitz.Point(ML, y), "Investigator: Aryan Kori", fontname=HELV, fontsize=9, color=BLACK)
y += 14
page.insert_text(fitz.Point(ML, y), "AIGGPA, Bhopal", fontname=HELV, fontsize=9, color=MGRAY)
y += 14
page.insert_text(fitz.Point(ML, y), "April 2026", fontname=HELV, fontsize=9, color=MGRAY)

y2 = H - 155
page.insert_text(fitz.Point(W/2 + 20, y2), "All data in this document is sourced from:", fontname=HELVB, fontsize=7.5, color=MGRAY)
y2 += 13
sources = [
    "UN DESA E-Government Survey",
    "TRAI Annual Performance Indicators",
    "Press Information Bureau (PIB)",
    "DARPG Secretariat Reforms Reports",
    "Venkatesh et al. (2003), MIS Quarterly",
]
for s in sources:
    page.insert_text(fitz.Point(W/2 + 25, y2), "- " + s, fontname=HELV, fontsize=7, color=MGRAY)
    y2 += 10

page.draw_rect(fitz.Rect(28, H-36, W-28, H-28), color=BLACK, fill=BLACK)
add_footer(page, 1)

# ═════════════════════════════════════════════════════════════
#  FIGURE PAGES
# ═════════════════════════════════════════════════════════════
figures = [
    {
        'file': 'fig1_un_egdi_ranking.png',
        'label': 'FIGURE 1',
        'title': "India's UN E-Government Ranking (2014 to 2024)",
        'explanation': (
            "This chart shows how India's rank has changed in the United Nations "
            "E-Government Development Index (EGDI) over ten years. The UN checks 193 "
            "countries every two years.\n\n"
            "India moved from rank 118 in 2014 to rank 97 in 2024. That is an improvement "
            "of 21 places. The best year was 2018 (rank 96). After that, India dropped to "
            "100 in 2020 and 105 in 2022, but came back to 97 in 2024.\n\n"
            "WHY IT MATTERS: This shows India is making progress but still not in the "
            "top 50. Many digital tools exist but are not fully used. This study will help "
            "find out why government employees do not use them."
        ),
        'source': 'Source: UN DESA, E-Government Survey 2014, 2016, 2018, 2020, 2022, 2024',
        'data_table': [
            ('Year', 'Rank'),
            ('2014', '118'),
            ('2016', '107'),
            ('2018', '96'),
            ('2020', '100'),
            ('2022', '105'),
            ('2024', '97'),
        ]
    },
    {
        'file': 'fig2_internet_subscribers.png',
        'label': 'FIGURE 2',
        'title': 'India: Total Internet Subscribers (2015 to 2024)',
        'explanation': (
            "This bar chart shows the total number of internet subscribers in India from "
            "2015 to 2024, as reported by TRAI (Telecom Regulatory Authority of India).\n\n"
            "The number grew from 30.2 crore in 2015 to 95.4 crore in 2024. That is a "
            "growth of more than 3 times (216 percent) in nine years. In November 2025, "
            "broadband users alone crossed 100 crore.\n\n"
            "WHY IT MATTERS: Internet is now available to most people in India. But having "
            "internet does not mean government employees use office tools. This study checks "
            "whether the problem is access to internet or something else."
        ),
        'source': 'Source: TRAI, Annual Performance Indicators (as of March each year)',
        'data_table': [
            ('Year', 'Subscribers (Crore)'),
            ('2015', '30.2'),
            ('2016', '34.3'),
            ('2017', '39.2'),
            ('2018', '49.4'),
            ('2019', '63.7'),
            ('2020', '74.3'),
            ('2021', '82.5'),
            ('2022', '83.4'),
            ('2023', '88.1'),
            ('2024', '95.4'),
        ]
    },
    {
        'file': 'fig3_igot_national.png',
        'label': 'FIGURE 3',
        'title': 'iGOT Karmayogi: National User Growth',
        'explanation': (
            "This line chart shows how many government employees signed up on the iGOT "
            "Karmayogi platform (Mission Karmayogi) at the national level.\n\n"
            "In January 2023, only 3 lakh users were registered. By March 2026, this grew "
            "to 1.53 crore. That is about 50 times more users in just 38 months.\n\n"
            "WHY IT MATTERS: The government is pushing digital training hard. But "
            "registering on a platform is not the same as actually using the tools daily. "
            "This study checks the gap between sign-up and real usage."
        ),
        'source': 'Source: PIB releases - Jan 2023, May 2025, Jul 2025, Dec 2025, Feb 2026, Mar 2026',
        'data_table': [
            ('Date', 'Users'),
            ('Jan 2023', '3 Lakh'),
            ('May 2025', '1.00 Crore'),
            ('Jul 2025', '1.26 Crore'),
            ('Dec 2025', '1.45 Crore'),
            ('Feb 2026', '1.48 Crore'),
            ('Mar 2026', '1.53 Crore'),
        ]
    },
    {
        'file': 'fig4_eoffice_rate.png',
        'label': 'FIGURE 4',
        'title': 'Central Secretariat: Paper vs Digital File Processing',
        'explanation': (
            "This chart shows how much of the Central Secretariat's file work is now done "
            "digitally using e-Office.\n\n"
            "94 percent of all files and 95 percent of all receipts are now processed "
            "electronically. Between 2019 and 2024, about 37 lakh files were handled "
            "through the system.\n\n"
            "WHY IT MATTERS: The central government in Delhi has almost fully moved to "
            "digital files. But state offices in Madhya Pradesh have not reached this level. "
            "This study looks at what is stopping state government employees from doing the same."
        ),
        'source': 'Source: DARPG, PIB - Secretariat Reforms Report, 2024',
        'data_table': [
            ('Metric', 'Electronic', 'Paper'),
            ('e-Files', '94%', '6%'),
            ('e-Receipts', '95%', '5%'),
        ]
    },
    {
        'file': 'fig5_mp_igot.png',
        'label': 'FIGURE 5',
        'title': 'Madhya Pradesh: iGOT Karmayogi Performance',
        'explanation': (
            "This chart shows how many government employees in Madhya Pradesh have signed up "
            "on iGOT Karmayogi and how many courses they have completed.\n\n"
            "As of March 6, 2026, there were 9.37 lakh registered users and 42.79 lakh "
            "course enrolments. That means each user has taken about 4.6 courses on average.\n\n"
            "WHY IT MATTERS: MP government employees are signing up and taking courses, but "
            "this study will check whether these courses actually help them use IT tools in "
            "their daily work. Training alone does not always lead to real change."
        ),
        'source': 'Source: PIB, Parliament Written Reply, March 2026 (pib.gov.in)',
        'data_table': [
            ('Metric', 'Value'),
            ('Registered Users', '9,36,951'),
            ('Course Enrolments', '42,78,599'),
            ('Courses per User', '4.6x average'),
        ]
    },
    {
        'file': 'fig6_eoffice_delayering.png',
        'label': 'FIGURE 6',
        'title': 'e-Office Analytics: Bureaucratic Delayering',
        'explanation': (
            "This chart shows how many levels (layers) a file has to pass through before "
            "a decision is made in the Central Secretariat.\n\n"
            "In 2021, a file passed through 7.19 levels on average. By June 2024, this "
            "dropped to 4.19. That is a 35 percent reduction in decision layers. In December "
            "2024, the number was 4.70.\n\n"
            "WHY IT MATTERS: Fewer layers means faster decisions. If IT tools can do this "
            "at the central level, the same should be possible at the state level. This "
            "study will check whether MP offices have similar efficiency gains."
        ),
        'source': 'Source: DARPG, e-Office Analytics Dashboard, Secretariat Reforms Monthly Reports',
        'data_table': [
            ('Period', 'Avg. Transaction Levels'),
            ('2021', '7.19'),
            ('Jan 2024', '4.58'),
            ('Jun 2024', '4.19'),
            ('Dec 2024', '4.70'),
        ]
    },
    {
        'file': 'fig7_utaut_model.png',
        'label': 'FIGURE 7',
        'title': 'UTAUT Framework: Study Design Model',
        'explanation': (
            "This diagram shows the research framework used in this study. It is called "
            "UTAUT (Unified Theory of Acceptance and Use of Technology). It was created by "
            "Venkatesh and others in 2003.\n\n"
            "The model says that four things decide whether a government employee will use a digital tool:\n"
            "1. Performance Expectancy: Does the tool make work faster?\n"
            "2. Effort Expectancy: Is the tool easy to use?\n"
            "3. Social Influence: Do bosses and coworkers push for its use?\n"
            "4. Facilitating Conditions: Is there a computer, internet, and tech help?\n\n"
            "WHY IT MATTERS: This model helps us sort every problem we find into one of "
            "these four groups. It makes the study results easy to understand and act on."
        ),
        'source': 'Source: Venkatesh, Morris, Davis & Davis (2003), MIS Quarterly, 27(3), 425-478',
        'data_table': None
    },
]

for idx, fig_data in enumerate(figures, 2):
    page = new_page()
    y = MT + 10

    # Figure label
    page.insert_text(fitz.Point(ML, y), fig_data['label'], fontname=HELVB, fontsize=8, color=MGRAY)
    y += 18

    # Title
    page.insert_text(fitz.Point(ML, y), fig_data['title'], fontname=HELVB, fontsize=13, color=BLACK)
    y += 10
    page.draw_line(fitz.Point(ML, y), fitz.Point(W - MR, y), color=BLACK, width=1.2)
    y += 12

    # Insert image
    img_path = os.path.join(GFX, fig_data['file'])
    if os.path.exists(img_path):
        img_w = TW
        img_h = img_w * 0.55  # aspect ratio
        img_rect = fitz.Rect(ML, y, ML + img_w, y + img_h)
        page.insert_image(img_rect, filename=img_path)
        y += img_h + 10

    # Explanation heading
    page.insert_text(fitz.Point(ML, y), "WHAT THIS SHOWS", fontname=HELVB, fontsize=8.5, color=MGRAY)
    y += 14
    y = wrap_text(page, y, fig_data['explanation'], fontsize=8.5)
    y += 8

    # Data table (if applicable)
    if fig_data['data_table'] and y < H - MB - 80:
        page.insert_text(fitz.Point(ML, y), "DATA", fontname=HELVB, fontsize=8.5, color=MGRAY)
        y += 6
        page.draw_line(fitz.Point(ML, y), fitz.Point(ML + 200, y), color=LGRAY, width=0.5)
        y += 10
        for row in fig_data['data_table']:
            x = ML + 5
            for j, cell in enumerate(row):
                fn = HELVB if row == fig_data['data_table'][0] else HELV
                page.insert_text(fitz.Point(x, y), cell, fontname=fn, fontsize=7.5, color=BLACK)
                x += 100
            y += 11

    # Source
    page.insert_text(fitz.Point(ML, H - MB - 10), fig_data['source'], fontname=HELV, fontsize=7, color=LGRAY)

    add_footer(page, idx)

# Save
doc.save(OUT)
doc.close()
print(f'Done: {OUT}')
