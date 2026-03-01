---
title: "Hetzner — Agent Profile"
date: "2026-02-28"
tags: [type/project, agent/hetzner, meta/profile, infra/server]
status: active
---

# Hetzner

## Identity

| Field | Value |
|-------|-------|
| Handle | @UltronVPS_bot (shared with Ultron) |
| Instance | `hetzner` |
| Host | Hetzner (100.67.25.53) |
| Role | Batch compute, large model inference |
| Status | ONLINE |

## Capabilities
- Batch compute tasks
- Large model inference
- Planned: PostgreSQL + pgvector for Tony's memory layers 2-5

## Connectivity

| System | Access |
|--------|--------|
| Tailscale | Online (100.67.25.53) |
| SSH from Mac Mini | No key configured |
| Obsidian Vault | No access |
| Telegram | @UltronVPS_bot (shared handle) |
| Discord | #hetzner channel |

## Planned Deployments
- PostgreSQL + pgvector for episodic/semantic memory (Tony Layer 2-3)
- text-embedding-3-small via OpenAI for document embeddings

## Notes
- Shares Telegram bot handle with Ultron (@UltronVPS_bot) — routing by instance ID
- No SSH key from Mac Mini — cannot be managed remotely
- Target host for Tony's memory infrastructure
