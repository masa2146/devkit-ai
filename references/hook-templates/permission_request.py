#!/usr/bin/env python3
"""Permission Request Hook - auto-allows safe operations, blocks dangerous ones.
Adapted by devkit-ai generate-hooks skill for each target project.
"""
import json, sys, re

SAFE_TOOLS = {"Read", "Glob", "Grep", "WebFetch", "WebSearch", "TodoWrite"}

SAFE_BASH_PATTERNS = [
    r"^ls\b", r"^cat\b", r"^head\b", r"^tail\b", r"^wc\b",
    r"^echo\b", r"^printf\b", r"^pwd$", r"^whoami$",
    r"^git\s+(status|log|diff|branch|show)\b",
    r"^find\b.*-type\b", r"^grep\b", r"^rg\b",
]

DANGEROUS_BASH_PATTERNS = [
    r"rm\s+(-[rf]+\s+)*(/|~)",
    r">\s*\.(env|env\.local|env\.production)",
    r"git\s+push\s+.*--force",
]

def main():
    try:
        hook_input = json.loads(sys.stdin.read())
        tool_name = hook_input.get("tool_name", "")
        tool_input = hook_input.get("tool_input", {})

        # Auto-allow safe tools
        if tool_name in SAFE_TOOLS:
            print(json.dumps({"decision": "allow"}))
            sys.exit(0)

        # Check bash commands
        if tool_name == "Bash":
            command = tool_input.get("command", "")

            # Block dangerous
            for pattern in DANGEROUS_BASH_PATTERNS:
                if re.search(pattern, command, re.IGNORECASE):
                    print(json.dumps({"decision": "deny", "reason": "Dangerous operation blocked"}))
                    sys.exit(0)

            # Allow safe
            for pattern in SAFE_BASH_PATTERNS:
                if re.search(pattern, command):
                    print(json.dumps({"decision": "allow"}))
                    sys.exit(0)

        # Default: ask user
        sys.exit(0)
    except Exception:
        sys.exit(0)

if __name__ == "__main__":
    main()
