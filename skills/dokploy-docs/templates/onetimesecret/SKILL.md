---
title: "One Time Secret | Dokploy"
source: "https://docs.dokploy.com/docs/templates/onetimesecret"
category: dokploy-docs
created: "2026-06-25T17:21:54.355Z"
---

One Time Secret | Dokploy

# One Time Secret

Copy as Markdown

Share sensitive information securely with self-destructing links that are only viewable once.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  onetimesecret-redis:
    image: redis:7-alpine
    command: redis-server --requirepass ${REDIS_PASSWORD}
    restart: unless-stopped
    healthcheck:
      test:
        - CMD
        - redis-cli
        - ping
      interval: 30s
      timeout: 10s
      retries: 3

  onetimesecret:
    image: 'onetimesecret/onetimesecret:latest'
    restart: unless-stopped
    environment:
      # To see all available environment variables, visit:
      # https://github.com/onetimesecret/onetimesecret/blob/develop/etc/config.example.yaml
      - AUTH_AUTOVERIFY=true
      - AUTH_SIGNUP=true

      # Accounts created with this email address will have admin access
      - COLONEL=${COLONEL}

      # If you change your domain, make sure to update the HOST environment variable.
      - HOST=${HOST}

      - RACK_ENV=production
      - REDIS_URL=redis://:${REDIS_PASSWORD}@onetimesecret-redis:6379/0
      - SECRET=${SECRET}
      - SSL=true
    depends_on:
      - onetimesecret-redis
    healthcheck:
      test:
        - CMD
        - ruby
        - '-rnet/http'
        - '-e'
        - "exit(Net::HTTP.get_response(URI('http://localhost:3000')).is_a?(Net::HTTPSuccess) ? 0 : 1)"
      interval: 30s
      timeout: 10s
      retries: 3
```

```
[variables]
main_domain = "${domain}"
secret = "${password:30}"
redis_password = "${password:30}"

[[config.domains]]
serviceName = "onetimesecret"
port = 3000
host = "${main_domain}"

[config.env]
COLONEL="[email protected]"
HOST="${main_domain}"
REDIS_PASSWORD = "${redis_password}"
SECRET="${secret}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBvbmV0aW1lc2VjcmV0LXJlZGlzOlxuICAgIGltYWdlOiByZWRpczo3LWFscGluZVxuICAgIGNvbW1hbmQ6IHJlZGlzLXNlcnZlciAtLXJlcXVpcmVwYXNzICR7UkVESVNfUEFTU1dPUkR9XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6XG4gICAgICAgIC0gQ01EXG4gICAgICAgIC0gcmVkaXMtY2xpXG4gICAgICAgIC0gcGluZ1xuICAgICAgaW50ZXJ2YWw6IDMwc1xuICAgICAgdGltZW91dDogMTBzXG4gICAgICByZXRyaWVzOiAzXG5cbiAgb25ldGltZXNlY3JldDpcbiAgICBpbWFnZTogJ29uZXRpbWVzZWNyZXQvb25ldGltZXNlY3JldDpsYXRlc3QnXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgICMgVG8gc2VlIGFsbCBhdmFpbGFibGUgZW52aXJvbm1lbnQgdmFyaWFibGVzLCB2aXNpdDpcbiAgICAgICMgaHR0cHM6Ly9naXRodWIuY29tL29uZXRpbWVzZWNyZXQvb25ldGltZXNlY3JldC9ibG9iL2RldmVsb3AvZXRjL2NvbmZpZy5leGFtcGxlLnlhbWxcbiAgICAgIC0gQVVUSF9BVVRPVkVSSUZZPXRydWVcbiAgICAgIC0gQVVUSF9TSUdOVVA9dHJ1ZVxuXG4gICAgICAjIEFjY291bnRzIGNyZWF0ZWQgd2l0aCB0aGlzIGVtYWlsIGFkZHJlc3Mgd2lsbCBoYXZlIGFkbWluIGFjY2Vzc1xuICAgICAgLSBDT0xPTkVMPSR7Q09MT05FTH1cblxuICAgICAgIyBJZiB5b3UgY2hhbmdlIHlvdXIgZG9tYWluLCBtYWtlIHN1cmUgdG8gdXBkYXRlIHRoZSBIT1NUIGVudmlyb25tZW50IHZhcmlhYmxlLlxuICAgICAgLSBIT1NUPSR7SE9TVH1cblxuICAgICAgLSBSQUNLX0VOVj1wcm9kdWN0aW9uXG4gICAgICAtIFJFRElTX1VSTD1yZWRpczovLzoke1JFRElTX1BBU1NXT1JEfUBvbmV0aW1lc2VjcmV0LXJlZGlzOjYzNzkvMFxuICAgICAgLSBTRUNSRVQ9JHtTRUNSRVR9XG4gICAgICAtIFNTTD10cnVlXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIC0gb25ldGltZXNlY3JldC1yZWRpc1xuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDpcbiAgICAgICAgLSBDTURcbiAgICAgICAgLSBydWJ5XG4gICAgICAgIC0gJy1ybmV0L2h0dHAnXG4gICAgICAgIC0gJy1lJ1xuICAgICAgICAtIFwiZXhpdChOZXQ6OkhUVFAuZ2V0X3Jlc3BvbnNlKFVSSSgnaHR0cDovL2xvY2FsaG9zdDozMDAwJykpLmlzX2E/KE5ldDo6SFRUUFN1Y2Nlc3MpID8gMCA6IDEpXCJcbiAgICAgIGludGVydmFsOiAzMHNcbiAgICAgIHRpbWVvdXQ6IDEwc1xuICAgICAgcmV0cmllczogM1xuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbnNlY3JldCA9IFwiJHtwYXNzd29yZDozMH1cIlxucmVkaXNfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MzB9XCJcblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwib25ldGltZXNlY3JldFwiXG5wb3J0ID0gMzAwMFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cbkNPTE9ORUw9XCJhZG1pbkBleGFtcGxlLmNvbVwiXG5IT1NUPVwiJHttYWluX2RvbWFpbn1cIlxuUkVESVNfUEFTU1dPUkQgPSBcIiR7cmVkaXNfcGFzc3dvcmR9XCJcblNFQ1JFVD1cIiR7c2VjcmV0fVwiXG4iCn0=
```

## Links

`auth`,`password`,`secret`,`secure`

---

Version:`latest`

OneDevGit server with CI/CD, kanban, and packages. Seamless integration. Unparalleled experience.

OntimeOntime is browser-based application that manages event rundowns, scheduliing and cuing

### On this page

ConfigurationBase64LinksTags