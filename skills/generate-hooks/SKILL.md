---
name: generate-hooks
description: Use when generating hook scripts and hook configuration for a target project. Called by generate-config.
---

# generate-hooks - Hook Dosyalari Olusturma

Hedef proje icin hook script'leri ve konfigurasyonu olusturur.
Olusturmadan once `${CLAUDE_PLUGIN_ROOT}/references/hook-templates/` altindaki dosyalari ve `${CLAUDE_PLUGIN_ROOT}/references/best-practices.md`'yi oku.

## Hook Mimarisi

### Exit Code Semantics
- **Exit 0**: Basarili (stdout transcript'e gosterilir)
- **Exit 2**: Engelleme (stderr Claude'a gonderilir, islem bloklanir)
- **Diger**: Non-blocking hata (kullaniciya gosterilir, islem devam eder)

### Python UV Single-File Pattern

Tum hook'lar bu pattern'i kullanir:
```python
#!/usr/bin/env python3
import json, sys
from pathlib import Path
from datetime import datetime

def main():
    try:
        hook_input = json.loads(sys.stdin.read())
        # Hook logic here
        sys.exit(0)
    except Exception:
        sys.exit(0)  # Fail-safe: never crash

if __name__ == "__main__":
    main()
```

## Olusturulacak Hook'lar

### 1. `session_start.py` - Context Loader

Template: `${CLAUDE_PLUGIN_ROOT}/references/hook-templates/session_start.py`

Islevler:
- TASK.md'yi okur, Current Sprint'teki aktif task'lari gosterir
- Git branch ve uncommitted changes sayisini gosterir
- Proje context'ini ozetler

Tech-stack adaptasyonu:
- Python: `pyproject.toml` dan proje bilgisi
- Node: `package.json` dan proje bilgisi
- Go: `go.mod` dan proje bilgisi

### 2. `pre_tool_use.py` - Security Gatekeeper

Template: `${CLAUDE_PLUGIN_ROOT}/references/hook-templates/pre_tool_use.py`

Engellenen islemler (exit 2):
- `rm -rf /` veya `rm -rf ~` (root/home silme)
- `.env` dosyasina Write/Edit (credential korunmasi)
- `git push --force` (force push engelleme)
- `DROP TABLE` / `DROP DATABASE` (DB korunmasi)

Proje-spesifik adaptasyon:
- Python: `pip install` uyarisi (requirements.txt guncelleme hatirlatmasi)
- Node: `npm publish` engelleme (yanlislikla publish korunmasi)
- Tum projeler: `.env`, `.env.local`, `.env.production` dosyalari korunur

### 3. `post_tool_use.py` - Validator

Template: `${CLAUDE_PLUGIN_ROOT}/references/hook-templates/post_tool_use.py`

Islevler:
- Bash/Write/Edit sonrasi dosya degisikligini loglar
- Tech-stack-specific validator calistirir

Tech-stack validatorlari:
- Python: `ruff check {file}` (lint)
- TypeScript: `npx eslint {file}` (lint)
- Go: `go vet {file}` (vet)

### 4. `user_prompt_submit.py` - TASK.md Reminder

Template: `${CLAUDE_PLUGIN_ROOT}/references/hook-templates/user_prompt_submit.py`

Islevler:
- Her prompt'ta TASK.md'deki Current Sprint'i hatirlatir
- Aktif [~] task varsa gosterir
- Context injection: "Aktif task: {task_name}"

### 5. `permission_request.py` - Auto-Allower

Template: `${CLAUDE_PLUGIN_ROOT}/references/hook-templates/permission_request.py`

Otomatik izin verilen islemler:
- Read, Glob, Grep (read-only)
- `ls`, `cat`, `head`, `tail`, `wc` (safe bash)
- `git status`, `git log`, `git diff` (git read)
- `echo`, `printf` (output)

Engellenen islemler:
- Redirection (`>`, `>>`) to sensitive files
- `rm` with force flags
- `.env` dosya islemleri

## Hook Konfigurasyonu

### Claude Code: `{TARGET_DIR}/.claude/settings.local.json`

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "python $CLAUDE_PROJECT_DIR/.claude/hooks/session_start.py --load-context"
          }
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "Bash|Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "python $CLAUDE_PROJECT_DIR/.claude/hooks/pre_tool_use.py"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Bash|Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "python $CLAUDE_PROJECT_DIR/.claude/hooks/post_tool_use.py"
          }
        ]
      }
    ],
    "UserPromptSubmit": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "python $CLAUDE_PROJECT_DIR/.claude/hooks/user_prompt_submit.py"
          }
        ]
      }
    ]
  }
}
```

### GitHub Copilot

> **Not:** GitHub Copilot su anda hook sistemi desteklemiyor.
> Copilot icin hook uretimi yapilMAZ. Sadece Claude Code icin hook'lar olusturulur.
> Copilot'a yonelik guvenlik ve konvansiyon kurallari `.github/instructions/` dosyalarina yazilir.

## Kurallar

- Her hook fail-safe olmali: exception durumunda exit 0 (crash etme)
- Sadece stdlib kullan (zero external dependencies)
- JSON stdin/stdout pattern'i kullan
- `$CLAUDE_PROJECT_DIR` prefix'i kullan (path resolution)
- Hassas dosyalari (.env) her zaman koru
- Loglama opsiyonel - varsayilan olarak kapali
