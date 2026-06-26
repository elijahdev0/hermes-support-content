---
title: "Gitea (MySQL) | Dokploy"
source: "https://docs.dokploy.com/docs/templates/gitea-mysql"
category: dokploy-docs
created: "2026-06-25T17:21:48.522Z"
---

Gitea (MySQL) | Dokploy

# Gitea (MySQL)

Copy as Markdown

Gitea bundled with MySQL 8.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  gitea:
    image: docker.gitea.com/gitea:1.24.4
    restart: unless-stopped
    environment:
      - USER_UID=1000
      - USER_GID=1000
      - GITEA__database__DB_TYPE=mysql
      - GITEA__database__HOST=mysql:3306
      - GITEA__database__NAME=gitea
      - GITEA__database__USER=gitea
      - GITEA__database__PASSWD=${GITEA_DB_PASSWORD:-gitea}
    volumes:
      - gitea-data:/data
    expose:
      - "3000"
      - "22"
    depends_on:
      - mysql
    healthcheck:
      test: ["CMD", "wget", "-q", "--spider", "http://localhost:3000/"]
      interval: 15s
      timeout: 5s
      retries: 10

  mysql:
    image: docker.io/library/mysql:8
    restart: unless-stopped
    environment:
      - MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD:-gitea}
      - MYSQL_USER=gitea
      - MYSQL_PASSWORD=${GITEA_DB_PASSWORD:-gitea}
      - MYSQL_DATABASE=gitea
    command: ["--default-authentication-plugin=mysql_native_password"]
    volumes:
      - mysql-data:/var/lib/mysql
    expose:
      - "3306"

volumes:
  gitea-data: {}
  mysql-data: {}
```

```
[variables]
main_domain = "${domain}"
db_password = "${password:24}"
db_root_password = "${password:24}"

[config]
[[config.domains]]
serviceName = "gitea"
port = 3000
host = "${main_domain}"

[config.env]
USER_UID = "1000"
USER_GID = "1000"
GITEA__database__DB_TYPE = "mysql"
GITEA__database__HOST = "mysql:3306"
GITEA__database__NAME = "gitea"
GITEA__database__USER = "gitea"
GITEA__database__PASSWD = "${db_password}"
GITEA_DB_PASSWORD = "${db_password}"
MYSQL_ROOT_PASSWORD = "${db_root_password}"

[[config.mounts]]
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIGdpdGVhOlxuICAgIGltYWdlOiBkb2NrZXIuZ2l0ZWEuY29tL2dpdGVhOjEuMjQuNFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIFVTRVJfVUlEPTEwMDBcbiAgICAgIC0gVVNFUl9HSUQ9MTAwMFxuICAgICAgLSBHSVRFQV9fZGF0YWJhc2VfX0RCX1RZUEU9bXlzcWxcbiAgICAgIC0gR0lURUFfX2RhdGFiYXNlX19IT1NUPW15c3FsOjMzMDZcbiAgICAgIC0gR0lURUFfX2RhdGFiYXNlX19OQU1FPWdpdGVhXG4gICAgICAtIEdJVEVBX19kYXRhYmFzZV9fVVNFUj1naXRlYVxuICAgICAgLSBHSVRFQV9fZGF0YWJhc2VfX1BBU1NXRD0ke0dJVEVBX0RCX1BBU1NXT1JEOi1naXRlYX1cbiAgICB2b2x1bWVzOlxuICAgICAgLSBnaXRlYS1kYXRhOi9kYXRhXG4gICAgZXhwb3NlOlxuICAgICAgLSBcIjMwMDBcIlxuICAgICAgLSBcIjIyXCJcbiAgICBkZXBlbmRzX29uOlxuICAgICAgLSBteXNxbFxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDogW1wiQ01EXCIsIFwid2dldFwiLCBcIi1xXCIsIFwiLS1zcGlkZXJcIiwgXCJodHRwOi8vbG9jYWxob3N0OjMwMDAvXCJdXG4gICAgICBpbnRlcnZhbDogMTVzXG4gICAgICB0aW1lb3V0OiA1c1xuICAgICAgcmV0cmllczogMTBcblxuICBteXNxbDpcbiAgICBpbWFnZTogZG9ja2VyLmlvL2xpYnJhcnkvbXlzcWw6OFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIE1ZU1FMX1JPT1RfUEFTU1dPUkQ9JHtNWVNRTF9ST09UX1BBU1NXT1JEOi1naXRlYX1cbiAgICAgIC0gTVlTUUxfVVNFUj1naXRlYVxuICAgICAgLSBNWVNRTF9QQVNTV09SRD0ke0dJVEVBX0RCX1BBU1NXT1JEOi1naXRlYX1cbiAgICAgIC0gTVlTUUxfREFUQUJBU0U9Z2l0ZWFcbiAgICBjb21tYW5kOiBbXCItLWRlZmF1bHQtYXV0aGVudGljYXRpb24tcGx1Z2luPW15c3FsX25hdGl2ZV9wYXNzd29yZFwiXVxuICAgIHZvbHVtZXM6XG4gICAgICAtIG15c3FsLWRhdGE6L3Zhci9saWIvbXlzcWxcbiAgICBleHBvc2U6XG4gICAgICAtIFwiMzMwNlwiXG5cbnZvbHVtZXM6XG4gIGdpdGVhLWRhdGE6IHt9XG4gIG15c3FsLWRhdGE6IHt9XG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuZGJfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MjR9XCJcbmRiX3Jvb3RfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MjR9XCJcblxuW2NvbmZpZ11cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImdpdGVhXCJcbnBvcnQgPSAzMDAwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuVVNFUl9VSUQgPSBcIjEwMDBcIlxuVVNFUl9HSUQgPSBcIjEwMDBcIlxuR0lURUFfX2RhdGFiYXNlX19EQl9UWVBFID0gXCJteXNxbFwiXG5HSVRFQV9fZGF0YWJhc2VfX0hPU1QgPSBcIm15c3FsOjMzMDZcIlxuR0lURUFfX2RhdGFiYXNlX19OQU1FID0gXCJnaXRlYVwiXG5HSVRFQV9fZGF0YWJhc2VfX1VTRVIgPSBcImdpdGVhXCJcbkdJVEVBX19kYXRhYmFzZV9fUEFTU1dEID0gXCIke2RiX3Bhc3N3b3JkfVwiXG5HSVRFQV9EQl9QQVNTV09SRCA9IFwiJHtkYl9wYXNzd29yZH1cIlxuTVlTUUxfUk9PVF9QQVNTV09SRCA9IFwiJHtkYl9yb290X3Bhc3N3b3JkfVwiXG5cbltbY29uZmlnLm1vdW50c11dIgp9
```

## Links

`git`,`scm`,`mysql`,`developer-tools`,`self-hosted`

---

Version:`1.24.4`

Gitea MirrorGitea Mirror is a modern web app for automatically mirroring repositories from GitHub to your self-hosted Gitea instance. It features a user-friendly interface to sync public, private, or starred GitHub repos, mirror entire organizations with structure preservation, and optionally mirror issues and labels. The application includes smart filtering, detailed logs, and scheduled automatic mirroring.

Gitea (PostgreSQL)Gitea bundled with PostgreSQL.

### On this page

ConfigurationBase64LinksTags