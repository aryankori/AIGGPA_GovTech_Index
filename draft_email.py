import subprocess

account = "aryan.kori14@gmail.com"
subject = "Final Fieldwork Documents - Framework & Schedules"
body = """Hi Sir,

The fieldwork instruments are ready for review.

I've attached the finalized internship framework and the five data collection schedules. 
I tightened up the framework to make it a fast read—one clean row per objective—but kept all the academic references mapped out.

For the schedules, I compressed them down to a strict 4-page limit. I also maxed out the checkbox sizes and widened the write-in blanks. That way, the field teams won't struggle to fill them out on a clipboard.

Let me know if you want any final tweaks before we print.

Best,
Aryan"""

attachments = [
    r"c:\Users\aryan\Downloads\Framework for Interns.xlsx",
    r"c:\Users\aryan\Downloads\AIGGPA_Printable_Schedule.docx",
    r"c:\Users\aryan\Downloads\Schedule_Revenue.docx",
    r"c:\Users\aryan\Downloads\Schedule_Rural_Development.docx",
    r"c:\Users\aryan\Downloads\Schedule_Forest.docx",
    r"c:\Users\aryan\Downloads\Schedule_Health.docx"
]

gog_bin = r"C:\Users\aryan\.gemini\antigravity\bin\gog.exe"

cmd = [
    gog_bin,
    "--account", account,
    "gmail", "drafts", "create",
    "--to", "boss@example.com",
    "--subject", subject,
    "--body", body
]

for att in attachments:
    cmd.extend(["--attach", att])

print("Running gog command to create draft...")
res = subprocess.run(cmd, capture_output=True, text=True)
print("STDOUT:", res.stdout)
if res.stderr:
    print("STDERR:", res.stderr)
