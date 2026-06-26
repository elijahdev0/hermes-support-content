---
title: "Open Notebook | Dokploy"
source: "https://docs.dokploy.com/docs/templates/open_notebook"
category: dokploy-docs
created: "2026-06-25T17:21:55.476Z"
---

Open Notebook | Dokploy

# Open Notebook

Copy as Markdown

Open Notebook with SurrealDB for data storage and AI-powered features.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  surrealdb:
    image: surrealdb/surrealdb:v2
    ports:
      - 8000
    volumes:
      - ../files/surreal_data:/mydata
    command: start --user root --pass root rocksdb:/mydata/mydatabase.db
    pull_policy: always
    user: root

  open_notebook:
    image: lfnovo/open_notebook:latest
    ports:
      - 8502
    environment:
      - SURREAL_URL=ws://surrealdb:8000/rpc
      - SURREAL_USER=root
      - SURREAL_PASSWORD=root
      - SURREAL_NAMESPACE=open_notebook
      - SURREAL_DATABASE=staging
    depends_on:
      - surrealdb
    pull_policy: always
    volumes:
      - ../files/notebook_data:/app/data
```

```
[variables]
main_domain = "${domain}"
surrealdb_port = "8000"
open_notebook_port = "8502"

[config]

[[config.domains]]
serviceName = "surrealdb"
port = 8000
host = "surrealdb-${main_domain}"

[[config.domains]]
serviceName = "open_notebook"
port = 8502
host = "${main_domain}"

[config.env]
SURREAL_URL = "ws://surrealdb:8000/rpc"
SURREAL_USER = "root"
SURREAL_PASSWORD = "root"
SURREAL_NAMESPACE = "open_notebook"
SURREAL_DATABASE = "staging"
# OPEN_NOTEBOOK_PASSWORD = "" # Uncomment and set to protect Open Notebook with a password for public hosting
# OPENAI_API_KEY = "" # API key for OpenAI integration
# ANTHROPIC_API_KEY = "" # API key for Anthropic integration
# GOOGLE_API_KEY = "" # API key for Google Gemini (best for long context and podcast generation)
# VERTEX_PROJECT = "" # Google Cloud project name for Vertex AI
# GOOGLE_APPLICATION_CREDENTIALS = "./google-credentials.json" # Path to Google credentials file
# VERTEX_LOCATION = "us-east5" # Vertex AI location
# MISTRAL_API_KEY = "" # API key for Mistral integration
# DEEPSEEK_API_KEY = "" # API key for DeepSeek integration
# OLLAMA_API_BASE = "http://10.20.30.20:11434" # Base URL for Ollama API
# OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1" # Base URL for OpenRouter
# OPENROUTER_API_KEY = "" # API key for OpenRouter
# GROQ_API_KEY = "" # API key for Groq integration
# XAI_API_KEY = "" # API key for xAI integration
# ELEVENLABS_API_KEY = "" # API key for ElevenLabs (used for podcast feature)
# VOYAGE_API_KEY = "" # API key for Voyage AI
# OPENAI_COMPATIBLE_BASE_URL = "http://localhost:1234/v1" # Base URL for OpenAI-compatible endpoints
# OPENAI_COMPATIBLE_API_KEY = "" # API key for OpenAI-compatible endpoints
# AZURE_OPENAI_API_KEY = "" # API key for Azure OpenAI
# AZURE_OPENAI_ENDPOINT = "" # Endpoint for Azure OpenAI
# AZURE_OPENAI_API_VERSION = "2024-12-01-preview" # API version for Azure OpenAI
# AZURE_OPENAI_DEPLOYMENT_NAME = "" # Deployment name for Azure OpenAI
# LANGCHAIN_TRACING_V2 = "true" # Enable LangChain tracing for debugging
# LANGCHAIN_ENDPOINT = "https://api.smith.langchain.com" # LangChain endpoint for debugging
# LANGCHAIN_API_KEY = "" # API key for LangChain debugging
# LANGCHAIN_PROJECT = "Open Notebook" # LangChain project name
# FIRECRAWL_API_KEY = "" # API key for Firecrawl (obtain at https://firecrawl.dev/)
# JINA_API_KEY = "" # API key for Jina (obtain at https://jina.ai/)

[[config.mounts]]
filePath = "/files/surreal_data"
content = ""

