---
title: "Open Fiesta | Dokploy"
source: "https://docs.dokploy.com/docs/templates/open-fiesta"
category: dokploy-docs
created: "2026-06-25T17:21:55.475Z"
---

Open Fiesta | Dokploy

# Open Fiesta

Copy as Markdown

Open Fiesta is an open-source AI chat and inference UI, supporting multiple backends such as OpenRouter, Gemini, and Ollama.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  ai_fiesta:
    image: ghcr.io/jaainil/open-fiesta-ghcr:latest
    restart: unless-stopped
    environment:
      NODE_ENV: production
      OPENROUTER_API_KEY: ${OPENROUTER_API_KEY}
      GEMINI_API_KEY: ${GEMINI_API_KEY}
      UNSTABLE_INFERENCE_API_KEY: ${UNSTABLE_INFERENCE_API_KEY}
      OLLAMA_URL: ${OLLAMA_URL}
```

```
[variables]
main_domain = "${domain}"

[config]
[[config.domains]]
serviceName = "ai_fiesta"
port = 3000
host = "${main_domain}"

[config.env]
OPENROUTER_API_KEY = "${OPENROUTER_API_KEY}"
GEMINI_API_KEY = "${GEMINI_API_KEY}"
UNSTABLE_INFERENCE_API_KEY = "${UNSTABLE_INFERENCE_API_KEY}"
OLLAMA_URL = "${OLLAMA_URL}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIGFpX2ZpZXN0YTpcbiAgICBpbWFnZTogZ2hjci5pby9qYWFpbmlsL29wZW4tZmllc3RhLWdoY3I6bGF0ZXN0XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIE5PREVfRU5WOiBwcm9kdWN0aW9uXG4gICAgICBPUEVOUk9VVEVSX0FQSV9LRVk6ICR7T1BFTlJPVVRFUl9BUElfS0VZfVxuICAgICAgR0VNSU5JX0FQSV9LRVk6ICR7R0VNSU5JX0FQSV9LRVl9XG4gICAgICBVTlNUQUJMRV9JTkZFUkVOQ0VfQVBJX0tFWTogJHtVTlNUQUJMRV9JTkZFUkVOQ0VfQVBJX0tFWX1cbiAgICAgIE9MTEFNQV9VUkw6ICR7T0xMQU1BX1VSTH1cbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJhaV9maWVzdGFcIlxucG9ydCA9IDMwMDBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5PUEVOUk9VVEVSX0FQSV9LRVkgPSBcIiR7T1BFTlJPVVRFUl9BUElfS0VZfVwiXG5HRU1JTklfQVBJX0tFWSA9IFwiJHtHRU1JTklfQVBJX0tFWX1cIlxuVU5TVEFCTEVfSU5GRVJFTkNFX0FQSV9LRVkgPSBcIiR7VU5TVEFCTEVfSU5GRVJFTkNFX0FQSV9LRVl9XCJcbk9MTEFNQV9VUkwgPSBcIiR7T0xMQU1BX1VSTH1cIiIKfQ==
```

## Links

`ai`,`chatbot`,`inference`,`frontend`

---

Version:`latest`

OntimeOntime is browser-based application that manages event rundowns, scheduliing and cuing

Open WebUIOpen WebUI is a free and open source chatgpt alternative. Open WebUI is an extensible, feature-rich, and user-friendly self-hosted WebUI designed to operate entirely offline. It supports various LLM runners, including Ollama and OpenAI-compatible APIs. The template include ollama and webui services.

### On this page

ConfigurationBase64LinksTags