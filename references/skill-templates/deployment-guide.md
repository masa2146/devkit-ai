---
name: deployment-guide
description: Use when deploying, configuring CI/CD, or managing environments for {project_name}.
---

# deployment-guide - Deployment Procedures

## Strategy: {deployment}
## CI/CD: {ci_cd}

### Environments
- Development: local
- Staging: {staging_details}
- Production: {production_details}

### Environment Variables
- Never commit secrets to git
- Use .env.example for documentation
- Use CI/CD secrets for production values

### Build Steps
1. Install dependencies: {install_command}
2. Run linter: {lint_command}
3. Run tests: {test_command}
4. Build: {build_command}
5. Deploy: {deploy_command}

### Rollback
{rollback procedure}

## Rules
- DO: Test in staging before production
- DO: Use environment variables for all config
- DO: Keep .env.example updated
- DO NOT: Deploy without passing tests
- DO NOT: Commit secrets
- DO NOT: Skip staging
