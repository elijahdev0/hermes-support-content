---
title: "Pyrodactyl | Dokploy"
source: "https://docs.dokploy.com/docs/templates/pyrodactyl"
category: dokploy-docs
created: "2026-06-25T17:21:57.937Z"
---

Pyrodactyl | Dokploy

# Pyrodactyl

Copy as Markdown

Pyrodactyl is the Pterodactyl-based game server panel that's faster, smaller, safer, and more accessible than Pelican.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  database:
    image: mariadb:11
    restart: always
    command: --default-authentication-plugin=mysql_native_password
    volumes:
      - "pterodb:/var/lib/mysql"
    environment:
      MYSQL_DATABASE: "panel"
      MYSQL_USER: "pterodactyl"
      MYSQL_PASSWORD:
      MYSQL_ROOT_PASSWORD:
  cache:
    image: redis:alpine
    restart: always
  panel:
    image: ghcr.io/pyrodactyl-oss/pyrodactyl:latest
    restart: always
    links:
      - database
      - cache
    volumes:
      - "pterovar:/app/var/"
      - "pteronginx:/etc/nginx/http.d/"
      - "pterocerts:/etc/letsencrypt/"
      - "pterologs:/app/storage/logs"
    environment:
      APP_URL: "https://${APP_DOMAIN}"
      APP_ENV: "production"
      APP_ENVIRONMENT_ONLY: "false"
      CACHE_DRIVER:
      SESSION_DRIVER:
      QUEUE_DRIVER:
      REDIS_HOST:
      DB_HOST:
      DB_PORT:
      DB_PASSWORD: ${MYSQL_PASSWORD}
      DB_CONNECTION: "mariadb"

volumes:
  pterodb:
  pterovar:
  pteronginx:
  pterocerts:
  pterologs:
```

```
[variables]
main_domain = "${domain}"
db_password = "${password:32}"
db_root_password = "${password:32}"
secret_key = "${base64:48}"

[config]
env = [
"Domain=${main_domain}",
"RECAPTCHA_ENABLED=true",
"APP_DOMAIN=${main_domain}",
"APP_TIMEZONE=UTC",
"[email protected]",
"[email protected]",
"MAIL_DRIVER=smtp",
"MAIL_HOST=mail",
"MAIL_PORT=1025",
"MAIL_USERNAME=",
"MAIL_PASSWORD=",
"MAIL_ENCRYPTION=true",
"MYSQL_PASSWORD=${db_password}",
"MYSQL_ROOT_PASSWORD=${db_root_password}",
"DB_PORT=3306",
"CACHE_DRIVER=redis",
"SESSION_DRIVER=redis",
"QUEUE_DRIVER=redis",
"REDIS_HOST=cache",
"DB_HOST=database",
]
mounts = []

