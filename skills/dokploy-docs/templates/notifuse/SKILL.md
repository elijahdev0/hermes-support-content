---
title: "Notifuse | Dokploy"
source: "https://docs.dokploy.com/docs/templates/notifuse"
category: dokploy-docs
created: "2026-06-25T17:21:54.355Z"
---

Notifuse | Dokploy

# Notifuse

Copy as Markdown

Open-source newsletter and notification platform that empowers teams to create, send, and track communications at scale.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  db:
    image: postgres:17-alpine
    restart: unless-stopped
    volumes:
      - db_data:/var/lib/postgresql/data
    environment:
      POSTGRES_DB: postgres
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      timeout: 5s
      retries: 5

  notifuse:
    image: notifuse/notifuse:latest
    restart: unless-stopped
    depends_on:
      - db
    environment:
      # Root user configuration
      ROOT_EMAIL: ${ROOT_EMAIL}

      # API configuration
      API_ENDPOINT: ${API_ENDPOINT}

      # Database configuration
      DB_HOST: db
      DB_PORT: 5432
      DB_USER: postgres
      DB_PASSWORD: postgres
      DB_PREFIX: notifuse
      DB_NAME: postgres
      DB_SSLMODE: disable

      # Secret key for authentication (auto-generated)
      SECRET_KEY: ${SECRET_KEY}

      # Server configuration
      SERVER_PORT: 8080
      SERVER_HOST: 0.0.0.0
      ENVIRONMENT: production
    volumes:
      - notifuse_data:/app/data
    healthcheck:
      test: ["CMD", "wget", "--no-verbose", "--tries=1", "--spider", "http://localhost:8080/healthz"]
      interval: 10s
      timeout: 5s
      retries: 3
      start_period: 10s

volumes:
  db_data: {}
  notifuse_data: {}
```

```
[variables]
main_domain = "${domain}"
secret_key = "${base64:64}"

[config]
[[config.domains]]
serviceName = "notifuse"
port = 8080
host = "${main_domain}"

[config.env]
ROOT_EMAIL = "${email}"
API_ENDPOINT = "https://${main_domain}"
SECRET_KEY = "${secret_key}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBkYjpcbiAgICBpbWFnZTogcG9zdGdyZXM6MTctYWxwaW5lXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICB2b2x1bWVzOlxuICAgICAgLSBkYl9kYXRhOi92YXIvbGliL3Bvc3RncmVzcWwvZGF0YVxuICAgIGVudmlyb25tZW50OlxuICAgICAgUE9TVEdSRVNfREI6IHBvc3RncmVzXG4gICAgICBQT1NUR1JFU19VU0VSOiBwb3N0Z3Jlc1xuICAgICAgUE9TVEdSRVNfUEFTU1dPUkQ6IHBvc3RncmVzXG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OiBbXCJDTUQtU0hFTExcIiwgXCJwZ19pc3JlYWR5IC1VIHBvc3RncmVzXCJdXG4gICAgICBpbnRlcnZhbDogNXNcbiAgICAgIHRpbWVvdXQ6IDVzXG4gICAgICByZXRyaWVzOiA1XG5cbiAgbm90aWZ1c2U6XG4gICAgaW1hZ2U6IG5vdGlmdXNlL25vdGlmdXNlOmxhdGVzdFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIC0gZGJcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgICMgUm9vdCB1c2VyIGNvbmZpZ3VyYXRpb25cbiAgICAgIFJPT1RfRU1BSUw6ICR7Uk9PVF9FTUFJTH1cblxuICAgICAgIyBBUEkgY29uZmlndXJhdGlvblxuICAgICAgQVBJX0VORFBPSU5UOiAke0FQSV9FTkRQT0lOVH1cblxuICAgICAgIyBEYXRhYmFzZSBjb25maWd1cmF0aW9uXG4gICAgICBEQl9IT1NUOiBkYlxuICAgICAgREJfUE9SVDogNTQzMlxuICAgICAgREJfVVNFUjogcG9zdGdyZXNcbiAgICAgIERCX1BBU1NXT1JEOiBwb3N0Z3Jlc1xuICAgICAgREJfUFJFRklYOiBub3RpZnVzZVxuICAgICAgREJfTkFNRTogcG9zdGdyZXNcbiAgICAgIERCX1NTTE1PREU6IGRpc2FibGVcblxuICAgICAgIyBTZWNyZXQga2V5IGZvciBhdXRoZW50aWNhdGlvbiAoYXV0by1nZW5lcmF0ZWQpXG4gICAgICBTRUNSRVRfS0VZOiAke1NFQ1JFVF9LRVl9XG5cbiAgICAgICMgU2VydmVyIGNvbmZpZ3VyYXRpb25cbiAgICAgIFNFUlZFUl9QT1JUOiA4MDgwXG4gICAgICBTRVJWRVJfSE9TVDogMC4wLjAuMFxuICAgICAgRU5WSVJPTk1FTlQ6IHByb2R1Y3Rpb25cbiAgICB2b2x1bWVzOlxuICAgICAgLSBub3RpZnVzZV9kYXRhOi9hcHAvZGF0YVxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDogW1wiQ01EXCIsIFwid2dldFwiLCBcIi0tbm8tdmVyYm9zZVwiLCBcIi0tdHJpZXM9MVwiLCBcIi0tc3BpZGVyXCIsIFwiaHR0cDovL2xvY2FsaG9zdDo4MDgwL2hlYWx0aHpcIl1cbiAgICAgIGludGVydmFsOiAxMHNcbiAgICAgIHRpbWVvdXQ6IDVzXG4gICAgICByZXRyaWVzOiAzXG4gICAgICBzdGFydF9wZXJpb2Q6IDEwc1xuXG52b2x1bWVzOlxuICBkYl9kYXRhOiB7fVxuICBub3RpZnVzZV9kYXRhOiB7fVxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbnNlY3JldF9rZXkgPSBcIiR7YmFzZTY0OjY0fVwiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJub3RpZnVzZVwiXG5wb3J0ID0gODA4MFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cblJPT1RfRU1BSUwgPSBcIiR7ZW1haWx9XCJcbkFQSV9FTkRQT0lOVCA9IFwiaHR0cHM6Ly8ke21haW5fZG9tYWlufVwiXG5TRUNSRVRfS0VZID0gXCIke3NlY3JldF9rZXl9XCJcbiIKfQ==
```

## Links

`newsletter`,`email`,`communication`,`notifications`

---

Version:`latest`

NocoDBNocoDB is an opensource Airtable alternative that turns any MySQL, PostgreSQL, SQL Server, SQLite & MariaDB into a smart spreadsheet.

NTFYntfy lets you send push notifications to your phone or desktop via scripts from any computer, using simple HTTP PUT or POST requests.

### On this page

ConfigurationBase64LinksTags