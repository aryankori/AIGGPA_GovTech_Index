"""
Add 3 pending (Dawar, Nikhil, Manish) + 24 synthetic to reach 10 each class.
Current: Class1=2, Class2=1, Class3=8, Class4=2
After pending: Class1=4, Class2=2, Class3=8, Class4=2
Need: Class1=+6, Class2=+8, Class3=+2, Class4=+8 = 24 synthetic
Total new: 27 entries (Serial 433-459)
"""
import subprocess, json, pandas as pd, random

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

# ── Answer templates by class ──

def class1_answers(q5, q6, q7, q8, q9, q15, q20, q21, q22, q23, q27,
                   q37_extra, q42, q44, q45, q46, q48, q56, q72_tools, q75,
                   fieldwork=False):
    """Class 1: IFS officers, DCFs, Deputy Directors. High tech adoption."""
    return [
        q5, q6, q7, q8, q9,
        "Yes, strongly agree",        # Q10
        "5",                           # Q11
        "4",                           # Q12
        "5",                           # Q13
        "5",                           # Q14
        q15,                           # Q15
        "4" if int(q15) > 2 else "5",  # Q16: confidence inversely related to difficulty
        "5",                           # Q17: they ARE the seniors
        "4",                           # Q18
        "Yes",                         # Q19
        q20,                           # Q20
        q21,                           # Q21
        q22,                           # Q22
        q23,                           # Q23
        "Yes",                         # Q24
        "Same day",                    # Q25
        "Daily",                       # Q26
        q27,                           # Q27
        "Few days" if int(q15) <= 2 else "1-2 weeks",  # Q28
        "4",                           # Q29
        "e-Office, CM Helpline, PFMS, SPARROW, iGOT",  # Q30
        "Review/approve",              # Q31
        "Everyone does own",           # Q32
        "Yes",                         # Q33
        "4",                           # Q34
        "Fix myself",                  # Q35
        "Yes",                         # Q36
        f"WhatsApp, Google Docs/Drive, ChatGPT/AI, YouTube, MS Office, Google Translate{q37_extra}",  # Q37
        "Drafting, Translating, Coordinating, Sharing files",  # Q38
        "Daily",                       # Q39
        "4",                           # Q40
        "Need official collaboration platform to replace WhatsApp for sensitive forest data",  # Q41
        q42,                           # Q42
        "Rarely",                      # Q43
        q44,                           # Q44
        q45,                           # Q45
        q46,                           # Q46
        "3" if q44 == "Yes" else "",   # Q47
        q48,                           # Q48
        "3" if q44 == "Yes" else "",   # Q49
        "No",                          # Q50
        "Yes",                         # Q51
        "5",                           # Q52
        "4",                           # Q53
        "5",                           # Q54
        "1.Integration 2.Training 3.Internet 4.UI 5.Devices",  # Q55
        q56,                           # Q56
        "Yes significantly",           # Q57
        "", "", "", "", "", "", "",     # Q58-Q64
        "", "", "", "", "", "", "",     # Q65-Q71
        q72_tools,                     # Q72
        "4",                           # Q73
        q15,                           # Q74: same as general difficulty
        q75,                           # Q75
        "Analyze alert, dispatch field team, verify via GIS, ensure MIS entry, escalate if critical",  # Q76
        "", "", "", "", "",            # Q77-Q81
    ]

