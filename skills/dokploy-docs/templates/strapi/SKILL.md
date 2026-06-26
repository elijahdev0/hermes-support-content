---
title: "Strapi | Dokploy"
source: "https://docs.dokploy.com/docs/templates/strapi"
category: dokploy-docs
created: "2026-06-25T17:21:59.115Z"
---

Strapi | Dokploy

# Strapi

Copy as Markdown

Open-source headless CMS to build powerful APIs with built-in content management.

## Configuration

docker-compose.ymltemplate.toml

```
# Self-host guide:
# - https://strapi.io/blog/how-to-self-host-your-headless-cms-using-docker-compose

services:
  strapi:
    image: elestio/strapi-production:v5.33.0
    environment:
      # https://docs.strapi.io/cms/configurations/environment
      NODE_ENV: production
      STRAPI_TELEMETRY_DISABLED: true
      STRAPI_PLUGIN_I18N_INIT_LOCALE_CODE: en
      FAST_REFRESH: true
      JWT_SECRET: ${JWT_SECRET}
      ADMIN_JWT_SECRET: ${ADMIN_JWT_SECRET}
      DATABASE_CLIENT: postgres
      DATABASE_HOST: strapi_postgres
      DATABASE_PORT: 5432
      DATABASE_NAME: strapi
      DATABASE_USERNAME: strapi
      DATABASE_PASSWORD: ${POSTGRES_PASSWORD}
    volumes:
      - strapi_data:/srv/app
    expose:
      - 1337
    depends_on:
      - strapi_postgres
    healthcheck:
      test:
        - CMD
        - wget
        - "-q"
        - "--spider"
        - "http://127.0.0.1:1337"
      start_period: 3s
      interval: 30s
      timeout: 10s
      retries: 5

  strapi_postgres:
    image: postgres:18
    environment:
      POSTGRES_DB: strapi
      POSTGRES_USER: strapi
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    volumes:
      - strapi_postgres_data:/var/lib/postgresql
    healthcheck:
      test:
        - CMD-SHELL
        - "pg_isready -U $${POSTGRES_USER} -d $${POSTGRES_DB}"
      start_period: 3s
      interval: 30s
      timeout: 10s
      retries: 5

volumes:
  strapi_data:
  strapi_postgres_data:
```

