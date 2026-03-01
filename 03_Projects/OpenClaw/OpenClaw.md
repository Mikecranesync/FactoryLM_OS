---
title: "OpenClaw Gateway"
date: "2026-02-28"
tags: [type/project, project/openclaw, infra/gateway]
status: active
owner: Mike
---

# OpenClaw Gateway — Project Spec

## Objective
> Agent runtime gateway that replaced clawdbot. Hosts all agent instances, manages model routing, cron scheduling, and inter-agent communication.

## Status

| Field | Value |
|-------|-------|
| Status | active |
| Owner | Mike Harper |
| Started | 2026-02-27 |
| Target | Ongoing |

## Background
> OpenClaw v2026.2.26 replaced clawdbot v2026.1.24-3 as the central agent runtime. It runs on the same port (18789), manages 75 agents across 19 workflow pipelines, and provides the dashboard, cron scheduling, and model routing layer. Installed via in-place migration with the old plist kept as `.bak`.

## Scope

### In Scope
- Agent instance hosting (75 agents, 19 workflows)
- Model routing: DeepSeek V3.2 primary, Groq + OpenRouter fallbacks
- Cron scheduling for workflow pipelines
- Agent-to-agent communication
- Dashboard at http://127.0.0.1:18789/
- Telegram + Discord channel integration
- Medic health checks (every 5 min)

### Out of Scope
- Direct PLC communication (agents delegate to Jarvis)
- Vault writes (read-only policy)

## Technical Approach
- **Port:** 18789 (same as former clawdbot)
- **launchd:** `ai.openclaw.gateway` (`~/Library/LaunchAgents/ai.openclaw.gateway.plist`)
- **Config:** `~/.openclaw/openclaw.json` (2816 lines)
- **Logs:** `~/.openclaw/logs/gateway.log` + `/tmp/openclaw/openclaw-*.log`
- **Model config:**
  - Primary: `deepseek/deepseek-chat` (DeepSeek V3.2, $0.28/$0.42 per MTok)
  - Fallbacks: `groq/llama-3.3-70b-versatile`, `openrouter/qwen/qwen3-coder:free`, `openrouter/openrouter/free`
  - Image: `google/gemini-2.5-flash`
- **Node path:** Hardcoded to Cellar version (25.6.1) in plist — may break on brew upgrade

## Dependencies
- Node.js 25.6.1 (Homebrew)
- [[03_Projects/Antfarm/Antfarm|Antfarm]] — workflow engine integration
- Doppler for secrets management

## Risks
- Node path hardcoded in plist — `brew upgrade` will break it
- OpenRouter `:free` model suffixes return 404 — always use paid IDs
- Do NOT use DeepSeek R1 — reasoning model, doesn't reliably call tools

## Links
- **Config:** `~/.openclaw/openclaw.json`
- **Dashboard:** http://127.0.0.1:18789/
- **Rollback:** `launchctl load ~/Library/LaunchAgents/com.clawdbot.gateway.plist.bak`
- **Workspace:** `~/.openclaw/workspace/`
