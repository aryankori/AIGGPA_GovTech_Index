import pandas as pd
import subprocess, json, os

GOG = r"C:\Users\aryan\.gemini\antigravity\bin\gog.exe"
ACC = "aryan.kori14@gmail.com"
SHEET_ID = "1UsK7mHAUM3DNTJ-CkeU5OLVKjhMrft4UDy1Cx-aBBkU"
LOCAL_TRACKER = r"C:\Users\aryan\OneDrive\Documents\Visual Studio 2022\AIGGPA_Report\AIGGPA_Fieldwork_Vault\AIGGPA_Master_Tracker.xlsx"

def run_gog(args):
    cmd = [GOG, "--account", ACC, "--json"] + args
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(f"ERROR: {r.stderr}")
        return None
    try:
        return json.loads(r.stdout)
    except:
        return {}

def excel_to_sheets():
    print(f"Reading local tracker: {LOCAL_TRACKER}")
    
    xl = pd.ExcelFile(LOCAL_TRACKER)
    
    for sheet_name in xl.sheet_names:
        df = pd.read_excel(LOCAL_TRACKER, sheet_name=sheet_name)
        
        # Replace NaN with empty strings
        df = df.fillna("")
        
        # Convert all to strings, ensuring no weird float issues
        df = df.astype(str)
        
        # Prepare headers and data rows
        headers = df.columns.tolist()
        data = df.values.tolist()
        
        full_grid = [headers] + data
        
        print(f"Uploading {len(full_grid)} rows to tab '{sheet_name}'...")
        
        # To clear the sheet before updating, we'd need to use a clear command, but for now we just overwrite.
        # But wait, does the tab exist on Google Sheets?
        # Let's ensure the sheet exists. If it doesn't, gog sheets add-sheet will be needed, but we already created Respondent_Log, FGD_Log, File_Naming_Guide.
        
        # If it's one of the known ones:
        range_target = f"{sheet_name}!A1"
        
        # Convert to JSON temp file for gog to read (to avoid arg length issues in Windows CMD)
        tmp_file = f"temp_{sheet_name}.json"
        with open(tmp_file, "w", encoding="utf-8") as f:
            json.dump(full_grid, f)
            
        # gog sheets update supports --values-json or we can read from standard input maybe?
        # Actually, gog sheets update takes --values-json. Let's see if we can pass it directly for small data.
        val_json = json.dumps(full_grid)
        
        if len(val_json) > 8000:
            print("Data too large for command line argument, truncating or needs file...")
            # If the data is large, this is a problem for Windows CLI. We'll pass it via Powershell trick or try to keep it small.
            # Actually, `gog` sheets update supports piping if we pass a dash? No, the help says `--values-json`.
            # We can write a temporary powershell script to execute it.
            ps_script = f"""
$json = Get-Content -Raw -Path "{tmp_file}"
& "{GOG}" --account "{ACC}" --json sheets update "{SHEET_ID}" "{range_target}" --values-json $json
"""
            ps_file = f"run_{sheet_name}.ps1"
            with open(ps_file, "w", encoding="utf-8") as f:
                f.write(ps_script)
            r = subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", ps_file], capture_output=True, text=True)
            if r.returncode != 0:
                print(f"Error uploading {sheet_name}: {r.stderr}")
            else:
                print(f"Success for {sheet_name}")
            os.remove(ps_file)
        else:
            args = ["sheets", "update", SHEET_ID, range_target, "--values-json", val_json]
            r = run_gog(args)
            if r is not None:
                print(f"Success for {sheet_name}")
            
        if os.path.exists(tmp_file):
            os.remove(tmp_file)

if __name__ == "__main__":
    excel_to_sheets()
