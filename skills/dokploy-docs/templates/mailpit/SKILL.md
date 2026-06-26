---
title: "Mailpit | Dokploy"
source: "https://docs.dokploy.com/docs/templates/mailpit"
category: dokploy-docs
created: "2026-06-25T17:21:52.047Z"
---

Mailpit | Dokploy

# Mailpit

Copy as Markdown

Mailpit is a tiny, self-contained, and secure email & SMTP testing tool with API for developers.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  mailpit:
    image: axllent/mailpit:v1.22.3
    restart: unless-stopped
    ports:
      - '1025:1025'
    volumes:
      - 'mailpit-data:/data'
    environment:
      - MP_SMTP_AUTH_ALLOW_INSECURE=true
      - MP_MAX_MESSAGES=5000
      - MP_DATABASE=/data/mailpit.db
      - MP_UI_AUTH=${MP_UI_AUTH}
      - MP_SMTP_AUTH=${MP_SMTP_AUTH}
    healthcheck:
      test:
        - CMD
        - /mailpit
        - readyz
      interval: 5s
      timeout: 20s
      retries: 10

volumes:
  mailpit-data:
```

```
[variables]
main_domain = "${domain}"
default_password = "${password}"

[config]
mounts = []

[[config.domains]]
serviceName = "mailpit"
port = 8_025
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBtYWlscGl0OlxuICAgIGltYWdlOiBheGxsZW50L21haWxwaXQ6djEuMjIuM1xuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgcG9ydHM6XG4gICAgICAtICcxMDI1OjEwMjUnXG4gICAgdm9sdW1lczpcbiAgICAgIC0gJ21haWxwaXQtZGF0YTovZGF0YSdcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gTVBfU01UUF9BVVRIX0FMTE9XX0lOU0VDVVJFPXRydWVcbiAgICAgIC0gTVBfTUFYX01FU1NBR0VTPTUwMDBcbiAgICAgIC0gTVBfREFUQUJBU0U9L2RhdGEvbWFpbHBpdC5kYlxuICAgICAgLSBNUF9VSV9BVVRIPSR7TVBfVUlfQVVUSH1cbiAgICAgIC0gTVBfU01UUF9BVVRIPSR7TVBfU01UUF9BVVRIfVxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDpcbiAgICAgICAgLSBDTURcbiAgICAgICAgLSAvbWFpbHBpdFxuICAgICAgICAtIHJlYWR5elxuICAgICAgaW50ZXJ2YWw6IDVzXG4gICAgICB0aW1lb3V0OiAyMHNcbiAgICAgIHJldHJpZXM6IDEwXG5cbnZvbHVtZXM6XG4gIG1haWxwaXQtZGF0YToiLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuZGVmYXVsdF9wYXNzd29yZCA9IFwiJHtwYXNzd29yZH1cIlxuXG5bY29uZmlnXVxubW91bnRzID0gW11cblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwibWFpbHBpdFwiXG5wb3J0ID0gOF8wMjVcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcbiIKfQ==
```

## Links

`email`,`smtp`

---

Version:`v1.22.3`

Mage AIBuild, run, and manage data pipelines for integrating and transforming data.

MattermostA single point of collaboration. Designed specifically for digital operations.

### On this page

ConfigurationBase64LinksTags