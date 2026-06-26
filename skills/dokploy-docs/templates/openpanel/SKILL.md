---
title: "OpenPanel | Dokploy"
source: "https://docs.dokploy.com/docs/templates/openpanel"
category: dokploy-docs
created: "2026-06-25T17:21:55.476Z"
---

OpenPanel | Dokploy

# OpenPanel

Copy as Markdown

An open-source web and product analytics platform that combines the power of Mixpanel with the ease of Plausible and one of the best Google Analytics replacements.

## Configuration

docker-compose.ymltemplate.toml

```
x-common: &x-common
  NODE_ENV: production
  SELF_HOSTED: "true"
  API_URL: ${API_URL}
  DASHBOARD_URL: ${DASHBOARD_URL}
  DATABASE_URL: postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@op-db:5432/${POSTGRES_DB}?schema=public
  DATABASE_URL_DIRECT: postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@op-db:5432/${POSTGRES_DB}?schema=public
  REDIS_URL: redis://default:${REDIS_PASSWORD}@op-kv:6379
  CLICKHOUSE_URL: http://op-ch:8123/openpanel

services:
  op-db:
    image: postgres:14-alpine
    restart: always
    volumes:
      - op-db-data:/var/lib/postgresql/data
    healthcheck:
      test: ['CMD-SHELL', 'pg_isready -U $${POSTGRES_USER} -d $${POSTGRES_DB}']
      interval: 10s
      timeout: 5s
      retries: 5
    environment:
      - POSTGRES_DB=${POSTGRES_DB}
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}

  op-kv:
    image: redis:7.2.5-alpine
    restart: always
    volumes:
      - op-kv-data:/data
    command: redis-server --requirepass ${REDIS_PASSWORD} --maxmemory-policy noeviction
    healthcheck:
      test: ['CMD', 'redis-cli', '-a', '${REDIS_PASSWORD}', 'ping']
      interval: 10s
      timeout: 5s
      retries: 5

  op-ch:
    image: clickhouse/clickhouse-server:25.10.2.65
    restart: always
    volumes:
      - op-ch-data:/var/lib/clickhouse
      - op-ch-logs:/var/log/clickhouse-server
      - ../files/clickhouse_config:/etc/clickhouse-server/config.d
      - ../files/clickhouse_users:/etc/clickhouse-server/users.d
      - ../files/clickhouse_init:/docker-entrypoint-initdb.d
    environment:
      - CLICKHOUSE_SKIP_USER_SETUP=1
    healthcheck:
      test: ['CMD-SHELL', 'clickhouse-client --query "SELECT 1" -d openpanel']
      interval: 10s
      timeout: 5s
      retries: 5

  op-api:
    image: lindesvard/openpanel-api:2
    restart: always
    command: >
      sh -c "
        echo 'Waiting for PostgreSQL to be ready...'
        while ! nc -z op-db 5432; do
          sleep 1
        done
        echo 'PostgreSQL is ready'

        echo 'Waiting for ClickHouse to be ready...'
        while ! nc -z op-ch 8123; do
          sleep 1
        done
        echo 'ClickHouse is ready'

        echo 'Running migrations...'

        CI=true pnpm -r run migrate:deploy

        pnpm start
      "
    environment:
      COOKIE_SECRET: ${COOKIE_SECRET}
      ALLOW_REGISTRATION: ${ALLOW_REGISTRATION}
      ALLOW_INVITATION: ${ALLOW_INVITATION}
      EMAIL_SENDER: ${EMAIL_SENDER}
      RESEND_API_KEY: ${RESEND_API_KEY}
      <<: *x-common
    healthcheck:
      test: ['CMD-SHELL', 'curl -f http://localhost:3000/healthcheck || exit 1']
      interval: 10s
      timeout: 5s
      retries: 5
    depends_on:
      op-db:
        condition: service_healthy
      op-ch:
        condition: service_healthy
      op-kv:
        condition: service_healthy

  op-dashboard:
    image: lindesvard/openpanel-dashboard:2
    restart: always
    depends_on:
      op-api:
        condition: service_healthy
    environment:
      <<: *x-common
    healthcheck:
      test: ['CMD-SHELL', 'curl -f http://localhost:3000/api/healthcheck || exit 1']
      interval: 10s
      timeout: 5s
      retries: 5

  op-worker:
    image: lindesvard/openpanel-worker:2
    restart: always
    depends_on:
      op-api:
        condition: service_healthy
    environment:
      <<: *x-common
    healthcheck:
      test: ['CMD-SHELL', 'curl -f http://localhost:3000/healthcheck || exit 1']
      interval: 10s
      timeout: 5s
      retries: 5

volumes:
  op-db-data:
  op-kv-data:
  op-ch-data:
  op-ch-logs:
```

