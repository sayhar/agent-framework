# Meta Instructions for {PROJECT_NAME}

**Project-specific instructions for meta-engineering work.**

For portable meta role definition, see `meta.agent.md`.
For file structure documentation, see `agents/README.md`.

---

## Bootup File Size Limits

Target sizes (these load every session):
- `*.agent.md`: <100 lines
- `this.*.agent.md`: <80 lines
- `*.context.md`: <100 lines

If exceeded: refactor for conciseness, move details to `agents/README.md` or oracle's knowledge base.
