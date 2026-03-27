---
name: security-checklist
description: Use when implementing auth, handling user data, or reviewing security. OWASP-based checklist.
---

# security-checklist - Security Best Practices

## Authentication
- Use bcrypt/argon2 for password hashing (never MD5/SHA)
- JWT: short expiry (15min access, 7d refresh)
- Session: httpOnly, secure, sameSite cookies
- Rate limit login attempts (5 per minute)

## Authorization
- Check permissions on EVERY endpoint
- Use role-based access control (RBAC)
- Never trust client-side authorization

## Input Validation
- Validate ALL user input (server-side)
- Sanitize for XSS
- Parameterized queries (prevent SQL injection)
- File upload: check type, size, scan for malware

## Data Protection
- Never log sensitive data (passwords, tokens, PII)
- Encrypt sensitive data at rest
- Use HTTPS everywhere
- .env files: never commit, always .gitignore

## OWASP Top 10 Checklist
- [ ] Injection prevention (SQL, NoSQL, OS, LDAP)
- [ ] Broken authentication checks
- [ ] Sensitive data exposure prevention
- [ ] XML external entities (XXE) protection
- [ ] Broken access control checks
- [ ] Security misconfiguration review
- [ ] XSS prevention
- [ ] Insecure deserialization check
- [ ] Known vulnerability scanning
- [ ] Logging and monitoring

## Rules
- DO: Review auth code with extra scrutiny
- DO: Use security linting tools
- DO: Keep dependencies updated
- DO NOT: Store plaintext passwords
- DO NOT: Expose stack traces in production
- DO NOT: Trust client input
