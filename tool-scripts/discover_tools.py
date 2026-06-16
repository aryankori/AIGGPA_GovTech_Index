import os
import json
import pathlib
from typing import Dict, List, Any

def discover_extension_commands(extensions_dir: str) -> Dict[str, Any]:
    """
    Parses the given IDE extensions directory, scanning each extension's 
    package.json to extract contributed commands and descriptions.
    """
    command_map = {}
    ext_path = pathlib.Path(extensions_dir).expanduser().resolve()
    
    if not ext_path.exists():
        print(f"Error: Directory not found at {ext_path}")
        return {}

    # Iterate through every item in the extensions directory
    for item in ext_path.iterdir():
        if item.is_dir():
            package_json_path = item / "package.json"
            
            if package_json_path.exists():
                try:
                    with open(package_json_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    
                    # Extract extension metadata
                    ext_name = data.get("name", item.name)
                    ext_publisher = data.get("publisher", "unknown")
                    ext_id = f"{ext_publisher}.{ext_name}"
                    
                    # Check for contributed commands
                    contributes = data.get("contributes", {})
                    commands = contributes.get("commands", [])
                    
                    if commands:
                        command_map[ext_id] = {
                            "displayName": data.get("displayName", ext_name),
                            "description": data.get("description", ""),
                            "version": data.get("version", "0.0.0"),
                            "commands": []
                        }
                        
                        # Extract individual command details
                        for cmd in commands:
                            cmd_id = cmd.get("command")
                            cmd_title = cmd.get("title")
                            cmd_category = cmd.get("category", "")
                            
                            # Construct a clean, human-readable full title
                            full_title = f"[{cmd_category}] {cmd_title}" if cmd_category else cmd_title
                            
                            if cmd_id:
                                command_map[ext_id]["commands"].append({
                                    "command_id": cmd_id,
                                    "description": full_title
                                })
                                
                except (json.JSONDecodeError, OSError) as e:
                    # Skip malformed or unreadable package.json files gracefully
                    continue

    return command_map

if __name__ == "__main__":
    # Default paths for standard VS Code-compatible extension setups
    # Adjust this path if Antigravity utilizes a custom environment directory
    default_paths = [
        "~/.vscode/extensions",
        "~/.antigravity/extensions" 
    ]
    
    discovered_data = {}
    for path in default_paths:
        resolved = pathlib.Path(path).expanduser()
        if resolved.exists():
            print(f"Scanning extensions in: {resolved}")
            discovered_data = discover_extension_commands(str(resolved))
            break
            
    # Output the results to a structured JSON file for the agent to read
    output_file = "discovered_commands.json"
    with open(output_file, "w", encoding="utf-8") as out:
        json.dump(discovered_data, out, indent=2)
        
    print(f"\nSuccess! Found {len(discovered_data)} extensions with executable commands.")
    print(f"Command map saved directly to: {os.path.abspath(output_file)}")
