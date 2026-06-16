import os

files_to_update = [
    # Brain artifacts
    r"C:\Users\aryan\.gemini\antigravity-ide\brain\c6604a0c-a934-469c-9bd2-1c855ba07caf\tomorrow_briefing.md",
    r"C:\Users\aryan\.gemini\antigravity-ide\brain\c6604a0c-a934-469c-9bd2-1c855ba07caf\meeting_prep.md",
    
    # Desktop Review Folder
    r"C:\Users\aryan\OneDrive\Desktop\AIGGPA_Fieldwork_Review\tomorrow_briefing.md",
    r"C:\Users\aryan\OneDrive\Desktop\AIGGPA_Fieldwork_Review\tomorrow_briefing.txt",
    r"C:\Users\aryan\OneDrive\Desktop\AIGGPA_Fieldwork_Review\meeting_prep.md",
    r"C:\Users\aryan\OneDrive\Desktop\AIGGPA_Fieldwork_Review\meeting_prep.txt",
    
    # Workspace Review Folder
    r"c:\Users\aryan\OneDrive\Documents\Visual Studio 2022\AIGGPA_Report\AIGGPA_Fieldwork_Review\tomorrow_briefing.md",
    r"c:\Users\aryan\OneDrive\Documents\Visual Studio 2022\AIGGPA_Report\AIGGPA_Fieldwork_Review\tomorrow_briefing.txt",
    r"c:\Users\aryan\OneDrive\Documents\Visual Studio 2022\AIGGPA_Report\AIGGPA_Fieldwork_Review\meeting_prep.md",
    r"c:\Users\aryan\OneDrive\Documents\Visual Studio 2022\AIGGPA_Report\AIGGPA_Fieldwork_Review\meeting_prep.txt",
]

# replacements
def update_tomorrow_briefing(content):
    # Table replacement
    content = content.replace(
        "| **Revenue** | 0 | 0 | **0** | 80 | 0% |",
        "| **Revenue** | 0 | 4 | **4** | 80 | **5%** |"
    )
    # Total update (from ~74 to ~78)
    content = content.replace(
        "| **TOTAL** | | | **~74** | **320** | **~23%** |",
        "| **TOTAL** | | | **~78** | **320** | **~24%** |"
    )
    # Talking script update
    old_script = "Rural Development HQ has 19 responses collected and logged.\nData entry for the DO and RD responses is currently in progress."
    new_script = "Rural Development HQ has 19 responses collected and logged.\nRevenue DO has 4 responses collected and logged (including Tehsildar & Patwari).\nData entry for these responses is currently in progress."
    content = content.replace(old_script, new_script)
    return content

def update_meeting_prep(content):
    # Table replacement
    content = content.replace(
        "| **Revenue** | 0 | 0 | **0** | 80 | 0% |",
        "| **Revenue** | 0 | 4 | **4** | 80 | **5%** |"
    )
    # Total update
    content = content.replace(
        "| **TOTAL** | | | **~74** | **320** | **~23%** |",
        "| **TOTAL** | | | **~78** | **320** | **~24%** |"
    )
    # QA replacement
    old_qa = '| **"Why haven\'t you started Revenue?"** | "We scheduled Revenue for Phase 2 (June 15-20) because Tehsildar/Patwari access is centralized through the Collector\'s office, which requires a specific clearance protocol. Those permission letters are routed and we launch field visits next week." |'
    new_qa = '| **"Why haven\'t you started Revenue?"** | "Actually, we have launched the Revenue surveys! We\'ve completed 4 pilot responses at the District Office/Tehsil level (including the Tehsildar of Betul, Naib Tehsildar of Shahpur, a Revenue Inspector, and a Patwari) to validate the Revenue schedule. The remaining 76 surveys are scheduled for Phase 2 (June 15-20) as we scale the fieldwork." |'
    content = content.replace(old_qa, new_qa)
    
    # Section 1.4 replacement
    old_sec4 = '4. **"Revenue and Health are scheduled for Phase 2 (June 15–20)"** — appointments being arranged through official channels. Permission letters sent.'
    new_sec4 = '4. **"Revenue DO pilot has launched"** — 4 responses collected at Betul and Shahpur Tehsil (Tehsildar, Naib Tehsildar, RI, Patwari). The remaining 76 are scheduled for Phase 2 (June 15–20) as we scale.'
    content = content.replace(old_sec4, new_sec4)
    
    # Section 5 FAQ replacement
    old_faq = 'Revenue and Health require different access protocols — Revenue operates through the Collector\'s office and Health through the CMHO. Those permission chains take longer. Forest was fastest because AIGGPA has existing institutional relationships with the Forest Department.'
    new_faq = 'We have already launched the Revenue DO pilot and completed 4 surveys (Tehsildar, Naib Tehsildar, RI, Patwari). For scaling, Revenue operates through the Collector\'s office, which requires a specific clearance protocol. Those permission letters are now routed, and we scale field visits next week.'
    content = content.replace(old_faq, new_faq)
    
    return content

print("--- UPDATING BRIEFINGS AND PREP SHEETS ---")
for file_path in files_to_update:
    if os.path.exists(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            orig_len = len(content)
            if "tomorrow_briefing" in file_path.lower():
                content = update_tomorrow_briefing(content)
            elif "meeting_prep" in file_path.lower():
                content = update_meeting_prep(content)
                
            if len(content) != orig_len:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"[✓] Updated: {os.path.basename(file_path)}")
            else:
                print(f"[!] No changes applied (check string matches): {os.path.basename(file_path)}")
        except Exception as e:
            print(f"Error updating {file_path}: {e}")
    else:
        print(f"File not found: {file_path}")

print("--- COMPLETED ---")
