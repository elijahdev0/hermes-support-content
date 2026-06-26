---
title: "Gitingest | Dokploy"
source: "https://docs.dokploy.com/docs/templates/gitingest"
category: dokploy-docs
created: "2026-06-25T17:21:48.522Z"
---

Gitingest | Dokploy

# Gitingest

Copy as Markdown

Gitingest is an application that supports Prometheus metrics, Sentry integration, and S3-backed storage.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  gitingest:
    image: elestio/gitingest:${SOFTWARE_VERSION_TAG}
    restart: unless-stopped
    expose:
      - 8000
    environment:
      - ALLOWED_HOSTS=${ALLOWED_HOSTS}
```

```
[variables]
main_domain = "${domain}"

[config]
[[config.domains]]
serviceName = "gitingest"
port = 8000
host = "${main_domain}"

[config.env]
SOFTWARE_VERSION_TAG = "latest"
ALLOWED_HOSTS = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBnaXRpbmdlc3Q6XG4gICAgaW1hZ2U6IGVsZXN0aW8vZ2l0aW5nZXN0OiR7U09GVFdBUkVfVkVSU0lPTl9UQUd9XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBleHBvc2U6XG4gICAgICAtIDgwMDBcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gQUxMT1dFRF9IT1NUUz0ke0FMTE9XRURfSE9TVFN9XG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJnaXRpbmdlc3RcIlxucG9ydCA9IDgwMDBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5TT0ZUV0FSRV9WRVJTSU9OX1RBRyA9IFwibGF0ZXN0XCJcbkFMTE9XRURfSE9TVFMgPSBcIiR7bWFpbl9kb21haW59XCJcbiIKfQ==
```

## Links

`analytics`,`s3`,`monitoring`,`sentry`,`metrics`

---

Version:`latest`

Gitea (SQLite)Self-hosted Git service using SQLite for a simple one-container setup.

GitLab CEGitLab Community Edition is a free and open source platform for managing Git repositories, CI/CD pipelines, and project management.

### On this page

ConfigurationBase64LinksTags