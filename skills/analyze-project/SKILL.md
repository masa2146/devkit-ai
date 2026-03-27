---
name: analyze-project
description: Use when analyzing a target project directory to detect tech stack, features, and architecture. Called by generate-config.
---

# analyze-project - Proje Analizi

Hedef dizini analiz ederek proje profilini olusturur. Iki senaryo destekler.

## Senaryo A: Bos Dizin (Sifirdan Proje)

Hedef dizin bos veya mevcut degilse, kullanicidan asagidaki bilgileri topla:

### Sorulacak Bilgiler (AskUserQuestion ile)

1. **Proje adi**: Ornek: "my-ecommerce", "task-api"
2. **Proje aciklamasi**: Kisa bir aciklama
3. **Proje tipi**: web-app | api | cli | library | mobile | fullstack
4. **Tech stack** (coklu secim):
   - Frontend: React, Vue, Angular, Next.js, Svelte, Astro
   - Backend: FastAPI, Django, Express, NestJS, Spring Boot, Go/Gin, Rails
   - Database: PostgreSQL, MySQL, MongoDB, Redis, SQLite, DynamoDB
   - Diger: GraphQL, gRPC, WebSocket, Message Queue
5. **Ozellikler** (coklu secim): auth, api, websocket, real-time, file-upload, search, payments, notifications, admin-panel, i18n
6. **Mimari**: monolith | microservices | serverless | modular-monolith
7. **Deployment**: docker | kubernetes | serverless | vercel | netlify | bare-metal
8. **CI/CD**: github-actions | gitlab-ci | jenkins | none

### Cikarim Kurallari

Tech stack'ten otomatik cikarim yap:
- React/Vue/Angular/Next.js/Svelte -> language: typescript, testing: jest/vitest
- FastAPI/Django -> language: python, testing: pytest
- Express/NestJS -> language: typescript, testing: jest
- Spring Boot -> language: java, testing: junit
- Go/Gin -> language: go, testing: go-test
- Rails -> language: ruby, testing: rspec

## Senaryo B: Mevcut Proje (Kod Var)

Hedef dizinde dosya varsa, asagidaki sirayla analiz et:

### 1. Paket Yoneticisi Dosyalari

| Dosya | Tespit |
|-------|--------|
| `package.json` | Node.js projesi. dependencies'den framework tespit et |
| `pyproject.toml` / `setup.py` / `requirements.txt` | Python projesi |
| `go.mod` | Go projesi |
| `Cargo.toml` | Rust projesi |
| `pom.xml` / `build.gradle` | Java/Kotlin projesi |
| `Gemfile` | Ruby projesi |
| `pubspec.yaml` | Flutter/Dart projesi |

### 2. Framework Tespiti

**package.json dependencies'den:**
- `react` / `react-dom` -> React
- `next` -> Next.js
- `vue` -> Vue
- `@angular/core` -> Angular
- `svelte` -> Svelte
- `express` -> Express
- `@nestjs/core` -> NestJS
- `fastify` -> Fastify

**Python dependencies'den:**
- `fastapi` -> FastAPI
- `django` -> Django
- `flask` -> Flask
- `sqlalchemy` -> SQL database
- `motor` / `pymongo` -> MongoDB

### 3. Database Tespiti

- `docker-compose.yml` iceriginde: postgres, mysql, mongo, redis
- `.env` / `.env.example` iceriginde: DATABASE_URL, MONGO_URI, REDIS_URL
- ORM dosyalari: prisma/schema.prisma, alembic/, migrations/

### 4. Test Framework Tespiti

- `jest.config.*` / `vitest.config.*` -> Jest/Vitest
- `pytest.ini` / `pyproject.toml [tool.pytest]` / `conftest.py` -> pytest
- `_test.go` dosyalari -> Go test
- `spec/` dizini -> RSpec

### 5. Deployment Tespiti

- `Dockerfile` / `docker-compose.yml` -> Docker
- `k8s/` / `kubernetes/` -> Kubernetes
- `serverless.yml` -> Serverless Framework
- `vercel.json` -> Vercel
- `netlify.toml` -> Netlify
- `.github/workflows/` -> GitHub Actions CI/CD

### 6. Feature Tespiti

- Auth: `passport`, `next-auth`, `django.contrib.auth`, JWT related packages
- API: route/controller files, OpenAPI spec
- WebSocket: `socket.io`, `ws`, `channels`
- Search: `elasticsearch`, `meilisearch`, `algolia`

## Cikti

Analiz sonucunu kullaniciya goster ve onayla:

```
Proje Profili:
  Ad: {name}
  Tip: {type}
  Dil: {language}
  Framework'ler: {frameworks}
  Database: {databases}
  Test: {testing}
  Ozellikler: {features}
  Mimari: {architecture}
  Deployment: {deployment}
  CI/CD: {ci_cd}

Bu profil dogru mu? Degisiklik yapmak ister misiniz?
```

Kullanici onayladiktan sonra bu profil diger skill'ler tarafindan kullanilir.
