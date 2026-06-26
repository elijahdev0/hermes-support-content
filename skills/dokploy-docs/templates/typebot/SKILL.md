---
title: "Typebot | Dokploy"
source: "https://docs.dokploy.com/docs/templates/typebot"
category: dokploy-docs
created: "2026-06-25T17:22:00.275Z"
---

Typebot | Dokploy

# Typebot

Copy as Markdown

Typebot is an open-source chatbot builder platform.

## Configuration

docker-compose.ymltemplate.toml

```
version: '3.3'

volumes:
  db-data:

services:
  typebot-db:
    image: postgres:14-alpine
    restart: always
    volumes:
      - db-data:/var/lib/postgresql/data
    environment:
      POSTGRES_USER: typebot
      POSTGRES_DB: typebot
      POSTGRES_PASSWORD: typebot

  typebot-builder:
    image: baptistearno/typebot-builder:2.27
    restart: always
    depends_on:
      - typebot-db
    environment:
      ENCRYPTION_SECRET: '${ENCRYPTION_SECRET}'
      DATABASE_URL: 'postgresql://typebot:typebot@typebot-db:5432/typebot'
      NEXTAUTH_URL: '${NEXTAUTH_URL}'
      NEXT_PUBLIC_VIEWER_URL: '${NEXT_PUBLIC_VIEWER_URL}'
      ADMIN_EMAIL: '${ADMIN_EMAIL}'
      SMTP_HOST: '${SMTP_HOST}'
      NEXT_PUBLIC_SMTP_FROM: '${NEXT_PUBLIC_SMTP_FROM}'
      SMTP_USERNAME: '${SMTP_USERNAME}'
      SMTP_PASSWORD: '${SMTP_PASSWORD}'
      DEFAULT_WORKSPACE_PLAN: '${DEFAULT_WORKSPACE_PLAN}'

  typebot-viewer:
    image: baptistearno/typebot-viewer:2.27.0
    restart: always
    environment:
      ENCRYPTION_SECRET: '${ENCRYPTION_SECRET}'
      DATABASE_URL: postgresql://typebot:typebot@typebot-db:5432/typebot
      NEXTAUTH_URL: '${NEXTAUTH_URL}'
      NEXT_PUBLIC_VIEWER_URL: '${NEXT_PUBLIC_VIEWER_URL}'
      ADMIN_EMAIL: '${ADMIN_EMAIL}'
      SMTP_HOST: '${SMTP_HOST}'
      NEXT_PUBLIC_SMTP_FROM: '${NEXT_PUBLIC_SMTP_FROM}'
      SMTP_USERNAME: '${SMTP_USERNAME}'
      SMTP_PASSWORD: '${SMTP_PASSWORD}'
      DEFAULT_WORKSPACE_PLAN: '${DEFAULT_WORKSPACE_PLAN}'
```