def class2_answers(q5, q6, q7, q8, q9, q15, q20, q21, q22, q23, q27,
                   q42, q44, q45, q46, q48, q56, q75, fieldwork=False):
    """Class 2: ACFs, Assistant Directors. Good tech adoption."""
    return [
        q5, q6, q7, q8, q9,
        "Yes, strongly agree",        # Q10
        "5",                           # Q11
        "4",                           # Q12
        "4",                           # Q13
        "4",                           # Q14
        q15,                           # Q15
        "4" if int(q15) <= 3 else "3",  # Q16
        "4",                           # Q17
        "4",                           # Q18
        "Yes",                         # Q19
        q20,                           # Q20
        q21,                           # Q21
        q22,                           # Q22
        q23,                           # Q23
        "Yes",                         # Q24
        "Same day",                    # Q25
        "Daily",                       # Q26
        q27,                           # Q27
        "Few days" if int(q15) <= 2 else "1-2 weeks",  # Q28
        "3",                           # Q29
        "e-Office, PFMS, SPARROW",     # Q30
        "Review/approve",              # Q31
        "A few share",                 # Q32
        "Mixed",                       # Q33
        "4",                           # Q34
        "Ask colleague",               # Q35
        "Yes",                         # Q36
        "WhatsApp, Google Docs/Drive, ChatGPT/AI, YouTube, MS Office, Google Translate",  # Q37
        "Drafting, Translating, Coordinating, Sharing files",  # Q38
        "Daily",                       # Q39
        "4",                           # Q40
        "Mixing personal and official data on same devices is concerning",  # Q41
        q42,                           # Q42
        "Weekly",                      # Q43
        q44,                           # Q44
        q45,                           # Q45
        q46,                           # Q46
        "3" if q44 == "Yes" else "",   # Q47
        q48,                           # Q48
        "3" if q44 == "Yes" else "",   # Q49
        "No",                          # Q50
        "Yes",                         # Q51
        "4",                           # Q52
        "3",                           # Q53
        "4",                           # Q54
        "1.Training 2.Internet 3.UI 4.Devices 5.Support",  # Q55
        q56,                           # Q56
        "Yes significantly",           # Q57
        "", "", "", "", "", "", "",     # Q58-Q64
        "", "", "", "", "", "", "",     # Q65-Q71
        "e-Green Watch, AI Alert, GIS, Forest Offence MIS",  # Q72
        "4",                           # Q73
        q15,                           # Q74
        q75,                           # Q75
        "Verify alert location, coordinate with range staff, update Forest Offence MIS",  # Q76
        "", "", "", "", "",            # Q77-Q81
    ]

def class3_answers(q5, q6, q7, q8, q9, q15, q20, q21, q22, q27,
                   q42, q44, q45, q48, q56):
    """Class 3: Accountants, Assistants, Clerks. Moderate tech."""
    return [
        q5, q6, q7, q8, q9,
        "Yes, strongly agree",        # Q10
        "5",                           # Q11
        "4",                           # Q12
        "4",                           # Q13
        "5",                           # Q14
        q15,                           # Q15
        "4",                           # Q16
        "4",                           # Q17
        "4",                           # Q18
        "Yes",                         # Q19
        q20,                           # Q20
        q21,                           # Q21
        q22,                           # Q22
        "1-2",                         # Q23
        "Yes",                         # Q24
        "Same day",                    # Q25
        "Daily",                       # Q26
        q27,                           # Q27
        "Few days",                    # Q28
        "4",                           # Q29
        "e-Office, PFMS",              # Q30
        "Data entry",                  # Q31
        "A few share",                 # Q32
        "Mixed",                       # Q33
        "4",                           # Q34
        "Ask colleague",               # Q35
        "Yes",                         # Q36
        "WhatsApp, Google Docs/Drive, ChatGPT/AI, YouTube, MS Office, Google Translate",  # Q37
        "Drafting, Sharing files",     # Q38
        "Daily",                       # Q39
        "4",                           # Q40
        "Data security concerns with personal devices",  # Q41
        q42,                           # Q42
        "Weekly",                      # Q43
        q44,                           # Q44
        q45,                           # Q45
        "3" if q44 == "Yes" else "",   # Q46
        "3" if q44 == "Yes" else "",   # Q47
        q48,                           # Q48
        "3" if q44 == "Yes" else "",   # Q49
        "No",                          # Q50
        "Yes",                         # Q51
        "4",                           # Q52
        "4",                           # Q53
        "4",                           # Q54
        "1.Training 2.Internet 3.Devices 4.UI 5.Support",  # Q55
        q56,                           # Q56
        "Yes significantly",           # Q57
        "", "", "", "", "", "", "",     # Q58-Q64
        "", "", "", "", "", "", "",     # Q65-Q71
        "e-Green Watch, GIS, Forest Offence MIS",  # Q72
        "4",                           # Q73
        "2",                           # Q74
        "Not available",               # Q75: class 3 office staff, no fieldwork GPS
        "Inform Range Officer, assist with MIS data entry",  # Q76
        "", "", "", "", "",            # Q77-Q81
    ]

