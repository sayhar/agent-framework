#!/usr/bin/env python3
"""
Pre-commit reminder hook for Claude Code.

Only fires if commit message lacks validation evidence keywords.
Helps agents remember to cite what they tested.
"""

import json
import sys


def main():
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError:
        sys.exit(0)

    command = data.get("tool_input", {}).get("command", "")

    if "git commit" not in command:
        sys.exit(0)

    # Check if commit message cites validation
    validation_keywords = ["tested", "verified", "checked", "confirmed", "validated", "inspected"]
    has_evidence = any(kw in command.lower() for kw in validation_keywords)

    if not has_evidence:
        print("TIP: Cite validation in commit message (e.g., 'tested on 3 files')")

    sys.exit(0)


if __name__ == "__main__":
    main()
