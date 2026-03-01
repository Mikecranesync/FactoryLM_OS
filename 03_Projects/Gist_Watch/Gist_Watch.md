---
title: "Gist Watch"
date: "2026-02-28"
tags: [type/project, project/gist-watch]
status: active
owner: Mike
---

# Gist Watch — Project Spec

## Objective
> MCP server and poller for monitoring GitHub Gists — provides the /gist skill and data access layer for CMMS workflows.

## Status

| Field | Value |
|-------|-------|
| Status | active |
| Owner | Mike Harper |
| Started | 2026-02-27 |
| Target | Ongoing |

## Background
> Added in PR #104, Gist Watch provides an MCP server for gist access plus a poller that monitors gist changes. PR #105 fixed UTF-8 encoding issues in the poller subprocess calls.

## Milestones

| Milestone | Target Date | Status |
|-----------|-------------|--------|
| MCP server + /gist skill | 2026-02-27 | done (PR #104) |
| UTF-8 encoding fix | 2026-02-27 | done (PR #105) |

## Dependencies
- [[03_Projects/Atlas_CMMS/Atlas_CMMS|Atlas CMMS]] — primary consumer
- GitHub Gist API

## Links
- **PRs:** #104, #105
- **Monorepo location:** TBD (check `services/` or `integrations/`)
