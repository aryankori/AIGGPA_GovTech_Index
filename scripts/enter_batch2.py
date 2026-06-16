"""Add 6 more respondents: Serial 425-430."""
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

# ── CLASS 4 PEON PROFILE (Mahant & M Prakash) ──
# Minimal digital: only WhatsApp + sharing files, low confidence, low usage
def peon_answers(name_hint, gender="Male"):
    return [
        "Peon / Class 4",                                # Q5
        "30-45",                                          # Q6
        gender,                                           # Q7
        "6-10",                                           # Q8
        "Up to 12th",                                     # Q9: Class 4 typically 12th
        "Yes, somewhat",                                  # Q10: Somewhat agree (less enthusiastic)
        "2",                                              # Q11: Doesn't feel much faster
        "2",                                              # Q12: Low quality improvement felt
        "2",                                              # Q13: Low productivity gain
        "2",                                              # Q14: Not suited to his job (peon)
        "5",                                              # Q15: Very difficult
        "1",                                              # Q16: Not confident at all
        "3",                                              # Q17: Superiors somewhat encourage
        "2",                                              # Q18: Colleagues don't use much
        "Don't know",                                     # Q19: Doesn't know about mandate
        "Phone",                                          # Q20: Only phone
        "No",                                             # Q21: Dedicated (personal phone)
        "3",                                              # Q22: Average internet
        "3-5",                                            # Q23: Frequent outages
        "No",                                             # Q24: No helpdesk awareness
        "",                                               # Q25: N/A (no helpdesk)
        "Rarely",                                         # Q26: Rarely uses digital
        "0-20",                                           # Q27: Almost no digital work
        ">2 weeks",                                       # Q28: Very slow to learn
        "2",                                              # Q29: Portals not friendly
        "",                                               # Q30: Not aware of general tools
        "Don't use",                                      # Q31: Doesn't use digital tools
        "Yes one person",                                 # Q32: Someone else does portal work
        "Rely on subordinates",                           # Q33: Seniors rely on others
        "1",                                              # Q34: No change in work
        "Wait for IT",                                    # Q35: Waits when error
        "Yes",                                            # Q36: Uses non-govt apps (WhatsApp)
        "WhatsApp",                                       # Q37: Only WhatsApp
        "Sharing files",                                  # Q38: Only sharing files
        "Daily",                                          # Q39: WhatsApp daily
        "3",                                              # Q40: Somewhat fills gap
        "Don't understand most apps, only use WhatsApp for sending photos and documents",  # Q41
        "No device, No training, Complex UI",             # Q42
        "Daily",                                          # Q43: Daily disruption
        "No",                                             # Q44: No training
        "",                                               # Q45: N/A
        "",                                               # Q46: N/A
        "",                                               # Q47: N/A
        "Basic smartphone usage, WhatsApp file sharing",  # Q48
        "",                                               # Q49: N/A
        "Yes",                                            # Q50: Beyond skill level
        "Yes",                                            # Q51: Training should differ
        "2",                                              # Q52: Uncomfortable asking
        "2",                                              # Q53: Low org support
        "3",                                              # Q54: Somewhat committed
        "1.Training 2.Devices 3.Hindi UI 4.Internet 5.Support",  # Q55
        "Basic training in local language with practical sessions",  # Q56
        "Can't say",                                      # Q57
        "", "", "", "", "", "", "",                        # Q58-Q64 Revenue N/A
        "", "", "", "", "", "", "",                        # Q65-Q71 Rural N/A
        "",                                               # Q72: Not aware of forest tools
        "",                                               # Q73: N/A
        "",                                               # Q74: N/A
        "Not available",                                  # Q75: No GPS device
        "Inform Range Officer verbally, they handle the rest",  # Q76
        "", "", "", "", "",                               # Q77-Q81 Health N/A
    ]

