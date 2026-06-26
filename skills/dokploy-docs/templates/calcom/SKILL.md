---
title: "Calcom | Dokploy"
source: "https://docs.dokploy.com/docs/templates/calcom"
category: dokploy-docs
created: "2026-06-25T17:21:42.678Z"
---

Calcom | Dokploy

# Calcom

Copy as Markdown

Calcom is a open source alternative to Calendly that allows to create scheduling and booking services.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  postgres:
    image: postgres:16-alpine

    volumes:
      - calcom-data:/var/lib/postgresql/data
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=db
      - DATABASE_URL=postgres://postgres:password@postgres:5432/db

  calcom:
    image: calcom/cal.com:v2.7.6
    depends_on:
      - postgres
    environment:
      - NEXTAUTH_SECRET=${NEXTAUTH_SECRET}
      - CALENDSO_ENCRYPTION_KEY=${CALENDSO_ENCRYPTION_KEY}
      - DATABASE_URL=postgres://postgres:password@postgres:5432/db
      - NEXT_PUBLIC_WEBAPP_URL=http://${CALCOM_HOST}
      - NEXTAUTH_URL=http://${CALCOM_HOST}/api/auth

volumes:
  calcom-data:
```

```
[variables]
main_domain = "${domain}"
calcom_encryption_key = "${base64:32}"
nextauth_secret = "${base64:32}"

[config]
env = [
  "CALCOM_HOST=${main_domain}",
  "NEXTAUTH_SECRET=${nextauth_secret}",
  "CALENDSO_ENCRYPTION_KEY=${calcom_encryption_key}",
]
mounts = []

[[config.domains]]
serviceName = "calcom"
port = 3_000
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBwb3N0Z3JlczpcbiAgICBpbWFnZTogcG9zdGdyZXM6MTYtYWxwaW5lXG5cbiAgICB2b2x1bWVzOlxuICAgICAgLSBjYWxjb20tZGF0YTovdmFyL2xpYi9wb3N0Z3Jlc3FsL2RhdGFcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gUE9TVEdSRVNfVVNFUj1wb3N0Z3Jlc1xuICAgICAgLSBQT1NUR1JFU19QQVNTV09SRD1wYXNzd29yZFxuICAgICAgLSBQT1NUR1JFU19EQj1kYlxuICAgICAgLSBEQVRBQkFTRV9VUkw9cG9zdGdyZXM6Ly9wb3N0Z3JlczpwYXNzd29yZEBwb3N0Z3Jlczo1NDMyL2RiXG5cbiAgY2FsY29tOlxuICAgIGltYWdlOiBjYWxjb20vY2FsLmNvbTp2Mi43LjZcbiAgICBkZXBlbmRzX29uOlxuICAgICAgLSBwb3N0Z3Jlc1xuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBORVhUQVVUSF9TRUNSRVQ9JHtORVhUQVVUSF9TRUNSRVR9XG4gICAgICAtIENBTEVORFNPX0VOQ1JZUFRJT05fS0VZPSR7Q0FMRU5EU09fRU5DUllQVElPTl9LRVl9XG4gICAgICAtIERBVEFCQVNFX1VSTD1wb3N0Z3JlczovL3Bvc3RncmVzOnBhc3N3b3JkQHBvc3RncmVzOjU0MzIvZGJcbiAgICAgIC0gTkVYVF9QVUJMSUNfV0VCQVBQX1VSTD1odHRwOi8vJHtDQUxDT01fSE9TVH1cbiAgICAgIC0gTkVYVEFVVEhfVVJMPWh0dHA6Ly8ke0NBTENPTV9IT1NUfS9hcGkvYXV0aFxuXG52b2x1bWVzOlxuICBjYWxjb20tZGF0YTpcbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5jYWxjb21fZW5jcnlwdGlvbl9rZXkgPSBcIiR7YmFzZTY0OjMyfVwiXG5uZXh0YXV0aF9zZWNyZXQgPSBcIiR7YmFzZTY0OjMyfVwiXG5cbltjb25maWddXG5lbnYgPSBbXG4gIFwiQ0FMQ09NX0hPU1Q9JHttYWluX2RvbWFpbn1cIixcbiAgXCJORVhUQVVUSF9TRUNSRVQ9JHtuZXh0YXV0aF9zZWNyZXR9XCIsXG4gIFwiQ0FMRU5EU09fRU5DUllQVElPTl9LRVk9JHtjYWxjb21fZW5jcnlwdGlvbl9rZXl9XCIsXG5dXG5tb3VudHMgPSBbXVxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJjYWxjb21cIlxucG9ydCA9IDNfMDAwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG4iCn0=
```

## Links

`scheduling`,`booking`

---

Version:`v2.7.6`

ByteStashByteStash is a self-hosted web application designed to store, organise, and manage your code snippets efficiently. With support for creating, editing, and filtering snippets, ByteStash helps you keep track of your code in one secure place.

CalibreCalibre is a comprehensive e-book management tool designed to organize, convert, and read your e-book collection. It supports most of the major e-book formats and is compatible with various e-book reader devices.

### On this page

ConfigurationBase64LinksTags