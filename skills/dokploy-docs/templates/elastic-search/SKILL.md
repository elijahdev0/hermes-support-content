---
title: "Elasticsearch | Dokploy"
source: "https://docs.dokploy.com/docs/templates/elastic-search"
category: dokploy-docs
created: "2026-06-25T17:21:47.358Z"
---

Elasticsearch | Dokploy

# Elasticsearch

Copy as Markdown

Elasticsearch is an open-source search and analytics engine, used for full-text search and analytics on structured data such as text, web pages, images, and videos.

## Configuration

docker-compose.ymltemplate.toml

```
version: '3.8'

services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:8.10.2
    container_name: elasticsearch
    environment:
      - discovery.type=single-node
      - xpack.security.enabled=false
      - bootstrap.memory_lock=true
      - ES_JAVA_OPTS=-Xms512m -Xmx512m
    ulimits:
      memlock:
        soft: -1
        hard: -1
    ports:
      - "9200"
    volumes:
      - es_data:/usr/share/elasticsearch/data

  kibana:
    image: docker.elastic.co/kibana/kibana:8.10.2
    container_name: kibana
    environment:
      - ELASTICSEARCH_HOSTS=http://elasticsearch:9200
    ports:
      - "5601"
    depends_on:
      - elasticsearch

volumes:
  es_data:
    driver: local
```

```
[variables]
main_domain = "${domain}"
api_domain = "${domain}"

[config]
env = []
mounts = []

[[config.domains]]
serviceName = "kibana"
port = 5_601
host = "${main_domain}"

[[config.domains]]
serviceName = "elasticsearch"
port = 9_200
host = "${api_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246ICczLjgnXG5cbnNlcnZpY2VzOlxuICBlbGFzdGljc2VhcmNoOlxuICAgIGltYWdlOiBkb2NrZXIuZWxhc3RpYy5jby9lbGFzdGljc2VhcmNoL2VsYXN0aWNzZWFyY2g6OC4xMC4yXG4gICAgY29udGFpbmVyX25hbWU6IGVsYXN0aWNzZWFyY2hcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gZGlzY292ZXJ5LnR5cGU9c2luZ2xlLW5vZGVcbiAgICAgIC0geHBhY2suc2VjdXJpdHkuZW5hYmxlZD1mYWxzZVxuICAgICAgLSBib290c3RyYXAubWVtb3J5X2xvY2s9dHJ1ZVxuICAgICAgLSBFU19KQVZBX09QVFM9LVhtczUxMm0gLVhteDUxMm1cbiAgICB1bGltaXRzOlxuICAgICAgbWVtbG9jazpcbiAgICAgICAgc29mdDogLTFcbiAgICAgICAgaGFyZDogLTFcbiAgICBwb3J0czpcbiAgICAgIC0gXCI5MjAwXCJcbiAgICB2b2x1bWVzOlxuICAgICAgLSBlc19kYXRhOi91c3Ivc2hhcmUvZWxhc3RpY3NlYXJjaC9kYXRhXG5cbiAga2liYW5hOlxuICAgIGltYWdlOiBkb2NrZXIuZWxhc3RpYy5jby9raWJhbmEva2liYW5hOjguMTAuMlxuICAgIGNvbnRhaW5lcl9uYW1lOiBraWJhbmFcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gRUxBU1RJQ1NFQVJDSF9IT1NUUz1odHRwOi8vZWxhc3RpY3NlYXJjaDo5MjAwXG4gICAgcG9ydHM6XG4gICAgICAtIFwiNTYwMVwiXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIC0gZWxhc3RpY3NlYXJjaFxuXG52b2x1bWVzOlxuICBlc19kYXRhOlxuICAgIGRyaXZlcjogbG9jYWxcbiAiLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuYXBpX2RvbWFpbiA9IFwiJHtkb21haW59XCJcblxuW2NvbmZpZ11cbmVudiA9IFtdXG5tb3VudHMgPSBbXVxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJraWJhbmFcIlxucG9ydCA9IDVfNjAxXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImVsYXN0aWNzZWFyY2hcIlxucG9ydCA9IDlfMjAwXG5ob3N0ID0gXCIke2FwaV9kb21haW59XCJcbiIKfQ==
```

## Links

`search`,`analytics`

---

Version:`8.10.2`

Easy!AppointmentsEasy!Appointments is a highly customizable web application that allows customers to book appointments with you via a sophisticated web interface.

EmbyEmby Server is a personal media server with apps on just about every device.

### On this page

ConfigurationBase64LinksTags