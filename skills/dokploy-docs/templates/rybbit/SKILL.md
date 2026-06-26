---
title: "Rybbit | Dokploy"
source: "https://docs.dokploy.com/docs/templates/rybbit"
category: dokploy-docs
created: "2026-06-25T17:21:57.938Z"
---

Rybbit | Dokploy

# Rybbit

Copy as Markdown

Open-source and privacy-friendly alternative to Google Analytics that is 10x more intuitive

## Configuration

docker-compose.ymltemplate.toml

```
# https://www.rybbit.io/docs/self-hosting-advanced

# NOTE: there are two sample HTTP traefik domain entries created:
# - rybbit_backend (port 3001, path /api),
# - rybbit_client (port 3002, path /)
#
# You should treat these as placeholders - Rybbit only supports HTTPS.
#
# You should also update the `BASE_URL`, and `DOMAIN_NAME` environment
# variable when updating the domain entries with your custom domain.

services:
  rybbit_clickhouse:
    image: clickhouse/clickhouse-server:25.5
    volumes:
      - clickhouse_data:/var/lib/clickhouse
      - ../files/clickhouse_config:/etc/clickhouse-server/config.d
    environment:
      - CLICKHOUSE_DB=${CLICKHOUSE_DB}
      - CLICKHOUSE_USER=${CLICKHOUSE_USER}
      - CLICKHOUSE_PASSWORD=${CLICKHOUSE_PASSWORD}
    healthcheck:
      test:
        [
          "CMD",
          "wget",
          "--no-verbose",
          "--tries=1",
          "--spider",
          "http://localhost:8123/ping",
        ]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 10s
    restart: unless-stopped

  rybbit_postgres:
    image: postgres:17.5
    environment:
      - POSTGRES_DB=${POSTGRES_DB}
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U $${POSTGRES_USER} -d $${POSTGRES_DB}"]
      interval: 30s
      timeout: 10s
      retries: 3
    restart: unless-stopped

  rybbit_backend:
    image: ghcr.io/rybbit-io/rybbit-backend:v1.5.1
    environment:
      - NODE_ENV=production
      - CLICKHOUSE_HOST=http://rybbit_clickhouse:8123
      - CLICKHOUSE_DB=${CLICKHOUSE_DB}
      - CLICKHOUSE_USER=${CLICKHOUSE_USER}
      - CLICKHOUSE_PASSWORD=${CLICKHOUSE_PASSWORD}
      - POSTGRES_HOST=rybbit_postgres
      - POSTGRES_PORT=5432
      - POSTGRES_DB=${POSTGRES_DB}
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
      - BETTER_AUTH_SECRET=${BETTER_AUTH_SECRET}
      - BASE_URL=${BASE_URL}
      - DOMAIN_NAME=${DOMAIN_NAME}
      - DISABLE_SIGNUP=${DISABLE_SIGNUP}
    depends_on:
      rybbit_clickhouse:
        condition: service_healthy
      rybbit_postgres:
        condition: service_started
    healthcheck:
      test: ["CMD", "wget", "--no-verbose", "--tries=1", "--spider", "http://127.0.0.1:3001/api/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 10s
    restart: unless-stopped

  rybbit_client:
    image: ghcr.io/rybbit-io/rybbit-client:v1.5.1
    environment:
      - NODE_ENV=production
      - NEXT_PUBLIC_BACKEND_URL=${BASE_URL}
      - DOMAIN_NAME=${DOMAIN_NAME}
      - NEXT_PUBLIC_DISABLE_SIGNUP=${DISABLE_SIGNUP}
    depends_on:
      - rybbit_backend
    restart: unless-stopped

volumes:
  clickhouse_data:
  postgres_data:
```

