# Platform Formats Reference

Her platformun beklenen dosya formatlari, dizin yapilari ve frontmatter kurallari.

---

## Claude Code

### Instruction File
- **Yol:** `CLAUDE.md` (proje kokunde)
- **Format:** Markdown, basliklari sections olarak kullanir
- **Ozellik:** Claude Code her session'da otomatik okur

### Skills
- **Yol:** `.claude/skills/{skill-name}.md`
- **Format:**
  ```markdown
  ---
  name: skill-name
  description: Use when {trigger condition}. Max 1024 karakter.
  ---

  # Skill Content
  {instructions}
  ```
- **Frontmatter kurallari:**
  - `name`: Kucuk harf, tire ile ayrilmis (kebab-case)
  - `description`: "Use when..." ile basla, max 1024 karakter
  - Baska frontmatter alani YOK (sadece name + description)

### Hooks
- **Yol:** `.claude/hooks/{hook_name}.py`
- **Config:** `.claude/settings.local.json`
- **Hook event'leri:** SessionStart, PreToolUse, PostToolUse, UserPromptSubmit, PermissionRequest, PreCompact, SessionEnd, Stop, SubagentStart, SubagentStop, Notification, PostToolUseFailure, Setup
- **Config formati:**
  ```json
  {
    "hooks": {
      "EventName": [
        {
          "matcher": "ToolPattern",
          "hooks": [
            {
              "type": "command",
              "command": "python $CLAUDE_PROJECT_DIR/.claude/hooks/script.py"
            }
          ]
        }
      ]
    }
  }
  ```

### Agents
- **Yol:** `.claude/agents/{role}.md`
- **Format:**
  ```markdown
  ---
  name: agent-name
  description: Agent description
  model: sonnet
  ---

  # Agent Role
  {agent instructions}
  ```

---

## GitHub Copilot

### Workspace Instructions
- **Yol:** `.github/copilot-instructions.md`
- **Format:** Plain markdown
- **Ozellik:** Copilot her conversation'da otomatik okur

### Task-Specific Instructions (Skills yerine)
- **Yol:** `.github/instructions/{name}.instructions.md`
- **Format:**
  ```markdown
  ---
  applyTo: "glob/pattern"
  ---

  # Instruction Title
  {instructions}
  ```
- **Ozellik:** `applyTo` glob pattern'i ile belirtilen dosyalara otomatik uygulanir
- **Ornek glob'lar:** `"**"` (tum dosyalar), `"**/*.py"` (Python), `"**/*.ts,**/*.tsx"` (TypeScript)
- **Opsiyonel:** `excludeAgent: "code-review"` ile belirli agent'lardan haric tutulabilir

> **Not:** Copilot `.github/skills/` formatini destekLEMEZ. Skill icerikleri
> `.github/instructions/{name}.instructions.md` olarak yazilmali.

### Hooks
> **Not:** GitHub Copilot su anda hook sistemi destekLEMEZ.
> Hook mantigi Copilot icin uretilemez.

### Agents
- **Yol:** `{role}.agent.md` (proje kokunde) veya `AGENTS.md`
- **Format:**
  ```markdown
  ---
  name: role-name
  description: Agent description
  ---

  {agent instructions}
  ```
- **Ozellik:** En yakin AGENTS.md dizin agacinda oncelik alir

---

## Gemini / Antigravity

### Instruction File
- **Yol:** `GEMINI.md` (proje kokunde)
- **Format:** Markdown
- **Ozellik:** Gemini CLI session basinda okur

### Skills
- **Yol:** `.agent/skills/{skill-name}.md`
- **Format:** Markdown, frontmatter ile
- **Ozellik:** Flat file (dizin yok)

### Agents
- Agent dosya formati henuz standartlasmadi
- GEMINI.md icerisinde agent rolleri tanimlanabilir

---

## Cursor

### Rules File
- **Yol:** `.cursorrules` (proje kokunde)
- **Format:** Plain text
- **Ozellik:** Cursor her session'da otomatik okur
- **Icerik:** Kisa, ozetli kurallar. Skill/hook/agent destegi yok.

---

## Ortak Kurallar

1. **Frontmatter:** YAML, `---` ile sarili
2. **name:** Kebab-case (kucuk harf, tire)
3. **description:** Net, spesifik trigger condition
4. **Icerik:** Markdown, baslikli sections
5. **Dosya adi:** Kebab-case, `.md` uzantili
