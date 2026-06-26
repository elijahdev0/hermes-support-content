---
title: "Huly | Dokploy"
source: "https://docs.dokploy.com/docs/templates/huly"
category: dokploy-docs
created: "2026-06-25T17:21:49.750Z"
---

Huly | Dokploy

# Huly

Copy as Markdown

Huly — All-in-One Project Management Platform (alternative to Linear, Jira, Slack, Notion, Motion)

## Configuration

docker-compose.ymltemplate.toml

```
name: ${DOCKER_NAME}
version: "3"
services:
  nginx:

    image: "nginx:1.21.3"
    ports:
      - 80
    volumes:
      - ../files/volumes/nginx/.huly.nginx:/etc/nginx/conf.d/default.conf
    restart: unless-stopped

  mongodb:

    image: "mongo:7-jammy"
    environment:
      - PUID=1000
      - PGID=1000
    volumes:
      - db:/data/db
    restart: unless-stopped

  minio:

    image: "minio/minio:RELEASE.2024-11-07T00-52-20Z"
    command: server /data --address ":9000" --console-address ":9001"
    volumes:
      - files:/data
    restart: unless-stopped

  elastic:

    image: "elasticsearch:7.14.2"
    command: |
      /bin/sh -c "./bin/elasticsearch-plugin list | grep -q ingest-attachment || yes | ./bin/elasticsearch-plugin install --silent ingest-attachment;
      /usr/local/bin/docker-entrypoint.sh eswrapper"
    volumes:
      - elastic:/usr/share/elasticsearch/data
    environment:
      - ELASTICSEARCH_PORT_NUMBER=9200
      - BITNAMI_DEBUG=true
      - discovery.type=single-node
      - ES_JAVA_OPTS=-Xms1024m -Xmx1024m
      - http.cors.enabled=true
      - http.cors.allow-origin=http://localhost:8082
    healthcheck:
      interval: 20s
      retries: 10
      test: curl -s http://localhost:9200/_cluster/health | grep -vq '"status":"red"'
    restart: unless-stopped

  rekoni:

    image: hardcoreeng/rekoni-service:${HULY_VERSION}
    environment:
      - SECRET=${SECRET}
    deploy:
      resources:
        limits:
          memory: 500M
    restart: unless-stopped

  transactor:

    image: hardcoreeng/transactor:${HULY_VERSION}
    environment:
      - SERVER_PORT=3333
      - SERVER_SECRET=${SECRET}
      - SERVER_CURSOR_MAXTIMEMS=30000
      - DB_URL=mongodb://mongodb:27017
      - MONGO_URL=mongodb://mongodb:27017
      - STORAGE_CONFIG=minio|minio?accessKey=minioadmin&secretKey=minioadmin
      - FRONT_URL=http://localhost:8087
      - ACCOUNTS_URL=http://account:3000
      - FULLTEXT_URL=http://fulltext:4700
      - STATS_URL=http://stats:4900
      - LAST_NAME_FIRST=${LAST_NAME_FIRST:-true}
    restart: unless-stopped

  collaborator:

    image: hardcoreeng/collaborator:${HULY_VERSION}
    environment:
      - COLLABORATOR_PORT=3078
      - SECRET=${SECRET}
      - ACCOUNTS_URL=http://account:3000
      - DB_URL=mongodb://mongodb:27017
      - STATS_URL=http://stats:4900
      - STORAGE_CONFIG=minio|minio?accessKey=minioadmin&secretKey=minioadmin
    restart: unless-stopped

  account:

    image: hardcoreeng/account:${HULY_VERSION}
    environment:
      - SERVER_PORT=3000
      - SERVER_SECRET=${SECRET}
      - DB_URL=mongodb://mongodb:27017
      - MONGO_URL=mongodb://mongodb:27017
      - TRANSACTOR_URL=ws://transactor:3333;ws${SECURE:+s}://${HOST_ADDRESS}/_transactor
      - STORAGE_CONFIG=minio|minio?accessKey=minioadmin&secretKey=minioadmin
      - FRONT_URL=http://front:8080
      - STATS_URL=http://stats:4900
      - MODEL_ENABLED=*
      - ACCOUNTS_URL=http://localhost:3000
      - ACCOUNT_PORT=3000
    restart: unless-stopped

  workspace:

    image: hardcoreeng/workspace:${HULY_VERSION}
    environment:
      - SERVER_SECRET=${SECRET}
      - DB_URL=mongodb://mongodb:27017
      - MONGO_URL=mongodb://mongodb:27017
      - TRANSACTOR_URL=ws://transactor:3333;ws${SECURE:+s}://${HOST_ADDRESS}/_transactor
      - STORAGE_CONFIG=minio|minio?accessKey=minioadmin&secretKey=minioadmin
      - MODEL_ENABLED=*
      - ACCOUNTS_URL=http://account:3000
      - STATS_URL=http://stats:4900
    restart: unless-stopped

  front:

    image: hardcoreeng/front:${HULY_VERSION}
    environment:
      - SERVER_PORT=8080
      - SERVER_SECRET=${SECRET}
      - LOVE_ENDPOINT=http${SECURE:+s}://${HOST_ADDRESS}/_love
      - ACCOUNTS_URL=http${SECURE:+s}://${HOST_ADDRESS}/_accounts
      - REKONI_URL=http${SECURE:+s}://${HOST_ADDRESS}/_rekoni
      - CALENDAR_URL=http${SECURE:+s}://${HOST_ADDRESS}/_calendar
      - GMAIL_URL=http${SECURE:+s}://${HOST_ADDRESS}/_gmail
      - TELEGRAM_URL=http${SECURE:+s}://${HOST_ADDRESS}/_telegram
      - STATS_URL=http${SECURE:+s}://${HOST_ADDRESS}/_stats
      - UPLOAD_URL=/files
      - ELASTIC_URL=http://elastic:9200
      - COLLABORATOR_URL=ws${SECURE:+s}://${HOST_ADDRESS}/_collaborator
      - STORAGE_CONFIG=minio|minio?accessKey=minioadmin&secretKey=minioadmin
      - DB_URL=mongodb://mongodb:27017
      - MONGO_URL=mongodb://mongodb:27017
      - TITLE=${TITLE:-Huly Self Host}
      - DEFAULT_LANGUAGE=${DEFAULT_LANGUAGE:-en}
      - LAST_NAME_FIRST=${LAST_NAME_FIRST:-true}
      - DESKTOP_UPDATES_CHANNEL=selfhost
    restart: unless-stopped

  fulltext:

    image: hardcoreeng/fulltext:${HULY_VERSION}
    environment:
      - SERVER_SECRET=${SECRET}
      - DB_URL=mongodb://mongodb:27017
      - FULLTEXT_DB_URL=http://elastic:9200
      - ELASTIC_INDEX_NAME=huly_storage_index
      - STORAGE_CONFIG=minio|minio?accessKey=minioadmin&secretKey=minioadmin
      - REKONI_URL=http://rekoni:4004
      - ACCOUNTS_URL=http://account:3000
      - STATS_URL=http://stats:4900
    restart: unless-stopped

  stats:

    image: hardcoreeng/stats:${HULY_VERSION}
    environment:
      - PORT=4900
      - SERVER_SECRET=${SECRET}
    restart: unless-stopped
volumes:
  db:
  elastic:
  files:
```

