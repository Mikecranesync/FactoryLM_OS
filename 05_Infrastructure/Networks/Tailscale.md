---
title: "Tailscale Network"
date: "2026-02-28"
tags: [type/runbook, infra/network]
status: active
---

# Tailscale Network

## Topology

All FactoryLM devices are on a Tailscale mesh network. The Mac Mini is the primary hub.

```
Mac Mini (100.108.19.94) ─── primary hub
├── DO VPS / Ultron (100.68.120.99)
├── Hetzner (100.67.25.53)
├── PLC Laptop (100.72.2.99) ─── Micro820 PLC (192.168.1.100)
├── Travel Laptop (100.83.251.23)
├── Pi Edge (100.66.216.6) ─── degraded
└── srv1078052 (100.102.30.102) ─── review for decommission
```

## SSH Access Gaps
- Mac Mini → DO VPS: No SSH key
- Mac Mini → Hetzner: No SSH key
- Mac Mini → Pi Edge: SSH broken (balenaOS)

## Notes
- Pi Tailscale IP changed from 100.97.210.121 to 100.66.216.6
- PLC Laptop user is `hharp` (not mike)
- See [[05_Infrastructure/Current_State|Current State]] for full device table