[[config.domains]]
serviceName = "panel"
port = 80
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBkYXRhYmFzZTpcbiAgICBpbWFnZTogbWFyaWFkYjoxMVxuICAgIHJlc3RhcnQ6IGFsd2F5c1xuICAgIGNvbW1hbmQ6IC0tZGVmYXVsdC1hdXRoZW50aWNhdGlvbi1wbHVnaW49bXlzcWxfbmF0aXZlX3Bhc3N3b3JkXG4gICAgdm9sdW1lczpcbiAgICAgIC0gXCJwdGVyb2RiOi92YXIvbGliL215c3FsXCJcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIE1ZU1FMX0RBVEFCQVNFOiBcInBhbmVsXCJcbiAgICAgIE1ZU1FMX1VTRVI6IFwicHRlcm9kYWN0eWxcIlxuICAgICAgTVlTUUxfUEFTU1dPUkQ6XG4gICAgICBNWVNRTF9ST09UX1BBU1NXT1JEOlxuICBjYWNoZTpcbiAgICBpbWFnZTogcmVkaXM6YWxwaW5lXG4gICAgcmVzdGFydDogYWx3YXlzXG4gIHBhbmVsOlxuICAgIGltYWdlOiBnaGNyLmlvL3B5cm9kYWN0eWwtb3NzL3B5cm9kYWN0eWw6bGF0ZXN0XG4gICAgcmVzdGFydDogYWx3YXlzXG4gICAgbGlua3M6XG4gICAgICAtIGRhdGFiYXNlXG4gICAgICAtIGNhY2hlXG4gICAgdm9sdW1lczpcbiAgICAgIC0gXCJwdGVyb3ZhcjovYXBwL3Zhci9cIlxuICAgICAgLSBcInB0ZXJvbmdpbng6L2V0Yy9uZ2lueC9odHRwLmQvXCJcbiAgICAgIC0gXCJwdGVyb2NlcnRzOi9ldGMvbGV0c2VuY3J5cHQvXCJcbiAgICAgIC0gXCJwdGVyb2xvZ3M6L2FwcC9zdG9yYWdlL2xvZ3NcIlxuICAgIGVudmlyb25tZW50OlxuICAgICAgQVBQX1VSTDogXCJodHRwczovLyR7QVBQX0RPTUFJTn1cIlxuICAgICAgQVBQX0VOVjogXCJwcm9kdWN0aW9uXCJcbiAgICAgIEFQUF9FTlZJUk9OTUVOVF9PTkxZOiBcImZhbHNlXCJcbiAgICAgIENBQ0hFX0RSSVZFUjpcbiAgICAgIFNFU1NJT05fRFJJVkVSOlxuICAgICAgUVVFVUVfRFJJVkVSOlxuICAgICAgUkVESVNfSE9TVDpcbiAgICAgIERCX0hPU1Q6XG4gICAgICBEQl9QT1JUOlxuICAgICAgREJfUEFTU1dPUkQ6ICR7TVlTUUxfUEFTU1dPUkR9XG4gICAgICBEQl9DT05ORUNUSU9OOiBcIm1hcmlhZGJcIlxuXG52b2x1bWVzOlxuICBwdGVyb2RiOlxuICBwdGVyb3ZhcjpcbiAgcHRlcm9uZ2lueDpcbiAgcHRlcm9jZXJ0czpcbiAgcHRlcm9sb2dzOlxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbmRiX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5kYl9yb290X3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5zZWNyZXRfa2V5ID0gXCIke2Jhc2U2NDo0OH1cIlxuXG5bY29uZmlnXVxuZW52ID0gW1xuXCJEb21haW49JHttYWluX2RvbWFpbn1cIixcblwiUkVDQVBUQ0hBX0VOQUJMRUQ9dHJ1ZVwiLFxuXCJBUFBfRE9NQUlOPSR7bWFpbl9kb21haW59XCIsXG5cIkFQUF9USU1FWk9ORT1VVENcIixcblwiQVBQX1NFUlZJQ0VfQVVUSE9SPW5vcmVwbHlAZXhhbXBsZS5jb21cIixcblwiTUFJTF9GUk9NPW5vcmVwbHlAZXhhbXBsZS5jb21cIixcblwiTUFJTF9EUklWRVI9c210cFwiLFxuXCJNQUlMX0hPU1Q9bWFpbFwiLFxuXCJNQUlMX1BPUlQ9MTAyNVwiLFxuXCJNQUlMX1VTRVJOQU1FPVwiLFxuXCJNQUlMX1BBU1NXT1JEPVwiLFxuXCJNQUlMX0VOQ1JZUFRJT049dHJ1ZVwiLFxuXCJNWVNRTF9QQVNTV09SRD0ke2RiX3Bhc3N3b3JkfVwiLFxuXCJNWVNRTF9ST09UX1BBU1NXT1JEPSR7ZGJfcm9vdF9wYXNzd29yZH1cIixcblwiREJfUE9SVD0zMzA2XCIsXG5cIkNBQ0hFX0RSSVZFUj1yZWRpc1wiLFxuXCJTRVNTSU9OX0RSSVZFUj1yZWRpc1wiLFxuXCJRVUVVRV9EUklWRVI9cmVkaXNcIixcblwiUkVESVNfSE9TVD1jYWNoZVwiLFxuXCJEQl9IT1NUPWRhdGFiYXNlXCIsXG5dXG5tb3VudHMgPSBbXVxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJwYW5lbFwiXG5wb3J0ID0gODBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcbiIKfQ==
```

## Links

`self-hosted`,`open-source`,`management`

---

Version:`main`

PulseA responsive monitoring platform for Proxmox VE, PBS, and Docker with real-time metrics across nodes and containers.

qBittorrentA free and open-source BitTorrent client with web interface for remote management. Default login: admin (check container logs for temporary password on first startup).

### On this page

ConfigurationBase64LinksTags