---
title: "Current System State"
date: "2026-02-28"
tags: [type/runbook, infra/server, infra/network, infra/gateway, status/active]
status: active
---

# Current System State

> Last updated: 2026-02-28

This document captures the live state of the FactoryLM infrastructure. Agents should update this after significant changes.

---

## Tailscale Network

| Device | IP | Status | Notes |
|--------|-----|--------|-------|
| Mac Mini (primary) | 100.108.19.94 | Online | Hosts Tony, OpenClaw, Discord Layer, Claude Code |
| DO VPS (Ultron) | 100.68.120.99 | Online | No SSH key from Mac Mini |
| Hetzner | 100.67.25.53 | Online | No SSH key from Mac Mini |
| PLC Laptop | 100.72.2.99 | Online | Jarvis Node :8765 working, user `hharp` |
| Travel Laptop | 100.83.251.23 | Online | Jarvis Local instance |
| Pi Edge | 100.66.216.6 | Degraded | Pings OK, SSH broken (balenaOS) |
| srv1078052 | 100.102.30.102 | Online | Review for decommission |

---

## Services (Mac Mini)

### launchd Services

| Service | Plist | Port | Status |
|---------|-------|------|--------|
| OpenClaw Gateway | `ai.openclaw.gateway` | 18789 | Running |
| Antfarm Dashboard | `com.factorylm.antfarm-dashboard` | 3333 | Running |
| Discord Relay | `com.factorylm.discord-relay` | 8765 | Running |
| Discord Layer Bot | `com.factorylm.discord-layer-bot` | — | Running |
| Discord Adapter | `com.factorylm.discord-adapter` | — | Running |
| LLM Router | `com.factorylm.llm-router` | — | Running |
| PLC Monitor | `com.factorylm.plc-monitor` | — | Running |
| Config Backup | `com.factorylm.config-backup` | — | Scheduled |
| Nightly Extraction | `com.factorylm.nightly-extraction` | — | Scheduled |

### Key Ports

| Port | Service |
|------|---------|
| 18789 | OpenClaw Gateway + Dashboard |
| 3333 | Antfarm Dashboard |
| 8765 | Discord Relay Daemon |
| 27123 | Obsidian REST API (HTTP) |
| 27124 | Obsidian REST API (HTTPS) |

---

## Model Configuration

| Role | Model | Cost |
|------|-------|------|
| Primary | `deepseek/deepseek-chat` (DeepSeek V3.2) | $0.28/$0.42 per MTok |
| Fallback 1 | `groq/llama-3.3-70b-versatile` | Free tier |
| Fallback 2 | `openrouter/qwen/qwen3-coder:free` | Free |
| Fallback 3 | `openrouter/openrouter/free` | Free |
| Image | `google/gemini-2.5-flash` | — |
| Enrichment | `moonshotai/kimi-k2-instruct` (via Groq) | Free tier |

> **Warning:** Do NOT use DeepSeek R1 — reasoning model, doesn't reliably call tools.
> **Warning:** OpenRouter `:free` model suffixes may 404. Always verify availability.

---

## Agent Crons (OpenClaw)

- 5 agent crons for `factorylm-feature-dev` workflow (delivery: none)
- 1 medic cron (checks every 5 min)
- Use `openclaw cron list --json` to see current schedule
- **Known bug:** `antfarm workflow ensure-crons` creates duplicates — always run manual dedup

---

## PLC Hardware

| Device | Address | Protocol | Status |
|--------|---------|----------|--------|
| Allen-Bradley Micro820 (2080-LC30-48QWB) | 192.168.1.100:502 | Modbus TCP | Working |

- **Coils:** 0-17 (digital control outputs)
- **Registers:** 100-105 (analog sensor readings)
- **Access:** Via PLC Laptop (100.72.2.99) → Jarvis Local

---

## What's NOT Running

| System | Why |
|--------|-----|
| Commit enricher | No launchd plist — must be triggered manually |
| Tony memory layers 2-5 | Need PostgreSQL + pgvector on Hetzner |
| Pi Edge SSH | balenaOS SSH broken |
| Celery workers | Master of Puppets stack not active |

---

## Recent Changes (Last 72h)

| Date | Change | PR |
|------|--------|----|
| 2026-02-28 | Cosmos demo desktop apps (PLC Reader + GitHub Scraper) | #108 |
| 2026-02-28 | PLC Reader desktop app + CI builds | #107 |
| 2026-02-28 | Health check endpoint for discord relay | #106 (open) |
| 2026-02-27 | UTF-8 fix for gist poller | #105 |
| 2026-02-27 | Gist watch MCP + /gist skill | #104 |
| 2026-02-27 | Tony intelligence stack sync (Kimi K2, dropped 8B) | #103 |
| 2026-02-27 | Phone controller for Mac Mini dispatch | #102 |
| 2026-02-27 | Antfarm workflow compat fix | #101 |
| 2026-02-26 | Discord Layer full deploy (PRs #92-#100) | #92-#100 |

---

## Key File Paths

| What | Path |
|------|------|
| OpenClaw config | `~/.openclaw/openclaw.json` |
| OpenClaw logs | `~/.openclaw/logs/gateway.log` |
| Antfarm install | `~/.openclaw/workspace/antfarm/` |
| Tony config | `~/factorylm/clawd/tony/` |
| Monorepo | `~/factorylm/factorylm/` |
| Vault | `~/FactoryLM_OS/` |
| Claude memory | `~/.claude/projects/-Users-factorylm/memory/` |
| Architecture map | `~/factorylm/ARCH-DISCOVERY.md` |
| Discord config | `~/.factorylm/config.toml` |