```
[variables]
builder_domain = "${domain}"
viewer_domain = "${domain}"
encryption_secret = "${base64:24}"

[config]
mounts = []

[[config.domains]]
serviceName = "typebot-builder"
port = 3_000
host = "${builder_domain}"

[[config.domains]]
serviceName = "typebot-viewer"
port = 3_000
host = "${viewer_domain}"

[config.env]
ENCRYPTION_SECRET = "${encryption_secret}"
NEXTAUTH_URL = "http://${builder_domain}"
NEXT_PUBLIC_VIEWER_URL = "http://${viewer_domain}"
ADMIN_EMAIL = "[email protected]"
SMTP_HOST = "'Fill'"
SMTP_PORT = "25"
SMTP_USERNAME = "'Fill'"
SMTP_PASSWORD = "'Fill'"
NEXT_PUBLIC_SMTP_FROM = "[email protected]"
DEFAULT_WORKSPACE_PLAN = "UNLIMITED"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246ICczLjMnXG5cbnZvbHVtZXM6XG4gIGRiLWRhdGE6XG5cbnNlcnZpY2VzOlxuICB0eXBlYm90LWRiOlxuICAgIGltYWdlOiBwb3N0Z3JlczoxNC1hbHBpbmVcbiAgICByZXN0YXJ0OiBhbHdheXNcbiAgICB2b2x1bWVzOlxuICAgICAgLSBkYi1kYXRhOi92YXIvbGliL3Bvc3RncmVzcWwvZGF0YVxuICAgIGVudmlyb25tZW50OlxuICAgICAgUE9TVEdSRVNfVVNFUjogdHlwZWJvdFxuICAgICAgUE9TVEdSRVNfREI6IHR5cGVib3RcbiAgICAgIFBPU1RHUkVTX1BBU1NXT1JEOiB0eXBlYm90XG5cblxuICB0eXBlYm90LWJ1aWxkZXI6XG4gICAgaW1hZ2U6IGJhcHRpc3RlYXJuby90eXBlYm90LWJ1aWxkZXI6Mi4yN1xuICAgIHJlc3RhcnQ6IGFsd2F5c1xuICAgIGRlcGVuZHNfb246XG4gICAgICAtIHR5cGVib3QtZGJcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIEVOQ1JZUFRJT05fU0VDUkVUOiAnJHtFTkNSWVBUSU9OX1NFQ1JFVH0nXG4gICAgICBEQVRBQkFTRV9VUkw6ICdwb3N0Z3Jlc3FsOi8vdHlwZWJvdDp0eXBlYm90QHR5cGVib3QtZGI6NTQzMi90eXBlYm90J1xuICAgICAgTkVYVEFVVEhfVVJMOiAnJHtORVhUQVVUSF9VUkx9J1xuICAgICAgTkVYVF9QVUJMSUNfVklFV0VSX1VSTDogJyR7TkVYVF9QVUJMSUNfVklFV0VSX1VSTH0nXG4gICAgICBBRE1JTl9FTUFJTDogJyR7QURNSU5fRU1BSUx9J1xuICAgICAgU01UUF9IT1NUOiAnJHtTTVRQX0hPU1R9J1xuICAgICAgTkVYVF9QVUJMSUNfU01UUF9GUk9NOiAnJHtORVhUX1BVQkxJQ19TTVRQX0ZST019J1xuICAgICAgU01UUF9VU0VSTkFNRTogJyR7U01UUF9VU0VSTkFNRX0nXG4gICAgICBTTVRQX1BBU1NXT1JEOiAnJHtTTVRQX1BBU1NXT1JEfSdcbiAgICAgIERFRkFVTFRfV09SS1NQQUNFX1BMQU46ICcke0RFRkFVTFRfV09SS1NQQUNFX1BMQU59J1xuXG4gIHR5cGVib3Qtdmlld2VyOlxuICAgIGltYWdlOiBiYXB0aXN0ZWFybm8vdHlwZWJvdC12aWV3ZXI6Mi4yNy4wXG4gICAgcmVzdGFydDogYWx3YXlzXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBFTkNSWVBUSU9OX1NFQ1JFVDogJyR7RU5DUllQVElPTl9TRUNSRVR9J1xuICAgICAgREFUQUJBU0VfVVJMOiBwb3N0Z3Jlc3FsOi8vdHlwZWJvdDp0eXBlYm90QHR5cGVib3QtZGI6NTQzMi90eXBlYm90XG4gICAgICBORVhUQVVUSF9VUkw6ICcke05FWFRBVVRIX1VSTH0nXG4gICAgICBORVhUX1BVQkxJQ19WSUVXRVJfVVJMOiAnJHtORVhUX1BVQkxJQ19WSUVXRVJfVVJMfSdcbiAgICAgIEFETUlOX0VNQUlMOiAnJHtBRE1JTl9FTUFJTH0nXG4gICAgICBTTVRQX0hPU1Q6ICcke1NNVFBfSE9TVH0nXG4gICAgICBORVhUX1BVQkxJQ19TTVRQX0ZST006ICcke05FWFRfUFVCTElDX1NNVFBfRlJPTX0nXG4gICAgICBTTVRQX1VTRVJOQU1FOiAnJHtTTVRQX1VTRVJOQU1FfSdcbiAgICAgIFNNVFBfUEFTU1dPUkQ6ICcke1NNVFBfUEFTU1dPUkR9J1xuICAgICAgREVGQVVMVF9XT1JLU1BBQ0VfUExBTjogJyR7REVGQVVMVF9XT1JLU1BBQ0VfUExBTn0nIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5idWlsZGVyX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbnZpZXdlcl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5lbmNyeXB0aW9uX3NlY3JldCA9IFwiJHtiYXNlNjQ6MjR9XCJcblxuW2NvbmZpZ11cbm1vdW50cyA9IFtdXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcInR5cGVib3QtYnVpbGRlclwiXG5wb3J0ID0gM18wMDBcbmhvc3QgPSBcIiR7YnVpbGRlcl9kb21haW59XCJcblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwidHlwZWJvdC12aWV3ZXJcIlxucG9ydCA9IDNfMDAwXG5ob3N0ID0gXCIke3ZpZXdlcl9kb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5FTkNSWVBUSU9OX1NFQ1JFVCA9IFwiJHtlbmNyeXB0aW9uX3NlY3JldH1cIlxuTkVYVEFVVEhfVVJMID0gXCJodHRwOi8vJHtidWlsZGVyX2RvbWFpbn1cIlxuTkVYVF9QVUJMSUNfVklFV0VSX1VSTCA9IFwiaHR0cDovLyR7dmlld2VyX2RvbWFpbn1cIlxuQURNSU5fRU1BSUwgPSBcInR5cGVib3RAZXhhbXBsZS5jb21cIlxuU01UUF9IT1NUID0gXCInRmlsbCdcIlxuU01UUF9QT1JUID0gXCIyNVwiXG5TTVRQX1VTRVJOQU1FID0gXCInRmlsbCdcIlxuU01UUF9QQVNTV09SRCA9IFwiJ0ZpbGwnXCJcbk5FWFRfUFVCTElDX1NNVFBfRlJPTSA9IFwidHlwZWJvdEBleGFtcGxlLmNvbVwiXG5ERUZBVUxUX1dPUktTUEFDRV9QTEFOID0gXCJVTkxJTUlURURcIlxuIgp9
```

## Links

`chatbot`,`builder`,`open-source`

---

Version:`2.27.0`

Twenty CRMTwenty is a modern CRM offering a powerful spreadsheet interface and open-source alternative to Salesforce.

TypechoTypecho 是一个轻量级的开源博客程序，基于 PHP 开发，支持多种数据库，简洁而强大。

### On this page

ConfigurationBase64LinksTags