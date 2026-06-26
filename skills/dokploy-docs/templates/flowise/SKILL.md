---
title: "Flowise | Dokploy"
source: "https://docs.dokploy.com/docs/templates/flowise"
category: dokploy-docs
created: "2026-06-25T17:21:47.359Z"
---

Flowise | Dokploy

# Flowise

Copy as Markdown

Flowise is an open-source UI visual tool to build and run LLM-powered applications.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  redis:
    image: redis:alpine
    restart: always
    volumes:
      - redis_data:/data

  flowise:
    image: flowiseai/flowise:latest
    restart: always
    expose:
      - 3000
    volumes:
      - flowise_data:/root/.flowise
    environment:
      PORT: 3000
      DATABASE_PATH: /root/.flowise
      REDIS_URL: redis://redis:6379
      JWT_AUTH_TOKEN_SECRET: ${JWT_AUTH_TOKEN_SECRET}
      JWT_REFRESH_TOKEN_SECRET: ${JWT_REFRESH_TOKEN_SECRET}
      EXPRESS_SESSION_SECRET: ${EXPRESS_SESSION_SECRET}
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000/api/v1/ping"]
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 30s
    entrypoint: /bin/sh -c "sleep 3; flowise start"
    depends_on:
      - redis

  flowise-worker:
    image: flowiseai/flowise-worker:latest
    restart: always
    volumes:
      - flowise_data:/root/.flowise
    environment:
      WORKER_PORT: 5566
      DATABASE_PATH: /root/.flowise
      REDIS_URL: redis://redis:6379
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:5566/healthz"]
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 30s
    entrypoint: /bin/sh -c "node /app/healthcheck/healthcheck.js & sleep 5 && pnpm run start-worker"
    depends_on:
      - redis
      - flowise

volumes:
  redis_data:
  flowise_data:
```

```
[variables]
main_domain = "${domain}"
jwt_secret = "${password:32}"
jwt_refresh_secret = "${password:32}"
express_secret = "${password:32}"

[config]
[[config.domains]]
serviceName = "flowise"
port = 3000
host = "${main_domain}"

[config.env]
JWT_AUTH_TOKEN_SECRET = "${jwt_secret}"
JWT_REFRESH_TOKEN_SECRET = "${jwt_refresh_secret}"
EXPRESS_SESSION_SECRET = "${express_secret}"

[[config.mounts]]
name = "flowise_data"
mountPath = "/root/.flowise"