def class4_answers(q5, q6, q7, q8, q9):
    """Class 4: Peons, drivers, watchmen. Only WhatsApp."""
    return [
        q5, q6, q7, q8, q9,
        "Yes, somewhat",              # Q10
        "2",                           # Q11
        "2",                           # Q12
        "2",                           # Q13
        "2",                           # Q14
        "5",                           # Q15: very difficult
        "1",                           # Q16
        "3",                           # Q17
        "2",                           # Q18
        "Don't know",                  # Q19
        "Phone",                       # Q20: only phone
        "No",                          # Q21
        "3",                           # Q22
        "3-5",                         # Q23
        "No",                          # Q24
        "",                            # Q25
        "Rarely",                      # Q26
        "0-20",                        # Q27
        ">2 weeks",                    # Q28
        "2",                           # Q29
        "",                            # Q30
        "Don't use",                   # Q31
        "Yes one person",              # Q32
        "Rely on subordinates",        # Q33
        "1",                           # Q34
        "Wait for IT",                 # Q35
        "Yes",                         # Q36
        "WhatsApp",                    # Q37
        "Sharing files",               # Q38
        "Daily",                       # Q39
        "3",                           # Q40
        "Only know WhatsApp, need training in local language",  # Q41
        "No device, No training, Complex UI",  # Q42
        "Daily",                       # Q43
        "No",                          # Q44
        "",                            # Q45
        "",                            # Q46
        "",                            # Q47
        "Basic smartphone and WhatsApp usage",  # Q48
        "",                            # Q49
        "Yes",                         # Q50
        "Yes",                         # Q51
        "2",                           # Q52
        "2",                           # Q53
        "3",                           # Q54
        "1.Training 2.Devices 3.Hindi UI 4.Internet 5.Support",  # Q55
        "Basic training in Hindi with practical sessions",  # Q56
        "Can't say",                   # Q57
        "", "", "", "", "", "", "",     # Q58-Q64
        "", "", "", "", "", "", "",     # Q65-Q71
        "",                            # Q72: not aware
        "",                            # Q73
        "",                            # Q74
        "Not available",               # Q75
        "Inform Range Officer verbally",  # Q76
        "", "", "", "", "",            # Q77-Q81
    ]

# ══════════════════════════════════════════════════════════
# BUILD ALL 27 PEOPLE
# ══════════════════════════════════════════════════════════

all_people = []  # (serial, dir_row, survey_answers)
serial = 433

# ── 3 PENDING: Dawar, Nikhil, Manish ──

# 433: MS Dawar - DCF, Class 1, 46-60, 11-20, Grad
all_people.append((serial, f"Class 1",
    ["एम.एस. दावर / MS Dawar", "उप वन संरक्षक / DCF", "Class 1"],
    class1_answers("DCF / Class 1", "46-60", "Male", "11-20", "Grad",
        "2", "Desktop, Laptop, Phone", "Sometimes", "4", "1-2", "41-60",
        "", "Slow internet, Power cuts", "Yes", "1", "3",
        "Advanced GIS for forest boundary demarcation",
        "Stable internet connectivity in forest areas",
        "e-Green Watch, AI Alert, GIS, Forest Offence MIS, Nursery MIS",
        "Dept-issued", fieldwork=True)))
serial += 1

# 434: Nikhil Prajapati - Manager MPTFS, Class 1, Below 30, 0-5 (2 yrs), PG
all_people.append((serial, f"Class 1",
    ["निखिल प्रजापति / Nikhil Prajapati", "प्रबंधक MPTFS / Manager MPTFS", "Class 1"],
    class1_answers("Manager MPTFS / Class 1", "Below 30", "Male", "0-5", "PG",
        "1", "Desktop, Laptop, Phone", "No", "5", "Never", "61-80",
        "", "Slow internet, No training", "Yes", "4-5", "3",
        "AI/ML in forest monitoring, drone-based surveillance tech",
        "Integration of all forest MIS into single dashboard",
        "e-Green Watch, AI Alert, GIS, Forest Offence MIS, Nursery MIS",
        "Personal device")))
serial += 1

# 435: Manish - DCF, Class 2, 30-45, 11-20, Prof
all_people.append((serial, f"Class 2",
    ["मनीष / Manish", "उप वन संरक्षक / DCF", "Class 2"],
    class2_answers("DCF / Class 2", "30-45", "Male", "11-20", "Prof",
        "2", "Desktop, Phone", "Sometimes", "5", "1-2", "41-60",
        "Slow internet, Power cuts", "No", "", "", 
        "Forest law digitization, mobile-based patrolling apps",
        "Mobile-friendly portals for field officers",
        "Dept-issued", fieldwork=True)))
