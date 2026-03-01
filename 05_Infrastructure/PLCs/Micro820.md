---
title: "Allen-Bradley Micro820"
date: "2026-02-28"
tags: [type/runbook, infra/plc]
status: active
---

# Allen-Bradley Micro820

## Hardware

| Field | Value |
|-------|-------|
| Model | 2080-LC30-48QWB |
| Address | 192.168.1.100:502 |
| Protocol | Modbus TCP |
| Status | Working |
| Access via | PLC Laptop (100.72.2.99) → [[04_Agents/Jarvis_Local/Jarvis_Local\|Jarvis Local]] |

## Register Map

### Coils (Digital Outputs)

| Coil | Range |
|------|-------|
| 0-17 | Control outputs |

### Holding Registers (Analog)

| Register | Range |
|----------|-------|
| 100-105 | Sensor readings |

## Safety Rules
- **AI agents can READ PLC data but NEVER WRITE to PLCs** without explicit human approval
- No PLC credential exposure in logs or agent messages
- Sub-agents have read-only access to PLC data via [[04_Agents/Jarvis_Local/Jarvis_Local|Jarvis]]

## Links
- [[04_Agents/Jarvis_Local/Jarvis_Local|Jarvis Local]] — PLC access agent
- [[05_Infrastructure/Networks/Tailscale|Tailscale Network]] — network topology
