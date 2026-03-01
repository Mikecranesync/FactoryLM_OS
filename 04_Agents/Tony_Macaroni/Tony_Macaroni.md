---
title: "Tony Macaroni — Agent Profile"
date: "2026-02-28"
tags: [type/project, agent/tony, meta/profile]
status: active
---

# Tony Macaroni

## Identity

| Field | Value |
|-------|-------|
| Handle | @Tony_Macaroni_bot |
| Instance | `oc_macaroni` |
| Host | Mac Mini (100.108.19.94) |
| Role | Boss agent, coordinator, Mike's single point of contact |
| Runtime | [[03_Projects/OpenClaw/OpenClaw\|OpenClaw Gateway]] |

## Capabilities
- **Local tools:** runtime, fs, sessions, messaging, web, obsidian_search/read/list
- **Delegation:** Routes to sub-agents (Ultron, Jarvis, Hetzner) via 7-step protocol
- **Channels:** Telegram DM (Mike only), Discord @FactoryLM in #factory-ops-hub
- **Vault access:** Read-only via Obsidian REST API (http://127.0.0.1:27123)

## Delegation Routing

| Task Type | Routes To |
|-----------|-----------|
| Web search / research | [[04_Agents/Ultron/Ultron\|Ultron]] |
| PLC register read/write | [[04_Agents/Jarvis_Local/Jarvis_Local\|Jarvis Local]] |
| Batch compute / large models | [[04_Agents/Hetzner/Hetzner\|Hetzner]] |
| Everything else | Handles locally |

## Model Stack
- **Primary:** DeepSeek V3.2 (`deepseek/deepseek-chat`)
- **Fallbacks:** Groq llama-3.3-70b, OpenRouter Qwen3-coder

## Memory Architecture
- **Layer 1 (deployed):** SOUL.md + vault read-only
- **Layer 2 (planned):** Episodic memory — pgvector, timestamped events
- **Layer 3 (planned):** Semantic memory — RAG over factory docs
- **Layer 4 (planned):** Playbook memory — lessons learned from resolved episodes
- **Layer 5 (planned):** Technician profiles — skill inventories + dispatch matching

## Config Sources
- `~/factorylm/clawd/tony/SOUL.md` — personality + rules
- `~/factorylm/clawd/tony/AGENTS.md` — sub-agent roster
- `~/factorylm/clawd/tony/MEMORY-STRATEGY.md` — 5-layer architecture
- `~/.openclaw/openclaw.json` — runtime config

## Links
- [[03_Projects/Tony_Macaroni/Tony_Macaroni|Tony Macaroni Project]]
