# devkit-ai

AI assistant configuration generator plugin for Claude Code and GitHub Copilot.

Generate CLAUDE.md, GEMINI.md, Copilot instructions, .cursorrules, skills, hooks, agents, and TASK.md for any software project — with a single command.

## Installation

### Claude Code

```bash
# From marketplace:
claude marketplace add <marketplace-url>
claude plugin install devkit-ai

# Local development:
claude --plugin-dir ./devkit-ai
```

### GitHub Copilot

```bash
copilot plugin install ./devkit-ai
```

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

## User Configuration

When enabling the plugin, you can configure which agents to generate:

| Config | Description | Default |
|--------|-------------|---------|
| `enable_planner` | Generate planner agent (feature decomposition) | yes |
| `enable_implementer` | Generate implementer agent (code + tests) | yes |
| `enable_reviewer` | Generate reviewer agent (code review) | yes |
| `enable_debugger` | Generate debugger agent (systematic debug) | yes |

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
│   ├── copilot-instructions.md
│   ├── instructions/             # Task-specific instructions
│   ├── skills/                   # Copilot skills
│   └── hooks/                    # Copilot hooks
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
| **Gemini / Antigravity** | GEMINI.md, .agent/skills/ |
| **GitHub Copilot** | .github/copilot-instructions.md, .github/instructions/, .github/skills/, *.agent.md |
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
├── settings.json                 # Default permissions
└── docs/                         # Developer documentation
```

## Migration from Clone-based Usage

If you were using devkit-ai by cloning the repo and running `claude .`:

1. Install as a plugin instead (see Installation above)
2. Use `/devkit-ai:generate-config` instead of manual prompts
3. All functionality is preserved — skills, hooks, agents, references

## License

MIT
