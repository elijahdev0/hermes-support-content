---
title: "MediaCMS | Dokploy"
source: "https://docs.dokploy.com/docs/templates/mediacms"
category: dokploy-docs
created: "2026-06-25T17:21:53.155Z"
---

MediaCMS | Dokploy

# MediaCMS

Copy as Markdown

MediaCMS is an open-source video and media CMS. It is a modern, full-featured solution for managing and streaming media content.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3"

services:
  migrations:
    image: mediacms/mediacms:latest
    volumes:
      - mediacms_data:/home/mediacms.io/mediacms/media
      - mediacms_static:/home/mediacms.io/mediacms/staticfiles
    environment:
      ENABLE_UWSGI: 'no'
      ENABLE_NGINX: 'no'
      ENABLE_CELERY_SHORT: 'no'
      ENABLE_CELERY_LONG: 'no'
      ENABLE_CELERY_BEAT: 'no'
      ENABLE_MIGRATIONS: 'yes'
      ADMIN_USER: 'admin'
      ADMIN_EMAIL: 'admin@localhost'
      ADMIN_PASSWORD: ${ADMIN_PASSWORD}
      DATABASE_HOST: db
      DATABASE_PORT: 5432
      DATABASE_USER: mediacms
      DATABASE_PASSWORD: ${POSTGRES_PASSWORD}
      DATABASE_NAME: mediacms
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      REDIS_HOST: redis
      REDIS_PORT: 6379
    command: "./deploy/docker/prestart.sh"
    restart: on-failure
    depends_on:
      redis:
        condition: service_healthy
      db:
        condition: service_healthy

  web:
    image: mediacms/mediacms:latest
    deploy:
      replicas: 1
    ports:
      - 80
    volumes:
      - mediacms_data:/home/mediacms.io/mediacms/media
      - mediacms_static:/home/mediacms.io/mediacms/staticfiles
    environment:
      ENABLE_CELERY_BEAT: 'no'
      ENABLE_CELERY_SHORT: 'no'
      ENABLE_CELERY_LONG: 'no'
      ENABLE_MIGRATIONS: 'no'
      DATABASE_HOST: db
      DATABASE_PORT: 5432
      DATABASE_USER: mediacms
      DATABASE_PASSWORD: ${POSTGRES_PASSWORD}
      DATABASE_NAME: mediacms
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      REDIS_HOST: redis
      REDIS_PORT: 6379
    depends_on:
      - migrations

  celery_beat:
    image: mediacms/mediacms:latest
    volumes:
      - mediacms_data:/home/mediacms.io/mediacms/media
      - mediacms_static:/home/mediacms.io/mediacms/staticfiles
    environment:
      ENABLE_UWSGI: 'no'
      ENABLE_NGINX: 'no'
      ENABLE_CELERY_SHORT: 'no'
      ENABLE_CELERY_LONG: 'no'
      ENABLE_MIGRATIONS: 'no'
      DATABASE_HOST: db
      DATABASE_PORT: 5432
      DATABASE_USER: mediacms
      DATABASE_PASSWORD: ${POSTGRES_PASSWORD}
      DATABASE_NAME: mediacms
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      REDIS_HOST: redis
      REDIS_PORT: 6379
    depends_on:
      - redis

  celery_worker:
    image: mediacms/mediacms:latest
    deploy:
      replicas: 1
    volumes:
      - mediacms_data:/home/mediacms.io/mediacms/media
      - mediacms_static:/home/mediacms.io/mediacms/staticfiles
    environment:
      ENABLE_UWSGI: 'no'
      ENABLE_NGINX: 'no'
      ENABLE_CELERY_BEAT: 'no'
      ENABLE_MIGRATIONS: 'no'
      DATABASE_HOST: db
      DATABASE_PORT: 5432
      DATABASE_USER: mediacms
      DATABASE_PASSWORD: ${POSTGRES_PASSWORD}
      DATABASE_NAME: mediacms
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      REDIS_HOST: redis
      REDIS_PORT: 6379
    depends_on:
      - migrations

  db:
    image: postgres:17.2-alpine
    volumes:
      - postgres_data:/var/lib/postgresql/data/
    restart: always
    environment:
      POSTGRES_USER: mediacms
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: mediacms
      TZ: Europe/London
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -d $${POSTGRES_DB} -U $${POSTGRES_USER}"]
      interval: 10s
      timeout: 5s
      retries: 5

  redis:
    image: "redis:alpine"
    restart: always
    healthcheck:
      test: ["CMD", "redis-cli","ping"]
      interval: 10s
      timeout: 5s
      retries: 3

