---
title: "Mage AI | Dokploy"
source: "https://docs.dokploy.com/docs/templates/mage-ai"
category: dokploy-docs
created: "2026-06-25T17:21:52.047Z"
---

Mage AI | Dokploy

# Mage AI

Copy as Markdown

Build, run, and manage data pipelines for integrating and transforming data.

## Configuration

docker-compose.ymltemplate.toml

```
# https://docs.mage.ai/getting-started/setup#docker-compose
#
# The default credentials are:
#     USERNAME: [email protected]
#     PASSWORD: admin

services:
  mage-ai:
    image: mageai/mageai:0.9.78
    command: mage start ${PROJECT_NAME}
    environment:
      USER_CODE_PATH: /home/src/${PROJECT_NAME}
      ENV: ${ENV}
    expose:
      - 6789
    volumes:
      - mageai_data:/home/src/
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-s", "-f", "-o", "/dev/null", "http://localhost:6789"]
      interval: 30s
      timeout: 10s
      retries: 5

volumes:
  mageai_data:
```

https://docs.dokploy.com/cdn-cgi/l/email-protection

```
[variables]
main_domain = "${domain}"

[[config.domains]]
serviceName = "mage-ai"
port = 6789
host = "${main_domain}"

[config.env]
PROJECT_NAME = "mage-ai"
ENV = "production"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogIiMgaHR0cHM6Ly9kb2NzLm1hZ2UuYWkvZ2V0dGluZy1zdGFydGVkL3NldHVwI2RvY2tlci1jb21wb3NlXG4jXG4jIFRoZSBkZWZhdWx0IGNyZWRlbnRpYWxzIGFyZTpcbiMgICAgIFVTRVJOQU1FOiBhZG1pbkBhZG1pbi5jb21cbiMgICAgIFBBU1NXT1JEOiBhZG1pblxuXG5zZXJ2aWNlczpcbiAgbWFnZS1haTpcbiAgICBpbWFnZTogbWFnZWFpL21hZ2VhaTowLjkuNzhcbiAgICBjb21tYW5kOiBtYWdlIHN0YXJ0ICR7UFJPSkVDVF9OQU1FfVxuICAgIGVudmlyb25tZW50OlxuICAgICAgVVNFUl9DT0RFX1BBVEg6IC9ob21lL3NyYy8ke1BST0pFQ1RfTkFNRX1cbiAgICAgIEVOVjogJHtFTlZ9XG4gICAgZXhwb3NlOlxuICAgICAgLSA2Nzg5XG4gICAgdm9sdW1lczpcbiAgICAgIC0gbWFnZWFpX2RhdGE6L2hvbWUvc3JjL1xuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OiBbXCJDTURcIiwgXCJjdXJsXCIsIFwiLXNcIiwgXCItZlwiLCBcIi1vXCIsIFwiL2Rldi9udWxsXCIsIFwiaHR0cDovL2xvY2FsaG9zdDo2Nzg5XCJdXG4gICAgICBpbnRlcnZhbDogMzBzXG4gICAgICB0aW1lb3V0OiAxMHNcbiAgICAgIHJldHJpZXM6IDVcblxudm9sdW1lczpcbiAgbWFnZWFpX2RhdGE6XG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJtYWdlLWFpXCJcbnBvcnQgPSA2Nzg5XG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuUFJPSkVDVF9OQU1FID0gXCJtYWdlLWFpXCJcbkVOViA9IFwicHJvZHVjdGlvblwiXG4iCn0=
```

## Links

`data`,`dbt`,`etl`,`pipelines`

---

Version:`0.9.78`

MacOS (dockerized)MacOS inside a Docker container.

MailpitMailpit is a tiny, self-contained, and secure email & SMTP testing tool with API for developers.

### On this page

ConfigurationBase64LinksTags