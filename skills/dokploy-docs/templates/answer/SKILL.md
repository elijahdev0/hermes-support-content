---
title: "Answer | Dokploy"
source: "https://docs.dokploy.com/docs/templates/answer"
category: dokploy-docs
created: "2026-06-25T17:21:40.415Z"
---

Answer | Dokploy

# Answer

Copy as Markdown

Answer is an open-source Q&A platform for building a self-hosted question-and-answer service.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  answer:
    image: apache/answer:1.4.1
    ports:
      - '80'
    restart: on-failure
    volumes:
      - answer-data:/data
    depends_on:
      db:
        condition: service_healthy
  db:
    image: postgres:16
    restart: always
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U $${POSTGRES_USER} -d $${POSTGRES_DB}"]
      interval: 5s
      timeout: 5s
      retries: 5

    volumes:
      - db-data:/var/lib/postgresql/data
    environment:
      POSTGRES_DB: answer
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres

volumes:
  answer-data:
  db-data:
```

```
[variables]
main_domain = "${domain}"
service_hash = "${hash:32}"

[config]
env = ["ANSWER_HOST=http://${main_domain}", "SERVICE_HASH=${service_hash}"]
mounts = []

[[config.domains]]
serviceName = "answer"
port = 9_080
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBhbnN3ZXI6XG4gICAgaW1hZ2U6IGFwYWNoZS9hbnN3ZXI6MS40LjFcbiAgICBwb3J0czpcbiAgICAgIC0gJzgwJ1xuICAgIHJlc3RhcnQ6IG9uLWZhaWx1cmVcbiAgICB2b2x1bWVzOlxuICAgICAgLSBhbnN3ZXItZGF0YTovZGF0YVxuICAgIGRlcGVuZHNfb246XG4gICAgICBkYjpcbiAgICAgICAgY29uZGl0aW9uOiBzZXJ2aWNlX2hlYWx0aHlcbiAgZGI6XG4gICAgaW1hZ2U6IHBvc3RncmVzOjE2XG4gICAgcmVzdGFydDogYWx3YXlzXG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OiBbXCJDTUQtU0hFTExcIiwgXCJwZ19pc3JlYWR5IC1VICQke1BPU1RHUkVTX1VTRVJ9IC1kICQke1BPU1RHUkVTX0RCfVwiXVxuICAgICAgaW50ZXJ2YWw6IDVzXG4gICAgICB0aW1lb3V0OiA1c1xuICAgICAgcmV0cmllczogNVxuXG4gICAgdm9sdW1lczpcbiAgICAgIC0gZGItZGF0YTovdmFyL2xpYi9wb3N0Z3Jlc3FsL2RhdGFcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIFBPU1RHUkVTX0RCOiBhbnN3ZXJcbiAgICAgIFBPU1RHUkVTX1VTRVI6IHBvc3RncmVzXG4gICAgICBQT1NUR1JFU19QQVNTV09SRDogcG9zdGdyZXNcblxudm9sdW1lczpcbiAgYW5zd2VyLWRhdGE6XG4gIGRiLWRhdGE6XG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuc2VydmljZV9oYXNoID0gXCIke2hhc2g6MzJ9XCJcblxuW2NvbmZpZ11cbmVudiA9IFtcIkFOU1dFUl9IT1NUPWh0dHA6Ly8ke21haW5fZG9tYWlufVwiLCBcIlNFUlZJQ0VfSEFTSD0ke3NlcnZpY2VfaGFzaH1cIl1cbm1vdW50cyA9IFtdXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImFuc3dlclwiXG5wb3J0ID0gOV8wODBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcbiIKfQ==
```

## Links

`q&a`,`self-hosted`

---

Version:`v1.4.1`

AnseAnse is an open-source alternative to ChatGPT web UI, supporting OpenAI-compatible APIs.

AnubisAnubis is a bot protector, It will block bots from accessing your website.

### On this page

ConfigurationBase64LinksTags