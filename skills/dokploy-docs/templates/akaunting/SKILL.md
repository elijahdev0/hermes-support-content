---
title: "Akaunting | Dokploy"
source: "https://docs.dokploy.com/docs/templates/akaunting"
category: dokploy-docs
created: "2026-06-25T17:21:40.414Z"
---

Akaunting | Dokploy

# Akaunting

Copy as Markdown

Akaunting is a self-hosted, open-source accounting app for small businesses.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  akaunting:
    image: docker.io/akaunting/akaunting:latest
    restart: unless-stopped
    depends_on:
      akaunting-db:
        condition: service_healthy
    environment:
      # App config
      APP_URL: ${APP_URL}
      LOCALE: ${LOCALE}

      # Database connection
      DB_HOST: akaunting-db
      DB_PORT: 3306
      DB_NAME: ${DB_NAME}
      DB_USERNAME: ${DB_USERNAME}
      DB_PASSWORD: ${DB_PASSWORD}
      DB_PREFIX: ${DB_PREFIX}

      # First-run bootstrap (company + admin)
      COMPANY_NAME: ${COMPANY_NAME}
      COMPANY_EMAIL: ${COMPANY_EMAIL}
      ADMIN_EMAIL: ${ADMIN_EMAIL}
      ADMIN_PASSWORD: ${ADMIN_PASSWORD}

    # Expose only to internal network; domain routing handled by Dokploy/Traefik
    expose:
      - "80"

    volumes:
      - akaunting-data:/var/www/html

  akaunting-db:
    image: mariadb:10.11
    restart: unless-stopped
    environment:
      MYSQL_DATABASE: ${MYSQL_DATABASE}
      MYSQL_USER: ${MYSQL_USER}
      MYSQL_PASSWORD: ${MYSQL_PASSWORD}
      # Randomizes root password on each deployment (recommended)
      MYSQL_RANDOM_ROOT_PASSWORD: "yes"
    volumes:
      - akaunting-db:/var/lib/mysql
    healthcheck:
      test: ["CMD", "mysqladmin", "ping", "-h", "localhost"]
      interval: 10s
      timeout: 5s
      retries: 5

volumes:
  akaunting-data: {}
  akaunting-db: {}
```

```
[variables]
# Domain & UI
main_domain = "${domain}"
locale = "en-US"

# DB credentials (safe defaults; user can override in UI)
db_name = "akaunting"
db_user = "admin"
mysql_password = "${password:24}"

# Akaunting setup variables
company_name = "My Company"
company_email = "${email}"
admin_email = "${email}"
admin_password = "${password:24}"

# Akaunting table prefix: 3 hex chars + underscore (e.g., "a1f_")
db_prefix = "${hash:3}_"

# Domain routing for the web UI
[[config.domains]]
serviceName = "akaunting"
port = 80
host = "${main_domain}"

[config]
env = [
  # App
  "APP_URL=${main_domain}",
  "LOCALE=${locale}",

  # Database (app)
  "DB_HOST=akaunting-db",
  "DB_PORT=3306",
  "DB_NAME=${db_name}",
  "DB_USERNAME=${db_user}",
  "DB_PASSWORD=${mysql_password}",
  "DB_PREFIX=${db_prefix}",

  # First-run bootstrap (app)
  "COMPANY_NAME=${company_name}",
  "COMPANY_EMAIL=${company_email}",
  "ADMIN_EMAIL=${admin_email}",
  "ADMIN_PASSWORD=${admin_password}",

  # Database (server)
  "MYSQL_DATABASE=${db_name}",
  "MYSQL_USER=${db_user}",
  "MYSQL_PASSWORD=${mysql_password}",
  "MYSQL_RANDOM_ROOT_PASSWORD=yes"
]

