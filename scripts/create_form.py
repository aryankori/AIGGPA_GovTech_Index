"""Create a Google Form with all questions from the AIGGPA schedules."""
import subprocess
import time
import sys

GOG = r"C:\Users\aryan\.gemini\antigravity\bin\gog.exe"
ACCOUNT = "aryan.kori14@gmail.com"

def run_gog(args):
    cmd = [GOG, "--no-input", "--account", ACCOUNT] + args
    print(f"Running: {' '.join(cmd)}", flush=True)
    res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
    if res.returncode != 0:
        print(f"Error: {res.stderr}", flush=True)
        return None
    return res.stdout

# 1. Create the form
title = "AIGGPA Research Schedule / अनुसंधान अनुसूची"
out = run_gog(["forms", "create", "--title", title, "--json"])
if not out:
    print("Failed to create form")
    sys.exit(1)

import json
form_data = json.loads(out)
form_id = form_data.get("form", {}).get("formId")
print(f"Created form with ID: {form_id}")

# Helper to add question
def add_q(q_title, q_type="text", options=None, description=None, required=False):
    if q_type == "radio" and not options:
        q_type = "paragraph"
    args = ["forms", "add-question", form_id, "--title", q_title, "--type", q_type]
    if description:
        args.extend(["--description", description])
    if required:
        args.append("--required")
    if options:
        for opt in options:
            args.extend(["-o", opt])
    
    run_gog(args)
    time.sleep(0.5)  # Avoid rate limits

# Load questions from hi.py
sys.path.append(r"c:\Users\aryan\OneDrive\Documents\Visual Studio 2022\AIGGPA_Report")
from hi import Q, ROLE, PERSONAL, DEPT_REVENUE, DEPT_RD, DEPT_FOREST, DEPT_HEALTH

print("Adding common questions...")
# Map types for common questions
types = {
    "Q1": ("text", None),
    "Q2": ("text", None),
    "Q3": ("radio", ["Below 30", "30-45", "46-60"]),
    "Q4": ("radio", ["Male", "Female", "Other"]),
    "Q5": ("radio", ["0-5", "6-10", "11-20", "21+"]),
    "Q6": ("radio", ["Up to 12th", "Grad", "PG", "Prof"]),
    "Q7": ("checkbox", ["Desktop", "Laptop", "Tablet", "Phone", "None"]),
    "Q8": ("radio", ["Yes, always", "Sometimes", "No, dedicated"]),
    "Q9": ("scale", None),  # Default 1-5
    "Q10": ("radio", ["Never", "1-2", "3-5", "Daily"]),
    "Q11": ("radio", ["Yes", "No"]),
    "Q12": ("radio", ["Same day", "2-3 days", "1 week+", "Never"]),
}
# Q13-Q18 are scale
for i in range(13, 19):
    types[f"Q{i}"] = ("scale", None)
types["Q19"] = ("radio", ["<1 day", "Few days", "1-2 weeks", ">2 weeks"])
types["Q20"] = ("scale", None)
types["Q21"] = ("scale", None)
types["Q22"] = ("scale", None)
types["Q23"] = ("radio", ["Yes", "No", "Don't know"])
types["Q24"] = ("checkbox", ["e-Office", "CM Helpline", "PFMS", "SPARROW", "iGOT", "MP eDistrict"])
types["Q25"] = ("radio", ["Daily", "Weekly", "Monthly", "Rarely", "Never"])
types["Q26"] = ("radio", ["0-20%", "21-40%", "41-60%", "61-80%", "81-100%"])
types["Q27"] = ("radio", ["Yes", "No"])
types["Q28"] = ("radio", ["1", "2-3", "4-5", "More than 5"])
types["Q29"] = ("scale", None)
types["Q30"] = ("scale", None)
types["Q31"] = ("paragraph", None)
types["Q32"] = ("checkbox", ["Slow internet", "Crashes", "No device", "Complex UI", "No training", "No support", "Power cuts"])
types["Q33"] = ("radio", ["Daily", "Weekly", "Monthly", "Rarely", "Never"])
types["Q34"] = ("scale", None)
types["Q35"] = ("scale", None)
types["Q36"] = ("scale", None)
types["Q37"] = ("paragraph", None) # Ranking
types["Q38"] = ("paragraph", None)
types["Q39"] = ("radio", ["Yes, significantly", "Somewhat", "No change", "Worsened", "Can't say"])

for qnum, en, hn in Q:
    q_title = f"{en} / {hn}"
    q_type, options = types.get(qnum, ("text", None))
    print(f"Adding {qnum}...")
    add_q(q_title, q_type, options)

