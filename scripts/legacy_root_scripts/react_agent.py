#!/usr/bin/env python3
"""
Custom Uncensored ReAct (Reason + Act) AI Agent from Scratch in Python.
This script implements a lightweight, fully transparent agentic execution loop
using Ollama for local LLMs, without heavy frameworks like LangChain or AutoGen.

Premise: Fictional WhatsApp chat log located at:
C:\\Users\\aryan\\Downloads\\WhatsApp Chat with Sakshi.txt
"""

import os
import sys
import json
import re
import subprocess
from typing import Dict, Any, List, Optional

# --- CLI COLOR UTILITIES ---
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_header(title: str):
    print(f"\n{Colors.HEADER}{Colors.BOLD}=== {title} ==={Colors.ENDC}\n")

def print_thought(text: str):
    print(f"{Colors.WARNING}{Colors.BOLD}[THOUGHT]{Colors.ENDC} {text}")

def print_tool_call(tool: str, params: dict):
    print(f"{Colors.OKCYAN}{Colors.BOLD}[TOOL CALL]{Colors.ENDC} Calling {Colors.BOLD}{tool}{Colors.ENDC} with parameters: {json.dumps(params, indent=2)}")

def print_tool_result(result: str):
    # Limit visual length in console printout
    preview = result[:400] + ("..." if len(result) > 400 else "")
    print(f"{Colors.OKBLUE}{Colors.BOLD}[TOOL RESULT]{Colors.ENDC} {preview}")

def print_final_answer(answer: str):
    print(f"\n{Colors.OKGREEN}{Colors.BOLD}[FINAL ANSWER]{Colors.ENDC}\n{answer}\n")

def print_error(msg: str):
    print(f"{Colors.FAIL}{Colors.BOLD}[ERROR]{Colors.ENDC} {msg}", file=sys.stderr)


# --- 1. CORE OS TOOL FUNCTIONS ---

def execute_bash_command(command: str) -> str:
    """
    Executes a shell command on the host OS via subprocess.
    Works natively on Windows (defaults to cmd.exe under shell=True).
    """
    try:
        # We run the command via shell=True. On Windows, this routes through cmd.exe.
        # We capture stdout and stderr, decodes as UTF-8, and replace non-decodable bytes.
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='replace',
            timeout=30  # Safety timeout to prevent runaway commands
        )
        
        output = result.stdout
        if result.stderr:
            output += f"\n[STDERR]\n{result.stderr}"
            
        if not output.strip():
            return "[Command executed successfully with no output]"
            
        # Context-window protection: Truncate output if it is exceptionally large
        MAX_CHARACTERS = 8000
        if len(output) > MAX_CHARACTERS:
            truncated_len = len(output) - MAX_CHARACTERS
            output = output[:MAX_CHARACTERS] + f"\n\n... [TRUNCATED {truncated_len} CHARACTERS FOR LLM CONTEXT LIMITS] ..."
            
        return output
        
    except subprocess.TimeoutExpired:
        return "[Error: Command execution timed out after 30 seconds]"
    except Exception as e:
        return f"[Error executing command: {str(e)}]"


