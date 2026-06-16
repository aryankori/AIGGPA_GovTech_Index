import os
import json
from openai import OpenAI

# 1. Connect to your local model
client = OpenAI(
    base_url="http://localhost:1234/v1", # Change to http://localhost:11434/v1 if using Ollama
    api_key="not-needed"
)

# ==============================================================================
# 2. WRITE YOUR SYSTEM PROMPT HERE (The Rules & Format)
# ==============================================================================
SYSTEM_PROMPT = """
You are an expert analyst for the AIGGPA Project.
You must output your response as a valid, parsable JSON object.
Do not include any greeting, explanation, or conversational text. Output ONLY the JSON object.

Format your JSON exactly like this:
{
  "summary": "A one-sentence summary of the feedback.",
  "department": "The name of the department mentioned.",
  "issue_type": "Technical, Training, or Unknown"
}
""".strip()

# ==============================================================================
# 3. WRITE YOUR USER INPUT HERE (The Data to Analyze)
# ==============================================================================
USER_INPUT = """
The rural development department recently deployed a new digital tracking tool, but many field agents are reporting that the offline sync feature fails when they are in remote villages without cell service.
""".strip()

def run_my_prompt():
    print("Sending your prompt to the local model...\n")
    
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": USER_INPUT}
    ]

    try:
        response = client.chat.completions.create(
            model="local-model", 
            messages=messages,
            temperature=0.3, # Keep this low (0.1 - 0.3) for strict formatting like JSON
        )
        
        reply = response.choices[0].message.content
        print("--- MODEL OUTPUT ---")
        print(reply)
        print("--------------------")
        
    except Exception as e:
        print(f"Error: Could not connect to the local model. Details: {e}")

if __name__ == "__main__":
    run_my_prompt()
