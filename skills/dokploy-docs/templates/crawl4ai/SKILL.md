---
title: "Crawl4AI | Dokploy"
source: "https://docs.dokploy.com/docs/templates/crawl4ai"
category: dokploy-docs
created: "2026-06-25T17:21:45.077Z"
---

Crawl4AI | Dokploy

# Crawl4AI

Copy as Markdown

Crawl4AI is a modern AI-powered web crawler with support for screenshots, PDFs, JavaScript execution, and LLM-based extraction. Includes an interactive playground and MCP (Model Context Protocol) integration.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  crawl4ai:
    image: unclecode/crawl4ai:latest
    restart: unless-stopped
    shm_size: 1g
    expose:
      - 11235
    environment:
      - LLM_PROVIDER=${LLM_PROVIDER}
      - OPENAI_API_KEY=${OPENAI_API_KEY}
      - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
      - DEEPSEEK_API_KEY=${DEEPSEEK_API_KEY}
      - GROQ_API_KEY=${GROQ_API_KEY}
      - TOGETHER_API_KEY=${TOGETHER_API_KEY}
      - MISTRAL_API_KEY=${MISTRAL_API_KEY}
      - GEMINI_API_TOKEN=${GEMINI_API_TOKEN}
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:11235/health"]
      interval: 30s
      timeout: 10s
      retries: 3
```

```
[variables]
main_domain = "${domain}"

[config]
[[config.domains]]
serviceName = "crawl4ai"
port = 11235
host = "${main_domain}"

[config.env]
LLM_PROVIDER = "openai/gpt-4o-mini"
OPENAI_API_KEY = "${password:48}"
ANTHROPIC_API_KEY = ""
DEEPSEEK_API_KEY = ""
GROQ_API_KEY = ""
TOGETHER_API_KEY = ""
MISTRAL_API_KEY = ""
GEMINI_API_TOKEN = ""
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIGNyYXdsNGFpOlxuICAgIGltYWdlOiB1bmNsZWNvZGUvY3Jhd2w0YWk6bGF0ZXN0XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBzaG1fc2l6ZTogMWdcbiAgICBleHBvc2U6XG4gICAgICAtIDExMjM1XG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIExMTV9QUk9WSURFUj0ke0xMTV9QUk9WSURFUn1cbiAgICAgIC0gT1BFTkFJX0FQSV9LRVk9JHtPUEVOQUlfQVBJX0tFWX1cbiAgICAgIC0gQU5USFJPUElDX0FQSV9LRVk9JHtBTlRIUk9QSUNfQVBJX0tFWX1cbiAgICAgIC0gREVFUFNFRUtfQVBJX0tFWT0ke0RFRVBTRUVLX0FQSV9LRVl9XG4gICAgICAtIEdST1FfQVBJX0tFWT0ke0dST1FfQVBJX0tFWX1cbiAgICAgIC0gVE9HRVRIRVJfQVBJX0tFWT0ke1RPR0VUSEVSX0FQSV9LRVl9XG4gICAgICAtIE1JU1RSQUxfQVBJX0tFWT0ke01JU1RSQUxfQVBJX0tFWX1cbiAgICAgIC0gR0VNSU5JX0FQSV9UT0tFTj0ke0dFTUlOSV9BUElfVE9LRU59XG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OiBbXCJDTURcIiwgXCJjdXJsXCIsIFwiLWZcIiwgXCJodHRwOi8vbG9jYWxob3N0OjExMjM1L2hlYWx0aFwiXVxuICAgICAgaW50ZXJ2YWw6IDMwc1xuICAgICAgdGltZW91dDogMTBzXG4gICAgICByZXRyaWVzOiAzXG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuXG5bY29uZmlnXVxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiY3Jhd2w0YWlcIlxucG9ydCA9IDExMjM1XG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuTExNX1BST1ZJREVSID0gXCJvcGVuYWkvZ3B0LTRvLW1pbmlcIlxuT1BFTkFJX0FQSV9LRVkgPSBcIiR7cGFzc3dvcmQ6NDh9XCJcbkFOVEhST1BJQ19BUElfS0VZID0gXCJcIlxuREVFUFNFRUtfQVBJX0tFWSA9IFwiXCJcbkdST1FfQVBJX0tFWSA9IFwiXCJcblRPR0VUSEVSX0FQSV9LRVkgPSBcIlwiXG5NSVNUUkFMX0FQSV9LRVkgPSBcIlwiXG5HRU1JTklfQVBJX1RPS0VOID0gXCJcIlxuIgp9
```

## Links

`crawler`,`scraping`,`AI`,`LLM`,`API`

---

Version:`0.7.3`

CouchDBCouchDB is a document-oriented NoSQL database that excels at replication and horizontal scaling.

CrowdsecCrowdSec provides open source solution for detecting and blocking malicious IPs, safeguarding both infrastructure and application security.

### On this page

ConfigurationBase64LinksTags