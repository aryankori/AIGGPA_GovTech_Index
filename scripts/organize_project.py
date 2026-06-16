import os
import shutil
import glob

# Path configurations
root_dir = r"c:\Users\aryan\OneDrive\Documents\Visual Studio 2022\AIGGPA_Report"
desktop_dir = r"C:\Users\aryan\OneDrive\Desktop"
desktop_review_dir = os.path.join(desktop_dir, "AIGGPA_Fieldwork_Review")
workspace_review_dir = os.path.join(root_dir, "AIGGPA_Fieldwork_Review")

vault_dir = os.path.join(root_dir, "AIGGPA_Fieldwork_Vault")
archive_dir = os.path.join(root_dir, "Organized_Archive")
prototype_dir = os.path.join(root_dir, "prototype")

brain_artifacts_dir = r"C:\Users\aryan\.gemini\antigravity-ide\brain\c6604a0c-a934-469c-9bd2-1c855ba07caf"

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created directory: {path}")

def copy_file(src, dst):
    if os.path.exists(src):
        try:
            shutil.copy2(src, dst)
            print(f"Copied {os.path.basename(src)} -> {dst}")
        except Exception as e:
            print(f"Error copying {src}: {e}")
    else:
        print(f"Source not found: {src}")

def move_file(src, dst):
    if os.path.exists(src):
        try:
            shutil.move(src, dst)
            print(f"Moved {os.path.basename(src)} -> {dst}")
        except Exception as e:
            print(f"Error moving {src}: {e}")

