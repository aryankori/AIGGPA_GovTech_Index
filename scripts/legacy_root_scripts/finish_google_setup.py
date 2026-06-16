import subprocess, json

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

print("\n=== Completing Survey Form Setup ===")
# We already created a blank form in the debug step. Let's use its ID:
form_id = "1KTwox42FUhRydLP9ws2ZAQQpaCI0cbhd-lkcCgKSiHI"

run(["forms", "update", form_id, "--description",
     "AIGGPA research survey on digital adoption in Revenue, Rural Development, Forest & Health departments. Responses are confidential. Takes ~10 minutes."])

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

print("\n=== Adding Calendar Events ===")
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
    r = run(["calendar", "create", "primary",
             "--summary", title,
             "--from", date,
             "--to", date,
             "--location", loc,
             "--all-day"])
    print(f"  {'OK' if r else 'FAIL'}: {title}")

print("\nDONE!")
print(f"Form (share): https://docs.google.com/forms/d/{form_id}/viewform")
