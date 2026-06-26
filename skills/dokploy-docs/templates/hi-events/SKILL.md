---
title: "Hi.events | Dokploy"
source: "https://docs.dokploy.com/docs/templates/hi-events"
category: dokploy-docs
created: "2026-06-25T17:21:49.750Z"
---

Hi.events | Dokploy

# Hi.events

Copy as Markdown

Hi.Events is a self-hosted event management and ticket selling platform that allows you to create, manage and promote events easily.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  all-in-one:
    image: daveearley/hi.events-all-in-one:v0.8.0-beta.1
    restart: always
    environment:
      - VITE_FRONTEND_URL=https://${DOMAIN}
      - APP_FRONTEND_URL=https://${DOMAIN}
      - VITE_API_URL_CLIENT=https://${DOMAIN}/api
      - VITE_API_URL_SERVER=http://localhost:80/api
      - VITE_STRIPE_PUBLISHABLE_KEY
      - LOG_CHANNEL=stderr
      - QUEUE_CONNECTION=sync
      - MAIL_MAILER=array
      - APP_KEY
      - JWT_SECRET
      - FILESYSTEM_PUBLIC_DISK=public
      - FILESYSTEM_PRIVATE_DISK=local
      - APP_CDN_URL=https://${DOMAIN}/storage
      - DATABASE_URL=postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@postgres:5432/${POSTGRES_DB}
      - MAIL_MAILER
      - MAIL_HOST
      - MAIL_PORT
      - MAIL_FROM_ADDRESS
      - MAIL_FROM_NAME
    depends_on:
      - postgres

  postgres:
    image: elestio/postgres:16
    restart: always

    environment:
      - POSTGRES_DB
      - POSTGRES_USER
      - POSTGRES_PASSWORD
    volumes:
      - pg_hi-events_data:/var/lib/postgresql/data

volumes:
  pg_hi-events_data:
```

```
[variables]
main_domain = "${domain}"
postgres_password = "${password}"
jwt_secret = "${password}"
app_key = "${password}"

[config]
env = [
  "DOMAIN=${main_domain}",
  "POSTGRES_DB=hievents",
  "POSTGRES_USER=hievents",
  "POSTGRES_PASSWORD=${postgres_password}",
  "VITE_STRIPE_PUBLISHABLE_KEY=",
  "APP_KEY=${app_key}",
  "JWT_SECRET=${jwt_secret}",
  "MAIL_MAILER=",
  "MAIL_HOST=",
  "MAIL_PORT=",
  "MAIL_FROM_ADDRESS=",
  "MAIL_FROM_NAME=",
]
mounts = []

