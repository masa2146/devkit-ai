#!/usr/bin/env python3
"""devkit-ai User Prompt Submit Hook.
Detects generation requests and reminds about the generate-config skill.
"""
import json
import sys


GENERATION_KEYWORDS = [
    "config olustur", "config oluştur", "generate config",
    "ai config", "setup ai", "proje olustur", "proje oluştur",
    "create project", "scaffold", "devkit",
    "skill olustur", "skill oluştur", "hook olustur", "hook oluştur",
]


def main():
    try:
        hook_input = json.loads(sys.stdin.read())
        prompt = hook_input.get("prompt", "").lower()

        for keyword in GENERATION_KEYWORDS:
            if keyword in prompt:
                print(
                    "Reminder: Use /devkit-ai:generate-config for AI config generation. "
                    "Follow the skill checklist step by step."
                )
                break

        sys.exit(0)
    except Exception:
        sys.exit(0)


if __name__ == "__main__":
    main()
