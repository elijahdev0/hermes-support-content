---
title: "CodeX Docs | Dokploy"
source: "https://docs.dokploy.com/docs/templates/codex-docs"
category: dokploy-docs
created: "2026-06-25T17:21:43.965Z"
---

CodeX Docs | Dokploy

# CodeX Docs

Copy as Markdown

CodeX is a comprehensive platform that brings together passionate engineers, designers, and specialists to create high-quality open-source projects. It includes Editor.js, Hawk.so, CodeX Notes, and more.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3"

services:
  codex:
    image: ghcr.io/codex-team/codex.docs:v2.2
    ports:
      - "3000"
    environment:
      - APP_CONFIG_database_driver=mongodb
      - APP_CONFIG_database_mongodb_uri=mongodb://mongo:${MONGO_PASSWORD}@mongo:27017
      - APP_CONFIG_auth_password=${AUTH_PASSWORD}
      - APP_CONFIG_auth_secret=${AUTH_SECRET}
    volumes:
      - uploads:/usr/src/app/uploads
      - db:/usr/src/app/db
      - ../files/docs-config.yaml:/usr/src/app/docs-config.yaml
    depends_on:
      - mongo

  mongo:
    image: mongo:4
    environment:
      - MONGO_INITDB_ROOT_PASSWORD=${MONGO_PASSWORD}
      - MONGO_INITDB_ROOT_USERNAME=${MONGO_USERNAME}
    volumes:
      - mongo-data:/data/db

volumes:
  uploads:
  db:
  mongo-data:
```

```
[variables]
MONGO_PASSWORD = "${password:16}"
AUTH_PASSWORD = "${password:16}"
AUTH_SECRET = "${password:32}"

[config]
[[config.domains]]
serviceName = "codex"
port = 3000
host = "${domain}"

[config.env]
MONGO_PASSWORD = "${MONGO_PASSWORD}"
AUTH_PASSWORD = "${AUTH_PASSWORD}"
AUTH_SECRET = "${AUTH_SECRET}"
MONGO_USERNAME = "mongo"

[[config.mounts]]
filePath = "/docs-config.yaml"
content = """
# Custom Config, view Here https://github.com/codex-team/codex.docs/blob/main/docs-config.yaml
# Can Also Be configured with ENV, see here https://docs.codex.so/configuration#override-properties-with-environment-variables
"""
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiM1wiXG5cbnNlcnZpY2VzOlxuICBjb2RleDpcbiAgICBpbWFnZTogZ2hjci5pby9jb2RleC10ZWFtL2NvZGV4LmRvY3M6djIuMlxuICAgIHBvcnRzOlxuICAgICAgLSBcIjMwMDBcIlxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBBUFBfQ09ORklHX2RhdGFiYXNlX2RyaXZlcj1tb25nb2RiXG4gICAgICAtIEFQUF9DT05GSUdfZGF0YWJhc2VfbW9uZ29kYl91cmk9bW9uZ29kYjovL21vbmdvOiR7TU9OR09fUEFTU1dPUkR9QG1vbmdvOjI3MDE3XG4gICAgICAtIEFQUF9DT05GSUdfYXV0aF9wYXNzd29yZD0ke0FVVEhfUEFTU1dPUkR9XG4gICAgICAtIEFQUF9DT05GSUdfYXV0aF9zZWNyZXQ9JHtBVVRIX1NFQ1JFVH1cbiAgICB2b2x1bWVzOlxuICAgICAgLSB1cGxvYWRzOi91c3Ivc3JjL2FwcC91cGxvYWRzXG4gICAgICAtIGRiOi91c3Ivc3JjL2FwcC9kYlxuICAgICAgLSAuLi9maWxlcy9kb2NzLWNvbmZpZy55YW1sOi91c3Ivc3JjL2FwcC9kb2NzLWNvbmZpZy55YW1sXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIC0gbW9uZ29cblxuICBtb25nbzpcbiAgICBpbWFnZTogbW9uZ286NFxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBNT05HT19JTklUREJfUk9PVF9QQVNTV09SRD0ke01PTkdPX1BBU1NXT1JEfVxuICAgICAgLSBNT05HT19JTklUREJfUk9PVF9VU0VSTkFNRT0ke01PTkdPX1VTRVJOQU1FfVxuICAgIHZvbHVtZXM6XG4gICAgICAtIG1vbmdvLWRhdGE6L2RhdGEvZGJcblxudm9sdW1lczpcbiAgdXBsb2FkczpcbiAgZGI6XG4gIG1vbmdvLWRhdGE6ICIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxuTU9OR09fUEFTU1dPUkQgPSBcIiR7cGFzc3dvcmQ6MTZ9XCJcbkFVVEhfUEFTU1dPUkQgPSBcIiR7cGFzc3dvcmQ6MTZ9XCJcbkFVVEhfU0VDUkVUID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJjb2RleFwiXG5wb3J0ID0gMzAwMFxuaG9zdCA9IFwiJHtkb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5NT05HT19QQVNTV09SRCA9IFwiJHtNT05HT19QQVNTV09SRH1cIlxuQVVUSF9QQVNTV09SRCA9IFwiJHtBVVRIX1BBU1NXT1JEfVwiXG5BVVRIX1NFQ1JFVCA9IFwiJHtBVVRIX1NFQ1JFVH1cIiBcbk1PTkdPX1VTRVJOQU1FID0gXCJtb25nb1wiXG5cbltbY29uZmlnLm1vdW50c11dXG5maWxlUGF0aCA9IFwiL2RvY3MtY29uZmlnLnlhbWxcIlxuY29udGVudCA9IFwiXCJcIlxuIyBDdXN0b20gQ29uZmlnLCB2aWV3IEhlcmUgaHR0cHM6Ly9naXRodWIuY29tL2NvZGV4LXRlYW0vY29kZXguZG9jcy9ibG9iL21haW4vZG9jcy1jb25maWcueWFtbFxuIyBDYW4gQWxzbyBCZSBjb25maWd1cmVkIHdpdGggRU5WLCBzZWUgaGVyZSBodHRwczovL2RvY3MuY29kZXguc28vY29uZmlndXJhdGlvbiNvdmVycmlkZS1wcm9wZXJ0aWVzLXdpdGgtZW52aXJvbm1lbnQtdmFyaWFibGVzXG5cIlwiXCIiCn0=
```

## Links

`documentation`,`development`,`collaboration`

---

Version:`v2.2`

CoderCoder is an open-source cloud development environment (CDE) that you host in your cloud or on-premises.

Colanode ServerOpen-source and local-first Slack and Notion alternative that puts you in control of your data

### On this page

ConfigurationBase64LinksTags