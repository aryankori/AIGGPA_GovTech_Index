"""Build AIGGPA Google Workspace assets using gog CLI."""
import subprocess, json, sys

GOG = r"C:\Users\aryan\.gemini\antigravity\bin\gog.exe"
ACC = "aryan.kori14@gmail.com"

def run(args, check=True):
    cmd = [GOG, "--account", ACC, "--json"] + args
    r = subprocess.run(cmd, capture_output=True, text=True)
    if check and r.returncode != 0:
        print(f"  ERROR: {r.stderr.strip()[:200]}")
        return None
    try:
        return json.loads(r.stdout)
    except:
        return {}

def folder_id(r):
    """drive mkdir returns {folder: {id: ...}}"""
    if not r: return None
    return (r.get("folder") or {}).get("id") or r.get("id")

def form_id_from(r):
    if not r: return None
    return r.get("formId") or r.get("id")

# ── 1. DRIVE FOLDERS ──────────────────────────────────────────────────────────
print("\n=== Creating Drive Folder Structure ===")
root = run(["drive", "mkdir", "AIGGPA_Research_2026"])
root_id = folder_id(root)
print(f"Root: {root_id}")

for name in ["01_Schedules_Raw","02_Audio_Recordings","03_Transcripts",
             "04_Observation_Notes","05_Photos_Evidence","06_Consent_Forms",
             "07_Secondary_Data","08_Data_Entry","09_Analysis_Output","10_Reports_Drafts"]:
    args = ["drive", "mkdir", name]
    if root_id:
        args += ["--parent", root_id]
    f = run(args)
    fid = folder_id(f)
    print(f"  {name}: {fid or 'FAILED'}")

# ── 2. GOOGLE FORM ────────────────────────────────────────────────────────────
print("\n=== Creating Survey Form ===")
form = run(["forms", "create", "--title",
            "AIGGPA Survey: Digital Tool Usage in MP Government Departments"])
form_id = form_id_from(form)
print(f"Form ID: {form_id}")

if not form_id:
    print("  Form creation failed — skipping questions")
else:
    run(["forms", "update", form_id, "--description",
     "AIGGPA research survey on digital adoption in Revenue, Rural Development, Forest & Health departments. Responses are confidential. Takes ~10 minutes."])

if form_id:
 questions_list_placeholder = True  # questions added below

