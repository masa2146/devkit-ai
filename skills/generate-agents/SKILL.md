---
name: generate-agents
description: Use when generating agent definition files for a target project across all platforms. Called by generate-config.
---

# generate-agents - Agent Dosyalari Olusturma

Hedef proje icin agent tanim dosyalarini olusturur.
Olusturmadan once `${CLAUDE_PLUGIN_ROOT}/references/agent-templates/` altindaki dosyalari ve `${CLAUDE_PLUGIN_ROOT}/references/best-practices.md`'yi oku.

## Pre-Check: userConfig

Before generating agents, check userConfig values: ${user_config.enable_planner}, ${user_config.enable_implementer}, ${user_config.enable_reviewer}, ${user_config.enable_debugger}. Skip disabled agents.

## Agent Naming Convention

Pattern: `{project-slug}-{role}`
Ornek: `ecommerce-planner`, `task-api-reviewer`, `my-app-debugger`

## Agent Listesi

### Core Agents (Her Zaman Olusturulur)

| Agent | Template | Amac |
|-------|----------|------|
| `planner` | `${CLAUDE_PLUGIN_ROOT}/references/agent-templates/planner.md` | Feature decomposition, TASK.md updates |
| `implementer` | `${CLAUDE_PLUGIN_ROOT}/references/agent-templates/implementer.md` | Kod yazma, test yazma |
| `reviewer` | `${CLAUDE_PLUGIN_ROOT}/references/agent-templates/reviewer.md` | Code review, quality gates |
| `debugger` | `${CLAUDE_PLUGIN_ROOT}/references/agent-templates/debugger.md` | Sistematik debugging |

### Conditional Agents (Feature-Based)

| Agent | Kosul | Amac |
|-------|-------|------|
| `api-designer` | "api" in features | API endpoint tasarimi, OpenAPI spec |
| `database-architect` | database var | Schema tasarimi, migration planlama |
| `devops-engineer` | deployment != "bare-metal" | CI/CD, infrastructure, Docker |
| `security-auditor` | "auth" in features | Guvenlik denetimi |

## Agent Definition Format

### Claude Code: `{TARGET_DIR}/.claude/agents/{role}.md`

```markdown
---
name: {project-slug}-{role}
description: {Role description} for {project name}. Specialist in {tech stack}.
model: sonnet
---

# {Role Title}

## Role Definition
{Bu agent'in gorevi - tek paragraf}

## Expertise
- {tech-stack-specific uzmanlik 1}
- {tech-stack-specific uzmanlik 2}
- {tech-stack-specific uzmanlik 3}

## Process
1. {adim 1 - her zaman TASK.md oku}
2. {adim 2}
3. {adim 3}
4. {son adim - her zaman TASK.md guncelle}

## Constraints
- {yapilmamasi gereken 1}
- {yapilmamasi gereken 2}
- task-tracking skill'ini takip et
- TASK.md'yi her islem sonrasi guncelle

## TASK.md Integration
- Islem oncesi: TASK.md oku, ilgili task'i [~] yap
- Islem sonrasi: Task'i [x] veya [!] yap
- Yeni task kesfedilirse: Backlog'a ekle
- Karar alinirsa: Decisions Log'a yaz
```

### GitHub Copilot: `{TARGET_DIR}/{role}.agent.md`

```markdown
---
name: {role}
description: {Role description}
---

{agent instructions - CLAUDE.md formatina benzer ama daha kisa}
{TASK.md integration kurallari dahil}
```

## Agent Icerik Detaylari

### planner Agent

- Feature'lari Epic'lere donusturur
- Her Epic'i max 4-saat task'lara boler
- TASK.md'ye yazar: Epic, Backlog, priority
- Dependency'leri belirler
- Proje mimarisini goz onunde bulundurur
- Expertise: proje tipi + framework capabilities

### implementer Agent

- TASK.md'den task alir
- code-standards skill'ini takip eder
- testing-strategy skill'ini takip eder
- Kodu yazar + test yazar
- TASK.md'yi gunceller
- Expertise: language + framework + database

### reviewer Agent

- Kodu code-standards'a gore inceler
- Test coverage kontrol eder
- Security checklist'i uygular (varsa)
- TASK.md Notes'a review sonucu yazar
- Expertise: language best practices + security

### debugger Agent

- 4-faz yaklasim: Observe -> Hypothesize -> Test -> Fix
- Proje-spesifik debug araclari kullanir
- TASK.md Notes'a debugging session ozeti yazar
- Expertise: framework error patterns + debugging tools

## Kurallar

- Her agent TASK.md integration'a sahip olmali
- Expertise proje tech stack'ine spesifik olmali
- Process adimlari net ve siralii olmali
- Constraints ile sinirlar belirle
- Generic agent yazma - her sey proje-spesifik
