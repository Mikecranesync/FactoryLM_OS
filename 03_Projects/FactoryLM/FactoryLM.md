---
title: "FactoryLM"
date: "2026-02-28"
tags: [type/project, project/factorylm, infra/plc, infra/celery]
status: active
owner: Mike
---

# FactoryLM — Project Spec

## Objective
> Industrial AI platform that connects PLCs, runs diagnostics, and predicts failures — built by a solo founder with 30 years of maintenance experience.

## Status

| Field | Value |
|-------|-------|
| Status | active |
| Owner | Mike Harper |
| Started | 2024-06 |
| Target | 2026-03-05 (Cosmos Cookoff + podcast) |

## Background
> FactoryLM is a 4-layer intelligence stack for industrial maintenance: PLC data collection → Celery worker processing → AI diagnosis → human-readable output. It's a monorepo (`~/factorylm/factorylm/`) with 73 top-level items spanning collectors, workers, agents, gateway, HMI, and simulation.

## Scope

### In Scope
- PLC data collection via Modbus TCP (Allen-Bradley Micro820 at 192.168.1.100:502)
- Celery worker pipelines for data processing and enrichment
- AI diagnosis engine (Hammurabi for quality, Herodotus for knowledge)
- Gateway/API layer (OpenClaw on port 18789)
- Cosmos demo pipeline for video generation
- Telegram + Discord agent interfaces

### Out of Scope
- Commercial deployment (pre-revenue)
- Multi-tenant SaaS (single-factory focus for now)

## Milestones

| Milestone | Target Date | Status |
|-----------|-------------|--------|
| Working demo | 2026-02-27 | done |
| Cosmos Cookoff + Jason Calacanis podcast | 2026-03-05 | active |
| PLC Reader desktop app (Electron) | 2026-02-28 | done (PR #107, #108) |

## Technical Approach
- **3-tier product:** Identify (MVP) → Connect (in dev) → Predict (design)
- **Stack:** Python (workers, agents), Node.js (gateway, HMI), Modbus TCP (PLC)
- **AI models:** DeepSeek V3.2 (primary), Groq llama-3.3-70b (fallback), Kimi K2 (enrichment)
- **Orchestration:** OpenClaw gateway + Antfarm workflow engine
- **Read-only constraint:** AI agents can read PLC data but NEVER write to PLCs

## Dependencies
- [[04_Agents/Tony_Macaroni/Tony_Macaroni|Tony Macaroni]] — coordinator agent
- [[03_Projects/OpenClaw/OpenClaw|OpenClaw Gateway]] — agent runtime
- [[03_Projects/Antfarm/Antfarm|Antfarm]] — workflow engine
- Allen-Bradley Micro820 PLC hardware

## Risks
- Solo founder — bus factor of 1
- Demo deadline pressure (Mar 5)
- DeepSeek API reliability for production use

## Links
- **Repo:** `~/factorylm/factorylm/` (Mikecranesync/factorylm on GitHub)
- **README:** v0.26 (2026-02-21) — canonical vision document
- **Architecture:** `~/factorylm/ARCH-DISCOVERY.md`
- **Recent PRs:** #108 (Cosmos demo apps), #107 (PLC Reader), #106 (relay health check)
