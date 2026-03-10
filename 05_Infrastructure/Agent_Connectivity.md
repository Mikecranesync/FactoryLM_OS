---
title: "Agent Connectivity Matrix"
date: "2026-02-28"
tags: [type/runbook, infra/network, agent/tony, agent/ultron, agent/jarvis, agent/hetzner, agent/claude-code]
status: active
---

# Agent Connectivity Matrix

> Which agents can access what systems, and what's missing.

---

## Current Access

| Agent | Vault Read | Vault Write | Telegram | Discord | GitHub | PLC |
|-------|-----------|-------------|----------|---------|--------|-----|
| [[04_Agents/Tony_Macaroni/Tony_Macaroni\|Tony]] | obsidian_search/read/list | 01_Daily, 02_Weekly, 06_Incidents (REST API) | DM (Mike only) | @FactoryLM | No | Via Jarvis |
| [[04_Agents/Claude_Code/Claude_Code\|Claude Code]] | MCP + filesystem | Full vault 01-09 (filesystem + MCP) | No | No | `gh` CLI | No |
| [[04_Agents/Ultron/Ultron\|Ultron]] | REST API via Tailscale Serve | No (request via Tony) | @UltronVPS_bot | #ultron | Unknown | No |
| [[04_Agents/Jarvis_Local/Jarvis_Local\|Jarvis]] | REST API via Tailscale Serve | No (request via Tony) | @TravelLaptop_bot | #jarvis | No | Modbus TCP |
| [[04_Agents/Hetzner/Hetzner\|Hetzner]] | REST API via Tailscale Serve | No (request via Tony) | @UltronVPS_bot | #hetzner | Unknown | No |
| [[04_Agents/FactoryLM_Bot/FactoryLM_Bot\|factorylm-bot]] | No | 10_Commit_Notes (Git push) | No | No | Full | No |

---

## Gaps & Remediation

### Gap 1: Remote agents can't read the vault — RESOLVED (2026-03-10)
**Resolution:** Obsidian REST API exposed via Tailscale Serve. Remote agents access vault at `https://michaels-mac-mini.<tailnet>.ts.net/`. Git clones on remote nodes provide offline fallback.

### Gap 2: No agent can write to the vault — RESOLVED (2026-03-10)
**Resolution:** Tiered write policy implemented. Claude Code has full write access (01-09) via filesystem + MCP. Tony has scoped write access (01, 02, 06) via REST API tools (`obsidian_write`, `obsidian_append`, `obsidian_create_daily`). Remote agents request writes via Tony delegation. See [[CLAUDE_TONY]] for full policy.

### Gap 3: Tony's memory layers 2-5 not deployed
**Impact:** Tony has no persistent memory beyond SOUL.md. Every session starts cold.
**Remediation:**
1. Deploy PostgreSQL + pgvector on Hetzner (100.67.25.53)
2. Install text-embedding-3-small via OpenAI
3. Implement episodic + semantic memory tables per MEMORY-STRATEGY.md
4. **Prereq:** SSH key from Mac Mini to Hetzner

### Gap 4: No SSH keys to remote hosts
**Hosts affected:** DO VPS (100.68.120.99), Hetzner (100.67.25.53)
**Impact:** Cannot deploy software, update configs, or manage services remotely from Mac Mini.
**Remediation:** Generate and distribute SSH keys via Tailscale admin console or manual setup.

### Gap 5: Enrichment pipeline disconnected
**Status:** Fixed (2026-02-28) — launchd plist `com.factorylm.commit-enricher` created, runs hourly.
**Remaining:** Load the plist with `launchctl load ~/Library/LaunchAgents/com.factorylm.commit-enricher.plist`

### Gap 6: MCP port documentation
**Issue:** `.claude/.mcp.json` uses port 27124 (HTTPS). Obsidian REST API also listens on 27123 (HTTP). Both work.
**Remediation:** Document both ports. Use 27124 (HTTPS) as canonical for agent access.

---

## Priority Order

| Priority | Gap | Effort | Impact |
|----------|-----|--------|--------|
| 1 | Lift vault write restriction | Low | Enables vault population |
| 2 | SSH keys to remote hosts | Low | Enables remote management |
| 3 | Load enricher launchd plist | Trivial | Automated enrichment |
| 4 | Deploy pgvector on Hetzner | Medium | Tony persistent memory |
| 5 | Vault API for remote agents | Medium | Multi-agent knowledge access |

---

## Links
- [[05_Infrastructure/Current_State|Current State]]
- [[05_Infrastructure/Networks/Tailscale|Tailscale Network]]
- [[04_Agents/Tony_Macaroni/Tony_Macaroni|Tony Macaroni]] — MEMORY-STRATEGY.md describes layers 2-5
