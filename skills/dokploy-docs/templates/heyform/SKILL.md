---
title: "HeyForm | Dokploy"
source: "https://docs.dokploy.com/docs/templates/heyform"
category: dokploy-docs
created: "2026-06-25T17:21:49.750Z"
---

HeyForm | Dokploy

# HeyForm

Copy as Markdown

Allows anyone to create engaging conversational forms for surveys, questionnaires, quizzes, and polls. No coding skills required.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  heyform:
    image: heyform/community-edition:latest
    restart: always
    volumes:
      # Persist uploaded images
      - heyform-data:/app/static/upload
    depends_on:
      - mongo
      - redis
    ports:
      - 8000
    env_file:
      - .env
    environment:
      MONGO_URI: 'mongodb://mongo:27017/heyform'
      REDIS_HOST: redis
      REDIS_PORT: 6379
    networks:
      - heyform-network

  mongo:
    image: percona/percona-server-mongodb:4.4
    restart: always
    networks:
      - heyform-network
    volumes:
      # Persist MongoDB data
      - mongo-data:/data/db

  redis:
    image: redis
    restart: always
    command: "redis-server --appendonly yes"
    networks:
      - heyform-network
    volumes:
      # Persist KeyDB data
      - redis-data:/data

networks:
  heyform-network:
    driver: bridge

volumes:
  heyform-data:
  mongo-data:
  redis-data:
```

```
[variables]
main_domain = "${domain}"
session_key = "${base64:64}"
form_encryption_key = "${base64:64}"

[config]
env = [
  "APP_HOMEPAGE_URL=http://${main_domain}",
  "SESSION_KEY=${session_key}",
  "FORM_ENCRYPTION_KEY=${form_encryption_key}",
]
mounts = []

[[config.domains]]
serviceName = "heyform"
port = 8_000
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBoZXlmb3JtOlxuICAgIGltYWdlOiBoZXlmb3JtL2NvbW11bml0eS1lZGl0aW9uOmxhdGVzdFxuICAgIHJlc3RhcnQ6IGFsd2F5c1xuICAgIHZvbHVtZXM6XG4gICAgICAjIFBlcnNpc3QgdXBsb2FkZWQgaW1hZ2VzXG4gICAgICAtIGhleWZvcm0tZGF0YTovYXBwL3N0YXRpYy91cGxvYWRcbiAgICBkZXBlbmRzX29uOlxuICAgICAgLSBtb25nb1xuICAgICAgLSByZWRpc1xuICAgIHBvcnRzOlxuICAgICAgLSA4MDAwXG4gICAgZW52X2ZpbGU6XG4gICAgICAtIC5lbnZcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIE1PTkdPX1VSSTogJ21vbmdvZGI6Ly9tb25nbzoyNzAxNy9oZXlmb3JtJ1xuICAgICAgUkVESVNfSE9TVDogcmVkaXNcbiAgICAgIFJFRElTX1BPUlQ6IDYzNzlcbiAgICBuZXR3b3JrczpcbiAgICAgIC0gaGV5Zm9ybS1uZXR3b3JrXG5cbiAgbW9uZ286XG4gICAgaW1hZ2U6IHBlcmNvbmEvcGVyY29uYS1zZXJ2ZXItbW9uZ29kYjo0LjRcbiAgICByZXN0YXJ0OiBhbHdheXNcbiAgICBuZXR3b3JrczpcbiAgICAgIC0gaGV5Zm9ybS1uZXR3b3JrXG4gICAgdm9sdW1lczpcbiAgICAgICMgUGVyc2lzdCBNb25nb0RCIGRhdGFcbiAgICAgIC0gbW9uZ28tZGF0YTovZGF0YS9kYlxuXG4gIHJlZGlzOlxuICAgIGltYWdlOiByZWRpc1xuICAgIHJlc3RhcnQ6IGFsd2F5c1xuICAgIGNvbW1hbmQ6IFwicmVkaXMtc2VydmVyIC0tYXBwZW5kb25seSB5ZXNcIlxuICAgIG5ldHdvcmtzOlxuICAgICAgLSBoZXlmb3JtLW5ldHdvcmtcbiAgICB2b2x1bWVzOlxuICAgICAgIyBQZXJzaXN0IEtleURCIGRhdGFcbiAgICAgIC0gcmVkaXMtZGF0YTovZGF0YVxuXG5uZXR3b3JrczpcbiAgaGV5Zm9ybS1uZXR3b3JrOlxuICAgIGRyaXZlcjogYnJpZGdlXG5cbnZvbHVtZXM6XG4gIGhleWZvcm0tZGF0YTpcbiAgbW9uZ28tZGF0YTpcbiAgcmVkaXMtZGF0YTpcbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5zZXNzaW9uX2tleSA9IFwiJHtiYXNlNjQ6NjR9XCJcbmZvcm1fZW5jcnlwdGlvbl9rZXkgPSBcIiR7YmFzZTY0OjY0fVwiXG5cbltjb25maWddXG5lbnYgPSBbXG4gIFwiQVBQX0hPTUVQQUdFX1VSTD1odHRwOi8vJHttYWluX2RvbWFpbn1cIixcbiAgXCJTRVNTSU9OX0tFWT0ke3Nlc3Npb25fa2V5fVwiLFxuICBcIkZPUk1fRU5DUllQVElPTl9LRVk9JHtmb3JtX2VuY3J5cHRpb25fa2V5fVwiLFxuXVxubW91bnRzID0gW11cblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiaGV5Zm9ybVwiXG5wb3J0ID0gOF8wMDBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcbiIKfQ==
```

## Links

`form`,`builder`,`questionnaire`,`quiz`,`survey`

---

Version:`latest`

HabiticaHabitica is a free habit and productivity app that treats your real life like a game. With in-game rewards and punishments to motivate you and a strong social network to inspire you, Habitica can help you achieve your goals to become healthy and hard-working.

Hi.eventsHi.Events is a self-hosted event management and ticket selling platform that allows you to create, manage and promote events easily.

### On this page

ConfigurationBase64LinksTags