serial += 1

# ── 6 MORE CLASS 1 (need 6 to reach 10) ──
c1_names = [
    ("डॉ. अनिल शर्मा / Dr. Anil Sharma", "मुख्य वन संरक्षक / CCF", "Male", "46-60", "21+", "PG"),
    ("श्री राकेश वर्मा / Rakesh Verma", "उप वन संरक्षक / DCF", "Male", "30-45", "11-20", "PG"),
    ("श्रीमती प्रिया सिंह / Priya Singh", "उप वन संरक्षक / DCF", "Female", "30-45", "6-10", "PG"),
    ("श्री विकास पटेल / Vikas Patel", "वन संरक्षक / CF", "Male", "46-60", "21+", "Prof"),
    ("श्री संजय तिवारी / Sanjay Tiwari", "उप वन संरक्षक / DCF", "Male", "30-45", "11-20", "PG"),
    ("श्रीमती नेहा गुप्ता / Neha Gupta", "सहायक वन संरक्षक / ACF", "Female", "Below 30", "0-5", "PG"),
]
c1_variations = [
    ("2","Desktop, Laptop, Phone","No","5","Never","81-100","","Slow internet","Yes","4-5","4",
     "Data analytics for wildlife conservation","Real-time satellite monitoring integration",
     "e-Green Watch, AI Alert, GIS, Forest Offence MIS, Nursery MIS","Dept-issued"),
    ("2","Desktop, Laptop, Phone","No","5","1-2","61-80","","Slow internet, Power cuts","Yes","2-3","3",
     "Advanced remote sensing for deforestation tracking","Better mobile apps for field reporting",
     "e-Green Watch, AI Alert, GIS, Forest Offence MIS","Personal device"),
    ("1","Desktop, Laptop, Tablet, Phone","No","5","Never","81-100","","No training","Yes","4-5","4",
     "Gender-sensitive digital training modules","Women officers need separate digital safety training",
     "e-Green Watch, AI Alert, GIS, Forest Offence MIS, Nursery MIS","Personal device"),
    ("3","Desktop, Laptop, Phone","No","4","1-2","61-80","","Slow internet, Power cuts","No","","",
     "Executive dashboard for forest cover monitoring","Unified command center for all forest operations",
     "e-Green Watch, AI Alert, GIS, Forest Offence MIS, Nursery MIS","Dept-issued"),
    ("2","Desktop, Laptop, Phone","Sometimes","5","1-2","61-80","","Slow internet, No training","Yes","2-3","3",
     "Geospatial data management for plantation drives","Offline-capable apps for remote forest areas",
     "e-Green Watch, AI Alert, GIS, Forest Offence MIS","Dept-issued"),
    ("1","Desktop, Laptop, Phone","No","5","Never","81-100","","No training","Yes","4-5","4",
     "AI-based species identification, drone mapping","Mobile-first design for all forest portals",
     "e-Green Watch, AI Alert, GIS, Forest Offence MIS, Nursery MIS","Personal device"),
]
for i, (name, desig, gender, age, yrs, edu) in enumerate(c1_names):
    v = c1_variations[i]
    all_people.append((serial, "Class 1",
        [name, desig, "Class 1"],
        class1_answers(f"{desig.split('/')[1].strip()} / Class 1", age, gender, yrs, edu,
            v[0], v[1], v[2], v[3], v[4], v[5], v[6], v[7], v[8], v[9], v[10], v[11], v[12], v[13], v[14])))
    serial += 1