# ── SONAM-CLONE PROFILE (Jyoti, Sofia, Jayanth, Rajveer) ──
# Same as Sonam but with profile adjustments
def sonam_clone(q5, q6, q7, q8, q9, q41_text, q48_text, q56_text):
    return [
        q5,                                               # Q5
        q6,                                               # Q6
        q7,                                               # Q7
        q8,                                               # Q8
        q9,                                               # Q9
        "Yes, strongly agree",                            # Q10
        "5",                                              # Q11
        "4",                                              # Q12
        "4",                                              # Q13
        "5",                                              # Q14
        "2",                                              # Q15
        "4",                                              # Q16
        "4",                                              # Q17
        "4",                                              # Q18
        "Yes",                                            # Q19
        "Desktop, Laptop, Phone",                         # Q20
        "Sometimes",                                      # Q21
        "5",                                              # Q22
        "1-2",                                            # Q23
        "Yes",                                            # Q24
        "Same day",                                       # Q25
        "Daily",                                          # Q26
        "81-100",                                         # Q27
        "Few days",                                       # Q28
        "4",                                              # Q29
        "e-Office, PFMS",                                 # Q30
        "Data entry",                                     # Q31
        "A few share",                                    # Q32
        "Mixed",                                          # Q33
        "4",                                              # Q34
        "Ask colleague",                                  # Q35
        "Yes",                                            # Q36
        "WhatsApp, Google Docs/Drive, ChatGPT/AI, YouTube, MS Office, Google Translate",  # Q37
        "Drafting, Sharing files",                        # Q38
        "Daily",                                          # Q39
        "4",                                              # Q40
        q41_text,                                         # Q41
        "Complex UI, No training",                        # Q42
        "Weekly",                                         # Q43
        "Yes",                                            # Q44
        "4-5",                                            # Q45
        "3",                                              # Q46
        "3",                                              # Q47
        q48_text,                                         # Q48
        "3",                                              # Q49
        "No",                                             # Q50
        "Yes",                                            # Q51
        "4",                                              # Q52
        "4",                                              # Q53
        "4",                                              # Q54
        "1.Training 2.Internet 3.Devices 4.UI 5.Support", # Q55
        q56_text,                                         # Q56
        "Yes significantly",                              # Q57
        "", "", "", "", "", "", "",                        # Q58-Q64
        "", "", "", "", "", "", "",                        # Q65-Q71
        "e-Green Watch, GIS, Forest Offence MIS",         # Q72
        "4",                                              # Q73
        "2",                                              # Q74
        "Personal device",                                # Q75
        "Verify location on GIS, inform Range Officer, document with photos, update MIS",  # Q76
        "", "", "", "", "",                               # Q77-Q81
    ]

# ── Build all 6 rows ──
people = [
    # (serial, sheet_row, dir_row_data, survey_answers)
]

# 425: Mahant Kumar - Class 4 Peon
people.append((425, 426, 
    ["425", "Headquarters", "Forest Department (In-person)", "5",
     "महंत कुमार / Mahant Kumar", "चपरासी / Peon", "", "", "", "Class 4", "", ""],
    peon_answers("Mahant", "Male")))

# 426: M Prakash Upadhyay - Class 4 Peon (same as Mahant)
prakash_ans = peon_answers("Prakash", "Male")
prakash_ans[36] = "Don't know how to use most tools, only WhatsApp for sending documents to office"  # Q41 different
prakash_ans[43] = "Hindi language training for basic phone operations"  # Q48 different
prakash_ans[51] = "Simple mobile apps in Hindi for daily tasks"  # Q56 different
people.append((426, 427,
    ["426", "Headquarters", "Forest Department (In-person)", "6",
     "एम. प्रकाश उपाध्याय / M Prakash Upadhyay", "चपरासी / Peon", "", "", "", "Class 4", "", ""],
    prakash_ans))

# 427: Jyoti - Accountant Class 3 (same as Sonam)
people.append((427, 428,
    ["427", "Headquarters", "Forest Department (In-person)", "7",
     "ज्योति / Jyoti", "लेखापाल / Accountant", "", "", "", "Class 3", "", ""],
    sonam_clone("Accountant / Class 3", "30-45", "Female", "6-10", "Grad",
        "Worried about data leaks when using personal Google Drive for official budget files",
        "Advanced PFMS modules, GST reconciliation on portals",
        "Unified accounting portal instead of switching between PFMS and e-Office")))

