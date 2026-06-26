---
title: "Coral | Dokploy"
source: "https://docs.dokploy.com/docs/templates/coralproject"
category: dokploy-docs
created: "2026-06-25T17:21:45.077Z"
---

Coral | Dokploy

# Coral

Copy as Markdown

Coral is a revolutionary commenting platform designed to enhance website interactions. It features smart technology for meaningful discussions, journalist identification, moderation tools with AI support, and complete data control without ads or trackers. Used by major news sites worldwide.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3"

services:
  coral:
    image: coralproject/talk:9.7.0
    ports:
      - "3000"
    environment:
      - MONGODB_URI=${MONGODB_URI}
      - REDIS_URI=${REDIS_URI}
      - SIGNING_SECRET=${SIGNING_SECRET}
      - NODE_ENV=production
    depends_on:
      - mongo
      - redis

  mongo:
    image: mongo:4
    environment:
      - MONGO_INITDB_ROOT_PASSWORD=${MONGO_PASSWORD}
      - MONGO_INITDB_ROOT_USERNAME=${MONGO_USER}
    volumes:
      - mongo-data:/data/db

  redis:
    image: redis:6
    command: redis-server --requirepass ${REDIS_PASSWORD}
    volumes:
      - redis-data:/data

volumes:
  mongo-data:
  redis-data:
```

```
[variables]
DOMAIN = "${domain}"
MONGO_PASSWORD = "${password:16}"
REDIS_PASSWORD = "${password:16}"
SIGNING_SECRET = "${password:45}"

[config]
[[config.domains]]
serviceName = "coral"
port = 3000
host = "${DOMAIN}"

[config.env]
MONGODB_URI = "mongodb://mongo:${MONGO_PASSWORD}@mongo:27017"
REDIS_URI = "redis://default:${REDIS_PASSWORD}@redis:6379"
SIGNING_SECRET = "${SIGNING_SECRET}"
NODE_ENV = "production"
MONGO_PASSWORD = "${MONGO_PASSWORD}"
REDIS_PASSWORD = "${REDIS_PASSWORD}"
MONGO_USER = "mongo"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiM1wiXG5cbnNlcnZpY2VzOlxuICBjb3JhbDpcbiAgICBpbWFnZTogY29yYWxwcm9qZWN0L3RhbGs6OS43LjBcbiAgICBwb3J0czpcbiAgICAgIC0gXCIzMDAwXCJcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gTU9OR09EQl9VUkk9JHtNT05HT0RCX1VSSX1cbiAgICAgIC0gUkVESVNfVVJJPSR7UkVESVNfVVJJfVxuICAgICAgLSBTSUdOSU5HX1NFQ1JFVD0ke1NJR05JTkdfU0VDUkVUfVxuICAgICAgLSBOT0RFX0VOVj1wcm9kdWN0aW9uXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIC0gbW9uZ29cbiAgICAgIC0gcmVkaXNcblxuICBtb25nbzpcbiAgICBpbWFnZTogbW9uZ286NFxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBNT05HT19JTklUREJfUk9PVF9QQVNTV09SRD0ke01PTkdPX1BBU1NXT1JEfVxuICAgICAgLSBNT05HT19JTklUREJfUk9PVF9VU0VSTkFNRT0ke01PTkdPX1VTRVJ9XG4gICAgdm9sdW1lczpcbiAgICAgIC0gbW9uZ28tZGF0YTovZGF0YS9kYlxuXG4gIHJlZGlzOlxuICAgIGltYWdlOiByZWRpczo2XG4gICAgY29tbWFuZDogcmVkaXMtc2VydmVyIC0tcmVxdWlyZXBhc3MgJHtSRURJU19QQVNTV09SRH1cbiAgICB2b2x1bWVzOlxuICAgICAgLSByZWRpcy1kYXRhOi9kYXRhXG5cbnZvbHVtZXM6XG4gIG1vbmdvLWRhdGE6XG4gIHJlZGlzLWRhdGE6ICIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxuRE9NQUlOID0gXCIke2RvbWFpbn1cIlxuTU9OR09fUEFTU1dPUkQgPSBcIiR7cGFzc3dvcmQ6MTZ9XCJcblJFRElTX1BBU1NXT1JEID0gXCIke3Bhc3N3b3JkOjE2fVwiXG5TSUdOSU5HX1NFQ1JFVCA9IFwiJHtwYXNzd29yZDo0NX1cIlxuXG5bY29uZmlnXVxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiY29yYWxcIlxucG9ydCA9IDMwMDBcbmhvc3QgPSBcIiR7RE9NQUlOfVwiXG5cbltjb25maWcuZW52XVxuTU9OR09EQl9VUkkgPSBcIm1vbmdvZGI6Ly9tb25nbzoke01PTkdPX1BBU1NXT1JEfUBtb25nbzoyNzAxN1wiXG5SRURJU19VUkkgPSBcInJlZGlzOi8vZGVmYXVsdDoke1JFRElTX1BBU1NXT1JEfUByZWRpczo2Mzc5XCJcblNJR05JTkdfU0VDUkVUID0gXCIke1NJR05JTkdfU0VDUkVUfVwiXG5OT0RFX0VOViA9IFwicHJvZHVjdGlvblwiXG5NT05HT19QQVNTV09SRCA9IFwiJHtNT05HT19QQVNTV09SRH1cIlxuUkVESVNfUEFTU1dPUkQgPSBcIiR7UkVESVNfUEFTU1dPUkR9XCIgXG5NT05HT19VU0VSID0gXCJtb25nb1wiIgp9
```

## Links

`communication`,`community`,`privacy`

---

Version:`9.7.0`

CookieCloudCookieCloud lets you sync and manage browser cookies across devices securely using a self-hosted backend.

CouchDBCouchDB is a document-oriented NoSQL database that excels at replication and horizontal scaling.

### On this page

ConfigurationBase64LinksTags