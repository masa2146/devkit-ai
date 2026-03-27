#!/usr/bin/env python3
"""Pre Compact Hook - backs up context before compaction.
Adapted by devkit-ai generate-hooks skill for each target project.
"""
import json, sys
from pathlib import Path
from datetime import datetime

def main():
    try:
        hook_input = json.loads(sys.stdin.read())
        # Optional: backup transcript before compaction
        # backup_dir = Path.cwd() / ".claude" / "backups"
        # backup_dir.mkdir(parents=True, exist_ok=True)
        # timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        # backup_file = backup_dir / f"pre_compact_{timestamp}.json"
        # backup_file.write_text(json.dumps(hook_input, indent=2))
        sys.exit(0)
    except Exception:
        sys.exit(0)

if __name__ == "__main__":
    main()
