import subprocess
import os

account = "aryan.kori14@gmail.com"
folder_id = "1vXHUgFW3xBUrND__h1JEgx7Ut2bpobLq"

files = [
    r"c:\Users\aryan\Downloads\Framework for Interns.xlsx",
    r"c:\Users\aryan\Downloads\AIGGPA_Printable_Schedule.docx",
    r"c:\Users\aryan\Downloads\Schedule_Revenue.docx",
    r"c:\Users\aryan\Downloads\Schedule_Rural_Development.docx",
    r"c:\Users\aryan\Downloads\Schedule_Forest.docx",
    r"c:\Users\aryan\Downloads\Schedule_Health.docx"
]

gog_bin = r"C:\Users\aryan\.gemini\antigravity\bin\gog.exe"

for fpath in files:
    if os.path.exists(fpath):
        fname = os.path.basename(fpath)
        print(f"Uploading {fname} to Drive...")
        cmd = [
            gog_bin, "--account", account,
            "drive", "upload", fpath, "--parent", folder_id, "--json"
        ]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode == 0:
            print(f"Success: {fname}")
        else:
            print(f"Failed to upload {fname}: {res.stderr}")
    else:
        print(f"File not found: {fpath}")

print("All Google Drive uploads completed.")
