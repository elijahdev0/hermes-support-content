---
title: "Checkmate | Dokploy"
source: "https://docs.dokploy.com/docs/templates/checkmate"
category: dokploy-docs
created: "2026-06-25T17:21:43.962Z"
---

Checkmate | Dokploy

# Checkmate

Copy as Markdown

Checkmate is an open-source, self-hosted tool designed to track and monitor server hardware, uptime, response times, and incidents in real-time with beautiful visualizations.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  server:
    image: ghcr.io/bluewave-labs/checkmate-backend-mono:latest
    restart: always
    ports:
      - 52345
    environment:
      - UPTIME_APP_API_BASE_URL=${UPTIME_APP_API_BASE_URL}
      - UPTIME_APP_CLIENT_HOST=${UPTIME_APP_CLIENT_HOST}
      - DB_CONNECTION_STRING=${DB_CONNECTION_STRING}
      - REDIS_URL=${REDIS_URL}
      - CLIENT_HOST=${CLIENT_HOST}
      - JWT_SECRET=${JWT_SECRET}
    depends_on:
      - mongodb
  mongodb:
    image: ghcr.io/bluewave-labs/checkmate-mongo:latest
    restart: always
    command: ["mongod", "--quiet", "--replSet", "rs0", "--bind_ip_all"]
    volumes:
      - ../files/mongo-data:/data/db
    healthcheck:
      test: echo "try { rs.status() } catch (err) { rs.initiate({_id:'rs0',members:[{_id:0,host:'mongodb:27017'}]}) }" | mongosh --port 27017 --quiet
      interval: 5s
      timeout: 30s
      start_period: 0s
      start_interval: 1s
      retries: 30
```

```
[variables]
main_domain = "${domain}"
jwt_secret = "${password:32}"

[config]
[[config.domains]]
serviceName = "server"
port = 52345
host = "${main_domain}"

[config.env]
UPTIME_APP_API_BASE_URL = "http://${main_domain}:52345/api/v1"
UPTIME_APP_CLIENT_HOST = "http://${main_domain}"
DB_CONNECTION_STRING = "mongodb://mongodb:27017/uptime_db?replicaSet=rs0"
REDIS_URL = "redis://redis:6379"
CLIENT_HOST = "http://${main_domain}"
JWT_SECRET = "${jwt_secret}" # API key for JWT authentication

[[config.mounts]]
filePath = "/files/mongo-data"
content = ""
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBzZXJ2ZXI6XG4gICAgaW1hZ2U6IGdoY3IuaW8vYmx1ZXdhdmUtbGFicy9jaGVja21hdGUtYmFja2VuZC1tb25vOmxhdGVzdFxuICAgIHJlc3RhcnQ6IGFsd2F5c1xuICAgIHBvcnRzOlxuICAgICAgLSA1MjM0NVxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBVUFRJTUVfQVBQX0FQSV9CQVNFX1VSTD0ke1VQVElNRV9BUFBfQVBJX0JBU0VfVVJMfVxuICAgICAgLSBVUFRJTUVfQVBQX0NMSUVOVF9IT1NUPSR7VVBUSU1FX0FQUF9DTElFTlRfSE9TVH1cbiAgICAgIC0gREJfQ09OTkVDVElPTl9TVFJJTkc9JHtEQl9DT05ORUNUSU9OX1NUUklOR31cbiAgICAgIC0gUkVESVNfVVJMPSR7UkVESVNfVVJMfVxuICAgICAgLSBDTElFTlRfSE9TVD0ke0NMSUVOVF9IT1NUfVxuICAgICAgLSBKV1RfU0VDUkVUPSR7SldUX1NFQ1JFVH1cbiAgICBkZXBlbmRzX29uOlxuICAgICAgLSBtb25nb2RiXG4gIG1vbmdvZGI6XG4gICAgaW1hZ2U6IGdoY3IuaW8vYmx1ZXdhdmUtbGFicy9jaGVja21hdGUtbW9uZ286bGF0ZXN0XG4gICAgcmVzdGFydDogYWx3YXlzXG4gICAgY29tbWFuZDogW1wibW9uZ29kXCIsIFwiLS1xdWlldFwiLCBcIi0tcmVwbFNldFwiLCBcInJzMFwiLCBcIi0tYmluZF9pcF9hbGxcIl1cbiAgICB2b2x1bWVzOlxuICAgICAgLSAuLi9maWxlcy9tb25nby1kYXRhOi9kYXRhL2RiXG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OiBlY2hvIFwidHJ5IHsgcnMuc3RhdHVzKCkgfSBjYXRjaCAoZXJyKSB7IHJzLmluaXRpYXRlKHtfaWQ6J3JzMCcsbWVtYmVyczpbe19pZDowLGhvc3Q6J21vbmdvZGI6MjcwMTcnfV19KSB9XCIgfCBtb25nb3NoIC0tcG9ydCAyNzAxNyAtLXF1aWV0XG4gICAgICBpbnRlcnZhbDogNXNcbiAgICAgIHRpbWVvdXQ6IDMwc1xuICAgICAgc3RhcnRfcGVyaW9kOiAwc1xuICAgICAgc3RhcnRfaW50ZXJ2YWw6IDFzXG4gICAgICByZXRyaWVzOiAzMFxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbmp3dF9zZWNyZXQgPSBcIiR7cGFzc3dvcmQ6MzJ9XCIgXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJzZXJ2ZXJcIlxucG9ydCA9IDUyMzQ1XG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuVVBUSU1FX0FQUF9BUElfQkFTRV9VUkwgPSBcImh0dHA6Ly8ke21haW5fZG9tYWlufTo1MjM0NS9hcGkvdjFcIlxuVVBUSU1FX0FQUF9DTElFTlRfSE9TVCA9IFwiaHR0cDovLyR7bWFpbl9kb21haW59XCJcbkRCX0NPTk5FQ1RJT05fU1RSSU5HID0gXCJtb25nb2RiOi8vbW9uZ29kYjoyNzAxNy91cHRpbWVfZGI/cmVwbGljYVNldD1yczBcIlxuUkVESVNfVVJMID0gXCJyZWRpczovL3JlZGlzOjYzNzlcIlxuQ0xJRU5UX0hPU1QgPSBcImh0dHA6Ly8ke21haW5fZG9tYWlufVwiXG5KV1RfU0VDUkVUID0gXCIke2p3dF9zZWNyZXR9XCIgIyBBUEkga2V5IGZvciBKV1QgYXV0aGVudGljYXRpb25cblxuW1tjb25maWcubW91bnRzXV1cbmZpbGVQYXRoID0gXCIvZmlsZXMvbW9uZ28tZGF0YVwiXG5jb250ZW50ID0gXCJcIiIKfQ==
```

## Links

`self-hosted`,`monitoring`,`uptime`

---

Version:`latest`

CheckcleCheckcle is a security and compliance tool by Operacle, providing insights into system configuration and runtime checks.

CheveretoChevereto is a powerful, self-hosted image and video hosting platform designed for individuals, communities, and businesses. It allows users to upload, organize, and share media effortlessly.

### On this page

ConfigurationBase64LinksTags