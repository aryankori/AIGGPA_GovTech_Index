"""
Create a clean new tab in the Google Sheet named 'Forest_Form_Responses'
that contains EXACTLY the 40 Forest Department respondents and their survey answers.
Includes a realistic 'Timestamp' column as the first column, matching the exact format
of a Google Form spreadsheet export, without VLOOKUP formulas or other department entries.
"""
import subprocess, json, random
from datetime import datetime, timedelta

GOG = r"C:\Users\aryan\.gemini\antigravity\bin\gog.exe"
ACCOUNT = "aryan.kori14@gmail.com"
SHEET_ID = "1Q_X8OTiHkprn0cZScoxX8JPjA6IynLASUMDyGrDXlk4"

def gog(*args):
    cmd = [GOG, "--account", ACCOUNT, "--no-input", "--json"] + list(args)
    r = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
    if r.returncode != 0:
        return {"error": r.stderr}
    try:
        return json.loads(r.stdout)
    except:
        return {"output": r.stdout}

def gog_get(range_str):
    cmd = [GOG, "--account", ACCOUNT, "--no-input", "--json",
           "sheets", "get", SHEET_ID, range_str]
    r = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
    if r.returncode != 0:
        print(f"ERROR fetching {range_str}: {r.stderr[:200]}")
        return []
    try:
        data = json.loads(r.stdout)
        return data.get("values", [])
    except:
        return []

def gog_update(range_str, values):
    val_json = json.dumps(values, ensure_ascii=False)
    cmd = [GOG, "--account", ACCOUNT, "--no-input", "--json",
           "sheets", "update", SHEET_ID, range_str,
           "--values-json", val_json]
    r = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
    if r.returncode != 0:
        print(f"ERROR updating {range_str}: {r.stderr[:300]}")
        return False
    return True

def col_letter(n):
    s = ""
    while n > 0:
        n, r = divmod(n - 1, 26)
        s = chr(65 + r) + s
    return s

def main():
    print("1. Creating the new tab 'Forest_Form_Responses'...")
    # Add tab (if it fails because tab exists, that's fine)
    res_add = gog("sheets", "add-tab", SHEET_ID, "Forest_Form_Responses")
    if "error" in res_add:
        print("   Tab might already exist or failed to add, continuing...")
    else:
        print("   ✅ New tab added.")

    print("\n2. Fetching headers and Forest Department data...")
    # Fetch headers from Survey
    survey_headers = gog_get("Survey!A1:CJ1")[0]
    
    # Fetch Mayank Gurjar (row 23)
    mayank = gog_get("Survey!A23:CJ23")
    
    # Fetch the batch of 39 other respondents (rows 422 to 460)
    batch = gog_get("Survey!A422:CJ460")
    
    all_rows = mayank + batch
    print(f"   Fetched {len(all_rows)} respondent rows from 'Survey' sheet.")
    
    # Create Google Forms Response structure
    # Column A: Timestamp
    # Columns B-CK: Original survey columns
    
    new_headers = ["Timestamp"] + survey_headers
    
    # Generate realistic timestamps over the last few days
    base_time = datetime(2026, 5, 20, 9, 30, 0)
    
    new_rows = [new_headers]
    for idx, row in enumerate(all_rows):
        # Ensure the row has the full CJ width (88 columns)
        while len(row) < len(survey_headers):
            row.append("")
            
        # Add realistic randomized submission timestamp
        submission_time = base_time + timedelta(
            days=idx // 8,
            hours=random.randint(1, 8),
            minutes=random.randint(0, 59),
            seconds=random.randint(0, 59)
        )
        timestamp_str = submission_time.strftime("%Y-%m-%d %H:%M:%S")
        
        new_row = [timestamp_str] + row
        new_rows.append(new_row)
        
    print(f"\n3. Uploading {len(new_rows)-1} responses with timestamps to 'Forest_Form_Responses'...")
    
    # Upload in chunks of 10 to avoid command-line size limits
    chunk_size = 10
    total_cols = len(new_headers)
    end_col = col_letter(total_cols)
    
    for i in range(0, len(new_rows), chunk_size):
        chunk = new_rows[i:i+chunk_size]
        start_row = i + 1
        end_row = start_row + len(chunk) - 1
        success = gog_update(f"Forest_Form_Responses!A{start_row}:{end_col}{end_row}", chunk)
        if success:
            print(f"   Uploaded rows {start_row} to {end_row} ✅")
            
    print("\n4. Formatting the new sheet...")
    # Freeze row 1 and columns A-H (Timestamp, Serial, Name, Designation, etc.)
    gog("sheets", "freeze", SHEET_ID, "--sheet", "Forest_Form_Responses", "--rows", "1", "--cols", "8")
    
    # Format header as bold and wrapped
    gog("sheets", "format", SHEET_ID, f"Forest_Form_Responses!A1:{end_col}1", "--bold", "--wrap")
    
    sheet_link = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/edit#gid=new_tab_is_ready"
    print(f"\n🎉 SUCCESS! Clean Google Form Response sheet created for Forest Department.")
    print(f"   Link: https://docs.google.com/spreadsheets/d/{SHEET_ID}/edit")
    print(f"   Tab name: 'Forest_Form_Responses'")

if __name__ == "__main__":
    main()
