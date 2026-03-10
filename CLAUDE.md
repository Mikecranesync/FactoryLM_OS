# CLAUDE.md — Vault Operating Instructions for Claude Code

## Context

You are operating inside the **FactoryLM_OS** Obsidian vault — the operating brain for FactoryLM, an industrial IoT platform. This vault is the shared memory layer for the entire agent fleet.

---

## Vault Structure

| Folder | Purpose |
|--------|---------|
| `00_Global/` | Dashboard, tags, commands, user profile — vault-wide references |
| `01_Daily/` | Daily journal entries (one per day) |
| `02_Weekly/` | Weekly review summaries |
| `03_Projects/` | Project specs, roadmaps, and dev notes (subdirs per project) |
| `04_Agents/` | Agent profiles and behavior docs |
| `05_Infrastructure/` | Hardware, servers, PLCs, gateway, network topology |
| `06_Incidents/` | Incident writeups and post-mortems |
| `07_Research/` | Research notes, spikes, explorations |
| `08_Runbooks/` | Deployment procedures and recovery playbooks |
| `09_Archive/` | Completed or deprecated items moved here |
| `10_Commit_Notes/` | Auto-generated commit digests (factorylm-bot only) |
| `_Templates/` | Obsidian templates for all entry types |

---

## Write Policy

Claude Code has **full write access** to folders 01-09. Use it.

| Agent | Write Scope | Mechanism |
|-------|-------------|-----------|
| Claude Code (Macaroni) | Full vault 01-09 | Filesystem + MCP |
| Tony Macaroni | 01_Daily, 02_Weekly, 06_Incidents | REST API (ClawdBot plugin) |
| factorylm-bot | 10_Commit_Notes only | Git push |
| Ultron, Jarvis, Hetzner | No direct write | Request via Tony delegation |

---

## MCP Access

You have the **Obsidian MCP server** configured in `~/.claude/.mcp.json`. Use it to read/write/search the vault programmatically. The REST API runs at `https://127.0.0.1:27124`.

You can also read/write vault files directly via filesystem tools since the vault is at `~/FactoryLM_OS/`.

---

## Filing Rules

1. **Always use the correct folder.** Don't dump files in the vault root.
2. **Always include YAML frontmatter.** Every file gets metadata at the top:
   ```yaml
   ---
   title: Note Title
   date: YYYY-MM-DD
   tags: [tag1, tag2]
   status: active | draft | archived
   ---
   ```
3. **Use tags from the taxonomy.** See `00_Global/Tags` — don't invent new tags without adding them there first.
4. **Use `[[wikilinks]]` for internal references.** Link liberally between related notes.
5. **Date format is `YYYY-MM-DD` everywhere.** No exceptions.
6. **File names use underscores**, not spaces. Keep them descriptive but short.

### Tag Categories
- `project/factorylm`, `project/tony-macaroni`
- `agent/hammurabi`, `agent/herodotus`, `agent/tony`, `agent/claude-code`
- `infra/plc`, `infra/gateway`, `infra/server`
- `type/incident`, `type/research`, `type/runbook`, `type/daily`, `type/weekly`
- `status/active`, `status/blocked`, `status/done`

Full taxonomy: `00_Global/Tags`

---

## Key Paths

| What | Path |
|------|------|
| This vault | `~/FactoryLM_OS/` |
| Code monorepo | `~/factorylm/` |
| Agent memory (code sessions) | `~/.claude/projects/-Users-factorylm/memory/MEMORY.md` |
| Tony config | `~/factorylm/clawd/tony/` |
| OpenClaw workspace | `~/factorylm/openclaw-workspace/` |

---

## Detailed Conventions

See [[CLAUDE_TONY]] for full conventions on entry creation, templates, wikilinks, and interaction style.