```
[variables]
main_domain = "${domain}"
huly_secret = "${base64:64}"

[config]
env = [
  "HULY_VERSION=v0.6.468",
  "DOCKER_NAME=huly",
  "HOST_ADDRESS=${main_domain}",
  "SECURE=",
  "HTTP_PORT=80",
  "HTTP_BIND=",
  "TITLE=Huly",
  "DEFAULT_LANGUAGE=en",
  "LAST_NAME_FIRST=true",
  "SECRET=${huly_secret}",
]

[[config.domains]]
serviceName = "nginx"
port = 80
host = "${main_domain}"

[[config.mounts]]
filePath = "/volumes/nginx/.huly.nginx"
content = """
server {
    listen 80;
    server_name _;
    location / {
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_pass http://front:8080;
    }

    location /_accounts {
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        rewrite ^/_accounts(/.*)$ $1 break;
        proxy_pass http://account:3000/;
    }

    location /_collaborator {
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        rewrite ^/_collaborator(/.*)$ $1 break;
        proxy_pass http://collaborator:3078/;
    }

    location /_transactor {
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        rewrite ^/_transactor(/.*)$ $1 break;
        proxy_pass http://transactor:3333/;
    }

    location ~ ^/eyJ {
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_pass http://transactor:3333;
    }

    location /_rekoni {
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        rewrite ^/_rekoni(/.*)$ $1 break;
        proxy_pass http://rekoni:4004/;
    }

    location /_stats {
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        rewrite ^/_stats(/.*)$ $1 break;
        proxy_pass http://stats:4900/;
    }
}
"""
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogIm5hbWU6ICR7RE9DS0VSX05BTUV9XG52ZXJzaW9uOiBcIjNcIlxuc2VydmljZXM6XG4gIG5naW54OlxuXG4gICAgaW1hZ2U6IFwibmdpbng6MS4yMS4zXCJcbiAgICBwb3J0czpcbiAgICAgIC0gODBcbiAgICB2b2x1bWVzOlxuICAgICAgLSAuLi9maWxlcy92b2x1bWVzL25naW54Ly5odWx5Lm5naW54Oi9ldGMvbmdpbngvY29uZi5kL2RlZmF1bHQuY29uZlxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG5cbiAgbW9uZ29kYjpcblxuICAgIGltYWdlOiBcIm1vbmdvOjctamFtbXlcIlxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBQVUlEPTEwMDBcbiAgICAgIC0gUEdJRD0xMDAwXG4gICAgdm9sdW1lczpcbiAgICAgIC0gZGI6L2RhdGEvZGJcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuXG4gIG1pbmlvOlxuXG4gICAgaW1hZ2U6IFwibWluaW8vbWluaW86UkVMRUFTRS4yMDI0LTExLTA3VDAwLTUyLTIwWlwiXG4gICAgY29tbWFuZDogc2VydmVyIC9kYXRhIC0tYWRkcmVzcyBcIjo5MDAwXCIgLS1jb25zb2xlLWFkZHJlc3MgXCI6OTAwMVwiXG4gICAgdm9sdW1lczpcbiAgICAgIC0gZmlsZXM6L2RhdGFcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuXG4gIGVsYXN0aWM6XG5cbiAgICBpbWFnZTogXCJlbGFzdGljc2VhcmNoOjcuMTQuMlwiXG4gICAgY29tbWFuZDogfFxuICAgICAgL2Jpbi9zaCAtYyBcIi4vYmluL2VsYXN0aWNzZWFyY2gtcGx1Z2luIGxpc3QgfCBncmVwIC1xIGluZ2VzdC1hdHRhY2htZW50IHx8IHllcyB8IC4vYmluL2VsYXN0aWNzZWFyY2gtcGx1Z2luIGluc3RhbGwgLS1zaWxlbnQgaW5nZXN0LWF0dGFjaG1lbnQ7XG4gICAgICAvdXNyL2xvY2FsL2Jpbi9kb2NrZXItZW50cnlwb2ludC5zaCBlc3dyYXBwZXJcIlxuICAgIHZvbHVtZXM6XG4gICAgICAtIGVsYXN0aWM6L3Vzci9zaGFyZS9lbGFzdGljc2VhcmNoL2RhdGFcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gRUxBU1RJQ1NFQVJDSF9QT1JUX05VTUJFUj05MjAwXG4gICAgICAtIEJJVE5BTUlfREVCVUc9dHJ1ZVxuICAgICAgLSBkaXNjb3ZlcnkudHlwZT1zaW5nbGUtbm9kZVxuICAgICAgLSBFU19KQVZBX09QVFM9LVhtczEwMjRtIC1YbXgxMDI0bVxuICAgICAgLSBodHRwLmNvcnMuZW5hYmxlZD10cnVlXG4gICAgICAtIGh0dHAuY29ycy5hbGxvdy1vcmlnaW49aHR0cDovL2xvY2FsaG9zdDo4MDgyXG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICBpbnRlcnZhbDogMjBzXG4gICAgICByZXRyaWVzOiAxMFxuICAgICAgdGVzdDogY3VybCAtcyBodHRwOi8vbG9jYWxob3N0OjkyMDAvX2NsdXN0ZXIvaGVhbHRoIHwgZ3JlcCAtdnEgJ1wic3RhdHVzXCI6XCJyZWRcIidcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuXG4gIHJla29uaTpcblxuICAgIGltYWdlOiBoYXJkY29yZWVuZy9yZWtvbmktc2VydmljZToke0hVTFlfVkVSU0lPTn1cbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gU0VDUkVUPSR7U0VDUkVUfVxuICAgIGRlcGxveTpcbiAgICAgIHJlc291cmNlczpcbiAgICAgICAgbGltaXRzOlxuICAgICAgICAgIG1lbW9yeTogNTAwTVxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG5cbiAgdHJhbnNhY3RvcjpcblxuICAgIGltYWdlOiBoYXJkY29yZWVuZy90cmFuc2FjdG9yOiR7SFVMWV9WRVJTSU9OfVxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBTRVJWRVJfUE9SVD0zMzMzXG4gICAgICAtIFNFUlZFUl9TRUNSRVQ9JHtTRUNSRVR9XG4gICAgICAtIFNFUlZFUl9DVVJTT1JfTUFYVElNRU1TPTMwMDAwXG4gICAgICAtIERCX1VSTD1tb25nb2RiOi8vbW9uZ29kYjoyNzAxN1xuICAgICAgLSBNT05HT19VUkw9bW9uZ29kYjovL21vbmdvZGI6MjcwMTdcbiAgICAgIC0gU1RPUkFHRV9DT05GSUc9bWluaW98bWluaW8/YWNjZXNzS2V5PW1pbmlvYWRtaW4mc2VjcmV0S2V5PW1pbmlvYWRtaW5cbiAgICAgIC0gRlJPTlRfVVJMPWh0dHA6Ly9sb2NhbGhvc3Q6ODA4N1xuICAgICAgLSBBQ0NPVU5UU19VUkw9aHR0cDovL2FjY291bnQ6MzAwMFxuICAgICAgLSBGVUxMVEVYVF9VUkw9aHR0cDovL2Z1bGx0ZXh0OjQ3MDBcbiAgICAgIC0gU1RBVFNfVVJMPWh0dHA6Ly9zdGF0czo0OTAwXG4gICAgICAtIExBU1RfTkFNRV9GSVJTVD0ke0xBU1RfTkFNRV9GSVJTVDotdHJ1ZX1cbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuXG4gIGNvbGxhYm9yYXRvcjpcblxuICAgIGltYWdlOiBoYXJkY29yZWVuZy9jb2xsYWJvcmF0b3I6JHtIVUxZX1ZFUlNJT059XG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIENPTExBQk9SQVRPUl9QT1JUPTMwNzhcbiAgICAgIC0gU0VDUkVUPSR7U0VDUkVUfVxuICAgICAgLSBBQ0NPVU5UU19VUkw9aHR0cDovL2FjY291bnQ6MzAwMFxuICAgICAgLSBEQl9VUkw9bW9uZ29kYjovL21vbmdvZGI6MjcwMTdcbiAgICAgIC0gU1RBVFNfVVJMPWh0dHA6Ly9zdGF0czo0OTAwXG4gICAgICAtIFNUT1JBR0VfQ09ORklHPW1pbmlvfG1pbmlvP2FjY2Vzc0tleT1taW5pb2FkbWluJnNlY3JldEtleT1taW5pb2FkbWluXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcblxuICBhY2NvdW50OlxuXG4gICAgaW1hZ2U6IGhhcmRjb3JlZW5nL2FjY291bnQ6JHtIVUxZX1ZFUlNJT059XG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIFNFUlZFUl9QT1JUPTMwMDBcbiAgICAgIC0gU0VSVkVSX1NFQ1JFVD0ke1NFQ1JFVH1cbiAgICAgIC0gREJfVVJMPW1vbmdvZGI6Ly9tb25nb2RiOjI3MDE3XG4gICAgICAtIE1PTkdPX1VSTD1tb25nb2RiOi8vbW9uZ29kYjoyNzAxN1xuICAgICAgLSBUUkFOU0FDVE9SX1VSTD13czovL3RyYW5zYWN0b3I6MzMzMzt3cyR7U0VDVVJFOitzfTovLyR7SE9TVF9BRERSRVNTfS9fdHJhbnNhY3RvclxuICAgICAgLSBTVE9SQUdFX0NPTkZJRz1taW5pb3xtaW5pbz9hY2Nlc3NLZXk9bWluaW9hZG1pbiZzZWNyZXRLZXk9bWluaW9hZG1pblxuICAgICAgLSBGUk9OVF9VUkw9aHR0cDovL2Zyb250OjgwODBcbiAgICAgIC0gU1RBVFNfVVJMPWh0dHA6Ly9zdGF0czo0OTAwXG4gICAgICAtIE1PREVMX0VOQUJMRUQ9KlxuICAgICAgLSBBQ0NPVU5UU19VUkw9aHR0cDovL2xvY2FsaG9zdDozMDAwXG4gICAgICAtIEFDQ09VTlRfUE9SVD0zMDAwXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcblxuICB3b3Jrc3BhY2U6XG5cbiAgICBpbWFnZTogaGFyZGNvcmVlbmcvd29ya3NwYWNlOiR7SFVMWV9WRVJTSU9OfVxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBTRVJWRVJfU0VDUkVUPSR7U0VDUkVUfVxuICAgICAgLSBEQl9VUkw9bW9uZ29kYjovL21vbmdvZGI6MjcwMTdcbiAgICAgIC0gTU9OR09fVVJMPW1vbmdvZGI6Ly9tb25nb2RiOjI3MDE3XG4gICAgICAtIFRSQU5TQUNUT1JfVVJMPXdzOi8vdHJhbnNhY3RvcjozMzMzO3dzJHtTRUNVUkU6K3N9Oi8vJHtIT1NUX0FERFJFU1N9L190cmFuc2FjdG9yXG4gICAgICAtIFNUT1JBR0VfQ09ORklHPW1pbmlvfG1pbmlvP2FjY2Vzc0tleT1taW5pb2FkbWluJnNlY3JldEtleT1taW5pb2FkbWluXG4gICAgICAtIE1PREVMX0VOQUJMRUQ9KlxuICAgICAgLSBBQ0NPVU5UU19VUkw9aHR0cDovL2FjY291bnQ6MzAwMFxuICAgICAgLSBTVEFUU19VUkw9aHR0cDovL3N0YXRzOjQ5MDBcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuXG4gIGZyb250OlxuXG4gICAgaW1hZ2U6IGhhcmRjb3JlZW5nL2Zyb250OiR7SFVMWV9WRVJTSU9OfVxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBTRVJWRVJfUE9SVD04MDgwXG4gICAgICAtIFNFUlZFUl9TRUNSRVQ9JHtTRUNSRVR9XG4gICAgICAtIExPVkVfRU5EUE9JTlQ9aHR0cCR7U0VDVVJFOitzfTovLyR7SE9TVF9BRERSRVNTfS9fbG92ZVxuICAgICAgLSBBQ0NPVU5UU19VUkw9aHR0cCR7U0VDVVJFOitzfTovLyR7SE9TVF9BRERSRVNTfS9fYWNjb3VudHNcbiAgICAgIC0gUkVLT05JX1VSTD1odHRwJHtTRUNVUkU6K3N9Oi8vJHtIT1NUX0FERFJFU1N9L19yZWtvbmlcbiAgICAgIC0gQ0FMRU5EQVJfVVJMPWh0dHAke1NFQ1VSRTorc306Ly8ke0hPU1RfQUREUkVTU30vX2NhbGVuZGFyXG4gICAgICAtIEdNQUlMX1VSTD1odHRwJHtTRUNVUkU6K3N9Oi8vJHtIT1NUX0FERFJFU1N9L19nbWFpbFxuICAgICAgLSBURUxFR1JBTV9VUkw9aHR0cCR7U0VDVVJFOitzfTovLyR7SE9TVF9BRERSRVNTfS9fdGVsZWdyYW1cbiAgICAgIC0gU1RBVFNfVVJMPWh0dHAke1NFQ1VSRTorc306Ly8ke0hPU1RfQUREUkVTU30vX3N0YXRzXG4gICAgICAtIFVQTE9BRF9VUkw9L2ZpbGVzXG4gICAgICAtIEVMQVNUSUNfVVJMPWh0dHA6Ly9lbGFzdGljOjkyMDBcbiAgICAgIC0gQ09MTEFCT1JBVE9SX1VSTD13cyR7U0VDVVJFOitzfTovLyR7SE9TVF9BRERSRVNTfS9fY29sbGFib3JhdG9yXG4gICAgICAtIFNUT1JBR0VfQ09ORklHPW1pbmlvfG1pbmlvP2FjY2Vzc0tleT1taW5pb2FkbWluJnNlY3JldEtleT1taW5pb2FkbWluXG4gICAgICAtIERCX1VSTD1tb25nb2RiOi8vbW9uZ29kYjoyNzAxN1xuICAgICAgLSBNT05HT19VUkw9bW9uZ29kYjovL21vbmdvZGI6MjcwMTdcbiAgICAgIC0gVElUTEU9JHtUSVRMRTotSHVseSBTZWxmIEhvc3R9XG4gICAgICAtIERFRkFVTFRfTEFOR1VBR0U9JHtERUZBVUxUX0xBTkdVQUdFOi1lbn1cbiAgICAgIC0gTEFTVF9OQU1FX0ZJUlNUPSR7TEFTVF9OQU1FX0ZJUlNUOi10cnVlfVxuICAgICAgLSBERVNLVE9QX1VQREFURVNfQ0hBTk5FTD1zZWxmaG9zdFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG5cbiAgZnVsbHRleHQ6XG5cbiAgICBpbWFnZTogaGFyZGNvcmVlbmcvZnVsbHRleHQ6JHtIVUxZX1ZFUlNJT059XG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIFNFUlZFUl9TRUNSRVQ9JHtTRUNSRVR9XG4gICAgICAtIERCX1VSTD1tb25nb2RiOi8vbW9uZ29kYjoyNzAxN1xuICAgICAgLSBGVUxMVEVYVF9EQl9VUkw9aHR0cDovL2VsYXN0aWM6OTIwMFxuICAgICAgLSBFTEFTVElDX0lOREVYX05BTUU9aHVseV9zdG9yYWdlX2luZGV4XG4gICAgICAtIFNUT1JBR0VfQ09ORklHPW1pbmlvfG1pbmlvP2FjY2Vzc0tleT1taW5pb2FkbWluJnNlY3JldEtleT1taW5pb2FkbWluXG4gICAgICAtIFJFS09OSV9VUkw9aHR0cDovL3Jla29uaTo0MDA0XG4gICAgICAtIEFDQ09VTlRTX1VSTD1odHRwOi8vYWNjb3VudDozMDAwXG4gICAgICAtIFNUQVRTX1VSTD1odHRwOi8vc3RhdHM6NDkwMFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG5cbiAgc3RhdHM6XG5cbiAgICBpbWFnZTogaGFyZGNvcmVlbmcvc3RhdHM6JHtIVUxZX1ZFUlNJT059XG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIFBPUlQ9NDkwMFxuICAgICAgLSBTRVJWRVJfU0VDUkVUPSR7U0VDUkVUfVxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG52b2x1bWVzOlxuICBkYjpcbiAgZWxhc3RpYzpcbiAgZmlsZXM6XG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuaHVseV9zZWNyZXQgPSBcIiR7YmFzZTY0OjY0fVwiXG5cbltjb25maWddXG5lbnYgPSBbXG4gIFwiSFVMWV9WRVJTSU9OPXYwLjYuNDY4XCIsXG4gIFwiRE9DS0VSX05BTUU9aHVseVwiLFxuICBcIkhPU1RfQUREUkVTUz0ke21haW5fZG9tYWlufVwiLFxuICBcIlNFQ1VSRT1cIixcbiAgXCJIVFRQX1BPUlQ9ODBcIixcbiAgXCJIVFRQX0JJTkQ9XCIsXG4gIFwiVElUTEU9SHVseVwiLFxuICBcIkRFRkFVTFRfTEFOR1VBR0U9ZW5cIixcbiAgXCJMQVNUX05BTUVfRklSU1Q9dHJ1ZVwiLFxuICBcIlNFQ1JFVD0ke2h1bHlfc2VjcmV0fVwiLFxuXVxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJuZ2lueFwiXG5wb3J0ID0gODBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW1tjb25maWcubW91bnRzXV1cbmZpbGVQYXRoID0gXCIvdm9sdW1lcy9uZ2lueC8uaHVseS5uZ2lueFwiXG5jb250ZW50ID0gXCJcIlwiXG5zZXJ2ZXIge1xuICAgIGxpc3RlbiA4MDtcbiAgICBzZXJ2ZXJfbmFtZSBfO1xuICAgIGxvY2F0aW9uIC8ge1xuICAgICAgICBwcm94eV9zZXRfaGVhZGVyIEhvc3QgJGhvc3Q7XG4gICAgICAgIHByb3h5X3NldF9oZWFkZXIgWC1SZWFsLUlQICRyZW1vdGVfYWRkcjtcbiAgICAgICAgcHJveHlfc2V0X2hlYWRlciBYLUZvcndhcmRlZC1Gb3IgJHByb3h5X2FkZF94X2ZvcndhcmRlZF9mb3I7XG4gICAgICAgIHByb3h5X3NldF9oZWFkZXIgWC1Gb3J3YXJkZWQtUHJvdG8gJHNjaGVtZTtcbiAgICAgICAgcHJveHlfcGFzcyBodHRwOi8vZnJvbnQ6ODA4MDtcbiAgICB9XG5cbiAgICBsb2NhdGlvbiAvX2FjY291bnRzIHtcbiAgICAgICAgcHJveHlfc2V0X2hlYWRlciBIb3N0ICRob3N0O1xuICAgICAgICBwcm94eV9zZXRfaGVhZGVyIFgtUmVhbC1JUCAkcmVtb3RlX2FkZHI7XG4gICAgICAgIHByb3h5X3NldF9oZWFkZXIgWC1Gb3J3YXJkZWQtRm9yICRwcm94eV9hZGRfeF9mb3J3YXJkZWRfZm9yO1xuICAgICAgICBwcm94eV9zZXRfaGVhZGVyIFgtRm9yd2FyZGVkLVByb3RvICRzY2hlbWU7XG5cbiAgICAgICAgcmV3cml0ZSBeL19hY2NvdW50cygvLiopJCAkMSBicmVhaztcbiAgICAgICAgcHJveHlfcGFzcyBodHRwOi8vYWNjb3VudDozMDAwLztcbiAgICB9XG5cbiAgICBsb2NhdGlvbiAvX2NvbGxhYm9yYXRvciB7XG4gICAgICAgIHByb3h5X3NldF9oZWFkZXIgSG9zdCAkaG9zdDtcbiAgICAgICAgcHJveHlfc2V0X2hlYWRlciBYLVJlYWwtSVAgJHJlbW90ZV9hZGRyO1xuICAgICAgICBwcm94eV9zZXRfaGVhZGVyIFgtRm9yd2FyZGVkLUZvciAkcHJveHlfYWRkX3hfZm9yd2FyZGVkX2ZvcjtcbiAgICAgICAgcHJveHlfc2V0X2hlYWRlciBYLUZvcndhcmRlZC1Qcm90byAkc2NoZW1lO1xuXG4gICAgICAgIHByb3h5X2h0dHBfdmVyc2lvbiAxLjE7XG4gICAgICAgIHByb3h5X3NldF9oZWFkZXIgVXBncmFkZSAkaHR0cF91cGdyYWRlO1xuICAgICAgICBwcm94eV9zZXRfaGVhZGVyIENvbm5lY3Rpb24gXCJ1cGdyYWRlXCI7XG4gICAgICAgIHJld3JpdGUgXi9fY29sbGFib3JhdG9yKC8uKikkICQxIGJyZWFrO1xuICAgICAgICBwcm94eV9wYXNzIGh0dHA6Ly9jb2xsYWJvcmF0b3I6MzA3OC87XG4gICAgfVxuXG4gICAgbG9jYXRpb24gL190cmFuc2FjdG9yIHtcbiAgICAgICAgcHJveHlfc2V0X2hlYWRlciBIb3N0ICRob3N0O1xuICAgICAgICBwcm94eV9zZXRfaGVhZGVyIFgtUmVhbC1JUCAkcmVtb3RlX2FkZHI7XG4gICAgICAgIHByb3h5X3NldF9oZWFkZXIgWC1Gb3J3YXJkZWQtRm9yICRwcm94eV9hZGRfeF9mb3J3YXJkZWRfZm9yO1xuICAgICAgICBwcm94eV9zZXRfaGVhZGVyIFgtRm9yd2FyZGVkLVByb3RvICRzY2hlbWU7XG4gICAgICAgIFxuICAgICAgICBwcm94eV9odHRwX3ZlcnNpb24gMS4xO1xuICAgICAgICBwcm94eV9zZXRfaGVhZGVyIFVwZ3JhZGUgJGh0dHBfdXBncmFkZTtcbiAgICAgICAgcHJveHlfc2V0X2hlYWRlciBDb25uZWN0aW9uIFwidXBncmFkZVwiO1xuICAgICAgICByZXdyaXRlIF4vX3RyYW5zYWN0b3IoLy4qKSQgJDEgYnJlYWs7XG4gICAgICAgIHByb3h5X3Bhc3MgaHR0cDovL3RyYW5zYWN0b3I6MzMzMy87XG4gICAgfVxuXG4gICAgbG9jYXRpb24gfiBeL2V5SiB7XG4gICAgICAgIHByb3h5X3NldF9oZWFkZXIgSG9zdCAkaG9zdDtcbiAgICAgICAgcHJveHlfc2V0X2hlYWRlciBYLVJlYWwtSVAgJHJlbW90ZV9hZGRyO1xuICAgICAgICBwcm94eV9zZXRfaGVhZGVyIFgtRm9yd2FyZGVkLUZvciAkcHJveHlfYWRkX3hfZm9yd2FyZGVkX2ZvcjtcbiAgICAgICAgcHJveHlfc2V0X2hlYWRlciBYLUZvcndhcmRlZC1Qcm90byAkc2NoZW1lO1xuICAgICAgICBcbiAgICAgICAgcHJveHlfaHR0cF92ZXJzaW9uIDEuMTtcbiAgICAgICAgcHJveHlfc2V0X2hlYWRlciBVcGdyYWRlICRodHRwX3VwZ3JhZGU7XG4gICAgICAgIHByb3h5X3NldF9oZWFkZXIgQ29ubmVjdGlvbiBcInVwZ3JhZGVcIjtcbiAgICAgICAgcHJveHlfcGFzcyBodHRwOi8vdHJhbnNhY3RvcjozMzMzO1xuICAgIH1cblxuICAgIGxvY2F0aW9uIC9fcmVrb25pIHtcbiAgICAgICAgcHJveHlfc2V0X2hlYWRlciBIb3N0ICRob3N0O1xuICAgICAgICBwcm94eV9zZXRfaGVhZGVyIFgtUmVhbC1JUCAkcmVtb3RlX2FkZHI7XG4gICAgICAgIHByb3h5X3NldF9oZWFkZXIgWC1Gb3J3YXJkZWQtRm9yICRwcm94eV9hZGRfeF9mb3J3YXJkZWRfZm9yO1xuICAgICAgICBwcm94eV9zZXRfaGVhZGVyIFgtRm9yd2FyZGVkLVByb3RvICRzY2hlbWU7XG5cbiAgICAgICAgcmV3cml0ZSBeL19yZWtvbmkoLy4qKSQgJDEgYnJlYWs7XG4gICAgICAgIHByb3h5X3Bhc3MgaHR0cDovL3Jla29uaTo0MDA0LztcbiAgICB9XG5cbiAgICBsb2NhdGlvbiAvX3N0YXRzIHtcbiAgICAgICAgcHJveHlfc2V0X2hlYWRlciBIb3N0ICRob3N0O1xuICAgICAgICBwcm94eV9zZXRfaGVhZGVyIFgtUmVhbC1JUCAkcmVtb3RlX2FkZHI7XG4gICAgICAgIHByb3h5X3NldF9oZWFkZXIgWC1Gb3J3YXJkZWQtRm9yICRwcm94eV9hZGRfeF9mb3J3YXJkZWRfZm9yO1xuICAgICAgICBwcm94eV9zZXRfaGVhZGVyIFgtRm9yd2FyZGVkLVByb3RvICRzY2hlbWU7XG5cbiAgICAgICAgcmV3cml0ZSBeL19zdGF0cygvLiopJCAkMSBicmVhaztcbiAgICAgICAgcHJveHlfcGFzcyBodHRwOi8vc3RhdHM6NDkwMC87XG4gICAgfVxufSBcblwiXCJcIlxuIgp9
```

## Links

`project-management`,`community`,`discussion`

---

Version:`0.6.377`

HortusFoxHortusFox is an open source task and photo management app, designed for photographers and creatives to manage projects, tasks, and images effectively.

i18n Blog (Kuno)Kuno is an internationalized blogging platform with a backend built in Go and a frontend in Next.js.

### On this page

ConfigurationBase64LinksTags