---
name: generate-skills
description: Use when generating skill files for a target project across all platforms. Called by generate-config.
---

# generate-skills - Skill Dosyalari Olusturma

Hedef proje icin skill dosyalarini olusturur. Her skill multi-platform yazilir.
Olusturmadan once `${CLAUDE_PLUGIN_ROOT}/references/best-practices.md` ve ilgili `${CLAUDE_PLUGIN_ROOT}/references/skill-templates/` dosyalarini oku.

## Skill Listesi

### Core Skills (Her Zaman Olusturulur)

| Skill | Template | Amac |
|-------|----------|------|
| `task-tracking` | `${CLAUDE_PLUGIN_ROOT}/references/skill-templates/task-tracking.md` | TASK.md yonetimi |
| `code-standards` | `${CLAUDE_PLUGIN_ROOT}/references/skill-templates/code-standards.md` | Kodlama kurallari |
| `testing-strategy` | `${CLAUDE_PLUGIN_ROOT}/references/skill-templates/testing-strategy.md` | Test yaklasimu |
| `git-workflow` | `${CLAUDE_PLUGIN_ROOT}/references/skill-templates/git-workflow.md` | Git kurallari |
| `architecture-guide` | `${CLAUDE_PLUGIN_ROOT}/references/skill-templates/architecture-guide.md` | Mimari rehber |
| `deployment-guide` | `${CLAUDE_PLUGIN_ROOT}/references/skill-templates/deployment-guide.md` | Deployment sureci |

### Conditional Skills (Feature-Based)

| Skill | Kosul | Template |
|-------|-------|----------|
| `api-conventions` | "api" in features VEYA proje tipi "api"/"web-app"/"fullstack" | `${CLAUDE_PLUGIN_ROOT}/references/skill-templates/api-conventions.md` |
| `security-checklist` | "auth" in features | `${CLAUDE_PLUGIN_ROOT}/references/skill-templates/security-checklist.md` |
| `database-guide` | database var | `${CLAUDE_PLUGIN_ROOT}/references/skill-templates/database-guide.md` |
| `docker-guide` | deployment "docker" veya "kubernetes" | `${CLAUDE_PLUGIN_ROOT}/references/skill-templates/docker-guide.md` |
| `websocket-guide` | "websocket" in features | Sifirdan olustur |
| `performance-guide` | "performance" in features | Sifirdan olustur |

## Her Skill Icin Yapilacaklar

1. Ilgili template'i `${CLAUDE_PLUGIN_ROOT}/references/skill-templates/` altindan oku
2. Proje-spesifik bilgilerle adapte et:
   - `{{ language }}` -> gercek dil (python, typescript, go, etc.)
   - `{{ framework }}` -> gercek framework (fastapi, react, etc.)
   - `{{ test_command }}` -> gercek test komutu (pytest, npm test, etc.)
   - `{{ lint_command }}` -> gercek lint komutu (ruff, eslint, etc.)
3. Multi-platform ciktiya yaz

## Multi-Platform Output Yollari

### Claude Code
```
{TARGET_DIR}/.claude/skills/{skill-name}.md
```

Format:
```markdown
---
name: {skill-name}
description: Use when {trigger condition}
---

{skill content}
```

### GitHub Copilot
```
{TARGET_DIR}/.github/instructions/{skill-name}.instructions.md
```

Format:
```markdown
---
applyTo: "**"
---

# {Skill Name}

{skill content}
```

> **Not:** Copilot `.github/instructions/*.instructions.md` formatini destekler.
> `applyTo` glob pattern'i ile hangi dosyalara uygulanacagi belirlenir.
> Skill-spesifik glob ornekleri: `"**/*.py"`, `"**/*.ts"`, `"**/test/**"`

### Gemini / Antigravity
```
{TARGET_DIR}/.agent/skills/{skill-name}.md
```

Format: Ayni icerik, frontmatter ile.

### Cursor
Cursor icin ayri skill dosyasi yok. Skill icerikleri `.cursorrules` dosyasina ozetlenir (generate-platform-docs tarafindan).

## Skill Icerik Yapisi

Her skill su sections'a sahip olmali:

```markdown
---
name: {skill-name}
description: Use when {trigger condition}
---

# {Skill Name}

## When to Use
- {trigger condition 1}
- {trigger condition 2}

## Process
1. {adim 1}
2. {adim 2}
3. {adim 3}

## Rules
- DO: {yapilmasi gereken}
- DO: {yapilmasi gereken}
- DO NOT: {yapilmamasi gereken}
- DO NOT: {yapilmamasi gereken}

## Examples
{proje-spesifik ornek kod/komut}

## References
- {ilgili dosya yollari}
```

## Kurallar

- Her skill tek sorumluluk tasir
- Trigger condition net ve spesifik olmali
- Rules bolumunde DO / DO NOT kaliplari kullan
- Examples bolumunde GERCEK proje-spesifik ornekler ver
- task-tracking skill'i ozellikle detayli yaz - bu en kritik skill
