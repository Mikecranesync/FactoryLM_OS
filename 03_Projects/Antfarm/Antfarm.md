---
title: "Antfarm"
date: "2026-02-28"
tags: [type/project, project/antfarm]
status: active
owner: Mike
---

# Antfarm — Project Spec

## Objective
> CLI workflow engine from snarktank/antfarm that orchestrates multi-agent pipelines. Runs planning → implementation → testing → review → PR cycles autonomously.

## Status

| Field | Value |
|-------|-------|
| Status | active |
| Owner | Mike Harper |
| Started | 2026-02-27 |
| Target | Ongoing |

## Background
> Antfarm v0.5.1 was installed to orchestrate complex multi-step workflows that are too involved for single-agent execution. It integrates with OpenClaw to schedule and run 19 workflow pipelines (3 built-in + 16 custom). The `factorylm-feature-dev` pipeline was the first to complete end-to-end autonomously, producing PR #106 in ~75 minutes for ~$0.20 on DeepSeek V3.2.

## Scope

### In Scope
- 19 registered workflows (bug-fix, feature-dev, security-audit + 16 custom)
- Dashboard at http://localhost:3333
- Cron-based scheduling via OpenClaw
- Pipeline orchestration: planner → implementer → tester → reviewer → PR creator

### Out of Scope
- Custom workflow authoring UI (YAML-only)
- Multi-repo workflows (single repo per run)

## Milestones

| Milestone | Target Date | Status |
|-----------|-------------|--------|
| Install + dashboard | 2026-02-27 | done |
| factorylm-feature-dev end-to-end | 2026-02-28 | done (PR #106) |
| All 19 workflows validated | TBD | pending |

## Technical Approach
- **Install:** `~/.openclaw/workspace/antfarm/`
- **Dashboard:** launchd `com.factorylm.antfarm-dashboard` at http://localhost:3333
- **Rollback:** `pre-antfarm-install` git tag

### Known Patches (to `dist/` — lost on `antfarm update`)
1. **step-ops.js** (~line 432): Added `'running'` to `NOT IN` clause for verify step claiming
2. **gateway-api.js** (~line 126): Added `--no-deliver` for `delivery.mode === "none"` crons
3. **workflow.yml** (factorylm-feature-dev): Fixed planner STORIES_JSON output, tester template vars, PR creator template vars

### Known Bug
- `antfarm workflow ensure-crons` creates duplicates — always run manual dedup after

## Dependencies
- [[03_Projects/OpenClaw/OpenClaw|OpenClaw Gateway]] — cron scheduling + agent hosting
- DeepSeek V3.2 API — primary model for all pipeline agents

## Risks
- Patches to `dist/` are lost on `antfarm update`
- Cron dedup bug requires manual cleanup
- ~75 min per feature-dev run — slow for iteration

## Links
- **Install:** `~/.openclaw/workspace/antfarm/`
- **Dashboard:** http://localhost:3333
- **Source:** snarktank/antfarm (upstream)
- **First successful run:** PR #106
