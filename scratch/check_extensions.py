import json

with open("Organized_Archive/discovered_commands.json", encoding="utf-8") as f:
    data = json.load(f)

keywords = ["python", "prettier", "black", "isort", "git", "latex", "eslint", "formatter"]
print("Available Automated Tools via VS Code Extensions:\n")

for ext_id, info in data.items():
    ext_lower = ext_id.lower()
    if any(k in ext_lower for k in keywords):
        cmds = info.get("commands", [])
        if cmds:
            print(f"### {info.get('displayName', ext_id)} (`{ext_id}`)")
            print(f"Description: {info.get('description', 'N/A')}")
            print("Commands:")
            # Display up to 6 relevant commands
            for cmd in cmds[:6]:
                print(f"  - `{cmd['command_id']}`: {cmd.get('description', '')}")
            if len(cmds) > 6:
                print(f"  - ... and {len(cmds) - 6} more commands")
            print()
