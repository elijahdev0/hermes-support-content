---
title: "Budibase | Dokploy"
source: "https://docs.dokploy.com/docs/templates/budibase"
category: dokploy-docs
created: "2026-06-25T17:21:42.677Z"
---

Budibase | Dokploy

# Budibase

Budibase is an open-source low-code platform that saves engineers 100s of hours building forms, portals, and approval apps, securely.

## Configuration

docker-compose.ymltemplate.toml

```
services:

  apps:
    image: budibase/apps:3.23.47
    restart: unless-stopped
    environment:
      SELF_HOSTED: 1
      LOG_LEVEL: info
      PORT: 4002
      INTERNAL_API_KEY: ${BB_INTERNAL_API_KEY}
      API_ENCRYPTION_KEY: ${BB_API_ENCRYPTION_KEY}
      JWT_SECRET: ${BB_JWT_SECRET}
      MINIO_ACCESS_KEY: ${BB_MINIO_ACCESS_KEY}
      MINIO_SECRET_KEY: ${BB_MINIO_SECRET_KEY}
      MINIO_URL: http://minio:9000
      REDIS_URL: redis:6379
      REDIS_PASSWORD: ${BB_REDIS_PASSWORD}
      WORKER_URL: http://worker:4003
      COUCH_DB_USERNAME: budibase
      COUCH_DB_PASSWORD: ${BB_COUCHDB_PASSWORD}
      COUCH_DB_URL: http://budibase:${BB_COUCHDB_PASSWORD}@couchdb:5984
      BUDIBASE_ENVIRONMENT: ${BUDIBASE_ENVIRONMENT:-PRODUCTION}
      ENABLE_ANALYTICS: ${ENABLE_ANALYTICS:-true}
      BB_ADMIN_USER_EMAIL: ''
      BB_ADMIN_USER_PASSWORD: ''
    depends_on:
      worker:
        condition: service_healthy
      redis:
        condition: service_healthy
    healthcheck:
      test:
        - CMD
        - wget
        - '--spider'
        - '-qO-'
        - 'http://localhost:4002/health'
      interval: 15s
      timeout: 15s
      retries: 5
      start_period: 10s

  worker:
    image: budibase/worker:3.23.47
    restart: unless-stopped
    environment:
      SELF_HOSTED: 1
      LOG_LEVEL: info
      PORT: 4003
      CLUSTER_PORT: 10000
      INTERNAL_API_KEY: ${BB_INTERNAL_API_KEY}
      API_ENCRYPTION_KEY: ${BB_API_ENCRYPTION_KEY}
      JWT_SECRET: ${BB_JWT_SECRET}
      MINIO_ACCESS_KEY: ${BB_MINIO_ACCESS_KEY}
      MINIO_SECRET_KEY: ${BB_MINIO_SECRET_KEY}
      APPS_URL: http://apps:4002
      MINIO_URL: http://minio:9000
      REDIS_URL: redis:6379
      REDIS_PASSWORD: ${BB_REDIS_PASSWORD}
      COUCH_DB_USERNAME: budibase
      COUCH_DB_PASSWORD: ${BB_COUCHDB_PASSWORD}
      COUCH_DB_URL: http://budibase:${BB_COUCHDB_PASSWORD}@couchdb:5984
      BUDIBASE_ENVIRONMENT: ${BUDIBASE_ENVIRONMENT:-PRODUCTION}
      ENABLE_ANALYTICS: ${ENABLE_ANALYTICS:-true}
    depends_on:
      redis:
        condition: service_healthy
      minio:
        condition: service_healthy
    healthcheck:
      test:
        - CMD
        - wget
        - '--spider'
        - '-qO-'
        - 'http://localhost:4003/health'
      interval: 15s
      timeout: 15s
      retries: 5
      start_period: 10s

  minio:
    image: minio/minio:RELEASE.2025-09-07T16-13-09Z
    restart: unless-stopped
    volumes:
      - 'minio_data:/data'
    environment:
      MINIO_ROOT_USER: ${BB_MINIO_ACCESS_KEY}
      MINIO_ROOT_PASSWORD: ${BB_MINIO_SECRET_KEY}
      MINIO_BROWSER: off
    command: 'server /data --console-address ":9001"'
    healthcheck:
      test:
        - CMD
        - curl
        - '-f'
        - 'http://localhost:9000/minio/health/live'
      interval: 30s
      timeout: 20s
      retries: 3

  proxy:
    image: budibase/proxy:3.23.47
    restart: unless-stopped
    environment:
      PROXY_RATE_LIMIT_WEBHOOKS_PER_SECOND: 10
      PROXY_RATE_LIMIT_API_PER_SECOND: 20
      APPS_UPSTREAM_URL: http://apps:4002
      WORKER_UPSTREAM_URL: http://worker:4003
      MINIO_UPSTREAM_URL: http://minio:9000
      COUCHDB_UPSTREAM_URL: http://couchdb:5984
      WATCHTOWER_UPSTREAM_URL: http://watchtower:8080
      RESOLVER: 127.0.0.11
    depends_on:
      minio:
        condition: service_healthy
      worker:
        condition: service_healthy
      apps:
        condition: service_healthy
      couchdb:
        condition: service_healthy
    healthcheck:
      test:
        - CMD
        - curl
        - '-f'
        - 'http://localhost:10000/'
      interval: 15s
      timeout: 15s
      retries: 5
      start_period: 10s

  couchdb:
    image: budibase/couchdb:v3.3.3
    restart: unless-stopped
    environment:
      COUCHDB_USER: budibase
      COUCHDB_PASSWORD: ${BB_COUCHDB_PASSWORD}
      TARGETBUILD: docker-compose
    healthcheck:
      test:
        - CMD
        - curl
        - '-f'
        - 'http://localhost:5984/'
      interval: 15s
      timeout: 15s
      retries: 5
      start_period: 10s
    volumes:
      - 'couchdb3_data:/opt/couchdb/data'

  redis:
    image: redis:8.4-alpine
    restart: unless-stopped
    command: 'redis-server --requirepass "${BB_REDIS_PASSWORD}"'
    volumes:
      - 'redis_data:/data'
    healthcheck:
      test:
        - CMD
        - redis-cli
        - '-a'
        - ${BB_REDIS_PASSWORD}
        - ping
      interval: 15s
      timeout: 15s
      retries: 5
      start_period: 10s

volumes:
  minio_data:
  couchdb3_data:
  redis_data:
```

