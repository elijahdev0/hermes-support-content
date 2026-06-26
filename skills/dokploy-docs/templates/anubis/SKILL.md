---
title: "Anubis | Dokploy"
source: "https://docs.dokploy.com/docs/templates/anubis"
category: dokploy-docs
created: "2026-06-25T17:21:40.415Z"
---

Anubis | Dokploy

# Anubis

Copy as Markdown

Anubis is a bot protector, It will block bots from accessing your website.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  anubis:
    image: ghcr.io/techarohq/anubis:latest
    restart: unless-stopped
    ports:
      - "8923" # Anubis default port
    environment:
      # Required: Point to your frontend service locally
      # Example: http://mydocker-wyeud:8080
      - TARGET=${TARGET}

      # Bind address
      - BIND=:8923

      # Cookie domain (set to your domain)
      - COOKIE_DOMAIN=${COOKIE_DOMAIN}

      # Challenge difficulty (1-20, default is 5)
      # Lower = easier for users, Higher = harder for bots
      - DIFFICULTY=${DIFFICULTY}

      # OpenGraph passthrough (allows social media previews to work)
      - OG_PASSTHROUGH=${OG_PASSTHROUGH}
      - OG_EXPIRY_TIME=${OG_EXPIRY_TIME}
      - OG_CACHE_CONSIDER_HOST=${OG_CACHE_CONSIDER_HOST}

      # Optional: Serve robots.txt to discourage indexing
      - SERVE_ROBOTS_TXT=${SERVE_ROBOTS_TXT} # Set to true if you don't want search engines

# Unconmment in case you want to connect the anubis container to dokploy-network
#     networks:
#       - dokploy-network

# networks:
#   dokploy-network:
#     external: true # Using existing dokploy-network to connect to your frontend locally
```

```
[variables]
main_domain = "${domain}"

[config.env]
COOKIE_DOMAIN = "${main_domain}"
TARGET = "YOURLOCALHOST:PORT"
DIFFICULTY = "5"
OG_PASSTHROUGH = true
OG_EXPIRY_TIME = "1h"
OG_CACHE_CONSIDER_HOST = true
SERVE_ROBOTS_TXT = false
mounts = []

[[config.domains]]
serviceName = "anubis"
port = 8923
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBhbnViaXM6XG4gICAgaW1hZ2U6IGdoY3IuaW8vdGVjaGFyb2hxL2FudWJpczpsYXRlc3RcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIHBvcnRzOlxuICAgICAgLSBcIjg5MjNcIiAjIEFudWJpcyBkZWZhdWx0IHBvcnRcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgICMgUmVxdWlyZWQ6IFBvaW50IHRvIHlvdXIgZnJvbnRlbmQgc2VydmljZSBsb2NhbGx5XG4gICAgICAjIEV4YW1wbGU6IGh0dHA6Ly9teWRvY2tlci13eWV1ZDo4MDgwXG4gICAgICAtIFRBUkdFVD0ke1RBUkdFVH1cblxuICAgICAgIyBCaW5kIGFkZHJlc3NcbiAgICAgIC0gQklORD06ODkyM1xuXG4gICAgICAjIENvb2tpZSBkb21haW4gKHNldCB0byB5b3VyIGRvbWFpbilcbiAgICAgIC0gQ09PS0lFX0RPTUFJTj0ke0NPT0tJRV9ET01BSU59XG5cbiAgICAgICMgQ2hhbGxlbmdlIGRpZmZpY3VsdHkgKDEtMjAsIGRlZmF1bHQgaXMgNSlcbiAgICAgICMgTG93ZXIgPSBlYXNpZXIgZm9yIHVzZXJzLCBIaWdoZXIgPSBoYXJkZXIgZm9yIGJvdHNcbiAgICAgIC0gRElGRklDVUxUWT0ke0RJRkZJQ1VMVFl9XG5cbiAgICAgICMgT3BlbkdyYXBoIHBhc3N0aHJvdWdoIChhbGxvd3Mgc29jaWFsIG1lZGlhIHByZXZpZXdzIHRvIHdvcmspXG4gICAgICAtIE9HX1BBU1NUSFJPVUdIPSR7T0dfUEFTU1RIUk9VR0h9XG4gICAgICAtIE9HX0VYUElSWV9USU1FPSR7T0dfRVhQSVJZX1RJTUV9XG4gICAgICAtIE9HX0NBQ0hFX0NPTlNJREVSX0hPU1Q9JHtPR19DQUNIRV9DT05TSURFUl9IT1NUfVxuXG4gICAgICAjIE9wdGlvbmFsOiBTZXJ2ZSByb2JvdHMudHh0IHRvIGRpc2NvdXJhZ2UgaW5kZXhpbmdcbiAgICAgIC0gU0VSVkVfUk9CT1RTX1RYVD0ke1NFUlZFX1JPQk9UU19UWFR9ICMgU2V0IHRvIHRydWUgaWYgeW91IGRvbid0IHdhbnQgc2VhcmNoIGVuZ2luZXNcblxuXG4jIFVuY29ubW1lbnQgaW4gY2FzZSB5b3Ugd2FudCB0byBjb25uZWN0IHRoZSBhbnViaXMgY29udGFpbmVyIHRvIGRva3Bsb3ktbmV0d29ya1xuIyAgICAgbmV0d29ya3M6XG4jICAgICAgIC0gZG9rcGxveS1uZXR3b3JrXG5cbiMgbmV0d29ya3M6XG4jICAgZG9rcGxveS1uZXR3b3JrOlxuIyAgICAgZXh0ZXJuYWw6IHRydWUgIyBVc2luZyBleGlzdGluZyBkb2twbG95LW5ldHdvcmsgdG8gY29ubmVjdCB0byB5b3VyIGZyb250ZW5kIGxvY2FsbHlcbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuQ09PS0lFX0RPTUFJTiA9IFwiJHttYWluX2RvbWFpbn1cIlxuVEFSR0VUID0gXCJZT1VSTE9DQUxIT1NUOlBPUlRcIlxuRElGRklDVUxUWSA9IFwiNVwiXG5PR19QQVNTVEhST1VHSCA9IHRydWVcbk9HX0VYUElSWV9USU1FID0gXCIxaFwiXG5PR19DQUNIRV9DT05TSURFUl9IT1NUID0gdHJ1ZVxuU0VSVkVfUk9CT1RTX1RYVCA9IGZhbHNlXG5tb3VudHMgPSBbXVxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJhbnViaXNcIlxucG9ydCA9IDg5MjNcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcbiIKfQ==
```

## Links

`self-hosted`,`bot-protection`

---

Version:`latest`

AnswerAnswer is an open-source Q&A platform for building a self-hosted question-and-answer service.

AnythingLLMAnythingLLM is a private, self-hosted, and local document chatbot platform that allows you to chat with your documents using various LLM providers.

### On this page

ConfigurationBase64LinksTags