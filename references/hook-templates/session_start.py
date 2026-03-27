#!/usr/bin/env python3
"""Session Start Hook - loads project context at session beginning.
Adapted by devkit-ai generate-hooks skill for each target project.
Placeholders: {project_name}
"""
import json, sys, subprocess
from pathlib import Path
from datetime import datetime

PROJECT_ROOT = Path.cwd()

def get_git_info():
    try:
        branch = subprocess.run(["git", "branch", "--show-current"], capture_output=True, text=True, cwd=PROJECT_ROOT).stdout.strip()
        status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True, cwd=PROJECT_ROOT).stdout.strip()
        uncommitted = len([l for l in status.splitlines() if l.strip()]) if status else 0
        return branch, uncommitted
    except Exception:
        return "unknown", 0

def get_active_tasks():
    task_file = PROJECT_ROOT / "TASK.md"
    if not task_file.exists():
        return []
    content = task_file.read_text()
    active = []
    for line in content.splitlines():
        stripped = line.strip()
        if stripped.startswith("- [~]"):
            active.append(stripped[5:].strip())
    return active

def main():
    try:
        hook_input = json.loads(sys.stdin.read())
        branch, uncommitted = get_git_info()
        active_tasks = get_active_tasks()

        output_parts = []
        output_parts.append(f"Project: {PROJECT_ROOT.name}")
        output_parts.append(f"Branch: {branch} | Uncommitted: {uncommitted}")

        if active_tasks:
            output_parts.append(f"Active tasks ({len(active_tasks)}):")
            for task in active_tasks[:5]:
                output_parts.append(f"  [~] {task}")
        else:
            output_parts.append("No active tasks. Check TASK.md Backlog.")

        print("\n".join(output_parts))
        sys.exit(0)
    except Exception:
        sys.exit(0)

if __name__ == "__main__":
    main()
