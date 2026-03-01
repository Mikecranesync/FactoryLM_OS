---
title: "OpenClaw Runtime"
date: "2026-02-28"
tags: [type/runbook, infra/gateway, project/openclaw]
status: active
---

# OpenClaw Runtime

## Service Details

| Field | Value |
|-------|-------|
| Version | v2026.2.26 |
| Port | 18789 |
| launchd | `ai.openclaw.gateway` |
| Config | `~/.openclaw/openclaw.json` |
| Logs | `~/.openclaw/logs/gateway.log` |
| Dashboard | http://127.0.0.1:18789/ |

## Workflows (19 total)

### Built-in (3)
- bug-fix (6 agents)
- feature-dev (7 agents)
- security-audit (8 agents)

### Custom (16)
- cmms-gist-dispatch (4), cmms-gist-monitor (3), cmms-gist-tester (5), cmms-gist-work-order (5)
- cosmos-video-pipeline (8+1)
- factory-opps-calendar (5), factorylm-feature-dev (5), factorylm-incident-response (5)
- factorylm-repo-resurrection (5)
- llm-router (4), maintenance-dispatcher (5), ops-reporter (4)
- robot-advisor (4), state-machine-tester (5), unified-orchestrator (6)
- wiring-telegram-component-enrichment (4)

**Total: 75 agents across all workflows**

## Rollback
```bash
# Stop OpenClaw
launchctl unload ~/Library/LaunchAgents/ai.openclaw.gateway.plist

# Restore clawdbot
launchctl load ~/Library/LaunchAgents/com.clawdbot.gateway.plist.bak
```

## Known Issues
- Node path in plist hardcoded to Cellar version (25.6.1) — breaks on `brew upgrade`
- OpenRouter `:free` model suffixes may 404

## Links
- [[03_Projects/OpenClaw/OpenClaw|OpenClaw Project]]
- [[05_Infrastructure/Current_State|Current State]]
