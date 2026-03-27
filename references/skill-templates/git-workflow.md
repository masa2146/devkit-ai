---
name: git-workflow
description: Use when creating branches, making commits, or managing pull requests.
---

# git-workflow - Git Conventions

## Branch Naming
- Feature: `feature/{epic-number}-{short-description}`
- Bugfix: `bugfix/{task-id}-{short-description}`
- Hotfix: `hotfix/{description}`
- Release: `release/{version}`

## Commit Messages (Conventional Commits)
```
{type}({scope}): {description}

{optional body}
```

Types: feat, fix, docs, style, refactor, test, chore, ci
Scope: feature name or module

Examples:
- `feat(auth): add JWT token refresh`
- `fix(api): handle null response in product list`
- `test(auth): add login integration tests`

## PR Rules
- Title matches commit convention
- Description references Epic/Task from TASK.md
- All tests pass
- Linter passes
- At least 1 review approval

## Rules
- DO: Commit early, commit often (atomic commits)
- DO: Write meaningful commit messages
- DO: Reference TASK.md tasks in commits
- DO NOT: Force push to shared branches
- DO NOT: Commit .env files
- DO NOT: Mix unrelated changes in one commit
