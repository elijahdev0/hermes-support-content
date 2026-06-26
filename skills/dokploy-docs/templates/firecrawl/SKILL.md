---
title: "Firecrawl | Dokploy"
source: "https://docs.dokploy.com/docs/templates/firecrawl"
category: dokploy-docs
created: "2026-06-25T17:21:47.359Z"
---

Firecrawl | Dokploy

# Firecrawl

Copy as Markdown

Firecrawl is an API service that takes a URL, crawls it, and converts it into clean markdown or structured data. It can crawl all accessible subpages and provide clean data for each.

## Configuration

docker-compose.ymltemplate.toml

```
name: firecrawl

x-common-service: &common-service
  image: ghcr.io/firecrawl/firecrawl:latest
  ulimits:
    nofile:
      soft: 65535
      hard: 65535
  extra_hosts:
    - "host.docker.internal:host-gateway"

x-common-env: &common-env
  REDIS_URL: ${REDIS_URL:-redis://redis:6379}
  REDIS_RATE_LIMIT_URL: ${REDIS_RATE_LIMIT_URL:-redis://redis:6379}
  PLAYWRIGHT_MICROSERVICE_URL: ${PLAYWRIGHT_MICROSERVICE_URL:-http://playwright-service:3000/scrape}
  NUQ_DATABASE_URL: ${NUQ_DATABASE_URL:-postgres://postgres:postgres@nuq-postgres:5432/postgres}
  USE_DB_AUTHENTICATION: ${USE_DB_AUTHENTICATION:-}
  OPENAI_API_KEY: ${OPENAI_API_KEY:-}
  OPENAI_BASE_URL: ${OPENAI_BASE_URL:-}
  MODEL_NAME: ${MODEL_NAME:-}
  MODEL_EMBEDDING_NAME: ${MODEL_EMBEDDING_NAME:-}
  OLLAMA_BASE_URL: ${OLLAMA_BASE_URL:-}
  SLACK_WEBHOOK_URL: ${SLACK_WEBHOOK_URL:-}
  BULL_AUTH_KEY: ${BULL_AUTH_KEY:-}
  TEST_API_KEY: ${TEST_API_KEY:-}
  POSTHOG_API_KEY: ${POSTHOG_API_KEY:-}
  POSTHOG_HOST: ${POSTHOG_HOST:-}
  SUPABASE_ANON_TOKEN: ${SUPABASE_ANON_TOKEN:-}
  SUPABASE_URL: ${SUPABASE_URL:-}
  SUPABASE_SERVICE_TOKEN: ${SUPABASE_SERVICE_TOKEN:-}
  SELF_HOSTED_WEBHOOK_URL: ${SELF_HOSTED_WEBHOOK_URL:-}
  SERPER_API_KEY: ${SERPER_API_KEY:-}
  SEARCHAPI_API_KEY: ${SEARCHAPI_API_KEY:-}
  LOGGING_LEVEL: ${LOGGING_LEVEL:-INFO}
  PROXY_SERVER: ${PROXY_SERVER:-}
  PROXY_USERNAME: ${PROXY_USERNAME:-}
  PROXY_PASSWORD: ${PROXY_PASSWORD:-}
  NO_PROXY: ${NO_PROXY:-localhost,127.0.0.1,redis,nuq-postgres,playwright-service,host.docker.internal}
  SEARXNG_ENDPOINT: ${SEARXNG_ENDPOINT:-}
  SEARXNG_ENGINES: ${SEARXNG_ENGINES:-}
  SEARXNG_CATEGORIES: ${SEARXNG_CATEGORIES:-}

services:
  playwright-service:
    image: ghcr.io/firecrawl/playwright-service:latest
    shm_size: "1g"
    restart: unless-stopped
    environment:
      PORT: 3000
      PROXY_SERVER: ${PROXY_SERVER:-}
      PROXY_USERNAME: ${PROXY_USERNAME:-}
      PROXY_PASSWORD: ${PROXY_PASSWORD:-}
      BLOCK_MEDIA: ${BLOCK_MEDIA:-}
      NO_PROXY: ${NO_PROXY:-localhost,127.0.0.1,redis,nuq-postgres,playwright-service,host.docker.internal}

  api:
    <<: *common-service
    restart: unless-stopped
    ports:
      - "3002"
    environment:
      <<: *common-env
      HOST: "0.0.0.0"
      PORT: 3002
      WORKER_PORT: 3005
      ENV: local
    depends_on:
      redis:
        condition: service_started
      playwright-service:
        condition: service_started
      nuq-postgres:
        condition: service_healthy
    command: node --import ./dist/src/otel.js dist/src/index.js

  worker:
    <<: *common-service
    restart: unless-stopped
    environment:
      <<: *common-env
      HOST: "0.0.0.0"
      PORT: 3005
      ENV: local
    depends_on:
      redis:
        condition: service_started
      nuq-postgres:
        condition: service_healthy
    command: node --import ./dist/src/otel.js dist/src/services/queue-worker.js

  extract-worker:
    <<: *common-service
    restart: unless-stopped
    environment:
      <<: *common-env
      HOST: "0.0.0.0"
      PORT: 3004
      ENV: local
    depends_on:
      redis:
        condition: service_started
      nuq-postgres:
        condition: service_healthy
    command: node --import ./dist/src/otel.js dist/src/services/extract-worker.js

  redis:
    image: redis:alpine
    command: redis-server --bind 0.0.0.0

  nuq-postgres:
    build:
      context: "https://github.com/firecrawl/firecrawl.git#main:apps/nuq-postgres"
      dockerfile: Dockerfile
    restart: unless-stopped
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: postgres
    volumes:
      - nuq_pg_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U $${POSTGRES_USER} -d $${POSTGRES_DB}"]
      start_period: 30s
      interval: 10s
      timeout: 5s
      retries: 10

volumes:
  nuq_pg_data:
```

