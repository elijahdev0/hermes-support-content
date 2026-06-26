---
title: "RSSHub | Dokploy"
source: "https://docs.dokploy.com/docs/templates/rsshub"
category: dokploy-docs
created: "2026-06-25T17:21:57.938Z"
---

RSSHub | Dokploy

# RSSHub

Copy as Markdown

RSSHub is the world's largest RSS network, consisting of over 5,000 global instances.RSSHub delivers millions of contents aggregated from all kinds of sources, our vibrant open source community is ensuring the deliver of RSSHub's new routes, new features and bug fixes.

## Configuration

docker-compose.ymltemplate.toml

```
services:
    rsshub:
        # two ways to enable puppeteer:
        # * comment out marked lines, then use this image instead: diygod/rsshub:chromium-bundled
        # * (consumes more disk space and memory) leave everything unchanged
        image: diygod/rsshub
        restart: always
        ports:
            - 1200
        environment:
            NODE_ENV: production
            CACHE_TYPE: redis
            REDIS_URL: "redis://redis:6379/"
            PUPPETEER_WS_ENDPOINT: "ws://browserless:3000" # marked
        healthcheck:
            test: ["CMD", "curl", "-f", "http://localhost:1200/healthz"]
            interval: 30s
            timeout: 10s
            retries: 3
        depends_on:
            - redis
            - browserless # marked

    browserless: # marked
        image: browserless/chrome # marked
        restart: always # marked
        ulimits: # marked
            core: # marked
                hard: 0 # marked
                soft: 0 # marked
        healthcheck:
            test: ["CMD", "curl", "-f", "http://localhost:3000/pressure"]
            interval: 30s
            timeout: 10s
            retries: 3

    redis:
        image: redis:alpine
        restart: always
        volumes:
            - redis-data:/data
        healthcheck:
            test: ["CMD", "redis-cli", "ping"]
            interval: 30s
            timeout: 10s
            retries: 5
            start_period: 5s

volumes:
    redis-data:
```

```
[variables]
main_domain = "${domain}"

[config]
[[config.domains]]
serviceName = "rsshub"
port = 1200
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICAgIHJzc2h1YjpcbiAgICAgICAgIyB0d28gd2F5cyB0byBlbmFibGUgcHVwcGV0ZWVyOlxuICAgICAgICAjICogY29tbWVudCBvdXQgbWFya2VkIGxpbmVzLCB0aGVuIHVzZSB0aGlzIGltYWdlIGluc3RlYWQ6IGRpeWdvZC9yc3NodWI6Y2hyb21pdW0tYnVuZGxlZFxuICAgICAgICAjICogKGNvbnN1bWVzIG1vcmUgZGlzayBzcGFjZSBhbmQgbWVtb3J5KSBsZWF2ZSBldmVyeXRoaW5nIHVuY2hhbmdlZFxuICAgICAgICBpbWFnZTogZGl5Z29kL3Jzc2h1YlxuICAgICAgICByZXN0YXJ0OiBhbHdheXNcbiAgICAgICAgcG9ydHM6XG4gICAgICAgICAgICAtIDEyMDBcbiAgICAgICAgZW52aXJvbm1lbnQ6XG4gICAgICAgICAgICBOT0RFX0VOVjogcHJvZHVjdGlvblxuICAgICAgICAgICAgQ0FDSEVfVFlQRTogcmVkaXNcbiAgICAgICAgICAgIFJFRElTX1VSTDogXCJyZWRpczovL3JlZGlzOjYzNzkvXCJcbiAgICAgICAgICAgIFBVUFBFVEVFUl9XU19FTkRQT0lOVDogXCJ3czovL2Jyb3dzZXJsZXNzOjMwMDBcIiAjIG1hcmtlZFxuICAgICAgICBoZWFsdGhjaGVjazpcbiAgICAgICAgICAgIHRlc3Q6IFtcIkNNRFwiLCBcImN1cmxcIiwgXCItZlwiLCBcImh0dHA6Ly9sb2NhbGhvc3Q6MTIwMC9oZWFsdGh6XCJdXG4gICAgICAgICAgICBpbnRlcnZhbDogMzBzXG4gICAgICAgICAgICB0aW1lb3V0OiAxMHNcbiAgICAgICAgICAgIHJldHJpZXM6IDNcbiAgICAgICAgZGVwZW5kc19vbjpcbiAgICAgICAgICAgIC0gcmVkaXNcbiAgICAgICAgICAgIC0gYnJvd3Nlcmxlc3MgIyBtYXJrZWRcblxuICAgIGJyb3dzZXJsZXNzOiAjIG1hcmtlZFxuICAgICAgICBpbWFnZTogYnJvd3Nlcmxlc3MvY2hyb21lICMgbWFya2VkXG4gICAgICAgIHJlc3RhcnQ6IGFsd2F5cyAjIG1hcmtlZFxuICAgICAgICB1bGltaXRzOiAjIG1hcmtlZFxuICAgICAgICAgICAgY29yZTogIyBtYXJrZWRcbiAgICAgICAgICAgICAgICBoYXJkOiAwICMgbWFya2VkXG4gICAgICAgICAgICAgICAgc29mdDogMCAjIG1hcmtlZFxuICAgICAgICBoZWFsdGhjaGVjazpcbiAgICAgICAgICAgIHRlc3Q6IFtcIkNNRFwiLCBcImN1cmxcIiwgXCItZlwiLCBcImh0dHA6Ly9sb2NhbGhvc3Q6MzAwMC9wcmVzc3VyZVwiXVxuICAgICAgICAgICAgaW50ZXJ2YWw6IDMwc1xuICAgICAgICAgICAgdGltZW91dDogMTBzXG4gICAgICAgICAgICByZXRyaWVzOiAzXG5cbiAgICByZWRpczpcbiAgICAgICAgaW1hZ2U6IHJlZGlzOmFscGluZVxuICAgICAgICByZXN0YXJ0OiBhbHdheXNcbiAgICAgICAgdm9sdW1lczpcbiAgICAgICAgICAgIC0gcmVkaXMtZGF0YTovZGF0YVxuICAgICAgICBoZWFsdGhjaGVjazpcbiAgICAgICAgICAgIHRlc3Q6IFtcIkNNRFwiLCBcInJlZGlzLWNsaVwiLCBcInBpbmdcIl1cbiAgICAgICAgICAgIGludGVydmFsOiAzMHNcbiAgICAgICAgICAgIHRpbWVvdXQ6IDEwc1xuICAgICAgICAgICAgcmV0cmllczogNVxuICAgICAgICAgICAgc3RhcnRfcGVyaW9kOiA1c1xuXG52b2x1bWVzOlxuICAgIHJlZGlzLWRhdGE6IiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcblxuW2NvbmZpZ11cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcInJzc2h1YlwiXG5wb3J0ID0gMTIwMFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuIgp9
```

## Links

`rss`,`api`,`self-hosted`

---

Version:`1.0.0`

RSS-BridgeRSS-Bridge is a PHP project capable of generating Atom feeds for websites that don't have one.

RustDeskRustDesk is a full-featured open source remote control alternative for self-hosting and security with minimal configuration.

### On this page

ConfigurationBase64LinksTags