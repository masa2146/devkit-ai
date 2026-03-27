#!/usr/bin/env python3
"""User Prompt Submit Hook - injects TASK.md context reminder.
Adapted by devkit-ai generate-hooks skill for each target project.
"""
import json, sys
from pathlib import Path

PROJECT_ROOT = Path.cwd()

def get_sprint_summary():
    task_file = PROJECT_ROOT / "TASK.md"
    if not task_file.exists():
        return None
    content = task_file.read_text()
    active = []
    for line in content.splitlines():
        stripped = line.strip()
        if stripped.startswith("- [~]"):
            active.append(stripped[5:].strip())
    if active:
        return f"Reminder: {len(active)} active task(s) in TASK.md: " + ", ".join(active[:3])
    return None

def main():
    try:
        hook_input = json.loads(sys.stdin.read())
        summary = get_sprint_summary()
        if summary:
            print(summary)
        sys.exit(0)
    except Exception:
        sys.exit(0)

if __name__ == "__main__":
    main()
