---
title: Dashboard
date: 2026-02-25
tags: [meta/dashboard]
status: active
---

# FactoryLM_OS — Dashboard

## Deadlines

| Date | Event | Status |
|------|-------|--------|
| 2026-02-27 | Working demo ready | done |
| 2026-03-05 | Cosmos Cookoff + Jason Calacanis podcast | active |

---

## Active Projects

```dataview
TABLE status, owner, date
FROM "03_Projects"
WHERE status = "active"
SORT date DESC
```

---

## Recent Daily Entries

```dataview
TABLE date, tags
FROM "01_Daily"
SORT date DESC
LIMIT 7
```

---

## Recent Incidents

```dataview
TABLE severity, system, date
FROM "06_Incidents"
SORT date DESC
LIMIT 5
```

---

## Open Action Items

```dataview
TASK
FROM "06_Incidents" OR "03_Projects" OR "08_Runbooks"
WHERE !completed
LIMIT 20
```

---

## Agent Status

| Agent | Role | Host | Status |
|-------|------|------|--------|
| [[04_Agents/Tony_Macaroni/Tony_Macaroni\|Tony Macaroni]] | Boss / coordinator | Mac Mini | Active |
| [[04_Agents/Claude_Code/Claude_Code\|Claude Code]] | System agent / orchestration | Mac Mini | Active |
| [[04_Agents/Ultron/Ultron\|Ultron]] | Cloud reasoning / research | DO VPS | Active |
| [[04_Agents/Jarvis_Local/Jarvis_Local\|Jarvis Local]] | PLC / Modbus edge | Travel Laptop | Active |
| [[04_Agents/Hetzner/Hetzner\|Hetzner]] | Batch compute | Hetzner | Active |
| [[04_Agents/FRIDAY/FRIDAY\|FRIDAY]] | Dev companion | Standalone | Active |
| [[04_Agents/Hammurabi/Hammurabi\|Hammurabi]] | Quality judge | TBD | In development |
| [[04_Agents/Herodotus/Herodotus\|Herodotus]] | Knowledge recorder | TBD | In development |
| [[04_Agents/FactoryLM_Bot/FactoryLM_Bot\|factorylm-bot]] | Commit sync | GitHub Actions | Active |

---

## Infrastructure

| Component | Location |
|-----------|----------|
| Current State | [[05_Infrastructure/Current_State\|Current State]] |
| Agent Connectivity | [[05_Infrastructure/Agent_Connectivity\|Connectivity Matrix]] |
| PLCs | [[05_Infrastructure/PLCs/Micro820\|Micro820 PLC]] |
| Gateway | [[05_Infrastructure/Gateway/OpenClaw_Runtime\|OpenClaw Runtime]] |
| Servers | [[05_Infrastructure/Servers/Mac_Mini\|Mac Mini]] |
| Networks | [[05_Infrastructure/Networks/Tailscale\|Tailscale Network]] |

---

## Quick Links

- [[00_Global/Tags|Tag Taxonomy]]
- [[00_Global/Commands|Vault Commands]]
- [[00_Global/Background_On_Me|About Mike]]
- [[_Templates/|Templates]]

---

## Recent Commits (from factorylm repo)

```dataview
TABLE date, tags
FROM "10_Commit_Notes"
SORT date DESC
LIMIT 5
```
