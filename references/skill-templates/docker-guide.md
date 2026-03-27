---
name: docker-guide
description: Use when working with Docker, docker-compose, or container configurations.
---

# docker-guide - Docker Best Practices

## Dockerfile Patterns
- Use multi-stage builds
- Use specific base image tags (not :latest)
- Order layers by change frequency (least -> most)
- Use .dockerignore
- Run as non-root user
- Minimize layer count

### Example Structure
```dockerfile
# Build stage
FROM {base_image} AS builder
WORKDIR /app
COPY {dependency_file} .
RUN {install_command}
COPY . .
RUN {build_command}

# Runtime stage
FROM {runtime_image}
WORKDIR /app
COPY --from=builder /app/{output} .
USER nonroot
EXPOSE {port}
CMD [{run_command}]
```

## Docker Compose
- Use named volumes for persistent data
- Use environment files (.env)
- Health checks for all services
- Explicit network definitions
- Pin service versions

## Rules
- DO: Use multi-stage builds
- DO: Pin base image versions
- DO: Add health checks
- DO: Use .dockerignore
- DO NOT: Run as root
- DO NOT: Store secrets in images
- DO NOT: Use :latest tag
- DO NOT: Copy unnecessary files into image
