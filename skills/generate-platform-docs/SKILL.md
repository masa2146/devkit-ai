---
name: generate-platform-docs
description: Use when generating platform-specific instruction files (CLAUDE.md, GEMINI.md, copilot-instructions, .cursorrules) for a target project. Called by generate-config.
---

# generate-platform-docs - Platform MD Dosyalari Olusturma

Hedef proje icin tum platform instruction dosyalarini olusturur.
Olusturmadan once `${CLAUDE_PLUGIN_ROOT}/references/platform-formats.md` dosyasini oku.

## Olusturulacak Dosyalar

1. `{TARGET_DIR}/CLAUDE.md`
2. `{TARGET_DIR}/GEMINI.md`
3. `{TARGET_DIR}/.github/copilot-instructions.md`
4. `{TARGET_DIR}/.github/instructions/*.instructions.md` (task-specific)
5. `{TARGET_DIR}/.cursorrules`

## CLAUDE.md Yapisi

```markdown
# {Project Name}

## Project Overview
- Name: {name}
- Type: {type}
- Description: {description}
- Architecture: {architecture}

## Tech Stack
{her teknoloji ve versiyonu}

## Project Structure
{proje tipi ve framework'e gore dizin yapisi}
{Ornek: src/components/, src/hooks/, app/api/, app/models/}

## Coding Conventions
### {Language}
{dil-spesifik kurallar: naming, formatting, imports, type hints vs}

### Naming Conventions
{dosya, fonksiyon, degisken, class naming kurallari}

### Error Handling
{framework-spesifik hata yonetimi}

## Testing
{test framework, test dosya yapisi, coverage kurallari}
{Ornek komutlar: pytest, npm test, go test}

## Database
{database tipi, ORM, migration kurallari}

## Git Conventions
- Branch naming: feature/, bugfix/, hotfix/
- Commit format: conventional commits (feat:, fix:, docs:, etc.)
- PR rules

## Deployment
{deployment stratejisi, ortam degiskenleri, build steps}

## Security
{auth yontemi, env dosyalari, secrets yonetimi}

## Key Commands
{proje-spesifik komutlar: build, test, lint, format, migrate, deploy}

## Skills Reference
{projeye yazilan skill'lerin listesi ve ne zaman kullanilacagi}

## TASK.md
- Bu projenin task yonetimi TASK.md uzerinden yapilir
- Her islem oncesi TASK.md'yi oku
- Her islem sonrasi TASK.md'yi guncelle
- Detaylar icin task-tracking skill'ine bak
```

## GEMINI.md Yapisi

CLAUDE.md ile ayni icerik, ancak:
- Gemini CLI instruction formatinda
- `.agent/skills/` referanslari
- Gemini-specific tool referanslari

## copilot-instructions.md Yapisi

Daha kisa ve code-generation odakli:

```markdown
# {Project Name} - Copilot Instructions

## Language & Framework
{language preferences, framework idioms}

## Code Style
{formatting, naming, import order}

## Patterns
{design patterns, error handling patterns}

## Testing
{test patterns, mocking approaches}

## Security
{input validation, auth patterns}
```

## Task-Specific Instructions (.github/instructions/)

Proje ozelliklerine gore olustur:

| Dosya | Kosul | Icerik |
|-------|-------|--------|
| `code-review.instructions.md` | Her zaman | Review checklist, quality gates |
| `testing.instructions.md` | Her zaman | Test yazma kurallari, patterns |
| `documentation.instructions.md` | Her zaman | Dokumantasyon standartlari |
| `api-design.instructions.md` | "api" in features | REST/GraphQL conventions |
| `database.instructions.md` | database var | Schema, migration, query patterns |
| `security.instructions.md` | "auth" in features | Auth, validation, OWASP |

## .cursorrules Yapisi

Plain text, kisa ve ozetli:

```
Project: {name}
Type: {type}
Stack: {stack}

Rules:
- {language-specific rule 1}
- {language-specific rule 2}
- {framework-specific pattern}
- {testing approach}
- {naming conventions}

Commands:
- Test: {test command}
- Lint: {lint command}
- Build: {build command}
```

## Kurallar

- Her dosyayi proje-spesifik bilgilerle doldur (generic birakma)
- Tech stack'e gore dogru conventions yaz
- Key commands gercek, calisabilir komutlar olsun
- TASK.md referansini her platform doc'a ekle
