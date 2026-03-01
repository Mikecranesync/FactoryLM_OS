---
title: "Discord Layer"
date: "2026-02-28"
tags: [type/project, project/discord-layer, project/discord-adapter, infra/network]
status: active
owner: Mike
---

# Discord Layer — Project Spec

## Objective
> Multi-agent Discord presence with slash commands, relay daemon, and Telegram bridge — built on top of the original Discord adapter.

## Status

| Field | Value |
|-------|-------|
| Status | active |
| Owner | Mike Harper |
| Started | 2026-02-26 |
| Target | Ongoing |

## Background
> The Discord Layer replaced the simple Discord adapter with a full relay system. It provides slash commands (/relay, /status, /config show, /fleet), a webhook-based relay daemon, and a Telegram-Discord message bridge. Guild ID 1474672178808229970 (Doppler-managed). Bot is FactoryLM#9772.

## Scope

### In Scope
- Relay daemon (POST /relay routes to agent webhooks) at http://127.0.0.1:8765
- Bot slash commands: /relay, /status, /config show, /fleet
- Telegram-Discord bridge
- Webhook rate limiter with token bucket
- Config via `~/.factorylm/config.toml` (4 agents with webhooks)

### Out of Scope
- Voice channels
- Reaction-based workflows

## Milestones

| Milestone | Target Date | Status |
|-----------|-------------|--------|
| Scaffold + config | 2026-02-26 | done (PRs #92, #93) |
| Relay daemon + rate limiter | 2026-02-26 | done (PRs #95, #96) |
| Bridge + slash commands | 2026-02-26 | done (PRs #97, #98) |
| Docs + impl fix | 2026-02-26 | done (PRs #99, #100) |
| Health check endpoint | 2026-02-28 | open (PR #106) |

## Technical Approach
- **3 launchd services:** `com.factorylm.discord-relay` (relay daemon), `com.factorylm.discord-layer-bot` (bot), `com.factorylm.discord-adapter` (legacy, untouched)
- **Channels:** FACTORY FLOOR (#plc-live, #alerts) / AGENTS (#tony, #ultron, #jarvis, #hetzner, #dispatch-log)
- **Rollback:** `pre-discord-layer-deploy` git tag

## Dependencies
- [[03_Projects/OpenClaw/OpenClaw|OpenClaw Gateway]] — agent webhooks
- [[04_Agents/Tony_Macaroni/Tony_Macaroni|Tony Macaroni]] — primary agent in #tony channel

## Risks
- Three separate launchd services to keep running
- Config.toml is manually maintained

## Links
- **Config:** `~/.factorylm/config.toml`
- **Guild:** 1474672178808229970
- **PRs:** #92-#100, #106
