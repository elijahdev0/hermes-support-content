---
title: "Stirling PDF | Dokploy"
source: "https://docs.dokploy.com/docs/templates/stirling"
category: dokploy-docs
created: "2026-06-25T17:21:59.115Z"
---

Stirling PDF | Dokploy

# Stirling PDF

Copy as Markdown

A locally hosted one-stop shop for all your PDF needs

## Configuration

docker-compose.ymltemplate.toml

```
services:
  stirling-pdf:
    image: docker.stirlingpdf.com/stirlingtools/stirling-pdf:latest
    ports:
      - 8080
    volumes:
      - stirling_pdf_trainingdata:/usr/share/tessdata # Required for extra OCR languages
      - stirling_pdf_extraconfigs:/configs
      - stirling_pdf_customfiles:/customFiles/
      - stirling_pdf_logs:/logs/
      - stirling_pdf_pipeline:/pipeline/
    environment:
      - DOCKER_ENABLE_SECURITY=false
      - LANGS=en_GB
volumes:
  stirling_pdf_trainingdata:
  stirling_pdf_extraconfigs:
  stirling_pdf_customfiles:
  stirling_pdf_logs:
  stirling_pdf_pipeline:
```

```
[variables]
main_domain = "${domain}"

[config]
env = {}
mounts = []

[[config.domains]]
serviceName = "stirling-pdf"
port = 8_080
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBzdGlybGluZy1wZGY6XG4gICAgaW1hZ2U6IGRvY2tlci5zdGlybGluZ3BkZi5jb20vc3Rpcmxpbmd0b29scy9zdGlybGluZy1wZGY6bGF0ZXN0XG4gICAgcG9ydHM6XG4gICAgICAtIDgwODBcbiAgICB2b2x1bWVzOlxuICAgICAgLSBzdGlybGluZ19wZGZfdHJhaW5pbmdkYXRhOi91c3Ivc2hhcmUvdGVzc2RhdGEgIyBSZXF1aXJlZCBmb3IgZXh0cmEgT0NSIGxhbmd1YWdlc1xuICAgICAgLSBzdGlybGluZ19wZGZfZXh0cmFjb25maWdzOi9jb25maWdzXG4gICAgICAtIHN0aXJsaW5nX3BkZl9jdXN0b21maWxlczovY3VzdG9tRmlsZXMvXG4gICAgICAtIHN0aXJsaW5nX3BkZl9sb2dzOi9sb2dzL1xuICAgICAgLSBzdGlybGluZ19wZGZfcGlwZWxpbmU6L3BpcGVsaW5lL1xuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBET0NLRVJfRU5BQkxFX1NFQ1VSSVRZPWZhbHNlXG4gICAgICAtIExBTkdTPWVuX0dCXG52b2x1bWVzOlxuICBzdGlybGluZ19wZGZfdHJhaW5pbmdkYXRhOlxuICBzdGlybGluZ19wZGZfZXh0cmFjb25maWdzOlxuICBzdGlybGluZ19wZGZfY3VzdG9tZmlsZXM6XG4gIHN0aXJsaW5nX3BkZl9sb2dzOlxuICBzdGlybGluZ19wZGZfcGlwZWxpbmU6IiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcblxuW2NvbmZpZ11cbmVudiA9IHt9XG5tb3VudHMgPSBbXVxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJzdGlybGluZy1wZGZcIlxucG9ydCA9IDhfMDgwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG4iCn0=
```

## Links

`pdf`,`tools`

---

Version:`0.30.1`

Statping-NGStatping-NG is an easy-to-use status page for monitoring websites and applications with beautiful metrics, analytics, and health checks.

StorydenWith a fresh new take on traditional bulletin board forum software, Storyden is a modern, secure and extensible platform for building communities.

### On this page

ConfigurationBase64LinksTags