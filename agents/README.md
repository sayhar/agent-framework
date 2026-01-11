# Agent System Architecture

This directory contains the agent coordination system.

## File Structure

**Portable files** (copy to new projects):
- `{role}.agent.md` - Role instructions (HOW to be this role)
- `principles/` - Universal methodology

**Project-specific files** (customize per project):
- `this.{role}.agent.md` - Project instructions for this role
- `{role}.context.md` - Project facts for this role
- `base.context.md` - Project-wide facts

**State files** (runtime):
- `state/inboxes/` - Agent communication
- `state/sessions/` - Session logs and handoffs

## Instructions vs Data

- **Instructions** (`*.agent.md`): HOW to work, WHEN to do things, WHAT to avoid
- **Data** (`*.context.md`): WHAT the current structure is, WHAT the workflow is

Why separate? Instructions are stable and portable. Data changes per project.

## Agent Types

Common patterns (define in `base.context.md`):

- **engineer** — Executes implementation
- **oracle** — Reviews code, critiques, suggests improvements
- **architect** — Plans with the user, designs approaches (if needed)
- **meta** — Works on the agent system itself

Each agent type has:
- `{type}.agent.md` - Portable role definition
- `this.{type}.agent.md` - Project-specific instructions
- `{type}.context.md` - Project-specific facts

## Setup for New Projects

1. Copy `agents/` directory
2. Customize `*.context.md` files for your project
3. Customize `this.*.agent.md` files for project-specific workflows
4. Update `.claude/CLAUDE.md` to route to correct files
