---
title: "Chatwoot | Dokploy"
source: "https://docs.dokploy.com/docs/templates/chatwoot"
category: dokploy-docs
created: "2026-06-25T17:21:43.962Z"
---

Chatwoot | Dokploy

# Chatwoot

Copy as Markdown

Open-source customer engagement platform that provides a shared inbox for teams, live chat, and omnichannel support.

## Configuration

docker-compose.ymltemplate.toml

```
version: '3'

x-base-config: &base-config
  image: chatwoot/chatwoot:v4.0.3
  volumes:
    - chatwoot-storage:/app/storage
  environment:
    - FRONTEND_URL=${FRONTEND_URL}
    - SECRET_KEY_BASE=${SECRET_KEY_BASE}
    - RAILS_ENV=${RAILS_ENV}
    - NODE_ENV=${NODE_ENV}
    - INSTALLATION_ENV=${INSTALLATION_ENV}
    - RAILS_LOG_TO_STDOUT=${RAILS_LOG_TO_STDOUT}
    - LOG_LEVEL=${LOG_LEVEL}
    - DEFAULT_LOCALE=${DEFAULT_LOCALE}
    - POSTGRES_HOST=${POSTGRES_HOST}
    - POSTGRES_PORT=${POSTGRES_PORT}
    - POSTGRES_DATABASE=${POSTGRES_DATABASE}
    - POSTGRES_USERNAME=${POSTGRES_USERNAME}
    - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
    - REDIS_URL=${REDIS_URL}
    - ENABLE_ACCOUNT_SIGNUP=${ENABLE_ACCOUNT_SIGNUP}
    - ACTIVE_STORAGE_SERVICE=${ACTIVE_STORAGE_SERVICE}

services:
  chatwoot-rails:
    <<: *base-config
    depends_on:
      chatwoot-postgres:
        condition: service_started
      chatwoot-redis:
        condition: service_started
    entrypoint: docker/entrypoints/rails.sh
    command: ['bundle', 'exec', 'sh', '-c', 'rails db:chatwoot_prepare && rails s -p 3000 -b 0.0.0.0']
    restart: always

  chatwoot-sidekiq:
    <<: *base-config
    depends_on:
      chatwoot-postgres:
        condition: service_started
      chatwoot-redis:
        condition: service_started
    command: ['bundle', 'exec', 'sidekiq', '-C', 'config/sidekiq.yml']
    restart: always

  chatwoot-postgres:
    image: pgvector/pgvector:pg14
    restart: always
    volumes:
      - chatwoot-postgres-data:/var/lib/postgresql/data
      - ./init-vector.sql:/docker-entrypoint-initdb.d/init-vector.sql
    environment:
      - POSTGRES_DB=${POSTGRES_DATABASE}
      - POSTGRES_USER=${POSTGRES_USERNAME}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}

  chatwoot-redis:
    image: redis:alpine
    restart: always
    volumes:
      - chatwoot-redis-data:/data

volumes:
  chatwoot-storage:
  chatwoot-postgres-data:
  chatwoot-redis-data:
```

