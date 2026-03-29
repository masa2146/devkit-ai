# devkit-ai

AI assistant configuration generator plugin for Claude Code.

Generate CLAUDE.md, GEMINI.md, Copilot instructions, .cursorrules, skills, hooks, agents, and TASK.md for any software project — with a single command.

## Installation

### Local Development (Test)

```bash
claude --plugin-dir ./devkit-ai
```

### From a Marketplace

If this plugin is published to a marketplace repository, install with:

```bash
# Add the marketplace (one-time)
/plugin install devkit-ai@<marketplace-name>
```

Or use the `/plugin` Discover tab inside Claude Code.

## Usage

After installing the plugin, use the namespaced skill:

```
/devkit-ai:generate-config /path/to/my-project
```

### Examples

**New project (empty directory):**
```
/devkit-ai:generate-config /Users/me/projects/my-ecommerce
> React + FastAPI + PostgreSQL ile e-ticaret projesi
```

**Existing project (auto-detect):**
```
/devkit-ai:generate-config /Users/me/projects/existing-app
```

## What Gets Generated

For a React + FastAPI + PostgreSQL web-app with auth and API features:

```
target-project/
├── CLAUDE.md                     # Claude Code instructions
├── GEMINI.md                     # Gemini instructions
├── TASK.md                       # Backlog/Sprint Board
├── .cursorrules                  # Cursor rules
│
├── .claude/
│   ├── settings.local.json       # Hook configuration
│   ├── skills/                   # 6-10 skills
│   ├── hooks/                    # 5 hook scripts
│   └── agents/                   # 4 agent definitions
│
├── .github/
│   ├── copilot-instructions.md   # Workspace instructions
│   └── instructions/             # Task-specific instructions
│
├── .agent/skills/                # Gemini skills
│
├── planner.agent.md              # Copilot agents
├── implementer.agent.md
├── reviewer.agent.md
└── debugger.agent.md
```

## Supported Platforms

| Platform | Outputs |
|----------|---------|
| **Claude Code** | CLAUDE.md, .claude/skills/, .claude/hooks/, .claude/agents/ |
| **Gemini** | GEMINI.md, .agent/skills/ |
| **GitHub Copilot** | .github/copilot-instructions.md, .github/instructions/, *.agent.md |
| **Cursor** | .cursorrules |

## Skills Generated

| Skill | Condition | Purpose |
|-------|-----------|---------|
| task-tracking | Always | TASK.md management (Single Source of Truth) |
| code-standards | Always | Coding conventions |
| testing-strategy | Always | Test approach |
| git-workflow | Always | Git conventions |
| architecture-guide | Always | Architecture patterns |
| deployment-guide | Always | Deployment procedures |
| api-conventions | API feature | REST/GraphQL patterns |
| security-checklist | Auth feature | OWASP security |
| database-guide | Database present | Schema/migration conventions |
| docker-guide | Docker deployment | Docker best practices |

## TASK.md

TASK.md is not a simple checklist. It's a full **Backlog/Sprint Board**:

- **Epics**: Feature-based grouping
- **Current Sprint**: Active tasks (max 5)
- **Backlog**: Prioritized (High/Medium/Low)
- **Completed**: With timestamps
- **Decisions Log**: Technical decisions + rationale
- **Session Log**: AI agent activity tracking

Every AI tool uses TASK.md as the **Single Source of Truth** via the `task-tracking` skill.

## Plugin Structure

```
devkit-ai/
├── .claude-plugin/plugin.json    # Plugin manifest
├── skills/                       # 7 skills (SKILL.md format)
├── agents/                       # Config generator agent
├── hooks/hooks.json              # Hook configuration
├── scripts/                      # Hook scripts
├── references/                   # Templates and best practices
└── docs/                         # Developer documentation
```

## License

MIT