```
[variables]
main_domain = "${domain}"
db_password = "${password:32}"
cookie_secret = "${base64:32}"
redis_password = "${password:32}"

[config]
# ClickHouse config files - mounted as directories
[[config.mounts]]
filePath = "./clickhouse_config/op-config.xml"
content = """
<clickhouse>
    <logger>
        <level>warning</level>
        <console>true</console>
    </logger>
    <keep_alive_timeout>10</keep_alive_timeout>
    <!-- Stop all the unnecessary logging -->
    <query_thread_log remove="remove"/>
    <query_log remove="remove"/>
    <text_log remove="remove"/>
    <trace_log remove="remove"/>
    <metric_log remove="remove"/>
    <asynchronous_metric_log remove="remove"/>
    <session_log remove="remove"/>
    <part_log remove="remove"/>
    <listen_host>0.0.0.0</listen_host>
    <interserver_listen_host>0.0.0.0</interserver_listen_host>
    <interserver_http_host>opch</interserver_http_host>
    <!-- Disable cgroup memory observer -->
    <cgroups_memory_usage_observer_wait_time>0</cgroups_memory_usage_observer_wait_time>
    <!-- Not used anymore, but kept for backwards compatibility -->
    <macros>
        <shard>1</shard>
        <replica>replica1</replica>
        <cluster>openpanel_cluster</cluster>
    </macros>
</clickhouse>
"""

[[config.mounts]]
filePath = "./clickhouse_users/op-user-config.xml"
content = """
<clickhouse>
    <profiles>
        <default>
            <log_queries>0</log_queries>
            <log_query_threads>0</log_query_threads>
        </default>
    </profiles>
</clickhouse>
"""

[[config.mounts]]
filePath = "./clickhouse_init/1_init-db.sql"
content = """
CREATE DATABASE IF NOT EXISTS openpanel;
"""

[[config.domains]]
serviceName = "op-dashboard"
port = 3000
host = "${main_domain}"

[[config.domains]]
serviceName = "op-api"
port = 3000
host = "${main_domain}"
path = "/api"
stripPath = true

[config.env]
DASHBOARD_URL = "http://${main_domain}"
API_URL = "http://${main_domain}/api"

# Database configuration
POSTGRES_DB = "openpanel"
POSTGRES_USER = "openpanel"
POSTGRES_PASSWORD = "${db_password}"
REDIS_PASSWORD = "${redis_password}"

# Security
COOKIE_SECRET = "${cookie_secret}"

# Registration settings
ALLOW_REGISTRATION = "true"
ALLOW_INVITATION = "true"

# Email configuration (optional - configure for email notifications)
EMAIL_SENDER = ""
RESEND_API_KEY = ""
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogIngtY29tbW9uOiAmeC1jb21tb25cbiAgTk9ERV9FTlY6IHByb2R1Y3Rpb25cbiAgU0VMRl9IT1NURUQ6IFwidHJ1ZVwiXG4gIEFQSV9VUkw6ICR7QVBJX1VSTH1cbiAgREFTSEJPQVJEX1VSTDogJHtEQVNIQk9BUkRfVVJMfVxuICBEQVRBQkFTRV9VUkw6IHBvc3RncmVzOi8vJHtQT1NUR1JFU19VU0VSfToke1BPU1RHUkVTX1BBU1NXT1JEfUBvcC1kYjo1NDMyLyR7UE9TVEdSRVNfREJ9P3NjaGVtYT1wdWJsaWNcbiAgREFUQUJBU0VfVVJMX0RJUkVDVDogcG9zdGdyZXM6Ly8ke1BPU1RHUkVTX1VTRVJ9OiR7UE9TVEdSRVNfUEFTU1dPUkR9QG9wLWRiOjU0MzIvJHtQT1NUR1JFU19EQn0/c2NoZW1hPXB1YmxpY1xuICBSRURJU19VUkw6IHJlZGlzOi8vZGVmYXVsdDoke1JFRElTX1BBU1NXT1JEfUBvcC1rdjo2Mzc5XG4gIENMSUNLSE9VU0VfVVJMOiBodHRwOi8vb3AtY2g6ODEyMy9vcGVucGFuZWxcblxuc2VydmljZXM6XG4gIG9wLWRiOlxuICAgIGltYWdlOiBwb3N0Z3JlczoxNC1hbHBpbmVcbiAgICByZXN0YXJ0OiBhbHdheXNcbiAgICB2b2x1bWVzOlxuICAgICAgLSBvcC1kYi1kYXRhOi92YXIvbGliL3Bvc3RncmVzcWwvZGF0YVxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDogWydDTUQtU0hFTEwnLCAncGdfaXNyZWFkeSAtVSAkJHtQT1NUR1JFU19VU0VSfSAtZCAkJHtQT1NUR1JFU19EQn0nXVxuICAgICAgaW50ZXJ2YWw6IDEwc1xuICAgICAgdGltZW91dDogNXNcbiAgICAgIHJldHJpZXM6IDVcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gUE9TVEdSRVNfREI9JHtQT1NUR1JFU19EQn1cbiAgICAgIC0gUE9TVEdSRVNfVVNFUj0ke1BPU1RHUkVTX1VTRVJ9XG4gICAgICAtIFBPU1RHUkVTX1BBU1NXT1JEPSR7UE9TVEdSRVNfUEFTU1dPUkR9XG5cbiAgb3Ata3Y6XG4gICAgaW1hZ2U6IHJlZGlzOjcuMi41LWFscGluZVxuICAgIHJlc3RhcnQ6IGFsd2F5c1xuICAgIHZvbHVtZXM6XG4gICAgICAtIG9wLWt2LWRhdGE6L2RhdGFcbiAgICBjb21tYW5kOiByZWRpcy1zZXJ2ZXIgLS1yZXF1aXJlcGFzcyAke1JFRElTX1BBU1NXT1JEfSAtLW1heG1lbW9yeS1wb2xpY3kgbm9ldmljdGlvblxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDogWydDTUQnLCAncmVkaXMtY2xpJywgJy1hJywgJyR7UkVESVNfUEFTU1dPUkR9JywgJ3BpbmcnXVxuICAgICAgaW50ZXJ2YWw6IDEwc1xuICAgICAgdGltZW91dDogNXNcbiAgICAgIHJldHJpZXM6IDVcblxuICBvcC1jaDpcbiAgICBpbWFnZTogY2xpY2tob3VzZS9jbGlja2hvdXNlLXNlcnZlcjoyNS4xMC4yLjY1XG4gICAgcmVzdGFydDogYWx3YXlzXG4gICAgdm9sdW1lczpcbiAgICAgIC0gb3AtY2gtZGF0YTovdmFyL2xpYi9jbGlja2hvdXNlXG4gICAgICAtIG9wLWNoLWxvZ3M6L3Zhci9sb2cvY2xpY2tob3VzZS1zZXJ2ZXJcbiAgICAgIC0gLi4vZmlsZXMvY2xpY2tob3VzZV9jb25maWc6L2V0Yy9jbGlja2hvdXNlLXNlcnZlci9jb25maWcuZFxuICAgICAgLSAuLi9maWxlcy9jbGlja2hvdXNlX3VzZXJzOi9ldGMvY2xpY2tob3VzZS1zZXJ2ZXIvdXNlcnMuZFxuICAgICAgLSAuLi9maWxlcy9jbGlja2hvdXNlX2luaXQ6L2RvY2tlci1lbnRyeXBvaW50LWluaXRkYi5kXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIENMSUNLSE9VU0VfU0tJUF9VU0VSX1NFVFVQPTFcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6IFsnQ01ELVNIRUxMJywgJ2NsaWNraG91c2UtY2xpZW50IC0tcXVlcnkgXCJTRUxFQ1QgMVwiIC1kIG9wZW5wYW5lbCddXG4gICAgICBpbnRlcnZhbDogMTBzXG4gICAgICB0aW1lb3V0OiA1c1xuICAgICAgcmV0cmllczogNVxuXG4gIG9wLWFwaTpcbiAgICBpbWFnZTogbGluZGVzdmFyZC9vcGVucGFuZWwtYXBpOjJcbiAgICByZXN0YXJ0OiBhbHdheXNcbiAgICBjb21tYW5kOiA+XG4gICAgICBzaCAtYyBcIlxuICAgICAgICBlY2hvICdXYWl0aW5nIGZvciBQb3N0Z3JlU1FMIHRvIGJlIHJlYWR5Li4uJ1xuICAgICAgICB3aGlsZSAhIG5jIC16IG9wLWRiIDU0MzI7IGRvXG4gICAgICAgICAgc2xlZXAgMVxuICAgICAgICBkb25lXG4gICAgICAgIGVjaG8gJ1Bvc3RncmVTUUwgaXMgcmVhZHknXG5cbiAgICAgICAgZWNobyAnV2FpdGluZyBmb3IgQ2xpY2tIb3VzZSB0byBiZSByZWFkeS4uLidcbiAgICAgICAgd2hpbGUgISBuYyAteiBvcC1jaCA4MTIzOyBkb1xuICAgICAgICAgIHNsZWVwIDFcbiAgICAgICAgZG9uZVxuICAgICAgICBlY2hvICdDbGlja0hvdXNlIGlzIHJlYWR5J1xuXG4gICAgICAgIGVjaG8gJ1J1bm5pbmcgbWlncmF0aW9ucy4uLidcblxuICAgICAgICBDST10cnVlIHBucG0gLXIgcnVuIG1pZ3JhdGU6ZGVwbG95XG5cbiAgICAgICAgcG5wbSBzdGFydFxuICAgICAgXCJcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIENPT0tJRV9TRUNSRVQ6ICR7Q09PS0lFX1NFQ1JFVH1cbiAgICAgIEFMTE9XX1JFR0lTVFJBVElPTjogJHtBTExPV19SRUdJU1RSQVRJT059XG4gICAgICBBTExPV19JTlZJVEFUSU9OOiAke0FMTE9XX0lOVklUQVRJT059XG4gICAgICBFTUFJTF9TRU5ERVI6ICR7RU1BSUxfU0VOREVSfVxuICAgICAgUkVTRU5EX0FQSV9LRVk6ICR7UkVTRU5EX0FQSV9LRVl9XG4gICAgICA8PDogKngtY29tbW9uXG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OiBbJ0NNRC1TSEVMTCcsICdjdXJsIC1mIGh0dHA6Ly9sb2NhbGhvc3Q6MzAwMC9oZWFsdGhjaGVjayB8fCBleGl0IDEnXVxuICAgICAgaW50ZXJ2YWw6IDEwc1xuICAgICAgdGltZW91dDogNXNcbiAgICAgIHJldHJpZXM6IDVcbiAgICBkZXBlbmRzX29uOlxuICAgICAgb3AtZGI6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9oZWFsdGh5XG4gICAgICBvcC1jaDpcbiAgICAgICAgY29uZGl0aW9uOiBzZXJ2aWNlX2hlYWx0aHlcbiAgICAgIG9wLWt2OlxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2VfaGVhbHRoeVxuXG4gIG9wLWRhc2hib2FyZDpcbiAgICBpbWFnZTogbGluZGVzdmFyZC9vcGVucGFuZWwtZGFzaGJvYXJkOjJcbiAgICByZXN0YXJ0OiBhbHdheXNcbiAgICBkZXBlbmRzX29uOlxuICAgICAgb3AtYXBpOlxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2VfaGVhbHRoeVxuICAgIGVudmlyb25tZW50OlxuICAgICAgPDw6ICp4LWNvbW1vblxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDogWydDTUQtU0hFTEwnLCAnY3VybCAtZiBodHRwOi8vbG9jYWxob3N0OjMwMDAvYXBpL2hlYWx0aGNoZWNrIHx8IGV4aXQgMSddXG4gICAgICBpbnRlcnZhbDogMTBzXG4gICAgICB0aW1lb3V0OiA1c1xuICAgICAgcmV0cmllczogNVxuXG4gIG9wLXdvcmtlcjpcbiAgICBpbWFnZTogbGluZGVzdmFyZC9vcGVucGFuZWwtd29ya2VyOjJcbiAgICByZXN0YXJ0OiBhbHdheXNcbiAgICBkZXBlbmRzX29uOlxuICAgICAgb3AtYXBpOlxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2VfaGVhbHRoeVxuICAgIGVudmlyb25tZW50OlxuICAgICAgPDw6ICp4LWNvbW1vblxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDogWydDTUQtU0hFTEwnLCAnY3VybCAtZiBodHRwOi8vbG9jYWxob3N0OjMwMDAvaGVhbHRoY2hlY2sgfHwgZXhpdCAxJ11cbiAgICAgIGludGVydmFsOiAxMHNcbiAgICAgIHRpbWVvdXQ6IDVzXG4gICAgICByZXRyaWVzOiA1XG5cbnZvbHVtZXM6XG4gIG9wLWRiLWRhdGE6XG4gIG9wLWt2LWRhdGE6XG4gIG9wLWNoLWRhdGE6XG4gIG9wLWNoLWxvZ3M6XG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuZGJfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcbmNvb2tpZV9zZWNyZXQgPSBcIiR7YmFzZTY0OjMyfVwiXG5yZWRpc19wYXNzd29yZCA9IFwiJHtwYXNzd29yZDozMn1cIlxuXG5bY29uZmlnXVxuIyBDbGlja0hvdXNlIGNvbmZpZyBmaWxlcyAtIG1vdW50ZWQgYXMgZGlyZWN0b3JpZXNcbltbY29uZmlnLm1vdW50c11dXG5maWxlUGF0aCA9IFwiLi9jbGlja2hvdXNlX2NvbmZpZy9vcC1jb25maWcueG1sXCJcbmNvbnRlbnQgPSBcIlwiXCJcbjxjbGlja2hvdXNlPlxuICAgIDxsb2dnZXI+XG4gICAgICAgIDxsZXZlbD53YXJuaW5nPC9sZXZlbD5cbiAgICAgICAgPGNvbnNvbGU+dHJ1ZTwvY29uc29sZT5cbiAgICA8L2xvZ2dlcj5cbiAgICA8a2VlcF9hbGl2ZV90aW1lb3V0PjEwPC9rZWVwX2FsaXZlX3RpbWVvdXQ+XG4gICAgPCEtLSBTdG9wIGFsbCB0aGUgdW5uZWNlc3NhcnkgbG9nZ2luZyAtLT5cbiAgICA8cXVlcnlfdGhyZWFkX2xvZyByZW1vdmU9XCJyZW1vdmVcIi8+XG4gICAgPHF1ZXJ5X2xvZyByZW1vdmU9XCJyZW1vdmVcIi8+XG4gICAgPHRleHRfbG9nIHJlbW92ZT1cInJlbW92ZVwiLz5cbiAgICA8dHJhY2VfbG9nIHJlbW92ZT1cInJlbW92ZVwiLz5cbiAgICA8bWV0cmljX2xvZyByZW1vdmU9XCJyZW1vdmVcIi8+XG4gICAgPGFzeW5jaHJvbm91c19tZXRyaWNfbG9nIHJlbW92ZT1cInJlbW92ZVwiLz5cbiAgICA8c2Vzc2lvbl9sb2cgcmVtb3ZlPVwicmVtb3ZlXCIvPlxuICAgIDxwYXJ0X2xvZyByZW1vdmU9XCJyZW1vdmVcIi8+XG4gICAgPGxpc3Rlbl9ob3N0PjAuMC4wLjA8L2xpc3Rlbl9ob3N0PlxuICAgIDxpbnRlcnNlcnZlcl9saXN0ZW5faG9zdD4wLjAuMC4wPC9pbnRlcnNlcnZlcl9saXN0ZW5faG9zdD5cbiAgICA8aW50ZXJzZXJ2ZXJfaHR0cF9ob3N0Pm9wY2g8L2ludGVyc2VydmVyX2h0dHBfaG9zdD5cbiAgICA8IS0tIERpc2FibGUgY2dyb3VwIG1lbW9yeSBvYnNlcnZlciAtLT5cbiAgICA8Y2dyb3Vwc19tZW1vcnlfdXNhZ2Vfb2JzZXJ2ZXJfd2FpdF90aW1lPjA8L2Nncm91cHNfbWVtb3J5X3VzYWdlX29ic2VydmVyX3dhaXRfdGltZT5cbiAgICA8IS0tIE5vdCB1c2VkIGFueW1vcmUsIGJ1dCBrZXB0IGZvciBiYWNrd2FyZHMgY29tcGF0aWJpbGl0eSAtLT5cbiAgICA8bWFjcm9zPlxuICAgICAgICA8c2hhcmQ+MTwvc2hhcmQ+XG4gICAgICAgIDxyZXBsaWNhPnJlcGxpY2ExPC9yZXBsaWNhPlxuICAgICAgICA8Y2x1c3Rlcj5vcGVucGFuZWxfY2x1c3RlcjwvY2x1c3Rlcj5cbiAgICA8L21hY3Jvcz5cbjwvY2xpY2tob3VzZT5cblwiXCJcIlxuXG5bW2NvbmZpZy5tb3VudHNdXVxuZmlsZVBhdGggPSBcIi4vY2xpY2tob3VzZV91c2Vycy9vcC11c2VyLWNvbmZpZy54bWxcIlxuY29udGVudCA9IFwiXCJcIlxuPGNsaWNraG91c2U+XG4gICAgPHByb2ZpbGVzPlxuICAgICAgICA8ZGVmYXVsdD5cbiAgICAgICAgICAgIDxsb2dfcXVlcmllcz4wPC9sb2dfcXVlcmllcz5cbiAgICAgICAgICAgIDxsb2dfcXVlcnlfdGhyZWFkcz4wPC9sb2dfcXVlcnlfdGhyZWFkcz5cbiAgICAgICAgPC9kZWZhdWx0PlxuICAgIDwvcHJvZmlsZXM+XG48L2NsaWNraG91c2U+XG5cIlwiXCJcblxuW1tjb25maWcubW91bnRzXV1cbmZpbGVQYXRoID0gXCIuL2NsaWNraG91c2VfaW5pdC8xX2luaXQtZGIuc3FsXCJcbmNvbnRlbnQgPSBcIlwiXCJcbkNSRUFURSBEQVRBQkFTRSBJRiBOT1QgRVhJU1RTIG9wZW5wYW5lbDtcblwiXCJcIlxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJvcC1kYXNoYm9hcmRcIlxucG9ydCA9IDMwMDBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwib3AtYXBpXCJcbnBvcnQgPSAzMDAwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5wYXRoID0gXCIvYXBpXCJcbnN0cmlwUGF0aCA9IHRydWVcblxuW2NvbmZpZy5lbnZdXG5EQVNIQk9BUkRfVVJMID0gXCJodHRwOi8vJHttYWluX2RvbWFpbn1cIlxuQVBJX1VSTCA9IFwiaHR0cDovLyR7bWFpbl9kb21haW59L2FwaVwiXG5cbiMgRGF0YWJhc2UgY29uZmlndXJhdGlvblxuUE9TVEdSRVNfREIgPSBcIm9wZW5wYW5lbFwiXG5QT1NUR1JFU19VU0VSID0gXCJvcGVucGFuZWxcIlxuUE9TVEdSRVNfUEFTU1dPUkQgPSBcIiR7ZGJfcGFzc3dvcmR9XCJcblJFRElTX1BBU1NXT1JEID0gXCIke3JlZGlzX3Bhc3N3b3JkfVwiXG5cbiMgU2VjdXJpdHlcbkNPT0tJRV9TRUNSRVQgPSBcIiR7Y29va2llX3NlY3JldH1cIlxuXG4jIFJlZ2lzdHJhdGlvbiBzZXR0aW5nc1xuQUxMT1dfUkVHSVNUUkFUSU9OID0gXCJ0cnVlXCJcbkFMTE9XX0lOVklUQVRJT04gPSBcInRydWVcIlxuXG4jIEVtYWlsIGNvbmZpZ3VyYXRpb24gKG9wdGlvbmFsIC0gY29uZmlndXJlIGZvciBlbWFpbCBub3RpZmljYXRpb25zKVxuRU1BSUxfU0VOREVSID0gXCJcIlxuUkVTRU5EX0FQSV9LRVkgPSBcIlwiXG4iCn0=
```

## Links

`analytics`

---

Version:`latest`

OpeninaryOpeninary is a self-hosted Cloudinary alternative.

OpenResty ManagerThe easiest using, powerful and beautiful OpenResty Manager (Nginx Enhanced Version) , open source alternative to OpenResty Edge, which can enable you to easily reverse proxy your websites with security running at home or internet, including Access Control, HTTP Flood Protection, Free SSL, without having to know too much about OpenResty or Let's Encrypt.

### On this page

ConfigurationBase64LinksTags