questions = [
    # (title, type, required, options, description, scale_low, scale_high, ll, hl)
    ("Which department do you work in?", "radio", True,
     ["Revenue","Rural Development","Forest","Health"], "", 0,0,"",""),
    ("Your designation / post:", "text", True, [], "", 0,0,"",""),
    ("Cadre class:", "radio", True,
     ["Class I (Collector / DFO / CMHO level)",
      "Class II (SDM / BDO / BMO / ACF level)",
      "Class III (Tehsildar / Patwari / ANM / GRS / RFO level)",
      "Class IV (Peon / Forest Guard / Ward Boy level)"], "", 0,0,"",""),
    ("Age group:", "radio", True,
     ["Below 30","30–45","46–60","Above 60"], "", 0,0,"",""),
    ("Years of service:", "radio", True,
     ["0–5 years","6–10 years","11–20 years","21+ years"], "", 0,0,"",""),
    ("Devices at your workstation:", "checkbox", True,
     ["Desktop","Laptop","Tablet","Shared smartphone","Personal phone only","No device"],
     "Tick all that apply.", 0,0,"",""),
    ("Do you share your device with colleagues?", "radio", True,
     ["Yes – one shared computer for the whole office",
      "Sometimes – I have my own but help others",
      "No – I have my own dedicated device"], "", 0,0,"",""),
    ("Rate internet connectivity at your office:", "scale", True, [],
     "1=No internet / unusable, 5=Fast and reliable", 1,5,"No internet","Fast & reliable"),
    ("How often do you face internet outages during work?", "radio", True,
     ["Never","1–2 times a week","3–5 times a week","Almost every day","Constantly"], "", 0,0,"",""),
    ("IT/technical support when portals break?", "radio", True,
     ["Yes – formal helpdesk","Yes – informal colleague help",
      "No – I figure it out myself","No – we just use paper"], "", 0,0,"",""),
    ("Digital tools help me complete tasks faster than paper.", "scale", True, [],
     "1=Strongly Disagree, 5=Strongly Agree", 1,5,"Strongly Disagree","Strongly Agree"),
    ("Digital tools improve accuracy of my work.", "scale", True, [],
     "1=Strongly Disagree, 5=Strongly Agree", 1,5,"Strongly Disagree","Strongly Agree"),
    ("Tools are well-suited to my actual job tasks.", "scale", True, [],
     "1=Strongly Disagree, 5=Strongly Agree", 1,5,"Strongly Disagree","Strongly Agree"),
    ("Digital tools increase my overall productivity.", "scale", True, [],
     "1=Strongly Disagree, 5=Strongly Agree", 1,5,"Strongly Disagree","Strongly Agree"),
    ("How difficult are the portals/apps you use?", "scale", True, [],
     "1=Very easy, 5=Very difficult / confusing", 1,5,"Very easy","Very difficult"),
    ("I feel confident using digital tools without assistance.", "scale", True, [],
     "1=Strongly Disagree, 5=Strongly Agree", 1,5,"Strongly Disagree","Strongly Agree"),
    ("Time to learn a new portal:", "radio", True,
     ["Less than 1 day","A few days","1–2 weeks","More than 2 weeks",
      "I haven't fully learned current portals yet"], "", 0,0,"",""),
    ("Superiors actively encourage digital tool use.", "scale", True, [],
     "1=Strongly Disagree, 5=Strongly Agree", 1,5,"Strongly Disagree","Strongly Agree"),
    ("Colleagues regularly use digital tools.", "scale", True, [],
     "1=Strongly Disagree, 5=Strongly Agree", 1,5,"Strongly Disagree","Strongly Agree"),
    ("Formal mandate for digital tool use exists?", "radio", True,
     ["Yes – written order","Yes – verbal instruction only",
      "No formal mandate","Don't know"], "", 0,0,"",""),
    ("How often do you use digital tools for core work?", "radio", True,
     ["Daily","4–5 times a week","2–3 times a week","Once a week","Rarely","Never"],
     "", 0,0,"",""),
    ("Percentage of your daily work done digitally:", "radio", True,
     ["0–20%","21–40%","41–60%","61–80%","81–100%"], "", 0,0,"",""),
    ("Digital training received in last 2 years:", "radio", True,
     ["Yes – formal government training",
      "Yes – informal / from colleague",
      "Yes – self-taught",
      "No training at all"], "", 0,0,"",""),
    ("Training was sufficient for my actual job needs:", "scale", True, [],
     "1=Not sufficient, 5=Completely sufficient. Skip if no training.", 1,5,
     "Not sufficient","Completely sufficient"),
    ("Digital skills I still need training on:", "paragraph", False, [],
     "e.g. RCMS case filing, NMMS app, ANMOL registration", 0,0,"",""),
    ("Challenges faced with digital tools:", "checkbox", True,
     ["Slow or no internet","Portal crashes / timeouts","No or shared computer only",
      "Confusing interface","Lack of training","No IT support",
      "Power cuts","Language barrier (no Hindi)","No challenges – all works fine"],
     "Tick all that apply.", 0,0,"",""),
    ("How often do technical problems disrupt your work?", "radio", True,
     ["Every day","Few times a week","Once a week","Rarely","Never"], "", 0,0,"",""),
    ("Organisation provides adequate digital support:", "scale", True, [],
     "1=Strongly Disagree, 5=Strongly Agree", 1,5,"Strongly Disagree","Strongly Agree"),
    ("One change that would most improve your digital tool use:", "paragraph", False, [],
     "e.g. Better internet, Hindi training, simpler design, dedicated computer", 0,0,"",""),
    ("Has digital adoption improved service delivery to citizens?", "radio", False,
     ["Yes, significantly","Yes, somewhat","No noticeable change",
      "No – it made things worse","Cannot say"], "", 0,0,"",""),
    ("Any other comments:", "paragraph", False, [], "", 0,0,"",""),
]

