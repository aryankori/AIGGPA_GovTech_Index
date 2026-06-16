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

print("\n=== Retrying Calendar Events ===")
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
