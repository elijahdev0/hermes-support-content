---
title: "Paymenter | Dokploy"
source: "https://docs.dokploy.com/docs/templates/paymenter"
category: dokploy-docs
created: "2026-06-25T17:21:55.477Z"
---

Paymenter | Dokploy

# Paymenter

Copy as Markdown

Paymenter is a modern billing and payment management system for hosting providers, with automation, invoicing, and client management features.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  database:
    image: mariadb:lts
    restart: unless-stopped
    command: --default-authentication-plugin=mysql_native_password
    volumes:
      - paymenter-database:/var/lib/mysql
    environment:
      - MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD}
      - MYSQL_DATABASE=${MYSQL_DATABASE:-paymenter}
      - MYSQL_USER=${MYSQL_USER:-paymenter}
      - MYSQL_PASSWORD=${MYSQL_PASSWORD}

  cache:
    image: redis:alpine
    restart: unless-stopped
    volumes:
      - paymenter-redis:/data

  paymenter:
    image: ghcr.io/paymenter/paymenter:latest
    restart: unless-stopped
    ports:
      - 80
    depends_on:
      - database
      - cache
    volumes:
      - paymenter-storage:/app/var
      - paymenter-logs:/app/storage/logs
      - paymenter-public:/app/storage/app/public
    environment:
      - APP_ENV=${APP_ENV:-production}
      - APP_DEBUG=false
      - APP_KEY=${APP_KEY}
      - APP_URL=${APP_URL}
      - DB_CONNECTION=mysql
      - DB_HOST=database
      - DB_PORT=3306
      - DB_DATABASE=${MYSQL_DATABASE:-paymenter}
      - DB_USERNAME=${MYSQL_USER:-paymenter}
      - DB_PASSWORD=${MYSQL_PASSWORD}
      - CACHE_STORE=redis
      - REDIS_HOST=cache
      - REDIS_PORT=6379
      - TRUSTED_PROXIES=*

volumes:
  paymenter-database: {}
  paymenter-storage: {}
  paymenter-logs: {}
  paymenter-public: {}
  paymenter-redis: {}
```

```
[variables]
main_domain = "${domain}"
app_key = "${base64:32}"
mysql_password = "${password:16}"
mysql_root_password = "${password:20}"

[config]
[[config.domains]]
serviceName = "paymenter"
port = 80
host = "${main_domain}"
path = "/"

[config.env]
APP_URL = "https://${main_domain}"
APP_KEY = "base64:${app_key}"
MYSQL_PASSWORD = "${mysql_password}"
MYSQL_ROOT_PASSWORD = "${mysql_root_password}"
MYSQL_DATABASE = "paymenter"
MYSQL_USER = "paymenter"

