import os
import subprocess
import re

# Keywords list
keywords = [
    "Technology Acceptance Model (TAM)",
    "Unified Theory of Acceptance and Use of Technology (UTAUT)",
    "Perceived Usefulness (PU) / Performance Expectancy (PE)",
    "Effort Expectancy (EE)",
    "Social Influence (SI)",
    "Facilitating Conditions (FC)",
    "Cronbach's Alpha (α)",
    "Mann-Whitney U Test",
    "Kruskal-Wallis H Test",
    "e-HRMS 2.0 (Electronic Human Resource Management System)",
    "iGOT Karmayogi (Mission Karmayogi)",
    "e-Office",
    "SPARROW (Smart Performance Appraisal Report Recording Online Window)",
    "PFMS (Public Financial Management System)",
    "GeM (Government e-Marketplace)",
    "MPOnline",
    "MP Bhulekh / WebGIS",
    "RCMS (Revenue Case Management System)",
    "SAMPADA 2.0",
    "NMMS (National Mobile Monitoring System)",
    "ANMOL MP (ANM Online)",
    "eVIN (Electronic Vaccine Intelligence Network)",
    "MAP_IT (Madhya Pradesh Agency for Promotion of Information Technology)"
]

# Set directories
script_dir = os.path.dirname(os.path.abspath(__file__))
workspace_dir = os.path.abspath(os.path.join(script_dir, ".."))
output_dir = os.path.join(workspace_dir, "last30")
os.makedirs(output_dir, exist_ok=True)

last30days_script = os.path.join(workspace_dir, ".agents", "skills", "last30days", "scripts", "last30days.py")

print(f"[+] Output directory: {output_dir}")
print(f"[+] last30days script: {last30days_script}")

def sanitize_filename(name):
    # Keep alphanumeric, underscores, hyphens, remove others
    s = re.sub(r'[\s/()]+', '_', name)
    s = re.sub(r'[^a-zA-Z0-9_-]', '', s)
    return s.strip('_') + ".md"

for idx, kw in enumerate(keywords, 1):
    filename = f"{idx:02d}_{sanitize_filename(kw)}"
    output_path = os.path.join(output_dir, filename)
    print(f"[{idx}/{len(keywords)}] Running last30days for: '{kw}' -> {filename}")
    
    # Construct subprocess call
    cmd = [
        "python",
        last30days_script,
        kw,
        "--mock",
        "--output",
        output_path
    ]
    
    try:
        # Run process and hide stdout to prevent terminal spam
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f"  [✓] Saved successfully")
    except subprocess.CalledProcessError as e:
        print(f"  [!] Failed for '{kw}': {e}")
        print(f"  [!] Stderr: {e.stderr}")

print("\n[✓] Batch generation complete!")
