# TASK.md Template

Bu dosya generate-task-md skill'inin referans aldigi tam TASK.md sablonudur.
Placeholder'lar `{curly braces}` icinde gosterilmistir.

---

```markdown
# TASK.md - {project_name}

> Bu dosya projenin tek kaynak noktasidir (Single Source of Truth).
> Tum AI araclari (Claude Code, Gemini, Copilot) bu dosya uzerinden calisir.
> Her islem oncesi bu dosyayi oku, her islem sonrasi guncelle.

## Project Info
- **Name:** {project_name}
- **Type:** {project_type}
- **Stack:** {tech_stack_comma_separated}
- **Architecture:** {architecture}
- **Started:** {date}
- **Last Updated:** {date}

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

### Epic 2: {feature_1_name}
- [ ] Design {feature_1} data model
- [ ] Implement {feature_1} backend logic
- [ ] Implement {feature_1} API endpoints
- [ ] Implement {feature_1} frontend (if applicable)
- [ ] Write {feature_1} unit tests
- [ ] Write {feature_1} integration tests
- [ ] {feature_1} code review

### Epic 3: {feature_2_name}
- [ ] Design {feature_2} data model
- [ ] Implement {feature_2} backend logic
- [ ] Implement {feature_2} API endpoints
- [ ] Implement {feature_2} frontend (if applicable)
- [ ] Write {feature_2} unit tests
- [ ] Write {feature_2} integration tests
- [ ] {feature_2} code review

{repeat for each feature}

---

## Current Sprint

> Aktif calisilanlar. Max 5 task ayni anda [~] olabilir.

| Task | Epic | Assignee | Status | Started | Notes |
|------|------|----------|--------|---------|-------|
| - | - | - | - | - | Sprint henuz baslamadi |

---

## Backlog

> Siradaki isler, oncelik sirasina gore.

### High Priority
- [ ] {core feature task 1} (Epic N)
- [ ] {core feature task 2} (Epic N)
- [ ] {critical infrastructure task} (Epic 1)

### Medium Priority
- [ ] {supporting feature task 1} (Epic N)
- [ ] {supporting feature task 2} (Epic N)

### Low Priority
- [ ] {nice-to-have task 1} (Epic N)
- [ ] {optimization task} (Epic N)

---

## Completed

> Tamamlanan isler, tarih ile.

- [x] Project initialized - {date}
- [x] AI configurations generated - {date}

---

## Decisions Log

> Alinan mimari/teknik kararlar ve sebepleri.

| Date | Decision | Rationale | Impact |
|------|----------|-----------|--------|
| {date} | Tech stack: {stack} | {why this stack was chosen} | All epics |
| {date} | Architecture: {arch} | {why this architecture} | All epics |
| {date} | Database: {db} | {why this database} | Data-related epics |

---

## Notes

> Genel notlar, blocker detaylari, debugging session ozetleri.

### Active Blockers
Henuz blocker yok.

### Session Log
| Date | Agent | Action | Result |
|------|-------|--------|--------|
| {date} | devkit-ai | Generated AI configurations | All config files created |
```

---

## Epic Olusturma Kurallari

1. **Her feature bir Epic** - Feature adini Epic basliginda kullan
2. **5-15 task per Epic** - Cok az: yeterli detay yok. Cok fazla: micro-management.
3. **Max 4 saat per task** - Buyuk task -> bol
4. **Siralama**: data model -> backend -> API -> frontend -> test -> review
5. **Bagimsizlik**: Mumkunse task'lar birbirinden bagimsiz olsun

## Backlog Priority Kurallari

- **High**: Core features, auth, data model, infrastructure
- **Medium**: Supporting features, UI polish, secondary endpoints
- **Low**: Optimization, documentation, nice-to-have features

## Decisions Log Kullanimi

Her onemli teknik karar buraya yazilir:
- Framework secimi
- Database secimi
- Auth yontemi
- API versioning stratejisi
- Deployment stratejisi
- Test stratejisi