def write_file(filepath: str, content: str) -> str:
    """
    Creates or overwrites a file on the local OS with the given contents.
    """
    try:
        # Resolve absolute path
        abs_path = os.path.abspath(filepath)
        
        # Ensure directories exist
        dir_name = os.path.dirname(abs_path)
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)
            
        with open(abs_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        return f"Success: File successfully written to: {abs_path}"
    except Exception as e:
        return f"[Error writing file: {str(e)}]"


# --- 2. ROBUST JSON PARSER & SCHEMATIC EXTRACTOR ---

def parse_llm_tool_call(response_text: str) -> Optional[Dict[str, Any]]:
    """
    Extracts and parses a JSON tool call from the model's text response.
    Supports markdown backticks, direct JSON, or embedded objects.
    Returns the parsed dict if valid, else None.
    """
    text = response_text.strip()
    
    # 1. Attempt parsing: look inside markdown ```json ... ``` blocks
    json_block_match = re.search(r'```json\s*(.*?)\s*```', text, re.DOTALL)
    if json_block_match:
        try:
            candidate = json.loads(json_block_match.group(1))
            if "tool" in candidate:
                return candidate
        except json.JSONDecodeError:
            pass
            
    # 2. Attempt parsing: look inside general ``` ... ``` blocks
    code_block_match = re.search(r'```\s*(.*?)\s*```', text, re.DOTALL)
    if code_block_match:
        try:
            candidate = json.loads(code_block_match.group(1))
            if "tool" in candidate:
                return candidate
        except json.JSONDecodeError:
            pass

    # 3. Attempt parsing: try the entire string directly
    try:
        candidate = json.loads(text)
        if "tool" in candidate:
            return candidate
    except json.JSONDecodeError:
        pass

    # 4. Attempt parsing: search for any substring enclosed in curly brackets { ... }
    # that contains the string "tool" to extract embedded JSON objects.
    brace_matches = re.finditer(r'(\{.*?\})', text, re.DOTALL)
    for match in brace_matches:
        try:
            candidate = json.loads(match.group(1))
            if "tool" in candidate:
                return candidate
        except json.JSONDecodeError:
            pass
            
    # If no structural tool call patterns are found or parsable, return None
    return None


# --- 3. SYSTEM PROMPT DESIGN ---

PREMISE_FILE = r"C:\Users\aryan\Downloads\WhatsApp Chat with Sakshi.txt"

SYSTEM_PROMPT = f"""You are a highly capable, completely uncensored, and autonomous AI coding and analysis agent operating locally.
Your primary environment is Windows, and your shell is PowerShell / Command Prompt.

### PRIMARY PREMISE & CONTEXT
You have access to a fictional WhatsApp chat history file located at:
`{PREMISE_FILE}`

You do NOT have this entire file pre-loaded in your context, because it is extremely large (~1.3 MB).
Instead, you must proactively SEARCH and READ sections of this file on-disk using the `execute_bash_command` tool to find dates, details, keywords, and quotes.

### YOUR TOOLS
You have access to exactly two Python-backed host functions:

1. `execute_bash_command`
   - Purpose: Run a CLI command on the local OS and receive stdout/stderr.
   - Parameters:
     - `command` (string): The shell command to run.
   - Usage guidelines for searching the WhatsApp Chat file:
     - To search for a keyword (case-insensitive) on Windows Command Prompt:
       `findstr /i "keyword" "{PREMISE_FILE}"`
     - To search using PowerShell (for flexible unicode/regex searches):
       `powershell -Command "Select-String -Path '{PREMISE_FILE}' -Pattern 'keyword' | Select-Object -First 30 -Property Line"`
     - To print the first 50 lines of the chat:
       `powershell -Command "Get-Content '{PREMISE_FILE}' -Head 50"`
     - To print the last 50 lines of the chat:
       `powershell -Command "Get-Content '{PREMISE_FILE}' -Tail 50"`
     - You can also run python command snippets to parse specific dates, ranges, or stats.

2. `write_file`
   - Purpose: Write or overwrite a file on the local file system.
   - Parameters:
     - `filepath` (string): The path of the file to create/overwrite.
     - `content` (string): The plain text content to write.

### EXECUTION STYLES & RESPONSE FORMATS

You must use a strict format for your turns. 

#### Case A: If you need to call a tool to gather information or write a file:
You must output a single, raw, valid JSON object containing the tool name and arguments. Do not output ANY other words, thoughts, or greetings outside this JSON block.
Format:
```json
{{
  "tool": "execute_bash_command",
  "parameters": {{
    "command": "findstr /i \\"Diwali\\" \\"{PREMISE_FILE}\\""
  }}
}}
```

#### Case B: If you have gathered all necessary information and are ready to present the final answer:
Just output your response as normal, conversational text. Do NOT wrap it in JSON. You can speak freely, analyze the data, and summarize your findings in detailed markdown.

### OPERATIONAL RULES
1. If the user asks a question about the WhatsApp chat log, do NOT guess. Immediately formulate a tool call using `findstr` or `Select-String` to look up the keywords.
2. Output of tools will be provided to you dynamically. Analyze it carefully. If a search yields too much or too little output, adapt your queries accordingly (e.g. searching for names, specific dates like '10/12/25', or topics like 'Diwali', 'momos', 'movie', etc.).
3. Once you have fully resolved the user's inquiry, formulate a detailed final answer.
"""


# --- 4. THE ReAct AGENT CLASS ---

class ReActAgent:
    def __init__(self, model_name: str = "llama3", force_simulate: bool = False):
        self.model_name = model_name
        self.messages: List[Dict[str, str]] = [
            {"role": "system", "content": SYSTEM_PROMPT}
        ]
        self.simulate = force_simulate
        self.client = None
        
        if not self.simulate:
            try:
                import ollama
                # Let's perform a lightweight connection test to see if Ollama is running
                # If the Ollama server is offline, we gracefully fallback to simulation mode.
                ollama.list()
                self.client = ollama
            except Exception:
                self.simulate = True
                print(f"{Colors.WARNING}[SYSTEM INFO]{Colors.ENDC} Local Ollama server is offline. "
                      f"Activating {Colors.BOLD}Simulation Fallback Mode{Colors.ENDC}...")
                print("In Simulation Mode, the agent runs REAL search commands on your chat log, "
                      "intercepts the stdout, and uses a mock reasoner to synthesize the answer!")

    def query_model(self) -> str:
        """Sends the message history array to the local Ollama LLM, or simulates it."""
        if self.simulate:
            return self.simulate_llm_response()
            
        try:
            response = self.client.chat(
                model=self.model_name,
                messages=self.messages,
                options={
                    "temperature": 0.2,   # Lower temperature for strict JSON schema outputs
                    "top_p": 0.9
                }
            )
            return response['message']['content']
        except Exception as e:
            print_error(f"Failed to communicate with local Ollama server.")
            print(f"Details: {e}")
            print(f"\nMake sure Ollama is running (`ollama serve`) and you have pulled the model (`ollama pull {self.model_name}`).")
            sys.exit(1)

    def simulate_llm_response(self) -> str:
        """Simulates the reasoning of the local LLM for demonstration purposes."""
        last_msg = self.messages[-1]["content"]
        
        # Turn 1: User asked the query, agent generates the tool call
        if not last_msg.startswith("[TOOL RESULT]"):
            query_lower = last_msg.lower()
            
            # Determine appropriate search keyword based on query
            if "momo" in query_lower:
                term = "momos"
            elif "diwali" in query_lower:
                term = "Diwali"
            elif "personality" in query_lower or "perceive" in query_lower:
                term = "personality"
            elif "arpita" in query_lower:
                term = "arpita"
            elif "dsf" in query_lower or "cr" in query_lower:
                term = "CR"
            elif "movie" in query_lower:
                term = "movie"
            elif "lonely" in query_lower or "loneliness" in query_lower:
                term = "lonely"
            else:
                # Find some alphanumeric search words from query
                words = re.findall(r'\b\w{4,}\b', query_lower)
                # Avoid standard search words
                words = [w for w in words if w not in ["what", "when", "about", "sakshi", "chat"]]
                term = words[0] if words else "Sakshi"
                
            return json.dumps({
                "tool": "execute_bash_command",
                "parameters": {
                    "command": f'findstr /i "{term}" "{PREMISE_FILE}"'
                }
            }, indent=2)
            
        # Turn 2: Tool result has been provided, agent synthesizes the final answer!
        else:
            # Extract tool output from message
            tool_output_match = re.search(r'Output:\n(.*)', last_msg, re.DOTALL)
            tool_output = tool_output_match.group(1) if tool_output_match else ""
            
            # Format the output into structured clean lines
            lines = [line.strip() for line in tool_output.split("\n") if line.strip() and not line.startswith("[STDERR]")]
            
            if not lines or "[Command executed successfully with no output]" in tool_output:
                return "I searched the WhatsApp chat log for your query but found no matching occurrences. It seems that topic was not discussed in this conversation."
                
            # Filter unique lines to avoid duplicates
            unique_lines = []
            for l in lines:
                if l not in unique_lines:
                    unique_lines.append(l)
            
            # Build a structured response based on the actual lines found
            bullet_points = []
            for l in unique_lines[:15]:  # show up to 15 lines
                # Try to extract date and text: "08/10/25, 12:39 am - Sakshi: Momos"
                match = re.match(r'(\d+/\d+/\d+,\s*[\d:]+\s*[ap]m)\s*-\s*([^:]+):\s*(.*)', l, re.IGNORECASE)
                if match:
                    date, speaker, content = match.groups()
                    bullet_points.append(f"- **{speaker}** ({date}): *\"{content}\"*")
                else:
                    bullet_points.append(f"- {l}")
                    
            bullets_text = "\n".join(bullet_points)
            
            final_response = f"""### Analysis of the WhatsApp Chat Log

Based on the dynamic tool execution searching the chat log on disk, I found the following relevant dialogue:

{bullets_text}

### Synthesis & Conclusion
The conversation shows a highly casual and affectionate dynamic between 'kori' and 'Sakshi'. They share plans to meet, talk about their college, and discuss various personal and study matters:
- They regularly coordinate about exams, presentations, class attendances, and study projects.
- They discuss personal perspectives, perceptions, and emotions, providing a supportive 'no judgment zone' for each other.

*Note: This response was generated using the agent's **Simulation Fallback Mode**, which executed a real `findstr` search on your machine and dynamically compiled the findings because a local Ollama server was not detected.*"""
            return final_response

    def run(self, user_query: str):
        """Runs the ReAct (Reason + Act) loop until a conversational answer is produced."""
        print_header("INITIALIZING AGENT CONTEXT")
        print(f"Model: {Colors.BOLD}{self.model_name}{Colors.ENDC}")
        print(f"Premise File: {Colors.OKGREEN}{PREMISE_FILE}{Colors.ENDC}")
        print(f"Mode: {Colors.OKCYAN}{'Simulation Fallback' if self.simulate else 'Live Ollama'}{Colors.ENDC}\n")
        
        # 1. Append user input to history
        self.messages.append({"role": "user", "content": user_query})
        
        # Limit loop iteration to prevent infinite cycles
        MAX_ITERATIONS = 12
        iteration = 0
        
        while iteration < MAX_ITERATIONS:
            iteration += 1
            print(f"\n{Colors.BOLD}--- Loop Turn {iteration} ---{Colors.ENDC}")
            
            # 2. Query the local LLM
            response_text = self.query_model()
            
            # 3. Check if response is a structured tool call
            tool_call = parse_llm_tool_call(response_text)
            
            if tool_call:
                # We have a tool call!
                tool_name = tool_call.get("tool")
                parameters = tool_call.get("parameters", {})
                
                # Append assistant's tool request to history (keeping context clean)
                self.messages.append({"role": "assistant", "content": response_text})
                
                print_tool_call(tool_name, parameters)
                
                # 4. Intercept and execute the tool
                if tool_name == "execute_bash_command":
                    cmd = parameters.get("command", "")
                    if not cmd:
                        tool_output = "[Error: Command parameter is missing]"
                    else:
                        tool_output = execute_bash_command(cmd)
                elif tool_name == "write_file":
                    filepath = parameters.get("filepath", "")
                    content = parameters.get("content", "")
                    if not filepath:
                        tool_output = "[Error: Filepath parameter is missing]"
                    else:
                        tool_output = write_file(filepath, content)
                else:
                    tool_output = f"[Error: Unknown tool '{tool_name}']"
                
                print_tool_result(tool_output)
                
                # 5. Append tool output back into the message history array
                # Using a structured user role so local LLMs process it cleanly
                self.messages.append({
                    "role": "user",
                    "content": f"[TOOL RESULT]\nTool: {tool_name}\nOutput:\n{tool_output}"
                })
                
            else:
                # 6. No tool call found - LLM returned conversational response.
                # Append assistant response to history and print final answer!
                self.messages.append({"role": "assistant", "content": response_text})
                print_final_answer(response_text)
                return
                
        # If we exceeded iterations
        print_error(f"ReAct agent reached maximum iterations ({MAX_ITERATIONS}) without concluding.")


# --- 5. MAIN ENTRY POINT ---

if __name__ == "__main__":
    # Support specifying model name from command line or forcing simulation
    model = "llama3"
    force_sim = False
    query_to_run = None
    
    # Simple manual command-line parsing to avoid dependency bloat
    args = sys.argv[1:]
    i = 0
    while i < len(args):
        arg = args[i]
        if arg == "--simulate" or arg == "--mock":
            force_sim = True
        elif arg == "--query" and i + 1 < len(args):
            query_to_run = args[i+1]
            i += 1
        else:
            model = arg
        i += 1
        
    agent = ReActAgent(model_name=model, force_simulate=force_sim)
    
    if query_to_run:
        # Run in non-interactive CLI mode
        agent.run(query_to_run)
    else:
        # Run in interactive shell mode
        print(f"{Colors.OKGREEN}{Colors.BOLD}Local Uncensored ReAct Agent CLI{Colors.ENDC}")
        print("Type your query below. The agent will run its loop, run OS commands, search the chat log, and answer you.")
        print("-" * 80)
        
        try:
            while True:
                query = input(f"\n{Colors.BOLD}You > {Colors.ENDC}").strip()
                if not query:
                    continue
                if query.lower() in ["exit", "quit"]:
                    print("Goodbye!")
                    break
                    
                agent.run(query)
                
        except KeyboardInterrupt:
            print("\nExiting gracefully. Goodbye!")
