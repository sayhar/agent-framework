# Oracle Instructions for {PROJECT_NAME}

**Project-specific instructions for code review work.**

For portable oracle role definition, see `oracle.agent.md`.
For project review calibration, see `oracle.context.md`.

---

## Daemon Mode

See `oracle.agent.md` for the daemon loop (reviews queue, wait/claim/respond commands).

**Project-specific notes:**
<!-- Customize: Add any project-specific daemon behavior -->

---

## Review Calibration

<!-- Customize: Add project-specific review focus -->

**DO review for:**
- Silent failures (will it break quietly?)
- Logic correctness
- Evidence-based claims (did they test 3-5 examples?)

**DON'T review for:**
- Test coverage (unless project requires it)
- Comprehensive error handling
- Edge cases that won't happen

---

## Knowledge Base

<!-- Customize: If using oracle/decisions.md and oracle/learnings.md -->
<!-- Add grep patterns specific to your project structure -->
