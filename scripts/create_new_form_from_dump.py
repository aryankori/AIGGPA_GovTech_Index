import subprocess
import time
import sys
import json
import re
import os

GOG = r"C:\Users\aryan\.gemini\antigravity\bin\gog.exe"
ACCOUNT = "aryan.kori14@gmail.com"

def run_gog(args):
    cmd = [GOG, "--no-input", "--account", ACCOUNT] + args
    res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
    if res.returncode != 0:
        print(f"Error executing gog: {res.stderr}")
        return None
    return res.stdout

def create_form():
    title = "AIGGPA Final Fieldwork Questionnaire"
    print(f"Creating new form: {title}...")
    out = run_gog(["forms", "create", "--title", title, "--json"])
    if not out:
        print("Failed to create form.")
        sys.exit(1)
        
    form_data = json.loads(out)
    form_id = form_data.get("form", {}).get("formId")
    print(f"Successfully created form with ID: {form_id}")
    return form_id

def add_q(form_id, q_title, q_type, options=None):
    # Map from custom extracted types to gog form types
    if q_type == "Short Answer":
        gtype = "text"
    elif q_type == "Paragraph":
        gtype = "paragraph"
    elif q_type == "RADIO":
        gtype = "radio"
    elif q_type == "CHECKBOX":
        gtype = "checkbox"
    elif q_type == "Scale (1 to 5)":
        gtype = "scale"
    else:
        gtype = "text"
        
    if gtype in ["radio", "checkbox"] and not options:
        gtype = "paragraph" 
        
    args = ["forms", "add-question", form_id, "--title", q_title, "--type", gtype]
    
    if options and gtype in ["radio", "checkbox"]:
        # Split options e.g., "- Below 30 - 30-45"
        opts = [o.strip() for o in options.split(" - ") if o.strip()]
        if opts and options.startswith("-"):
            opts = [o for o in opts if o]
        for opt in opts:
            if opt.startswith("-"): opt = opt[1:].strip()
            args.extend(["-o", opt])
            
    run_gog(args)
    time.sleep(1.2) # Rate limit protection

def main():
    dump_path = os.path.join(os.path.dirname(__file__), "..", "temp_docx_dump.txt")
    if not os.path.exists(dump_path):
        dump_path = "temp_docx_dump.txt" # Try local if running from root
        if not os.path.exists(dump_path):
            print("Could not find temp_docx_dump.txt. Aborting.")
            sys.exit(1)
        
    form_id = create_form()
    
    with open(dump_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    count = 1
    for line in lines:
        line = line.strip()
        if not line or line.startswith("Section") or line.startswith("AIGGPA"):
            continue
            
        if line.startswith("Q:"):
            match = re.search(r"Q: (.*?)\s+Type: (.*?)(?:\s+Options: (.*))?$", line)
            if match:
                q_text = match.group(1)
                q_type = match.group(2).strip()
                options = match.group(3)
                print(f"[{count}] Adding: {q_text[:40]}...")
                add_q(form_id, q_text, q_type, options)
                count += 1

    print(f"\n==========================================")
    print(f"Done! Form created successfully.")
    print(f"URL: https://docs.google.com/forms/d/{form_id}/edit")
    print(f"==========================================")

if __name__ == "__main__":
    main()
