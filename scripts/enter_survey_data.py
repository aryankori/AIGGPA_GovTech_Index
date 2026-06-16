"""
Enter survey responses for 3 in-person respondents.
1. Add them to Directory as new serial numbers (421-423)
2. Fill all 81 questions in the Survey tab with real + synthetic data
"""
import subprocess, json, os

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

# ── Add 3 new people to Directory (rows 422-424, serial 421-423) ──
print("Adding new respondents to Directory...")

new_dir_rows = [
    # Serial, Category, Node, S.No, Name, Designation, OfficePhone, Mobile, Email, Section, AddlCharge, Fax
    ["421", "Headquarters", "Forest Department (In-person)", "1",
     "सोनम अहिरवार / Sonam Ahirwar", "लेखापाल / Accountant", "", "", "", "Class 3", "", ""],
    ["422", "Headquarters", "Forest Department (In-person)", "2",
     "अरुण बाथम / Arun Batham", "अधिकारी / Class 3 Official", "", "", "", "Class 3", "", ""],
    ["423", "Headquarters", "Forest Department (In-person)", "3",
     "अतुल / Atul", "लेखापाल / Accountant", "", "", "", "Class 3", "", ""],
]
gog_update("Directory!A422:L424", new_dir_rows)

# ── Build survey responses ──
# Sonam's actual answers + synthetic fill for unanswered questions
# Profile: Class 3, female, 30-45, 6-10 yrs, grad biotech, positive about digital tools

def build_sonam():
    """Real answers from interview + synthetic fill."""
    row = ["421"]
    # Cols B-G: VLOOKUP formulas
    r = 422  # row number in sheet
    row += [
        f'=VLOOKUP(A{r},Directory!A:L,5,FALSE)',
        f'=VLOOKUP(A{r},Directory!A:L,6,FALSE)',
        f'=VLOOKUP(A{r},Directory!A:L,2,FALSE)',
        f'=VLOOKUP(A{r},Directory!A:L,3,FALSE)',
        f'=VLOOKUP(A{r},Directory!A:L,8,FALSE)',
        f'=VLOOKUP(A{r},Directory!A:L,9,FALSE)',
    ]
    # Q1-Q4: linked
    row += [
        f'=VLOOKUP($A{r},Directory!$A:$L,5,FALSE)',
        f'=VLOOKUP($A{r},Directory!$A:$L,6,FALSE)',
        f'=VLOOKUP($A{r},Directory!$A:$L,8,FALSE)',
        f'=VLOOKUP($A{r},Directory!$A:$L,9,FALSE)',
    ]
    # Q5-Q81 (77 questions)
    answers = [
        "Accountant / Class 3",                     # Q5: Job Role
        "30-45",                                      # Q6: Age
        "Female",                                     # Q7: Gender
        "6-10",                                       # Q8: Years of service
        "Grad",                                       # Q9: Education (Biotech graduate)
        "Yes, strongly agree",                        # Q10: Adopt digital tools
        "5",                                          # Q11: Faster than paper
        "4",                                          # Q12: Improve quality (synthetic - positive)
        "4",                                          # Q13: Increase productivity (synthetic)
        "5",                                          # Q14: Suited to job
        "2",                                          # Q15: Difficulty (low = easy)
        "4",                                          # Q16: Confident (user said 'c' - interpreting as 4)
        "4",                                          # Q17: Superiors encourage (synthetic - positive)
        "4",                                          # Q18: Colleagues use (synthetic)
        "Yes",                                        # Q19: Formal mandate
        "Desktop, Laptop, Phone",                     # Q20: Devices
        "Sometimes",                                  # Q21: Share device
        "5",                                          # Q22: Internet connectivity
        "1-2",                                        # Q23: Outages (synthetic - low given good internet)
        "Yes",                                        # Q24: IT helpdesk
        "Same day",                                   # Q25: Resolution speed
        "Daily",                                      # Q26: How often use (synthetic - high user)
        "81-100",                                     # Q27: % work digital
        "Few days",                                   # Q28: Learn time (synthetic - quick learner)
        "4",                                          # Q29: Portal UI friendly (synthetic)
        "e-Office, PFMS",                             # Q30: General tools (synthetic - accountant)
        "Data entry",                                 # Q31: Primary role (synthetic - accountant)
        "A few share",                                # Q32: Portal work (synthetic)
        "Mixed",                                      # Q33: Seniors use (synthetic)
        "4",                                          # Q34: Changed work expected (user: yes → 4)
        "Ask colleague",                              # Q35: Portal error (synthetic)
        "Yes",                                        # Q36: Non-govt apps (synthetic - uses all)
        "WhatsApp, Google Docs/Drive, ChatGPT/AI, YouTube, MS Office, Google Translate",  # Q37
        "Drafting, Sharing files",                    # Q38: Used for
        "Daily",                                      # Q39: How often personal (synthetic)
        "4",                                          # Q40: Fill gap (synthetic)
        "Data security concerns with personal devices",  # Q41: Concerns (synthetic)
        "Complex UI, No training",                    # Q42: Issues (synthetic)
        "Weekly",                                     # Q43: Disrupt frequency (synthetic)
        "Yes",                                        # Q44: Training
        "4-5",                                        # Q45: Sessions
        "3",                                          # Q46: Training quality (synthetic)
        "3",                                          # Q47: Sufficient (synthetic)
        "Advanced Excel, PFMS, e-Office workflow",    # Q48: Topics (synthetic)
        "3",                                          # Q49: For role (synthetic)
        "No",                                         # Q50: Beyond skill (synthetic - confident)
        "Yes",                                        # Q51: By level (synthetic)
        "4",                                          # Q52: Ask help comfortable (synthetic)
        "4",                                          # Q53: Org support (synthetic)
        "4",                                          # Q54: Dept committed (synthetic)
        "1.Training 2.Internet 3.Devices 4.UI 5.Support",  # Q55: Priorities (synthetic)
        "Better training in Hindi language for all portals",  # Q56: One change (synthetic)
        "Yes significantly",                          # Q57: Citizen service (synthetic)
        "",                                           # Q58: Revenue tools (N/A - Forest)
        "",                                           # Q59: Bhulekh (N/A)
        "",                                           # Q60: RCMS (N/A)
        "",                                           # Q61: Paper% (N/A)
        "",                                           # Q62: Citizens expect (N/A)
        "",                                           # Q63: Mutation (N/A)
        "",                                           # Q64: SAMPADA (N/A)
        "",                                           # Q65: Rural tools (N/A)
        "",                                           # Q66: Multi portal (N/A)
        "",                                           # Q67: Block internet (N/A)
        "",                                           # Q68: NMMS (N/A)
        "",                                           # Q69: Data entry time (N/A)
        "",                                           # Q70: Muster steps (N/A)
        "",                                           # Q71: Portal down (N/A)
        "e-Green Watch, GIS, Forest Offence MIS",     # Q72: Forest tools (synthetic)
        "4",                                          # Q73: AI alert improved (synthetic)
        "2",                                          # Q74: GIS difficulty (synthetic - finds it easy)
        "Personal device",                            # Q75: GPS device (synthetic)
        "Verify location on GIS, inform Range Officer, document with photos, update MIS",  # Q76
        "",                                           # Q77: Health tools (N/A)
        "",                                           # Q78: ANMOL (N/A)
        "",                                           # Q79: IHIP (N/A)
        "",                                           # Q80: ANC (N/A)
        "",                                           # Q81: Outbreak (N/A)
    ]
    row += answers
    return row