print("Adding Revenue questions...")
for idx, (en, hn) in enumerate(DEPT_REVENUE):
    q_title = f"[Revenue] {en} / {hn}"
    q_type = "scale" if "How difficult" in en or "Has" in en or "Rate" in en else "radio"
    opts = None
    if q_type == "radio":
        if "percentage" in en.lower():
            opts = ["0-20%", "21-40%", "41-60%", "61-80%", "81-100%"]
        elif "aware" in en.lower():
            q_type = "checkbox"
            opts = ["Bhulekh/WebGIS", "RCMS", "SAARA", "SAMPADA", "e-Court", "None"]
        elif "citizens visit" in en.lower():
            q_type = "scale"
        elif "steps are digital" in en.lower():
            q_type = "paragraph"
    
    add_q(q_title, q_type, opts)

print("Adding RD questions...")
for idx, (en, hn) in enumerate(DEPT_RD):
    q_title = f"[Rural Dev] {en} / {hn}"
    q_type = "scale" if "How difficult" in en or "Has" in en or "Rate" in en else "radio"
    opts = None
    if "aware" in en.lower():
        q_type = "checkbox"
        opts = ["NREGASoft/NMMS", "e-Gram Swaraj", "PMAY-G", "SBM-G", "Panchayat Darpan", "PFMS", "None"]
    elif "working day" in en.lower():
        opts = ["<1hr", "1-2hr", "2-4hr", "4+hr", "Almost all day"]
    elif "steps are digital" in en.lower():
        q_type = "paragraph"
    elif "what do you do" in en.lower():
        opts = ["Wait/retry", "Paper, upload later", "Block office", "Ask someone", "Skip"]
    
    add_q(q_title, q_type, opts)

print("Adding Forest questions...")
for idx, (en, hn) in enumerate(DEPT_FOREST):
    q_title = f"[Forest] {en} / {hn}"
    q_type = "scale" if "How difficult" in en or "Has" in en or "Rate" in en else "radio"
    opts = None
    if "aware" in en.lower():
        q_type = "checkbox"
        opts = ["e-Green Watch", "AI Alert", "GIS", "Forest Offence MIS", "Nursery MIS", "None"]
    elif "device" in en.lower():
        opts = ["Dept-issued", "Personal device", "Not available"]
    elif "steps" in en.lower() or "what do you do" in en.lower():
        q_type = "paragraph"
    
    add_q(q_title, q_type, opts)

print("Adding Health questions...")
for idx, (en, hn) in enumerate(DEPT_HEALTH):
    q_title = f"[Health] {en} / {hn}"
    q_type = "scale" if "How difficult" in en or "Has" in en or "Rate" in en or "reliable" in en.lower() or "much" in en.lower() else "radio"
    opts = None
    if "aware" in en.lower():
        q_type = "checkbox"
        opts = ["ANMOL", "HMIS", "Nikshay", "eVIN", "IHIP", "ABHA", "MPCDSR", "None"]
    elif "SAME data" in en.lower():
        q_type = "scale"
    elif "steps" in en.lower() or "report it" in en.lower():
        q_type = "paragraph"
    
    add_q(q_title, q_type, opts)

print("Adding Role questions...")
role_opts = [
    ["Data entry", "Review/approve", "Field verification", "Don't use", "Other"],
    ["Yes, one person", "A few share", "Everyone does own", "N/A"],
    None, # scale
    ["Wait for IT", "Ask colleague", "Use paper", "Fix myself", "Tell supervisor", "Abandon"],
    ["Yes", "Rely on subordinates", "Mixed", "Don't know"],
    None, # scale
    ["Yes", "No"],
    ["Yes", "Somewhat", "No"]
]
for idx, (en, hn) in enumerate(ROLE):
    q_title = f"{en} / {hn}"
    q_type = "scale" if role_opts[idx] is None else "radio"
    if idx == 6 or idx == 7:
        q_type = "radio"
    add_q(q_title, q_type, role_opts[idx])

print("Adding Personal Tools questions...")
pt_opts = [
    ["Yes", "No"],
    ["WhatsApp", "Google Docs/Drive", "ChatGPT/AI", "YouTube", "Personal email", "MS Office", "Google Translate", "Other"],
    ["Drafting", "Translating", "Coordinating", "Learning portals", "Backup", "Sharing files", "Other"],
    ["Daily", "Few times/week", "Occasionally", "Rarely", "Never"],
    None, # scale
    None # paragraph
]
for idx, (en, hn) in enumerate(PERSONAL):
    q_title = f"{en} / {hn}"
    q_type = "radio"
    if idx == 1 or idx == 2:
        q_type = "checkbox"
    elif idx == 4:
        q_type = "scale"
    elif idx == 5:
        q_type = "paragraph"
    add_q(q_title, q_type, pt_opts[idx])

print(f"\nDone! Form created: https://docs.google.com/forms/d/{form_id}/edit")
