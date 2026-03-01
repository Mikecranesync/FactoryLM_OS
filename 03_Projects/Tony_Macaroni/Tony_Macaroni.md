---
title: "Tony Macaroni"
date: "2026-02-28"
tags: [type/project, project/tony-macaroni, agent/tony]
status: active
owner: Mike
---

# Tony Macaroni — Project Spec

## Objective
> Boss agent and single point of contact for Mike. Coordinates all sub-agents, handles delegation, and maintains the knowledge layer.

## Status

| Field | Value |
|-------|-------|
| Status | active |
| Owner | Mike Harper |
| Started | 2026-02 |
| Target | Ongoing |

## Background
> Tony is the coordinator agent running on Mac Mini via OpenClaw gateway. He's Mike's only direct Telegram contact — all other agents are reached through Tony's delegation protocol. Tony has read-only access to the Obsidian vault and delegates to Ultron (web research), Jarvis (PLC ops), and Hetzner (batch compute).

## Scope

### In Scope
- Telegram bot interface (@Tony_Macaroni_bot)
- Sub-agent delegation with 5-minute timeout
- Obsidian vault read access (search, read, list)
- Discord integration (@FactoryLM in #factory-ops-hub)
- Memory layers 1-5 (SOUL.md → Technician Profiles)

### Out of Scope
- Direct PLC write operations (delegated to Jarvis)
- Heavy compute (delegated to Hetzner)
- Web research (delegated to Ultron)

## Milestones

| Milestone | Target Date | Status |
|-----------|-------------|--------|
| Basic delegation working | 2026-02-25 | done |
| Intelligence stack updated (Kimi K2, dropped 8B) | 2026-02-27 | done (PR #103) |
| Memory layers 2-5 deployed | TBD | pending |
| Vault write access | TBD | pending |

## Technical Approach
- **Runtime:** OpenClaw gateway instance `oc_macaroni` on Mac Mini
- **Model:** DeepSeek V3.2 (primary), Groq llama-3.3-70b (fallback)
- **Delegation protocol:** 7-step process — parse intent → select sub-agent → forward → await (5min timeout) → relay response → log → update memory
- **Memory architecture:** 5 layers defined in `MEMORY-STRATEGY.md`, only Layer 1 (SOUL.md) deployed
- **Security:** No ClawHub skills without Clawdex scan, no PLC credential exposure, sub-agents read-only to Mike's Brain

## Dependencies
- [[03_Projects/OpenClaw/OpenClaw|OpenClaw Gateway]] — runtime
- [[04_Agents/Ultron/Ultron|Ultron]] — web research sub-agent
- [[04_Agents/Jarvis_Local/Jarvis_Local|Jarvis Local]] — PLC sub-agent
- [[04_Agents/Hetzner/Hetzner|Hetzner]] — batch compute sub-agent

## Risks
- Memory layers 2-5 need PostgreSQL + pgvector (not yet deployed)
- 5-minute sub-agent timeout may be too short for complex tasks
- Vault is read-only — Tony can't update project state

## Links
- **Config:** `~/factorylm/clawd/tony/` (SOUL.md, AGENTS.md, MEMORY-STRATEGY.md)
- **Telegram:** @Tony_Macaroni_bot
- **Instance:** `oc_macaroni` on Mac Mini (100.108.19.94)
- **PR #103:** Intelligence stack sync
