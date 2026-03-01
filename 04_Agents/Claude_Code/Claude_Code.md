---
title: "Claude Code (Macaroni) — Agent Profile"
date: "2026-02-28"
tags: [type/project, agent/claude-code, meta/profile]
status: active
---

# Claude Code (Macaroni)

## Identity

| Field | Value |
|-------|-------|
| Handle | N/A (CLI agent) |
| Instance | `macaroni` |
| Host | Mac Mini (100.108.19.94) |
| Role | FactoryLM system agent — orchestration, discovery, automation |
| Runtime | Claude Code CLI (Anthropic) |

## Capabilities
- Full filesystem access on Mac Mini
- Git operations across all repos
- MCP server access (Serena for code intelligence, Obsidian REST API)
- Bash command execution
- Multi-agent task delegation (subagents)
- Persistent auto-memory at `~/.claude/projects/-Users-factorylm/memory/`

## Connectivity

| System | Access |
|--------|--------|
| Obsidian Vault | MCP via port 27124 (HTTPS) — read-only by policy |
| All local repos | Full read/write |
| GitHub | Via `gh` CLI |
| Tailscale network | Can ping all nodes |
| OpenClaw | Local access (port 18789) |

## Notes
- Primary development agent for infrastructure work
- Has the most comprehensive system knowledge (MEMORY.md)
- Read-only vault policy per CLAUDE_TONY.md
- Model: Claude Opus 4.6