print(f"Adding {len(questions)} questions...")
for i, (title, qtype, req, opts, desc, sl, sh, ll, hl) in enumerate(questions):
    if not form_id:
        print("  Skipping – no form ID"); break
    args = ["forms", "add-question", "--title", title, "--type", qtype, form_id]
    if req: args.append("--required")
    if desc: args += ["--description", desc]
    if qtype == "scale":
        args += ["--scale-low", str(sl), "--scale-high", str(sh)]
        if ll: args += ["--scale-low-label", ll]
        if hl: args += ["--scale-high-label", hl]
    for opt in opts:
        args += ["--option", opt]
    r = run(args, check=False)
    status = "OK" if r is not None else "FAIL"
    print(f"  [{i+1}/{len(questions)}] {status}: {title[:55]}")

# ── 3. GOOGLE SHEET ───────────────────────────────────────────────────────────
print("\n=== Creating Master Tracker Sheet ===")
sheet = run(["sheets", "create", "AIGGPA_Master_Tracker_2026",
             "--sheets", "Respondent_Log,FGD_Log,File_Naming_Guide"])
sheet_id = (sheet.get("spreadsheetId") or sheet.get("id")) if sheet else None
print(f"Sheet ID: {sheet_id}")

if sheet_id:
    headers = [["Respondent ID","Department","Cadre","Designation","Date","Office",
                "District","Interviewer","Audio File","Consent Signed",
                "Schedule Scanned","Data Entered","Notes"]]
    run(["sheets", "update", sheet_id, "Respondent_Log!A1",
         "--values-json", json.dumps(headers)])
    print("  Header row added to Respondent_Log")

# ── 4. CALENDAR EVENTS ────────────────────────────────────────────────────────
print("\n=== Adding Calendar Events ===")
CAL = "primary"
events = [
    ("AIGGPA Fieldwork: Revenue Dept Phase 1", "2026-05-12", "Bhopal – Head Office + Collectorate"),
    ("AIGGPA Fieldwork: Health Dept Phase 1",  "2026-05-15", "CMHO Office + District Hospital"),
    ("AIGGPA Fieldwork: Rural Dev Phase 1",    "2026-05-19", "Janpad + Block offices"),
    ("AIGGPA Fieldwork: Forest Dept Phase 1",  "2026-05-22", "DFO + Range Office"),
    ("AIGGPA: Weekly Data Entry & Validation", "2026-05-25", "Validate tracker, transcribe audio"),
    ("AIGGPA Fieldwork: Revenue Dept Phase 2", "2026-06-02", "District + Tehsil offices"),
    ("AIGGPA Fieldwork: Health Dept Phase 2",  "2026-06-05", "PHC + CHC visits"),
    ("AIGGPA Fieldwork: Rural Dev Phase 2",    "2026-06-09", "Gram Panchayat level"),
    ("AIGGPA Fieldwork: Forest Dept Phase 2",  "2026-06-12", "Range + Beat level"),
    ("AIGGPA: Mid-point Review with Manager",  "2026-06-15", "Present stats + preliminary findings"),
    ("AIGGPA: Final Report Submission",        "2026-07-15", "Submit to AIGGPA management"),
]
for title, date, loc in events:
    r = run(["calendar", "create", CAL,
             "--summary", title,
             "--from", f"{date}T09:00:00+05:30",
             "--to",   f"{date}T17:00:00+05:30",
             "--location", loc,
             "--all-day"])
    print(f"  {'OK' if r else 'FAIL'}: {title}")

# ── SUMMARY ───────────────────────────────────────────────────────────────────
print("\n" + "="*55)
print("DONE – AIGGPA Google Workspace Setup")
print("="*55)
if root_id:
    print(f"Drive Folder : https://drive.google.com/drive/folders/{root_id}")
if form_id:
    print(f"Form (edit)  : https://docs.google.com/forms/d/{form_id}/edit")
    print(f"Form (share) : https://docs.google.com/forms/d/{form_id}/viewform")
if sheet_id:
    print(f"Tracker Sheet: https://docs.google.com/spreadsheets/d/{sheet_id}/edit")
print(f"\nCalendar: {len(events)} fieldwork events added")
