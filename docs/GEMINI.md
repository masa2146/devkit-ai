# GEMINI.md - devkit-ai (Development)

> Bu dosya devkit-ai plugin'inin gelistiricileri icindir.

## Plugin Yapisi

devkit-ai bir AI config generator plugin'idir. Hedef proje icin tum AI asistan yapilandirma dosyalarini olusturur.

## Desteklenen Platformlar

- Claude Code: CLAUDE.md, .claude/skills/, .claude/hooks/, .claude/agents/
- Gemini / Antigravity: GEMINI.md, .agent/skills/
- GitHub Copilot: .github/copilot-instructions.md, .github/instructions/, .github/skills/, .github/hooks/, *.agent.md
- Cursor: .cursorrules

## Skill Akisi

```
generate-config -> analyze-project -> generate-platform-docs
  -> generate-skills -> generate-hooks -> generate-agents -> generate-task-md
```

## Gemini-Specific

- Hedef projede .agent/skills/ altina skill dosyalari yaz
- GEMINI.md'yi hedef projeye yaz
- Skill format: frontmatter (name, description) + markdown icerik
