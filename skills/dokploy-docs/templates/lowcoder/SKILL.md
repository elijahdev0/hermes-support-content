---
title: "Lowcoder | Dokploy"
source: "https://docs.dokploy.com/docs/templates/lowcoder"
category: dokploy-docs
created: "2026-06-25T17:21:52.046Z"
---

Lowcoder | Dokploy

# Lowcoder

Copy as Markdown

Rapid business App Builder for Everyone

## Configuration

docker-compose.ymltemplate.toml

```
version: "3"

services:
  ## Start Lowcoder (all-in-one)
  lowcoder-api-service:
    image: lowcoderorg/lowcoder-ce:2.6.4
    environment:
      REDIS_ENABLED: "true"
      MONGODB_ENABLED: "true"
      API_SERVICE_ENABLED: "true"
      NODE_SERVICE_ENABLED: "true"
      FRONTEND_ENABLED: "true"
      PUID: "1000"
      PGID: "1000"
      DEFAULT_ORGS_PER_USER: 100
      DEFAULT_ORG_MEMBER_COUNT: 1000
      DEFAULT_ORG_GROUP_COUNT: 100
      DEFAULT_ORG_APP_COUNT: 1000
      DEFAULT_DEVELOPER_COUNT: 50
      MONGODB_URL: "mongodb://localhost:27017/lowcoder?authSource=admin"
      REDIS_URL: "redis://localhost:6379"
      ENABLE_USER_SIGN_UP: ${ENABLE_USER_SIGN_UP}
      ENCRYPTION_PASSWORD: ${ENCRYPTION_PASSWORD}
      ENCRYPTION_SALT: ${ENCRYPTION_SALT}
      CORS_ALLOWED_DOMAINS: ${CORS_ALLOWED_DOMAINS}
      LOWCODER_API_KEY_SECRET: ${LOWCODER_API_KEY_SECRET}
      LOWCODER_API_SERVICE_URL: "http://localhost:8080"
      LOWCODER_NODE_SERVICE_URL: "http://localhost:6060"
    volumes:
      - ../files/volumes/lowcoder-stacks:/lowcoder-stacks
    restart: unless-stopped
    expose:
      - 3000
```

```
[variables]
main_domain = "${domain}"
encryption_password = "${password:32}"
encryption_salt = "${password:32}"
api_secret = "${password:32}"

[config]
[[config.domains]]
serviceName = "lowcoder-api-service"
port = 3000
host = "${main_domain}"

[config.env]
ENABLE_USER_SIGN_UP = false
ENCRYPTION_PASSWORD = "${encryption_password}"
ENCRYPTION_SALT = "${encryption_salt}"
CORS_ALLOWED_DOMAINS = "*"
LOWCODER_API_KEY_SECRET = "${api_secret}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiM1wiXG5cbnNlcnZpY2VzOlxuICAjIyBTdGFydCBMb3djb2RlciAoYWxsLWluLW9uZSlcbiAgbG93Y29kZXItYXBpLXNlcnZpY2U6XG4gICAgaW1hZ2U6IGxvd2NvZGVyb3JnL2xvd2NvZGVyLWNlOjIuNi40XG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBSRURJU19FTkFCTEVEOiBcInRydWVcIlxuICAgICAgTU9OR09EQl9FTkFCTEVEOiBcInRydWVcIlxuICAgICAgQVBJX1NFUlZJQ0VfRU5BQkxFRDogXCJ0cnVlXCJcbiAgICAgIE5PREVfU0VSVklDRV9FTkFCTEVEOiBcInRydWVcIlxuICAgICAgRlJPTlRFTkRfRU5BQkxFRDogXCJ0cnVlXCJcbiAgICAgIFBVSUQ6IFwiMTAwMFwiXG4gICAgICBQR0lEOiBcIjEwMDBcIlxuICAgICAgREVGQVVMVF9PUkdTX1BFUl9VU0VSOiAxMDBcbiAgICAgIERFRkFVTFRfT1JHX01FTUJFUl9DT1VOVDogMTAwMFxuICAgICAgREVGQVVMVF9PUkdfR1JPVVBfQ09VTlQ6IDEwMFxuICAgICAgREVGQVVMVF9PUkdfQVBQX0NPVU5UOiAxMDAwXG4gICAgICBERUZBVUxUX0RFVkVMT1BFUl9DT1VOVDogNTBcbiAgICAgIE1PTkdPREJfVVJMOiBcIm1vbmdvZGI6Ly9sb2NhbGhvc3Q6MjcwMTcvbG93Y29kZXI/YXV0aFNvdXJjZT1hZG1pblwiXG4gICAgICBSRURJU19VUkw6IFwicmVkaXM6Ly9sb2NhbGhvc3Q6NjM3OVwiXG4gICAgICBFTkFCTEVfVVNFUl9TSUdOX1VQOiAke0VOQUJMRV9VU0VSX1NJR05fVVB9XG4gICAgICBFTkNSWVBUSU9OX1BBU1NXT1JEOiAke0VOQ1JZUFRJT05fUEFTU1dPUkR9XG4gICAgICBFTkNSWVBUSU9OX1NBTFQ6ICR7RU5DUllQVElPTl9TQUxUfVxuICAgICAgQ09SU19BTExPV0VEX0RPTUFJTlM6ICR7Q09SU19BTExPV0VEX0RPTUFJTlN9XG4gICAgICBMT1dDT0RFUl9BUElfS0VZX1NFQ1JFVDogJHtMT1dDT0RFUl9BUElfS0VZX1NFQ1JFVH1cbiAgICAgIExPV0NPREVSX0FQSV9TRVJWSUNFX1VSTDogXCJodHRwOi8vbG9jYWxob3N0OjgwODBcIlxuICAgICAgTE9XQ09ERVJfTk9ERV9TRVJWSUNFX1VSTDogXCJodHRwOi8vbG9jYWxob3N0OjYwNjBcIlxuICAgIHZvbHVtZXM6XG4gICAgICAtIC4uL2ZpbGVzL3ZvbHVtZXMvbG93Y29kZXItc3RhY2tzOi9sb3djb2Rlci1zdGFja3NcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGV4cG9zZTogXG4gICAgICAtIDMwMDBcbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5lbmNyeXB0aW9uX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5lbmNyeXB0aW9uX3NhbHQgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcbmFwaV9zZWNyZXQgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcblxuW2NvbmZpZ11cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImxvd2NvZGVyLWFwaS1zZXJ2aWNlXCJcbnBvcnQgPSAzMDAwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuRU5BQkxFX1VTRVJfU0lHTl9VUCA9IGZhbHNlXG5FTkNSWVBUSU9OX1BBU1NXT1JEID0gXCIke2VuY3J5cHRpb25fcGFzc3dvcmR9XCJcbkVOQ1JZUFRJT05fU0FMVCA9IFwiJHtlbmNyeXB0aW9uX3NhbHR9XCJcbkNPUlNfQUxMT1dFRF9ET01BSU5TID0gXCIqXCJcbkxPV0NPREVSX0FQSV9LRVlfU0VDUkVUID0gXCIke2FwaV9zZWNyZXR9XCJcbiIKfQ==
```

## Links

`low-code`,`no-code`,`development`

---

Version:`2.6.4`

LogtoLogto is an open-source Identity and Access Management (IAM) platform designed to streamline Customer Identity and Access Management (CIAM) and Workforce Identity Management.

MacOS (dockerized)MacOS inside a Docker container.

### On this page

ConfigurationBase64LinksTags