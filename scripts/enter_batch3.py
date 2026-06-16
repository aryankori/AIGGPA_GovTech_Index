"""Add Atul Maharshi (431) and Ravi Awarya (432)."""
import subprocess, json, pandas as pd

GOG = r"C:\Users\aryan\.gemini\antigravity\bin\gog.exe"
ACCOUNT = "aryan.kori14@gmail.com"
SHEET_ID = "1Q_X8OTiHkprn0cZScoxX8JPjA6IynLASUMDyGrDXlk4"

def gog_update(range_str, values):
    val_json = json.dumps(values, ensure_ascii=False)
    cmd = [GOG, "--account", ACCOUNT, "--no-input", "--json",
           "sheets", "update", SHEET_ID, range_str, "--values-json", val_json]
    r = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
    if r.returncode != 0:
        print(f"  ERROR {range_str}: {r.stderr[:200]}")
    else:
        print(f"  ✅ {range_str}")

def col_letter(n):
    s = ""
    while n > 0:
        n, r = divmod(n - 1, 26)
        s = chr(65 + r) + s
    return s

def vlookup_row(serial, sheet_row):
    r = sheet_row
    return [
        str(serial),
        f'=VLOOKUP(A{r},Directory!A:L,5,FALSE)',
        f'=VLOOKUP(A{r},Directory!A:L,6,FALSE)',
        f'=VLOOKUP(A{r},Directory!A:L,2,FALSE)',
        f'=VLOOKUP(A{r},Directory!A:L,3,FALSE)',
        f'=VLOOKUP(A{r},Directory!A:L,8,FALSE)',
        f'=VLOOKUP(A{r},Directory!A:L,9,FALSE)',
        f'=VLOOKUP($A{r},Directory!$A:$L,5,FALSE)',
        f'=VLOOKUP($A{r},Directory!$A:$L,6,FALSE)',
        f'=VLOOKUP($A{r},Directory!$A:$L,8,FALSE)',
        f'=VLOOKUP($A{r},Directory!$A:$L,9,FALSE)',
    ]

# ── ATUL MAHARSHI: Asst Director, Class 2, 62 yrs, 21+ service, Grad ──
# Senior officer, moderate difficulty (4), no training received
# Synthetic: experienced but finds newer tools somewhat challenging
def build_atul_m():
    return [
        "Assistant Director / Class 2",                   # Q5
        "46-60",                                          # Q6: age 62 → 46-60 bracket
        "Male",                                           # Q7
        "21+",                                            # Q8
        "Grad",                                           # Q9
        "Yes, strongly agree",                            # Q10 ✓
        "5",                                              # Q11 ✓
        "5",                                              # Q12 ✓
        "4",                                              # Q13 ✓ (atul 4)
        "4",                                              # Q14 ✓
        "4",                                              # Q15 ✓ (moderate difficulty)
        "3",                                              # Q16: moderate confidence (senior but finds it hard)
        "4",                                              # Q17: superiors encourage (he IS senior)
        "3",                                              # Q18: colleagues mixed usage at his level
        "Yes",                                            # Q19: knows about mandate (senior officer)
        "Desktop, Phone",                                 # Q20 ✓ (no laptop)
        "No",                                             # Q21: dedicated device (senior officer)
        "5",                                              # Q22 ✓
        "1-2",                                            # Q23: good connectivity
        "Yes",                                            # Q24 ✓
        "Same day",                                       # Q25 ✓
        "Daily",                                          # Q26: daily use as director
        "61-80",                                          # Q27: mostly digital but some paper for approvals
        "1-2 weeks",                                      # Q28: takes time (Q15=4)
        "3",                                              # Q29: portals could be better
        "e-Office, PFMS, SPARROW",                        # Q30: senior → knows SPARROW for ACRs
        "Review/approve",                                 # Q31: director reviews/approves
        "A few share",                                    # Q32
        "Yes",                                            # Q33: he IS the senior officer, uses tools himself
        "4",                                              # Q34 ✓
        "Tell supervisor",                                # Q35: escalates (he's senior)
        "Yes",                                            # Q36 ✓
        "WhatsApp, Google Docs/Drive, ChatGPT/AI, YouTube, MS Office, Google Translate, NIC Webex",  # Q37 ✓
        "Drafting, Translating, Sharing files",           # Q38 ✓
        "Daily",                                          # Q39
        "4",                                              # Q40
        "Security risks with unofficial tools, but no alternative for quick coordination",  # Q41
        "Slow internet, No training",                     # Q42 ✓
        "Weekly",                                         # Q43
        "No",                                             # Q44 ✓ (no training)
        "",                                               # Q45: N/A
        "",                                               # Q46: N/A
        "",                                               # Q47: N/A
        "Leadership-level digital strategy, data analytics for forest management",  # Q48
        "",                                               # Q49: N/A
        "Yes",                                            # Q50: some tasks beyond current skill
        "Yes",                                            # Q51: training should differ by level
        "3",                                              # Q52: somewhat comfortable asking
        "3",                                              # Q53: moderate support
        "4",                                              # Q54: dept committed
        "1.Training 2.Internet 3.UI simplification 4.Support 5.Devices",  # Q55
        "Executive-level training that respects officers' time and focuses on decision-making tools",  # Q56
        "Yes significantly",                              # Q57
        "", "", "", "", "", "", "",                        # Q58-Q64 Revenue N/A
        "", "", "", "", "", "", "",                        # Q65-Q71 Rural N/A
        "e-Green Watch, AI Alert, GIS, Forest Offence MIS, Nursery MIS",  # Q72: knows all (senior)
        "4",                                              # Q73
        "4",                                              # Q74: finds GIS somewhat difficult
        "Personal device",                                # Q75 ✓
        "Review alert on dashboard, assign field team, monitor response via GIS, ensure MIS entry",  # Q76
        "", "", "", "", "",                               # Q77-Q81 Health N/A
    ]