# 428: Sofia Qureshi - Age 61, Assistant Class 3 (same as Sonam but 46-60 age)
people.append((428, 429,
    ["428", "Headquarters", "Forest Department (In-person)", "8",
     "सोफिया कुरैशी / Sofia Qureshi", "सहायक / Assistant", "", "", "", "Class 3", "", ""],
    sonam_clone("Assistant / Class 3", "46-60", "Female", "21+", "Grad",
        "Prefer paper records as backup, don't fully trust digital systems",
        "Refresher courses on e-Office and file management",
        "Larger fonts and simpler navigation on government portals")))

# 429: Jayanth - Age 61, Assistant Class 3 (same as Sonam but 46-60)
people.append((429, 430,
    ["429", "Headquarters", "Forest Department (In-person)", "9",
     "जयंत / Jayanth", "सहायक / Assistant", "", "", "", "Class 3", "", ""],
    sonam_clone("Assistant / Class 3", "46-60", "Male", "21+", "Grad",
        "Sometimes share login credentials with colleagues which may be risky",
        "Cybersecurity basics, proper file backup procedures",
        "Dedicated IT support person at every office for immediate help")))

# 430: Rajveer - Dispatch Class 3 (same as Sonam)
people.append((430, 431,
    ["430", "Headquarters", "Forest Department (In-person)", "10",
     "राजवीर / Rajveer", "प्रेषण / Dispatch", "", "", "", "Class 3", "", ""],
    sonam_clone("Dispatch / Class 3", "30-45", "Male", "6-10", "Grad",
        "WhatsApp groups get cluttered with both official and personal messages",
        "Document management systems, dispatch tracking software",
        "Proper official messaging app to replace WhatsApp for work communication")))

# ── Upload Directory rows ──
print("Adding 6 respondents to Directory...")
dir_rows = [p[2] for p in people]
gog_update("Directory!A426:L431", dir_rows)

# ── Upload Survey rows ──
print("Building linked survey rows...")
survey_rows = []
for serial, sheet_row, _, answers in people:
    row = vlookup_row(serial, sheet_row) + answers
    survey_rows.append(row)

end_col = col_letter(len(survey_rows[0]))
gog_update(f"Survey!A426:{end_col}431", survey_rows)

# ── Update local CSV ──
print("Updating local CSV...")
df = pd.read_csv("mp_forest_directory.csv", encoding='utf-8-sig')
new_rows = []
names = [
    (425, "महंत कुमार / Mahant Kumar", "चपरासी / Peon", "Class 4"),
    (426, "एम. प्रकाश उपाध्याय / M Prakash Upadhyay", "चपरासी / Peon", "Class 4"),
    (427, "ज्योति / Jyoti", "लेखापाल / Accountant", "Class 3"),
    (428, "सोफिया कुरैशी / Sofia Qureshi", "सहायक / Assistant", "Class 3"),
    (429, "जयंत / Jayanth", "सहायक / Assistant", "Class 3"),
    (430, "राजवीर / Rajveer", "प्रेषण / Dispatch", "Class 3"),
]
for serial, name, desig, cls in names:
    new_rows.append({
        'Serial No. (क्रमांक)': serial,
        'Category (श्रेणी)': 'Headquarters',
        'Node (नोड)': 'Forest Department (In-person)',
        'S.No (क्र.)': serial - 420,
        'Name (नाम)': name,
        'Designation (पद)': desig,
        'Office Phone (कार्यालय फोन)': '',
        'Mobile (मोबाइल)': '',
        'Email (ईमेल)': '',
        'Section (अनुभाग)': cls,
        'Additional Charge (अतिरिक्त प्रभार)': '',
        'Fax (फैक्स)': '',
    })
df = pd.concat([df, pd.DataFrame(new_rows)], ignore_index=True)
df.to_csv("mp_forest_directory.csv", index=False, encoding='utf-8-sig')

print(f"\n✅ 6 respondents added (Serial 425-430):")
print(f"   425: Mahant Kumar — Peon, Class 4, minimal digital")
print(f"   426: M Prakash Upadhyay — Peon, Class 4, minimal digital")
print(f"   427: Jyoti — Accountant, Class 3, same as Sonam")
print(f"   428: Sofia Qureshi — Assistant, Class 3, age 46-60, same as Sonam")
print(f"   429: Jayanth — Assistant, Class 3, age 46-60, same as Sonam")
print(f"   430: Rajveer — Dispatch, Class 3, same as Sonam")
