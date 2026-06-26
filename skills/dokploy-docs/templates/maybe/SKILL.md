---
title: "Maybe | Dokploy"
source: "https://docs.dokploy.com/docs/templates/maybe"
category: dokploy-docs
created: "2026-06-25T17:21:53.154Z"
---

Maybe | Dokploy

# Maybe

Copy as Markdown

Maybe is a self-hosted finance tracking application designed to simplify budgeting and expenses.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  app:
    image: ghcr.io/maybe-finance/maybe:sha-68c570eed8810fd59b5b33cca51bbad5eabb4cb4
    restart: unless-stopped
    volumes:
      - ../files/uploads:/app/uploads
    environment:
      DATABASE_URL: postgresql://maybe:maybe@db:5432/maybe
      SECRET_KEY_BASE: ${SECRET_KEY_BASE}
      SELF_HOSTED: true
      SYNTH_API_KEY: ${SYNTH_API_KEY}
      RAILS_FORCE_SSL: "false"
      RAILS_ASSUME_SSL: "false"
      GOOD_JOB_EXECUTION_MODE: async
    depends_on:
      db:
        condition: service_healthy

  db:
    image: postgres:16
    restart: always
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U $${POSTGRES_USER} -d $${POSTGRES_DB}"]
      interval: 5s
      timeout: 5s
      retries: 5

    volumes:
      - db-data:/var/lib/postgresql/data
    environment:
      POSTGRES_DB: maybe
      POSTGRES_USER: maybe
      POSTGRES_PASSWORD: maybe

volumes:
  db-data:
```

```
[variables]
main_domain = "${domain}"
secret_key_base = "${base64:64}"
synth_api_key = "${base64:32}"

[[config.domains]]
serviceName = "app"
port = 3_000
host = "${main_domain}"

[config.env]
SECRET_KEY_BASE = "${secret_key_base}"
SELF_HOSTED = "true"
SYNTH_API_KEY = "${synth_api_key}"
RAILS_FORCE_SSL = "false"
RAILS_ASSUME_SSL = "false"
GOOD_JOB_EXECUTION_MODE = "async"

[[config.mounts]]
filePath = "./uploads"
content = "This is where user uploads will be stored"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBhcHA6XG4gICAgaW1hZ2U6IGdoY3IuaW8vbWF5YmUtZmluYW5jZS9tYXliZTpzaGEtNjhjNTcwZWVkODgxMGZkNTliNWIzM2NjYTUxYmJhZDVlYWJiNGNiNFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgdm9sdW1lczpcbiAgICAgIC0gLi4vZmlsZXMvdXBsb2FkczovYXBwL3VwbG9hZHNcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIERBVEFCQVNFX1VSTDogcG9zdGdyZXNxbDovL21heWJlOm1heWJlQGRiOjU0MzIvbWF5YmVcbiAgICAgIFNFQ1JFVF9LRVlfQkFTRTogJHtTRUNSRVRfS0VZX0JBU0V9XG4gICAgICBTRUxGX0hPU1RFRDogdHJ1ZVxuICAgICAgU1lOVEhfQVBJX0tFWTogJHtTWU5USF9BUElfS0VZfVxuICAgICAgUkFJTFNfRk9SQ0VfU1NMOiBcImZhbHNlXCJcbiAgICAgIFJBSUxTX0FTU1VNRV9TU0w6IFwiZmFsc2VcIlxuICAgICAgR09PRF9KT0JfRVhFQ1VUSU9OX01PREU6IGFzeW5jXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIGRiOlxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2VfaGVhbHRoeVxuXG4gIGRiOlxuICAgIGltYWdlOiBwb3N0Z3JlczoxNlxuICAgIHJlc3RhcnQ6IGFsd2F5c1xuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDogW1wiQ01ELVNIRUxMXCIsIFwicGdfaXNyZWFkeSAtVSAkJHtQT1NUR1JFU19VU0VSfSAtZCAkJHtQT1NUR1JFU19EQn1cIl1cbiAgICAgIGludGVydmFsOiA1c1xuICAgICAgdGltZW91dDogNXNcbiAgICAgIHJldHJpZXM6IDVcblxuICAgIHZvbHVtZXM6XG4gICAgICAtIGRiLWRhdGE6L3Zhci9saWIvcG9zdGdyZXNxbC9kYXRhXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBQT1NUR1JFU19EQjogbWF5YmVcbiAgICAgIFBPU1RHUkVTX1VTRVI6IG1heWJlXG4gICAgICBQT1NUR1JFU19QQVNTV09SRDogbWF5YmVcblxudm9sdW1lczpcbiAgZGItZGF0YTpcbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5zZWNyZXRfa2V5X2Jhc2UgPSBcIiR7YmFzZTY0OjY0fVwiXG5zeW50aF9hcGlfa2V5ID0gXCIke2Jhc2U2NDozMn1cIlxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJhcHBcIlxucG9ydCA9IDNfMDAwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuU0VDUkVUX0tFWV9CQVNFID0gXCIke3NlY3JldF9rZXlfYmFzZX1cIlxuU0VMRl9IT1NURUQgPSBcInRydWVcIlxuU1lOVEhfQVBJX0tFWSA9IFwiJHtzeW50aF9hcGlfa2V5fVwiXG5SQUlMU19GT1JDRV9TU0wgPSBcImZhbHNlXCJcblJBSUxTX0FTU1VNRV9TU0wgPSBcImZhbHNlXCJcbkdPT0RfSk9CX0VYRUNVVElPTl9NT0RFID0gXCJhc3luY1wiXG5cbltbY29uZmlnLm1vdW50c11dXG5maWxlUGF0aCA9IFwiLi91cGxvYWRzXCJcbmNvbnRlbnQgPSBcIlRoaXMgaXMgd2hlcmUgdXNlciB1cGxvYWRzIHdpbGwgYmUgc3RvcmVkXCJcbiIKfQ==
```

## Links

`finance`,`self-hosted`

---

Version:`latest`

MauticMautic is the world's largest open-source marketing automation project. It allows you to automate the process of finding and nurturing contacts through landing pages and forms, sending email, text messages, web notifications, and tracking your contacts.

MAZANOKEMAZANOKE is a modern, self-hosted image hosting and sharing platform. Upload, organize, and share your images with a clean and intuitive interface.

### On this page

ConfigurationBase64LinksTags