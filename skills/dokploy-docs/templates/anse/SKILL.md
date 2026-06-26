---
title: "Anse | Dokploy"
source: "https://docs.dokploy.com/docs/templates/anse"
category: dokploy-docs
created: "2026-06-25T17:21:40.414Z"
---

Anse | Dokploy

# Anse

Copy as Markdown

Anse is an open-source alternative to ChatGPT web UI, supporting OpenAI-compatible APIs.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  anse-demo:
    image: ddiu8081/anse:latest
    restart: always
    expose:
      - 3000
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
      - OPENAI_API_BASE_URL=${OPENAI_API_BASE_URL}
      - HEAD_SCRIPTS=${HEAD_SCRIPTS}
      - SECRET_KEY=${SECRET_KEY}
      - SITE_PASSWORD=${SITE_PASSWORD}
      - OPENAI_API_MODEL=${OPENAI_API_MODEL}
```

```
[variables]
main_domain = "${domain}"
secret_key = "${password:32}"
site_password = "${password:16}"

[config]
[[config.domains]]
serviceName = "anse-demo"
port = 3000
host = "${main_domain}"

[config.env]
OPENAI_API_KEY = ""
OPENAI_API_BASE_URL = "https://api.openai.com"
HEAD_SCRIPTS = ""
SECRET_KEY = "${secret_key}"
SITE_PASSWORD = "${site_password}"
OPENAI_API_MODEL = "gpt-4o-mini"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIGFuc2UtZGVtbzpcbiAgICBpbWFnZTogZGRpdTgwODEvYW5zZTpsYXRlc3RcbiAgICByZXN0YXJ0OiBhbHdheXNcbiAgICBleHBvc2U6XG4gICAgICAtIDMwMDBcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gT1BFTkFJX0FQSV9LRVk9JHtPUEVOQUlfQVBJX0tFWX1cbiAgICAgIC0gT1BFTkFJX0FQSV9CQVNFX1VSTD0ke09QRU5BSV9BUElfQkFTRV9VUkx9XG4gICAgICAtIEhFQURfU0NSSVBUUz0ke0hFQURfU0NSSVBUU31cbiAgICAgIC0gU0VDUkVUX0tFWT0ke1NFQ1JFVF9LRVl9XG4gICAgICAtIFNJVEVfUEFTU1dPUkQ9JHtTSVRFX1BBU1NXT1JEfVxuICAgICAgLSBPUEVOQUlfQVBJX01PREVMPSR7T1BFTkFJX0FQSV9NT0RFTH1cbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5zZWNyZXRfa2V5ID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5zaXRlX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkOjE2fVwiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJhbnNlLWRlbW9cIlxucG9ydCA9IDMwMDBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5PUEVOQUlfQVBJX0tFWSA9IFwiXCJcbk9QRU5BSV9BUElfQkFTRV9VUkwgPSBcImh0dHBzOi8vYXBpLm9wZW5haS5jb21cIlxuSEVBRF9TQ1JJUFRTID0gXCJcIlxuU0VDUkVUX0tFWSA9IFwiJHtzZWNyZXRfa2V5fVwiXG5TSVRFX1BBU1NXT1JEID0gXCIke3NpdGVfcGFzc3dvcmR9XCJcbk9QRU5BSV9BUElfTU9ERUwgPSBcImdwdC00by1taW5pXCIiCn0=
```

## Links

`ai`,`chatbot`,`openai`,`ui`

---

Version:`latest`

AnonUploadAnonUpload is a secure, anonymous file sharing application that does not require a database. It is built with privacy as a priority, ensuring that the direct filename used is not displayed.

AnswerAnswer is an open-source Q&A platform for building a self-hosted question-and-answer service.

### On this page

ConfigurationBase64LinksTags