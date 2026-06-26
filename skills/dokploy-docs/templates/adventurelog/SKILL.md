---
title: "AdventureLog | Dokploy"
source: "https://docs.dokploy.com/docs/templates/adventurelog"
category: dokploy-docs
created: "2026-06-25T17:21:40.413Z"
---

AdventureLog | Dokploy

# AdventureLog

Copy as Markdown

AdventureLog is an open-source activity tracker with maps, journaling, and Strava integration.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  web:
    image: ghcr.io/seanmorley15/adventurelog-frontend:latest
    restart: unless-stopped
    depends_on:
      - server
    environment:
      # Frontend needs to know where the backend is
      PUBLIC_SERVER_URL: ${PUBLIC_SERVER_URL}
      ORIGIN: ${ORIGIN}
      BODY_SIZE_LIMIT: ${BODY_SIZE_LIMIT}

  db:
    image: postgis/postgis:16-3.5
    restart: unless-stopped
    volumes:
      - postgres_data:/var/lib/postgresql/data/
    environment:
      POSTGRES_DB: ${POSTGRES_DB}
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}

  server:
    image: ghcr.io/seanmorley15/adventurelog-backend:latest
    restart: unless-stopped
    depends_on:
      - db
    volumes:
      - adventurelog_media:/code/media/
    environment:
      # DB settings for Django
      PGHOST: ${PGHOST}
      POSTGRES_DB: ${POSTGRES_DB}
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}

      # Django app settings
      SECRET_KEY: ${SECRET_KEY}
      DJANGO_ADMIN_USERNAME: ${DJANGO_ADMIN_USERNAME}
      DJANGO_ADMIN_PASSWORD: ${DJANGO_ADMIN_PASSWORD}
      DJANGO_ADMIN_EMAIL: ${DJANGO_ADMIN_EMAIL}
      DEBUG: ${DEBUG}
      CSRF_TRUSTED_ORIGINS: ${CSRF_TRUSTED_ORIGINS}
      FRONTEND_URL: ${FRONTEND_URL}
      PUBLIC_URL: ${PUBLIC_URL}

volumes:
  postgres_data: {}
  adventurelog_media: {}
```

```
[variables]
frontend_domain = "${domain}"
backend_domain = "${domain}"
postgres_password = "${password:16}"
secret_key = "${password:32}"
admin_username = "admin"
admin_password = "${password:12}"
admin_email = "${email}"

[config]

# Frontend domain
[[config.domains]]
serviceName = "web"
port = 3000
host = "${frontend_domain}"

# Backend domain
[[config.domains]]
serviceName = "server"
port = 80
host = "${backend_domain}"

[config.env]
# --- Postgres (values used by both db and server services)
PGHOST = "db"
POSTGRES_DB = "adventure"
POSTGRES_USER = "adventure"
POSTGRES_PASSWORD = "${postgres_password}"

# --- Django Backend
SECRET_KEY = "${secret_key}"
DJANGO_ADMIN_USERNAME = "${admin_username}"
DJANGO_ADMIN_PASSWORD = "${admin_password}"
DJANGO_ADMIN_EMAIL = "${admin_email}"
DEBUG = "False"
CSRF_TRUSTED_ORIGINS = "http://${backend_domain},http://${frontend_domain}"
FRONTEND_URL = "http://${frontend_domain}"
PUBLIC_URL = "http://${backend_domain}"

