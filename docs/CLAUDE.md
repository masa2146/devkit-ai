# CLAUDE.md - devkit-ai (Development)

> Bu dosya devkit-ai plugin'inin gelistiricileri icindir. Plugin kullanimci icin README.md'ye bakin.

## Plugin Yapisi

devkit-ai bir Claude Code plugin'idir. Yapisal degisikliklerde su dosyalari guncelle:

- `.claude-plugin/plugin.json` - Plugin manifest
- `skills/*/SKILL.md` - Skill dosyalari
- `agents/*.md` - Agent tanimlari
- `hooks/hooks.json` - Hook konfigurasyonu
- `scripts/*.py` - Hook script'leri
- `references/` - Template ve referans dosyalar
- `settings.json` - Default permissions

## Skill Akisi

```
generate-config (orchestrator)
  -> analyze-project
  -> generate-platform-docs
  -> generate-skills
  -> generate-hooks
  -> generate-agents
  -> generate-task-md
```

## Test Etme

```bash
claude --plugin-dir ./devkit-ai
/devkit-ai:generate-config /tmp/test-project
```

## Kurallar

1. Skill icerisindeki path'ler `${CLAUDE_PLUGIN_ROOT}/` ile baslmali
2. Hedef proje output path'leri `{TARGET_DIR}/` ile baslamali
3. references/ altindaki template'ler placeholder kullanir: `{project_name}`, `{language}`, etc.
4. userConfig degerleri `${user_config.KEY}` ile erisilir
