---
title: "Mixpost | Dokploy"
source: "https://docs.dokploy.com/docs/templates/mixpost"
category: dokploy-docs
created: "2026-06-25T17:21:53.155Z"
---

Mixpost | Dokploy

# Mixpost

Copy as Markdown

Mixpost is an open-source social media management tool that allows you to create, schedule, and publish posts across multiple social media platforms from a single interface.

## Configuration

docker-compose.ymltemplate.toml

```
services:
    mixpost:
        image: inovector/mixpost:latest
        environment:
            APP_NAME: ${APP_NAME}
            APP_KEY: ${APP_KEY}
            APP_DEBUG: ${APP_DEBUG}
            APP_DOMAIN: ${APP_DOMAIN}
            APP_URL: ${APP_URL}
            DB_DATABASE: ${DB_DATABASE}
            DB_USERNAME: ${DB_USERNAME}
            DB_PASSWORD: ${DB_PASSWORD}
        volumes:
            - storage:/var/www/html/storage/app
            - logs:/var/www/html/storage/logs
        depends_on:
            - mysql
            - redis
        restart: unless-stopped
    mysql:
        image: 'mysql/mysql-server:8.0'
        environment:
            MYSQL_DATABASE: ${DB_DATABASE}
            MYSQL_USER: ${DB_USERNAME}
            MYSQL_PASSWORD: ${DB_PASSWORD}
        volumes:
            - 'mysql:/var/lib/mysql'
        healthcheck:
            test: ["CMD", "mysqladmin", "ping", "-p ${DB_PASSWORD}"]
            retries: 3
            timeout: 5s
        restart: unless-stopped
    redis:
        image: 'redis:latest'
        command: redis-server --appendonly yes --replica-read-only no
        volumes:
            - 'redis:/data'
        healthcheck:
            test: ["CMD", "redis-cli", "ping"]
            retries: 3
            timeout: 5s
        restart: unless-stopped

volumes:
    mysql: {}
    redis: {}
    storage: {}
    logs: {}
```

