---
title: Tag Taxonomy
date: 2026-02-25
tags: [meta/tags]
status: active
---

# Tag Taxonomy

All tags used in this vault. **Do not invent new tags** — add them here first, then use them.

---

## Type Tags
> What kind of note is this?

| Tag | Usage |
|-----|-------|
| `type/daily` | Daily journal entries |
| `type/weekly` | Weekly review entries |
| `type/project` | Project specs and notes |
| `type/incident` | Incident writeups and post-mortems |
| `type/research` | Research notes and spikes |
| `type/runbook` | Deployment and recovery procedures |
| `type/commit-note` | Auto-generated commit digests |

---

## Project Tags
> Which project does this relate to?

| Tag | Usage |
|-----|-------|
| `project/factorylm` | Core FactoryLM platform |
| `project/tony-macaroni` | Tony_Macaroni assistant |
| `project/clawdbot` | Clawdbot project |
| `project/discord-adapter` | Discord adapter project |

---

## Agent Tags
> Which AI agent is involved?

| Tag | Usage |
|-----|-------|
| `agent/tony` | Tony_Macaroni — resident assistant |
| `agent/hammurabi` | Hammurabi — quality judge |
| `agent/herodotus` | Herodotus — knowledge recorder |

---

## Infrastructure Tags
> What systems or hardware are involved?

| Tag | Usage |
|-----|-------|
| `infra/plc` | PLC hardware and collectors |
| `infra/gateway` | Raspberry Pi edge gateway |
| `infra/server` | Cloud servers and compute |
| `infra/network` | Network topology and connectivity |
| `infra/celery` | Celery workers and task queues |
| `infra/database` | Database systems |

---

## Status Tags
> What state is this item in?

| Tag | Usage |
|-----|-------|
| `status/active` | Currently being worked on |
| `status/blocked` | Waiting on something |
| `status/done` | Completed |
| `status/archived` | Moved to 09_Archive |
| `status/draft` | Not yet finalized |

---

## Meta Tags
> Vault-level organizational tags

| Tag | Usage |
|-----|-------|
| `meta/profile` | User profile and background |
| `meta/dashboard` | Dashboard and overview pages |
| `meta/tags` | This file |
| `meta/commands` | Vault workflow commands |

---

## Severity Tags (Incidents only)

| Tag | Usage |
|-----|-------|
| `severity/low` | Minor issue, no user impact |
| `severity/medium` | Degraded service, workaround exists |
| `severity/high` | Significant impact, needs prompt fix |
| `severity/critical` | System down, all hands on deck |

---

## Adding New Tags

1. Add the tag to the appropriate section in this file
2. Include a short description of when to use it
3. Then use it in your notes
4. Never create orphan tags — they all live here
