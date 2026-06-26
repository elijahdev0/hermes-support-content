---
title: "n8n | Dokploy"
source: "https://docs.dokploy.com/docs/templates/n8n"
category: dokploy-docs
created: "2026-06-25T17:21:54.354Z"
---

n8n | Dokploy

# n8n

Copy as Markdown

n8n is an open source low-code platform for automating workflows and integrations.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  n8n:
    image: docker.n8n.io/n8nio/n8n:1.104.0
    restart: always
    environment:
      - N8N_HOST=${N8N_HOST}
      - N8N_PORT=${N8N_PORT}
      - N8N_PROTOCOL=http
      - NODE_ENV=production
      - WEBHOOK_URL=https://${N8N_HOST}/
      - GENERIC_TIMEZONE=${GENERIC_TIMEZONE}
      - N8N_SECURE_COOKIE=false
    volumes:
      - n8n_data:/home/node/.n8n

volumes:
  n8n_data:
```

```
[variables]
main_domain = "${domain}"

[config]
mounts = []

[[config.domains]]
serviceName = "n8n"
port = 5_678
host = "${main_domain}"

[config.env]
N8N_HOST = "${main_domain}"
N8N_PORT = "5678"
GENERIC_TIMEZONE = "Europe/Berlin"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBuOG46XG4gICAgaW1hZ2U6IGRvY2tlci5uOG4uaW8vbjhuaW8vbjhuOjEuMTA0LjBcbiAgICByZXN0YXJ0OiBhbHdheXNcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gTjhOX0hPU1Q9JHtOOE5fSE9TVH1cbiAgICAgIC0gTjhOX1BPUlQ9JHtOOE5fUE9SVH1cbiAgICAgIC0gTjhOX1BST1RPQ09MPWh0dHBcbiAgICAgIC0gTk9ERV9FTlY9cHJvZHVjdGlvblxuICAgICAgLSBXRUJIT09LX1VSTD1odHRwczovLyR7TjhOX0hPU1R9L1xuICAgICAgLSBHRU5FUklDX1RJTUVaT05FPSR7R0VORVJJQ19USU1FWk9ORX1cbiAgICAgIC0gTjhOX1NFQ1VSRV9DT09LSUU9ZmFsc2VcbiAgICB2b2x1bWVzOlxuICAgICAgLSBuOG5fZGF0YTovaG9tZS9ub2RlLy5uOG5cblxudm9sdW1lczpcbiAgbjhuX2RhdGE6XG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuXG5bY29uZmlnXVxubW91bnRzID0gW11cblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwibjhuXCJcbnBvcnQgPSA1XzY3OFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cbk44Tl9IT1NUID0gXCIke21haW5fZG9tYWlufVwiXG5OOE5fUE9SVCA9IFwiNTY3OFwiXG5HRU5FUklDX1RJTUVaT05FID0gXCJFdXJvcGUvQmVybGluXCJcbiIKfQ==
```

## Links

`automation`

---

Version:`1.104.0`

MumbleMumble is an open-source, low-latency, high-quality voice chat software primarily intended for use while gaming.

n8n + Worker + Runner with Redis/Postgres and Ollaman8n is an open source low-code platform for automating workflows and integrations with PostgreSQL database and Ollama AI model.

### On this page

ConfigurationBase64LinksTags