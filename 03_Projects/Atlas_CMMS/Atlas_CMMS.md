---
title: "Atlas CMMS"
date: "2026-02-28"
tags: [type/project, project/atlas-cmms, infra/database]
status: active
owner: Mike
---

# Atlas CMMS — Project Spec

## Objective
> Computerized Maintenance Management System for tracking work orders, assets, and maintenance schedules across the factory.

## Status

| Field | Value |
|-------|-------|
| Status | active |
| Owner | Mike Harper |
| Started | 2026-02 |
| Target | TBD |

## Background
> Atlas CMMS is FactoryLM's maintenance management layer. It has dedicated Antfarm workflows for dispatch, monitoring, testing, and work order creation. The system uses GitHub Gists as a lightweight data store and has dedicated worker agents (cmms-gist-dispatch, cmms-gist-monitor, cmms-gist-tester, cmms-gist-work-order).

## Scope

### In Scope
- Work order creation and tracking
- Gist-based data storage
- Monitoring pipeline (scanner → validator → reporter)
- Dispatch pipeline (designer → dev → tester → devops)
- Integration with FactoryLM maintenance-dispatcher workflow

### Out of Scope
- Full ERP integration
- Inventory management (future)

## Milestones

| Milestone | Target Date | Status |
|-----------|-------------|--------|
| Gist dispatch workflow | 2026-02-28 | active |
| Gist monitor workflow | 2026-02-28 | active |
| Work order workflow | TBD | pending |

## Technical Approach
- **4 Antfarm workflows:** cmms-gist-dispatch (4 agents), cmms-gist-monitor (3 agents), cmms-gist-tester (5 agents), cmms-gist-work-order (5 agents)
- **Data store:** GitHub Gists via [[03_Projects/Gist_Watch/Gist_Watch|Gist Watch]] MCP
- **Integration:** maintenance-dispatcher workflow (5 agents: alarm-monitor, triager, wo-creator, dispatcher, followup)

## Dependencies
- [[03_Projects/Antfarm/Antfarm|Antfarm]] — workflow orchestration
- [[03_Projects/OpenClaw/OpenClaw|OpenClaw Gateway]] — agent hosting
- [[03_Projects/Gist_Watch/Gist_Watch|Gist Watch]] — gist data access

## Risks
- GitHub Gist as data store has rate limits and no ACID guarantees
- Multiple overlapping CMMS workflows may conflict

## Links
- **Monorepo:** `~/factorylm/factorylm/cmms/`
- **Workflows:** cmms-gist-dispatch, cmms-gist-monitor, cmms-gist-tester, cmms-gist-work-order
