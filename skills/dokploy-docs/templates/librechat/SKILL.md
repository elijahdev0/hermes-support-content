---
title: "LibreChat | Dokploy"
source: "https://docs.dokploy.com/docs/templates/librechat"
category: dokploy-docs
created: "2026-06-25T17:21:52.046Z"
---

LibreChat | Dokploy

# LibreChat

Copy as Markdown

LibreChat is the ultimate open-source app for all your AI conversations, fully customizable and compatible with any AI provider (Openai, Ollama, Google etc.) — all in one sleek interface.

## Configuration

docker-compose.ymltemplate.toml

```
# LibreChat Docker Compose for Dokploy Template
# Setting up authentication: "npm run create-user", refer to https://www.librechat.ai/docs/configuration/authentication

services:
  librechat:
    image: ghcr.io/danny-avila/librechat-dev:latest
    restart: always
    depends_on:
      - mongodb
      - rag_api
    environment:
      # Server Configuration
      - HOST=0.0.0.0
      - PORT=${PORT:-3080}
      # Domain Configuration
      - DOMAIN_CLIENT=${DOMAIN_CLIENT}
      - DOMAIN_SERVER=${DOMAIN_SERVER}
      # Database and Search Configuration
      - MONGO_URI=mongodb://mongodb:27017/LibreChat
      - MEILI_HOST=http://meilisearch:7700
      - SEARCH=true
      - NO_INDEX=true
      - MEILI_NO_ANALYTICS=true
      - MEILI_MASTER_KEY=${MEILI_MASTER_KEY}
      # Security & Sessions
      - JWT_SECRET=${JWT_SECRET}
      - JWT_REFRESH_SECRET=${JWT_REFRESH_SECRET}
      - CREDS_KEY=${CREDS_KEY}
      - CREDS_IV=${CREDS_IV}
      - RAG_PORT=${RAG_PORT:-8000}
      - RAG_API_URL=http://rag_api:${RAG_PORT:-8000}
      # API Keys and Secrets
      - OPENAI_API_KEY=${OPENAI_API_KEY}
      - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
      - OPENROUTER_KEY=${OPENROUTER_KEY}
      - GOOGLE_KEY=${GOOGLE_KEY}
      - ENDPOINTS=google,openAI,assistants,azureOpenAI,anthropic
      # ... Additional Endpoints
      # UI
      - APP_TITLE=${APP_TITLE:-LibreChat}
      - CUSTOM_FOOTER=${CUSTOM_FOOTER:-Made with ❤️ by LibreChat}
      - ALLOW_EMAIL_LOGIN=${ALLOW_EMAIL_LOGIN:-true}
      - ALLOW_SOCIAL_LOGIN=${ALLOW_SOCIAL_LOGIN:-false}
      - ALLOW_REGISTRATION=${ALLOW_REGISTRATION:-false}
    volumes:
      - type: bind
        source: ../files/librechat.yaml
        target: /app/librechat.yaml
      - librechat_data:/app/client/public/images
      - librechat_data:/app/uploads
      - librechat_data:/app/logs

  mongodb:
    image: mongo
    restart: always
    volumes:
      - mongo_data:/data/db
    command: mongod --noauth

  meilisearch:
    image: getmeili/meilisearch:v1.12.3
    restart: always
    environment:
      - MEILI_HOST=http://meilisearch:7700
      - MEILI_NO_ANALYTICS=true
      - MEILI_MASTER_KEY=${MEILI_MASTER_KEY}
    volumes:
      - meili_data:/meili_data

  vectordb:
    image: pgvector/pgvector:0.8.0-pg15-trixie
    environment:
      - POSTGRES_DB=${POSTGRES_DB:-mydatabase}
      - POSTGRES_USER=${POSTGRES_USER:-myuser}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD:-mypassword}
    restart: always
    volumes:
      - postgres_data:/var/lib/postgresql/data

  rag_api:
    image: ghcr.io/danny-avila/librechat-rag-api-dev-lite:latest
    environment:
      - DB_HOST=vectordb
      - VECTOR_DB_TYPE=pgvector
      - POSTGRES_DB=${POSTGRES_DB:-mydatabase}
      - POSTGRES_USER=${POSTGRES_USER:-myuser}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD:-mypassword}
      - RAG_PORT=${RAG_PORT:-8000}
      - OPENAI_API_KEY=${OPENAI_API_KEY}
      - RAG_OPENAI_API_KEY=${RAG_OPENAI_API_KEY}
      - GOOGLE_KEY=${GOOGLE_KEY}
      - RAG_GOOGLE_API_KEY=${RAG_GOOGLE_API_KEY}
      - JWT_SECRET=${JWT_SECRET}
      - COLLECTION_NAME=${COLLECTION_NAME:-librechat_collection}
      - CHUNK_SIZE=${CHUNK_SIZE:-1500}
      - CHUNK_OVERLAP=${CHUNK_OVERLAP:-100}
      - EMBEDDINGS_PROVIDER=${EMBEDDINGS_PROVIDER:-openai}
      - EMBEDDINGS_MODEL=${EMBEDDINGS_MODEL:-text-embedding-3-small}
      - DEBUG_RAG_API=false
      - DEBUG_PGVECTOR_QUERIES=false
      - CONSOLE_JSON=false
    restart: always
    depends_on:
      - vectordb

volumes:
  mongo_data:
  meili_data:
  postgres_data:
  librechat_data:
```

