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
| 2026-02-27 | Working demo ready | active |
| 2026-03-05 | Cosmos Cookoff + Jason Calacanis podcast | upcoming |

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

| Agent | Role | Profile |
|-------|------|---------|
| [[04_Agents/Tony_Macaroni/Tony_Macaroni\|Tony_Macaroni]] | Resident assistant | Active |
| [[04_Agents/Hammurabi/Hammurabi\|Hammurabi]] | Quality judge | In development |
| [[04_Agents/Herodotus/Herodotus\|Herodotus]] | Knowledge recorder | In development |

---

## Infrastructure

| Component | Location |
|-----------|----------|
| PLCs | [[05_Infrastructure/PLCs/]] |
| Gateway (Pi) | [[05_Infrastructure/Gateway/]] |
| Servers | [[05_Infrastructure/Servers/]] |
| Networks | [[05_Infrastructure/Networks/]] |

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
