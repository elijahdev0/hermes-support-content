---
title: "Pterodactyl | Dokploy"
source: "https://docs.dokploy.com/docs/templates/pterodactyl"
category: dokploy-docs
created: "2026-06-25T17:21:57.937Z"
---

Pterodactyl | Dokploy

# Pterodactyl

Copy as Markdown

A free, open-source game server management panel.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  database:
    image: mariadb:10.5
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
    image: ghcr.io/pterodactyl/panel:latest
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
      APP_ENV: "production"
      APP_ENVIRONMENT_ONLY: "false"
      CACHE_DRIVER:
      SESSION_DRIVER:
      QUEUE_DRIVER:
      REDIS_HOST:
      DB_HOST:
      DB_PASSWORD: ${MYSQL_PASSWORD}
      DB_PORT:
      MYSQL_PASSWORD:
      MYSQL_ROOT_PASSWORD:
      DB_CONNECTION: "mysql"

networks:
  default:
    ipam:
      config:
        - subnet: 172.20.0.0/16

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
"APP_URL={$main_domain}",
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
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBkYXRhYmFzZTpcbiAgICBpbWFnZTogbWFyaWFkYjoxMC41XG4gICAgcmVzdGFydDogYWx3YXlzXG4gICAgY29tbWFuZDogLS1kZWZhdWx0LWF1dGhlbnRpY2F0aW9uLXBsdWdpbj1teXNxbF9uYXRpdmVfcGFzc3dvcmRcbiAgICB2b2x1bWVzOlxuICAgICAgLSBcInB0ZXJvZGI6L3Zhci9saWIvbXlzcWxcIlxuICAgIGVudmlyb25tZW50OlxuICAgICAgTVlTUUxfREFUQUJBU0U6IFwicGFuZWxcIlxuICAgICAgTVlTUUxfVVNFUjogXCJwdGVyb2RhY3R5bFwiXG4gICAgICBNWVNRTF9QQVNTV09SRDpcbiAgICAgIE1ZU1FMX1JPT1RfUEFTU1dPUkQ6XG4gIGNhY2hlOlxuICAgIGltYWdlOiByZWRpczphbHBpbmVcbiAgICByZXN0YXJ0OiBhbHdheXNcbiAgcGFuZWw6XG4gICAgaW1hZ2U6IGdoY3IuaW8vcHRlcm9kYWN0eWwvcGFuZWw6bGF0ZXN0XG4gICAgcmVzdGFydDogYWx3YXlzXG4gICAgbGlua3M6XG4gICAgICAtIGRhdGFiYXNlXG4gICAgICAtIGNhY2hlXG4gICAgdm9sdW1lczpcbiAgICAgIC0gXCJwdGVyb3ZhcjovYXBwL3Zhci9cIlxuICAgICAgLSBcInB0ZXJvbmdpbng6L2V0Yy9uZ2lueC9odHRwLmQvXCJcbiAgICAgIC0gXCJwdGVyb2NlcnRzOi9ldGMvbGV0c2VuY3J5cHQvXCJcbiAgICAgIC0gXCJwdGVyb2xvZ3M6L2FwcC9zdG9yYWdlL2xvZ3NcIlxuICAgIGVudmlyb25tZW50OlxuICAgICAgQVBQX0VOVjogXCJwcm9kdWN0aW9uXCJcbiAgICAgIEFQUF9FTlZJUk9OTUVOVF9PTkxZOiBcImZhbHNlXCJcbiAgICAgIENBQ0hFX0RSSVZFUjpcbiAgICAgIFNFU1NJT05fRFJJVkVSOlxuICAgICAgUVVFVUVfRFJJVkVSOlxuICAgICAgUkVESVNfSE9TVDpcbiAgICAgIERCX0hPU1Q6XG4gICAgICBEQl9QQVNTV09SRDogJHtNWVNRTF9QQVNTV09SRH1cbiAgICAgIERCX1BPUlQ6XG4gICAgICBNWVNRTF9QQVNTV09SRDpcbiAgICAgIE1ZU1FMX1JPT1RfUEFTU1dPUkQ6XG4gICAgICBEQl9DT05ORUNUSU9OOiBcIm15c3FsXCJcblxubmV0d29ya3M6XG4gIGRlZmF1bHQ6XG4gICAgaXBhbTpcbiAgICAgIGNvbmZpZzpcbiAgICAgICAgLSBzdWJuZXQ6IDE3Mi4yMC4wLjAvMTZcblxudm9sdW1lczpcbiAgcHRlcm9kYjpcbiAgcHRlcm92YXI6XG4gIHB0ZXJvbmdpbng6XG4gIHB0ZXJvY2VydHM6XG4gIHB0ZXJvbG9nczpcbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5kYl9wYXNzd29yZCA9IFwiJHtwYXNzd29yZDozMn1cIlxuZGJfcm9vdF9wYXNzd29yZCA9IFwiJHtwYXNzd29yZDozMn1cIlxuc2VjcmV0X2tleSA9IFwiJHtiYXNlNjQ6NDh9XCJcblxuW2NvbmZpZ11cbmVudiA9IFtcblwiRG9tYWluPSR7bWFpbl9kb21haW59XCIsXG5cIkFQUF9VUkw9eyRtYWluX2RvbWFpbn1cIixcblwiQVBQX1RJTUVaT05FPVVUQ1wiLFxuXCJBUFBfU0VSVklDRV9BVVRIT1I9bm9yZXBseUBleGFtcGxlLmNvbVwiLFxuXCJNQUlMX0ZST009bm9yZXBseUBleGFtcGxlLmNvbVwiLFxuXCJNQUlMX0RSSVZFUj1zbXRwXCIsXG5cIk1BSUxfSE9TVD1tYWlsXCIsXG5cIk1BSUxfUE9SVD0xMDI1XCIsXG5cIk1BSUxfVVNFUk5BTUU9XCIsXG5cIk1BSUxfUEFTU1dPUkQ9XCIsXG5cIk1BSUxfRU5DUllQVElPTj10cnVlXCIsXG5cIk1ZU1FMX1BBU1NXT1JEPSR7ZGJfcGFzc3dvcmR9XCIsXG5cIk1ZU1FMX1JPT1RfUEFTU1dPUkQ9JHtkYl9yb290X3Bhc3N3b3JkfVwiLFxuXCJEQl9QT1JUPTMzMDZcIixcblwiQ0FDSEVfRFJJVkVSPXJlZGlzXCIsXG5cIlNFU1NJT05fRFJJVkVSPXJlZGlzXCIsXG5cIlFVRVVFX0RSSVZFUj1yZWRpc1wiLFxuXCJSRURJU19IT1NUPWNhY2hlXCIsXG5cIkRCX0hPU1Q9ZGF0YWJhc2VcIixcbl1cbm1vdW50cyA9IFtdXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcInBhbmVsXCJcbnBvcnQgPSA4MFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuIgp9
```

## Links

`self-hosted`,`open-source`,`management`

---

Version:`latest`

PrometheusPrometheus is an open-source monitoring and alerting toolkit designed for reliability and scalability.

PulseA responsive monitoring platform for Proxmox VE, PBS, and Docker with real-time metrics across nodes and containers.

### On this page

ConfigurationBase64LinksTags