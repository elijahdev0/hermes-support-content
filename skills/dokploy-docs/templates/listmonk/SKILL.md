---
title: "Listmonk | Dokploy"
source: "https://docs.dokploy.com/docs/templates/listmonk"
category: dokploy-docs
created: "2026-06-25T17:21:52.046Z"
---

Listmonk | Dokploy

# Listmonk

Copy as Markdown

High performance, self-hosted, newsletter and mailing list manager with a modern dashboard.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  db:
    image: postgres:17-alpine
    ports:
      - 5432
    environment:
      - POSTGRES_USER=listmonk
      - POSTGRES_PASSWORD=listmonk
      - POSTGRES_DB=listmonk
    restart: unless-stopped
    healthcheck:
      test: [ "CMD-SHELL", "pg_isready -U listmonk" ]
      interval: 10s
      timeout: 5s
      retries: 6
    volumes:
      - listmonk-data:/var/lib/postgresql/data

  app:
    restart: unless-stopped
    image: listmonk/listmonk:v5.0.0
    environment:
      - LISTMONK_app__address=0.0.0.0:9000
      - LISTMONK_db__user=listmonk
      - LISTMONK_db__password=listmonk
      - LISTMONK_db__database=listmonk
      - LISTMONK_db__host=db
      - LISTMONK_db__port=5432
      - LISTMONK_db__ssl_mode=disable
      - LISTMONK_db__max_open=25
      - LISTMONK_db__max_idle=25
      - LISTMONK_db__max_lifetime=300s
      - TZ=Etc/UTC
    depends_on:
      - db
    command: [ sh, -c, "./listmonk --install --idempotent --yes --config '' && ./listmonk --upgrade --yes --config '' && ./listmonk --config ''" ]
      # --config (file) param is set to empty so that listmonk only uses the env vars (below) for config.
      # --install --idempotent ensures that DB installation happens only once on an empty DB, on the first ever start.
      # --upgrade automatically runs any DB migrations when a new image is pulled.
    volumes:
      - ../files/config.toml:/listmonk/config.toml
      - listmonk-uploads:/listmonk/uploads

volumes:
  listmonk-uploads:
  listmonk-data:
    driver: local
```

```
[variables]
main_domain = "${domain}"

[config]
[[config.domains]]
serviceName = "app"
port = 9_000
host = "${main_domain}"

