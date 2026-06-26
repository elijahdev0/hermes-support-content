---
title: "Argilla | Dokploy"
source: "https://docs.dokploy.com/docs/templates/argilla"
category: dokploy-docs
created: "2026-06-25T17:21:41.529Z"
---

Argilla | Dokploy

# Argilla

Copy as Markdown

Argilla is a robust platform designed to help engineers and data scientists streamline the management of machine learning data workflows. It simplifies tasks like data labeling, annotation, and quality control.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  argilla-web:
    image: argilla/argilla-server:latest
    restart: unless-stopped
    ports:
      - 6900
    environment:
      - ARGILLA_HOME_PATH=/var/lib/argilla
      - ARGILLA_ELASTICSEARCH=http://argilla-elasticsearch:9200
      - ARGILLA_DATABASE_URL=postgresql+asyncpg://postgres:${DB_PASSWORD}@argilla-db:5432/argilla
      - ARGILLA_REDIS_URL=redis://:${REDIS_PASSWORD}@argilla-redis:6379/0
      - USERNAME=${LOGIN_USERNAME}
      - PASSWORD=${LOGIN_PASSWORD}
      - API_KEY=argilla.apikey
      - WORKSPACE=default
    volumes:
      - argilladata:/var/lib/argilla
    depends_on:
      - argilla-elasticsearch
      - argilla-db
      - argilla-redis

  argilla-worker:
    image: argilla/argilla-server:latest
    restart: unless-stopped
    environment:
      - BACKGROUND_NUM_WORKERS=2
      - ARGILLA_HOME_PATH=/var/lib/argilla
      - ARGILLA_ELASTICSEARCH=http://argilla-elasticsearch:9200
      - ARGILLA_DATABASE_URL=postgresql+asyncpg://postgres:${DB_PASSWORD}@argilla-db:5432/argilla
      - ARGILLA_REDIS_URL=redis://:${REDIS_PASSWORD}@argilla-redis:6379/0
    volumes:
      - argilladata:/var/lib/argilla
    command: python -m argilla_server worker --num-workers ${BACKGROUND_NUM_WORKERS}
    depends_on:
      - argilla-elasticsearch
      - argilla-db
      - argilla-redis

  argilla-elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:8.12.2
    restart: unless-stopped
    environment:
      - node.name=elasticsearch
      - cluster.name=es-argilla-local
      - discovery.type=single-node
      - ES_JAVA_OPTS=-Xms512m -Xmx512m
      - cluster.routing.allocation.disk.threshold_enabled=false
      - xpack.security.enabled=false
    volumes:
      - elasticdata:/usr/share/elasticsearch/data

  argilla-db:
    image: postgres:15-alpine
    restart: unless-stopped
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=${DB_PASSWORD}
      - POSTGRES_DB=argilla
    volumes:
      - dbdata:/var/lib/postgresql/data

  argilla-redis:
    image: redis:7-alpine
    restart: unless-stopped
    environment:
      - REDIS_PASSWORD=${REDIS_PASSWORD}
    command: redis-server --requirepass ${REDIS_PASSWORD}
    volumes:
      - redisdata:/data

volumes:
  argilladata: {}
  elasticdata: {}
  dbdata: {}
  redisdata: {}
```

```
[variables]
main_domain = "${domain}"
login_username = "${username}"
login_password = "${password:8}"
db_password = "${password:16}"
redis_password = "${password:16}"

[config]
[[config.domains]]
serviceName = "argilla-web"
port = 6900
host = "${main_domain}"

