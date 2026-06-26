---
title: "Docling Serve | Dokploy"
source: "https://docs.dokploy.com/docs/templates/docling-serve"
category: dokploy-docs
created: "2026-06-25T17:21:46.245Z"
---

Docling Serve | Dokploy

# Docling Serve

Copy as Markdown

Running Docling as an API service for document processing and conversion with AI-powered capabilities.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  docling-serve:
    image: quay.io/docling-project/docling-serve:latest
    restart: unless-stopped
    ports:
      - 5001
    environment:
      - DOCLING_SERVE_ENABLE_UI=1
      - DOCLING_SERVE_HOST=0.0.0.0
      - DOCLING_SERVE_PORT=5001
    volumes:
      - docling-data:/app/data
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:5001/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s

volumes:
  docling-data: {}
```

```
[variables]
main_domain = "${domain}"

[config]
[[config.domains]]
serviceName = "docling-serve"
port = 5001
host = "${main_domain}"

[config.env]
DOCLING_SERVE_ENABLE_UI = "1"
DOCLING_SERVE_HOST = "0.0.0.0"
DOCLING_SERVE_PORT = "5001"

[[config.mounts]]
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBkb2NsaW5nLXNlcnZlOlxuICAgIGltYWdlOiBxdWF5LmlvL2RvY2xpbmctcHJvamVjdC9kb2NsaW5nLXNlcnZlOmxhdGVzdFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgcG9ydHM6XG4gICAgICAtIDUwMDFcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gRE9DTElOR19TRVJWRV9FTkFCTEVfVUk9MVxuICAgICAgLSBET0NMSU5HX1NFUlZFX0hPU1Q9MC4wLjAuMFxuICAgICAgLSBET0NMSU5HX1NFUlZFX1BPUlQ9NTAwMVxuICAgIHZvbHVtZXM6XG4gICAgICAtIGRvY2xpbmctZGF0YTovYXBwL2RhdGFcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6IFtcIkNNRFwiLCBcImN1cmxcIiwgXCItZlwiLCBcImh0dHA6Ly9sb2NhbGhvc3Q6NTAwMS9oZWFsdGhcIl1cbiAgICAgIGludGVydmFsOiAzMHNcbiAgICAgIHRpbWVvdXQ6IDEwc1xuICAgICAgcmV0cmllczogM1xuICAgICAgc3RhcnRfcGVyaW9kOiA0MHNcblxudm9sdW1lczpcbiAgZG9jbGluZy1kYXRhOiB7fVxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcblxuW2NvbmZpZ11cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImRvY2xpbmctc2VydmVcIlxucG9ydCA9IDUwMDFcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5ET0NMSU5HX1NFUlZFX0VOQUJMRV9VSSA9IFwiMVwiXG5ET0NMSU5HX1NFUlZFX0hPU1QgPSBcIjAuMC4wLjBcIlxuRE9DTElOR19TRVJWRV9QT1JUID0gXCI1MDAxXCJcblxuW1tjb25maWcubW91bnRzXV1cbiIKfQ==
```

## Links

`document-processing`,`api`,`ai`,`conversion`,`pdf`,`office`

---

Version:`latest`

DiscourseDiscourse is a modern forum software for your community. Use it as a mailing list, discussion forum, or long-form chat room.

DocmostDocmost, is an open-source collaborative wiki and documentation software.

### On this page

ConfigurationBase64LinksTags