def main():
    print("--- STARTING WORKSPACE & VAULT REORGANIZATION ---")
    
    # 1. Create necessary folders
    ensure_dir(desktop_review_dir)
    ensure_dir(workspace_review_dir)
    ensure_dir(os.path.join(archive_dir, "01_PDFs"))
    ensure_dir(os.path.join(archive_dir, "02_Build_Artifacts"))
    ensure_dir(os.path.join(archive_dir, "05_Word_Docs"))
    ensure_dir(os.path.join(vault_dir, "07_Secondary_Data"))
    
    # 2. Gather meeting files (The briefing lists these as priority to open)
    meeting_files = [
        # Fieldwork Journal & Master Tracker
        (os.path.join(vault_dir, "04_Observation_Notes", "AIGGPA_Fieldwork_Journal.xlsx"), "01_AIGGPA_Fieldwork_Journal.xlsx"),
        (os.path.join(vault_dir, "AIGGPA_Master_Tracker.xlsx"), "02_AIGGPA_Master_Tracker.xlsx"),
        
        # Coded spreadsheets & results from Review_Presentation_Desk
        (os.path.join(root_dir, "Review_Presentation_Desk", "03_Rural_Development_Responses_Form.xlsx"), "03_Rural_Development_Responses_Form.xlsx"),
        (os.path.join(root_dir, "Review_Presentation_Desk", "04_AIGGPA_Forest_Coded_DataMatrix.xlsx"), "04_AIGGPA_Forest_Coded_DataMatrix.xlsx"),
        (os.path.join(root_dir, "Review_Presentation_Desk", "05_Forest_Descriptive_Statistics.xlsx"), "05_Forest_Descriptive_Statistics.xlsx"),
        (os.path.join(root_dir, "Review_Presentation_Desk", "06_Forest_CrossTabs_CadreDivide.xlsx"), "06_Forest_CrossTabs_CadreDivide.xlsx"),
        
        # Visualisations
        (os.path.join(vault_dir, "09_Analysis_Output", "Visualisations", "cadre_radar.png"), "07_Forest_Cadre_RadarChart.png"),
        (os.path.join(vault_dir, "09_Analysis_Output", "Visualisations", "digital_divide_heatmap.png"), "08_Forest_DigitalDivide_Heatmap.png"),
        (os.path.join(vault_dir, "09_Analysis_Output", "Visualisations", "training_gap.png"), "09_Forest_TrainingGap_BarChart.png"),
        (os.path.join(vault_dir, "09_Analysis_Output", "Visualisations", "device_availability.png"), "10_Forest_DeviceAvailability_Chart.png"),
        
        # Questionnaire & Schedules PDFs for proof
        (os.path.join(vault_dir, "01_Schedules_Raw", "Schedules_Templates", "AIGGPA_Dept_Questionnaire.pdf"), "AIGGPA_Dept_Questionnaire.pdf"),
        (os.path.join(vault_dir, "01_Schedules_Raw", "Schedules_Templates", "AIGGPA_Questionnaire.pdf"), "AIGGPA_Questionnaire.pdf"),
        (os.path.join(vault_dir, "01_Schedules_Raw", "Schedules_Templates", "Schedule_Forest.pdf"), "Schedule_Forest.pdf"),
        (os.path.join(vault_dir, "01_Schedules_Raw", "Schedules_Templates", "Schedule_Rural_Development.pdf"), "Schedule_Rural_Development.pdf"),
    ]
    
    # 3. Copy files to desktop review folder and workspace review folder
    print("\n--- COPYING MEETING FILES TO SHORTCUT DIRECTORIES ---")
    for src_path, dest_name in meeting_files:
        # To Desktop review folder
        copy_file(src_path, os.path.join(desktop_review_dir, dest_name))
        # To Workspace review folder
        copy_file(src_path, os.path.join(workspace_review_dir, dest_name))
        
    # Copy meeting prep documents (as markdown and txt)
    prep_docs = ["meeting_prep.md", "tomorrow_briefing.md"]
    for doc in prep_docs:
        src = os.path.join(brain_artifacts_dir, doc)
        if os.path.exists(src):
            # Copy markdown
            copy_file(src, os.path.join(desktop_review_dir, doc))
            copy_file(src, os.path.join(workspace_review_dir, doc))
            # Copy plain text version for easier reading on any device
            txt_doc = doc.replace(".md", ".txt")
            shutil.copy2(src, os.path.join(desktop_review_dir, txt_doc))
            shutil.copy2(src, os.path.join(workspace_review_dir, txt_doc))
            print(f"Copied plain text {txt_doc} version.")
            
    # 4. Organize loose files in root
    print("\n--- ORGANIZING LOOSE ROOT FILES ---")
    
    # 4a. Loose PDFs -> Organized_Archive/01_PDFs/
    pdf_files = glob.glob(os.path.join(root_dir, "*.pdf"))
    for pdf in pdf_files:
        move_file(pdf, os.path.join(archive_dir, "01_PDFs"))
        
    # 4b. Loose Word docs (.docx) -> Organized_Archive/05_Word_Docs/
    docx_files = glob.glob(os.path.join(root_dir, "*.docx"))
    for docx in docx_files:
        # Ignore temporary word file lock ~$
        if not os.path.basename(docx).startswith("~$"):
            move_file(docx, os.path.join(archive_dir, "05_Word_Docs"))
            
    # 4c. Loose build artifacts (.aux, .log, .out, .toc) -> Organized_Archive/02_Build_Artifacts/
    extensions = ["*.aux", "*.log", "*.out", "*.toc", "*.synctex.gz"]
    for ext in extensions:
        artifacts = glob.glob(os.path.join(root_dir, ext))
        for art in artifacts:
            move_file(art, os.path.join(archive_dir, "02_Build_Artifacts"))
            
    # 4d. Loose prototype files -> prototype/
    proto_files = [
        "ClinicalDashboard.tsx",
        "ClinicalDashboard.css",
        "ResearchDashboard.tsx",
        "ResearchDashboard.html",
        "ResearchDashboard.css",
        "forest_circles.html",
        "forest_finance.html",
        "forest_home.html",
        "leaf.html",
        "betul_full.html",
        "fieldwork_map.html",
        "fieldwork_map.png"
    ]
    for pf in proto_files:
        src = os.path.join(root_dir, pf)
        if os.path.exists(src):
            move_file(src, os.path.join(prototype_dir, pf))
            
    # 4e. Loose secondary/vault data -> vault/07_Secondary_Data/ and other subfolders
    secondary_data_files = [
        ("AIGGPA_Forest_Department_Report.docx", os.path.join(vault_dir, "07_Secondary_Data")),
        ("AIGGPA_Forest_Department_Report.xlsx", os.path.join(vault_dir, "07_Secondary_Data")),
        ("Framework_Completed.xlsx", os.path.join(vault_dir, "07_Secondary_Data")),
        ("Framework_View.html", os.path.join(vault_dir, "07_Secondary_Data")),
        ("Framework_for_Interns.xlsx", os.path.join(vault_dir, "07_Secondary_Data")),
        ("Permission_Letter_Draft.txt", os.path.join(vault_dir, "07_Secondary_Data")),
        ("Reference_Papers_UTAUT.md", os.path.join(vault_dir, "07_Secondary_Data")),
        ("mp_forest_directory.csv", os.path.join(vault_dir, "07_Secondary_Data")),
        ("mp_forest_survey.xlsx", os.path.join(vault_dir, "07_Secondary_Data")),
        ("AIGGPA_Form_Content.md", os.path.join(vault_dir, "01_Schedules_Raw", "Schedules_Templates")),
        ("Gemini_Analysis_Prompt.md", os.path.join(vault_dir, "09_Analysis_Output")),
        ("TODO_repo-indexer.md", os.path.join(archive_dir))
    ]
    for filename, dest_folder in secondary_data_files:
        src = os.path.join(root_dir, filename)
        if os.path.exists(src):
            move_file(src, os.path.join(dest_folder, filename))
            
    print("\n--- REORGANIZATION COMPLETE ---")

if __name__ == "__main__":
    main()