```
[variables]
# Domain Configuration
main_domain = "${domain}"

# Security & Authentication
jwt_secret = "${password:64}"
jwt_refresh_secret = "${password:64}"
creds_key = "f34be427ebb29de8d88c107a71546019685ed8b241d8f2ed00c3df97ad2566f0"
creds_iv = "e2341419ec3dd3d19b13a1a87fafcbfb"
meili_master_key = "${password:32}"

# Database Configuration
mongo_password = "${password:16}"
postgresql_password = "${password:16}"

[config]
version = "1.0.0"
# Main service domain mapping
[[config.domains]]
serviceName = "librechat"
port = 3080
host = "${main_domain}"

[config.env]
# Basic Configuration
HOST="0.0.0.0"
PORT="3080"
DOMAIN_CLIENT="https://${main_domain}"
DOMAIN_SERVER="https://${main_domain}"

# Search Configuration
MEILI_MASTER_KEY="${meili_master_key}"

# Security
JWT_SECRET="${jwt_secret}"
JWT_REFRESH_SECRET="${jwt_refresh_secret}"
CREDS_KEY="${creds_key}"
CREDS_IV="${creds_iv}"

# API Keys
OPENAI_API_KEY=""
ANTHROPIC_API_KEY=""
GOOGLE_KEY=""
OPENROUTER_KEY=""

# Database
POSTGRES_DB="librechat_db"
POSTGRES_USER="librechat_user"
POSTGRES_PASSWORD="${postgresql_password}"

# Security & Sessions

# User Interface
APP_TITLE="LibreChat"
CUSTOM_FOOTER="Made with ❤️ by LibreChat"
ALLOW_EMAIL_LOGIN="true"
ALLOW_REGISTRATION="false"
ALLOW_SOCIAL_LOGIN="false"

# RAG
RAG_OPENAI_API_KEY=""
RAG_GOOGLE_API_KEY=""
EMBEDDINGS_PROVIDER="openai"
EMBEDDINGS_MODEL="text-embedding-3-small"

CHUNK_SIZE=1500
CHUNK_OVERLAP=100

[[config.mounts]]
filePath = "librechat.yaml"
content = """
### librechat.yaml configs ###

version: 1.2.8
cache: true
endpoints:
  custom:
    - name: "OpenRouter"
      apiKey: "${OPENROUTER_KEY}"
      baseURL: "https://openrouter.ai/api/v1"
      models:
        default: ["meta-llama/llama-3.3-70b-instruct:free"]
        fetch: true
      titleConvo: true
      titleModel: "current_model"
      summarize: false
      summaryModel: "current_model"
      forcePrompt: false
      dropParams: ["stop"]
      modelDisplayLabel: "OpenRouter"
"""
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogIiMgTGlicmVDaGF0IERvY2tlciBDb21wb3NlIGZvciBEb2twbG95IFRlbXBsYXRlXG4jIFNldHRpbmcgdXAgYXV0aGVudGljYXRpb246IFwibnBtIHJ1biBjcmVhdGUtdXNlclwiLCByZWZlciB0byBodHRwczovL3d3dy5saWJyZWNoYXQuYWkvZG9jcy9jb25maWd1cmF0aW9uL2F1dGhlbnRpY2F0aW9uXG5cbnNlcnZpY2VzOlxuICBsaWJyZWNoYXQ6XG4gICAgaW1hZ2U6IGdoY3IuaW8vZGFubnktYXZpbGEvbGlicmVjaGF0LWRldjpsYXRlc3RcbiAgICByZXN0YXJ0OiBhbHdheXNcbiAgICBkZXBlbmRzX29uOlxuICAgICAgLSBtb25nb2RiXG4gICAgICAtIHJhZ19hcGlcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgICMgU2VydmVyIENvbmZpZ3VyYXRpb25cbiAgICAgIC0gSE9TVD0wLjAuMC4wXG4gICAgICAtIFBPUlQ9JHtQT1JUOi0zMDgwfVxuICAgICAgIyBEb21haW4gQ29uZmlndXJhdGlvblxuICAgICAgLSBET01BSU5fQ0xJRU5UPSR7RE9NQUlOX0NMSUVOVH1cbiAgICAgIC0gRE9NQUlOX1NFUlZFUj0ke0RPTUFJTl9TRVJWRVJ9XG4gICAgICAjIERhdGFiYXNlIGFuZCBTZWFyY2ggQ29uZmlndXJhdGlvblxuICAgICAgLSBNT05HT19VUkk9bW9uZ29kYjovL21vbmdvZGI6MjcwMTcvTGlicmVDaGF0XG4gICAgICAtIE1FSUxJX0hPU1Q9aHR0cDovL21laWxpc2VhcmNoOjc3MDBcbiAgICAgIC0gU0VBUkNIPXRydWVcbiAgICAgIC0gTk9fSU5ERVg9dHJ1ZVxuICAgICAgLSBNRUlMSV9OT19BTkFMWVRJQ1M9dHJ1ZVxuICAgICAgLSBNRUlMSV9NQVNURVJfS0VZPSR7TUVJTElfTUFTVEVSX0tFWX1cbiAgICAgICMgU2VjdXJpdHkgJiBTZXNzaW9uc1xuICAgICAgLSBKV1RfU0VDUkVUPSR7SldUX1NFQ1JFVH1cbiAgICAgIC0gSldUX1JFRlJFU0hfU0VDUkVUPSR7SldUX1JFRlJFU0hfU0VDUkVUfVxuICAgICAgLSBDUkVEU19LRVk9JHtDUkVEU19LRVl9XG4gICAgICAtIENSRURTX0lWPSR7Q1JFRFNfSVZ9XG4gICAgICAtIFJBR19QT1JUPSR7UkFHX1BPUlQ6LTgwMDB9XG4gICAgICAtIFJBR19BUElfVVJMPWh0dHA6Ly9yYWdfYXBpOiR7UkFHX1BPUlQ6LTgwMDB9XG4gICAgICAjIEFQSSBLZXlzIGFuZCBTZWNyZXRzXG4gICAgICAtIE9QRU5BSV9BUElfS0VZPSR7T1BFTkFJX0FQSV9LRVl9XG4gICAgICAtIEFOVEhST1BJQ19BUElfS0VZPSR7QU5USFJPUElDX0FQSV9LRVl9XG4gICAgICAtIE9QRU5ST1VURVJfS0VZPSR7T1BFTlJPVVRFUl9LRVl9XG4gICAgICAtIEdPT0dMRV9LRVk9JHtHT09HTEVfS0VZfVxuICAgICAgLSBFTkRQT0lOVFM9Z29vZ2xlLG9wZW5BSSxhc3Npc3RhbnRzLGF6dXJlT3BlbkFJLGFudGhyb3BpY1xuICAgICAgIyAuLi4gQWRkaXRpb25hbCBFbmRwb2ludHNcbiAgICAgICMgVUlcbiAgICAgIC0gQVBQX1RJVExFPSR7QVBQX1RJVExFOi1MaWJyZUNoYXR9XG4gICAgICAtIENVU1RPTV9GT09URVI9JHtDVVNUT01fRk9PVEVSOi1NYWRlIHdpdGgg4p2k77iPIGJ5IExpYnJlQ2hhdH1cbiAgICAgIC0gQUxMT1dfRU1BSUxfTE9HSU49JHtBTExPV19FTUFJTF9MT0dJTjotdHJ1ZX1cbiAgICAgIC0gQUxMT1dfU09DSUFMX0xPR0lOPSR7QUxMT1dfU09DSUFMX0xPR0lOOi1mYWxzZX1cbiAgICAgIC0gQUxMT1dfUkVHSVNUUkFUSU9OPSR7QUxMT1dfUkVHSVNUUkFUSU9OOi1mYWxzZX1cbiAgICB2b2x1bWVzOlxuICAgICAgLSB0eXBlOiBiaW5kXG4gICAgICAgIHNvdXJjZTogLi4vZmlsZXMvbGlicmVjaGF0LnlhbWxcbiAgICAgICAgdGFyZ2V0OiAvYXBwL2xpYnJlY2hhdC55YW1sXG4gICAgICAtIGxpYnJlY2hhdF9kYXRhOi9hcHAvY2xpZW50L3B1YmxpYy9pbWFnZXNcbiAgICAgIC0gbGlicmVjaGF0X2RhdGE6L2FwcC91cGxvYWRzXG4gICAgICAtIGxpYnJlY2hhdF9kYXRhOi9hcHAvbG9nc1xuXG4gIG1vbmdvZGI6XG4gICAgaW1hZ2U6IG1vbmdvXG4gICAgcmVzdGFydDogYWx3YXlzXG4gICAgdm9sdW1lczpcbiAgICAgIC0gbW9uZ29fZGF0YTovZGF0YS9kYlxuICAgIGNvbW1hbmQ6IG1vbmdvZCAtLW5vYXV0aFxuXG4gIG1laWxpc2VhcmNoOlxuICAgIGltYWdlOiBnZXRtZWlsaS9tZWlsaXNlYXJjaDp2MS4xMi4zXG4gICAgcmVzdGFydDogYWx3YXlzXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIE1FSUxJX0hPU1Q9aHR0cDovL21laWxpc2VhcmNoOjc3MDBcbiAgICAgIC0gTUVJTElfTk9fQU5BTFlUSUNTPXRydWVcbiAgICAgIC0gTUVJTElfTUFTVEVSX0tFWT0ke01FSUxJX01BU1RFUl9LRVl9XG4gICAgdm9sdW1lczpcbiAgICAgIC0gbWVpbGlfZGF0YTovbWVpbGlfZGF0YVxuXG4gIHZlY3RvcmRiOlxuICAgIGltYWdlOiBwZ3ZlY3Rvci9wZ3ZlY3RvcjowLjguMC1wZzE1LXRyaXhpZVxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBQT1NUR1JFU19EQj0ke1BPU1RHUkVTX0RCOi1teWRhdGFiYXNlfVxuICAgICAgLSBQT1NUR1JFU19VU0VSPSR7UE9TVEdSRVNfVVNFUjotbXl1c2VyfVxuICAgICAgLSBQT1NUR1JFU19QQVNTV09SRD0ke1BPU1RHUkVTX1BBU1NXT1JEOi1teXBhc3N3b3JkfVxuICAgIHJlc3RhcnQ6IGFsd2F5c1xuICAgIHZvbHVtZXM6XG4gICAgICAtIHBvc3RncmVzX2RhdGE6L3Zhci9saWIvcG9zdGdyZXNxbC9kYXRhXG5cbiAgcmFnX2FwaTpcbiAgICBpbWFnZTogZ2hjci5pby9kYW5ueS1hdmlsYS9saWJyZWNoYXQtcmFnLWFwaS1kZXYtbGl0ZTpsYXRlc3RcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gREJfSE9TVD12ZWN0b3JkYlxuICAgICAgLSBWRUNUT1JfREJfVFlQRT1wZ3ZlY3RvclxuICAgICAgLSBQT1NUR1JFU19EQj0ke1BPU1RHUkVTX0RCOi1teWRhdGFiYXNlfVxuICAgICAgLSBQT1NUR1JFU19VU0VSPSR7UE9TVEdSRVNfVVNFUjotbXl1c2VyfVxuICAgICAgLSBQT1NUR1JFU19QQVNTV09SRD0ke1BPU1RHUkVTX1BBU1NXT1JEOi1teXBhc3N3b3JkfVxuICAgICAgLSBSQUdfUE9SVD0ke1JBR19QT1JUOi04MDAwfVxuICAgICAgLSBPUEVOQUlfQVBJX0tFWT0ke09QRU5BSV9BUElfS0VZfVxuICAgICAgLSBSQUdfT1BFTkFJX0FQSV9LRVk9JHtSQUdfT1BFTkFJX0FQSV9LRVl9XG4gICAgICAtIEdPT0dMRV9LRVk9JHtHT09HTEVfS0VZfVxuICAgICAgLSBSQUdfR09PR0xFX0FQSV9LRVk9JHtSQUdfR09PR0xFX0FQSV9LRVl9XG4gICAgICAtIEpXVF9TRUNSRVQ9JHtKV1RfU0VDUkVUfVxuICAgICAgLSBDT0xMRUNUSU9OX05BTUU9JHtDT0xMRUNUSU9OX05BTUU6LWxpYnJlY2hhdF9jb2xsZWN0aW9ufVxuICAgICAgLSBDSFVOS19TSVpFPSR7Q0hVTktfU0laRTotMTUwMH1cbiAgICAgIC0gQ0hVTktfT1ZFUkxBUD0ke0NIVU5LX09WRVJMQVA6LTEwMH1cbiAgICAgIC0gRU1CRURESU5HU19QUk9WSURFUj0ke0VNQkVERElOR1NfUFJPVklERVI6LW9wZW5haX1cbiAgICAgIC0gRU1CRURESU5HU19NT0RFTD0ke0VNQkVERElOR1NfTU9ERUw6LXRleHQtZW1iZWRkaW5nLTMtc21hbGx9XG4gICAgICAtIERFQlVHX1JBR19BUEk9ZmFsc2VcbiAgICAgIC0gREVCVUdfUEdWRUNUT1JfUVVFUklFUz1mYWxzZVxuICAgICAgLSBDT05TT0xFX0pTT049ZmFsc2VcbiAgICByZXN0YXJ0OiBhbHdheXNcbiAgICBkZXBlbmRzX29uOlxuICAgICAgLSB2ZWN0b3JkYlxuXG52b2x1bWVzOlxuICBtb25nb19kYXRhOlxuICBtZWlsaV9kYXRhOlxuICBwb3N0Z3Jlc19kYXRhOlxuICBsaWJyZWNoYXRfZGF0YToiLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbiMgRG9tYWluIENvbmZpZ3VyYXRpb25cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuXG4jIFNlY3VyaXR5ICYgQXV0aGVudGljYXRpb25cbmp3dF9zZWNyZXQgPSBcIiR7cGFzc3dvcmQ6NjR9XCJcbmp3dF9yZWZyZXNoX3NlY3JldCA9IFwiJHtwYXNzd29yZDo2NH1cIlxuY3JlZHNfa2V5ID0gXCJmMzRiZTQyN2ViYjI5ZGU4ZDg4YzEwN2E3MTU0NjAxOTY4NWVkOGIyNDFkOGYyZWQwMGMzZGY5N2FkMjU2NmYwXCJcbmNyZWRzX2l2ID0gXCJlMjM0MTQxOWVjM2RkM2QxOWIxM2ExYTg3ZmFmY2JmYlwiXG5tZWlsaV9tYXN0ZXJfa2V5ID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5cbiMgRGF0YWJhc2UgQ29uZmlndXJhdGlvblxubW9uZ29fcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MTZ9XCJcbnBvc3RncmVzcWxfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MTZ9XCJcblxuW2NvbmZpZ11cbnZlcnNpb24gPSBcIjEuMC4wXCJcbiMgTWFpbiBzZXJ2aWNlIGRvbWFpbiBtYXBwaW5nXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJsaWJyZWNoYXRcIlxucG9ydCA9IDMwODBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG4jIEJhc2ljIENvbmZpZ3VyYXRpb25cbkhPU1Q9XCIwLjAuMC4wXCJcblBPUlQ9XCIzMDgwXCJcbkRPTUFJTl9DTElFTlQ9XCJodHRwczovLyR7bWFpbl9kb21haW59XCJcbkRPTUFJTl9TRVJWRVI9XCJodHRwczovLyR7bWFpbl9kb21haW59XCJcblxuIyBTZWFyY2ggQ29uZmlndXJhdGlvblxuTUVJTElfTUFTVEVSX0tFWT1cIiR7bWVpbGlfbWFzdGVyX2tleX1cIlxuXG4jIFNlY3VyaXR5XG5KV1RfU0VDUkVUPVwiJHtqd3Rfc2VjcmV0fVwiXG5KV1RfUkVGUkVTSF9TRUNSRVQ9XCIke2p3dF9yZWZyZXNoX3NlY3JldH1cIlxuQ1JFRFNfS0VZPVwiJHtjcmVkc19rZXl9XCJcbkNSRURTX0lWPVwiJHtjcmVkc19pdn1cIlxuXG4jIEFQSSBLZXlzXG5PUEVOQUlfQVBJX0tFWT1cIlwiXG5BTlRIUk9QSUNfQVBJX0tFWT1cIlwiXG5HT09HTEVfS0VZPVwiXCJcbk9QRU5ST1VURVJfS0VZPVwiXCJcblxuIyBEYXRhYmFzZVxuUE9TVEdSRVNfREI9XCJsaWJyZWNoYXRfZGJcIlxuUE9TVEdSRVNfVVNFUj1cImxpYnJlY2hhdF91c2VyXCJcblBPU1RHUkVTX1BBU1NXT1JEPVwiJHtwb3N0Z3Jlc3FsX3Bhc3N3b3JkfVwiXG5cbiMgU2VjdXJpdHkgJiBTZXNzaW9uc1xuXG4jIFVzZXIgSW50ZXJmYWNlXG5BUFBfVElUTEU9XCJMaWJyZUNoYXRcIlxuQ1VTVE9NX0ZPT1RFUj1cIk1hZGUgd2l0aCDinaTvuI8gYnkgTGlicmVDaGF0XCJcbkFMTE9XX0VNQUlMX0xPR0lOPVwidHJ1ZVwiXG5BTExPV19SRUdJU1RSQVRJT049XCJmYWxzZVwiXG5BTExPV19TT0NJQUxfTE9HSU49XCJmYWxzZVwiXG5cbiMgUkFHXG5SQUdfT1BFTkFJX0FQSV9LRVk9XCJcIlxuUkFHX0dPT0dMRV9BUElfS0VZPVwiXCJcbkVNQkVERElOR1NfUFJPVklERVI9XCJvcGVuYWlcIlxuRU1CRURESU5HU19NT0RFTD1cInRleHQtZW1iZWRkaW5nLTMtc21hbGxcIlxuXG5DSFVOS19TSVpFPTE1MDBcbkNIVU5LX09WRVJMQVA9MTAwXG5cblxuXG5bW2NvbmZpZy5tb3VudHNdXVxuZmlsZVBhdGggPSBcImxpYnJlY2hhdC55YW1sXCJcbmNvbnRlbnQgPSBcIlwiXCJcbiMjIyBsaWJyZWNoYXQueWFtbCBjb25maWdzICMjI1xuXG52ZXJzaW9uOiAxLjIuOFxuY2FjaGU6IHRydWVcbmVuZHBvaW50czpcbiAgY3VzdG9tOlxuICAgIC0gbmFtZTogXCJPcGVuUm91dGVyXCJcbiAgICAgIGFwaUtleTogXCIke09QRU5ST1VURVJfS0VZfVwiXG4gICAgICBiYXNlVVJMOiBcImh0dHBzOi8vb3BlbnJvdXRlci5haS9hcGkvdjFcIlxuICAgICAgbW9kZWxzOlxuICAgICAgICBkZWZhdWx0OiBbXCJtZXRhLWxsYW1hL2xsYW1hLTMuMy03MGItaW5zdHJ1Y3Q6ZnJlZVwiXVxuICAgICAgICBmZXRjaDogdHJ1ZVxuICAgICAgdGl0bGVDb252bzogdHJ1ZVxuICAgICAgdGl0bGVNb2RlbDogXCJjdXJyZW50X21vZGVsXCJcbiAgICAgIHN1bW1hcml6ZTogZmFsc2VcbiAgICAgIHN1bW1hcnlNb2RlbDogXCJjdXJyZW50X21vZGVsXCJcbiAgICAgIGZvcmNlUHJvbXB0OiBmYWxzZVxuICAgICAgZHJvcFBhcmFtczogW1wic3RvcFwiXVxuICAgICAgbW9kZWxEaXNwbGF5TGFiZWw6IFwiT3BlblJvdXRlclwiXG5cIlwiXCIiCn0=
```

## Links

`ai`,`chatbot`,`llm`,`MIT-license`,`BYOK`,`generative-ai`

---

Version:`latest`

LetterfeedConvert email newsletters into RSS feeds

LibredeskOpen source, self-hosted customer support desk. Single binary app.

### On this page

ConfigurationBase64LinksTags