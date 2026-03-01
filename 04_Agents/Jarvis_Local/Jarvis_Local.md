---
title: "Jarvis Local — Agent Profile"
date: "2026-02-28"
tags: [type/project, agent/jarvis, meta/profile, infra/plc]
status: active
---

# Jarvis Local

## Identity

| Field | Value |
|-------|-------|
| Handle | @TravelLaptop_bot |
| Instance | `jarvis-local` |
| Host | Travel Laptop (100.83.251.23) |
| Role | PLC/Modbus edge compute, factory floor |
| Runtime | Jarvis Node at :8765 |

## Capabilities
- PLC register read/write via Modbus TCP
- Direct connection to Allen-Bradley Micro820 at 192.168.1.100:502
- Edge compute on factory floor network

## PLC Access

| Register | Type | Description |
|----------|------|-------------|
| Coils 0-17 | Digital | Control outputs |
| Registers 100-105 | Analog | Sensor readings |

## Connectivity

| System | Access |
|--------|--------|
| Tailscale | Online (100.83.251.23) |
| PLC Laptop | 100.72.2.99 (Jarvis Node :8765 working) |
| Obsidian Vault | No access |
| Telegram | @TravelLaptop_bot |
| Discord | #jarvis channel |

## Notes
- PLC Laptop user is `hharp` (not mike)
- Jarvis Node at port 8765 confirmed working on PLC Laptop
- Receives PLC tasks from [[04_Agents/Tony_Macaroni/Tony_Macaroni|Tony]] via delegation
- **Read-only constraint for AI:** AI agents can read PLC data but NEVER write to PLCs without explicit human approval
