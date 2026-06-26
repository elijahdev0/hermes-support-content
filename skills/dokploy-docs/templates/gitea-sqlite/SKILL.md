---
title: "Gitea (SQLite) | Dokploy"
source: "https://docs.dokploy.com/docs/templates/gitea-sqlite"
category: dokploy-docs
created: "2026-06-25T17:21:48.522Z"
---

Gitea (SQLite) | Dokploy

# Gitea (SQLite)

Copy as Markdown

Self-hosted Git service using SQLite for a simple one-container setup.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  gitea:
    image: docker.gitea.com/gitea:1.24.4
    restart: unless-stopped
    environment:
      - USER_UID=1000
      - USER_GID=1000
      # SQLite (default) lives at /data/gitea
      # Example optional overrides (set in template.toml env or UI):
      # - GITEA__mailer__ENABLED=true
    volumes:
      - gitea-data:/data
    expose:
      - "3000" # Web UI
      - "22" # SSH (internal only)
    healthcheck:
      test: ["CMD", "wget", "-q", "--spider", "http://localhost:3000/"]
      interval: 15s
      timeout: 5s
      retries: 10

volumes:
  gitea-data: {}
```

```
[variables]
main_domain = "${domain}"

[config]
[[config.domains]]
serviceName = "gitea"
port = 3000
host = "${main_domain}"

[config.env]
USER_UID = "1000"
USER_GID = "1000"

# Optional: enable SMTP (or set later in UI)
# GITEA__mailer__ENABLED = "true"
# GITEA__mailer__FROM = "gitea@${username}.example.com"
# GITEA__mailer__PROTOCOL = "smtps"
# GITEA__mailer__SMTP_ADDR = "smtp.example.com"
# GITEA__mailer__SMTP_PORT = "465"
# GITEA__mailer__USER = "apikey"
# GITEA__mailer__PASSWD = "${password:32}"

[[config.mounts]]
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIGdpdGVhOlxuICAgIGltYWdlOiBkb2NrZXIuZ2l0ZWEuY29tL2dpdGVhOjEuMjQuNFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIFVTRVJfVUlEPTEwMDBcbiAgICAgIC0gVVNFUl9HSUQ9MTAwMFxuICAgICAgIyBTUUxpdGUgKGRlZmF1bHQpIGxpdmVzIGF0IC9kYXRhL2dpdGVhXG4gICAgICAjIEV4YW1wbGUgb3B0aW9uYWwgb3ZlcnJpZGVzIChzZXQgaW4gdGVtcGxhdGUudG9tbCBlbnYgb3IgVUkpOlxuICAgICAgIyAtIEdJVEVBX19tYWlsZXJfX0VOQUJMRUQ9dHJ1ZVxuICAgIHZvbHVtZXM6XG4gICAgICAtIGdpdGVhLWRhdGE6L2RhdGFcbiAgICBleHBvc2U6XG4gICAgICAtIFwiMzAwMFwiICMgV2ViIFVJXG4gICAgICAtIFwiMjJcIiAjIFNTSCAoaW50ZXJuYWwgb25seSlcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6IFtcIkNNRFwiLCBcIndnZXRcIiwgXCItcVwiLCBcIi0tc3BpZGVyXCIsIFwiaHR0cDovL2xvY2FsaG9zdDozMDAwL1wiXVxuICAgICAgaW50ZXJ2YWw6IDE1c1xuICAgICAgdGltZW91dDogNXNcbiAgICAgIHJldHJpZXM6IDEwXG5cbnZvbHVtZXM6XG4gIGdpdGVhLWRhdGE6IHt9XG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuXG5bY29uZmlnXVxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiZ2l0ZWFcIlxucG9ydCA9IDMwMDBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5VU0VSX1VJRCA9IFwiMTAwMFwiXG5VU0VSX0dJRCA9IFwiMTAwMFwiXG5cbiMgT3B0aW9uYWw6IGVuYWJsZSBTTVRQIChvciBzZXQgbGF0ZXIgaW4gVUkpXG4jIEdJVEVBX19tYWlsZXJfX0VOQUJMRUQgPSBcInRydWVcIlxuIyBHSVRFQV9fbWFpbGVyX19GUk9NID0gXCJnaXRlYUAke3VzZXJuYW1lfS5leGFtcGxlLmNvbVwiXG4jIEdJVEVBX19tYWlsZXJfX1BST1RPQ09MID0gXCJzbXRwc1wiXG4jIEdJVEVBX19tYWlsZXJfX1NNVFBfQUREUiA9IFwic210cC5leGFtcGxlLmNvbVwiXG4jIEdJVEVBX19tYWlsZXJfX1NNVFBfUE9SVCA9IFwiNDY1XCJcbiMgR0lURUFfX21haWxlcl9fVVNFUiA9IFwiYXBpa2V5XCJcbiMgR0lURUFfX21haWxlcl9fUEFTU1dEID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5cbltbY29uZmlnLm1vdW50c11dIgp9
```

## Links

`git`,`scm`,`developer-tools`,`self-hosted`

---

Version:`1.24.4`

Gitea (PostgreSQL)Gitea bundled with PostgreSQL.

GitingestGitingest is an application that supports Prometheus metrics, Sentry integration, and S3-backed storage.

### On this page

ConfigurationBase64LinksTags