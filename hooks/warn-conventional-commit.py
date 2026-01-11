#!/usr/bin/env python3
"""
Warn if commit message doesn't follow conventional commit format.

Soft reminder, not blocking. Conventional format: feat:|fix:|refactor:|docs:|chore:|test:
"""

import json
import sys
import re


def main():
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError:
        sys.exit(0)

    command = data.get("tool_input", {}).get("command", "")

    if "git commit" not in command:
        sys.exit(0)

    # Check for conventional commit prefix
    conventional_prefixes = r"(feat|fix|refactor|docs|chore|test|style|perf|ci|build|revert):"

    if not re.search(conventional_prefixes, command, re.IGNORECASE):
        print("TIP: Use conventional commit format (feat:|fix:|refactor:|docs:|chore:|test:)")

    sys.exit(0)


if __name__ == "__main__":
    main()
