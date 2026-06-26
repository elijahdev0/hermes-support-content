---
title: "ByteStash | Dokploy"
source: "https://docs.dokploy.com/docs/templates/bytestash"
category: dokploy-docs
created: "2026-06-25T17:21:42.677Z"
---

ByteStash | Dokploy

# ByteStash

Copy as Markdown

ByteStash is a self-hosted web application designed to store, organise, and manage your code snippets efficiently. With support for creating, editing, and filtering snippets, ByteStash helps you keep track of your code in one secure place.

## Configuration

docker-compose.ymltemplate.toml

```
version: '3.8'

services:
  bytestash:
    image: ghcr.io/jordan-dalby/bytestash:1.5.6
    restart: unless-stopped
    ports:
      - "5000"
    environment:
      - BASE_PATH=
      - JWT_SECRET=${JWT_SECRET}
      - TOKEN_EXPIRY=24h
      - ALLOW_NEW_ACCOUNTS=true
      - DEBUG=true
      - DISABLE_ACCOUNTS=false
      - DISABLE_INTERNAL_ACCOUNTS=false
      - OIDC_ENABLED=false
      - OIDC_DISPLAY_NAME=
      - OIDC_ISSUER_URL=
      - OIDC_CLIENT_ID=
      - OIDC_CLIENT_SECRET=
      - OIDC_SCOPES=
    volumes:
      - snippets:/data/snippets

volumes:
  snippets:
```

```
[variables]
jwt_secret = "${password:32}"

[config]
[[config.domains]]
serviceName = "bytestash"
port = 5000
host = "${domain}"

[config.env]
JWT_SECRET = "${jwt_secret}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246ICczLjgnXG5cbnNlcnZpY2VzOlxuICBieXRlc3Rhc2g6XG4gICAgaW1hZ2U6IGdoY3IuaW8vam9yZGFuLWRhbGJ5L2J5dGVzdGFzaDoxLjUuNlxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgcG9ydHM6XG4gICAgICAtIFwiNTAwMFwiXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIEJBU0VfUEFUSD1cbiAgICAgIC0gSldUX1NFQ1JFVD0ke0pXVF9TRUNSRVR9XG4gICAgICAtIFRPS0VOX0VYUElSWT0yNGhcbiAgICAgIC0gQUxMT1dfTkVXX0FDQ09VTlRTPXRydWVcbiAgICAgIC0gREVCVUc9dHJ1ZVxuICAgICAgLSBESVNBQkxFX0FDQ09VTlRTPWZhbHNlXG4gICAgICAtIERJU0FCTEVfSU5URVJOQUxfQUNDT1VOVFM9ZmFsc2VcbiAgICAgIC0gT0lEQ19FTkFCTEVEPWZhbHNlXG4gICAgICAtIE9JRENfRElTUExBWV9OQU1FPVxuICAgICAgLSBPSURDX0lTU1VFUl9VUkw9XG4gICAgICAtIE9JRENfQ0xJRU5UX0lEPVxuICAgICAgLSBPSURDX0NMSUVOVF9TRUNSRVQ9XG4gICAgICAtIE9JRENfU0NPUEVTPVxuICAgIHZvbHVtZXM6XG4gICAgICAtIHNuaXBwZXRzOi9kYXRhL3NuaXBwZXRzXG5cbnZvbHVtZXM6XG4gIHNuaXBwZXRzOiAiLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbmp3dF9zZWNyZXQgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcblxuW2NvbmZpZ11cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImJ5dGVzdGFzaFwiXG5wb3J0ID0gNTAwMFxuaG9zdCA9IFwiJHtkb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5KV1RfU0VDUkVUID0gXCIke2p3dF9zZWNyZXR9XCIiCn0=
```

## Links

`file-storage`,`self-hosted`

---

Version:`latest`

BytebaseBytebase is a database management tool that allows you to manage your databases with ease. It provides a simple and effective solution for managing your databases from anywhere.

CalcomCalcom is a open source alternative to Calendly that allows to create scheduling and booking services.

### On this page

ConfigurationBase64LinksTags