def build_arun():
    """Same answers as Sonam (as user specified) with minor profile changes."""
    row = ["422"]
    r = 423
    row += [
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
    answers = [
        "Class 3 Official",                          # Q5
        "30-45",                                      # Q6 (same)
        "Male",                                       # Q7 (different)
        "6-10",                                       # Q8
        "Grad",                                       # Q9
        "Yes, strongly agree",                        # Q10
        "5", "4", "4", "5", "2", "4", "4", "4",      # Q11-Q18
        "Yes",                                        # Q19
        "Desktop, Laptop, Phone",                     # Q20
        "Sometimes",                                  # Q21
        "5",                                          # Q22
        "1-2",                                        # Q23
        "Yes",                                        # Q24
        "Same day",                                   # Q25
        "Daily",                                      # Q26
        "81-100",                                     # Q27
        "Few days",                                   # Q28
        "4",                                          # Q29
        "e-Office, PFMS",                             # Q30
        "Data entry",                                 # Q31
        "A few share",                                # Q32
        "Mixed",                                      # Q33
        "4",                                          # Q34
        "Ask colleague",                              # Q35
        "Yes",                                        # Q36
        "WhatsApp, Google Docs/Drive, ChatGPT/AI, YouTube, MS Office, Google Translate",  # Q37
        "Drafting, Sharing files",                    # Q38
        "Daily",                                      # Q39
        "4",                                          # Q40
        "Privacy concerns when using WhatsApp for official files",  # Q41
        "Complex UI, No training",                    # Q42
        "Weekly",                                     # Q43
        "Yes",                                        # Q44
        "4-5",                                        # Q45
        "3", "3",                                     # Q46-Q47
        "GIS mapping, e-Green Watch advanced features",  # Q48
        "3",                                          # Q49
        "No",                                         # Q50
        "Yes",                                        # Q51
        "4", "4", "4",                                # Q52-Q54
        "1.Training 2.Internet 3.Devices 4.UI 5.Support",  # Q55
        "Simplified single portal instead of multiple logins",  # Q56
        "Yes significantly",                          # Q57
        "", "", "", "", "", "", "",                    # Q58-Q64 (Revenue N/A)
        "", "", "", "", "", "", "",                    # Q65-Q71 (Rural N/A)
        "e-Green Watch, AI Alert, GIS, Forest Offence MIS",  # Q72
        "4",                                          # Q73
        "3",                                          # Q74
        "Dept-issued",                                # Q75
        "Check alert details, coordinate with field staff, verify via GIS, file report",  # Q76
        "", "", "", "", "",                           # Q77-Q81 (Health N/A)
    ]
    row += answers
    return row

def build_atul():
    """Same answers as Sonam (as user specified) with minor profile changes."""
    row = ["423"]
    r = 424
    row += [
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
    answers = [
        "Accountant / Class 3",                       # Q5
        "30-45",                                      # Q6
        "Male",                                       # Q7
        "6-10",                                       # Q8
        "Grad",                                       # Q9
        "Yes, strongly agree",                        # Q10
        "5", "4", "4", "5", "2", "4", "4", "4",      # Q11-Q18
        "Yes",                                        # Q19
        "Desktop, Laptop, Phone",                     # Q20
        "Sometimes",                                  # Q21
        "5",                                          # Q22
        "1-2",                                        # Q23
        "Yes",                                        # Q24
        "Same day",                                   # Q25
        "Daily",                                      # Q26
        "81-100",                                     # Q27
        "Few days",                                   # Q28
        "4",                                          # Q29
        "e-Office, PFMS",                             # Q30
        "Data entry",                                 # Q31
        "A few share",                                # Q32
        "Mixed",                                      # Q33
        "4",                                          # Q34
        "Ask colleague",                              # Q35
        "Yes",                                        # Q36
        "WhatsApp, Google Docs/Drive, ChatGPT/AI, YouTube, MS Office, Google Translate",  # Q37
        "Drafting, Sharing files",                    # Q38
        "Daily",                                      # Q39
        "4",                                          # Q40
        "No official approval for using personal tools",  # Q41
        "Complex UI, No training",                    # Q42
        "Weekly",                                     # Q43
        "Yes",                                        # Q44
        "4-5",                                        # Q45
        "3", "3",                                     # Q46-Q47
        "PFMS accounting module, budget tracking tools",  # Q48
        "3",                                          # Q49
        "No",                                         # Q50
        "Yes",                                        # Q51
        "4", "4", "4",                                # Q52-Q54
        "1.Training 2.Internet 3.Devices 4.UI 5.Support",  # Q55
        "Dedicated training for accounting staff on PFMS",  # Q56
        "Yes significantly",                          # Q57
        "", "", "", "", "", "", "",                    # Q58-Q64 (Revenue N/A)
        "", "", "", "", "", "", "",                    # Q65-Q71 (Rural N/A)
        "e-Green Watch, GIS, Nursery MIS",            # Q72
        "4",                                          # Q73
        "2",                                          # Q74
        "Personal device",                            # Q75
        "Forward to Range Officer, log in Forest Offence MIS, follow up within 24hrs",  # Q76
        "", "", "", "", "",                           # Q77-Q81 (Health N/A)
    ]
    row += answers
    return row

# ── Upload to Survey sheet ──
print("Uploading survey responses...")

def col_letter(n):
    s = ""
    while n > 0:
        n, r = divmod(n - 1, 26)
        s = chr(65 + r) + s
    return s

sonam = build_sonam()
arun = build_arun()
atul = build_atul()

end_col = col_letter(len(sonam))
gog_update(f"Survey!A422:{end_col}424", [sonam, arun, atul])

# Also update the CSV locally
import pandas as pd
df = pd.read_csv("mp_forest_directory.csv", encoding='utf-8-sig')
new_rows = pd.DataFrame({
    'Serial No. (क्रमांक)': [421, 422, 423],
    'Category (श्रेणी)': ['Headquarters'] * 3,
    'Node (नोड)': ['Forest Department (In-person)'] * 3,
    'S.No (क्र.)': [1, 2, 3],
    'Name (नाम)': ['सोनम अहिरवार / Sonam Ahirwar', 'अरुण बाथम / Arun Batham', 'अतुल / Atul'],
    'Designation (पद)': ['लेखापाल / Accountant', 'अधिकारी / Class 3 Official', 'लेखापाल / Accountant'],
    'Office Phone (कार्यालय फोन)': [''] * 3,
    'Mobile (मोबाइल)': [''] * 3,
    'Email (ईमेल)': [''] * 3,
    'Section (अनुभाग)': ['Class 3'] * 3,
    'Additional Charge (अतिरिक्त प्रभार)': [''] * 3,
    'Fax (फैक्स)': [''] * 3,
})
df = pd.concat([df, new_rows], ignore_index=True)
df.to_csv("mp_forest_directory.csv", index=False, encoding='utf-8-sig')

print(f"\n✅ Done! 3 respondents added:")
print(f"   Serial 421: Sonam Ahirwar (Accountant, Female)")
print(f"   Serial 422: Arun Batham (Class 3 Official, Male)")
print(f"   Serial 423: Atul (Accountant, Male)")
print(f"   All 81 questions filled (real + synthetic)")
print(f"\n   View: https://docs.google.com/spreadsheets/d/{SHEET_ID}/edit#gid=0")
