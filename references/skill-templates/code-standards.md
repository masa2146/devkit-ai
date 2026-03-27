---
name: code-standards
description: Use when writing or reviewing code. Defines coding conventions for {language} with {framework}.
---

# code-standards - Coding Conventions

## Language: {language}

### Naming Conventions
{language-specific naming rules}
- Files: {file_naming_pattern}
- Functions: {function_naming_pattern}
- Variables: {variable_naming_pattern}
- Classes: {class_naming_pattern}
- Constants: {constant_naming_pattern}

### Formatting
- Formatter: {format_command}
- Line length: {max_line_length}
- Indentation: {indent_style}
- Import ordering: {import_order_rules}

### Type Safety
{type annotation/checking rules for the language}

### Error Handling
{framework-specific error handling patterns}

### File Organization
{project structure conventions}

## Rules
- DO: Run {lint_command} before committing
- DO: Run {format_command} before committing
- DO: Use type annotations/hints
- DO: Keep functions under 50 lines
- DO NOT: Use `any` type (TypeScript) or skip type hints (Python)
- DO NOT: Leave commented-out code
- DO NOT: Use magic numbers without constants
- DO NOT: Catch generic exceptions without re-raising
