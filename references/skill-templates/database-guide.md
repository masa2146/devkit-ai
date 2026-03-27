---
name: database-guide
description: Use when working with database schemas, migrations, or queries for {database}.
---

# database-guide - Database Conventions

## Database: {database}
## ORM: {orm}

### Schema Conventions
- Table names: plural, snake_case ({resources})
- Column names: snake_case
- Primary key: `id` (UUID or auto-increment)
- Timestamps: `created_at`, `updated_at` on all tables
- Soft delete: `deleted_at` (nullable timestamp)

### Migration Rules
- One migration per change
- Migration names: {timestamp}_{descriptive_name}
- Always write reversible migrations
- Test migrations on staging before production
- Never edit existing migrations (create new ones)

### Query Patterns
- Use ORM for standard CRUD
- Raw SQL only for complex queries (document why)
- Always use parameterized queries
- Index frequently queried columns
- Avoid N+1 queries (use eager loading)

### Performance
- Add indexes for: foreign keys, frequently filtered columns, unique constraints
- Use pagination for list queries
- Connection pooling for production
- Monitor slow queries

## Rules
- DO: Write migrations for ALL schema changes
- DO: Test migrations in both directions (up/down)
- DO: Use transactions for multi-table operations
- DO NOT: Edit data directly in production
- DO NOT: Store large blobs in the database
- DO NOT: Skip indexing foreign keys