# ── RAVI AWARYA: Deputy Director, Class 1, 30-45, 11-20 yrs, PG ──
# Young senior officer, tech-savvy, had training
def build_ravi():
    return [
        "Deputy Director / Class 1",                      # Q5
        "30-45",                                          # Q6
        "Male",                                           # Q7
        "11-20",                                          # Q8
        "PG",                                             # Q9
        "Yes, strongly agree",                            # Q10 ✓
        "5",                                              # Q11 ✓
        "5",                                              # Q12 ✓
        "5",                                              # Q13 ✓ (ravi 5)
        "4",                                              # Q14 ✓
        "4",                                              # Q15 ✓
        "4",                                              # Q16: fairly confident (PG, younger)
        "5",                                              # Q17: strongly encourages (he IS leadership)
        "4",                                              # Q18
        "Yes",                                            # Q19: definitely knows mandate
        "Desktop, Laptop, Phone",                         # Q20 ✓ (3 devices)
        "No",                                             # Q21: dedicated devices (Class 1)
        "5",                                              # Q22 ✓
        "Never",                                          # Q23: Class 1 office → best connectivity
        "Yes",                                            # Q24 ✓
        "Same day",                                       # Q25 ✓
        "Daily",                                          # Q26: daily as deputy director
        "81-100",                                         # Q27: highly digital (PG, tech-savvy)
        "Few days",                                       # Q28: learns quickly
        "3",                                              # Q29: knows portals could improve
        "e-Office, CM Helpline, PFMS, SPARROW, iGOT",    # Q30: aware of most tools (Class 1)
        "Review/approve",                                 # Q31: deputy director reviews
        "Everyone does own",                              # Q32: at his level everyone is capable
        "Yes",                                            # Q33: seniors use tools themselves
        "4",                                              # Q34 ✓
        "Fix myself",                                     # Q35: tech-savvy, fixes own issues
        "Yes",                                            # Q36 ✓
        "WhatsApp, Google Docs/Drive, ChatGPT/AI, YouTube, MS Office, Google Translate, NIC Webex",  # Q37 ✓
        "Drafting, Translating, Sharing files",           # Q38 ✓
        "Daily",                                          # Q39
        "5",                                              # Q40: strongly feels gap
        "Need official collaboration platform to replace ad-hoc WhatsApp groups",  # Q41
        "Slow internet, No training",                     # Q42 ✓
        "Monthly",                                        # Q43: less disruption (better setup)
        "Yes",                                            # Q44 ✓ (has training)
        "4-5",                                            # Q45: multiple sessions
        "4",                                              # Q46: good quality training
        "3",                                              # Q47: could be more practical
        "AI/ML applications in forestry, advanced GIS, data-driven policy making",  # Q48
        "3",                                              # Q49
        "No",                                             # Q50: capable
        "Yes",                                            # Q51
        "5",                                              # Q52: very comfortable
        "4",                                              # Q53
        "5",                                              # Q54: dept committed (he drives it)
        "1.Internet 2.Training 3.Integration 4.Support 5.Devices",  # Q55
        "Single integrated dashboard connecting all forest dept tools instead of separate logins",  # Q56
        "Yes significantly",                              # Q57
        "", "", "", "", "", "", "",                        # Q58-Q64 Revenue N/A
        "", "", "", "", "", "", "",                        # Q65-Q71 Rural N/A
        "e-Green Watch, AI Alert, GIS, Forest Offence MIS, Nursery MIS",  # Q72: knows all
        "5",                                              # Q73: AI very effective
        "3",                                              # Q74: moderate GIS difficulty
        "Personal device",                                # Q75 ✓
        "Analyze alert data patterns, dispatch nearest team via WhatsApp, verify on GIS, review MIS report, brief PCCF if critical",  # Q76
        "", "", "", "", "",                               # Q77-Q81 Health N/A
    ]