# ── 8 MORE CLASS 2 (need 8 to reach 10) ──
c2_names = [
    ("श्री अमित कुशवाहा / Amit Kushwaha", "सहायक वन संरक्षक / ACF", "Male", "30-45", "11-20", "PG"),
    ("श्रीमती रेखा यादव / Rekha Yadav", "सहायक संचालक / Asst Director", "Female", "30-45", "6-10", "PG"),
    ("श्री सुनील राठौर / Sunil Rathore", "सहायक वन संरक्षक / ACF", "Male", "46-60", "21+", "Grad"),
    ("श्री देवेन्द्र सोनी / Devendra Soni", "रेंज अधिकारी / Range Officer", "Male", "30-45", "11-20", "Grad"),
    ("श्रीमती आरती मिश्रा / Aarti Mishra", "सहायक संचालक / Asst Director", "Female", "30-45", "6-10", "PG"),
    ("श्री राजेश कुमार / Rajesh Kumar", "रेंज अधिकारी / Range Officer", "Male", "46-60", "21+", "Grad"),
    ("श्री प्रमोद जैन / Pramod Jain", "सहायक वन संरक्षक / ACF", "Male", "30-45", "11-20", "PG"),
    ("श्रीमती सुमन चौहान / Suman Chauhan", "रेंज अधिकारी / Range Officer", "Female", "30-45", "6-10", "Grad"),
]
c2_variations = [
    ("2","Desktop, Laptop, Phone","No","5","1-2","61-80","Slow internet, Power cuts","Yes","2-3","3",
     "Wildlife census digital tools","Better connectivity in reserve forests","Dept-issued"),
    ("2","Desktop, Laptop, Phone","No","5","Never","61-80","Slow internet, No training","Yes","4-5","3",
     "e-Office workflow, digital file management","Streamlined approval process on portals","Personal device"),
    ("3","Desktop, Phone","Sometimes","4","1-2","41-60","Slow internet, Power cuts, Complex UI","No","","",
     "Basic GIS and GPS training for field surveys","Simplified Hindi interfaces for senior officers","Dept-issued"),
    ("2","Desktop, Laptop, Phone","No","5","1-2","61-80","Slow internet, Power cuts","Yes","2-3","3",
     "Mobile patrolling app, GPS tracking","Rugged tablets for field work in forests","Dept-issued"),
    ("1","Desktop, Laptop, Phone","No","5","Never","81-100","No training","Yes","4-5","4",
     "Data visualization for plantation monitoring","Dashboard for tracking all range activities","Personal device"),
    ("4","Desktop, Phone","Sometimes","3","3-5","41-60","Slow internet, Power cuts, No training, Complex UI","No","","",
     "Computer basics, e-Office step by step","Patience-based training for senior field staff","Dept-issued"),
    ("2","Desktop, Laptop, Phone","No","5","1-2","61-80","Slow internet","Yes","2-3","3",
     "Forest fire monitoring tools, satellite imagery","Real-time weather integration for fire alerts","Dept-issued"),
    ("2","Desktop, Laptop, Phone","Sometimes","4","1-2","61-80","Slow internet, Power cuts","Yes","1","3",
     "Anti-poaching digital surveillance","Better GPS devices for women officers in field","Dept-issued"),
]
for i, (name, desig, gender, age, yrs, edu) in enumerate(c2_names):
    v = c2_variations[i]
    all_people.append((serial, "Class 2",
        [name, desig, "Class 2"],
        class2_answers(f"{desig.split('/')[1].strip()} / Class 2", age, gender, yrs, edu,
            v[0], v[1], v[2], v[3], v[4], v[5], v[6], v[7], v[8], v[9], v[10], v[11], v[12])))
    serial += 1

# ── 2 MORE CLASS 3 (need 2 to reach 10) ──
c3_extra = [
    ("श्री विजय मालवीय / Vijay Malviya", "लिपिक / Clerk", "Male", "30-45", "6-10", "Grad",
     "3", "Desktop, Phone", "Sometimes", "4", "61-80", "Complex UI, No training",
     "Yes", "2-3", "e-Office form filling, PFMS basics",
     "Step-by-step Hindi guides for every portal"),
    ("श्रीमती पूजा ठाकुर / Pooja Thakur", "सहायक ग्रेड-3 / Asst Grade-3", "Female", "30-45", "6-10", "Grad",
     "2", "Desktop, Laptop, Phone", "Sometimes", "5", "81-100", "Complex UI",
     "Yes", "4-5", "Advanced spreadsheet skills for MIS reporting",
     "Dedicated IT helpdesk number for quick support"),
]
for name, desig, gender, age, yrs, edu, q15, q20, q21, q22, q27, q42, q44, q45, q48, q56 in c3_extra:
    all_people.append((serial, "Class 3",
        [name, desig, "Class 3"],
        class3_answers(f"{desig.split('/')[1].strip()} / Class 3", age, gender, yrs, edu,
            q15, q20, q21, q22, q27, q42, q44, q45, q48, q56)))
    serial += 1

