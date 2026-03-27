# Copilot Instructions - devkit-ai (Development)

This plugin is an AI config generator. It creates AI assistant configuration files
(CLAUDE.md, GEMINI.md, copilot-instructions, .cursorrules, skills, hooks, agents, TASK.md)
for any software project.

## How to Use

When a user asks to generate config for a project, follow the generate-config skill:
1. Get target directory and project info
2. Analyze target (empty dir = ask questions, existing code = auto-detect)
3. Generate platform docs (CLAUDE.md, GEMINI.md, copilot-instructions, .cursorrules)
4. Generate skills (task-tracking, code-standards, testing-strategy, etc.)
5. Generate hooks (session_start, pre_tool_use, post_tool_use, etc.)
6. Generate agents (planner, implementer, reviewer, debugger)
7. Generate TASK.md with Backlog/Sprint Board + task-tracking skill

## Key Rules

- TASK.md = Single Source of Truth for project management
- Generate for all platforms: Claude Code, Gemini, Copilot, Cursor
- Use references/ templates for consistent output quality
- Adapt all content to the specific tech stack and project features
