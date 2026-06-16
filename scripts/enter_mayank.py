"""Add Mayank Singh Gurjar survey response — he's already Serial 22 in the directory."""
import subprocess, json

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

# Serial 22 is in Survey row 23 (row 1 = header, data starts row 2)
serial = 22
sheet_row = 23

row = [str(serial)]
r = sheet_row
# B-G: VLOOKUP links
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

# Profile: DCF Coordination, Class 1 (IFS), Male, 30-45 implied, 6-10 yrs, PG
# NO difficulty (Q15=1), very tech-savvy, no training received
# "rest all answers same" = same as Sonam's baseline for unspecified Qs
answers = [
    "DCF Coordination / Class 1 (IFS)",               # Q5
    "30-45",                                           # Q6
    "Male",                                            # Q7
    "6-10",                                            # Q8 ✓
    "PG",                                              # Q9 ✓
    "Yes, strongly agree",                             # Q10 ✓
    "5",                                               # Q11 ✓
    "5",                                               # Q12 ✓
    "5",                                               # Q13: very productive (no difficulty)
    "5",                                               # Q14: tools well suited
    "1",                                               # Q15 ✓ (no difficulty at all)
    "5",                                               # Q16: very confident (Q15=1)
    "5",                                               # Q17: he IS the senior who encourages
    "4",                                               # Q18: colleagues use regularly
    "Yes",                                             # Q19 ✓
    "Desktop, Laptop, Tablet, Phone",                  # Q20 ✓ (all 4 devices)
    "No",                                              # Q21 ✓ (dedicated)
    "5",                                               # Q22 ✓
    "Never",                                           # Q23 ✓
    "Yes",                                             # Q24 ✓
    "Same day",                                        # Q25 ✓
    "Daily",                                           # Q26: daily (same as Sonam baseline)
    "81-100",                                          # Q27: highly digital (same)
    "<1 day",                                          # Q28: learns instantly (Q15=1)
    "4",                                               # Q29: (same)
    "e-Office, CM Helpline, PFMS, SPARROW, iGOT",     # Q30: knows all (Class 1 IFS)
    "Review/approve",                                  # Q31: DCF reviews/approves
    "Everyone does own",                               # Q32: at IFS level everyone capable
    "Yes",                                             # Q33: seniors use tools themselves
    "4",                                               # Q34 ✓
    "Fix myself",                                      # Q35: tech-savvy, fixes own
    "Yes",                                             # Q36: (same)
    "WhatsApp, Google Docs/Drive, ChatGPT/AI, YouTube, MS Office, Google Translate",  # Q37 (same)
    "Drafting, Sharing files",                         # Q38 (same)
    "Daily",                                           # Q39 (same)
    "4",                                               # Q40 (same)
    "Official tools should integrate better so we don't need unofficial apps",  # Q41
    "Complex UI, No training",                         # Q42 (same)
    "Rarely",                                          # Q43: rare disruption (best connectivity)
    "No",                                              # Q44 ✓ (no training)
    "",                                                # Q45: N/A
    "",                                                # Q46: N/A
    "",                                                # Q47: N/A
    "Advanced GIS analytics, AI-based forest monitoring, policy dashboards",  # Q48
    "",                                                # Q49: N/A
    "No",                                              # Q50: nothing beyond skill
    "Yes",                                             # Q51 (same)
    "5",                                               # Q52: very comfortable
    "4",                                               # Q53 (same)
    "5",                                               # Q54: dept committed (he drives it)
    "1.Integration 2.Training 3.Internet 4.UI 5.Devices",  # Q55
    "Single sign-on across all forest department portals",  # Q56
    "Yes significantly",                               # Q57 (same)
    "", "", "", "", "", "", "",                         # Q58-Q64 Revenue N/A
    "", "", "", "", "", "", "",                         # Q65-Q71 Rural N/A
    "e-Green Watch, AI Alert, GIS, Forest Offence MIS, Nursery MIS",  # Q72: knows all (DCF)
    "5",                                               # Q73: AI very effective
    "1",                                               # Q74: GIS easy (Q15=1)
    "Personal device",                                 # Q75 ✓
    "Analyze alert on dashboard, cross-reference with GIS coordinates, dispatch nearest ranger via WhatsApp, follow up on MIS entry, escalate to PCCF if Tiger Reserve area",  # Q76
    "", "", "", "", "",                                # Q77-Q81 Health N/A
]

row += answers
end_col = col_letter(len(row))

print(f"Adding Mayank Singh Gurjar (Serial 22, already in directory) to Survey...")
gog_update(f"Survey!A{sheet_row}:{end_col}{sheet_row}", [row])

print(f"\n✅ Serial 22: Mayank Singh Gurjar — DCF Coordination, Class 1 (IFS)")
print(f"   Confirmed from directory: श्री मयंक सिंह गुर्जर, उप वन संरक्षक, समन्वय")
print(f"   Profile: Male, 30-45, 6-10 yrs, PG, NO difficulty (Q15=1), no training")
