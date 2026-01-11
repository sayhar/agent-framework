#!/usr/bin/env python3
"""
Post-commit Oracle reminder hook for Claude Code.

Nudges agents to consider Oracle review after significant commits.
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

    # Only nudge for feature/refactor commits (not docs/chore)
    significant = any(kw in command.lower() for kw in ["feat", "refactor", "fix"])

    if significant:
        print("TIP: Consider Oracle review for significant changes.")

    sys.exit(0)


if __name__ == "__main__":
    main()