# No custom mounts needed; volumes are already defined in compose.
[[config.mounts]]
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIGFrYXVudGluZzpcbiAgICBpbWFnZTogZG9ja2VyLmlvL2FrYXVudGluZy9ha2F1bnRpbmc6bGF0ZXN0XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBkZXBlbmRzX29uOlxuICAgICAgYWthdW50aW5nLWRiOlxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2VfaGVhbHRoeVxuICAgIGVudmlyb25tZW50OlxuICAgICAgIyBBcHAgY29uZmlnXG4gICAgICBBUFBfVVJMOiAke0FQUF9VUkx9XG4gICAgICBMT0NBTEU6ICR7TE9DQUxFfVxuXG4gICAgICAjIERhdGFiYXNlIGNvbm5lY3Rpb25cbiAgICAgIERCX0hPU1Q6IGFrYXVudGluZy1kYlxuICAgICAgREJfUE9SVDogMzMwNlxuICAgICAgREJfTkFNRTogJHtEQl9OQU1FfVxuICAgICAgREJfVVNFUk5BTUU6ICR7REJfVVNFUk5BTUV9XG4gICAgICBEQl9QQVNTV09SRDogJHtEQl9QQVNTV09SRH1cbiAgICAgIERCX1BSRUZJWDogJHtEQl9QUkVGSVh9XG5cbiAgICAgICMgRmlyc3QtcnVuIGJvb3RzdHJhcCAoY29tcGFueSArIGFkbWluKVxuICAgICAgQ09NUEFOWV9OQU1FOiAke0NPTVBBTllfTkFNRX1cbiAgICAgIENPTVBBTllfRU1BSUw6ICR7Q09NUEFOWV9FTUFJTH1cbiAgICAgIEFETUlOX0VNQUlMOiAke0FETUlOX0VNQUlMfVxuICAgICAgQURNSU5fUEFTU1dPUkQ6ICR7QURNSU5fUEFTU1dPUkR9XG5cbiAgICAjIEV4cG9zZSBvbmx5IHRvIGludGVybmFsIG5ldHdvcms7IGRvbWFpbiByb3V0aW5nIGhhbmRsZWQgYnkgRG9rcGxveS9UcmFlZmlrXG4gICAgZXhwb3NlOlxuICAgICAgLSBcIjgwXCJcblxuICAgIHZvbHVtZXM6XG4gICAgICAtIGFrYXVudGluZy1kYXRhOi92YXIvd3d3L2h0bWxcblxuICBha2F1bnRpbmctZGI6XG4gICAgaW1hZ2U6IG1hcmlhZGI6MTAuMTFcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGVudmlyb25tZW50OlxuICAgICAgTVlTUUxfREFUQUJBU0U6ICR7TVlTUUxfREFUQUJBU0V9XG4gICAgICBNWVNRTF9VU0VSOiAke01ZU1FMX1VTRVJ9XG4gICAgICBNWVNRTF9QQVNTV09SRDogJHtNWVNRTF9QQVNTV09SRH1cbiAgICAgICMgUmFuZG9taXplcyByb290IHBhc3N3b3JkIG9uIGVhY2ggZGVwbG95bWVudCAocmVjb21tZW5kZWQpXG4gICAgICBNWVNRTF9SQU5ET01fUk9PVF9QQVNTV09SRDogXCJ5ZXNcIlxuICAgIHZvbHVtZXM6XG4gICAgICAtIGFrYXVudGluZy1kYjovdmFyL2xpYi9teXNxbFxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDogW1wiQ01EXCIsIFwibXlzcWxhZG1pblwiLCBcInBpbmdcIiwgXCItaFwiLCBcImxvY2FsaG9zdFwiXVxuICAgICAgaW50ZXJ2YWw6IDEwc1xuICAgICAgdGltZW91dDogNXNcbiAgICAgIHJldHJpZXM6IDVcblxudm9sdW1lczpcbiAgYWthdW50aW5nLWRhdGE6IHt9XG4gIGFrYXVudGluZy1kYjoge31cbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxuIyBEb21haW4gJiBVSVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5sb2NhbGUgPSBcImVuLVVTXCJcblxuIyBEQiBjcmVkZW50aWFscyAoc2FmZSBkZWZhdWx0czsgdXNlciBjYW4gb3ZlcnJpZGUgaW4gVUkpXG5kYl9uYW1lID0gXCJha2F1bnRpbmdcIlxuZGJfdXNlciA9IFwiYWRtaW5cIlxubXlzcWxfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MjR9XCJcblxuIyBBa2F1bnRpbmcgc2V0dXAgdmFyaWFibGVzXG5jb21wYW55X25hbWUgPSBcIk15IENvbXBhbnlcIlxuY29tcGFueV9lbWFpbCA9IFwiJHtlbWFpbH1cIlxuYWRtaW5fZW1haWwgPSBcIiR7ZW1haWx9XCJcbmFkbWluX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkOjI0fVwiXG5cbiMgQWthdW50aW5nIHRhYmxlIHByZWZpeDogMyBoZXggY2hhcnMgKyB1bmRlcnNjb3JlIChlLmcuLCBcImExZl9cIilcbmRiX3ByZWZpeCA9IFwiJHtoYXNoOjN9X1wiXG5cbiMgRG9tYWluIHJvdXRpbmcgZm9yIHRoZSB3ZWIgVUlcbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImFrYXVudGluZ1wiXG5wb3J0ID0gODBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW2NvbmZpZ11cbmVudiA9IFtcbiAgIyBBcHBcbiAgXCJBUFBfVVJMPSR7bWFpbl9kb21haW59XCIsXG4gIFwiTE9DQUxFPSR7bG9jYWxlfVwiLFxuXG4gICMgRGF0YWJhc2UgKGFwcClcbiAgXCJEQl9IT1NUPWFrYXVudGluZy1kYlwiLFxuICBcIkRCX1BPUlQ9MzMwNlwiLFxuICBcIkRCX05BTUU9JHtkYl9uYW1lfVwiLFxuICBcIkRCX1VTRVJOQU1FPSR7ZGJfdXNlcn1cIixcbiAgXCJEQl9QQVNTV09SRD0ke215c3FsX3Bhc3N3b3JkfVwiLFxuICBcIkRCX1BSRUZJWD0ke2RiX3ByZWZpeH1cIixcblxuICAjIEZpcnN0LXJ1biBib290c3RyYXAgKGFwcClcbiAgXCJDT01QQU5ZX05BTUU9JHtjb21wYW55X25hbWV9XCIsXG4gIFwiQ09NUEFOWV9FTUFJTD0ke2NvbXBhbnlfZW1haWx9XCIsXG4gIFwiQURNSU5fRU1BSUw9JHthZG1pbl9lbWFpbH1cIixcbiAgXCJBRE1JTl9QQVNTV09SRD0ke2FkbWluX3Bhc3N3b3JkfVwiLFxuXG4gICMgRGF0YWJhc2UgKHNlcnZlcilcbiAgXCJNWVNRTF9EQVRBQkFTRT0ke2RiX25hbWV9XCIsXG4gIFwiTVlTUUxfVVNFUj0ke2RiX3VzZXJ9XCIsXG4gIFwiTVlTUUxfUEFTU1dPUkQ9JHtteXNxbF9wYXNzd29yZH1cIixcbiAgXCJNWVNRTF9SQU5ET01fUk9PVF9QQVNTV09SRD15ZXNcIlxuXVxuXG4jIE5vIGN1c3RvbSBtb3VudHMgbmVlZGVkOyB2b2x1bWVzIGFyZSBhbHJlYWR5IGRlZmluZWQgaW4gY29tcG9zZS5cbltbY29uZmlnLm1vdW50c11dXG4iCn0=
```

## Links

`finance`,`accounting`,`php`,`mariadb`,`self-hosted`

---

Version:`latest`

Agent DVRAgent DVR is a comprehensive video surveillance software with motion detection, alerts, and remote access capabilities.

AList🗂️A file list/WebDAV program that supports multiple storages, powered by Gin and Solidjs.

### On this page

ConfigurationBase64LinksTags