```
[variables]
main_domain = "${domain}"
api_key = "${password:32}"
encryption_key = "${password:32}"
jwt_secret = "${password:32}"
couchdb_password = "${password:32}"
redis_password = "${password:32}"
minio_access_key = "${password:32}"
minio_secret_key = "${password:32}"
watchtower_password = "${password:32}"

[config]
env = [
  "BB_HOST=${main_domain}",
  "BB_INTERNAL_API_KEY=${api_key}",
  "BB_API_ENCRYPTION_KEY=${encryption_key}",
  "BB_JWT_SECRET=${jwt_secret}",
  "BB_COUCHDB_PASSWORD=${couchdb_password}",
  "BB_REDIS_PASSWORD=${redis_password}",
  "BB_WATCHTOWER_PASSWORD=${watchtower_password}",
  "BB_MINIO_ACCESS_KEY=${minio_access_key}",
  "BB_MINIO_SECRET_KEY=${minio_secret_key}",
]
mounts = []

[[config.domains]]
serviceName = "proxy"
port = 10_000
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuXG4gIGFwcHM6XG4gICAgaW1hZ2U6IGJ1ZGliYXNlL2FwcHM6My4yMy40N1xuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBTRUxGX0hPU1RFRDogMVxuICAgICAgTE9HX0xFVkVMOiBpbmZvXG4gICAgICBQT1JUOiA0MDAyXG4gICAgICBJTlRFUk5BTF9BUElfS0VZOiAke0JCX0lOVEVSTkFMX0FQSV9LRVl9XG4gICAgICBBUElfRU5DUllQVElPTl9LRVk6ICR7QkJfQVBJX0VOQ1JZUFRJT05fS0VZfVxuICAgICAgSldUX1NFQ1JFVDogJHtCQl9KV1RfU0VDUkVUfVxuICAgICAgTUlOSU9fQUNDRVNTX0tFWTogJHtCQl9NSU5JT19BQ0NFU1NfS0VZfVxuICAgICAgTUlOSU9fU0VDUkVUX0tFWTogJHtCQl9NSU5JT19TRUNSRVRfS0VZfVxuICAgICAgTUlOSU9fVVJMOiBodHRwOi8vbWluaW86OTAwMFxuICAgICAgUkVESVNfVVJMOiByZWRpczo2Mzc5XG4gICAgICBSRURJU19QQVNTV09SRDogJHtCQl9SRURJU19QQVNTV09SRH1cbiAgICAgIFdPUktFUl9VUkw6IGh0dHA6Ly93b3JrZXI6NDAwM1xuICAgICAgQ09VQ0hfREJfVVNFUk5BTUU6IGJ1ZGliYXNlXG4gICAgICBDT1VDSF9EQl9QQVNTV09SRDogJHtCQl9DT1VDSERCX1BBU1NXT1JEfVxuICAgICAgQ09VQ0hfREJfVVJMOiBodHRwOi8vYnVkaWJhc2U6JHtCQl9DT1VDSERCX1BBU1NXT1JEfUBjb3VjaGRiOjU5ODRcbiAgICAgIEJVRElCQVNFX0VOVklST05NRU5UOiAke0JVRElCQVNFX0VOVklST05NRU5UOi1QUk9EVUNUSU9OfVxuICAgICAgRU5BQkxFX0FOQUxZVElDUzogJHtFTkFCTEVfQU5BTFlUSUNTOi10cnVlfVxuICAgICAgQkJfQURNSU5fVVNFUl9FTUFJTDogJydcbiAgICAgIEJCX0FETUlOX1VTRVJfUEFTU1dPUkQ6ICcnXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIHdvcmtlcjpcbiAgICAgICAgY29uZGl0aW9uOiBzZXJ2aWNlX2hlYWx0aHlcbiAgICAgIHJlZGlzOlxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2VfaGVhbHRoeVxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDpcbiAgICAgICAgLSBDTURcbiAgICAgICAgLSB3Z2V0XG4gICAgICAgIC0gJy0tc3BpZGVyJ1xuICAgICAgICAtICctcU8tJ1xuICAgICAgICAtICdodHRwOi8vbG9jYWxob3N0OjQwMDIvaGVhbHRoJ1xuICAgICAgaW50ZXJ2YWw6IDE1c1xuICAgICAgdGltZW91dDogMTVzXG4gICAgICByZXRyaWVzOiA1XG4gICAgICBzdGFydF9wZXJpb2Q6IDEwc1xuXG4gIHdvcmtlcjpcbiAgICBpbWFnZTogYnVkaWJhc2Uvd29ya2VyOjMuMjMuNDdcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGVudmlyb25tZW50OlxuICAgICAgU0VMRl9IT1NURUQ6IDFcbiAgICAgIExPR19MRVZFTDogaW5mb1xuICAgICAgUE9SVDogNDAwM1xuICAgICAgQ0xVU1RFUl9QT1JUOiAxMDAwMFxuICAgICAgSU5URVJOQUxfQVBJX0tFWTogJHtCQl9JTlRFUk5BTF9BUElfS0VZfVxuICAgICAgQVBJX0VOQ1JZUFRJT05fS0VZOiAke0JCX0FQSV9FTkNSWVBUSU9OX0tFWX1cbiAgICAgIEpXVF9TRUNSRVQ6ICR7QkJfSldUX1NFQ1JFVH1cbiAgICAgIE1JTklPX0FDQ0VTU19LRVk6ICR7QkJfTUlOSU9fQUNDRVNTX0tFWX1cbiAgICAgIE1JTklPX1NFQ1JFVF9LRVk6ICR7QkJfTUlOSU9fU0VDUkVUX0tFWX1cbiAgICAgIEFQUFNfVVJMOiBodHRwOi8vYXBwczo0MDAyXG4gICAgICBNSU5JT19VUkw6IGh0dHA6Ly9taW5pbzo5MDAwXG4gICAgICBSRURJU19VUkw6IHJlZGlzOjYzNzlcbiAgICAgIFJFRElTX1BBU1NXT1JEOiAke0JCX1JFRElTX1BBU1NXT1JEfVxuICAgICAgQ09VQ0hfREJfVVNFUk5BTUU6IGJ1ZGliYXNlXG4gICAgICBDT1VDSF9EQl9QQVNTV09SRDogJHtCQl9DT1VDSERCX1BBU1NXT1JEfVxuICAgICAgQ09VQ0hfREJfVVJMOiBodHRwOi8vYnVkaWJhc2U6JHtCQl9DT1VDSERCX1BBU1NXT1JEfUBjb3VjaGRiOjU5ODRcbiAgICAgIEJVRElCQVNFX0VOVklST05NRU5UOiAke0JVRElCQVNFX0VOVklST05NRU5UOi1QUk9EVUNUSU9OfVxuICAgICAgRU5BQkxFX0FOQUxZVElDUzogJHtFTkFCTEVfQU5BTFlUSUNTOi10cnVlfVxuICAgIGRlcGVuZHNfb246XG4gICAgICByZWRpczpcbiAgICAgICAgY29uZGl0aW9uOiBzZXJ2aWNlX2hlYWx0aHlcbiAgICAgIG1pbmlvOlxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2VfaGVhbHRoeVxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDpcbiAgICAgICAgLSBDTURcbiAgICAgICAgLSB3Z2V0XG4gICAgICAgIC0gJy0tc3BpZGVyJ1xuICAgICAgICAtICctcU8tJ1xuICAgICAgICAtICdodHRwOi8vbG9jYWxob3N0OjQwMDMvaGVhbHRoJ1xuICAgICAgaW50ZXJ2YWw6IDE1c1xuICAgICAgdGltZW91dDogMTVzXG4gICAgICByZXRyaWVzOiA1XG4gICAgICBzdGFydF9wZXJpb2Q6IDEwc1xuXG4gIG1pbmlvOlxuICAgIGltYWdlOiBtaW5pby9taW5pbzpSRUxFQVNFLjIwMjUtMDktMDdUMTYtMTMtMDlaXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICB2b2x1bWVzOlxuICAgICAgLSAnbWluaW9fZGF0YTovZGF0YSdcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIE1JTklPX1JPT1RfVVNFUjogJHtCQl9NSU5JT19BQ0NFU1NfS0VZfVxuICAgICAgTUlOSU9fUk9PVF9QQVNTV09SRDogJHtCQl9NSU5JT19TRUNSRVRfS0VZfVxuICAgICAgTUlOSU9fQlJPV1NFUjogb2ZmXG4gICAgY29tbWFuZDogJ3NlcnZlciAvZGF0YSAtLWNvbnNvbGUtYWRkcmVzcyBcIjo5MDAxXCInXG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OlxuICAgICAgICAtIENNRFxuICAgICAgICAtIGN1cmxcbiAgICAgICAgLSAnLWYnXG4gICAgICAgIC0gJ2h0dHA6Ly9sb2NhbGhvc3Q6OTAwMC9taW5pby9oZWFsdGgvbGl2ZSdcbiAgICAgIGludGVydmFsOiAzMHNcbiAgICAgIHRpbWVvdXQ6IDIwc1xuICAgICAgcmV0cmllczogM1xuXG4gIHByb3h5OlxuICAgIGltYWdlOiBidWRpYmFzZS9wcm94eTozLjIzLjQ3XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIFBST1hZX1JBVEVfTElNSVRfV0VCSE9PS1NfUEVSX1NFQ09ORDogMTBcbiAgICAgIFBST1hZX1JBVEVfTElNSVRfQVBJX1BFUl9TRUNPTkQ6IDIwXG4gICAgICBBUFBTX1VQU1RSRUFNX1VSTDogaHR0cDovL2FwcHM6NDAwMlxuICAgICAgV09SS0VSX1VQU1RSRUFNX1VSTDogaHR0cDovL3dvcmtlcjo0MDAzXG4gICAgICBNSU5JT19VUFNUUkVBTV9VUkw6IGh0dHA6Ly9taW5pbzo5MDAwXG4gICAgICBDT1VDSERCX1VQU1RSRUFNX1VSTDogaHR0cDovL2NvdWNoZGI6NTk4NFxuICAgICAgV0FUQ0hUT1dFUl9VUFNUUkVBTV9VUkw6IGh0dHA6Ly93YXRjaHRvd2VyOjgwODBcbiAgICAgIFJFU09MVkVSOiAxMjcuMC4wLjExXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIG1pbmlvOlxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2VfaGVhbHRoeVxuICAgICAgd29ya2VyOlxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2VfaGVhbHRoeVxuICAgICAgYXBwczpcbiAgICAgICAgY29uZGl0aW9uOiBzZXJ2aWNlX2hlYWx0aHlcbiAgICAgIGNvdWNoZGI6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9oZWFsdGh5XG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OlxuICAgICAgICAtIENNRFxuICAgICAgICAtIGN1cmxcbiAgICAgICAgLSAnLWYnXG4gICAgICAgIC0gJ2h0dHA6Ly9sb2NhbGhvc3Q6MTAwMDAvJ1xuICAgICAgaW50ZXJ2YWw6IDE1c1xuICAgICAgdGltZW91dDogMTVzXG4gICAgICByZXRyaWVzOiA1XG4gICAgICBzdGFydF9wZXJpb2Q6IDEwc1xuXG4gIGNvdWNoZGI6XG4gICAgaW1hZ2U6IGJ1ZGliYXNlL2NvdWNoZGI6djMuMy4zXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIENPVUNIREJfVVNFUjogYnVkaWJhc2VcbiAgICAgIENPVUNIREJfUEFTU1dPUkQ6ICR7QkJfQ09VQ0hEQl9QQVNTV09SRH1cbiAgICAgIFRBUkdFVEJVSUxEOiBkb2NrZXItY29tcG9zZVxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDpcbiAgICAgICAgLSBDTURcbiAgICAgICAgLSBjdXJsXG4gICAgICAgIC0gJy1mJ1xuICAgICAgICAtICdodHRwOi8vbG9jYWxob3N0OjU5ODQvJ1xuICAgICAgaW50ZXJ2YWw6IDE1c1xuICAgICAgdGltZW91dDogMTVzXG4gICAgICByZXRyaWVzOiA1XG4gICAgICBzdGFydF9wZXJpb2Q6IDEwc1xuICAgIHZvbHVtZXM6XG4gICAgICAtICdjb3VjaGRiM19kYXRhOi9vcHQvY291Y2hkYi9kYXRhJ1xuXG4gIHJlZGlzOlxuICAgIGltYWdlOiByZWRpczo4LjQtYWxwaW5lXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBjb21tYW5kOiAncmVkaXMtc2VydmVyIC0tcmVxdWlyZXBhc3MgXCIke0JCX1JFRElTX1BBU1NXT1JEfVwiJ1xuICAgIHZvbHVtZXM6XG4gICAgICAtICdyZWRpc19kYXRhOi9kYXRhJ1xuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDpcbiAgICAgICAgLSBDTURcbiAgICAgICAgLSByZWRpcy1jbGlcbiAgICAgICAgLSAnLWEnXG4gICAgICAgIC0gJHtCQl9SRURJU19QQVNTV09SRH1cbiAgICAgICAgLSBwaW5nXG4gICAgICBpbnRlcnZhbDogMTVzXG4gICAgICB0aW1lb3V0OiAxNXNcbiAgICAgIHJldHJpZXM6IDVcbiAgICAgIHN0YXJ0X3BlcmlvZDogMTBzXG5cblxudm9sdW1lczpcbiAgbWluaW9fZGF0YTpcbiAgY291Y2hkYjNfZGF0YTpcbiAgcmVkaXNfZGF0YTogXG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuYXBpX2tleSA9IFwiJHtwYXNzd29yZDozMn1cIlxuZW5jcnlwdGlvbl9rZXkgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcbmp3dF9zZWNyZXQgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcbmNvdWNoZGJfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcbnJlZGlzX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5taW5pb19hY2Nlc3Nfa2V5ID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5taW5pb19zZWNyZXRfa2V5ID0gXCIke3Bhc3N3b3JkOjMyfVwiXG53YXRjaHRvd2VyX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5cbltjb25maWddXG5lbnYgPSBbXG4gIFwiQkJfSE9TVD0ke21haW5fZG9tYWlufVwiLFxuICBcIkJCX0lOVEVSTkFMX0FQSV9LRVk9JHthcGlfa2V5fVwiLFxuICBcIkJCX0FQSV9FTkNSWVBUSU9OX0tFWT0ke2VuY3J5cHRpb25fa2V5fVwiLFxuICBcIkJCX0pXVF9TRUNSRVQ9JHtqd3Rfc2VjcmV0fVwiLFxuICBcIkJCX0NPVUNIREJfUEFTU1dPUkQ9JHtjb3VjaGRiX3Bhc3N3b3JkfVwiLFxuICBcIkJCX1JFRElTX1BBU1NXT1JEPSR7cmVkaXNfcGFzc3dvcmR9XCIsXG4gIFwiQkJfV0FUQ0hUT1dFUl9QQVNTV09SRD0ke3dhdGNodG93ZXJfcGFzc3dvcmR9XCIsXG4gIFwiQkJfTUlOSU9fQUNDRVNTX0tFWT0ke21pbmlvX2FjY2Vzc19rZXl9XCIsXG4gIFwiQkJfTUlOSU9fU0VDUkVUX0tFWT0ke21pbmlvX3NlY3JldF9rZXl9XCIsXG5dXG5tb3VudHMgPSBbXVxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJwcm94eVwiXG5wb3J0ID0gMTBfMDAwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG4iCn0=
```

## Links

- Website
- Github
- Documentation

`database`,`low-code`,`nocode`,`applications`

---

Version:`3.23.47`

Budget BoardSelf-hosted budgeting app with a web UI and a server backed by PostgreSQL.

BugsinkBugsink is a self-hosted Error Tracker. Built to self-host; Sentry-SDK compatible; Scalable and reliable

### On this page

ConfigurationBase64LinksTags

