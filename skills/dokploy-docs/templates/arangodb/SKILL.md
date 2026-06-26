---
title: "ArangoDB | Dokploy"
source: "https://docs.dokploy.com/docs/templates/arangodb"
category: dokploy-docs
created: "2026-06-25T17:21:41.529Z"
---

ArangoDB | Dokploy

# ArangoDB

Copy as Markdown

ArangoDB is a native multi-model database with flexible data models for documents, graphs, and key-values. Build high performance applications using a convenient SQL-like query language or JavaScript extensions.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  arangodb:
    image: arangodb:3.12.4
    restart: unless-stopped
    ports:
      - 8529
    environment:
      - ARANGO_ROOT_PASSWORD=${ARANGO_PASSWORD}
    volumes:
      - data:/var/lib/arangodb3

volumes:
  data: {}
```

```
[variables]
main_domain = "${domain}"
arango_password = "${password:16}"

[config]
[[config.domains]]
serviceName = "arangodb"
port = 8529
host = "${main_domain}"

[config.env]
ARANGO_PASSWORD = "${arango_password}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBhcmFuZ29kYjpcbiAgICBpbWFnZTogYXJhbmdvZGI6My4xMi40XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBwb3J0czpcbiAgICAgIC0gODUyOVxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBBUkFOR09fUk9PVF9QQVNTV09SRD0ke0FSQU5HT19QQVNTV09SRH1cbiAgICB2b2x1bWVzOlxuICAgICAgLSBkYXRhOi92YXIvbGliL2FyYW5nb2RiM1xuXG52b2x1bWVzOlxuICBkYXRhOiB7fSAiLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuYXJhbmdvX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkOjE2fVwiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJhcmFuZ29kYlwiXG5wb3J0ID0gODUyOVxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cbkFSQU5HT19QQVNTV09SRCA9IFwiJHthcmFuZ29fcGFzc3dvcmR9XCIgIgp9
```

## Links

`database`,`graph-database`,`nosql`

---

Version:`latest`

AptabaseAptabase is a self-hosted web analytics platform that lets you track website traffic and user behavior.

ArgillaArgilla is a robust platform designed to help engineers and data scientists streamline the management of machine learning data workflows. It simplifies tasks like data labeling, annotation, and quality control.

### On this page

ConfigurationBase64LinksTags