---
title: "Mac Mini"
date: "2026-02-28"
tags: [type/runbook, infra/server]
status: active
---

# Mac Mini (Primary Hub)

## Identity

| Field | Value |
|-------|-------|
| Hostname | michaels-mac-mini |
| Tailscale IP | 100.108.19.94 |
| Role | Primary hub — hosts all core services |

## Services Running

| Service | Plist | Port |
|---------|-------|------|
| [[05_Infrastructure/Gateway/OpenClaw_Runtime\|OpenClaw Gateway]] | `ai.openclaw.gateway` | 18789 |
| [[03_Projects/Antfarm/Antfarm\|Antfarm Dashboard]] | `com.factorylm.antfarm-dashboard` | 3333 |
| Discord Relay | `com.factorylm.discord-relay` | 8765 |
| Discord Layer Bot | `com.factorylm.discord-layer-bot` | — |
| Discord Adapter | `com.factorylm.discord-adapter` | — |
| LLM Router | `com.factorylm.llm-router` | — |
| PLC Monitor | `com.factorylm.plc-monitor` | — |
| Config Backup | `com.factorylm.config-backup` | — |
| Nightly Extraction | `com.factorylm.nightly-extraction` | — |
| Obsidian REST API | (Obsidian plugin) | 27123/27124 |

## Agents Hosted
- [[04_Agents/Tony_Macaroni/Tony_Macaroni|Tony Macaroni]] (oc_macaroni)
- [[04_Agents/Claude_Code/Claude_Code|Claude Code]] (Macaroni)

## Key Paths
- Repos: `~/factorylm/`
- Vault: `~/FactoryLM_OS/`
- OpenClaw: `~/.openclaw/`
- Claude memory: `~/.claude/projects/-Users-factorylm/memory/`

## Links
- [[05_Infrastructure/Current_State|Current State]]
- [[05_Infrastructure/Networks/Tailscale|Tailscale Network]]
