---
title: "Hoarder | Dokploy"
source: "https://docs.dokploy.com/docs/templates/hoarder"
category: dokploy-docs
created: "2026-06-25T17:21:49.750Z"
---

Hoarder | Dokploy

# Hoarder

Copy as Markdown

Hoarder is an open source "Bookmark Everything" app that uses AI for automatically tagging the content you throw at it.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  web:
    image: ghcr.io/hoarder-app/hoarder:0.22.0
    restart: unless-stopped
    volumes:
      - hoarder-data:/data
    ports:
      - 3000
    environment:
      - DISABLE_SIGNUPS
      - NEXTAUTH_URL
      - NEXTAUTH_SECRET
      - MEILI_ADDR=http://meilisearch:7700
      - BROWSER_WEB_URL=http://chrome:9222
      - DATA_DIR=/data
      - MEILI_MASTER_KEY
  chrome:
    image: gcr.io/zenika-hub/alpine-chrome:124
    restart: unless-stopped
    command:
      - --no-sandbox
      - --disable-gpu
      - --disable-dev-shm-usage
      - --remote-debugging-address=0.0.0.0
      - --remote-debugging-port=9222
      - --hide-scrollbars
  meilisearch:
    image: getmeili/meilisearch:v1.6
    restart: unless-stopped
    environment:
      - MEILI_MASTER_KEY
      - MEILI_NO_ANALYTICS=true
    volumes:
      - meilisearch-data:/meili_data
    healthcheck:
      test:
        - CMD
        - curl
        - '-f'
        - 'http://127.0.0.1:7700/health'
      interval: 2s
      timeout: 10s
      retries: 15
volumes:
  meilisearch-data:
  hoarder-data:
```

```
[variables]
main_domain = "${domain}"
postgres_password = "${password}"
next_secret = "${base64:32}"
meili_master_key = "${base64:32}"

[config]
env = [
  "NEXTAUTH_SECRET=${next_secret}",
  "MEILI_MASTER_KEY=${meili_master_key}",
  "NEXTAUTH_URL=http://${main_domain}",
]
mounts = []

[[config.domains]]
serviceName = "web"
port = 3_000
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICB3ZWI6XG4gICAgaW1hZ2U6IGdoY3IuaW8vaG9hcmRlci1hcHAvaG9hcmRlcjowLjIyLjBcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIHZvbHVtZXM6XG4gICAgICAtIGhvYXJkZXItZGF0YTovZGF0YVxuICAgIHBvcnRzOlxuICAgICAgLSAzMDAwXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIERJU0FCTEVfU0lHTlVQU1xuICAgICAgLSBORVhUQVVUSF9VUkxcbiAgICAgIC0gTkVYVEFVVEhfU0VDUkVUXG4gICAgICAtIE1FSUxJX0FERFI9aHR0cDovL21laWxpc2VhcmNoOjc3MDBcbiAgICAgIC0gQlJPV1NFUl9XRUJfVVJMPWh0dHA6Ly9jaHJvbWU6OTIyMlxuICAgICAgLSBEQVRBX0RJUj0vZGF0YVxuICAgICAgLSBNRUlMSV9NQVNURVJfS0VZXG4gIGNocm9tZTpcbiAgICBpbWFnZTogZ2NyLmlvL3plbmlrYS1odWIvYWxwaW5lLWNocm9tZToxMjRcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGNvbW1hbmQ6XG4gICAgICAtIC0tbm8tc2FuZGJveFxuICAgICAgLSAtLWRpc2FibGUtZ3B1XG4gICAgICAtIC0tZGlzYWJsZS1kZXYtc2htLXVzYWdlXG4gICAgICAtIC0tcmVtb3RlLWRlYnVnZ2luZy1hZGRyZXNzPTAuMC4wLjBcbiAgICAgIC0gLS1yZW1vdGUtZGVidWdnaW5nLXBvcnQ9OTIyMlxuICAgICAgLSAtLWhpZGUtc2Nyb2xsYmFyc1xuICBtZWlsaXNlYXJjaDpcbiAgICBpbWFnZTogZ2V0bWVpbGkvbWVpbGlzZWFyY2g6djEuNlxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIE1FSUxJX01BU1RFUl9LRVlcbiAgICAgIC0gTUVJTElfTk9fQU5BTFlUSUNTPXRydWVcbiAgICB2b2x1bWVzOlxuICAgICAgLSBtZWlsaXNlYXJjaC1kYXRhOi9tZWlsaV9kYXRhXG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OlxuICAgICAgICAtIENNRFxuICAgICAgICAtIGN1cmxcbiAgICAgICAgLSAnLWYnXG4gICAgICAgIC0gJ2h0dHA6Ly8xMjcuMC4wLjE6NzcwMC9oZWFsdGgnXG4gICAgICBpbnRlcnZhbDogMnNcbiAgICAgIHRpbWVvdXQ6IDEwc1xuICAgICAgcmV0cmllczogMTVcbnZvbHVtZXM6XG4gIG1laWxpc2VhcmNoLWRhdGE6XG4gIGhvYXJkZXItZGF0YToiLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxucG9zdGdyZXNfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmR9XCJcbm5leHRfc2VjcmV0ID0gXCIke2Jhc2U2NDozMn1cIlxubWVpbGlfbWFzdGVyX2tleSA9IFwiJHtiYXNlNjQ6MzJ9XCJcblxuW2NvbmZpZ11cbmVudiA9IFtcbiAgXCJORVhUQVVUSF9TRUNSRVQ9JHtuZXh0X3NlY3JldH1cIixcbiAgXCJNRUlMSV9NQVNURVJfS0VZPSR7bWVpbGlfbWFzdGVyX2tleX1cIixcbiAgXCJORVhUQVVUSF9VUkw9aHR0cDovLyR7bWFpbl9kb21haW59XCIsXG5dXG5tb3VudHMgPSBbXVxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJ3ZWJcIlxucG9ydCA9IDNfMDAwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG4iCn0=
```

## Links

`self-hosted`,`bookmarks`,`link-sharing`

---

Version:`0.22.0`

Hi.eventsHi.Events is a self-hosted event management and ticket selling platform that allows you to create, manage and promote events easily.

HomarrA sleek, modern dashboard that puts all your apps and services in one place with Docker integration.

### On this page

ConfigurationBase64LinksTags