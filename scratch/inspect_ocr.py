import json

path = r"C:\Users\aryan\Downloads\Photos-3-001\ocr_results.json"
with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

for img, text in data.items():
    print(f"--- {img} ---")
    print(text[:500])
