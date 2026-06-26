---
title: "Blinko | Dokploy"
source: "https://docs.dokploy.com/docs/templates/blinko"
category: dokploy-docs
created: "2026-06-25T17:21:42.676Z"
---

Blinko | Dokploy

# Blinko

Copy as Markdown

Blinko is a modern web application for managing and organizing your digital content and workflows.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  blinko-website:
    image: blinkospace/blinko:1.6.3
    environment:
      NODE_ENV: production
      # API Key for NextAuth
      NEXTAUTH_SECRET: ${NEXTAUTH_SECRET}
      DATABASE_URL: ${DATABASE_URL}
      NEXTAUTH_URL: ${NEXTAUTH_URL}
      NEXT_PUBLIC_BASE_URL: ${NEXT_PUBLIC_BASE_URL}
    depends_on:
      blinko-postgres:
        condition: service_healthy
    restart: always
    logging:
      options:
        max-size: "10m"
        max-file: "3"
    ports:
      - 1111

  blinko-postgres:
    image: postgres:14
    restart: always
    environment:
      POSTGRES_DB: postgres
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      TZ: Asia/Shanghai
    volumes:
      - blinko-db:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD", "pg_isready", "-U", "postgres", "-d", "postgres"]
      interval: 5s
      timeout: 10s
      retries: 5

volumes:
  blinko-db: {}
```

```
[variables]
main_domain = "${domain}"
postgres_password = "${password:32}"
nextauth_secret = "${password:32}"
database_url = "postgresql://postgres:${postgres_password}@blinko-postgres:5432/postgres"
nextauth_url = "http://${main_domain}"
next_public_base_url = "http://${main_domain}"

[config]
[[config.domains]]
serviceName = "blinko-website"
port = 1111
host = "${main_domain}"

[config.env]
NEXTAUTH_SECRET = "${nextauth_secret}"
POSTGRES_PASSWORD = "${postgres_password}"
DATABASE_URL = "${database_url}"
NEXTAUTH_URL = "${nextauth_url}"
NEXT_PUBLIC_BASE_URL = "${next_public_base_url}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBibGlua28td2Vic2l0ZTpcbiAgICBpbWFnZTogYmxpbmtvc3BhY2UvYmxpbmtvOjEuNi4zXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBOT0RFX0VOVjogcHJvZHVjdGlvblxuICAgICAgIyBBUEkgS2V5IGZvciBOZXh0QXV0aFxuICAgICAgTkVYVEFVVEhfU0VDUkVUOiAke05FWFRBVVRIX1NFQ1JFVH1cbiAgICAgIERBVEFCQVNFX1VSTDogJHtEQVRBQkFTRV9VUkx9XG4gICAgICBORVhUQVVUSF9VUkw6ICR7TkVYVEFVVEhfVVJMfVxuICAgICAgTkVYVF9QVUJMSUNfQkFTRV9VUkw6ICR7TkVYVF9QVUJMSUNfQkFTRV9VUkx9XG4gICAgZGVwZW5kc19vbjpcbiAgICAgIGJsaW5rby1wb3N0Z3JlczpcbiAgICAgICAgY29uZGl0aW9uOiBzZXJ2aWNlX2hlYWx0aHlcbiAgICByZXN0YXJ0OiBhbHdheXNcbiAgICBsb2dnaW5nOlxuICAgICAgb3B0aW9uczpcbiAgICAgICAgbWF4LXNpemU6IFwiMTBtXCJcbiAgICAgICAgbWF4LWZpbGU6IFwiM1wiXG4gICAgcG9ydHM6XG4gICAgICAtIDExMTFcblxuICBibGlua28tcG9zdGdyZXM6XG4gICAgaW1hZ2U6IHBvc3RncmVzOjE0XG4gICAgcmVzdGFydDogYWx3YXlzXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBQT1NUR1JFU19EQjogcG9zdGdyZXNcbiAgICAgIFBPU1RHUkVTX1VTRVI6IHBvc3RncmVzXG4gICAgICBQT1NUR1JFU19QQVNTV09SRDogJHtQT1NUR1JFU19QQVNTV09SRH1cbiAgICAgIFRaOiBBc2lhL1NoYW5naGFpXG4gICAgdm9sdW1lczpcbiAgICAgIC0gYmxpbmtvLWRiOi92YXIvbGliL3Bvc3RncmVzcWwvZGF0YVxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDogW1wiQ01EXCIsIFwicGdfaXNyZWFkeVwiLCBcIi1VXCIsIFwicG9zdGdyZXNcIiwgXCItZFwiLCBcInBvc3RncmVzXCJdXG4gICAgICBpbnRlcnZhbDogNXNcbiAgICAgIHRpbWVvdXQ6IDEwc1xuICAgICAgcmV0cmllczogNVxuXG52b2x1bWVzOlxuICBibGlua28tZGI6IHt9XG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxucG9zdGdyZXNfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcbm5leHRhdXRoX3NlY3JldCA9IFwiJHtwYXNzd29yZDozMn1cIlxuZGF0YWJhc2VfdXJsID0gXCJwb3N0Z3Jlc3FsOi8vcG9zdGdyZXM6JHtwb3N0Z3Jlc19wYXNzd29yZH1AYmxpbmtvLXBvc3RncmVzOjU0MzIvcG9zdGdyZXNcIlxubmV4dGF1dGhfdXJsID0gXCJodHRwOi8vJHttYWluX2RvbWFpbn1cIlxubmV4dF9wdWJsaWNfYmFzZV91cmwgPSBcImh0dHA6Ly8ke21haW5fZG9tYWlufVwiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJibGlua28td2Vic2l0ZVwiXG5wb3J0ID0gMTExMVxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cbk5FWFRBVVRIX1NFQ1JFVCA9IFwiJHtuZXh0YXV0aF9zZWNyZXR9XCJcblBPU1RHUkVTX1BBU1NXT1JEID0gXCIke3Bvc3RncmVzX3Bhc3N3b3JkfVwiXG5EQVRBQkFTRV9VUkwgPSBcIiR7ZGF0YWJhc2VfdXJsfVwiXG5ORVhUQVVUSF9VUkwgPSBcIiR7bmV4dGF1dGhfdXJsfVwiXG5ORVhUX1BVQkxJQ19CQVNFX1VSTCA9IFwiJHtuZXh0X3B1YmxpY19iYXNlX3VybH1cIiIKfQ==
```

## Links

`productivity`,`organization`,`workflow`,`nextjs`

---

Version:`latest`

BlenderBlender is a free and open-source 3D creation suite. It supports the entire 3D pipeline—modeling, rigging, animation, simulation, rendering, compositing and motion tracking, video editing and 2D animation pipeline.

Bluesky PDSBluesky PDS is a personal data server for Bluesky.

### On this page

ConfigurationBase64LinksTags