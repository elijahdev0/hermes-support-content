---
title: "Gitea Mirror | Dokploy"
source: "https://docs.dokploy.com/docs/templates/gitea-mirror"
category: dokploy-docs
created: "2026-06-25T17:21:48.522Z"
---

Gitea Mirror | Dokploy

# Gitea Mirror

Copy as Markdown

Gitea Mirror is a modern web app for automatically mirroring repositories from GitHub to your self-hosted Gitea instance. It features a user-friendly interface to sync public, private, or starred GitHub repos, mirror entire organizations with structure preservation, and optionally mirror issues and labels. The application includes smart filtering, detailed logs, and scheduled automatic mirroring.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  gitea-mirror:
    image: ghcr.io/raylabshq/gitea-mirror:latest
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "wget", "--no-verbose", "--tries=3", "--spider", "http://localhost:4321/api/health"]
      interval: 30s
      timeout: 10s
      retries: 5
      start_period: 15s
    environment:
      # Absolutely required - cannot be changed via UI
      - BETTER_AUTH_SECRET=${BETTER_AUTH_SECRET}
      - BETTER_AUTH_URL=${BETTER_AUTH_URL}
      # Core settings with defaults
      - NODE_ENV=production
      - DATABASE_URL=file:data/gitea-mirror.db
      - HOST=0.0.0.0
      - PORT=4321
    volumes:
      - gitea_mirror_data:/app/data

volumes:
  gitea_mirror_data:
```

```
[variables]
main_domain = "${domain}"

[config]
mounts = []

[[config.domains]]
serviceName = "gitea-mirror"
port = 4_321
host = "${main_domain}"

[config.env]
BETTER_AUTH_SECRET = "${base64:64}"
BETTER_AUTH_URL = "https://${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBnaXRlYS1taXJyb3I6XG4gICAgaW1hZ2U6IGdoY3IuaW8vcmF5bGFic2hxL2dpdGVhLW1pcnJvcjpsYXRlc3RcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDogW1wiQ01EXCIsIFwid2dldFwiLCBcIi0tbm8tdmVyYm9zZVwiLCBcIi0tdHJpZXM9M1wiLCBcIi0tc3BpZGVyXCIsIFwiaHR0cDovL2xvY2FsaG9zdDo0MzIxL2FwaS9oZWFsdGhcIl1cbiAgICAgIGludGVydmFsOiAzMHNcbiAgICAgIHRpbWVvdXQ6IDEwc1xuICAgICAgcmV0cmllczogNVxuICAgICAgc3RhcnRfcGVyaW9kOiAxNXNcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgICMgQWJzb2x1dGVseSByZXF1aXJlZCAtIGNhbm5vdCBiZSBjaGFuZ2VkIHZpYSBVSVxuICAgICAgLSBCRVRURVJfQVVUSF9TRUNSRVQ9JHtCRVRURVJfQVVUSF9TRUNSRVR9XG4gICAgICAtIEJFVFRFUl9BVVRIX1VSTD0ke0JFVFRFUl9BVVRIX1VSTH1cbiAgICAgICMgQ29yZSBzZXR0aW5ncyB3aXRoIGRlZmF1bHRzXG4gICAgICAtIE5PREVfRU5WPXByb2R1Y3Rpb25cbiAgICAgIC0gREFUQUJBU0VfVVJMPWZpbGU6ZGF0YS9naXRlYS1taXJyb3IuZGJcbiAgICAgIC0gSE9TVD0wLjAuMC4wXG4gICAgICAtIFBPUlQ9NDMyMVxuICAgIHZvbHVtZXM6XG4gICAgICAtIGdpdGVhX21pcnJvcl9kYXRhOi9hcHAvZGF0YVxuXG52b2x1bWVzOlxuICBnaXRlYV9taXJyb3JfZGF0YTpcbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5cbltjb25maWddXG5tb3VudHMgPSBbXVxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJnaXRlYS1taXJyb3JcIlxucG9ydCA9IDRfMzIxXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuQkVUVEVSX0FVVEhfU0VDUkVUID0gXCIke2Jhc2U2NDo2NH1cIlxuQkVUVEVSX0FVVEhfVVJMID0gXCJodHRwczovLyR7bWFpbl9kb21haW59XCIiCn0=
```

## Links

`git`,`mirror`,`github`,`gitea`,`self-hosted`,`automation`

---

Version:`v2.11.2`

GhostGhost is a free and open source, professional publishing platform built on a modern Node.js technology stack.

Gitea (MySQL)Gitea bundled with MySQL 8.

### On this page

ConfigurationBase64LinksTags