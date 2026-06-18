import json
import os

transcript_path = r"C:\Users\aryan\.gemini\antigravity-ide\brain\c6604a0c-a934-469c-9bd2-1c855ba07caf\.system_generated\logs\transcript.jsonl"

with open(transcript_path, "r", encoding="utf-8") as f:
    for line_num, line in enumerate(f, 1):
        if '"step_index":203' in line or '"step_index":204' in line:
            try:
                obj = json.loads(line)
                step = obj.get('step_index')
                print(f"\n================ STEP {step} ==================")
                content = obj.get('content') or ''
                print(content[:4000])
            except Exception as e:
                pass