```
[variables]
main_domain = "${domain}"
better_auth_secret = "${password:32}"
clickhouse_password = "${password:32}"
postgres_password = "${password:32}"

[[config.domains]]
serviceName = "rybbit_backend"
port = 3001
host = "${main_domain}"
path = "/api"

[[config.domains]]
serviceName = "rybbit_client"
port = 3002
host = "${main_domain}"

[config.env]
BASE_URL = "http://${main_domain}"
DOMAIN_NAME= "${main_domain}"
BETTER_AUTH_SECRET = "${better_auth_secret}"
DISABLE_SIGNUP = "false"
CLICKHOUSE_DB = "analytics"
CLICKHOUSE_USER = "default"
CLICKHOUSE_PASSWORD = "${clickhouse_password}"
POSTGRES_DB = "analytics"
POSTGRES_USER = "frog"
POSTGRES_PASSWORD = "${postgres_password}"

[[config.mounts]]
filePath = "./clickhouse_config/enable_json.xml"
content = """
<clickhouse>
    <settings>
        <enable_json_type>1</enable_json_type>
    </settings>
</clickhouse>
"""

[[config.mounts]]
filePath = "./clickhouse_config/logging_rules.xml"
content = """
<clickhouse>
    <logger>
        <level>warning</level>
        <console>true</console>
    </logger>
    <query_thread_log remove="remove"/>
    <query_log remove="remove"/>
    <text_log remove="remove"/>
    <trace_log remove="remove"/>
    <metric_log remove="remove"/>
    <asynchronous_metric_log remove="remove"/>
    <session_log remove="remove"/>
    <part_log remove="remove"/>
    <latency_log remove="remove"/>
    <processors_profile_log remove="remove"/>
</clickhouse>
"""

[[config.mounts]]
filePath = "./clickhouse_config/network.xml"
content = """
<clickhouse>
    <listen_host>0.0.0.0</listen_host>
</clickhouse>
"""

[[config.mounts]]
filePath = "./clickhouse_config/user_logging.xml"
content = """
<clickhouse>
    <profiles>
        <default>
            <log_queries>0</log_queries>
            <log_query_threads>0</log_query_threads>
            <log_processors_profiles>0</log_processors_profiles>
        </default>
    </profiles>
</clickhouse>
"""
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogIiMgaHR0cHM6Ly93d3cucnliYml0LmlvL2RvY3Mvc2VsZi1ob3N0aW5nLWFkdmFuY2VkXG5cbiMgTk9URTogdGhlcmUgYXJlIHR3byBzYW1wbGUgSFRUUCB0cmFlZmlrIGRvbWFpbiBlbnRyaWVzIGNyZWF0ZWQ6XG4jIC0gcnliYml0X2JhY2tlbmQgKHBvcnQgMzAwMSwgcGF0aCAvYXBpKSwgXG4jIC0gcnliYml0X2NsaWVudCAocG9ydCAzMDAyLCBwYXRoIC8pXG4jXG4jIFlvdSBzaG91bGQgdHJlYXQgdGhlc2UgYXMgcGxhY2Vob2xkZXJzIC0gUnliYml0IG9ubHkgc3VwcG9ydHMgSFRUUFMuXG4jXG4jIFlvdSBzaG91bGQgYWxzbyB1cGRhdGUgdGhlIGBCQVNFX1VSTGAsIGFuZCBgRE9NQUlOX05BTUVgIGVudmlyb25tZW50XG4jIHZhcmlhYmxlIHdoZW4gdXBkYXRpbmcgdGhlIGRvbWFpbiBlbnRyaWVzIHdpdGggeW91ciBjdXN0b20gZG9tYWluLlxuXG5zZXJ2aWNlczpcbiAgcnliYml0X2NsaWNraG91c2U6XG4gICAgaW1hZ2U6IGNsaWNraG91c2UvY2xpY2tob3VzZS1zZXJ2ZXI6MjUuNVxuICAgIHZvbHVtZXM6XG4gICAgICAtIGNsaWNraG91c2VfZGF0YTovdmFyL2xpYi9jbGlja2hvdXNlXG4gICAgICAtIC4uL2ZpbGVzL2NsaWNraG91c2VfY29uZmlnOi9ldGMvY2xpY2tob3VzZS1zZXJ2ZXIvY29uZmlnLmRcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gQ0xJQ0tIT1VTRV9EQj0ke0NMSUNLSE9VU0VfREJ9XG4gICAgICAtIENMSUNLSE9VU0VfVVNFUj0ke0NMSUNLSE9VU0VfVVNFUn1cbiAgICAgIC0gQ0xJQ0tIT1VTRV9QQVNTV09SRD0ke0NMSUNLSE9VU0VfUEFTU1dPUkR9XG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OlxuICAgICAgICBbXG4gICAgICAgICAgXCJDTURcIixcbiAgICAgICAgICBcIndnZXRcIixcbiAgICAgICAgICBcIi0tbm8tdmVyYm9zZVwiLFxuICAgICAgICAgIFwiLS10cmllcz0xXCIsXG4gICAgICAgICAgXCItLXNwaWRlclwiLFxuICAgICAgICAgIFwiaHR0cDovL2xvY2FsaG9zdDo4MTIzL3BpbmdcIixcbiAgICAgICAgXVxuICAgICAgaW50ZXJ2YWw6IDMwc1xuICAgICAgdGltZW91dDogMTBzXG4gICAgICByZXRyaWVzOiAzXG4gICAgICBzdGFydF9wZXJpb2Q6IDEwc1xuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG5cbiAgcnliYml0X3Bvc3RncmVzOlxuICAgIGltYWdlOiBwb3N0Z3JlczoxNy41XG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIFBPU1RHUkVTX0RCPSR7UE9TVEdSRVNfREJ9XG4gICAgICAtIFBPU1RHUkVTX1VTRVI9JHtQT1NUR1JFU19VU0VSfVxuICAgICAgLSBQT1NUR1JFU19QQVNTV09SRD0ke1BPU1RHUkVTX1BBU1NXT1JEfVxuICAgIHZvbHVtZXM6XG4gICAgICAtIHBvc3RncmVzX2RhdGE6L3Zhci9saWIvcG9zdGdyZXNxbC9kYXRhXG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OiBbXCJDTUQtU0hFTExcIiwgXCJwZ19pc3JlYWR5IC1VICQke1BPU1RHUkVTX1VTRVJ9IC1kICQke1BPU1RHUkVTX0RCfVwiXVxuICAgICAgaW50ZXJ2YWw6IDMwc1xuICAgICAgdGltZW91dDogMTBzXG4gICAgICByZXRyaWVzOiAzXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcblxuICByeWJiaXRfYmFja2VuZDpcbiAgICBpbWFnZTogZ2hjci5pby9yeWJiaXQtaW8vcnliYml0LWJhY2tlbmQ6djEuNS4xXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIE5PREVfRU5WPXByb2R1Y3Rpb25cbiAgICAgIC0gQ0xJQ0tIT1VTRV9IT1NUPWh0dHA6Ly9yeWJiaXRfY2xpY2tob3VzZTo4MTIzXG4gICAgICAtIENMSUNLSE9VU0VfREI9JHtDTElDS0hPVVNFX0RCfVxuICAgICAgLSBDTElDS0hPVVNFX1VTRVI9JHtDTElDS0hPVVNFX1VTRVJ9XG4gICAgICAtIENMSUNLSE9VU0VfUEFTU1dPUkQ9JHtDTElDS0hPVVNFX1BBU1NXT1JEfVxuICAgICAgLSBQT1NUR1JFU19IT1NUPXJ5YmJpdF9wb3N0Z3Jlc1xuICAgICAgLSBQT1NUR1JFU19QT1JUPTU0MzJcbiAgICAgIC0gUE9TVEdSRVNfREI9JHtQT1NUR1JFU19EQn1cbiAgICAgIC0gUE9TVEdSRVNfVVNFUj0ke1BPU1RHUkVTX1VTRVJ9XG4gICAgICAtIFBPU1RHUkVTX1BBU1NXT1JEPSR7UE9TVEdSRVNfUEFTU1dPUkR9XG4gICAgICAtIEJFVFRFUl9BVVRIX1NFQ1JFVD0ke0JFVFRFUl9BVVRIX1NFQ1JFVH1cbiAgICAgIC0gQkFTRV9VUkw9JHtCQVNFX1VSTH1cbiAgICAgIC0gRE9NQUlOX05BTUU9JHtET01BSU5fTkFNRX1cbiAgICAgIC0gRElTQUJMRV9TSUdOVVA9JHtESVNBQkxFX1NJR05VUH1cbiAgICBkZXBlbmRzX29uOlxuICAgICAgcnliYml0X2NsaWNraG91c2U6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9oZWFsdGh5XG4gICAgICByeWJiaXRfcG9zdGdyZXM6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9zdGFydGVkXG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OiBbXCJDTURcIiwgXCJ3Z2V0XCIsIFwiLS1uby12ZXJib3NlXCIsIFwiLS10cmllcz0xXCIsIFwiLS1zcGlkZXJcIiwgXCJodHRwOi8vMTI3LjAuMC4xOjMwMDEvYXBpL2hlYWx0aFwiXVxuICAgICAgaW50ZXJ2YWw6IDMwc1xuICAgICAgdGltZW91dDogMTBzXG4gICAgICByZXRyaWVzOiAzXG4gICAgICBzdGFydF9wZXJpb2Q6IDEwc1xuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG5cbiAgcnliYml0X2NsaWVudDpcbiAgICBpbWFnZTogZ2hjci5pby9yeWJiaXQtaW8vcnliYml0LWNsaWVudDp2MS41LjFcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gTk9ERV9FTlY9cHJvZHVjdGlvblxuICAgICAgLSBORVhUX1BVQkxJQ19CQUNLRU5EX1VSTD0ke0JBU0VfVVJMfVxuICAgICAgLSBET01BSU5fTkFNRT0ke0RPTUFJTl9OQU1FfVxuICAgICAgLSBORVhUX1BVQkxJQ19ESVNBQkxFX1NJR05VUD0ke0RJU0FCTEVfU0lHTlVQfVxuICAgIGRlcGVuZHNfb246XG4gICAgICAtIHJ5YmJpdF9iYWNrZW5kXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcblxudm9sdW1lczpcbiAgY2xpY2tob3VzZV9kYXRhOlxuICBwb3N0Z3Jlc19kYXRhOlxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbmJldHRlcl9hdXRoX3NlY3JldCA9IFwiJHtwYXNzd29yZDozMn1cIlxuY2xpY2tob3VzZV9wYXNzd29yZCA9IFwiJHtwYXNzd29yZDozMn1cIlxucG9zdGdyZXNfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwicnliYml0X2JhY2tlbmRcIlxucG9ydCA9IDMwMDFcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcbnBhdGggPSBcIi9hcGlcIlxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJyeWJiaXRfY2xpZW50XCJcbnBvcnQgPSAzMDAyXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuQkFTRV9VUkwgPSBcImh0dHA6Ly8ke21haW5fZG9tYWlufVwiXG5ET01BSU5fTkFNRT0gXCIke21haW5fZG9tYWlufVwiXG5CRVRURVJfQVVUSF9TRUNSRVQgPSBcIiR7YmV0dGVyX2F1dGhfc2VjcmV0fVwiXG5ESVNBQkxFX1NJR05VUCA9IFwiZmFsc2VcIlxuQ0xJQ0tIT1VTRV9EQiA9IFwiYW5hbHl0aWNzXCJcbkNMSUNLSE9VU0VfVVNFUiA9IFwiZGVmYXVsdFwiXG5DTElDS0hPVVNFX1BBU1NXT1JEID0gXCIke2NsaWNraG91c2VfcGFzc3dvcmR9XCJcblBPU1RHUkVTX0RCID0gXCJhbmFseXRpY3NcIlxuUE9TVEdSRVNfVVNFUiA9IFwiZnJvZ1wiXG5QT1NUR1JFU19QQVNTV09SRCA9IFwiJHtwb3N0Z3Jlc19wYXNzd29yZH1cIlxuXG5bW2NvbmZpZy5tb3VudHNdXVxuZmlsZVBhdGggPSBcIi4vY2xpY2tob3VzZV9jb25maWcvZW5hYmxlX2pzb24ueG1sXCJcbmNvbnRlbnQgPSBcIlwiXCJcbjxjbGlja2hvdXNlPlxuICAgIDxzZXR0aW5ncz5cbiAgICAgICAgPGVuYWJsZV9qc29uX3R5cGU+MTwvZW5hYmxlX2pzb25fdHlwZT5cbiAgICA8L3NldHRpbmdzPlxuPC9jbGlja2hvdXNlPlxuXCJcIlwiXG5cbltbY29uZmlnLm1vdW50c11dXG5maWxlUGF0aCA9IFwiLi9jbGlja2hvdXNlX2NvbmZpZy9sb2dnaW5nX3J1bGVzLnhtbFwiXG5jb250ZW50ID0gXCJcIlwiXG48Y2xpY2tob3VzZT5cbiAgICA8bG9nZ2VyPlxuICAgICAgICA8bGV2ZWw+d2FybmluZzwvbGV2ZWw+XG4gICAgICAgIDxjb25zb2xlPnRydWU8L2NvbnNvbGU+XG4gICAgPC9sb2dnZXI+XG4gICAgPHF1ZXJ5X3RocmVhZF9sb2cgcmVtb3ZlPVwicmVtb3ZlXCIvPlxuICAgIDxxdWVyeV9sb2cgcmVtb3ZlPVwicmVtb3ZlXCIvPlxuICAgIDx0ZXh0X2xvZyByZW1vdmU9XCJyZW1vdmVcIi8+XG4gICAgPHRyYWNlX2xvZyByZW1vdmU9XCJyZW1vdmVcIi8+XG4gICAgPG1ldHJpY19sb2cgcmVtb3ZlPVwicmVtb3ZlXCIvPlxuICAgIDxhc3luY2hyb25vdXNfbWV0cmljX2xvZyByZW1vdmU9XCJyZW1vdmVcIi8+XG4gICAgPHNlc3Npb25fbG9nIHJlbW92ZT1cInJlbW92ZVwiLz5cbiAgICA8cGFydF9sb2cgcmVtb3ZlPVwicmVtb3ZlXCIvPlxuICAgIDxsYXRlbmN5X2xvZyByZW1vdmU9XCJyZW1vdmVcIi8+XG4gICAgPHByb2Nlc3NvcnNfcHJvZmlsZV9sb2cgcmVtb3ZlPVwicmVtb3ZlXCIvPlxuPC9jbGlja2hvdXNlPlxuXCJcIlwiXG5cbltbY29uZmlnLm1vdW50c11dXG5maWxlUGF0aCA9IFwiLi9jbGlja2hvdXNlX2NvbmZpZy9uZXR3b3JrLnhtbFwiXG5jb250ZW50ID0gXCJcIlwiXG48Y2xpY2tob3VzZT5cbiAgICA8bGlzdGVuX2hvc3Q+MC4wLjAuMDwvbGlzdGVuX2hvc3Q+XG48L2NsaWNraG91c2U+XG5cIlwiXCJcblxuW1tjb25maWcubW91bnRzXV1cbmZpbGVQYXRoID0gXCIuL2NsaWNraG91c2VfY29uZmlnL3VzZXJfbG9nZ2luZy54bWxcIlxuY29udGVudCA9IFwiXCJcIlxuPGNsaWNraG91c2U+XG4gICAgPHByb2ZpbGVzPlxuICAgICAgICA8ZGVmYXVsdD5cbiAgICAgICAgICAgIDxsb2dfcXVlcmllcz4wPC9sb2dfcXVlcmllcz5cbiAgICAgICAgICAgIDxsb2dfcXVlcnlfdGhyZWFkcz4wPC9sb2dfcXVlcnlfdGhyZWFkcz5cbiAgICAgICAgICAgIDxsb2dfcHJvY2Vzc29yc19wcm9maWxlcz4wPC9sb2dfcHJvY2Vzc29yc19wcm9maWxlcz5cbiAgICAgICAgPC9kZWZhdWx0PlxuICAgIDwvcHJvZmlsZXM+XG48L2NsaWNraG91c2U+XG5cIlwiXCJcbiIKfQ==
```

## Links

`analytics`

---

Version:`v1.5.1`

ruTorrentruTorrent + rTorrent BitTorrent client (crazy-max image). Web UI on 8080, XMLRPC on 8000, with P2P ports exposed for seeding.

RyotA self-hosted platform for tracking various media types including movies, TV shows, video games, books, audiobooks, and more.

### On this page

ConfigurationBase64LinksTags