"""
Populate the Google Sheet with:
  Tab 1 "Directory" — full directory data with serial numbers
  Tab 2 "Survey" — linked to Directory via VLOOKUP formulas
Uses temp files to avoid command-line length limits.
"""
import subprocess, json, csv, os, tempfile

GOG = r"C:\Users\aryan\.gemini\antigravity\bin\gog.exe"
ACCOUNT = "aryan.kori14@gmail.com"
SHEET_ID = "1Q_X8OTiHkprn0cZScoxX8JPjA6IynLASUMDyGrDXlk4"

def gog(*args):
    cmd = [GOG, "--account", ACCOUNT, "--no-input", "--json"] + list(args)
    r = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
    if r.returncode != 0:
        print(f"  ERROR: {r.stderr[:200]}")
    return r.stdout

def gog_update(range_str, values):
    """Update a range using a temp file to avoid command-line length limits."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False, encoding='utf-8') as f:
        json.dump(values, f, ensure_ascii=False)
        tmp_path = f.name
    try:
        cmd = [GOG, "--account", ACCOUNT, "--no-input", "--json",
               "sheets", "update", SHEET_ID, range_str,
               "--values-json-file", tmp_path]
        r = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
        if r.returncode != 0:
            # Fallback: try --values-json with the data directly
            # But first check if the tool supports --values-json-file
            # If not, write smaller chunks
            print(f"  Trying direct approach for {range_str}...")
            val_json = json.dumps(values, ensure_ascii=False)
            cmd2 = [GOG, "--account", ACCOUNT, "--no-input", "--json",
                    "sheets", "update", SHEET_ID, range_str,
                    "--values-json", val_json]
            r2 = subprocess.run(cmd2, capture_output=True, text=True, encoding='utf-8')
            if r2.returncode != 0:
                print(f"  ERROR: {r2.stderr[:300]}")
            else:
                print(f"  ✅ {range_str}")
        else:
            print(f"  ✅ {range_str}")
    finally:
        os.unlink(tmp_path)

def col_letter(n):
    s = ""
    while n > 0:
        n, r = divmod(n - 1, 26)
        s = chr(65 + r) + s
    return s

# ── Step 1: Rename default tab, add Survey tab ──
print("Setting up tabs...")
gog("sheets", "rename-tab", SHEET_ID, "Sheet1", "Directory")
gog("sheets", "add-tab", SHEET_ID, "Survey")

# ── Step 2: Load CSV ──
print("Loading directory CSV...")
with open("mp_forest_directory.csv", encoding="utf-8-sig") as f:
    rows = list(csv.reader(f))
headers = rows[0]
data_rows = rows[1:]
total = len(data_rows)
print(f"  {total} entries")

# ── Step 3: Upload Directory data row-by-row in small chunks ──
print("Uploading Directory data...")
chunk_size = 20  # small chunks to avoid command line limits
all_rows = [headers] + data_rows
for i in range(0, len(all_rows), chunk_size):
    chunk = all_rows[i:i+chunk_size]
    start = i + 1
    end = start + len(chunk) - 1
    gog_update(f"Directory!A{start}:L{end}", chunk)

# ── Step 4: Build Survey header ──
print("Building Survey headers...")

q_headers = [
    "Q5: Job Role/Level", "Q6: Age [Below 30|30-45|46-60]", "Q7: Gender [M|F|Other]",
    "Q8: Service yrs [0-5|6-10|11-20|21+]", "Q9: Education [12th|Grad|PG|Prof]",
    "Q10: Adopt digital? [5 opts]", "Q11: Faster than paper [1-5]", "Q12: Improve quality [1-5]",
    "Q13: Increase productivity [1-5]", "Q14: Suited to job [1-5]", "Q15: Difficulty [1-5]",
    "Q16: Confident [1-5]", "Q17: Superiors encourage [1-5]", "Q18: Colleagues use [1-5]",
    "Q19: Mandate? [Y/N/DK]", "Q20: Devices [multi]", "Q21: Share? [3 opts]",
    "Q22: Internet [1-5]", "Q23: Outages [4 opts]", "Q24: Helpdesk? [Y/N]",
    "Q25: Resolution [4 opts]", "Q26: How often? [5 opts]", "Q27: % digital [5 opts]",
    "Q28: Learn time [4 opts]", "Q29: UI friendly [1-5]", "Q30: General tools [multi]",
    "Q31: Primary role [5 opts]", "Q32: One person? [4 opts]", "Q33: Seniors use? [4 opts]",
    "Q34: Changed work [1-5]", "Q35: Error action [6 opts]", "Q36: Non-govt apps? [Y/N]",
    "Q37: Which tools [multi]", "Q38: Used for [multi]", "Q39: How often personal [5 opts]",
    "Q40: Fill gap [1-5]", "Q41: Concerns [text]", "Q42: Issues [multi]",
    "Q43: Disrupt freq [5 opts]", "Q44: Training? [Y/N]", "Q45: Sessions [4 opts]",
    "Q46: Quality [1-5]", "Q47: Sufficient [1-5]", "Q48: Topics [text]",
    "Q49: For role [1-5]", "Q50: Beyond skill? [Y/N]", "Q51: By level? [3 opts]",
    "Q52: Ask help [1-5]", "Q53: Org support [1-5]", "Q54: Committed [1-5]",
    "Q55: Priorities [text]", "Q56: One change [text]",
    "Q57: Citizen service [5 opts]",
    "Q58: Rev tools [multi]", "Q59: Bhulekh [1-5]", "Q60: RCMS [1-5]",
    "Q61: Paper% [5 opts]", "Q62: Citizens expect [1-5]", "Q63: Mutation [text]",
    "Q64: SAMPADA [1-5]",
    "Q65: Rural tools [multi]", "Q66: Multi portal [1-5]", "Q67: Block internet [1-5]",
    "Q68: NMMS [1-5]", "Q69: Data entry time [5 opts]", "Q70: Muster steps [text]",
    "Q71: Portal down [6 opts]",
    "Q72: Forest tools [multi]", "Q73: AI alert [1-5]", "Q74: GIS difficulty [1-5]",
    "Q75: GPS device [3 opts]", "Q76: AI alert action [text]",
    "Q77: Health tools [multi]", "Q78: ANMOL/ABHA [1-5]", "Q79: IHIP workload [1-5]",
    "Q80: ANC steps [text]", "Q81: Outbreak report [text]",
]

# Fixed columns + Q1-Q4 (linked) + Q5-Q81
header_row = [
    "Serial No.", "Name ← linked", "Designation ← linked", "Category ← linked",
    "Node ← linked", "Mobile ← linked", "Email ← linked",
    "Q1: Name [linked]", "Q2: Designation [linked]", "Q3: Mobile [linked]", "Q4: Email [linked]",
] + q_headers

total_cols = len(header_row)
end_col = col_letter(total_cols)
gog_update(f"Survey!A1:{end_col}1", [header_row])

# ── Step 5: Build linked rows ──
print("Building VLOOKUP-linked survey rows...")
survey_rows = []
for i in range(1, total + 1):
    r = i + 1  # row in sheet (row 1 = header)
    row = [
        str(i),
        f'=VLOOKUP(A{r},Directory!A:L,5,FALSE)',  # Name
        f'=VLOOKUP(A{r},Directory!A:L,6,FALSE)',  # Designation
        f'=VLOOKUP(A{r},Directory!A:L,2,FALSE)',  # Category
        f'=VLOOKUP(A{r},Directory!A:L,3,FALSE)',  # Node
        f'=VLOOKUP(A{r},Directory!A:L,8,FALSE)',  # Mobile
        f'=VLOOKUP(A{r},Directory!A:L,9,FALSE)',  # Email
        f'=VLOOKUP($A{r},Directory!$A:$L,5,FALSE)', # Q1 Name
        f'=VLOOKUP($A{r},Directory!$A:$L,6,FALSE)', # Q2 Designation
        f'=VLOOKUP($A{r},Directory!$A:$L,8,FALSE)', # Q3 Mobile
        f'=VLOOKUP($A{r},Directory!$A:$L,9,FALSE)', # Q4 Email
    ]
    row += [""] * len(q_headers)  # Q5-Q81 empty for data entry
    survey_rows.append(row)

# Upload survey rows in chunks
for i in range(0, len(survey_rows), chunk_size):
    chunk = survey_rows[i:i+chunk_size]
    start = i + 2  # data starts at row 2
    end = start + len(chunk) - 1
    gog_update(f"Survey!A{start}:{end_col}{end}", chunk)

# ── Step 6: Formatting ──
print("Formatting...")
gog("sheets", "freeze", SHEET_ID, "--sheet", "Survey", "--rows", "1", "--cols", "7")
gog("sheets", "freeze", SHEET_ID, "--sheet", "Directory", "--rows", "1", "--cols", "1")
gog("sheets", "format", SHEET_ID, "Directory!A1:L1", "--bold")
gog("sheets", "format", SHEET_ID, f"Survey!A1:{end_col}1", "--bold", "--wrap")

print(f"\n🎉 Done! Your linked Google Sheet:")
print(f"   https://docs.google.com/spreadsheets/d/{SHEET_ID}/edit")
print(f"   Directory: {total} entries | Survey: {total} rows × {total_cols} columns")
print(f"   VLOOKUP formulas link Survey → Directory by Serial No.")
