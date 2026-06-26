---
title: "Moltbot | Dokploy"
source: "https://docs.dokploy.com/docs/templates/moltbot"
category: dokploy-docs
created: "2026-06-25T17:21:53.155Z"
---

Moltbot | Dokploy

# Moltbot

Copy as Markdown

WhatsApp gateway CLI with Pi RPC agent - self-hosted AI-powered messaging platform

## Configuration

docker-compose.ymltemplate.toml

```
services:
  moltbot-gateway:
    image: ghcr.io/moltbot/clawdbot:2026.1.24-1
    environment:
      HOME: /home/node
      TERM: xterm-256color
      CLAWDBOT_GATEWAY_TOKEN: ${CLAWDBOT_GATEWAY_TOKEN}
      CLAUDE_AI_SESSION_KEY: ${CLAUDE_AI_SESSION_KEY}
      CLAUDE_WEB_SESSION_KEY: ${CLAUDE_WEB_SESSION_KEY}
      CLAUDE_WEB_COOKIE: ${CLAUDE_WEB_COOKIE}
      CLAWDBOT_GATEWAY_URL: ws://0.0.0.0:18789
      OPENROUTER_API_KEY: ${OPENROUTER_API_KEY}
    volumes:
      - moltbot-config:/home/node/.clawdbot
      - moltbot-workspace:/home/node/clawd
    ports:
      - "18789"
      - "18790"
    init: true
    restart: unless-stopped
    command:
      [
        "node",
        "dist/index.js",
        "gateway",
        "--bind",
        "auto",
        "--port",
        "18789",
        "--allow-unconfigured"
      ]

volumes:
  moltbot-config:
  moltbot-workspace:
```

```
[variables]
gateway_token = "${password:32}"

[config]
[[config.domains]]
serviceName = "moltbot-gateway"
port = 18789
host = "${domain}"

[config.env]
CLAWDBOT_GATEWAY_TOKEN = "${gateway_token}"
CLAWDBOT_GATEWAY_PORT = 18789
CLAWDBOT_BRIDGE_PORT = 18790
CLAWDBOT_GATEWAY_BIND="lan"
CLAWDBOT_PLUGINS="discord,memory-core"
# Get here https://openrouter.ai/
OPENROUTER_API_KEY="YOUR-API-KEY"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBtb2x0Ym90LWdhdGV3YXk6XG4gICAgaW1hZ2U6IGdoY3IuaW8vbW9sdGJvdC9jbGF3ZGJvdDoyMDI2LjEuMjQtMVxuICAgIGVudmlyb25tZW50OlxuICAgICAgSE9NRTogL2hvbWUvbm9kZVxuICAgICAgVEVSTTogeHRlcm0tMjU2Y29sb3JcbiAgICAgIENMQVdEQk9UX0dBVEVXQVlfVE9LRU46ICR7Q0xBV0RCT1RfR0FURVdBWV9UT0tFTn1cbiAgICAgIENMQVVERV9BSV9TRVNTSU9OX0tFWTogJHtDTEFVREVfQUlfU0VTU0lPTl9LRVl9XG4gICAgICBDTEFVREVfV0VCX1NFU1NJT05fS0VZOiAke0NMQVVERV9XRUJfU0VTU0lPTl9LRVl9XG4gICAgICBDTEFVREVfV0VCX0NPT0tJRTogJHtDTEFVREVfV0VCX0NPT0tJRX1cbiAgICAgIENMQVdEQk9UX0dBVEVXQVlfVVJMOiB3czovLzAuMC4wLjA6MTg3ODlcbiAgICAgIE9QRU5ST1VURVJfQVBJX0tFWTogJHtPUEVOUk9VVEVSX0FQSV9LRVl9XG4gICAgdm9sdW1lczpcbiAgICAgIC0gbW9sdGJvdC1jb25maWc6L2hvbWUvbm9kZS8uY2xhd2Rib3RcbiAgICAgIC0gbW9sdGJvdC13b3Jrc3BhY2U6L2hvbWUvbm9kZS9jbGF3ZFxuICAgIHBvcnRzOlxuICAgICAgLSBcIjE4Nzg5XCJcbiAgICAgIC0gXCIxODc5MFwiXG4gICAgaW5pdDogdHJ1ZVxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgY29tbWFuZDpcbiAgICAgIFtcbiAgICAgICAgXCJub2RlXCIsXG4gICAgICAgIFwiZGlzdC9pbmRleC5qc1wiLFxuICAgICAgICBcImdhdGV3YXlcIixcbiAgICAgICAgXCItLWJpbmRcIixcbiAgICAgICAgXCJhdXRvXCIsXG4gICAgICAgIFwiLS1wb3J0XCIsXG4gICAgICAgIFwiMTg3ODlcIixcbiAgICAgICAgXCItLWFsbG93LXVuY29uZmlndXJlZFwiXG4gICAgICBdXG5cbnZvbHVtZXM6XG4gIG1vbHRib3QtY29uZmlnOlxuICBtb2x0Ym90LXdvcmtzcGFjZToiLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbmdhdGV3YXlfdG9rZW4gPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcblxuXG5bY29uZmlnXVxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwibW9sdGJvdC1nYXRld2F5XCJcbnBvcnQgPSAxODc4OVxuaG9zdCA9IFwiJHtkb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5DTEFXREJPVF9HQVRFV0FZX1RPS0VOID0gXCIke2dhdGV3YXlfdG9rZW59XCJcbkNMQVdEQk9UX0dBVEVXQVlfUE9SVCA9IDE4Nzg5XG5DTEFXREJPVF9CUklER0VfUE9SVCA9IDE4NzkwXG5DTEFXREJPVF9HQVRFV0FZX0JJTkQ9XCJsYW5cIlxuQ0xBV0RCT1RfUExVR0lOUz1cImRpc2NvcmQsbWVtb3J5LWNvcmVcIlxuIyBHZXQgaGVyZSBodHRwczovL29wZW5yb3V0ZXIuYWkvXG5PUEVOUk9VVEVSX0FQSV9LRVk9XCJZT1VSLUFQSS1LRVlcIlxuIgp9
```

## Links

`whatsapp`,`ai`,`messaging`,`chatbot`,`gateway`,`self-hosted`,`automation`

---

Version:`2026.1.25`

MixpostMixpost is an open-source social media management tool that allows you to create, schedule, and publish posts across multiple social media platforms from a single interface.

MorphosMorphos is a lightweight service for distributed operations and orchestration.

### On this page

ConfigurationBase64LinksTags