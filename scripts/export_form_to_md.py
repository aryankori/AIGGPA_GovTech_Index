import json
import subprocess

form_id = "1LmQXjlGRlE55zW7DjyAsEBWscMpktPcy2pNBV1PE7V0"
gog_path = r"C:\Users\aryan\.gemini\antigravity\bin\gog.exe"

print(f"Fetching form {form_id}...")
r = subprocess.run([gog_path, "--account", "aryan.kori14@gmail.com", "forms", "get", form_id, "--json"], capture_output=True, text=True, encoding="utf-8")
if r.returncode != 0:
    print(f"Error fetching form: {r.stderr}")
    exit(1)

data = json.loads(r.stdout)
form = data.get("form", data)
items = form.get("items", [])

md = []
md.append(f"# {form.get('title', 'Google Form')}")
if "description" in form:
    md.append(f"{form['description']}\n")

section_count = 1
md.append(f"## Section {section_count}")

for item in items:
    title = item.get("title", "")
    if "pageBreakItem" in item:
        section_count += 1
        md.append(f"\n## Section {section_count}: {title}")
    elif "questionItem" in item:
        q = item["questionItem"]["question"]
        qtype = "Short Answer"
        options = []
        if "choiceQuestion" in q:
            qtype = q["choiceQuestion"]["type"]
            options = [o["value"] for o in q["choiceQuestion"].get("options", [])]
        elif "scaleQuestion" in q:
            scale = q["scaleQuestion"]
            qtype = f"Scale ({scale.get('low', 1)} to {scale.get('high', 5)})"
        elif "textQuestion" in q:
            if q["textQuestion"].get("paragraph"):
                qtype = "Paragraph"
        
        req = " *(Required)*" if q.get("required") else ""
        md.append(f"\n**Q: {title}**{req}")
        md.append(f"*Type:* {qtype}")
        if options:
            md.append("*Options:*")
            for o in options:
                md.append(f"  - {o}")
    elif "textItem" in item:
        md.append(f"\n**Text Block: {title}**")
        if "description" in item:
            md.append(item["description"])

output_file = "AIGGPA_Form_Content.md"
with open(output_file, "w", encoding="utf-8") as f:
    f.write("\n".join(md))

print(f"Saved to {output_file}")
