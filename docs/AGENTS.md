# AGENTS.md - devkit-ai (Development)

> Cross-platform agent instructions for devkit-ai plugin development.

## Purpose

This plugin generates AI assistant configuration files for any software project.
When a user invokes /devkit-ai:generate-config, follow the skill flow.

## Workflow

1. User provides target directory + project description
2. Analyze target (empty = ask questions, existing = auto-detect)
3. Generate all config files: CLAUDE.md, GEMINI.md, copilot-instructions, .cursorrules
4. Generate skills, hooks, agents for the target project
5. Generate TASK.md with full Backlog/Sprint Board structure
6. Write task-tracking skill so all AI tools manage TASK.md consistently

## Key Rules

- Always follow the skill checklist - no skipping steps
- TASK.md is the Single Source of Truth for project management
- Generate for all 4 platforms unless user specifies otherwise
- Use ${CLAUDE_PLUGIN_ROOT}/references/ templates for consistent quality
- Adapt content to the specific tech stack and features
- Respect userConfig toggles for agent generation