# --- Frontend
PUBLIC_SERVER_URL = "${backend_domain}"
ORIGIN = "http://${frontend_domain}"
BODY_SIZE_LIMIT = "Infinity"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIHdlYjpcbiAgICBpbWFnZTogZ2hjci5pby9zZWFubW9ybGV5MTUvYWR2ZW50dXJlbG9nLWZyb250ZW5kOmxhdGVzdFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIC0gc2VydmVyXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAjIEZyb250ZW5kIG5lZWRzIHRvIGtub3cgd2hlcmUgdGhlIGJhY2tlbmQgaXNcbiAgICAgIFBVQkxJQ19TRVJWRVJfVVJMOiAke1BVQkxJQ19TRVJWRVJfVVJMfVxuICAgICAgT1JJR0lOOiAke09SSUdJTn1cbiAgICAgIEJPRFlfU0laRV9MSU1JVDogJHtCT0RZX1NJWkVfTElNSVR9XG5cbiAgZGI6XG4gICAgaW1hZ2U6IHBvc3RnaXMvcG9zdGdpczoxNi0zLjVcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIHZvbHVtZXM6XG4gICAgICAtIHBvc3RncmVzX2RhdGE6L3Zhci9saWIvcG9zdGdyZXNxbC9kYXRhL1xuICAgIGVudmlyb25tZW50OlxuICAgICAgUE9TVEdSRVNfREI6ICR7UE9TVEdSRVNfREJ9XG4gICAgICBQT1NUR1JFU19VU0VSOiAke1BPU1RHUkVTX1VTRVJ9XG4gICAgICBQT1NUR1JFU19QQVNTV09SRDogJHtQT1NUR1JFU19QQVNTV09SRH1cblxuICBzZXJ2ZXI6XG4gICAgaW1hZ2U6IGdoY3IuaW8vc2Vhbm1vcmxleTE1L2FkdmVudHVyZWxvZy1iYWNrZW5kOmxhdGVzdFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIC0gZGJcbiAgICB2b2x1bWVzOlxuICAgICAgLSBhZHZlbnR1cmVsb2dfbWVkaWE6L2NvZGUvbWVkaWEvXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAjIERCIHNldHRpbmdzIGZvciBEamFuZ29cbiAgICAgIFBHSE9TVDogJHtQR0hPU1R9XG4gICAgICBQT1NUR1JFU19EQjogJHtQT1NUR1JFU19EQn1cbiAgICAgIFBPU1RHUkVTX1VTRVI6ICR7UE9TVEdSRVNfVVNFUn1cbiAgICAgIFBPU1RHUkVTX1BBU1NXT1JEOiAke1BPU1RHUkVTX1BBU1NXT1JEfVxuXG4gICAgICAjIERqYW5nbyBhcHAgc2V0dGluZ3NcbiAgICAgIFNFQ1JFVF9LRVk6ICR7U0VDUkVUX0tFWX1cbiAgICAgIERKQU5HT19BRE1JTl9VU0VSTkFNRTogJHtESkFOR09fQURNSU5fVVNFUk5BTUV9XG4gICAgICBESkFOR09fQURNSU5fUEFTU1dPUkQ6ICR7REpBTkdPX0FETUlOX1BBU1NXT1JEfVxuICAgICAgREpBTkdPX0FETUlOX0VNQUlMOiAke0RKQU5HT19BRE1JTl9FTUFJTH1cbiAgICAgIERFQlVHOiAke0RFQlVHfVxuICAgICAgQ1NSRl9UUlVTVEVEX09SSUdJTlM6ICR7Q1NSRl9UUlVTVEVEX09SSUdJTlN9XG4gICAgICBGUk9OVEVORF9VUkw6ICR7RlJPTlRFTkRfVVJMfVxuICAgICAgUFVCTElDX1VSTDogJHtQVUJMSUNfVVJMfVxuXG52b2x1bWVzOlxuICBwb3N0Z3Jlc19kYXRhOiB7fVxuICBhZHZlbnR1cmVsb2dfbWVkaWE6IHt9XG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbmZyb250ZW5kX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbmJhY2tlbmRfZG9tYWluID0gXCIke2RvbWFpbn1cIlxucG9zdGdyZXNfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MTZ9XCJcbnNlY3JldF9rZXkgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcbmFkbWluX3VzZXJuYW1lID0gXCJhZG1pblwiXG5hZG1pbl9wYXNzd29yZCA9IFwiJHtwYXNzd29yZDoxMn1cIlxuYWRtaW5fZW1haWwgPSBcIiR7ZW1haWx9XCJcblxuW2NvbmZpZ11cblxuIyBGcm9udGVuZCBkb21haW5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcIndlYlwiXG5wb3J0ID0gMzAwMFxuaG9zdCA9IFwiJHtmcm9udGVuZF9kb21haW59XCJcblxuIyBCYWNrZW5kIGRvbWFpblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwic2VydmVyXCJcbnBvcnQgPSA4MFxuaG9zdCA9IFwiJHtiYWNrZW5kX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cbiMgLS0tIFBvc3RncmVzICh2YWx1ZXMgdXNlZCBieSBib3RoIGRiIGFuZCBzZXJ2ZXIgc2VydmljZXMpXG5QR0hPU1QgPSBcImRiXCJcblBPU1RHUkVTX0RCID0gXCJhZHZlbnR1cmVcIlxuUE9TVEdSRVNfVVNFUiA9IFwiYWR2ZW50dXJlXCJcblBPU1RHUkVTX1BBU1NXT1JEID0gXCIke3Bvc3RncmVzX3Bhc3N3b3JkfVwiXG5cbiMgLS0tIERqYW5nbyBCYWNrZW5kXG5TRUNSRVRfS0VZID0gXCIke3NlY3JldF9rZXl9XCJcbkRKQU5HT19BRE1JTl9VU0VSTkFNRSA9IFwiJHthZG1pbl91c2VybmFtZX1cIlxuREpBTkdPX0FETUlOX1BBU1NXT1JEID0gXCIke2FkbWluX3Bhc3N3b3JkfVwiXG5ESkFOR09fQURNSU5fRU1BSUwgPSBcIiR7YWRtaW5fZW1haWx9XCJcbkRFQlVHID0gXCJGYWxzZVwiXG5DU1JGX1RSVVNURURfT1JJR0lOUyA9IFwiaHR0cDovLyR7YmFja2VuZF9kb21haW59LGh0dHA6Ly8ke2Zyb250ZW5kX2RvbWFpbn1cIlxuRlJPTlRFTkRfVVJMID0gXCJodHRwOi8vJHtmcm9udGVuZF9kb21haW59XCJcblBVQkxJQ19VUkwgPSBcImh0dHA6Ly8ke2JhY2tlbmRfZG9tYWlufVwiXG5cbiMgLS0tIEZyb250ZW5kXG5QVUJMSUNfU0VSVkVSX1VSTCA9IFwiJHtiYWNrZW5kX2RvbWFpbn1cIiBcbk9SSUdJTiA9IFwiaHR0cDovLyR7ZnJvbnRlbmRfZG9tYWlufVwiXG5CT0RZX1NJWkVfTElNSVQgPSBcIkluZmluaXR5XCJcbiIKfQ==
```

## Links

`activity`,`maps`,`django`,`react`,`postgres`

---

Version:`latest`

AdminerAdminer is a comprehensive database management tool that supports MySQL, MariaDB, PostgreSQL, SQLite, MS SQL, Oracle, Elasticsearch, MongoDB and others. It provides a clean interface for efficient database operations, with strong security features and extensive customization options.

Affine ProAffine Pro is a modern, self-hosted platform designed for collaborative content creation and project management. It offers an intuitive interface, seamless real-time collaboration, and powerful tools for organizing tasks, notes, and ideas.

### On this page

ConfigurationBase64LinksTags