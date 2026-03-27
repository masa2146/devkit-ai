---
name: task-tracking
description: Use ALWAYS before starting any work and after completing any task. Manages TASK.md as the project's Single Source of Truth.
---

# task-tracking - TASK.md Management

## ABSOLUTE RULES

1. **READ TASK.md BEFORE every operation**
2. **UPDATE TASK.md AFTER every operation**
3. These rules are NON-NEGOTIABLE - always apply

## Task Lifecycle

### Starting a Task
1. Read TASK.md
2. Find the task to work on
3. Change status to `[~]`
4. Add to Current Sprint table (with date)
5. Begin work

### Completing a Task
1. Change status to `[x]`
2. Move to Completed section (with date)
3. Remove from Current Sprint table
4. Add Session Log entry

### Task Blocked
1. Change status to `[!]`
2. Write detail in Notes > Active Blockers
3. Specify resolution plan
4. Move to another task

### New Task Discovered
1. Add to relevant Epic or Backlog
2. Set priority (High/Medium/Low)
3. If larger than 4 hours -> split into smaller tasks

### Making a Decision
1. Write in Decisions Log
2. Fill: Date, Decision, Rationale, Impact

### Code Review
1. Change task to `[?]`
2. Write review result in Notes
3. If approved: `[?]` -> `[x]`
4. If changes needed: `[?]` -> `[~]` with review notes

## Constraints
- Max 5 tasks `[~]` in Current Sprint at once
- Each task max 4 hours scope
- Large task -> split and add sub-tasks to Epic
- Always update Last Updated date on changes

## Session End
- Add Session Log entry: Date, Agent, Action, Result
- Check all `[~]` tasks (any forgotten?)
- Update Last Updated date
