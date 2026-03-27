---
name: generate-config
description: Use when the user wants to generate AI assistant configuration files for a software project. This is the main orchestrator skill.
---

# generate-config - AI Config Generator Orchestrator

Bu skill, bir hedef proje icin tum AI asistan yapilandirma dosyalarini olusturur.
Deterministik calisir - asagidaki checklist'i adim adim takip et, HICBIR ADIMI ATLAMA.

## Plugin Config

Bu skill devkit-ai plugin'i icinden calisir. Kullanici tercihleri:
- `${user_config.enable_planner}`: Planner agent olusturulsun mu
- `${user_config.enable_implementer}`: Implementer agent olusturulsun mu
- `${user_config.enable_reviewer}`: Reviewer agent olusturulsun mu
- `${user_config.enable_debugger}`: Debugger agent olusturulsun mu

Disable edilen agent'lari atlayarak devam et.

## CHECKLIST (TodoWrite ile izle)

```
[ ] 1. Hedef dizin bilgisini al
[ ] 2. Proje bilgilerini topla / analiz et (analyze-project skill)
[ ] 3. Platform MD dosyalarini olustur (generate-platform-docs skill)
[ ] 4. Skill dosyalarini olustur (generate-skills skill)
[ ] 5. Hook dosyalarini olustur (generate-hooks skill)
[ ] 6. Agent dosyalarini olustur (generate-agents skill)
[ ] 7. TASK.md ve task-tracking olustur (generate-task-md skill)
[ ] 8. Sonuc ozeti goster
```

## Adim 1: Hedef Dizin

Kullanicidan hedef dizin yolunu al. Ornek:
- `/Users/me/projects/my-app/`
- Kullanici belirtmediyse sor: "Hedef proje dizini nedir?"

Hedef dizini `TARGET_DIR` olarak kaydet.

## Adim 2: Proje Analizi

`/devkit-ai:analyze-project` skill'ini calistir.

Bu skill iki senaryo icin calisir:
- **Bos dizin**: Kullanicidan soru-cevap ile bilgi toplar
- **Mevcut proje**: Dosya sistemi analizi ile otomatik tespit eder

Sonuc: Proje profili (name, type, stack, features, architecture, deployment)

## Adim 3: Platform MD Dosyalari

`/devkit-ai:generate-platform-docs` skill'ini calistir.

Olusturulacak dosyalar:
- `{TARGET_DIR}/CLAUDE.md`
- `{TARGET_DIR}/GEMINI.md`
- `{TARGET_DIR}/.github/copilot-instructions.md`
- `{TARGET_DIR}/.github/instructions/*.instructions.md`
- `{TARGET_DIR}/.cursorrules`

## Adim 4: Skill Dosyalari

`/devkit-ai:generate-skills` skill'ini calistir.

Core skills (her zaman) + conditional skills (feature-based).
Multi-platform output: .claude/skills/, .github/instructions/, .agent/skills/

## Adim 5: Hook Dosyalari

`/devkit-ai:generate-hooks` skill'ini calistir.

Python hook script'leri + hook config dosyalari.
Sadece Claude Code hooks (Copilot hook desteklemiyor).

## Adim 6: Agent Dosyalari

`/devkit-ai:generate-agents` skill'ini calistir.

userConfig'e gore agent'lari olustur veya atla.
Multi-platform output: .claude/agents/, *.agent.md

## Adim 7: TASK.md

`/devkit-ai:generate-task-md` skill'ini calistir.

Bu adim KRITIK:
- TASK.md = Full Backlog/Sprint Board (basit checklist DEGIL)
- task-tracking skill hedef projenin TUM platformlarina yazilir
- Her AI araci TASK.md uzerinden calisir

## Adim 8: Sonuc Ozeti

Olusturulan tum dosyalarin listesini goster:
```
Olusturulan dosyalar:
  Platform Docs: CLAUDE.md, GEMINI.md, copilot-instructions.md, .cursorrules
  Skills (N adet): task-tracking, code-standards, ...
  Hooks (N adet): session_start.py, pre_tool_use.py, ...
  Agents (N adet): planner, implementer, ...
  TASK.md: Epic sayisi, Backlog task sayisi

Hedef projeyi AI aracinizla acin ve gelistirmeye baslayin!
```

## Kurallar

- Her adimi TodoWrite ile izle
- Bir adim basarisiz olursa DUR ve kullaniciya sor
- Adim atlama - sirali ilerle
- Her skill invoke edilmeden once `${CLAUDE_PLUGIN_ROOT}/references/` altindaki ilgili dosyalari oku
- Kullanici sadece belirli platformlar istiyorsa, sadece onlari olustur
