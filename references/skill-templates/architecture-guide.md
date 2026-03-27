---
name: architecture-guide
description: Use when designing features, creating new modules, or making structural decisions. Defines {architecture} patterns for {project_name}.
---

# architecture-guide - Architecture Patterns

## Architecture: {architecture}

### Module Structure
{architecture-specific module organization}

### Dependency Rules
{which modules can depend on which}

### Communication Patterns
{how modules/services communicate}

### Data Flow
{typical data flow through the application}

## Design Principles
- Single Responsibility: one module = one purpose
- Dependency Inversion: depend on abstractions
- Interface Segregation: small, focused interfaces
- Keep it simple: no premature abstraction

## Rules
- DO: Follow existing module boundaries
- DO: Document new architectural decisions in TASK.md Decisions Log
- DO: Consider scalability implications
- DO NOT: Create circular dependencies
- DO NOT: Put business logic in controllers/handlers
- DO NOT: Bypass the established layer structure