```
[variables]
main_domain = "${domain}"
secret_key_base = "${base64:64}"
postgres_password = "${password}"

[config]
env = [
  "FRONTEND_URL=http://${main_domain}",
  "SECRET_KEY_BASE=${secret_key_base}",
  "RAILS_ENV=production",
  "NODE_ENV=production",
  "INSTALLATION_ENV=docker",
  "RAILS_LOG_TO_STDOUT=true",
  "LOG_LEVEL=info",
  "DEFAULT_LOCALE=en",
  "POSTGRES_HOST=chatwoot-postgres",
  "POSTGRES_PORT=5432",
  "POSTGRES_DATABASE=chatwoot",
  "POSTGRES_USERNAME=postgres",
  "POSTGRES_PASSWORD=${postgres_password}",
  "REDIS_URL=redis://chatwoot-redis:6379",
  "ENABLE_ACCOUNT_SIGNUP=false",
  "ACTIVE_STORAGE_SERVICE=local",
]
mounts = []

[[config.domains]]
serviceName = "chatwoot-rails"
port = 3_000
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246ICczJ1xuXG54LWJhc2UtY29uZmlnOiAmYmFzZS1jb25maWdcbiAgaW1hZ2U6IGNoYXR3b290L2NoYXR3b290OnY0LjAuM1xuICB2b2x1bWVzOlxuICAgIC0gY2hhdHdvb3Qtc3RvcmFnZTovYXBwL3N0b3JhZ2VcbiAgZW52aXJvbm1lbnQ6XG4gICAgLSBGUk9OVEVORF9VUkw9JHtGUk9OVEVORF9VUkx9XG4gICAgLSBTRUNSRVRfS0VZX0JBU0U9JHtTRUNSRVRfS0VZX0JBU0V9XG4gICAgLSBSQUlMU19FTlY9JHtSQUlMU19FTlZ9XG4gICAgLSBOT0RFX0VOVj0ke05PREVfRU5WfVxuICAgIC0gSU5TVEFMTEFUSU9OX0VOVj0ke0lOU1RBTExBVElPTl9FTlZ9XG4gICAgLSBSQUlMU19MT0dfVE9fU1RET1VUPSR7UkFJTFNfTE9HX1RPX1NURE9VVH1cbiAgICAtIExPR19MRVZFTD0ke0xPR19MRVZFTH1cbiAgICAtIERFRkFVTFRfTE9DQUxFPSR7REVGQVVMVF9MT0NBTEV9XG4gICAgLSBQT1NUR1JFU19IT1NUPSR7UE9TVEdSRVNfSE9TVH1cbiAgICAtIFBPU1RHUkVTX1BPUlQ9JHtQT1NUR1JFU19QT1JUfVxuICAgIC0gUE9TVEdSRVNfREFUQUJBU0U9JHtQT1NUR1JFU19EQVRBQkFTRX1cbiAgICAtIFBPU1RHUkVTX1VTRVJOQU1FPSR7UE9TVEdSRVNfVVNFUk5BTUV9XG4gICAgLSBQT1NUR1JFU19QQVNTV09SRD0ke1BPU1RHUkVTX1BBU1NXT1JEfVxuICAgIC0gUkVESVNfVVJMPSR7UkVESVNfVVJMfVxuICAgIC0gRU5BQkxFX0FDQ09VTlRfU0lHTlVQPSR7RU5BQkxFX0FDQ09VTlRfU0lHTlVQfVxuICAgIC0gQUNUSVZFX1NUT1JBR0VfU0VSVklDRT0ke0FDVElWRV9TVE9SQUdFX1NFUlZJQ0V9XG5cbnNlcnZpY2VzOlxuICBjaGF0d29vdC1yYWlsczpcbiAgICA8PDogKmJhc2UtY29uZmlnXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIGNoYXR3b290LXBvc3RncmVzOlxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2Vfc3RhcnRlZFxuICAgICAgY2hhdHdvb3QtcmVkaXM6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9zdGFydGVkXG4gICAgZW50cnlwb2ludDogZG9ja2VyL2VudHJ5cG9pbnRzL3JhaWxzLnNoXG4gICAgY29tbWFuZDogWydidW5kbGUnLCAnZXhlYycsICdzaCcsICctYycsICdyYWlscyBkYjpjaGF0d29vdF9wcmVwYXJlICYmIHJhaWxzIHMgLXAgMzAwMCAtYiAwLjAuMC4wJ11cbiAgICByZXN0YXJ0OiBhbHdheXNcblxuICBjaGF0d29vdC1zaWRla2lxOlxuICAgIDw8OiAqYmFzZS1jb25maWdcbiAgICBkZXBlbmRzX29uOlxuICAgICAgY2hhdHdvb3QtcG9zdGdyZXM6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9zdGFydGVkXG4gICAgICBjaGF0d29vdC1yZWRpczpcbiAgICAgICAgY29uZGl0aW9uOiBzZXJ2aWNlX3N0YXJ0ZWRcbiAgICBjb21tYW5kOiBbJ2J1bmRsZScsICdleGVjJywgJ3NpZGVraXEnLCAnLUMnLCAnY29uZmlnL3NpZGVraXEueW1sJ11cbiAgICByZXN0YXJ0OiBhbHdheXNcblxuICBjaGF0d29vdC1wb3N0Z3JlczpcbiAgICBpbWFnZTogcGd2ZWN0b3IvcGd2ZWN0b3I6cGcxNFxuICAgIHJlc3RhcnQ6IGFsd2F5c1xuICAgIHZvbHVtZXM6XG4gICAgICAtIGNoYXR3b290LXBvc3RncmVzLWRhdGE6L3Zhci9saWIvcG9zdGdyZXNxbC9kYXRhXG4gICAgICAtIC4vaW5pdC12ZWN0b3Iuc3FsOi9kb2NrZXItZW50cnlwb2ludC1pbml0ZGIuZC9pbml0LXZlY3Rvci5zcWxcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gUE9TVEdSRVNfREI9JHtQT1NUR1JFU19EQVRBQkFTRX1cbiAgICAgIC0gUE9TVEdSRVNfVVNFUj0ke1BPU1RHUkVTX1VTRVJOQU1FfVxuICAgICAgLSBQT1NUR1JFU19QQVNTV09SRD0ke1BPU1RHUkVTX1BBU1NXT1JEfVxuXG4gIGNoYXR3b290LXJlZGlzOlxuICAgIGltYWdlOiByZWRpczphbHBpbmVcbiAgICByZXN0YXJ0OiBhbHdheXNcbiAgICB2b2x1bWVzOlxuICAgICAgLSBjaGF0d29vdC1yZWRpcy1kYXRhOi9kYXRhXG5cbnZvbHVtZXM6XG4gIGNoYXR3b290LXN0b3JhZ2U6XG4gIGNoYXR3b290LXBvc3RncmVzLWRhdGE6XG4gIGNoYXR3b290LXJlZGlzLWRhdGE6IiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbnNlY3JldF9rZXlfYmFzZSA9IFwiJHtiYXNlNjQ6NjR9XCJcbnBvc3RncmVzX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkfVwiXG5cbltjb25maWddXG5lbnYgPSBbXG4gIFwiRlJPTlRFTkRfVVJMPWh0dHA6Ly8ke21haW5fZG9tYWlufVwiLFxuICBcIlNFQ1JFVF9LRVlfQkFTRT0ke3NlY3JldF9rZXlfYmFzZX1cIixcbiAgXCJSQUlMU19FTlY9cHJvZHVjdGlvblwiLFxuICBcIk5PREVfRU5WPXByb2R1Y3Rpb25cIixcbiAgXCJJTlNUQUxMQVRJT05fRU5WPWRvY2tlclwiLFxuICBcIlJBSUxTX0xPR19UT19TVERPVVQ9dHJ1ZVwiLFxuICBcIkxPR19MRVZFTD1pbmZvXCIsXG4gIFwiREVGQVVMVF9MT0NBTEU9ZW5cIixcbiAgXCJQT1NUR1JFU19IT1NUPWNoYXR3b290LXBvc3RncmVzXCIsXG4gIFwiUE9TVEdSRVNfUE9SVD01NDMyXCIsXG4gIFwiUE9TVEdSRVNfREFUQUJBU0U9Y2hhdHdvb3RcIixcbiAgXCJQT1NUR1JFU19VU0VSTkFNRT1wb3N0Z3Jlc1wiLFxuICBcIlBPU1RHUkVTX1BBU1NXT1JEPSR7cG9zdGdyZXNfcGFzc3dvcmR9XCIsXG4gIFwiUkVESVNfVVJMPXJlZGlzOi8vY2hhdHdvb3QtcmVkaXM6NjM3OVwiLFxuICBcIkVOQUJMRV9BQ0NPVU5UX1NJR05VUD1mYWxzZVwiLFxuICBcIkFDVElWRV9TVE9SQUdFX1NFUlZJQ0U9bG9jYWxcIixcbl1cbm1vdW50cyA9IFtdXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImNoYXR3b290LXJhaWxzXCJcbnBvcnQgPSAzXzAwMFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuIgp9
```

## Links

`support`,`chat`,`customer-service`

---

Version:`v3.14.1`

Change DetectionChangedetection.io is an intelligent tool designed to monitor changes on websites. Perfect for smart shoppers, data journalists, research engineers, data scientists, and security researchers.

CheckcleCheckcle is a security and compliance tool by Operacle, providing insights into system configuration and runtime checks.

### On this page

ConfigurationBase64LinksTags