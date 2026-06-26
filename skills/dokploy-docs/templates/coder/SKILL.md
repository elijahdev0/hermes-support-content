---
title: "Coder | Dokploy"
source: "https://docs.dokploy.com/docs/templates/coder"
category: dokploy-docs
created: "2026-06-25T17:21:43.965Z"
---

Coder | Dokploy

# Coder

Copy as Markdown

Coder is an open-source cloud development environment (CDE) that you host in your cloud or on-premises.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  coder:
    image: ghcr.io/coder/coder:v2.15.3

    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    group_add:
      - "988"
    depends_on:
      db:
        condition: service_healthy
    environment:
      - CODER_ACCESS_URL
      - CODER_HTTP_ADDRESS
      - CODER_PG_CONNECTION_URL=postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@db/${POSTGRES_DB}?sslmode=disable

  db:
    image: postgres:17

    environment:
      - POSTGRES_PASSWORD
      - POSTGRES_USER
      - POSTGRES_DB
    healthcheck:
      test:
        [
          "CMD-SHELL",
          "pg_isready -U ${POSTGRES_USER} -d ${POSTGRES_DB}",
        ]
      interval: 5s
      timeout: 5s
      retries: 5
    volumes:
      - db_coder_data:/var/lib/postgresql/data

volumes:
  db_coder_data:
```

```
[variables]
main_domain = "${domain}"
postgres_password = "${password}"

[config]
env = [
  "CODER_ACCESS_URL=",
  "CODER_HTTP_ADDRESS=0.0.0.0:7080",
  "POSTGRES_DB=coder",
  "POSTGRES_USER=coder",
  "POSTGRES_PASSWORD=${postgres_password}",
]
mounts = []

[[config.domains]]
serviceName = "coder"
port = 7_080
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBjb2RlcjpcbiAgICBpbWFnZTogZ2hjci5pby9jb2Rlci9jb2Rlcjp2Mi4xNS4zXG5cbiAgICB2b2x1bWVzOlxuICAgICAgLSAvdmFyL3J1bi9kb2NrZXIuc29jazovdmFyL3J1bi9kb2NrZXIuc29ja1xuICAgIGdyb3VwX2FkZDpcbiAgICAgIC0gXCI5ODhcIlxuICAgIGRlcGVuZHNfb246XG4gICAgICBkYjpcbiAgICAgICAgY29uZGl0aW9uOiBzZXJ2aWNlX2hlYWx0aHlcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gQ09ERVJfQUNDRVNTX1VSTFxuICAgICAgLSBDT0RFUl9IVFRQX0FERFJFU1NcbiAgICAgIC0gQ09ERVJfUEdfQ09OTkVDVElPTl9VUkw9cG9zdGdyZXNxbDovLyR7UE9TVEdSRVNfVVNFUn06JHtQT1NUR1JFU19QQVNTV09SRH1AZGIvJHtQT1NUR1JFU19EQn0/c3NsbW9kZT1kaXNhYmxlXG5cbiAgZGI6XG4gICAgaW1hZ2U6IHBvc3RncmVzOjE3XG5cbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gUE9TVEdSRVNfUEFTU1dPUkRcbiAgICAgIC0gUE9TVEdSRVNfVVNFUlxuICAgICAgLSBQT1NUR1JFU19EQlxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDpcbiAgICAgICAgW1xuICAgICAgICAgIFwiQ01ELVNIRUxMXCIsXG4gICAgICAgICAgXCJwZ19pc3JlYWR5IC1VICR7UE9TVEdSRVNfVVNFUn0gLWQgJHtQT1NUR1JFU19EQn1cIixcbiAgICAgICAgXVxuICAgICAgaW50ZXJ2YWw6IDVzXG4gICAgICB0aW1lb3V0OiA1c1xuICAgICAgcmV0cmllczogNVxuICAgIHZvbHVtZXM6XG4gICAgICAtIGRiX2NvZGVyX2RhdGE6L3Zhci9saWIvcG9zdGdyZXNxbC9kYXRhXG5cbnZvbHVtZXM6XG4gIGRiX2NvZGVyX2RhdGE6XG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxucG9zdGdyZXNfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmR9XCJcblxuW2NvbmZpZ11cbmVudiA9IFtcbiAgXCJDT0RFUl9BQ0NFU1NfVVJMPVwiLFxuICBcIkNPREVSX0hUVFBfQUREUkVTUz0wLjAuMC4wOjcwODBcIixcbiAgXCJQT1NUR1JFU19EQj1jb2RlclwiLFxuICBcIlBPU1RHUkVTX1VTRVI9Y29kZXJcIixcbiAgXCJQT1NUR1JFU19QQVNTV09SRD0ke3Bvc3RncmVzX3Bhc3N3b3JkfVwiLFxuXVxubW91bnRzID0gW11cblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiY29kZXJcIlxucG9ydCA9IDdfMDgwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG4iCn0=
```

## Links

`self-hosted`,`open-source`,`builder`

---

Version:`2.15.3`

CockpitCockpit is a headless content platform designed to streamline the creation, connection, and delivery of content for creators, marketers, and developers. It is built with an API-first approach, enabling limitless digital solutions.

CodeX DocsCodeX is a comprehensive platform that brings together passionate engineers, designers, and specialists to create high-quality open-source projects. It includes Editor.js, Hawk.so, CodeX Notes, and more.

### On this page

ConfigurationBase64LinksTags