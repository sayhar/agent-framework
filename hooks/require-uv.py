#!/usr/bin/env python3
"""
Require uv hook for Claude Code.

Blocks direct python/python3 commands - must use 'uv run python' instead.
This ensures consistent environment and dependency management.
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

    # Check for direct python usage (not via uv)
    # Match: python3 ..., python ..., but NOT: uv run python
    if re.match(r"^python3?\s", command) and "uv run" not in command:
        print(
            json.dumps(
                {
                    "hookSpecificOutput": {
                        "hookEventName": "PreToolUse",
                        "permissionDecision": "deny",
                        "permissionDecisionReason": "Use 'uv run python' instead of 'python3'. This ensures correct environment.",
                    }
                }
            )
        )
        sys.exit(0)

    sys.exit(0)


if __name__ == "__main__":
    main()