[[config.mounts]]
filePath = "/files/notebook_data"
content = ""
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBzdXJyZWFsZGI6XG4gICAgaW1hZ2U6IHN1cnJlYWxkYi9zdXJyZWFsZGI6djJcbiAgICBwb3J0czpcbiAgICAgIC0gODAwMFxuICAgIHZvbHVtZXM6XG4gICAgICAtIC4uL2ZpbGVzL3N1cnJlYWxfZGF0YTovbXlkYXRhXG4gICAgY29tbWFuZDogc3RhcnQgLS11c2VyIHJvb3QgLS1wYXNzIHJvb3Qgcm9ja3NkYjovbXlkYXRhL215ZGF0YWJhc2UuZGJcbiAgICBwdWxsX3BvbGljeTogYWx3YXlzXG4gICAgdXNlcjogcm9vdFxuXG4gIG9wZW5fbm90ZWJvb2s6XG4gICAgaW1hZ2U6IGxmbm92by9vcGVuX25vdGVib29rOmxhdGVzdFxuICAgIHBvcnRzOlxuICAgICAgLSA4NTAyXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIFNVUlJFQUxfVVJMPXdzOi8vc3VycmVhbGRiOjgwMDAvcnBjXG4gICAgICAtIFNVUlJFQUxfVVNFUj1yb290XG4gICAgICAtIFNVUlJFQUxfUEFTU1dPUkQ9cm9vdFxuICAgICAgLSBTVVJSRUFMX05BTUVTUEFDRT1vcGVuX25vdGVib29rXG4gICAgICAtIFNVUlJFQUxfREFUQUJBU0U9c3RhZ2luZ1xuICAgIGRlcGVuZHNfb246XG4gICAgICAtIHN1cnJlYWxkYlxuICAgIHB1bGxfcG9saWN5OiBhbHdheXNcbiAgICB2b2x1bWVzOlxuICAgICAgLSAuLi9maWxlcy9ub3RlYm9va19kYXRhOi9hcHAvZGF0YVxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbnN1cnJlYWxkYl9wb3J0ID0gXCI4MDAwXCJcbm9wZW5fbm90ZWJvb2tfcG9ydCA9IFwiODUwMlwiXG5cbltjb25maWddXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcInN1cnJlYWxkYlwiXG5wb3J0ID0gODAwMFxuaG9zdCA9IFwic3VycmVhbGRiLSR7bWFpbl9kb21haW59XCJcblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwib3Blbl9ub3RlYm9va1wiXG5wb3J0ID0gODUwMlxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cblNVUlJFQUxfVVJMID0gXCJ3czovL3N1cnJlYWxkYjo4MDAwL3JwY1wiXG5TVVJSRUFMX1VTRVIgPSBcInJvb3RcIlxuU1VSUkVBTF9QQVNTV09SRCA9IFwicm9vdFwiXG5TVVJSRUFMX05BTUVTUEFDRSA9IFwib3Blbl9ub3RlYm9va1wiXG5TVVJSRUFMX0RBVEFCQVNFID0gXCJzdGFnaW5nXCJcbiMgT1BFTl9OT1RFQk9PS19QQVNTV09SRCA9IFwiXCIgIyBVbmNvbW1lbnQgYW5kIHNldCB0byBwcm90ZWN0IE9wZW4gTm90ZWJvb2sgd2l0aCBhIHBhc3N3b3JkIGZvciBwdWJsaWMgaG9zdGluZ1xuIyBPUEVOQUlfQVBJX0tFWSA9IFwiXCIgIyBBUEkga2V5IGZvciBPcGVuQUkgaW50ZWdyYXRpb25cbiMgQU5USFJPUElDX0FQSV9LRVkgPSBcIlwiICMgQVBJIGtleSBmb3IgQW50aHJvcGljIGludGVncmF0aW9uXG4jIEdPT0dMRV9BUElfS0VZID0gXCJcIiAjIEFQSSBrZXkgZm9yIEdvb2dsZSBHZW1pbmkgKGJlc3QgZm9yIGxvbmcgY29udGV4dCBhbmQgcG9kY2FzdCBnZW5lcmF0aW9uKVxuIyBWRVJURVhfUFJPSkVDVCA9IFwiXCIgIyBHb29nbGUgQ2xvdWQgcHJvamVjdCBuYW1lIGZvciBWZXJ0ZXggQUlcbiMgR09PR0xFX0FQUExJQ0FUSU9OX0NSRURFTlRJQUxTID0gXCIuL2dvb2dsZS1jcmVkZW50aWFscy5qc29uXCIgIyBQYXRoIHRvIEdvb2dsZSBjcmVkZW50aWFscyBmaWxlXG4jIFZFUlRFWF9MT0NBVElPTiA9IFwidXMtZWFzdDVcIiAjIFZlcnRleCBBSSBsb2NhdGlvblxuIyBNSVNUUkFMX0FQSV9LRVkgPSBcIlwiICMgQVBJIGtleSBmb3IgTWlzdHJhbCBpbnRlZ3JhdGlvblxuIyBERUVQU0VFS19BUElfS0VZID0gXCJcIiAjIEFQSSBrZXkgZm9yIERlZXBTZWVrIGludGVncmF0aW9uXG4jIE9MTEFNQV9BUElfQkFTRSA9IFwiaHR0cDovLzEwLjIwLjMwLjIwOjExNDM0XCIgIyBCYXNlIFVSTCBmb3IgT2xsYW1hIEFQSVxuIyBPUEVOUk9VVEVSX0JBU0VfVVJMID0gXCJodHRwczovL29wZW5yb3V0ZXIuYWkvYXBpL3YxXCIgIyBCYXNlIFVSTCBmb3IgT3BlblJvdXRlclxuIyBPUEVOUk9VVEVSX0FQSV9LRVkgPSBcIlwiICMgQVBJIGtleSBmb3IgT3BlblJvdXRlclxuIyBHUk9RX0FQSV9LRVkgPSBcIlwiICMgQVBJIGtleSBmb3IgR3JvcSBpbnRlZ3JhdGlvblxuIyBYQUlfQVBJX0tFWSA9IFwiXCIgIyBBUEkga2V5IGZvciB4QUkgaW50ZWdyYXRpb25cbiMgRUxFVkVOTEFCU19BUElfS0VZID0gXCJcIiAjIEFQSSBrZXkgZm9yIEVsZXZlbkxhYnMgKHVzZWQgZm9yIHBvZGNhc3QgZmVhdHVyZSlcbiMgVk9ZQUdFX0FQSV9LRVkgPSBcIlwiICMgQVBJIGtleSBmb3IgVm95YWdlIEFJXG4jIE9QRU5BSV9DT01QQVRJQkxFX0JBU0VfVVJMID0gXCJodHRwOi8vbG9jYWxob3N0OjEyMzQvdjFcIiAjIEJhc2UgVVJMIGZvciBPcGVuQUktY29tcGF0aWJsZSBlbmRwb2ludHNcbiMgT1BFTkFJX0NPTVBBVElCTEVfQVBJX0tFWSA9IFwiXCIgIyBBUEkga2V5IGZvciBPcGVuQUktY29tcGF0aWJsZSBlbmRwb2ludHNcbiMgQVpVUkVfT1BFTkFJX0FQSV9LRVkgPSBcIlwiICMgQVBJIGtleSBmb3IgQXp1cmUgT3BlbkFJXG4jIEFaVVJFX09QRU5BSV9FTkRQT0lOVCA9IFwiXCIgIyBFbmRwb2ludCBmb3IgQXp1cmUgT3BlbkFJXG4jIEFaVVJFX09QRU5BSV9BUElfVkVSU0lPTiA9IFwiMjAyNC0xMi0wMS1wcmV2aWV3XCIgIyBBUEkgdmVyc2lvbiBmb3IgQXp1cmUgT3BlbkFJXG4jIEFaVVJFX09QRU5BSV9ERVBMT1lNRU5UX05BTUUgPSBcIlwiICMgRGVwbG95bWVudCBuYW1lIGZvciBBenVyZSBPcGVuQUlcbiMgTEFOR0NIQUlOX1RSQUNJTkdfVjIgPSBcInRydWVcIiAjIEVuYWJsZSBMYW5nQ2hhaW4gdHJhY2luZyBmb3IgZGVidWdnaW5nXG4jIExBTkdDSEFJTl9FTkRQT0lOVCA9IFwiaHR0cHM6Ly9hcGkuc21pdGgubGFuZ2NoYWluLmNvbVwiICMgTGFuZ0NoYWluIGVuZHBvaW50IGZvciBkZWJ1Z2dpbmdcbiMgTEFOR0NIQUlOX0FQSV9LRVkgPSBcIlwiICMgQVBJIGtleSBmb3IgTGFuZ0NoYWluIGRlYnVnZ2luZ1xuIyBMQU5HQ0hBSU5fUFJPSkVDVCA9IFwiT3BlbiBOb3RlYm9va1wiICMgTGFuZ0NoYWluIHByb2plY3QgbmFtZVxuIyBGSVJFQ1JBV0xfQVBJX0tFWSA9IFwiXCIgIyBBUEkga2V5IGZvciBGaXJlY3Jhd2wgKG9idGFpbiBhdCBodHRwczovL2ZpcmVjcmF3bC5kZXYvKVxuIyBKSU5BX0FQSV9LRVkgPSBcIlwiICMgQVBJIGtleSBmb3IgSmluYSAob2J0YWluIGF0IGh0dHBzOi8vamluYS5haS8pXG5cbltbY29uZmlnLm1vdW50c11dXG5maWxlUGF0aCA9IFwiL2ZpbGVzL3N1cnJlYWxfZGF0YVwiXG5jb250ZW50ID0gXCJcIlxuXG5bW2NvbmZpZy5tb3VudHNdXVxuZmlsZVBhdGggPSBcIi9maWxlcy9ub3RlYm9va19kYXRhXCJcbmNvbnRlbnQgPSBcIlwiIgp9
```

## Links

`notebook`,`ai`,`database`,`surrealdb`

---

Version:`latest`

Open WebUIOpen WebUI is a free and open source chatgpt alternative. Open WebUI is an extensible, feature-rich, and user-friendly self-hosted WebUI designed to operate entirely offline. It supports various LLM runners, including Ollama and OpenAI-compatible APIs. The template include ollama and webui services.

OpenclawWhatsApp gateway CLI with Pi RPC agent - self-hosted AI-powered messaging platform

### On this page

ConfigurationBase64LinksTags