#!/usr/bin/env python3
"""Pre Tool Use Hook - blocks dangerous operations.
Adapted by devkit-ai generate-hooks skill for each target project.
"""
import json, sys, re

BLOCKED_PATTERNS = [
    (r"rm\s+(-[rf]+\s+)*(/|~|\.\.)", "Blocked: destructive rm on root/home"),
    (r"git\s+push\s+.*--force", "Blocked: force push"),
    (r"DROP\s+(TABLE|DATABASE)", "Blocked: destructive SQL"),
]

PROTECTED_FILES = [".env", ".env.local", ".env.production", ".env.staging"]

def check_bash_command(command):
    for pattern, message in BLOCKED_PATTERNS:
        if re.search(pattern, command, re.IGNORECASE):
            return False, message
    return True, ""

def check_file_access(tool_name, file_path):
    if not file_path:
        return True, ""
    for protected in PROTECTED_FILES:
        if file_path.endswith(protected) or f"/{protected}" in file_path:
            if tool_name in ("Write", "Edit"):
                return False, f"Blocked: write access to {protected}"
    return True, ""

def main():
    try:
        hook_input = json.loads(sys.stdin.read())
        tool_name = hook_input.get("tool_name", "")
        tool_input = hook_input.get("tool_input", {})

        if tool_name == "Bash":
            command = tool_input.get("command", "")
            allowed, message = check_bash_command(command)
            if not allowed:
                print(message, file=sys.stderr)
                sys.exit(2)

        if tool_name in ("Write", "Edit", "Read"):
            file_path = tool_input.get("file_path", "")
            allowed, message = check_file_access(tool_name, file_path)
            if not allowed:
                print(message, file=sys.stderr)
                sys.exit(2)

        sys.exit(0)
    except Exception:
        sys.exit(0)

if __name__ == "__main__":
    main()
