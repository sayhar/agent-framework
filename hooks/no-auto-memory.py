#!/usr/bin/env python3
"""
Block writes to an agent's auto-memory directory.

Persistent state belongs in instruction files or inbox, not automated memory files.
"""

import json
import sys


def main():
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError:
        sys.exit(0)

    file_path = data.get("tool_input", {}).get("file_path", "")

    # Check for both Claude and Gemini memory paths
    is_claude_memory = "/.claude/" in file_path and "/memory/" in file_path
    is_gemini_memory = "/.gemini/" in file_path and "/memory/" in file_path

    if not (is_claude_memory or is_gemini_memory):
        sys.exit(0)

    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": (
                "Don't use auto-memory. Instead: "
                "(1) edit an instruction file (this.*.agent.md, *.context.md, principles/) or "
                "(2) send meta an inbox message to make the change."
            ),
        }
    }))
    sys.exit(0)


if __name__ == "__main__":
    main()