[[config.mounts]]
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBkYXRhYmFzZTpcbiAgICBpbWFnZTogbWFyaWFkYjpsdHNcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGNvbW1hbmQ6IC0tZGVmYXVsdC1hdXRoZW50aWNhdGlvbi1wbHVnaW49bXlzcWxfbmF0aXZlX3Bhc3N3b3JkXG4gICAgdm9sdW1lczpcbiAgICAgIC0gcGF5bWVudGVyLWRhdGFiYXNlOi92YXIvbGliL215c3FsXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIE1ZU1FMX1JPT1RfUEFTU1dPUkQ9JHtNWVNRTF9ST09UX1BBU1NXT1JEfVxuICAgICAgLSBNWVNRTF9EQVRBQkFTRT0ke01ZU1FMX0RBVEFCQVNFOi1wYXltZW50ZXJ9XG4gICAgICAtIE1ZU1FMX1VTRVI9JHtNWVNRTF9VU0VSOi1wYXltZW50ZXJ9XG4gICAgICAtIE1ZU1FMX1BBU1NXT1JEPSR7TVlTUUxfUEFTU1dPUkR9XG5cbiAgY2FjaGU6XG4gICAgaW1hZ2U6IHJlZGlzOmFscGluZVxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgdm9sdW1lczpcbiAgICAgIC0gcGF5bWVudGVyLXJlZGlzOi9kYXRhXG5cbiAgcGF5bWVudGVyOlxuICAgIGltYWdlOiBnaGNyLmlvL3BheW1lbnRlci9wYXltZW50ZXI6bGF0ZXN0XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBwb3J0czpcbiAgICAgIC0gODBcbiAgICBkZXBlbmRzX29uOlxuICAgICAgLSBkYXRhYmFzZVxuICAgICAgLSBjYWNoZVxuICAgIHZvbHVtZXM6XG4gICAgICAtIHBheW1lbnRlci1zdG9yYWdlOi9hcHAvdmFyXG4gICAgICAtIHBheW1lbnRlci1sb2dzOi9hcHAvc3RvcmFnZS9sb2dzXG4gICAgICAtIHBheW1lbnRlci1wdWJsaWM6L2FwcC9zdG9yYWdlL2FwcC9wdWJsaWNcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gQVBQX0VOVj0ke0FQUF9FTlY6LXByb2R1Y3Rpb259XG4gICAgICAtIEFQUF9ERUJVRz1mYWxzZVxuICAgICAgLSBBUFBfS0VZPSR7QVBQX0tFWX1cbiAgICAgIC0gQVBQX1VSTD0ke0FQUF9VUkx9XG4gICAgICAtIERCX0NPTk5FQ1RJT049bXlzcWxcbiAgICAgIC0gREJfSE9TVD1kYXRhYmFzZVxuICAgICAgLSBEQl9QT1JUPTMzMDZcbiAgICAgIC0gREJfREFUQUJBU0U9JHtNWVNRTF9EQVRBQkFTRTotcGF5bWVudGVyfVxuICAgICAgLSBEQl9VU0VSTkFNRT0ke01ZU1FMX1VTRVI6LXBheW1lbnRlcn1cbiAgICAgIC0gREJfUEFTU1dPUkQ9JHtNWVNRTF9QQVNTV09SRH1cbiAgICAgIC0gQ0FDSEVfU1RPUkU9cmVkaXNcbiAgICAgIC0gUkVESVNfSE9TVD1jYWNoZVxuICAgICAgLSBSRURJU19QT1JUPTYzNzlcbiAgICAgIC0gVFJVU1RFRF9QUk9YSUVTPSpcblxudm9sdW1lczpcbiAgcGF5bWVudGVyLWRhdGFiYXNlOiB7fVxuICBwYXltZW50ZXItc3RvcmFnZToge31cbiAgcGF5bWVudGVyLWxvZ3M6IHt9XG4gIHBheW1lbnRlci1wdWJsaWM6IHt9XG4gIHBheW1lbnRlci1yZWRpczoge30iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuYXBwX2tleSA9IFwiJHtiYXNlNjQ6MzJ9XCJcbm15c3FsX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkOjE2fVwiXG5teXNxbF9yb290X3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkOjIwfVwiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJwYXltZW50ZXJcIlxucG9ydCA9IDgwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5wYXRoID0gXCIvXCJcblxuW2NvbmZpZy5lbnZdXG5BUFBfVVJMID0gXCJodHRwczovLyR7bWFpbl9kb21haW59XCJcbkFQUF9LRVkgPSBcImJhc2U2NDoke2FwcF9rZXl9XCJcbk1ZU1FMX1BBU1NXT1JEID0gXCIke215c3FsX3Bhc3N3b3JkfVwiXG5NWVNRTF9ST09UX1BBU1NXT1JEID0gXCIke215c3FsX3Jvb3RfcGFzc3dvcmR9XCJcbk1ZU1FMX0RBVEFCQVNFID0gXCJwYXltZW50ZXJcIlxuTVlTUUxfVVNFUiA9IFwicGF5bWVudGVyXCJcblxuW1tjb25maWcubW91bnRzXV0iCn0=
```

## Links

`billing`,`payment`,`hosting`,`invoicing`,`business`,`automation`,`client-management`

---

Version:`latest`

PastefyPastefy is an open-source pastebin with support for syntax highlighting and OAuth2 authentication.

PeerDBData integration platform that synchronizes and federates data across databases with a unified API.

### On this page

ConfigurationBase64LinksTags