[[config.domains]]
serviceName = "all-in-one"
port = 80
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBhbGwtaW4tb25lOlxuICAgIGltYWdlOiBkYXZlZWFybGV5L2hpLmV2ZW50cy1hbGwtaW4tb25lOnYwLjguMC1iZXRhLjFcbiAgICByZXN0YXJ0OiBhbHdheXNcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gVklURV9GUk9OVEVORF9VUkw9aHR0cHM6Ly8ke0RPTUFJTn1cbiAgICAgIC0gQVBQX0ZST05URU5EX1VSTD1odHRwczovLyR7RE9NQUlOfVxuICAgICAgLSBWSVRFX0FQSV9VUkxfQ0xJRU5UPWh0dHBzOi8vJHtET01BSU59L2FwaVxuICAgICAgLSBWSVRFX0FQSV9VUkxfU0VSVkVSPWh0dHA6Ly9sb2NhbGhvc3Q6ODAvYXBpXG4gICAgICAtIFZJVEVfU1RSSVBFX1BVQkxJU0hBQkxFX0tFWVxuICAgICAgLSBMT0dfQ0hBTk5FTD1zdGRlcnJcbiAgICAgIC0gUVVFVUVfQ09OTkVDVElPTj1zeW5jXG4gICAgICAtIE1BSUxfTUFJTEVSPWFycmF5XG4gICAgICAtIEFQUF9LRVlcbiAgICAgIC0gSldUX1NFQ1JFVFxuICAgICAgLSBGSUxFU1lTVEVNX1BVQkxJQ19ESVNLPXB1YmxpY1xuICAgICAgLSBGSUxFU1lTVEVNX1BSSVZBVEVfRElTSz1sb2NhbFxuICAgICAgLSBBUFBfQ0ROX1VSTD1odHRwczovLyR7RE9NQUlOfS9zdG9yYWdlXG4gICAgICAtIERBVEFCQVNFX1VSTD1wb3N0Z3Jlc3FsOi8vJHtQT1NUR1JFU19VU0VSfToke1BPU1RHUkVTX1BBU1NXT1JEfUBwb3N0Z3Jlczo1NDMyLyR7UE9TVEdSRVNfREJ9XG4gICAgICAtIE1BSUxfTUFJTEVSXG4gICAgICAtIE1BSUxfSE9TVFxuICAgICAgLSBNQUlMX1BPUlRcbiAgICAgIC0gTUFJTF9GUk9NX0FERFJFU1NcbiAgICAgIC0gTUFJTF9GUk9NX05BTUVcbiAgICBkZXBlbmRzX29uOlxuICAgICAgLSBwb3N0Z3Jlc1xuXG4gIHBvc3RncmVzOlxuICAgIGltYWdlOiBlbGVzdGlvL3Bvc3RncmVzOjE2XG4gICAgcmVzdGFydDogYWx3YXlzXG5cbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gUE9TVEdSRVNfREJcbiAgICAgIC0gUE9TVEdSRVNfVVNFUlxuICAgICAgLSBQT1NUR1JFU19QQVNTV09SRFxuICAgIHZvbHVtZXM6XG4gICAgICAtIHBnX2hpLWV2ZW50c19kYXRhOi92YXIvbGliL3Bvc3RncmVzcWwvZGF0YVxuXG52b2x1bWVzOlxuICBwZ19oaS1ldmVudHNfZGF0YToiLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxucG9zdGdyZXNfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmR9XCJcbmp3dF9zZWNyZXQgPSBcIiR7cGFzc3dvcmR9XCJcbmFwcF9rZXkgPSBcIiR7cGFzc3dvcmR9XCJcblxuW2NvbmZpZ11cbmVudiA9IFtcbiAgXCJET01BSU49JHttYWluX2RvbWFpbn1cIixcbiAgXCJQT1NUR1JFU19EQj1oaWV2ZW50c1wiLFxuICBcIlBPU1RHUkVTX1VTRVI9aGlldmVudHNcIixcbiAgXCJQT1NUR1JFU19QQVNTV09SRD0ke3Bvc3RncmVzX3Bhc3N3b3JkfVwiLFxuICBcIlZJVEVfU1RSSVBFX1BVQkxJU0hBQkxFX0tFWT1cIixcbiAgXCJBUFBfS0VZPSR7YXBwX2tleX1cIixcbiAgXCJKV1RfU0VDUkVUPSR7and0X3NlY3JldH1cIixcbiAgXCJNQUlMX01BSUxFUj1cIixcbiAgXCJNQUlMX0hPU1Q9XCIsXG4gIFwiTUFJTF9QT1JUPVwiLFxuICBcIk1BSUxfRlJPTV9BRERSRVNTPVwiLFxuICBcIk1BSUxfRlJPTV9OQU1FPVwiLFxuXVxubW91bnRzID0gW11cblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiYWxsLWluLW9uZVwiXG5wb3J0ID0gODBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcbiIKfQ==
```

## Links

`self-hosted`,`open-source`,`manager`

---

Version:`0.8.0-beta.1`

HeyFormAllows anyone to create engaging conversational forms for surveys, questionnaires, quizzes, and polls. No coding skills required.

HoarderHoarder is an open source "Bookmark Everything" app that uses AI for automatically tagging the content you throw at it.

### On this page

ConfigurationBase64LinksTags