[[config.mounts]]
filePath = "config.toml"
content = """
[app]
address = "0.0.0.0:9000"

[db]
host = "db"
port = 5432
user = "listmonk"
password = "listmonk"
database = "listmonk"

ssl_mode = "disable"
max_open = 25
max_idle = 25
max_lifetime = "300s"

params = ""
"""
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBkYjpcbiAgICBpbWFnZTogcG9zdGdyZXM6MTctYWxwaW5lXG4gICAgcG9ydHM6XG4gICAgICAtIDU0MzJcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gUE9TVEdSRVNfVVNFUj1saXN0bW9ua1xuICAgICAgLSBQT1NUR1JFU19QQVNTV09SRD1saXN0bW9ua1xuICAgICAgLSBQT1NUR1JFU19EQj1saXN0bW9ua1xuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OiBbIFwiQ01ELVNIRUxMXCIsIFwicGdfaXNyZWFkeSAtVSBsaXN0bW9ua1wiIF1cbiAgICAgIGludGVydmFsOiAxMHNcbiAgICAgIHRpbWVvdXQ6IDVzXG4gICAgICByZXRyaWVzOiA2XG4gICAgdm9sdW1lczpcbiAgICAgIC0gbGlzdG1vbmstZGF0YTovdmFyL2xpYi9wb3N0Z3Jlc3FsL2RhdGFcblxuICBhcHA6XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBpbWFnZTogbGlzdG1vbmsvbGlzdG1vbms6djUuMC4wXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIExJU1RNT05LX2FwcF9fYWRkcmVzcz0wLjAuMC4wOjkwMDBcbiAgICAgIC0gTElTVE1PTktfZGJfX3VzZXI9bGlzdG1vbmtcbiAgICAgIC0gTElTVE1PTktfZGJfX3Bhc3N3b3JkPWxpc3Rtb25rXG4gICAgICAtIExJU1RNT05LX2RiX19kYXRhYmFzZT1saXN0bW9ua1xuICAgICAgLSBMSVNUTU9OS19kYl9faG9zdD1kYlxuICAgICAgLSBMSVNUTU9OS19kYl9fcG9ydD01NDMyXG4gICAgICAtIExJU1RNT05LX2RiX19zc2xfbW9kZT1kaXNhYmxlXG4gICAgICAtIExJU1RNT05LX2RiX19tYXhfb3Blbj0yNVxuICAgICAgLSBMSVNUTU9OS19kYl9fbWF4X2lkbGU9MjVcbiAgICAgIC0gTElTVE1PTktfZGJfX21heF9saWZldGltZT0zMDBzXG4gICAgICAtIFRaPUV0Yy9VVENcbiAgICBkZXBlbmRzX29uOlxuICAgICAgLSBkYlxuICAgIGNvbW1hbmQ6IFsgc2gsIC1jLCBcIi4vbGlzdG1vbmsgLS1pbnN0YWxsIC0taWRlbXBvdGVudCAtLXllcyAtLWNvbmZpZyAnJyAmJiAuL2xpc3Rtb25rIC0tdXBncmFkZSAtLXllcyAtLWNvbmZpZyAnJyAmJiAuL2xpc3Rtb25rIC0tY29uZmlnICcnXCIgXVxuICAgICAgIyAtLWNvbmZpZyAoZmlsZSkgcGFyYW0gaXMgc2V0IHRvIGVtcHR5IHNvIHRoYXQgbGlzdG1vbmsgb25seSB1c2VzIHRoZSBlbnYgdmFycyAoYmVsb3cpIGZvciBjb25maWcuXG4gICAgICAjIC0taW5zdGFsbCAtLWlkZW1wb3RlbnQgZW5zdXJlcyB0aGF0IERCIGluc3RhbGxhdGlvbiBoYXBwZW5zIG9ubHkgb25jZSBvbiBhbiBlbXB0eSBEQiwgb24gdGhlIGZpcnN0IGV2ZXIgc3RhcnQuXG4gICAgICAjIC0tdXBncmFkZSBhdXRvbWF0aWNhbGx5IHJ1bnMgYW55IERCIG1pZ3JhdGlvbnMgd2hlbiBhIG5ldyBpbWFnZSBpcyBwdWxsZWQuXG4gICAgdm9sdW1lczpcbiAgICAgIC0gLi4vZmlsZXMvY29uZmlnLnRvbWw6L2xpc3Rtb25rL2NvbmZpZy50b21sXG4gICAgICAtIGxpc3Rtb25rLXVwbG9hZHM6L2xpc3Rtb25rL3VwbG9hZHNcblxudm9sdW1lczpcbiAgbGlzdG1vbmstdXBsb2FkczpcbiAgbGlzdG1vbmstZGF0YTpcbiAgICBkcml2ZXI6IGxvY2FsXG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuXG5bY29uZmlnXVxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiYXBwXCJcbnBvcnQgPSA5XzAwMFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bW2NvbmZpZy5tb3VudHNdXVxuZmlsZVBhdGggPSBcImNvbmZpZy50b21sXCJcbmNvbnRlbnQgPSBcIlwiXCJcblthcHBdXG5hZGRyZXNzID0gXCIwLjAuMC4wOjkwMDBcIlxuXG5bZGJdXG5ob3N0ID0gXCJkYlwiXG5wb3J0ID0gNTQzMlxudXNlciA9IFwibGlzdG1vbmtcIlxucGFzc3dvcmQgPSBcImxpc3Rtb25rXCJcbmRhdGFiYXNlID0gXCJsaXN0bW9ua1wiXG5cbnNzbF9tb2RlID0gXCJkaXNhYmxlXCJcbm1heF9vcGVuID0gMjVcbm1heF9pZGxlID0gMjVcbm1heF9saWZldGltZSA9IFwiMzAwc1wiXG5cbnBhcmFtcyA9IFwiXCJcblwiXCJcIlxuIgp9
```

## Links

`email`,`newsletter`,`mailing-list`

---

Version:`v3.0.0`

LinkwardenSelf-hosted, open-source collaborative bookmark manager to collect, organize and archive webpages.

LiteLLMLiteLLM is a lightweight OpenAI API-compatible proxy for managing multiple LLM providers with a single endpoint.

### On this page

ConfigurationBase64LinksTags