volumes:
  postgres_data:
  mediacms_data:
  mediacms_static:
```

```
[variables]
main_domain = "${domain}"
postgres_password = "${password}"
admin_password = "${password}"

[config]
mounts = []

[[config.domains]]
serviceName = "web"
port = 80
host = "${main_domain}"

[config.env]
POSTGRES_PASSWORD = "${postgres_password}"
ADMIN_PASSWORD = "${admin_password}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiM1wiXG5cbnNlcnZpY2VzOlxuICBtaWdyYXRpb25zOlxuICAgIGltYWdlOiBtZWRpYWNtcy9tZWRpYWNtczpsYXRlc3RcbiAgICB2b2x1bWVzOlxuICAgICAgLSBtZWRpYWNtc19kYXRhOi9ob21lL21lZGlhY21zLmlvL21lZGlhY21zL21lZGlhXG4gICAgICAtIG1lZGlhY21zX3N0YXRpYzovaG9tZS9tZWRpYWNtcy5pby9tZWRpYWNtcy9zdGF0aWNmaWxlc1xuICAgIGVudmlyb25tZW50OlxuICAgICAgRU5BQkxFX1VXU0dJOiAnbm8nXG4gICAgICBFTkFCTEVfTkdJTlg6ICdubydcbiAgICAgIEVOQUJMRV9DRUxFUllfU0hPUlQ6ICdubydcbiAgICAgIEVOQUJMRV9DRUxFUllfTE9ORzogJ25vJ1xuICAgICAgRU5BQkxFX0NFTEVSWV9CRUFUOiAnbm8nXG4gICAgICBFTkFCTEVfTUlHUkFUSU9OUzogJ3llcydcbiAgICAgIEFETUlOX1VTRVI6ICdhZG1pbidcbiAgICAgIEFETUlOX0VNQUlMOiAnYWRtaW5AbG9jYWxob3N0J1xuICAgICAgQURNSU5fUEFTU1dPUkQ6ICR7QURNSU5fUEFTU1dPUkR9XG4gICAgICBEQVRBQkFTRV9IT1NUOiBkYlxuICAgICAgREFUQUJBU0VfUE9SVDogNTQzMlxuICAgICAgREFUQUJBU0VfVVNFUjogbWVkaWFjbXNcbiAgICAgIERBVEFCQVNFX1BBU1NXT1JEOiAke1BPU1RHUkVTX1BBU1NXT1JEfVxuICAgICAgREFUQUJBU0VfTkFNRTogbWVkaWFjbXNcbiAgICAgIFBPU1RHUkVTX1BBU1NXT1JEOiAke1BPU1RHUkVTX1BBU1NXT1JEfVxuICAgICAgUkVESVNfSE9TVDogcmVkaXNcbiAgICAgIFJFRElTX1BPUlQ6IDYzNzlcbiAgICBjb21tYW5kOiBcIi4vZGVwbG95L2RvY2tlci9wcmVzdGFydC5zaFwiXG4gICAgcmVzdGFydDogb24tZmFpbHVyZVxuICAgIGRlcGVuZHNfb246XG4gICAgICByZWRpczpcbiAgICAgICAgY29uZGl0aW9uOiBzZXJ2aWNlX2hlYWx0aHlcbiAgICAgIGRiOlxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2VfaGVhbHRoeVxuXG4gIHdlYjpcbiAgICBpbWFnZTogbWVkaWFjbXMvbWVkaWFjbXM6bGF0ZXN0XG4gICAgZGVwbG95OlxuICAgICAgcmVwbGljYXM6IDFcbiAgICBwb3J0czpcbiAgICAgIC0gODBcbiAgICB2b2x1bWVzOlxuICAgICAgLSBtZWRpYWNtc19kYXRhOi9ob21lL21lZGlhY21zLmlvL21lZGlhY21zL21lZGlhXG4gICAgICAtIG1lZGlhY21zX3N0YXRpYzovaG9tZS9tZWRpYWNtcy5pby9tZWRpYWNtcy9zdGF0aWNmaWxlc1xuICAgIGVudmlyb25tZW50OlxuICAgICAgRU5BQkxFX0NFTEVSWV9CRUFUOiAnbm8nXG4gICAgICBFTkFCTEVfQ0VMRVJZX1NIT1JUOiAnbm8nXG4gICAgICBFTkFCTEVfQ0VMRVJZX0xPTkc6ICdubydcbiAgICAgIEVOQUJMRV9NSUdSQVRJT05TOiAnbm8nXG4gICAgICBEQVRBQkFTRV9IT1NUOiBkYlxuICAgICAgREFUQUJBU0VfUE9SVDogNTQzMlxuICAgICAgREFUQUJBU0VfVVNFUjogbWVkaWFjbXNcbiAgICAgIERBVEFCQVNFX1BBU1NXT1JEOiAke1BPU1RHUkVTX1BBU1NXT1JEfVxuICAgICAgREFUQUJBU0VfTkFNRTogbWVkaWFjbXNcbiAgICAgIFBPU1RHUkVTX1BBU1NXT1JEOiAke1BPU1RHUkVTX1BBU1NXT1JEfVxuICAgICAgUkVESVNfSE9TVDogcmVkaXNcbiAgICAgIFJFRElTX1BPUlQ6IDYzNzlcbiAgICBkZXBlbmRzX29uOlxuICAgICAgLSBtaWdyYXRpb25zXG5cbiAgY2VsZXJ5X2JlYXQ6XG4gICAgaW1hZ2U6IG1lZGlhY21zL21lZGlhY21zOmxhdGVzdFxuICAgIHZvbHVtZXM6XG4gICAgICAtIG1lZGlhY21zX2RhdGE6L2hvbWUvbWVkaWFjbXMuaW8vbWVkaWFjbXMvbWVkaWFcbiAgICAgIC0gbWVkaWFjbXNfc3RhdGljOi9ob21lL21lZGlhY21zLmlvL21lZGlhY21zL3N0YXRpY2ZpbGVzXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBFTkFCTEVfVVdTR0k6ICdubydcbiAgICAgIEVOQUJMRV9OR0lOWDogJ25vJ1xuICAgICAgRU5BQkxFX0NFTEVSWV9TSE9SVDogJ25vJ1xuICAgICAgRU5BQkxFX0NFTEVSWV9MT05HOiAnbm8nXG4gICAgICBFTkFCTEVfTUlHUkFUSU9OUzogJ25vJ1xuICAgICAgREFUQUJBU0VfSE9TVDogZGJcbiAgICAgIERBVEFCQVNFX1BPUlQ6IDU0MzJcbiAgICAgIERBVEFCQVNFX1VTRVI6IG1lZGlhY21zXG4gICAgICBEQVRBQkFTRV9QQVNTV09SRDogJHtQT1NUR1JFU19QQVNTV09SRH1cbiAgICAgIERBVEFCQVNFX05BTUU6IG1lZGlhY21zXG4gICAgICBQT1NUR1JFU19QQVNTV09SRDogJHtQT1NUR1JFU19QQVNTV09SRH1cbiAgICAgIFJFRElTX0hPU1Q6IHJlZGlzXG4gICAgICBSRURJU19QT1JUOiA2Mzc5XG4gICAgZGVwZW5kc19vbjpcbiAgICAgIC0gcmVkaXNcblxuICBjZWxlcnlfd29ya2VyOlxuICAgIGltYWdlOiBtZWRpYWNtcy9tZWRpYWNtczpsYXRlc3RcbiAgICBkZXBsb3k6XG4gICAgICByZXBsaWNhczogMVxuICAgIHZvbHVtZXM6XG4gICAgICAtIG1lZGlhY21zX2RhdGE6L2hvbWUvbWVkaWFjbXMuaW8vbWVkaWFjbXMvbWVkaWFcbiAgICAgIC0gbWVkaWFjbXNfc3RhdGljOi9ob21lL21lZGlhY21zLmlvL21lZGlhY21zL3N0YXRpY2ZpbGVzXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBFTkFCTEVfVVdTR0k6ICdubydcbiAgICAgIEVOQUJMRV9OR0lOWDogJ25vJ1xuICAgICAgRU5BQkxFX0NFTEVSWV9CRUFUOiAnbm8nXG4gICAgICBFTkFCTEVfTUlHUkFUSU9OUzogJ25vJ1xuICAgICAgREFUQUJBU0VfSE9TVDogZGJcbiAgICAgIERBVEFCQVNFX1BPUlQ6IDU0MzJcbiAgICAgIERBVEFCQVNFX1VTRVI6IG1lZGlhY21zXG4gICAgICBEQVRBQkFTRV9QQVNTV09SRDogJHtQT1NUR1JFU19QQVNTV09SRH1cbiAgICAgIERBVEFCQVNFX05BTUU6IG1lZGlhY21zXG4gICAgICBQT1NUR1JFU19QQVNTV09SRDogJHtQT1NUR1JFU19QQVNTV09SRH1cbiAgICAgIFJFRElTX0hPU1Q6IHJlZGlzXG4gICAgICBSRURJU19QT1JUOiA2Mzc5XG4gICAgZGVwZW5kc19vbjpcbiAgICAgIC0gbWlncmF0aW9uc1xuXG4gIGRiOlxuICAgIGltYWdlOiBwb3N0Z3JlczoxNy4yLWFscGluZVxuICAgIHZvbHVtZXM6XG4gICAgICAtIHBvc3RncmVzX2RhdGE6L3Zhci9saWIvcG9zdGdyZXNxbC9kYXRhL1xuICAgIHJlc3RhcnQ6IGFsd2F5c1xuICAgIGVudmlyb25tZW50OlxuICAgICAgUE9TVEdSRVNfVVNFUjogbWVkaWFjbXNcbiAgICAgIFBPU1RHUkVTX1BBU1NXT1JEOiAke1BPU1RHUkVTX1BBU1NXT1JEfVxuICAgICAgUE9TVEdSRVNfREI6IG1lZGlhY21zXG4gICAgICBUWjogRXVyb3BlL0xvbmRvblxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDogW1wiQ01ELVNIRUxMXCIsIFwicGdfaXNyZWFkeSAtZCAkJHtQT1NUR1JFU19EQn0gLVUgJCR7UE9TVEdSRVNfVVNFUn1cIl1cbiAgICAgIGludGVydmFsOiAxMHNcbiAgICAgIHRpbWVvdXQ6IDVzXG4gICAgICByZXRyaWVzOiA1XG5cbiAgcmVkaXM6XG4gICAgaW1hZ2U6IFwicmVkaXM6YWxwaW5lXCJcbiAgICByZXN0YXJ0OiBhbHdheXNcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6IFtcIkNNRFwiLCBcInJlZGlzLWNsaVwiLFwicGluZ1wiXVxuICAgICAgaW50ZXJ2YWw6IDEwc1xuICAgICAgdGltZW91dDogNXNcbiAgICAgIHJldHJpZXM6IDNcblxudm9sdW1lczpcbiAgcG9zdGdyZXNfZGF0YTpcbiAgbWVkaWFjbXNfZGF0YTpcbiAgbWVkaWFjbXNfc3RhdGljOlxuXG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxucG9zdGdyZXNfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmR9XCJcbmFkbWluX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkfVwiXG5cbltjb25maWddXG5tb3VudHMgPSBbXVxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJ3ZWJcIlxucG9ydCA9IDgwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuUE9TVEdSRVNfUEFTU1dPUkQgPSBcIiR7cG9zdGdyZXNfcGFzc3dvcmR9XCJcbkFETUlOX1BBU1NXT1JEID0gXCIke2FkbWluX3Bhc3N3b3JkfVwiXG5cbiIKfQ==
```

## Links

`media`,`video`,`cms`,`streaming`,`self-hosted`

---

Version:`latest`

Mealie (sqlite version) Mealie is an intuitive and easy to use recipe management app. It's designed to make your life easier by being the best recipes management experience on the web and providing you with an easy to use interface to manage your growing collection of recipes.

MediaFetchA tiny, self-hosted web wrapper for yt-dlp to download video and audio. Optional basic auth.

### On this page

ConfigurationBase64LinksTags