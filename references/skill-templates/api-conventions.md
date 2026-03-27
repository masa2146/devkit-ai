---
name: api-conventions
description: Use when designing or implementing API endpoints. Defines REST/GraphQL conventions for {framework}.
---

# api-conventions - API Design Patterns

## Style: REST (or GraphQL if applicable)
## Framework: {framework}

### URL Patterns
- Collection: GET /api/v1/{resources}
- Single: GET /api/v1/{resources}/{id}
- Create: POST /api/v1/{resources}
- Update: PUT /api/v1/{resources}/{id}
- Partial: PATCH /api/v1/{resources}/{id}
- Delete: DELETE /api/v1/{resources}/{id}

### Response Format
```json
{
  "data": {},
  "meta": {"page": 1, "total": 100},
  "errors": []
}
```

### Status Codes
- 200: Success
- 201: Created
- 204: No Content (delete)
- 400: Bad Request (validation)
- 401: Unauthorized
- 403: Forbidden
- 404: Not Found
- 422: Unprocessable Entity
- 500: Internal Server Error

### Pagination
- Query: ?page=1&limit=20
- Response meta: page, limit, total, total_pages

### Versioning
- URL prefix: /api/v1/

## Rules
- DO: Validate all request input
- DO: Return consistent error format
- DO: Document endpoints (OpenAPI/Swagger)
- DO: Use proper HTTP methods and status codes
- DO NOT: Return sensitive data (passwords, tokens)
- DO NOT: Allow unlimited list responses (always paginate)
- DO NOT: Use verbs in URLs (use nouns)