```
[variables]
main_domain = "${domain}"
openai_api_key = "${OPENAI_API_KEY}"
openai_base_url = "${OPENAI_BASE_URL}"
ollama_base_url = "${OLLAMA_BASE_URL}"
model_name = "${MODEL_NAME}"
model_embedding_name = "${MODEL_EMBEDDING_NAME}"
proxy_server = "${PROXY_SERVER}"
proxy_username = "${PROXY_USERNAME}"
proxy_password = "${PROXY_PASSWORD}"
searxng_endpoint = "${SEARXNG_ENDPOINT}"
searxng_engines = "${SEARXNG_ENGINES}"
searxng_categories = "${SEARXNG_CATEGORIES}"
supabase_anon_token = "${SUPABASE_ANON_TOKEN}"
supabase_url = "${SUPABASE_URL}"
supabase_service_token = "${SUPABASE_SERVICE_TOKEN}"
test_api_key = "${TEST_API_KEY}"
bull_auth_key = "${password:32}"
llamaparse_api_key = "${LLAMAPARSE_API_KEY}"
slack_webhook_url = "${SLACK_WEBHOOK_URL}"
posthog_api_key = "${POSTHOG_API_KEY}"
posthog_host = "${POSTHOG_HOST}"
max_cpu = "${MAX_CPU}"
max_ram = "${MAX_RAM}"

[config]
env = [
  "PORT=3002",
  "HOST=0.0.0.0",
  "USE_DB_AUTHENTICATION=false",
  "BULL_AUTH_KEY=${bull_auth_key}",
  "PLAYWRIGHT_MICROSERVICE_URL=http://playwright-service:3000/scrape",
  "REDIS_URL=redis://redis:6379",
  "REDIS_RATE_LIMIT_URL=redis://redis:6379",
  "OPENAI_API_KEY=${openai_api_key}",
  "OPENAI_BASE_URL=${openai_base_url}",
  "OLLAMA_BASE_URL=${ollama_base_url}",
  "MODEL_NAME=${model_name}",
  "MODEL_EMBEDDING_NAME=${model_embedding_name}",
  "PROXY_SERVER=${proxy_server}",
  "PROXY_USERNAME=${proxy_username}",
  "PROXY_PASSWORD=${proxy_password}",
  "SEARXNG_ENDPOINT=${searxng_endpoint}",
  "SEARXNG_ENGINES=${searxng_engines}",
  "SEARXNG_CATEGORIES=${searxng_categories}",
  "SUPABASE_ANON_TOKEN=${supabase_anon_token}",
  "SUPABASE_URL=${supabase_url}",
  "SUPABASE_SERVICE_TOKEN=${supabase_service_token}",
  "TEST_API_KEY=${test_api_key}",
  "LLAMAPARSE_API_KEY=${llamaparse_api_key}",
  "SLACK_WEBHOOK_URL=${slack_webhook_url}",
  "POSTHOG_API_KEY=${posthog_api_key}",
  "POSTHOG_HOST=${posthog_host}",
  "MAX_CPU=0.8",
  "MAX_RAM=0.8"
]
mounts = []

[[config.domains]]
serviceName = "api"
port = 3002
host = "${main_domain}"
path = "/"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogIm5hbWU6IGZpcmVjcmF3bFxuIFxueC1jb21tb24tc2VydmljZTogJmNvbW1vbi1zZXJ2aWNlXG4gIGltYWdlOiBnaGNyLmlvL2ZpcmVjcmF3bC9maXJlY3Jhd2w6bGF0ZXN0XG4gIHVsaW1pdHM6XG4gICAgbm9maWxlOlxuICAgICAgc29mdDogNjU1MzVcbiAgICAgIGhhcmQ6IDY1NTM1XG4gIGV4dHJhX2hvc3RzOlxuICAgIC0gXCJob3N0LmRvY2tlci5pbnRlcm5hbDpob3N0LWdhdGV3YXlcIlxuIFxueC1jb21tb24tZW52OiAmY29tbW9uLWVudlxuICBSRURJU19VUkw6ICR7UkVESVNfVVJMOi1yZWRpczovL3JlZGlzOjYzNzl9XG4gIFJFRElTX1JBVEVfTElNSVRfVVJMOiAke1JFRElTX1JBVEVfTElNSVRfVVJMOi1yZWRpczovL3JlZGlzOjYzNzl9XG4gIFBMQVlXUklHSFRfTUlDUk9TRVJWSUNFX1VSTDogJHtQTEFZV1JJR0hUX01JQ1JPU0VSVklDRV9VUkw6LWh0dHA6Ly9wbGF5d3JpZ2h0LXNlcnZpY2U6MzAwMC9zY3JhcGV9XG4gIE5VUV9EQVRBQkFTRV9VUkw6ICR7TlVRX0RBVEFCQVNFX1VSTDotcG9zdGdyZXM6Ly9wb3N0Z3Jlczpwb3N0Z3Jlc0BudXEtcG9zdGdyZXM6NTQzMi9wb3N0Z3Jlc31cbiAgVVNFX0RCX0FVVEhFTlRJQ0FUSU9OOiAke1VTRV9EQl9BVVRIRU5USUNBVElPTjotfVxuICBPUEVOQUlfQVBJX0tFWTogJHtPUEVOQUlfQVBJX0tFWTotfVxuICBPUEVOQUlfQkFTRV9VUkw6ICR7T1BFTkFJX0JBU0VfVVJMOi19XG4gIE1PREVMX05BTUU6ICR7TU9ERUxfTkFNRTotfVxuICBNT0RFTF9FTUJFRERJTkdfTkFNRTogJHtNT0RFTF9FTUJFRERJTkdfTkFNRTotfVxuICBPTExBTUFfQkFTRV9VUkw6ICR7T0xMQU1BX0JBU0VfVVJMOi19XG4gIFNMQUNLX1dFQkhPT0tfVVJMOiAke1NMQUNLX1dFQkhPT0tfVVJMOi19XG4gIEJVTExfQVVUSF9LRVk6ICR7QlVMTF9BVVRIX0tFWTotfVxuICBURVNUX0FQSV9LRVk6ICR7VEVTVF9BUElfS0VZOi19XG4gIFBPU1RIT0dfQVBJX0tFWTogJHtQT1NUSE9HX0FQSV9LRVk6LX1cbiAgUE9TVEhPR19IT1NUOiAke1BPU1RIT0dfSE9TVDotfVxuICBTVVBBQkFTRV9BTk9OX1RPS0VOOiAke1NVUEFCQVNFX0FOT05fVE9LRU46LX1cbiAgU1VQQUJBU0VfVVJMOiAke1NVUEFCQVNFX1VSTDotfVxuICBTVVBBQkFTRV9TRVJWSUNFX1RPS0VOOiAke1NVUEFCQVNFX1NFUlZJQ0VfVE9LRU46LX1cbiAgU0VMRl9IT1NURURfV0VCSE9PS19VUkw6ICR7U0VMRl9IT1NURURfV0VCSE9PS19VUkw6LX1cbiAgU0VSUEVSX0FQSV9LRVk6ICR7U0VSUEVSX0FQSV9LRVk6LX1cbiAgU0VBUkNIQVBJX0FQSV9LRVk6ICR7U0VBUkNIQVBJX0FQSV9LRVk6LX1cbiAgTE9HR0lOR19MRVZFTDogJHtMT0dHSU5HX0xFVkVMOi1JTkZPfVxuICBQUk9YWV9TRVJWRVI6ICR7UFJPWFlfU0VSVkVSOi19XG4gIFBST1hZX1VTRVJOQU1FOiAke1BST1hZX1VTRVJOQU1FOi19XG4gIFBST1hZX1BBU1NXT1JEOiAke1BST1hZX1BBU1NXT1JEOi19XG4gIE5PX1BST1hZOiAke05PX1BST1hZOi1sb2NhbGhvc3QsMTI3LjAuMC4xLHJlZGlzLG51cS1wb3N0Z3JlcyxwbGF5d3JpZ2h0LXNlcnZpY2UsaG9zdC5kb2NrZXIuaW50ZXJuYWx9XG4gIFNFQVJYTkdfRU5EUE9JTlQ6ICR7U0VBUlhOR19FTkRQT0lOVDotfVxuICBTRUFSWE5HX0VOR0lORVM6ICR7U0VBUlhOR19FTkdJTkVTOi19XG4gIFNFQVJYTkdfQ0FURUdPUklFUzogJHtTRUFSWE5HX0NBVEVHT1JJRVM6LX1cbiBcbnNlcnZpY2VzOlxuICBwbGF5d3JpZ2h0LXNlcnZpY2U6XG4gICAgaW1hZ2U6IGdoY3IuaW8vZmlyZWNyYXdsL3BsYXl3cmlnaHQtc2VydmljZTpsYXRlc3RcbiAgICBzaG1fc2l6ZTogXCIxZ1wiXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIFBPUlQ6IDMwMDBcbiAgICAgIFBST1hZX1NFUlZFUjogJHtQUk9YWV9TRVJWRVI6LX1cbiAgICAgIFBST1hZX1VTRVJOQU1FOiAke1BST1hZX1VTRVJOQU1FOi19XG4gICAgICBQUk9YWV9QQVNTV09SRDogJHtQUk9YWV9QQVNTV09SRDotfVxuICAgICAgQkxPQ0tfTUVESUE6ICR7QkxPQ0tfTUVESUE6LX1cbiAgICAgIE5PX1BST1hZOiAke05PX1BST1hZOi1sb2NhbGhvc3QsMTI3LjAuMC4xLHJlZGlzLG51cS1wb3N0Z3JlcyxwbGF5d3JpZ2h0LXNlcnZpY2UsaG9zdC5kb2NrZXIuaW50ZXJuYWx9XG4gXG4gIGFwaTpcbiAgICA8PDogKmNvbW1vbi1zZXJ2aWNlXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBwb3J0czpcbiAgICAgIC0gXCIzMDAyXCJcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIDw8OiAqY29tbW9uLWVudlxuICAgICAgSE9TVDogXCIwLjAuMC4wXCJcbiAgICAgIFBPUlQ6IDMwMDJcbiAgICAgIFdPUktFUl9QT1JUOiAzMDA1XG4gICAgICBFTlY6IGxvY2FsXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIHJlZGlzOlxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2Vfc3RhcnRlZFxuICAgICAgcGxheXdyaWdodC1zZXJ2aWNlOlxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2Vfc3RhcnRlZFxuICAgICAgbnVxLXBvc3RncmVzOlxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2VfaGVhbHRoeVxuICAgIGNvbW1hbmQ6IG5vZGUgLS1pbXBvcnQgLi9kaXN0L3NyYy9vdGVsLmpzIGRpc3Qvc3JjL2luZGV4LmpzXG4gXG4gIHdvcmtlcjpcbiAgICA8PDogKmNvbW1vbi1zZXJ2aWNlXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIDw8OiAqY29tbW9uLWVudlxuICAgICAgSE9TVDogXCIwLjAuMC4wXCJcbiAgICAgIFBPUlQ6IDMwMDVcbiAgICAgIEVOVjogbG9jYWxcbiAgICBkZXBlbmRzX29uOlxuICAgICAgcmVkaXM6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9zdGFydGVkXG4gICAgICBudXEtcG9zdGdyZXM6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9oZWFsdGh5XG4gICAgY29tbWFuZDogbm9kZSAtLWltcG9ydCAuL2Rpc3Qvc3JjL290ZWwuanMgZGlzdC9zcmMvc2VydmljZXMvcXVldWUtd29ya2VyLmpzXG4gXG4gIGV4dHJhY3Qtd29ya2VyOlxuICAgIDw8OiAqY29tbW9uLXNlcnZpY2VcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGVudmlyb25tZW50OlxuICAgICAgPDw6ICpjb21tb24tZW52XG4gICAgICBIT1NUOiBcIjAuMC4wLjBcIlxuICAgICAgUE9SVDogMzAwNFxuICAgICAgRU5WOiBsb2NhbFxuICAgIGRlcGVuZHNfb246XG4gICAgICByZWRpczpcbiAgICAgICAgY29uZGl0aW9uOiBzZXJ2aWNlX3N0YXJ0ZWRcbiAgICAgIG51cS1wb3N0Z3JlczpcbiAgICAgICAgY29uZGl0aW9uOiBzZXJ2aWNlX2hlYWx0aHlcbiAgICBjb21tYW5kOiBub2RlIC0taW1wb3J0IC4vZGlzdC9zcmMvb3RlbC5qcyBkaXN0L3NyYy9zZXJ2aWNlcy9leHRyYWN0LXdvcmtlci5qc1xuIFxuICByZWRpczpcbiAgICBpbWFnZTogcmVkaXM6YWxwaW5lXG4gICAgY29tbWFuZDogcmVkaXMtc2VydmVyIC0tYmluZCAwLjAuMC4wXG4gXG4gIG51cS1wb3N0Z3JlczpcbiAgICBidWlsZDpcbiAgICAgIGNvbnRleHQ6IFwiaHR0cHM6Ly9naXRodWIuY29tL2ZpcmVjcmF3bC9maXJlY3Jhd2wuZ2l0I21haW46YXBwcy9udXEtcG9zdGdyZXNcIlxuICAgICAgZG9ja2VyZmlsZTogRG9ja2VyZmlsZVxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBQT1NUR1JFU19VU0VSOiBwb3N0Z3Jlc1xuICAgICAgUE9TVEdSRVNfUEFTU1dPUkQ6IHBvc3RncmVzXG4gICAgICBQT1NUR1JFU19EQjogcG9zdGdyZXNcbiAgICB2b2x1bWVzOlxuICAgICAgLSBudXFfcGdfZGF0YTovdmFyL2xpYi9wb3N0Z3Jlc3FsL2RhdGFcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6IFtcIkNNRC1TSEVMTFwiLCBcInBnX2lzcmVhZHkgLVUgJCR7UE9TVEdSRVNfVVNFUn0gLWQgJCR7UE9TVEdSRVNfREJ9XCJdXG4gICAgICBzdGFydF9wZXJpb2Q6IDMwc1xuICAgICAgaW50ZXJ2YWw6IDEwc1xuICAgICAgdGltZW91dDogNXNcbiAgICAgIHJldHJpZXM6IDEwXG4gXG52b2x1bWVzOlxuICBudXFfcGdfZGF0YToiLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxub3BlbmFpX2FwaV9rZXkgPSBcIiR7T1BFTkFJX0FQSV9LRVl9XCJcbm9wZW5haV9iYXNlX3VybCA9IFwiJHtPUEVOQUlfQkFTRV9VUkx9XCJcbm9sbGFtYV9iYXNlX3VybCA9IFwiJHtPTExBTUFfQkFTRV9VUkx9XCJcbm1vZGVsX25hbWUgPSBcIiR7TU9ERUxfTkFNRX1cIlxubW9kZWxfZW1iZWRkaW5nX25hbWUgPSBcIiR7TU9ERUxfRU1CRURESU5HX05BTUV9XCJcbnByb3h5X3NlcnZlciA9IFwiJHtQUk9YWV9TRVJWRVJ9XCJcbnByb3h5X3VzZXJuYW1lID0gXCIke1BST1hZX1VTRVJOQU1FfVwiXG5wcm94eV9wYXNzd29yZCA9IFwiJHtQUk9YWV9QQVNTV09SRH1cIlxuc2VhcnhuZ19lbmRwb2ludCA9IFwiJHtTRUFSWE5HX0VORFBPSU5UfVwiXG5zZWFyeG5nX2VuZ2luZXMgPSBcIiR7U0VBUlhOR19FTkdJTkVTfVwiXG5zZWFyeG5nX2NhdGVnb3JpZXMgPSBcIiR7U0VBUlhOR19DQVRFR09SSUVTfVwiXG5zdXBhYmFzZV9hbm9uX3Rva2VuID0gXCIke1NVUEFCQVNFX0FOT05fVE9LRU59XCJcbnN1cGFiYXNlX3VybCA9IFwiJHtTVVBBQkFTRV9VUkx9XCJcbnN1cGFiYXNlX3NlcnZpY2VfdG9rZW4gPSBcIiR7U1VQQUJBU0VfU0VSVklDRV9UT0tFTn1cIlxudGVzdF9hcGlfa2V5ID0gXCIke1RFU1RfQVBJX0tFWX1cIlxuYnVsbF9hdXRoX2tleSA9IFwiJHtwYXNzd29yZDozMn1cIlxubGxhbWFwYXJzZV9hcGlfa2V5ID0gXCIke0xMQU1BUEFSU0VfQVBJX0tFWX1cIlxuc2xhY2tfd2ViaG9va191cmwgPSBcIiR7U0xBQ0tfV0VCSE9PS19VUkx9XCJcbnBvc3Rob2dfYXBpX2tleSA9IFwiJHtQT1NUSE9HX0FQSV9LRVl9XCJcbnBvc3Rob2dfaG9zdCA9IFwiJHtQT1NUSE9HX0hPU1R9XCJcbm1heF9jcHUgPSBcIiR7TUFYX0NQVX1cIlxubWF4X3JhbSA9IFwiJHtNQVhfUkFNfVwiXG5cbltjb25maWddXG5lbnYgPSBbXG4gIFwiUE9SVD0zMDAyXCIsXG4gIFwiSE9TVD0wLjAuMC4wXCIsXG4gIFwiVVNFX0RCX0FVVEhFTlRJQ0FUSU9OPWZhbHNlXCIsXG4gIFwiQlVMTF9BVVRIX0tFWT0ke2J1bGxfYXV0aF9rZXl9XCIsXG4gIFwiUExBWVdSSUdIVF9NSUNST1NFUlZJQ0VfVVJMPWh0dHA6Ly9wbGF5d3JpZ2h0LXNlcnZpY2U6MzAwMC9zY3JhcGVcIixcbiAgXCJSRURJU19VUkw9cmVkaXM6Ly9yZWRpczo2Mzc5XCIsXG4gIFwiUkVESVNfUkFURV9MSU1JVF9VUkw9cmVkaXM6Ly9yZWRpczo2Mzc5XCIsXG4gIFwiT1BFTkFJX0FQSV9LRVk9JHtvcGVuYWlfYXBpX2tleX1cIixcbiAgXCJPUEVOQUlfQkFTRV9VUkw9JHtvcGVuYWlfYmFzZV91cmx9XCIsXG4gIFwiT0xMQU1BX0JBU0VfVVJMPSR7b2xsYW1hX2Jhc2VfdXJsfVwiLFxuICBcIk1PREVMX05BTUU9JHttb2RlbF9uYW1lfVwiLFxuICBcIk1PREVMX0VNQkVERElOR19OQU1FPSR7bW9kZWxfZW1iZWRkaW5nX25hbWV9XCIsXG4gIFwiUFJPWFlfU0VSVkVSPSR7cHJveHlfc2VydmVyfVwiLFxuICBcIlBST1hZX1VTRVJOQU1FPSR7cHJveHlfdXNlcm5hbWV9XCIsXG4gIFwiUFJPWFlfUEFTU1dPUkQ9JHtwcm94eV9wYXNzd29yZH1cIixcbiAgXCJTRUFSWE5HX0VORFBPSU5UPSR7c2VhcnhuZ19lbmRwb2ludH1cIixcbiAgXCJTRUFSWE5HX0VOR0lORVM9JHtzZWFyeG5nX2VuZ2luZXN9XCIsXG4gIFwiU0VBUlhOR19DQVRFR09SSUVTPSR7c2VhcnhuZ19jYXRlZ29yaWVzfVwiLFxuICBcIlNVUEFCQVNFX0FOT05fVE9LRU49JHtzdXBhYmFzZV9hbm9uX3Rva2VufVwiLFxuICBcIlNVUEFCQVNFX1VSTD0ke3N1cGFiYXNlX3VybH1cIixcbiAgXCJTVVBBQkFTRV9TRVJWSUNFX1RPS0VOPSR7c3VwYWJhc2Vfc2VydmljZV90b2tlbn1cIixcbiAgXCJURVNUX0FQSV9LRVk9JHt0ZXN0X2FwaV9rZXl9XCIsXG4gIFwiTExBTUFQQVJTRV9BUElfS0VZPSR7bGxhbWFwYXJzZV9hcGlfa2V5fVwiLFxuICBcIlNMQUNLX1dFQkhPT0tfVVJMPSR7c2xhY2tfd2ViaG9va191cmx9XCIsXG4gIFwiUE9TVEhPR19BUElfS0VZPSR7cG9zdGhvZ19hcGlfa2V5fVwiLFxuICBcIlBPU1RIT0dfSE9TVD0ke3Bvc3Rob2dfaG9zdH1cIixcbiAgXCJNQVhfQ1BVPTAuOFwiLFxuICBcIk1BWF9SQU09MC44XCJcbl1cbm1vdW50cyA9IFtdXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImFwaVwiXG5wb3J0ID0gMzAwMlxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxucGF0aCA9IFwiL1wiXG5cbiAiCn0=
```

## Links

`api`,`crawler`,`scraping`,`data-extraction`,`llm`

---

Version:`latest`

FilestashFilestash is the enterprise-grade file manager connecting your storage with your identity provider and authorisations.

FiveM ServerA modded GTA V multiplayer server with optional txAdmin web interface for easy server management.

### On this page

ConfigurationBase64LinksTags