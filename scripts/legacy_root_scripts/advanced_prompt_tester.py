import os
from openai import OpenAI

# Initialize the client pointing to your local model
client = OpenAI(
    base_url="http://localhost:1234/v1", # Adjust if using Ollama (http://localhost:11434/v1)
    api_key="not-needed"
)

def run_test(test_name, system_prompt, user_prompt):
    print(f"\n{'='*50}")
    print(f"TESTING: {test_name}")
    print(f"{'='*50}")
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
    
    try:
        response = client.chat.completions.create(
            model="local-model",
            messages=messages,
            temperature=0.3, # Low temperature for more logical, structured output
            max_tokens=300
        )
        print("\n--- MODEL RESPONSE ---")
        print(response.choices[0].message.content)
        print("----------------------\n")
    except Exception as e:
        print(f"Connection Error: Ensure your local model is running. Details: {e}")

def run_all_tests():
    # ---------------------------------------------------------
    # TEST 1: The "Bad" Basic Prompt
    # ---------------------------------------------------------
    # This is how most people prompt: vague instructions, no formatting constraints.
    run_test(
        test_name="1. Basic / Vague Prompt",
        system_prompt="You are a helpful assistant.",
        user_prompt="Extract the key entities from this text: 'The AIGGPA project evaluated the rural development department in Madhya Pradesh. 450 users were surveyed.'"
    )

    # ---------------------------------------------------------
    # TEST 2: XML Tagging for Structured Data
    # ---------------------------------------------------------
    # Advanced models (and even 8B/70B local models) parse XML tags very well.
    # It allows you to strictly separate instructions, data, and output formats.
    xml_system_prompt = """
You are a Data Extraction Assistant. Your job is to strictly follow the extraction rules.
<rules>
1. Identify the project name, department, location, and survey count.
2. If a value is missing, output 'N/A'.
3. Do not include conversational filler in your response.
</rules>

<output_format>
Return the data in the following XML structure:
<extraction>
    <project>...</project>
    <department>...</department>
    <location>...</location>
    <survey_count>...</survey_count>
</extraction>
</output_format>
    """.strip()
    
    xml_user_prompt = """
<input_text>
The AIGGPA project evaluated the rural development department in Madhya Pradesh. 450 users were surveyed.
</input_text>
    """.strip()
    
    run_test(
        test_name="2. XML-Structured Prompt",
        system_prompt=xml_system_prompt,
        user_prompt=xml_user_prompt
    )

    # ---------------------------------------------------------
    # TEST 3: Few-Shot + Chain of Thought (CoT)
    # ---------------------------------------------------------
    # By providing examples (Few-Shot) and forcing the model to think out loud (CoT),
    # you drastically reduce hallucinations on complex logic.
    cot_system_prompt = """
You are an expert analyst. You will be given a sentiment statement.
First, analyze the sentiment step-by-step inside <scratchpad> tags.
Then, output your final classification inside <sentiment> tags (Positive, Negative, or Neutral).

<examples>
  <example>
    <input>The new portal is fast, but the login keeps crashing.</input>
    <scratchpad>The user mentions speed as a positive, but a crashing login is a critical functional failure. Functional failures heavily outweigh speed.</scratchpad>
    <sentiment>Negative</sentiment>
  </example>
</examples>
    """.strip()
    
    cot_user_prompt = "<input>The staff training for the digital tools was very informative, though it took up the whole afternoon.</input>"
    
    run_test(
        test_name="3. Few-Shot + Chain-of-Thought (CoT)",
        system_prompt=cot_system_prompt,
        user_prompt=cot_user_prompt
    )

if __name__ == "__main__":
    run_all_tests()
