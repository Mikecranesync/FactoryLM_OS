---
title: "Cosmos Demo Pipeline"
date: "2026-02-28"
tags: [type/project, project/cosmos]
status: active
owner: Mike
---

# Cosmos Demo Pipeline — Project Spec

## Objective
> Video generation and demo pipeline for the Cosmos Cookoff competition and Jason Calacanis podcast appearance.

## Status

| Field | Value |
|-------|-------|
| Status | active |
| Owner | Mike Harper |
| Started | 2026-02-26 |
| Target | 2026-03-05 (Cosmos Cookoff + podcast) |

## Background
> Cosmos is FactoryLM's demo and video pipeline — an 8-agent Antfarm workflow that curates content, generates scripts, produces videos, validates quality, and distributes the final output. Desktop apps (PLC Reader + GitHub Scraper) were built as Electron apps for the demo.

## Milestones

| Milestone | Target Date | Status |
|-----------|-------------|--------|
| Celery PLC simulator | 2026-02-26 | done (PR #89) |
| PLC Reader desktop app | 2026-02-28 | done (PR #107) |
| Cosmos demo desktop apps | 2026-02-28 | done (PR #108) |
| Cookoff submission | 2026-03-05 | pending |

## Technical Approach
- **Antfarm workflow:** cosmos-video-pipeline (8 agents: content-curator, content-judge, script-improver, cosmos-generator, quality-validator, video-improver, post-processor, distributor + pipeline-orchestrator)
- **Desktop apps:** Electron-based PLC Reader + GitHub Scraper
- **PLC sim:** Celery-based simulator for demo scenarios

## Dependencies
- [[03_Projects/FactoryLM/FactoryLM|FactoryLM]] — core platform
- [[03_Projects/Antfarm/Antfarm|Antfarm]] — workflow engine

## Risks
- Hard deadline: March 5, 2026
- Video generation quality depends on AI model availability

## Links
- **Monorepo:** `~/factorylm/factorylm/cosmos/`
- **Config:** `cosmos.yaml` in repo root
- **PRs:** #89, #107, #108
