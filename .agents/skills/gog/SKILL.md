---
name: gog
description: >
  Use when the user needs to interact with any Google Workspace service —
  Gmail, Calendar, Drive, Docs, Sheets, Slides, Forms, Apps Script, Contacts,
  Tasks, People, Groups, Keep, or Admin — from the terminal or within an agent
  workflow. Covers reads, writes, searches, audits, and backups.
  The gog binary is installed at: C:\Users\aryan\.gemini\antigravity\bin\gog.exe
---

# gog — Google Workspace CLI Skill

`gog` is a single binary that covers every major Google API with stable JSON/plain-text output designed for terminal use, shell pipelines, CI, and coding agents.

## Binary Location

```
C:\Users\aryan\.gemini\antigravity\bin\gog.exe
```

Always reference the full path or ensure it is on `PATH`. To check it is working:

```powershell
C:\Users\aryan\.gemini\antigravity\bin\gog.exe --version
C:\Users\aryan\.gemini\antigravity\bin\gog.exe auth list --check --json --no-input
C:\Users\aryan\.gemini\antigravity\bin\gog.exe auth doctor --check --json --no-input
```

## First-Time Auth Setup (Human Required Once)

Auth setup requires a browser consent step — the user must do this once per Google account.

```powershell
# Add a Google account with the services you need (narrow scope = safer)
gog.exe auth add you@gmail.com --services gmail,calendar,drive --readonly
gog.exe auth add you@gmail.com --services docs,sheets,slides

# Check auth health
gog.exe auth doctor --check --json
```

Always specify the account explicitly in agent tasks to avoid ambiguity:

```powershell
gog.exe --account you@gmail.com gmail search 'newer_than:7d' --json
```

## Safety Rules (ALWAYS follow these)

- **Never** print or log access tokens, refresh tokens, or OAuth client secrets.
- **Always** use `--no-input` in automated/agent flows so prompts fail clearly rather than hanging.
- **Always** use `--dry-run` first for any write or delete command that supports it.
- **Never** add `--force` unless the user explicitly requested a destructive mutation.
- Use `--gmail-no-send` or `GOG_GMAIL_NO_SEND=1` unless the user specifically asked to send mail.
- Prefer `--json` output for all agent parsing. Human hints go to stderr; stdout is clean data.
- Use narrow service scopes (`--readonly`) when the task only reads.

Runtime command guards (lock down what the agent can do):

```powershell
gog.exe --enable-commands gmail.search,gmail.get --gmail-no-send `
  --account you@gmail.com gmail search 'from:boss@example.com' --json

gog.exe --enable-commands drive.ls,docs.cat --disable-commands drive.delete `
  --account you@gmail.com drive ls --max 10 --json
```

## Common Read Commands

```powershell
# Gmail
gog.exe --account you@gmail.com gmail search 'newer_than:3d' --max 10 --json
gog.exe --account you@gmail.com gmail get <messageId> --sanitize-content --json
gog.exe --account you@gmail.com gmail thread get <threadId> --sanitize-content --json

# Calendar
gog.exe --account you@gmail.com calendar events --today --json
gog.exe --account you@gmail.com calendar events --days 7 --json

# Drive
gog.exe --account you@gmail.com drive ls --max 20 --json
gog.exe --account you@gmail.com drive tree --max-depth 3 --json

# Docs / Sheets / Slides
gog.exe --account you@gmail.com docs cat <documentId> --json
gog.exe --account you@gmail.com sheets get <spreadsheetId> Sheet1!A1:D20 --json

# Contacts / Tasks
gog.exe --account you@gmail.com contacts list --max 20 --json
gog.exe --account you@gmail.com tasks list --json
```

## Common Write Commands

Always prefer `--dry-run` first, then confirm with the user before executing.

```powershell
# Append text to a Google Doc
gog.exe --account you@gmail.com docs write <documentId> --append --text 'My text here'

# Update a cell range in Sheets
gog.exe --account you@gmail.com sheets update <spreadsheetId> Sheet1!A1 --values-json '[[\"value\"]]'

# Upload a file to Drive
gog.exe --account you@gmail.com drive upload .\file.txt --parent <folderId> --json

# Create a calendar event (dry run first)
gog.exe --account you@gmail.com calendar create --dry-run --title "Meeting" --start "2026-05-10T10:00" --end "2026-05-10T11:00" --json
```

## Discovery — When Unsure of Flags

```powershell
gog.exe <service> --help
gog.exe <service> <command> --help
gog.exe schema <service> <command> --json
gog.exe schema --json   # full schema dump
```

Full command index: https://gogcli.sh/commands/

## AIGGPA Project — Specific Use Cases

For this project, `gog` is particularly useful for:

1. **Uploading research files to Drive:**
   ```powershell
   gog.exe --account you@gmail.com drive upload .\AIGGPA_Department_Guide.pdf --parent <folderId> --json
   ```

2. **Updating the Master Tracker in Sheets** (if you migrate it to Google Sheets):
   ```powershell
   gog.exe --account you@gmail.com sheets update <spreadsheetId> Respondent_Log!A2 --values-json '[[\"R001\",\"Revenue\",\"Class III\",\"2026-05-10\"]]'
   ```

3. **Checking your calendar for field visit scheduling:**
   ```powershell
   gog.exe --account you@gmail.com calendar events --days 14 --json
   ```

4. **Sending a bulk summary email after fieldwork:**
   ```powershell
   # Always check with --gmail-no-send first
   gog.exe --account you@gmail.com gmail send --to manager@aiggpa.mp.gov.in --subject "Weekly Fieldwork Update" --body "..." --gmail-no-send
   ```

## Updating

Windows: download the new ZIP from https://github.com/steipete/gogcli/releases and replace `gog.exe` at `C:\Users\aryan\.gemini\antigravity\bin\gog.exe`.

## Reference Links
- Full docs: https://gogcli.sh/
- Command index: https://gogcli.sh/commands/
- Safety profiles: https://gogcli.sh/safety-profiles.html
- Auth setup: https://gogcli.sh/quickstart.html
- GitHub: https://github.com/steipete/gogcli
