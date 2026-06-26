---
title: "Kokoro Web | Dokploy"
source: "https://docs.dokploy.com/docs/templates/kokoro-web"
category: dokploy-docs
created: "2026-06-25T17:21:50.891Z"
---

Kokoro Web | Dokploy

# Kokoro Web

Copy as Markdown

Kokoro Web provides an interface for text-to-speech using advanced AI voice synthesis. It allows model caching and API integration with authentication.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  kokoro-web:
    image: ghcr.io/eduardolat/kokoro-web:latest
    restart: unless-stopped
    environment:
      - KW_SECRET_API_KEY=${KW_SECRET_API_KEY}
      - KW_PUBLIC_NO_TRACK=${KW_PUBLIC_NO_TRACK}
    volumes:
      - kokoro-cache:/kokoro/cache

volumes:
  kokoro-cache: {}
```

```
[variables]
main_domain = "${domain}"
api_key = "${password:32}"   # Secure random API key for Kokoro Web
no_track = "false"           # Set to "true" to opt out of analytics

[config]
[[config.domains]]
serviceName = "kokoro-web"
port = 3000
host = "${main_domain}"

[config.env]
KW_SECRET_API_KEY = "${api_key}"
KW_PUBLIC_NO_TRACK = "${no_track}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIGtva29yby13ZWI6XG4gICAgaW1hZ2U6IGdoY3IuaW8vZWR1YXJkb2xhdC9rb2tvcm8td2ViOmxhdGVzdFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIEtXX1NFQ1JFVF9BUElfS0VZPSR7S1dfU0VDUkVUX0FQSV9LRVl9XG4gICAgICAtIEtXX1BVQkxJQ19OT19UUkFDSz0ke0tXX1BVQkxJQ19OT19UUkFDS31cbiAgICB2b2x1bWVzOlxuICAgICAgLSBrb2tvcm8tY2FjaGU6L2tva29yby9jYWNoZVxuXG52b2x1bWVzOlxuICBrb2tvcm8tY2FjaGU6IHt9XG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuYXBpX2tleSA9IFwiJHtwYXNzd29yZDozMn1cIiAgICMgU2VjdXJlIHJhbmRvbSBBUEkga2V5IGZvciBLb2tvcm8gV2ViXG5ub190cmFjayA9IFwiZmFsc2VcIiAgICAgICAgICAgIyBTZXQgdG8gXCJ0cnVlXCIgdG8gb3B0IG91dCBvZiBhbmFseXRpY3NcblxuW2NvbmZpZ11cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImtva29yby13ZWJcIlxucG9ydCA9IDMwMDBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5LV19TRUNSRVRfQVBJX0tFWSA9IFwiJHthcGlfa2V5fVwiXG5LV19QVUJMSUNfTk9fVFJBQ0sgPSBcIiR7bm9fdHJhY2t9XCJcbiIKfQ==
```

## Links

`text-to-speech`,`ai`,`voice`,`web`

---

Version:`latest`

Kokoro TTSDockerized FastAPI wrapper for the Kokoro-82M text-to-speech model with multi-language support and OpenAI-compatible endpoints.

Komari MonitorA lightweight, self-hosted server monitoring tool for tracking server performance.

### On this page

ConfigurationBase64LinksTags