```
[variables]
main_domain = "${domain}"
postgres_password = "${password:32}"
jwt_secret = "${password:32}"
admin_jwt_secret = "${password:32}"

[[config.domains]]
serviceName = "strapi"
port = 1337
host = "${main_domain}"

[config.env]
POSTGRES_PASSWORD = "${postgres_password}"
JWT_SECRET = "${jwt_secret}"
ADMIN_JWT_SECRET = "${admin_jwt_secret}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogIiMgU2VsZi1ob3N0IGd1aWRlOlxuIyAtIGh0dHBzOi8vc3RyYXBpLmlvL2Jsb2cvaG93LXRvLXNlbGYtaG9zdC15b3VyLWhlYWRsZXNzLWNtcy11c2luZy1kb2NrZXItY29tcG9zZVxuXG5zZXJ2aWNlczpcbiAgc3RyYXBpOlxuICAgIGltYWdlOiBlbGVzdGlvL3N0cmFwaS1wcm9kdWN0aW9uOnY1LjMzLjBcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgICMgaHR0cHM6Ly9kb2NzLnN0cmFwaS5pby9jbXMvY29uZmlndXJhdGlvbnMvZW52aXJvbm1lbnRcbiAgICAgIE5PREVfRU5WOiBwcm9kdWN0aW9uXG4gICAgICBTVFJBUElfVEVMRU1FVFJZX0RJU0FCTEVEOiB0cnVlXG4gICAgICBTVFJBUElfUExVR0lOX0kxOE5fSU5JVF9MT0NBTEVfQ09ERTogZW5cbiAgICAgIEZBU1RfUkVGUkVTSDogdHJ1ZVxuICAgICAgSldUX1NFQ1JFVDogJHtKV1RfU0VDUkVUfVxuICAgICAgQURNSU5fSldUX1NFQ1JFVDogJHtBRE1JTl9KV1RfU0VDUkVUfVxuICAgICAgREFUQUJBU0VfQ0xJRU5UOiBwb3N0Z3Jlc1xuICAgICAgREFUQUJBU0VfSE9TVDogc3RyYXBpX3Bvc3RncmVzXG4gICAgICBEQVRBQkFTRV9QT1JUOiA1NDMyXG4gICAgICBEQVRBQkFTRV9OQU1FOiBzdHJhcGlcbiAgICAgIERBVEFCQVNFX1VTRVJOQU1FOiBzdHJhcGlcbiAgICAgIERBVEFCQVNFX1BBU1NXT1JEOiAke1BPU1RHUkVTX1BBU1NXT1JEfVxuICAgIHZvbHVtZXM6XG4gICAgICAtIHN0cmFwaV9kYXRhOi9zcnYvYXBwXG4gICAgZXhwb3NlOlxuICAgICAgLSAxMzM3XG4gICAgZGVwZW5kc19vbjpcbiAgICAgIC0gc3RyYXBpX3Bvc3RncmVzXG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OlxuICAgICAgICAtIENNRFxuICAgICAgICAtIHdnZXRcbiAgICAgICAgLSBcIi1xXCJcbiAgICAgICAgLSBcIi0tc3BpZGVyXCJcbiAgICAgICAgLSBcImh0dHA6Ly8xMjcuMC4wLjE6MTMzN1wiXG4gICAgICBzdGFydF9wZXJpb2Q6IDNzXG4gICAgICBpbnRlcnZhbDogMzBzXG4gICAgICB0aW1lb3V0OiAxMHNcbiAgICAgIHJldHJpZXM6IDVcblxuICBzdHJhcGlfcG9zdGdyZXM6XG4gICAgaW1hZ2U6IHBvc3RncmVzOjE4XG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBQT1NUR1JFU19EQjogc3RyYXBpXG4gICAgICBQT1NUR1JFU19VU0VSOiBzdHJhcGlcbiAgICAgIFBPU1RHUkVTX1BBU1NXT1JEOiAke1BPU1RHUkVTX1BBU1NXT1JEfVxuICAgIHZvbHVtZXM6XG4gICAgICAtIHN0cmFwaV9wb3N0Z3Jlc19kYXRhOi92YXIvbGliL3Bvc3RncmVzcWxcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6XG4gICAgICAgIC0gQ01ELVNIRUxMXG4gICAgICAgIC0gXCJwZ19pc3JlYWR5IC1VICQke1BPU1RHUkVTX1VTRVJ9IC1kICQke1BPU1RHUkVTX0RCfVwiXG4gICAgICBzdGFydF9wZXJpb2Q6IDNzXG4gICAgICBpbnRlcnZhbDogMzBzXG4gICAgICB0aW1lb3V0OiAxMHNcbiAgICAgIHJldHJpZXM6IDVcblxudm9sdW1lczpcbiAgc3RyYXBpX2RhdGE6XG4gIHN0cmFwaV9wb3N0Z3Jlc19kYXRhOlxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbnBvc3RncmVzX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5qd3Rfc2VjcmV0ID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5hZG1pbl9qd3Rfc2VjcmV0ID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcInN0cmFwaVwiXG5wb3J0ID0gMTMzN1xuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cblBPU1RHUkVTX1BBU1NXT1JEID0gXCIke3Bvc3RncmVzX3Bhc3N3b3JkfVwiXG5KV1RfU0VDUkVUID0gXCIke2p3dF9zZWNyZXR9XCJcbkFETUlOX0pXVF9TRUNSRVQgPSBcIiR7YWRtaW5fand0X3NlY3JldH1cIlxuIgp9
```

## Links

`headless`,`cms`,`content-management`

---

Version:`v5.33.0`

StorydenWith a fresh new take on traditional bulletin board forum software, Storyden is a modern, secure and extensible platform for building communities.

StreamFlowStreamFlow is a multi-platform live streaming web application that enables simultaneous RTMP streaming to YouTube, Facebook, and other platforms with video gallery, scheduled streaming, and real-time monitoring.

### On this page

ConfigurationBase64LinksTags