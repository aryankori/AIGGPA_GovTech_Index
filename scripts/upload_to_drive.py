import subprocess
import os

GOG = r"C:\Users\aryan\.gemini\antigravity\bin\gog.exe"
ACCOUNT = "aryan.kori14@gmail.com"

folders = {
    "scripts/": "1d9yVzyQAmNm0Dz9zY5YWi28cwxvDUJzX",
    "schedules/pdf/": "11buTDr83_iNKGcV_XVKX9agr1lSj4Rw8",
    "schedules/docx/": "1pAgk_bb9aSojw4LTLzg_UZ8w8je5NHPW"
}

for local_dir, drive_id in folders.items():
    print(f"Uploading files from {local_dir}...")
    if not os.path.exists(local_dir):
        print(f"Directory {local_dir} does not exist")
        continue
        
    for filename in os.listdir(local_dir):
        file_path = os.path.join(local_dir, filename)
        if os.path.isfile(file_path):
            cmd = [GOG, "--no-input", "--account", ACCOUNT, "drive", "upload", file_path, "--parent", drive_id, "--json"]
            print(f"Running: {' '.join(cmd)}")
            res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
            if res.returncode != 0:
                print(f"Error uploading {filename}: {res.stderr}")
            else:
                print(f"Uploaded {filename}")
                
print("All uploads complete!")
