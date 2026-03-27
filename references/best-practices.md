# Best Practices Reference

Skill, hook, agent ve TASK.md olusturma icin best practice'ler.
Kaynak: awesome-agent-skills, superpowers, awesome-copilot, VoltAgent, disler hooks-mastery, alirezarezvani claude-skills

---

## Skill Best Practices

### Yapi
- Her skill tek sorumluluk tasir (Single Responsibility)
- SKILL.md entry point, opsiyonel scripts/ ve references/ klasorleri
- Frontmatter: sadece `name` + `description` (baska alan yok)

### Description
- "Use when {trigger condition}" ile basla
- Max 1024 karakter
- Ucuncu sahis simdiki zaman
- NE YAPTIGINI degil, NE ZAMAN KULLANILACAGINI acikla

### Icerik
- **When to Use**: Spesifik trigger condition'lar
- **Process**: Adim adim workflow (numaralandirilmis)
- **Rules**: DO / DO NOT kaliplari
- **Examples**: Gercek, proje-spesifik ornekler
- **References**: Ilgili dosya yollari

### Anti-Patterns
- Generic, her yerde gecerli kurallar yazma -> proje-spesifik yaz
- Cok uzun skill yazma -> bol, her biri tek sorumluluk
- Trigger condition'siz skill -> ne zaman kullanilacagi belirsiz
- Ornek olmayan skill -> soyut kalir, uygulanamaz

---

## Hook Best Practices

### Mimari
- **Fail-safe**: Exception'da her zaman exit 0 (crash etme)
- **Zero deps**: Sadece Python stdlib kullan
- **JSON stdin/stdout**: Standart I/O pattern
- **Exit codes**: 0=success, 2=block, diger=non-blocking error

### Security Layers (Multi-Layer Defense)
1. **PreToolUse**: Tehlikeli komutlari ENGELLE (rm -rf, .env access)
2. **PermissionRequest**: Guvenli islemleri OTOMATIK ONAYLA (read-only)
3. **PostToolUse**: Sonuclari DOGRULA (lint, type check)

### Engellenmesi Gereken Islemler
- `rm -rf /` veya `rm -rf ~` (root/home silme)
- `.env` dosyasina yazma/okuma (credential korunmasi)
- `git push --force` (force push)
- `DROP TABLE` / `DROP DATABASE` (database korunmasi)
- `npm publish` / `pip upload` (yanlislikla publish)

### Otomatik Izin Verilecek Islemler
- Read, Glob, Grep (read-only araclar)
- `ls`, `cat`, `head`, `tail`, `wc` (safe bash)
- `git status`, `git log`, `git diff` (git read)
- `echo`, `printf` (output)

### Anti-Patterns
- LLM-based karar verme -> deterministik regex/pattern matching kullan
- Hook crash'i -> fail-safe wrapper kullan
- Cok fazla loglama -> varsayilan kapali, flag ile ac
- Environment variable ile secrets -> `.env` dosyasi veya direct variable

---

## Agent Best Practices

### Naming
- Pattern: `{project-slug}-{role}`
- Kebab-case
- Descriptive: role ne yaptigini anlatmali

### Yapi (from VoltAgent)
1. **Role Definition**: Tek paragraf, ne yapar
2. **Expertise**: Tech-stack-specific uzmanlik alanlari
3. **Process**: Numaralandirilmis adimlar
4. **Constraints**: Yapilmamasi gerekenler
5. **Integration**: Diger agent'lar ve TASK.md ile etkilesim

### Domain Categories (from VoltAgent)
1. Core Development (frontend, backend, fullstack)
2. Language Specialists (python, typescript, go, rust)
3. Infrastructure (docker, k8s, ci/cd)
4. Quality & Security (testing, security audit)
5. Data & AI (database, ML)

### TASK.md Integration (ZORUNLU)
Her agent MUTLAKA:
- Islem oncesi TASK.md oku
- Islem sonrasi TASK.md guncelle
- Yeni task kesfedilirse Backlog'a ekle
- Karar alinirsa Decisions Log'a yaz

### Anti-Patterns
- Generic agent (her seyi yapan) -> tek sorumluluk
- TASK.md integration'siz agent -> proje takibi kopuk
- Tech-stack-agnostic expertise -> proje-spesifik yaz
- Process'siz agent -> deterministik calisamaz

---

## TASK.md Best Practices

### Yapi
- **Epics**: Her feature bir Epic
- **Backlog**: Priority-based (High/Medium/Low)
- **Current Sprint**: Max 5 aktif task
- **Completed**: Tarihli
- **Decisions Log**: Karar + rationale + impact
- **Session Log**: Hangi AI araci ne yapti

### Task Kurallari
- Max 4 saat scope per task
- Buyuk task -> bol
- Bagimsiz task'lar tercih et
- Siralama: data model -> backend -> API -> frontend -> test

### Status Flow
```
[ ] TODO -> [~] IN PROGRESS -> [x] DONE
                             -> [!] BLOCKED
                             -> [?] REVIEW -> [x] DONE
```

### Anti-Patterns
- Basit checklist ([ ] / [x] only) -> full backlog yapisi kullan
- Status guncellememek -> MUTLAK KURAL: her islem sonrasi guncelle
- 50+ task tek Sprint'te -> max 5 aktif
- Decisions Log bos -> her teknik karar yazilmali
- Session Log bos -> her session'da entry eklenmeli

---

## Cross-Platform Consistency

### Ayni Icerik, Farkli Format
- Skill icerigi her platform icin AYNI olmali
- Sadece format farki: Claude flat file, Copilot dizin-tabanli, Gemini flat file
- .cursorrules icin icerik OZETLENIR (skill dosyasi yok)

### TASK.md Everywhere
- TASK.md proje kokunde, platform-agnostic
- task-tracking skill TUM platformlara yazilir
- session_start hook TUM platformlarda TASK.md okur
- user_prompt_submit hook TUM platformlarda TASK.md hatirlatir
