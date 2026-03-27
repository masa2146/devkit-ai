---
name: testing-strategy
description: Use when writing tests or reviewing test coverage. Defines testing approach for {testing_framework}.
---

# testing-strategy - Testing Approach

## Framework: {testing_framework}

### Test File Structure
- Location: {test_directory}
- Naming: {test_file_pattern}
- Run command: {test_command}
- Coverage command: {coverage_command}

### Test Types
1. **Unit Tests**: Individual functions/methods
2. **Integration Tests**: Component interactions
3. **E2E Tests**: Full user flows (if applicable)

### Test Naming
- Pattern: `test_{what}_{condition}_{expected_result}`
- Example: `test_login_with_invalid_email_returns_400`

### Coverage Requirements
- Minimum: 80% line coverage
- Critical paths: 100% coverage (auth, payments, data mutation)

### Mocking Strategy
{framework-specific mocking approach}

## Rules
- DO: Write tests BEFORE or WITH implementation
- DO: Test edge cases and error paths
- DO: Use descriptive test names
- DO: Keep tests independent (no shared state)
- DO NOT: Test implementation details (test behavior)
- DO NOT: Skip tests to save time
- DO NOT: Write tests that depend on external services without mocking
