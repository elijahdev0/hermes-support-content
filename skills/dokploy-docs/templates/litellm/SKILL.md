---
title: "LiteLLM | Dokploy"
source: "https://docs.dokploy.com/docs/templates/litellm"
category: dokploy-docs
created: "2026-06-25T17:21:52.046Z"
---

LiteLLM | Dokploy

# LiteLLM

Copy as Markdown

LiteLLM is a lightweight OpenAI API-compatible proxy for managing multiple LLM providers with a single endpoint.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  litellm:
    image: ghcr.io/berriai/litellm:main-latest
    restart: unless-stopped
    depends_on:
      litellm-db:
        condition: service_healthy
    environment:
      DATABASE_URL: ${DATABASE_URL}
      LITELLM_MASTER_KEY: ${LITELLM_MASTER_KEY}
      UI_USERNAME: ${UI_USERNAME}
      UI_PASSWORD: ${UI_PASSWORD}
      STORE_MODEL_IN_DB: "True"

      # Provider Keys
      OPENAI_API_KEY: ${OPENAI_API_KEY}
      OPENAI_BASE_URL: ${OPENAI_BASE_URL}
      COHERE_API_KEY: ${COHERE_API_KEY}
      OR_SITE_URL: ${OR_SITE_URL}
      OR_APP_NAME: ${OR_APP_NAME}
      OR_API_KEY: ${OR_API_KEY}
      AZURE_API_BASE: ${AZURE_API_BASE}
      AZURE_API_VERSION: ${AZURE_API_VERSION}
      AZURE_API_KEY: ${AZURE_API_KEY}
      REPLICATE_API_KEY: ${REPLICATE_API_KEY}
      REPLICATE_API_TOKEN: ${REPLICATE_API_TOKEN}
      ANTHROPIC_API_KEY: ${ANTHROPIC_API_KEY}
      INFISICAL_TOKEN: ${INFISICAL_TOKEN}
      NOVITA_API_KEY: ${NOVITA_API_KEY}
      INFINITY_API_KEY: ${INFINITY_API_KEY}

    expose:
      - 4000

  litellm-db:
    image: postgres:16-alpine
    restart: on-failure:5
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER} -d ${POSTGRES_DB}"]
      interval: 5s
      timeout: 5s
      retries: 5
    volumes:
      - litellm-db:/var/lib/postgresql/data
    environment:
      POSTGRES_DB: ${POSTGRES_DB}
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}

volumes:
  litellm-db: {}
```

```
[variables]
main_domain = "${domain}"

# Database
postgres_db = "litellm"
postgres_user = "litellm"
postgres_password = "${password:32}"

# LiteLLM UI + Master Key
ui_username = "${username}"
ui_password = "${password:32}"
litellm_master_key = "${password:64}"

# Provider API Keys (empty by default)
openai_api_key = ""
openai_base_url = ""
cohere_api_key = ""
or_site_url = ""
or_app_name = "LiteLLM Example app"
or_api_key = ""
azure_api_base = ""
azure_api_version = ""
azure_api_key = ""
replicate_api_key = ""
replicate_api_token = ""
anthropic_api_key = ""
infisical_token = ""
novita_api_key = ""
infinity_api_key = ""

[config]
[[config.domains]]
serviceName = "litellm"
port = 4000
host = "${main_domain}"

[config.env]
# Database
DATABASE_URL = "postgresql://${postgres_user}:${postgres_password}@litellm-db:5432/${postgres_db}"
POSTGRES_DB = "${postgres_db}"
POSTGRES_USER = "${postgres_user}"
POSTGRES_PASSWORD = "${postgres_password}"

# LiteLLM
UI_USERNAME = "${ui_username}"
UI_PASSWORD = "${ui_password}"
LITELLM_MASTER_KEY = "${litellm_master_key}"
STORE_MODEL_IN_DB = "True"

# Providers
OPENAI_API_KEY = "${openai_api_key}"
OPENAI_BASE_URL = "${openai_base_url}"
COHERE_API_KEY = "${cohere_api_key}"
OR_SITE_URL = "${or_site_url}"
OR_APP_NAME = "${or_app_name}"
OR_API_KEY = "${or_api_key}"
AZURE_API_BASE = "${azure_api_base}"
AZURE_API_VERSION = "${azure_api_version}"
AZURE_API_KEY = "${azure_api_key}"
REPLICATE_API_KEY = "${replicate_api_key}"
REPLICATE_API_TOKEN = "${replicate_api_token}"
ANTHROPIC_API_KEY = "${anthropic_api_key}"
INFISICAL_TOKEN = "${infisical_token}"
NOVITA_API_KEY = "${novita_api_key}"
INFINITY_API_KEY = "${infinity_api_key}"