```
[variables]
main_domain = "${domain}"
mx_password = "${password:32}"

[config]
[[config.domains]]
serviceName = "mixpost"
port = 80
host = "${main_domain}"

[config.env]
APP_NAME="Mixpost"
APP_KEY="base64:ygtEUxD0fB3vUchihbUYqUzN57rfNi9ER5alJ98dWiA="
APP_DEBUG="false"
APP_DOMAIN="${main_domain}"
APP_URL="http://${APP_DOMAIN}"
DB_DATABASE="mixpost_db"
DB_USERNAME="mixpost_user"
DB_PASSWORD="${mx_password}"

[[config.mounts]]
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICAgIG1peHBvc3Q6XG4gICAgICAgIGltYWdlOiBpbm92ZWN0b3IvbWl4cG9zdDpsYXRlc3RcbiAgICAgICAgZW52aXJvbm1lbnQ6XG4gICAgICAgICAgICBBUFBfTkFNRTogJHtBUFBfTkFNRX1cbiAgICAgICAgICAgIEFQUF9LRVk6ICR7QVBQX0tFWX1cbiAgICAgICAgICAgIEFQUF9ERUJVRzogJHtBUFBfREVCVUd9XG4gICAgICAgICAgICBBUFBfRE9NQUlOOiAke0FQUF9ET01BSU59XG4gICAgICAgICAgICBBUFBfVVJMOiAke0FQUF9VUkx9XG4gICAgICAgICAgICBEQl9EQVRBQkFTRTogJHtEQl9EQVRBQkFTRX1cbiAgICAgICAgICAgIERCX1VTRVJOQU1FOiAke0RCX1VTRVJOQU1FfVxuICAgICAgICAgICAgREJfUEFTU1dPUkQ6ICR7REJfUEFTU1dPUkR9XG4gICAgICAgIHZvbHVtZXM6XG4gICAgICAgICAgICAtIHN0b3JhZ2U6L3Zhci93d3cvaHRtbC9zdG9yYWdlL2FwcFxuICAgICAgICAgICAgLSBsb2dzOi92YXIvd3d3L2h0bWwvc3RvcmFnZS9sb2dzXG4gICAgICAgIGRlcGVuZHNfb246XG4gICAgICAgICAgICAtIG15c3FsXG4gICAgICAgICAgICAtIHJlZGlzIFxuICAgICAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIG15c3FsOlxuICAgICAgICBpbWFnZTogJ215c3FsL215c3FsLXNlcnZlcjo4LjAnXG4gICAgICAgIGVudmlyb25tZW50OlxuICAgICAgICAgICAgTVlTUUxfREFUQUJBU0U6ICR7REJfREFUQUJBU0V9XG4gICAgICAgICAgICBNWVNRTF9VU0VSOiAke0RCX1VTRVJOQU1FfVxuICAgICAgICAgICAgTVlTUUxfUEFTU1dPUkQ6ICR7REJfUEFTU1dPUkR9XG4gICAgICAgIHZvbHVtZXM6XG4gICAgICAgICAgICAtICdteXNxbDovdmFyL2xpYi9teXNxbCdcbiAgICAgICAgaGVhbHRoY2hlY2s6XG4gICAgICAgICAgICB0ZXN0OiBbXCJDTURcIiwgXCJteXNxbGFkbWluXCIsIFwicGluZ1wiLCBcIi1wICR7REJfUEFTU1dPUkR9XCJdXG4gICAgICAgICAgICByZXRyaWVzOiAzXG4gICAgICAgICAgICB0aW1lb3V0OiA1c1xuICAgICAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIHJlZGlzOlxuICAgICAgICBpbWFnZTogJ3JlZGlzOmxhdGVzdCdcbiAgICAgICAgY29tbWFuZDogcmVkaXMtc2VydmVyIC0tYXBwZW5kb25seSB5ZXMgLS1yZXBsaWNhLXJlYWQtb25seSBub1xuICAgICAgICB2b2x1bWVzOlxuICAgICAgICAgICAgLSAncmVkaXM6L2RhdGEnXG4gICAgICAgIGhlYWx0aGNoZWNrOlxuICAgICAgICAgICAgdGVzdDogW1wiQ01EXCIsIFwicmVkaXMtY2xpXCIsIFwicGluZ1wiXVxuICAgICAgICAgICAgcmV0cmllczogM1xuICAgICAgICAgICAgdGltZW91dDogNXNcbiAgICAgICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWQgIFxuXG52b2x1bWVzOlxuICAgIG15c3FsOiB7fVxuICAgIHJlZGlzOiB7fVxuICAgIHN0b3JhZ2U6IHt9XG4gICAgbG9nczoge30iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxubXhfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcblxuW2NvbmZpZ11cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcIm1peHBvc3RcIlxucG9ydCA9IDgwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cblxuW2NvbmZpZy5lbnZdXG5BUFBfTkFNRT1cIk1peHBvc3RcIlxuQVBQX0tFWT1cImJhc2U2NDp5Z3RFVXhEMGZCM3ZVY2hpaGJVWXFVek41N3JmTmk5RVI1YWxKOThkV2lBPVwiXG5BUFBfREVCVUc9XCJmYWxzZVwiXG5BUFBfRE9NQUlOPVwiJHttYWluX2RvbWFpbn1cIlxuQVBQX1VSTD1cImh0dHA6Ly8ke0FQUF9ET01BSU59XCJcbkRCX0RBVEFCQVNFPVwibWl4cG9zdF9kYlwiXG5EQl9VU0VSTkFNRT1cIm1peHBvc3RfdXNlclwiXG5EQl9QQVNTV09SRD1cIiR7bXhfcGFzc3dvcmR9XCJcblxuXG5bW2NvbmZpZy5tb3VudHNdXVxuIgp9
```

## Links

`social-media`,`management`,`scheduling`

---

Version:`latest`

Misaka Danmu ServerA self-hosted danmaku (bullet comments) server for live streaming and video platforms.

MoltbotWhatsApp gateway CLI with Pi RPC agent - self-hosted AI-powered messaging platform

### On this page

ConfigurationBase64LinksTags