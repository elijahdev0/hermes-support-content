---
title: "Bugsink | Dokploy"
source: "https://docs.dokploy.com/docs/templates/bugsink"
category: dokploy-docs
created: "2026-06-25T17:21:42.677Z"
---

Bugsink | Dokploy

# Bugsink

Copy as Markdown

Bugsink is a self-hosted Error Tracker. Built to self-host; Sentry-SDK compatible; Scalable and reliable

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  db:
    image: postgres:17-alpine
    restart: unless-stopped
    environment:
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: ${POSTGRES_DB}
    volumes:
      - db-data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -h db"]
      retries: 5
      start_period: 10s
      interval: 5s
      timeout: 5s

  web:
    image: bugsink/bugsink:latest
    depends_on:
      db:
        condition: service_healthy
    restart: unless-stopped
    expose:
      - 8000
    environment:
      SECRET_KEY: ${SECRET_KEY}
      CREATE_SUPERUSER: ${CREATE_SUPERUSER}
      PORT: 8000
      DATABASE_URL: postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@db:5432/${POSTGRES_DB}
      BEHIND_HTTPS_PROXY: ${BEHIND_HTTPS_PROXY}
      BASE_URL: ${BASE_URL}
    healthcheck:
      test:
        [
          "CMD-SHELL",
          'python -c ''import requests; requests.get("http://localhost:8000/").raise_for_status()''',
        ]
      interval: 5s
      timeout: 20s
      retries: 10

volumes:
  db-data:
```

```
[variables]
main_domain = "${domain}"
postgres_user = "bugsinkuser"
postgres_password = "${password:32}"
postgres_db = "bugsink"
secret_key = "${password:64}"
superuser = "admin:admin"
behind_https_proxy = "false"

[config]

[[config.domains]]
serviceName = "web"
port = 8000
host = "${main_domain}"

[config.env]
POSTGRES_USER = "${postgres_user}"
POSTGRES_PASSWORD = "${postgres_password}"
POSTGRES_DB = "${postgres_db}"
SECRET_KEY = "${secret_key}"
CREATE_SUPERUSER = "${superuser}"
BEHIND_HTTPS_PROXY = "${behind_https_proxy}"
BASE_URL = "https://${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIGRiOlxuICAgIGltYWdlOiBwb3N0Z3JlczoxNy1hbHBpbmVcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGVudmlyb25tZW50OlxuICAgICAgUE9TVEdSRVNfVVNFUjogJHtQT1NUR1JFU19VU0VSfVxuICAgICAgUE9TVEdSRVNfUEFTU1dPUkQ6ICR7UE9TVEdSRVNfUEFTU1dPUkR9XG4gICAgICBQT1NUR1JFU19EQjogJHtQT1NUR1JFU19EQn1cbiAgICB2b2x1bWVzOlxuICAgICAgLSBkYi1kYXRhOi92YXIvbGliL3Bvc3RncmVzcWwvZGF0YVxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDogW1wiQ01ELVNIRUxMXCIsIFwicGdfaXNyZWFkeSAtaCBkYlwiXVxuICAgICAgcmV0cmllczogNVxuICAgICAgc3RhcnRfcGVyaW9kOiAxMHNcbiAgICAgIGludGVydmFsOiA1c1xuICAgICAgdGltZW91dDogNXNcblxuICB3ZWI6XG4gICAgaW1hZ2U6IGJ1Z3NpbmsvYnVnc2luazpsYXRlc3RcbiAgICBkZXBlbmRzX29uOlxuICAgICAgZGI6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9oZWFsdGh5XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBleHBvc2U6XG4gICAgICAtIDgwMDBcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIFNFQ1JFVF9LRVk6ICR7U0VDUkVUX0tFWX1cbiAgICAgIENSRUFURV9TVVBFUlVTRVI6ICR7Q1JFQVRFX1NVUEVSVVNFUn1cbiAgICAgIFBPUlQ6IDgwMDBcbiAgICAgIERBVEFCQVNFX1VSTDogcG9zdGdyZXNxbDovLyR7UE9TVEdSRVNfVVNFUn06JHtQT1NUR1JFU19QQVNTV09SRH1AZGI6NTQzMi8ke1BPU1RHUkVTX0RCfVxuICAgICAgQkVISU5EX0hUVFBTX1BST1hZOiAke0JFSElORF9IVFRQU19QUk9YWX1cbiAgICAgIEJBU0VfVVJMOiAke0JBU0VfVVJMfVxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDpcbiAgICAgICAgW1xuICAgICAgICAgIFwiQ01ELVNIRUxMXCIsXG4gICAgICAgICAgJ3B5dGhvbiAtYyAnJ2ltcG9ydCByZXF1ZXN0czsgcmVxdWVzdHMuZ2V0KFwiaHR0cDovL2xvY2FsaG9zdDo4MDAwL1wiKS5yYWlzZV9mb3Jfc3RhdHVzKCknJycsXG4gICAgICAgIF1cbiAgICAgIGludGVydmFsOiA1c1xuICAgICAgdGltZW91dDogMjBzXG4gICAgICByZXRyaWVzOiAxMFxuXG52b2x1bWVzOlxuICBkYi1kYXRhOlxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbnBvc3RncmVzX3VzZXIgPSBcImJ1Z3Npbmt1c2VyXCJcbnBvc3RncmVzX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5wb3N0Z3Jlc19kYiA9IFwiYnVnc2lua1wiXG5zZWNyZXRfa2V5ID0gXCIke3Bhc3N3b3JkOjY0fVwiXG5zdXBlcnVzZXIgPSBcImFkbWluOmFkbWluXCJcbmJlaGluZF9odHRwc19wcm94eSA9IFwiZmFsc2VcIlxuXG5bY29uZmlnXVxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJ3ZWJcIlxucG9ydCA9IDgwMDBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5QT1NUR1JFU19VU0VSID0gXCIke3Bvc3RncmVzX3VzZXJ9XCJcblBPU1RHUkVTX1BBU1NXT1JEID0gXCIke3Bvc3RncmVzX3Bhc3N3b3JkfVwiXG5QT1NUR1JFU19EQiA9IFwiJHtwb3N0Z3Jlc19kYn1cIlxuU0VDUkVUX0tFWSA9IFwiJHtzZWNyZXRfa2V5fVwiXG5DUkVBVEVfU1VQRVJVU0VSID0gXCIke3N1cGVydXNlcn1cIlxuQkVISU5EX0hUVFBTX1BST1hZID0gXCIke2JlaGluZF9odHRwc19wcm94eX1cIlxuQkFTRV9VUkwgPSBcImh0dHBzOi8vJHttYWluX2RvbWFpbn1cIlxuIgp9
```

## Links

`hosting`,`self-hosted`,`development`

---

Version:`latest`

BudibaseBudibase is an open-source low-code platform that saves engineers 100s of hours building forms, portals, and approval apps, securely.

BytebaseBytebase is a database management tool that allows you to manage your databases with ease. It provides a simple and effective solution for managing your databases from anywhere.

### On this page

ConfigurationBase64LinksTags