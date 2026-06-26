---
title: "Grimoire | Dokploy"
source: "https://docs.dokploy.com/docs/templates/grimoire"
category: dokploy-docs
created: "2026-06-25T17:21:49.750Z"
---

Grimoire | Dokploy

# Grimoire

Copy as Markdown

Grimoire is a self-hosted bookmarking app designed for speed and simplicity.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  grimoire:
    image: goniszewski/grimoire:latest
    restart: unless-stopped
    volumes:
      - grimoire_data:/app/data
    ports:
      - "5173"
volumes:
  grimoire_data: {}
```

```
[variables]
main_domain = "${domain}"

[config]
[[config.domains]]
serviceName = "grimoire"
port = 5173
host = "${main_domain}"

[config.env]
PORT = "5173"
PUBLIC_ORIGIN = "https://${main_domain}"
PUBLIC_HTTPS_ONLY = "true"
PUBLIC_SIGNUP_DISABLED = "false"

[[config.mounts]]
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBncmltb2lyZTpcbiAgICBpbWFnZTogZ29uaXN6ZXdza2kvZ3JpbW9pcmU6bGF0ZXN0XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICB2b2x1bWVzOlxuICAgICAgLSBncmltb2lyZV9kYXRhOi9hcHAvZGF0YVxuICAgIHBvcnRzOlxuICAgICAgLSBcIjUxNzNcIlxudm9sdW1lczpcbiAgZ3JpbW9pcmVfZGF0YToge31cbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJncmltb2lyZVwiXG5wb3J0ID0gNTE3M1xuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cblBPUlQgPSBcIjUxNzNcIlxuUFVCTElDX09SSUdJTiA9IFwiaHR0cHM6Ly8ke21haW5fZG9tYWlufVwiXG5QVUJMSUNfSFRUUFNfT05MWSA9IFwidHJ1ZVwiXG5QVUJMSUNfU0lHTlVQX0RJU0FCTEVEID0gXCJmYWxzZVwiXG5cbltbY29uZmlnLm1vdW50c11dXG4iCn0=
```

## Links

`bookmarks`,`self-hosted`,`knowledge-management`

---

Version:`latest`

GrafanaGrafana is an open source platform for data visualization and monitoring.

GristGrist is an open-source spreadsheet and database alternative that combines the flexibility of spreadsheets with the power of databases.

### On this page

ConfigurationBase64LinksTags