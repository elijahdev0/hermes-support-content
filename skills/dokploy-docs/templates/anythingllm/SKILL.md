---
title: "AnythingLLM | Dokploy"
source: "https://docs.dokploy.com/docs/templates/anythingllm"
category: dokploy-docs
created: "2026-06-25T17:21:40.415Z"
---

AnythingLLM | Dokploy

# AnythingLLM

Copy as Markdown

AnythingLLM is a private, self-hosted, and local document chatbot platform that allows you to chat with your documents using various LLM providers.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  anythingllm:
    image: mintplexlabs/anythingllm:latest
    restart: unless-stopped
    ports:
      - 3001
    environment:
      - STORAGE_DIR=/app/server/storage
    volumes:
      - storage:/app/server/storage
    cap_add:
      - SYS_ADMIN

volumes:
  storage: {}
```

```
[variables]
main_domain = "${domain}"

[config]
[[config.domains]]
serviceName = "anythingllm"
port = 3001
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBhbnl0aGluZ2xsbTpcbiAgICBpbWFnZTogbWludHBsZXhsYWJzL2FueXRoaW5nbGxtOmxhdGVzdFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgcG9ydHM6XG4gICAgICAtIDMwMDFcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gU1RPUkFHRV9ESVI9L2FwcC9zZXJ2ZXIvc3RvcmFnZVxuICAgIHZvbHVtZXM6XG4gICAgICAtIHN0b3JhZ2U6L2FwcC9zZXJ2ZXIvc3RvcmFnZVxuICAgIGNhcF9hZGQ6XG4gICAgICAtIFNZU19BRE1JTlxuXG52b2x1bWVzOlxuICBzdG9yYWdlOiB7fSAiLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuXG5bY29uZmlnXVxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiYW55dGhpbmdsbG1cIlxucG9ydCA9IDMwMDFcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCIgIgp9
```

## Links

`ai`,`llm`,`chatbot`

---

Version:`latest`

AnubisAnubis is a bot protector, It will block bots from accessing your website.

AnytypeAnytype is a personal knowledge base—your digital brain—that lets you gather, connect and remix all kinds of information. Create pages, tasks, wikis, journals—even entire apps—and define your own data model while your data stays offline-first, private and encrypted across devices. After installation, you can view the Anytype client configuration by running `cat /data/client-config.yml` inside the service container.

### On this page

ConfigurationBase64LinksTags