[[config.mounts]]
name = "redis_data"
mountPath = "/data"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIHJlZGlzOlxuICAgIGltYWdlOiByZWRpczphbHBpbmVcbiAgICByZXN0YXJ0OiBhbHdheXNcbiAgICB2b2x1bWVzOlxuICAgICAgLSByZWRpc19kYXRhOi9kYXRhXG5cbiAgZmxvd2lzZTpcbiAgICBpbWFnZTogZmxvd2lzZWFpL2Zsb3dpc2U6bGF0ZXN0XG4gICAgcmVzdGFydDogYWx3YXlzXG4gICAgZXhwb3NlOlxuICAgICAgLSAzMDAwXG4gICAgdm9sdW1lczpcbiAgICAgIC0gZmxvd2lzZV9kYXRhOi9yb290Ly5mbG93aXNlXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBQT1JUOiAzMDAwXG4gICAgICBEQVRBQkFTRV9QQVRIOiAvcm9vdC8uZmxvd2lzZVxuICAgICAgUkVESVNfVVJMOiByZWRpczovL3JlZGlzOjYzNzlcbiAgICAgIEpXVF9BVVRIX1RPS0VOX1NFQ1JFVDogJHtKV1RfQVVUSF9UT0tFTl9TRUNSRVR9XG4gICAgICBKV1RfUkVGUkVTSF9UT0tFTl9TRUNSRVQ6ICR7SldUX1JFRlJFU0hfVE9LRU5fU0VDUkVUfVxuICAgICAgRVhQUkVTU19TRVNTSU9OX1NFQ1JFVDogJHtFWFBSRVNTX1NFU1NJT05fU0VDUkVUfVxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDogW1wiQ01EXCIsIFwiY3VybFwiLCBcIi1mXCIsIFwiaHR0cDovL2xvY2FsaG9zdDozMDAwL2FwaS92MS9waW5nXCJdXG4gICAgICBpbnRlcnZhbDogMTBzXG4gICAgICB0aW1lb3V0OiA1c1xuICAgICAgcmV0cmllczogNVxuICAgICAgc3RhcnRfcGVyaW9kOiAzMHNcbiAgICBlbnRyeXBvaW50OiAvYmluL3NoIC1jIFwic2xlZXAgMzsgZmxvd2lzZSBzdGFydFwiXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIC0gcmVkaXNcblxuICBmbG93aXNlLXdvcmtlcjpcbiAgICBpbWFnZTogZmxvd2lzZWFpL2Zsb3dpc2Utd29ya2VyOmxhdGVzdFxuICAgIHJlc3RhcnQ6IGFsd2F5c1xuICAgIHZvbHVtZXM6XG4gICAgICAtIGZsb3dpc2VfZGF0YTovcm9vdC8uZmxvd2lzZVxuICAgIGVudmlyb25tZW50OlxuICAgICAgV09SS0VSX1BPUlQ6IDU1NjZcbiAgICAgIERBVEFCQVNFX1BBVEg6IC9yb290Ly5mbG93aXNlXG4gICAgICBSRURJU19VUkw6IHJlZGlzOi8vcmVkaXM6NjM3OVxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDogW1wiQ01EXCIsIFwiY3VybFwiLCBcIi1mXCIsIFwiaHR0cDovL2xvY2FsaG9zdDo1NTY2L2hlYWx0aHpcIl1cbiAgICAgIGludGVydmFsOiAxMHNcbiAgICAgIHRpbWVvdXQ6IDVzXG4gICAgICByZXRyaWVzOiA1XG4gICAgICBzdGFydF9wZXJpb2Q6IDMwc1xuICAgIGVudHJ5cG9pbnQ6IC9iaW4vc2ggLWMgXCJub2RlIC9hcHAvaGVhbHRoY2hlY2svaGVhbHRoY2hlY2suanMgJiBzbGVlcCA1ICYmIHBucG0gcnVuIHN0YXJ0LXdvcmtlclwiXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIC0gcmVkaXNcbiAgICAgIC0gZmxvd2lzZVxuXG52b2x1bWVzOlxuICByZWRpc19kYXRhOlxuICBmbG93aXNlX2RhdGE6XG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuand0X3NlY3JldCA9IFwiJHtwYXNzd29yZDozMn1cIlxuand0X3JlZnJlc2hfc2VjcmV0ID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5leHByZXNzX3NlY3JldCA9IFwiJHtwYXNzd29yZDozMn1cIlxuXG5bY29uZmlnXVxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiZmxvd2lzZVwiXG5wb3J0ID0gMzAwMFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cbkpXVF9BVVRIX1RPS0VOX1NFQ1JFVCA9IFwiJHtqd3Rfc2VjcmV0fVwiXG5KV1RfUkVGUkVTSF9UT0tFTl9TRUNSRVQgPSBcIiR7and0X3JlZnJlc2hfc2VjcmV0fVwiXG5FWFBSRVNTX1NFU1NJT05fU0VDUkVUID0gXCIke2V4cHJlc3Nfc2VjcmV0fVwiXG5cbltbY29uZmlnLm1vdW50c11dXG5uYW1lID0gXCJmbG93aXNlX2RhdGFcIlxubW91bnRQYXRoID0gXCIvcm9vdC8uZmxvd2lzZVwiXG5cbltbY29uZmlnLm1vdW50c11dXG5uYW1lID0gXCJyZWRpc19kYXRhXCJcbm1vdW50UGF0aCA9IFwiL2RhdGFcIlxuIgp9
```

## Links

`AI`,`LLM`,`workflow`,`automation`

---

Version:`latest`

Flatnotes (TOTP)Flatnotes with TOTP authentication enabled (username + password + one-time passcode).

FMD ServerA server to communicate with the FMD Android app, to locate and control your devices.

### On this page

ConfigurationBase64LinksTags