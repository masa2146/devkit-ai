---
name: generate-task-md
description: Use when generating TASK.md (project management backlog/sprint board) and task-tracking skill for a target project. Called by generate-config. This is the most critical skill.
---

# generate-task-md - TASK.md ve Task Tracking Olusturma

Bu skill KRITIK. TASK.md projenin Single Source of Truth'u. Tum AI araclari bu dosya uzerinden calisir.
Olusturmadan once `${CLAUDE_PLUGIN_ROOT}/references/task-md-template.md` dosyasini oku.

## Olusturulacak Dosyalar

1. `{TARGET_DIR}/TASK.md` - Ana proje yonetim dosyasi
2. `{TARGET_DIR}/.claude/skills/task-tracking.md` - Claude Code skill
3. `{TARGET_DIR}/.github/instructions/task-tracking.instructions.md` - Copilot instruction
4. `{TARGET_DIR}/.agent/skills/task-tracking.md` - Gemini skill

## TASK.md Yapisi

`${CLAUDE_PLUGIN_ROOT}/references/task-md-template.md`'yi referans alarak olustur:

```markdown
# TASK.md - {Project Name}

> Bu dosya projenin tek kaynak noktasidir (Single Source of Truth).
> Tum AI araclari (Claude Code, Gemini, Copilot) bu dosya uzerinden calisir.
> Her islem oncesi bu dosyayi oku, her islem sonrasi guncelle.

## Project Info
- **Name:** {project-name}
- **Type:** {project-type}
- **Stack:** {tech-stack-listesi}
- **Architecture:** {architecture}
- **Started:** {today's date}
- **Last Updated:** {today's date}

## Status Legend
- `[ ]` TODO - Henuz baslanmadi
- `[~]` IN PROGRESS - Uzerinde calisiyor
- `[x]` DONE - Tamamlandi
- `[!]` BLOCKED - Engellendi (sebebi Notes'a yazilir)
- `[?]` REVIEW - Code review bekliyor

---

## Epics

### Epic 1: Project Setup
- [x] Initialize project structure
- [x] Generate AI assistant configurations
- [ ] Setup CI/CD pipeline
- [ ] Configure development environment
- [ ] Setup linting and formatting
- [ ] Configure test framework
- [ ] Create initial documentation

### Epic 2: {Feature 1 Name}
{feature'in alt task'lari - max 4 saat scope}

### Epic 3: {Feature 2 Name}
{feature'in alt task'lari}

{... her feature icin bir Epic ...}

---

## Current Sprint

> Aktif calisilanlar. Max 5 task ayni anda [~] olabilir.

| Task | Epic | Assignee | Status | Started | Notes |
|------|------|----------|--------|---------|-------|
| - | - | - | - | - | Henuz sprint baslamadi |

---

## Backlog

> Siradaki isler, oncelik sirasina gore.

### High Priority
{en onemli task'lar - core features, blockers}

### Medium Priority
{orta oncelikli - supporting features}

### Low Priority
{dusuk oncelikli - nice-to-have, optimization}

---

## Completed

> Tamamlanan isler, tarih ile.

- [x] Project initialized - {today's date}
- [x] AI configurations generated - {today's date}

---

## Decisions Log

> Alinan mimari/teknik kararlar ve sebepleri.

| Date | Decision | Rationale | Impact |
|------|----------|-----------|--------|
| {today} | Tech stack: {stack} | {reason} | All epics |
| {today} | Architecture: {arch} | {reason} | All epics |

---

## Notes

> Genel notlar, blocker detaylari, debugging session ozetleri.

### Active Blockers
Henuz blocker yok.

### Session Log
| Date | Agent | Action | Result |
|------|-------|--------|--------|
| {today} | devkit-ai | Generated AI configurations | All config files created |
```

## Epic Olusturma Kurallari

1. Her feature bir Epic olur
2. Her Epic 5-15 task icerir
3. Her task max 4 saat scope'ta
4. Task'lar bagimsiz calisilabilir olmali (mumkunse)
5. Task siralama: data model -> backend -> frontend -> test -> integration
6. "Project Setup" Epic'i her zaman ilk sirada

## Feature -> Task Breakdown Ornekleri

### "auth" feature icin:
```
### Epic: User Authentication
- [ ] Design auth data model (User, Session, Token)
- [ ] Implement user registration endpoint
- [ ] Implement login endpoint
- [ ] Implement logout endpoint
- [ ] Add JWT/session token management
- [ ] Implement password reset flow
- [ ] Add email verification
- [ ] Write auth middleware
- [ ] Write auth unit tests
- [ ] Write auth integration tests
- [ ] Security review: OWASP auth checklist
```

### "api" feature icin:
```
### Epic: API Layer
- [ ] Design API route structure
- [ ] Implement base CRUD endpoints
- [ ] Add request validation
- [ ] Add response serialization
- [ ] Implement error handling
- [ ] Add pagination
- [ ] Add filtering and sorting
- [ ] Write API tests
- [ ] Generate API documentation (OpenAPI)
```

## task-tracking Skill Icerigi

Asagidaki icerigi hedef projenin TUM platformlarina yaz:

```markdown
---
name: task-tracking
description: Use ALWAYS before starting any work and after completing any task. Manages TASK.md as the project's Single Source of Truth.
---

# task-tracking - TASK.md Yonetimi

## MUTLAK KURALLAR

1. **HER ISLEM ONCESI** TASK.md'yi oku
2. **HER ISLEM SONRASI** TASK.md'yi guncelle
3. Bu kurallar TARTISILAMAZ - her zaman uygulanir

## Task Lifecycle

### Task Baslama
1. TASK.md oku
2. Calisacagin task'i bul
3. Status'u `[~]` yap
4. Current Sprint tablosuna ekle (tarih ile)
5. Calismaya basla

### Task Bitirme
1. Task'i `[x]` yap
2. Completed section'a tasi (tarih ile)
3. Current Sprint'ten cikar
4. Session Log'a entry ekle

### Task Engellenme
1. Task'i `[!]` yap
2. Notes > Active Blockers'a detay yaz
3. Cozum plani belirt
4. Baska task'a gec

### Yeni Task Kesfi
1. Ilgili Epic'e veya Backlog'a ekle
2. Priority belirle (High/Medium/Low)
3. 4-saat scope'tan buyukse bol

### Karar Alma
1. Decisions Log'a yaz
2. Date, Decision, Rationale, Impact doldur

### Code Review
1. Task'i `[?]` yap
2. Review sonucunu Notes'a yaz
3. Onaylanirsa `[x]` yap

## Sinirlama Kurallari
- Current Sprint'te max 5 task [~] olabilir
- Bir task max 4 saat scope'ta olmali
- Buyuk task -> bol ve Epic'e alt-task ekle
- Last Updated tarihini her degisiklikte guncelle

## Session Sonu
- Session Log'a entry ekle: Date, Agent, Action, Result
- Tum [~] task'lari kontrol et (unutulan var mi?)
```

## Kurallar

- TASK.md HICBIR ZAMAN basit checklist olmamali
- Her section (Epics, Sprint, Backlog, Completed, Decisions, Notes) DOLU olmali
- task-tracking skill TUM platformlara yazilmali (Claude, Copilot, Gemini)
- Epic'ler proje feature'larindan turetilmeli
- Backlog priority'leri mantikli olmali (core features = high)
- Session Log ilk entry'si "AI configurations generated" olmali