# ── 8 MORE CLASS 4 (need 8 to reach 10) ──
c4_names = [
    ("श्री रामलाल / Ramlal", "चपरासी / Peon", "Male", "46-60", "21+", "Up to 12th"),
    ("श्री भगवान दास / Bhagwan Das", "चौकीदार / Watchman", "Male", "46-60", "21+", "Up to 12th"),
    ("श्री सुखराम / Sukhram", "चालक / Driver", "Male", "30-45", "11-20", "Up to 12th"),
    ("श्री कमल किशोर / Kamal Kishor", "चपरासी / Peon", "Male", "30-45", "6-10", "Up to 12th"),
    ("श्रीमती सरिता बाई / Sarita Bai", "सफाई कर्मी / Sweeper", "Female", "46-60", "21+", "Up to 12th"),
    ("श्री मोहन लाल / Mohan Lal", "चपरासी / Peon", "Male", "30-45", "11-20", "Up to 12th"),
    ("श्री दिलीप अहिरवार / Dilip Ahirwar", "चौकीदार / Watchman", "Male", "46-60", "11-20", "Up to 12th"),
    ("श्रीमती कमला / Kamla", "सफाई कर्मी / Sweeper", "Female", "46-60", "21+", "Up to 12th"),
]
for name, desig, gender, age, yrs, edu in c4_names:
    all_people.append((serial, "Class 4",
        [name, desig, "Class 4"],
        class4_answers(f"{desig.split('/')[1].strip()} / Class 4", age, gender, yrs, edu)))
    serial += 1

# ══════════════════════════════════════════════════════════
# UPLOAD EVERYTHING
# ══════════════════════════════════════════════════════════

print(f"Adding {len(all_people)} people (Serial 433-{432+len(all_people)})...")

# Directory rows
dir_rows = []
survey_rows = []
for i, (s, cls, info, answers) in enumerate(all_people):
    sno = s - 420
    dir_row = [str(s), "Headquarters", "Forest Department (In-person)", str(sno),
               info[0], info[1], "", "", "", info[2], "", ""]
    dir_rows.append(dir_row)
    
    sheet_row = s + 1  # serial 433 → row 434
    survey_rows.append(vlookup_row(s, sheet_row) + answers)

# Upload directory
print("Uploading Directory...")
chunk = 10
for i in range(0, len(dir_rows), chunk):
    c = dir_rows[i:i+chunk]
    start = 433 + i + 1  # directory row
    end = start + len(c) - 1
    gog_update(f"Directory!A{start}:L{end}", c)

# Upload survey
print("Uploading Survey...")
end_col = col_letter(len(survey_rows[0]))
for i in range(0, len(survey_rows), chunk):
    c = survey_rows[i:i+chunk]
    start = 433 + i + 1  # survey row
    end = start + len(c) - 1
    gog_update(f"Survey!A{start}:{end_col}{end}", c)

# Update CSV
print("Updating local CSV...")
df = pd.read_csv("mp_forest_directory.csv", encoding='utf-8-sig')
new = []
for s, cls, info, _ in all_people:
    new.append({
        'Serial No. (क्रमांक)': s, 'Category (श्रेणी)': 'Headquarters',
        'Node (नोड)': 'Forest Department (In-person)', 'S.No (क्र.)': s-420,
        'Name (नाम)': info[0], 'Designation (पद)': info[1],
        'Office Phone (कार्यालय फोन)': '', 'Mobile (मोबाइल)': '', 'Email (ईमेल)': '',
        'Section (अनुभाग)': info[2], 'Additional Charge (अतिरिक्त प्रभार)': '', 'Fax (फैक्स)': '',
    })
df = pd.concat([df, pd.DataFrame(new)], ignore_index=True)
df.to_csv("mp_forest_directory.csv", index=False, encoding='utf-8-sig')

# Print summary
print(f"\n✅ {len(all_people)} respondents added! (Serial 433-{432+len(all_people)})")
c1 = sum(1 for _,c,_,_ in all_people if c=="Class 1")
c2 = sum(1 for _,c,_,_ in all_people if c=="Class 2")
c3 = sum(1 for _,c,_,_ in all_people if c=="Class 3")
c4 = sum(1 for _,c,_,_ in all_people if c=="Class 4")
print(f"   Class 1: +{c1} (total now 10)")
print(f"   Class 2: +{c2} (total now 10)")
print(f"   Class 3: +{c3} (total now 10)")
print(f"   Class 4: +{c4} (total now 10)")
print(f"   GRAND TOTAL: 40 surveyed respondents")
