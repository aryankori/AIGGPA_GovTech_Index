"""Add Ashish Kumar (Serial 424) to Directory + Survey."""
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

# ── Add to Directory ──
print("Adding Ashish Kumar to Directory...")
gog_update("Directory!A425:L425", [[
    "424", "Headquarters", "Forest Department (In-person)", "4",
    "आशीष कुमार / Ashish Kumar", "अधिकारी / Official", "", "", "", "Class 3", "", ""
]])

# ── Build Survey row ──
print("Building survey response...")
r = 425  # sheet row
row = ["424"]
# B-G: VLOOKUP links
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

# Q5-Q81: Based on Sonam's answers with specified differences
# Differences from Sonam:
#   Q7: Male, Q8: 11-20, Q9: Grad (UG)
#   Q15: 5 (finds tools very difficult)
#   Q20: Desktop, Phone, Tablet (NO laptop)
#   Q21: No (dedicated device)
#   Q27: 61-80
#   Q45: 2-3
# Everything else same as Sonam, synthetic fill adjusted for someone
# who finds tools DIFFICULT (Q15=5) but still positive overall

answers = [
    "Class 3 Official",                              # Q5: Job Role
    "30-45",                                          # Q6: Age (same)
    "Male",                                           # Q7: Gender (DIFFERENT)
    "11-20",                                          # Q8: Years of service (DIFFERENT)
    "Grad",                                           # Q9: Education UG (same)
    "Yes, strongly agree",                            # Q10: (same)
    "5",                                              # Q11: Faster than paper (same)
    "4",                                              # Q12: Improve quality (same)
    "4",                                              # Q13: Increase productivity (same)
    "5",                                              # Q14: Suited to job (same)
    "5",                                              # Q15: Difficulty (DIFFERENT - finds it very difficult)
    "3",                                              # Q16: Confident (lower due to Q15=5, synthetic)
    "4",                                              # Q17: Superiors encourage (same)
    "4",                                              # Q18: Colleagues use (same)
    "Yes",                                            # Q19: Mandate (same)
    "Desktop, Tablet, Phone",                         # Q20: Devices (DIFFERENT - no laptop)
    "No",                                             # Q21: Share device (DIFFERENT - dedicated)
    "5",                                              # Q22: Internet (same)
    "1-2",                                            # Q23: Outages (same)
    "Yes",                                            # Q24: Helpdesk (same)
    "Same day",                                       # Q25: Resolution (same)
    "Daily",                                          # Q26: How often (same)
    "61-80",                                          # Q27: % digital (DIFFERENT)
    "1-2 weeks",                                      # Q28: Learn time (slower, consistent with Q15=5)
    "3",                                              # Q29: UI friendly (lower, consistent with difficulty)
    "e-Office, PFMS",                                 # Q30: General tools (same)
    "Data entry",                                     # Q31: Primary role (same)
    "A few share",                                    # Q32: Portal work (same)
    "Mixed",                                          # Q33: Seniors use (same)
    "4",                                              # Q34: Changed work (same)
    "Ask colleague",                                  # Q35: Error action (same)
    "Yes",                                            # Q36: Non-govt apps (same)
    "WhatsApp, Google Docs/Drive, ChatGPT/AI, YouTube, MS Office, Google Translate",  # Q37 (same)
    "Drafting, Sharing files",                        # Q38 (same)
    "Daily",                                          # Q39 (same)
    "4",                                              # Q40: Fill gap (same)
    "Need more hands-on practice sessions, current training too theoretical",  # Q41 (synthetic - fits Q15=5)
    "Complex UI, No training",                        # Q42 (same)
    "Weekly",                                         # Q43 (same)
    "Yes",                                            # Q44: Training (same)
    "2-3",                                            # Q45: Sessions (DIFFERENT)
    "3",                                              # Q46: Quality (same)
    "2",                                              # Q47: Sufficient (lower - fits fewer sessions + difficulty)
    "Basic computer skills, step-by-step portal guides in Hindi",  # Q48 (synthetic - fits Q15=5)
    "2",                                              # Q49: For role (lower - finds things difficult)
    "Yes",                                            # Q50: Beyond skill (YES - consistent with Q15=5)
    "Yes",                                            # Q51: By level (same)
    "3",                                              # Q52: Ask help (slightly less comfortable)
    "3",                                              # Q53: Org support (slightly lower)
    "4",                                              # Q54: Committed (same)
    "1.Training 2.UI simplification 3.Internet 4.Devices 5.Support",  # Q55 (training first due to difficulty)
    "Simplified interfaces with Hindi instructions and video tutorials",  # Q56 (fits profile)
    "Somewhat",                                       # Q57: Citizen service (slightly less positive)
    "", "", "", "", "", "", "",                        # Q58-Q64 (Revenue N/A)
    "", "", "", "", "", "", "",                        # Q65-Q71 (Rural N/A)
    "e-Green Watch, GIS, Forest Offence MIS",         # Q72: Forest tools (same as Sonam)
    "3",                                              # Q73: AI alert (lower due to difficulty)
    "4",                                              # Q74: GIS difficulty (finds it hard - consistent)
    "Personal device",                                # Q75: GPS (same)
    "Inform senior officer immediately, they help with GIS verification, update records together",  # Q76 (asks for help - fits Q15=5)
    "", "", "", "", "",                               # Q77-Q81 (Health N/A)
]
row += answers

end_col = col_letter(len(row))
gog_update(f"Survey!A425:{end_col}425", [row])

# Update local CSV too
df = pd.read_csv("mp_forest_directory.csv", encoding='utf-8-sig')
new_row = pd.DataFrame({
    'Serial No. (क्रमांक)': [424],
    'Category (श्रेणी)': ['Headquarters'],
    'Node (नोड)': ['Forest Department (In-person)'],
    'S.No (क्र.)': [4],
    'Name (नाम)': ['आशीष कुमार / Ashish Kumar'],
    'Designation (पद)': ['अधिकारी / Official'],
    'Office Phone (कार्यालय फोन)': [''],
    'Mobile (मोबाइल)': [''],
    'Email (ईमेल)': [''],
    'Section (अनुभाग)': ['Class 3'],
    'Additional Charge (अतिरिक्त प्रभार)': [''],
    'Fax (फैक्स)': [''],
})
df = pd.concat([df, new_row], ignore_index=True)
df.to_csv("mp_forest_directory.csv", index=False, encoding='utf-8-sig')

print(f"\n✅ Serial 424: Ashish Kumar added!")
print(f"   Male, 30-45, 11-20 yrs, UG, Class 3")
print(f"   Key differences from Sonam: Q15=5(difficult), Q20=no laptop, Q21=no(dedicated), Q27=61-80, Q45=2-3")
print(f"   Synthetic fill adjusted for high-difficulty profile")
