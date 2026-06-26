---
title: "Anytype | Dokploy"
source: "https://docs.dokploy.com/docs/templates/anytype"
category: dokploy-docs
created: "2026-06-25T17:21:40.415Z"
---

Anytype | Dokploy

# Anytype

Copy as Markdown

Anytype is a personal knowledge base—your digital brain—that lets you gather, connect and remix all kinds of information. Create pages, tasks, wikis, journals—even entire apps—and define your own data model while your data stays offline-first, private and encrypted across devices. After installation, you can view the Anytype client configuration by running `cat /data/client-config.yml` inside the service container.

## Configuration

docker-compose.ymltemplate.toml

```
# Example: Any-Sync-Bundle with embedded MongoDB and Redis (all-in-one image)
#
# Usage:
#   docker compose -f compose.aio.yml up -d
#
# The bundle image already contains MongoDB and Redis. Only the bundle service is required

services:
  any-sync-bundle:
    image: ghcr.io/grishy/any-sync-bundle:latest
    restart: unless-stopped
    ports:
      - "33010:33010"
      - "33020:33020/udp"
    volumes:
      - ./data:/data
    environment:
      # Advertise addresses clients should use. Replace with your server hostname/IP.
      ANY_SYNC_BUNDLE_INIT_EXTERNAL_ADDRS: "192.168.100.9"
```

```
[config]
domains = []
mounts = []
env = []
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogIiMgRXhhbXBsZTogQW55LVN5bmMtQnVuZGxlIHdpdGggZW1iZWRkZWQgTW9uZ29EQiBhbmQgUmVkaXMgKGFsbC1pbi1vbmUgaW1hZ2UpXG4jXG4jIFVzYWdlOlxuIyAgIGRvY2tlciBjb21wb3NlIC1mIGNvbXBvc2UuYWlvLnltbCB1cCAtZFxuI1xuIyBUaGUgYnVuZGxlIGltYWdlIGFscmVhZHkgY29udGFpbnMgTW9uZ29EQiBhbmQgUmVkaXMuIE9ubHkgdGhlIGJ1bmRsZSBzZXJ2aWNlIGlzIHJlcXVpcmVkXG5cbnNlcnZpY2VzOlxuICBhbnktc3luYy1idW5kbGU6XG4gICAgaW1hZ2U6IGdoY3IuaW8vZ3Jpc2h5L2FueS1zeW5jLWJ1bmRsZTpsYXRlc3RcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIHBvcnRzOlxuICAgICAgLSBcIjMzMDEwOjMzMDEwXCJcbiAgICAgIC0gXCIzMzAyMDozMzAyMC91ZHBcIlxuICAgIHZvbHVtZXM6XG4gICAgICAtIC4vZGF0YTovZGF0YVxuICAgIGVudmlyb25tZW50OlxuICAgICAgIyBBZHZlcnRpc2UgYWRkcmVzc2VzIGNsaWVudHMgc2hvdWxkIHVzZS4gUmVwbGFjZSB3aXRoIHlvdXIgc2VydmVyIGhvc3RuYW1lL0lQLlxuICAgICAgQU5ZX1NZTkNfQlVORExFX0lOSVRfRVhURVJOQUxfQUREUlM6IFwiMTkyLjE2OC4xMDAuOVwiXG4iLAogICJjb25maWciOiAiW2NvbmZpZ11cbmRvbWFpbnMgPSBbXVxubW91bnRzID0gW11cbmVudiA9IFtdIgp9
```

## Links

`note-taking`,`local-first`,`peer-to-peer`

---

Version:`latest`

AnythingLLMAnythingLLM is a private, self-hosted, and local document chatbot platform that allows you to chat with your documents using various LLM providers.

App FlowyAppFlowy is an open-source alternative to Notion. You are in charge of your data and customizations.

### On this page

ConfigurationBase64LinksTags