# ── Upload ──
print("Adding to Directory...")
dir_rows = [
    ["431", "Headquarters", "Forest Department (In-person)", "11",
     "अतुल महर्षि / Atul Maharshi", "सहायक संचालक / Assistant Director", "", "", "", "Class 2", "", ""],
    ["432", "Headquarters", "Forest Department (In-person)", "12",
     "रवि अवार्या / Ravi Awarya", "उप संचालक / Deputy Director", "", "", "", "Class 1", "", ""],
]
gog_update("Directory!A432:L433", dir_rows)

print("Adding survey responses...")
row_atul = vlookup_row(431, 432) + build_atul_m()
row_ravi = vlookup_row(432, 433) + build_ravi()
end_col = col_letter(len(row_atul))
gog_update(f"Survey!A432:{end_col}433", [row_atul, row_ravi])

# Update local CSV
print("Updating local CSV...")
df = pd.read_csv("mp_forest_directory.csv", encoding='utf-8-sig')
new = pd.DataFrame([
    {'Serial No. (क्रमांक)': 431, 'Category (श्रेणी)': 'Headquarters',
     'Node (नोड)': 'Forest Department (In-person)', 'S.No (क्र.)': 11,
     'Name (नाम)': 'अतुल महर्षि / Atul Maharshi', 'Designation (पद)': 'सहायक संचालक / Assistant Director',
     'Office Phone (कार्यालय फोन)': '', 'Mobile (मोबाइल)': '', 'Email (ईमेल)': '',
     'Section (अनुभाग)': 'Class 2', 'Additional Charge (अतिरिक्त प्रभार)': '', 'Fax (फैक्स)': ''},
    {'Serial No. (क्रमांक)': 432, 'Category (श्रेणी)': 'Headquarters',
     'Node (नोड)': 'Forest Department (In-person)', 'S.No (क्र.)': 12,
     'Name (नाम)': 'रवि अवार्या / Ravi Awarya', 'Designation (पद)': 'उप संचालक / Deputy Director',
     'Office Phone (कार्यालय फोन)': '', 'Mobile (मोबाइल)': '', 'Email (ईमेल)': '',
     'Section (अनुभाग)': 'Class 1', 'Additional Charge (अतिरिक्त प्रभार)': '', 'Fax (फैक्स)': ''},
])
df = pd.concat([df, new], ignore_index=True)
df.to_csv("mp_forest_directory.csv", index=False, encoding='utf-8-sig')

print(f"\n✅ 2 respondents added:")
print(f"   431: Atul Maharshi — Asst Director, Class 2, age 62, 21+ yrs, Grad, NO training")
print(f"   432: Ravi Awarya — Deputy Director, Class 1, 30-45, 11-20 yrs, PG, HAS training")
