---
title: Vault Commands & Workflows
date: 2026-02-25
tags: [meta/commands]
status: active
---

# Vault Commands & Workflows

Quick reference for daily operations in the FactoryLM_OS vault.

---

## Create a New Daily Entry

1. Open the command palette: `Cmd + P`
2. Type **"Templates: Insert template"**
3. Select `Daily_Journal`
4. Move the file to `01_Daily/` and rename it `YYYY-MM-DD.md`

**Faster method (with Templater plugin):**
1. `Cmd + P` → "Templater: Create new note from template"
2. Select `Daily_Journal`
3. It auto-names and places the file if Templater is configured

**File:** `01_Daily/YYYY-MM-DD.md`
**Tags:** `type/daily`

---

## Create a Weekly Review

1. `Cmd + P` → Insert template → `Weekly_Review`
2. Move to `02_Weekly/` and rename to `YYYY-Www.md` (e.g., `2026-W09.md`)
3. Fill in goals from the past week's daily entries
4. Set next week's top 3 priorities

**File:** `02_Weekly/YYYY-Www.md`
**Tags:** `type/weekly`

---

## Start a New Project

1. Create a new folder under `03_Projects/<ProjectName>/`
2. `Cmd + P` → Insert template → `Project_Spec`
3. Save as `03_Projects/<ProjectName>/Spec.md`
4. Fill in objective, scope, milestones
5. Add the project tag to [[00_Global/Tags]] if it doesn't exist yet

**File:** `03_Projects/<ProjectName>/Spec.md`
**Tags:** `type/project`, `project/<name>`

---

## File an Incident

1. `Cmd + P` → Insert template → `Incident_Writeup`
2. Save as `06_Incidents/YYYY-MM-DD_<short-slug>.md`
3. Fill in severity, timeline, root cause
4. **Every incident must have action items.** No exceptions.
5. Link to affected systems in `05_Infrastructure/`

**File:** `06_Incidents/YYYY-MM-DD_<short-slug>.md`
**Tags:** `type/incident`, `severity/<level>`, relevant `infra/*` tags

---

## Add a Research Note

1. `Cmd + P` → Insert template → `Research_Note`
2. Save as `07_Research/YYYY-MM-DD_<topic-slug>.md`
3. Fill in source, summary, key takeaways
4. Add "How This Applies to FactoryLM" section

**File:** `07_Research/YYYY-MM-DD_<topic-slug>.md`
**Tags:** `type/research`

---

## Search & Navigation

### Quick Open
`Cmd + O` — open any file by name. Start typing and it fuzzy-matches.

### Search Vault
`Cmd + Shift + F` — full-text search across all files.

### Follow a Link
`Cmd + Click` on any `[[wikilink]]` to jump to that note.

### Back / Forward
`Cmd + Alt + Left/Right` — navigate back and forward through your history.

### Graph View
`Cmd + G` — visual map of all notes and their connections.

### Tag Search
Click any tag in a note, or search `tag:type/incident` in the search bar.

---

## Useful Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Cmd + P` | Command palette |
| `Cmd + O` | Quick open file |
| `Cmd + Shift + F` | Search vault |
| `Cmd + N` | New note |
| `Cmd + E` | Toggle edit/preview |
| `Cmd + Click` | Follow wikilink |
| `Cmd + Alt + Left` | Navigate back |
| `Cmd + Alt + Right` | Navigate forward |
| `Cmd + G` | Graph view |
| `Cmd + ,` | Settings |

---

## Obsidian Tips

### Recommended Plugins
- **Templater** — advanced template insertion with auto-naming and auto-placement
- **Dataview** — powers the [[00_Global/Dashboard]] queries
- **Calendar** — sidebar calendar for quick daily note access
- **Periodic Notes** — auto-create daily/weekly notes on schedule

### Frontmatter
Every note needs YAML frontmatter at the top. Templates handle this automatically. If creating a note manually, always add:
```yaml
---
title: Note Title
date: YYYY-MM-DD
tags: [tag1, tag2]
status: active
---
```

### Linking
- Use `[[wikilinks]]` for internal links (not markdown links)
- Use `[[folder/filename|display text]]` to control what text shows
- Link liberally — orphan notes are useless notes

### Archiving
When a project is done or a note is no longer relevant:
1. Move it to `09_Archive/`
2. Update its `status` frontmatter to `archived`
3. Don't delete — archive. You might need it later.