[config.env]
LOGIN_USERNAME = "${login_username}"
LOGIN_PASSWORD = "${login_password}"
DB_PASSWORD = "${db_password}"
REDIS_PASSWORD = "${redis_password}"
BACKGROUND_NUM_WORKERS = "2"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBhcmdpbGxhLXdlYjpcbiAgICBpbWFnZTogYXJnaWxsYS9hcmdpbGxhLXNlcnZlcjpsYXRlc3RcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIHBvcnRzOlxuICAgICAgLSA2OTAwXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIEFSR0lMTEFfSE9NRV9QQVRIPS92YXIvbGliL2FyZ2lsbGFcbiAgICAgIC0gQVJHSUxMQV9FTEFTVElDU0VBUkNIPWh0dHA6Ly9hcmdpbGxhLWVsYXN0aWNzZWFyY2g6OTIwMFxuICAgICAgLSBBUkdJTExBX0RBVEFCQVNFX1VSTD1wb3N0Z3Jlc3FsK2FzeW5jcGc6Ly9wb3N0Z3Jlczoke0RCX1BBU1NXT1JEfUBhcmdpbGxhLWRiOjU0MzIvYXJnaWxsYVxuICAgICAgLSBBUkdJTExBX1JFRElTX1VSTD1yZWRpczovLzoke1JFRElTX1BBU1NXT1JEfUBhcmdpbGxhLXJlZGlzOjYzNzkvMFxuICAgICAgLSBVU0VSTkFNRT0ke0xPR0lOX1VTRVJOQU1FfVxuICAgICAgLSBQQVNTV09SRD0ke0xPR0lOX1BBU1NXT1JEfVxuICAgICAgLSBBUElfS0VZPWFyZ2lsbGEuYXBpa2V5XG4gICAgICAtIFdPUktTUEFDRT1kZWZhdWx0XG4gICAgdm9sdW1lczpcbiAgICAgIC0gYXJnaWxsYWRhdGE6L3Zhci9saWIvYXJnaWxsYVxuICAgIGRlcGVuZHNfb246XG4gICAgICAtIGFyZ2lsbGEtZWxhc3RpY3NlYXJjaFxuICAgICAgLSBhcmdpbGxhLWRiXG4gICAgICAtIGFyZ2lsbGEtcmVkaXNcblxuICBhcmdpbGxhLXdvcmtlcjpcbiAgICBpbWFnZTogYXJnaWxsYS9hcmdpbGxhLXNlcnZlcjpsYXRlc3RcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBCQUNLR1JPVU5EX05VTV9XT1JLRVJTPTJcbiAgICAgIC0gQVJHSUxMQV9IT01FX1BBVEg9L3Zhci9saWIvYXJnaWxsYVxuICAgICAgLSBBUkdJTExBX0VMQVNUSUNTRUFSQ0g9aHR0cDovL2FyZ2lsbGEtZWxhc3RpY3NlYXJjaDo5MjAwXG4gICAgICAtIEFSR0lMTEFfREFUQUJBU0VfVVJMPXBvc3RncmVzcWwrYXN5bmNwZzovL3Bvc3RncmVzOiR7REJfUEFTU1dPUkR9QGFyZ2lsbGEtZGI6NTQzMi9hcmdpbGxhXG4gICAgICAtIEFSR0lMTEFfUkVESVNfVVJMPXJlZGlzOi8vOiR7UkVESVNfUEFTU1dPUkR9QGFyZ2lsbGEtcmVkaXM6NjM3OS8wXG4gICAgdm9sdW1lczpcbiAgICAgIC0gYXJnaWxsYWRhdGE6L3Zhci9saWIvYXJnaWxsYVxuICAgIGNvbW1hbmQ6IHB5dGhvbiAtbSBhcmdpbGxhX3NlcnZlciB3b3JrZXIgLS1udW0td29ya2VycyAke0JBQ0tHUk9VTkRfTlVNX1dPUktFUlN9XG4gICAgZGVwZW5kc19vbjpcbiAgICAgIC0gYXJnaWxsYS1lbGFzdGljc2VhcmNoXG4gICAgICAtIGFyZ2lsbGEtZGJcbiAgICAgIC0gYXJnaWxsYS1yZWRpc1xuXG4gIGFyZ2lsbGEtZWxhc3RpY3NlYXJjaDpcbiAgICBpbWFnZTogZG9ja2VyLmVsYXN0aWMuY28vZWxhc3RpY3NlYXJjaC9lbGFzdGljc2VhcmNoOjguMTIuMlxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIG5vZGUubmFtZT1lbGFzdGljc2VhcmNoXG4gICAgICAtIGNsdXN0ZXIubmFtZT1lcy1hcmdpbGxhLWxvY2FsXG4gICAgICAtIGRpc2NvdmVyeS50eXBlPXNpbmdsZS1ub2RlXG4gICAgICAtIEVTX0pBVkFfT1BUUz0tWG1zNTEybSAtWG14NTEybVxuICAgICAgLSBjbHVzdGVyLnJvdXRpbmcuYWxsb2NhdGlvbi5kaXNrLnRocmVzaG9sZF9lbmFibGVkPWZhbHNlXG4gICAgICAtIHhwYWNrLnNlY3VyaXR5LmVuYWJsZWQ9ZmFsc2VcbiAgICB2b2x1bWVzOlxuICAgICAgLSBlbGFzdGljZGF0YTovdXNyL3NoYXJlL2VsYXN0aWNzZWFyY2gvZGF0YVxuXG4gIGFyZ2lsbGEtZGI6XG4gICAgaW1hZ2U6IHBvc3RncmVzOjE1LWFscGluZVxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIFBPU1RHUkVTX1VTRVI9cG9zdGdyZXNcbiAgICAgIC0gUE9TVEdSRVNfUEFTU1dPUkQ9JHtEQl9QQVNTV09SRH1cbiAgICAgIC0gUE9TVEdSRVNfREI9YXJnaWxsYVxuICAgIHZvbHVtZXM6XG4gICAgICAtIGRiZGF0YTovdmFyL2xpYi9wb3N0Z3Jlc3FsL2RhdGFcblxuICBhcmdpbGxhLXJlZGlzOlxuICAgIGltYWdlOiByZWRpczo3LWFscGluZVxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIFJFRElTX1BBU1NXT1JEPSR7UkVESVNfUEFTU1dPUkR9XG4gICAgY29tbWFuZDogcmVkaXMtc2VydmVyIC0tcmVxdWlyZXBhc3MgJHtSRURJU19QQVNTV09SRH1cbiAgICB2b2x1bWVzOlxuICAgICAgLSByZWRpc2RhdGE6L2RhdGFcblxudm9sdW1lczpcbiAgYXJnaWxsYWRhdGE6IHt9XG4gIGVsYXN0aWNkYXRhOiB7fVxuICBkYmRhdGE6IHt9XG4gIHJlZGlzZGF0YToge30gIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbmxvZ2luX3VzZXJuYW1lID0gXCIke3VzZXJuYW1lfVwiXG5sb2dpbl9wYXNzd29yZCA9IFwiJHtwYXNzd29yZDo4fVwiXG5kYl9wYXNzd29yZCA9IFwiJHtwYXNzd29yZDoxNn1cIlxucmVkaXNfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MTZ9XCJcblxuW2NvbmZpZ11cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImFyZ2lsbGEtd2ViXCJcbnBvcnQgPSA2OTAwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuTE9HSU5fVVNFUk5BTUUgPSBcIiR7bG9naW5fdXNlcm5hbWV9XCJcbkxPR0lOX1BBU1NXT1JEID0gXCIke2xvZ2luX3Bhc3N3b3JkfVwiXG5EQl9QQVNTV09SRCA9IFwiJHtkYl9wYXNzd29yZH1cIlxuUkVESVNfUEFTU1dPUkQgPSBcIiR7cmVkaXNfcGFzc3dvcmR9XCJcbkJBQ0tHUk9VTkRfTlVNX1dPUktFUlMgPSBcIjJcIiAiCn0=
```

## Links

`machine-learning`,`data-labeling`,`ai`

---

Version:`latest`

ArangoDBArangoDB is a native multi-model database with flexible data models for documents, graphs, and key-values. Build high performance applications using a convenient SQL-like query language or JavaScript extensions.

AudiobookshelfAudiobookshelf is a self-hosted server designed to manage and play your audiobooks and podcasts. It works best when you have an organized directory structure.

### On this page

ConfigurationBase64LinksTags