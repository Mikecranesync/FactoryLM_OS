---
title: "Vault Remote Access Setup"
date: "2026-03-10"
tags: [type/runbook, infra/network, infra/server]
status: active
---

# Vault Remote Access — Tailscale Serve

Exposes the Obsidian REST API to all Tailscale nodes.

## Prerequisites
- Tailscale running on Mac Mini (`open /Applications/Tailscale.app`)
- Obsidian running with REST API plugin (port 27124 HTTPS)

## Enable Tailscale Serve

```bash
# Expose the HTTPS REST API to all Tailscale nodes
tailscale serve --bg https://127.0.0.1:27124
```

This makes the vault API available at:
```
https://michaels-mac-mini.<tailnet>.ts.net/
```

Tailscale handles TLS and authentication at the network level.

## Verify

```bash
# From Mac Mini
tailscale serve status

# From any remote node (e.g. Travel Laptop)
curl -sk "https://michaels-mac-mini.<tailnet>.ts.net/vault/" \
  -H "Authorization: Bearer <OBSIDIAN_API_KEY>" --max-time 10
```

## Fallback: Caddy Reverse Proxy

If Tailscale Serve isn't available:

```bash
brew install caddy

# Create Caddyfile
cat > ~/Caddyfile <<'EOF'
:27200 {
    reverse_proxy https://127.0.0.1:27124 {
        transport http {
            tls_insecure_skip_verify
        }
    }
    @not_tailscale {
        not remote_ip 100.64.0.0/10
    }
    respond @not_tailscale 403
}
EOF

caddy start --config ~/Caddyfile
```

## Remote Node Shell Wrapper

Install on each remote node for CLI access:

```bash
cat > /usr/local/bin/vault-query <<'SCRIPT'
#!/bin/bash
# vault-query — CLI wrapper for Obsidian REST API
VAULT_URL="${OBSIDIAN_HOST:-https://michaels-mac-mini.<tailnet>.ts.net}"
API_KEY="${OBSIDIAN_API_KEY}"
if [ -z "$API_KEY" ]; then echo "Set OBSIDIAN_API_KEY"; exit 1; fi

case "$1" in
  read)  curl -sk "$VAULT_URL/vault/$2" -H "Authorization: Bearer $API_KEY" ;;
  list)  curl -sk "$VAULT_URL/vault/${2:-/}" -H "Authorization: Bearer $API_KEY" ;;
  search) curl -sk -X POST "$VAULT_URL/search/simple/?query=$(python3 -c "import urllib.parse; print(urllib.parse.quote('$2'))")" -H "Authorization: Bearer $API_KEY" ;;
  *) echo "Usage: vault-query {read|list|search} [path|query]" ;;
esac
SCRIPT
chmod +x /usr/local/bin/vault-query
```

## API Key Management

Store in Doppler: project `openclaw`, key `OBSIDIAN_API_KEY`.

## Links
- [[05_Infrastructure/Agent_Connectivity|Agent Connectivity Matrix]]
- [[CLAUDE_TONY|Vault Operating Instructions]]
