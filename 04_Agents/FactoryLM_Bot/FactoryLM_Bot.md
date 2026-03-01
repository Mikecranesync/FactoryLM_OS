---
title: "factorylm-bot — Agent Profile"
date: "2026-02-28"
tags: [type/project, agent/factorylm-bot, meta/profile]
status: active
---

# factorylm-bot

## Identity

| Field | Value |
|-------|-------|
| Handle | N/A (GitHub Actions bot) |
| Instance | GitHub Actions |
| Host | GitHub-hosted runners |
| Role | Commit notes sync — writes raw commit tables to vault every 30 minutes |

## Capabilities
- Crawls all Mikecranesync repos via GitHub API
- Creates/updates `10_Commit_Notes/YYYY-MM-DD.md` files
- Pushes directly to FactoryLM_OS main branch

## Workflows
- **`commit-notes-sync.yml`** (in FactoryLM_OS): 30-min cron, crawls all repos
- **`commit-notes-to-vault.yml`** (in factorylm): On push to main, syncs that repo's commits

## Known Issues
- Generates significant noise: `sync: update commit notes` commits are recursive (the sync itself creates commits that get synced)
- No enrichment — writes raw hash/message/author tables only
- No wikilinks to projects, agents, or infrastructure
- No awareness of vault structure or taxonomy
- Two separate workflows produce slightly different section header formats

## Connectivity

| System | Access |
|--------|--------|
| GitHub API | Full (via GITHUB_TOKEN) |
| Vault (write) | Direct git push to FactoryLM_OS |
| Vault (read) | No context awareness |
| Obsidian | No access |

## Notes
- The primary data source for 10_Commit_Notes/ (344 files spanning 20 months)
- Enrichment is a separate, disconnected process (see [[03_Projects/FactoryLM/FactoryLM|enricher]])
