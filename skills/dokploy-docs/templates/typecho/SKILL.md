---
title: "Typecho | Dokploy"
source: "https://docs.dokploy.com/docs/templates/typecho"
category: dokploy-docs
created: "2026-06-25T17:22:00.275Z"
---

Typecho | Dokploy

# Typecho

Copy as Markdown

Typecho 是一个轻量级的开源博客程序，基于 PHP 开发，支持多种数据库，简洁而强大。

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  typecho:
    image: 80x86/typecho:latest
    restart: unless-stopped
    environment:
      PHP_TZ: Asia/Shanghai
      PHP_MAX_EXECUTION_TIME: 600
    volumes:
      - typecho_data:/data
    depends_on:
      - db

  db:
    image: mysql:5.7
    restart: unless-stopped
    environment:
      MYSQL_DATABASE: typecho
      MYSQL_USER: typecho
      MYSQL_PASSWORD: typecho_password
      MYSQL_ROOT_PASSWORD: root_password
    volumes:
      - db_data:/var/lib/mysql

volumes:
  typecho_data:
  db_data:
```

```
[variables]
main_domain = "${domain}"
db_password = "${password:16}"
root_password = "${password:16}"

[config]
env = {}
mounts = []

[[config.domains]]
serviceName = "typecho"
port = 80
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICB0eXBlY2hvOlxuICAgIGltYWdlOiA4MHg4Ni90eXBlY2hvOmxhdGVzdFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBQSFBfVFo6IEFzaWEvU2hhbmdoYWlcbiAgICAgIFBIUF9NQVhfRVhFQ1VUSU9OX1RJTUU6IDYwMFxuICAgIHZvbHVtZXM6XG4gICAgICAtIHR5cGVjaG9fZGF0YTovZGF0YVxuICAgIGRlcGVuZHNfb246XG4gICAgICAtIGRiXG5cbiAgZGI6XG4gICAgaW1hZ2U6IG15c3FsOjUuN1xuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBNWVNRTF9EQVRBQkFTRTogdHlwZWNob1xuICAgICAgTVlTUUxfVVNFUjogdHlwZWNob1xuICAgICAgTVlTUUxfUEFTU1dPUkQ6IHR5cGVjaG9fcGFzc3dvcmRcbiAgICAgIE1ZU1FMX1JPT1RfUEFTU1dPUkQ6IHJvb3RfcGFzc3dvcmRcbiAgICB2b2x1bWVzOlxuICAgICAgLSBkYl9kYXRhOi92YXIvbGliL215c3FsXG5cbnZvbHVtZXM6XG4gIHR5cGVjaG9fZGF0YTpcbiAgZGJfZGF0YToiLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuZGJfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MTZ9XCJcbnJvb3RfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MTZ9XCJcblxuW2NvbmZpZ11cbmVudiA9IHt9XG5tb3VudHMgPSBbXVxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJ0eXBlY2hvXCJcbnBvcnQgPSA4MFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIiIKfQ==
```

## Links

`blog`,`cms`,`php`

---

Version:`stable`

TypebotTypebot is an open-source chatbot builder platform.

TypesenseTypesense is a fast, open-source search engine for building modern search experiences.

### On this page

ConfigurationBase64LinksTags