[[config.mounts]]
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIGxpdGVsbG06XG4gICAgaW1hZ2U6IGdoY3IuaW8vYmVycmlhaS9saXRlbGxtOm1haW4tbGF0ZXN0XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBkZXBlbmRzX29uOlxuICAgICAgbGl0ZWxsbS1kYjpcbiAgICAgICAgY29uZGl0aW9uOiBzZXJ2aWNlX2hlYWx0aHlcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIERBVEFCQVNFX1VSTDogJHtEQVRBQkFTRV9VUkx9XG4gICAgICBMSVRFTExNX01BU1RFUl9LRVk6ICR7TElURUxMTV9NQVNURVJfS0VZfVxuICAgICAgVUlfVVNFUk5BTUU6ICR7VUlfVVNFUk5BTUV9XG4gICAgICBVSV9QQVNTV09SRDogJHtVSV9QQVNTV09SRH1cbiAgICAgIFNUT1JFX01PREVMX0lOX0RCOiBcIlRydWVcIlxuXG4gICAgICAjIFByb3ZpZGVyIEtleXNcbiAgICAgIE9QRU5BSV9BUElfS0VZOiAke09QRU5BSV9BUElfS0VZfVxuICAgICAgT1BFTkFJX0JBU0VfVVJMOiAke09QRU5BSV9CQVNFX1VSTH1cbiAgICAgIENPSEVSRV9BUElfS0VZOiAke0NPSEVSRV9BUElfS0VZfVxuICAgICAgT1JfU0lURV9VUkw6ICR7T1JfU0lURV9VUkx9XG4gICAgICBPUl9BUFBfTkFNRTogJHtPUl9BUFBfTkFNRX1cbiAgICAgIE9SX0FQSV9LRVk6ICR7T1JfQVBJX0tFWX1cbiAgICAgIEFaVVJFX0FQSV9CQVNFOiAke0FaVVJFX0FQSV9CQVNFfVxuICAgICAgQVpVUkVfQVBJX1ZFUlNJT046ICR7QVpVUkVfQVBJX1ZFUlNJT059XG4gICAgICBBWlVSRV9BUElfS0VZOiAke0FaVVJFX0FQSV9LRVl9XG4gICAgICBSRVBMSUNBVEVfQVBJX0tFWTogJHtSRVBMSUNBVEVfQVBJX0tFWX1cbiAgICAgIFJFUExJQ0FURV9BUElfVE9LRU46ICR7UkVQTElDQVRFX0FQSV9UT0tFTn1cbiAgICAgIEFOVEhST1BJQ19BUElfS0VZOiAke0FOVEhST1BJQ19BUElfS0VZfVxuICAgICAgSU5GSVNJQ0FMX1RPS0VOOiAke0lORklTSUNBTF9UT0tFTn1cbiAgICAgIE5PVklUQV9BUElfS0VZOiAke05PVklUQV9BUElfS0VZfVxuICAgICAgSU5GSU5JVFlfQVBJX0tFWTogJHtJTkZJTklUWV9BUElfS0VZfVxuXG4gICAgZXhwb3NlOlxuICAgICAgLSA0MDAwXG5cbiAgbGl0ZWxsbS1kYjpcbiAgICBpbWFnZTogcG9zdGdyZXM6MTYtYWxwaW5lXG4gICAgcmVzdGFydDogb24tZmFpbHVyZTo1XG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OiBbXCJDTUQtU0hFTExcIiwgXCJwZ19pc3JlYWR5IC1VICR7UE9TVEdSRVNfVVNFUn0gLWQgJHtQT1NUR1JFU19EQn1cIl1cbiAgICAgIGludGVydmFsOiA1c1xuICAgICAgdGltZW91dDogNXNcbiAgICAgIHJldHJpZXM6IDVcbiAgICB2b2x1bWVzOlxuICAgICAgLSBsaXRlbGxtLWRiOi92YXIvbGliL3Bvc3RncmVzcWwvZGF0YVxuICAgIGVudmlyb25tZW50OlxuICAgICAgUE9TVEdSRVNfREI6ICR7UE9TVEdSRVNfREJ9XG4gICAgICBQT1NUR1JFU19VU0VSOiAke1BPU1RHUkVTX1VTRVJ9XG4gICAgICBQT1NUR1JFU19QQVNTV09SRDogJHtQT1NUR1JFU19QQVNTV09SRH1cblxudm9sdW1lczpcbiAgbGl0ZWxsbS1kYjoge31cbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5cbiMgRGF0YWJhc2VcbnBvc3RncmVzX2RiID0gXCJsaXRlbGxtXCJcbnBvc3RncmVzX3VzZXIgPSBcImxpdGVsbG1cIlxucG9zdGdyZXNfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcblxuIyBMaXRlTExNIFVJICsgTWFzdGVyIEtleVxudWlfdXNlcm5hbWUgPSBcIiR7dXNlcm5hbWV9XCJcbnVpX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5saXRlbGxtX21hc3Rlcl9rZXkgPSBcIiR7cGFzc3dvcmQ6NjR9XCJcblxuIyBQcm92aWRlciBBUEkgS2V5cyAoZW1wdHkgYnkgZGVmYXVsdClcbm9wZW5haV9hcGlfa2V5ID0gXCJcIlxub3BlbmFpX2Jhc2VfdXJsID0gXCJcIlxuY29oZXJlX2FwaV9rZXkgPSBcIlwiXG5vcl9zaXRlX3VybCA9IFwiXCJcbm9yX2FwcF9uYW1lID0gXCJMaXRlTExNIEV4YW1wbGUgYXBwXCJcbm9yX2FwaV9rZXkgPSBcIlwiXG5henVyZV9hcGlfYmFzZSA9IFwiXCJcbmF6dXJlX2FwaV92ZXJzaW9uID0gXCJcIlxuYXp1cmVfYXBpX2tleSA9IFwiXCJcbnJlcGxpY2F0ZV9hcGlfa2V5ID0gXCJcIlxucmVwbGljYXRlX2FwaV90b2tlbiA9IFwiXCJcbmFudGhyb3BpY19hcGlfa2V5ID0gXCJcIlxuaW5maXNpY2FsX3Rva2VuID0gXCJcIlxubm92aXRhX2FwaV9rZXkgPSBcIlwiXG5pbmZpbml0eV9hcGlfa2V5ID0gXCJcIlxuXG5bY29uZmlnXVxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwibGl0ZWxsbVwiXG5wb3J0ID0gNDAwMFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cbiMgRGF0YWJhc2VcbkRBVEFCQVNFX1VSTCA9IFwicG9zdGdyZXNxbDovLyR7cG9zdGdyZXNfdXNlcn06JHtwb3N0Z3Jlc19wYXNzd29yZH1AbGl0ZWxsbS1kYjo1NDMyLyR7cG9zdGdyZXNfZGJ9XCJcblBPU1RHUkVTX0RCID0gXCIke3Bvc3RncmVzX2RifVwiXG5QT1NUR1JFU19VU0VSID0gXCIke3Bvc3RncmVzX3VzZXJ9XCJcblBPU1RHUkVTX1BBU1NXT1JEID0gXCIke3Bvc3RncmVzX3Bhc3N3b3JkfVwiXG5cbiMgTGl0ZUxMTVxuVUlfVVNFUk5BTUUgPSBcIiR7dWlfdXNlcm5hbWV9XCJcblVJX1BBU1NXT1JEID0gXCIke3VpX3Bhc3N3b3JkfVwiXG5MSVRFTExNX01BU1RFUl9LRVkgPSBcIiR7bGl0ZWxsbV9tYXN0ZXJfa2V5fVwiXG5TVE9SRV9NT0RFTF9JTl9EQiA9IFwiVHJ1ZVwiXG5cbiMgUHJvdmlkZXJzXG5PUEVOQUlfQVBJX0tFWSA9IFwiJHtvcGVuYWlfYXBpX2tleX1cIlxuT1BFTkFJX0JBU0VfVVJMID0gXCIke29wZW5haV9iYXNlX3VybH1cIlxuQ09IRVJFX0FQSV9LRVkgPSBcIiR7Y29oZXJlX2FwaV9rZXl9XCJcbk9SX1NJVEVfVVJMID0gXCIke29yX3NpdGVfdXJsfVwiXG5PUl9BUFBfTkFNRSA9IFwiJHtvcl9hcHBfbmFtZX1cIlxuT1JfQVBJX0tFWSA9IFwiJHtvcl9hcGlfa2V5fVwiXG5BWlVSRV9BUElfQkFTRSA9IFwiJHthenVyZV9hcGlfYmFzZX1cIlxuQVpVUkVfQVBJX1ZFUlNJT04gPSBcIiR7YXp1cmVfYXBpX3ZlcnNpb259XCJcbkFaVVJFX0FQSV9LRVkgPSBcIiR7YXp1cmVfYXBpX2tleX1cIlxuUkVQTElDQVRFX0FQSV9LRVkgPSBcIiR7cmVwbGljYXRlX2FwaV9rZXl9XCJcblJFUExJQ0FURV9BUElfVE9LRU4gPSBcIiR7cmVwbGljYXRlX2FwaV90b2tlbn1cIlxuQU5USFJPUElDX0FQSV9LRVkgPSBcIiR7YW50aHJvcGljX2FwaV9rZXl9XCJcbklORklTSUNBTF9UT0tFTiA9IFwiJHtpbmZpc2ljYWxfdG9rZW59XCJcbk5PVklUQV9BUElfS0VZID0gXCIke25vdml0YV9hcGlfa2V5fVwiXG5JTkZJTklUWV9BUElfS0VZID0gXCIke2luZmluaXR5X2FwaV9rZXl9XCJcblxuW1tjb25maWcubW91bnRzXV1cbiIKfQ==
```

## Links

`ai`,`proxy`,`llm`,`openai-compatible`,`monitoring`

---

Version:`main-stable`

ListmonkHigh performance, self-hosted, newsletter and mailing list manager with a modern dashboard.

LivekitLiveKit is an open source platform for developers building realtime media applications.

### On this page

ConfigurationBase64LinksTags