---
title: "Stalwart | Dokploy"
source: "https://docs.dokploy.com/docs/templates/stalwart"
category: dokploy-docs
created: "2026-06-25T17:21:59.115Z"
---

Stalwart | Dokploy

# Stalwart

Copy as Markdown

Stalwart Mail Server is an open-source mail server solution with JMAP, IMAP4, POP3, and SMTP support and a wide range of modern features. It is written in Rust and designed to be secure, fast, robust and scalable.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  stalwart-mail:
    image: stalwartlabs/stalwart:latest-alpine # for production choose specific version from https://hub.docker.com/r/stalwartlabs/stalwart/tags
    ports:
      - "443"    # HTTPS
      - "8080"   # HTTP API
      - "25"     # SMTP
      - "587"    # Submission
      - "465"    # SMTPS
      - "143"    # IMAP
      - "993"    # IMAPS
      - "4190"   # ManageSieve
      - "110"    # POP3
      - "995"    # POP3S
    volumes:
      - stalwart_data:/opt/stalwart-mail
    restart: unless-stopped

volumes:
  stalwart_data:
```

```
[variables]
main_domain = "${domain}"

[config]
[[config.domains]]
serviceName = "stalwart-mail"
port = 8_080
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBzdGFsd2FydC1tYWlsOlxuICAgIGltYWdlOiBzdGFsd2FydGxhYnMvc3RhbHdhcnQ6bGF0ZXN0LWFscGluZSAjIGZvciBwcm9kdWN0aW9uIGNob29zZSBzcGVjaWZpYyB2ZXJzaW9uIGZyb20gaHR0cHM6Ly9odWIuZG9ja2VyLmNvbS9yL3N0YWx3YXJ0bGFicy9zdGFsd2FydC90YWdzXG4gICAgcG9ydHM6XG4gICAgICAtIFwiNDQzXCIgICAgIyBIVFRQU1xuICAgICAgLSBcIjgwODBcIiAgICMgSFRUUCBBUElcbiAgICAgIC0gXCIyNVwiICAgICAjIFNNVFBcbiAgICAgIC0gXCI1ODdcIiAgICAjIFN1Ym1pc3Npb25cbiAgICAgIC0gXCI0NjVcIiAgICAjIFNNVFBTXG4gICAgICAtIFwiMTQzXCIgICAgIyBJTUFQXG4gICAgICAtIFwiOTkzXCIgICAgIyBJTUFQU1xuICAgICAgLSBcIjQxOTBcIiAgICMgTWFuYWdlU2lldmVcbiAgICAgIC0gXCIxMTBcIiAgICAjIFBPUDNcbiAgICAgIC0gXCI5OTVcIiAgICAjIFBPUDNTXG4gICAgdm9sdW1lczpcbiAgICAgIC0gc3RhbHdhcnRfZGF0YTovb3B0L3N0YWx3YXJ0LW1haWxcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuXG52b2x1bWVzOlxuICBzdGFsd2FydF9kYXRhOiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJzdGFsd2FydC1tYWlsXCJcbnBvcnQgPSA4XzA4MFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIiIKfQ==
```

## Links

`email`,`smtp`,`jmap`,`imap4`,`pop3`,`self-hosted`,`mail-server`

---

Version:`latest`

Stack AuthOpen-source Auth0/Clerk alternative. Stack Auth is a free and open source authentication tool that allows you to authenticate your users.

Statping-NGStatping-NG is an easy-to-use status page for monitoring websites and applications with beautiful metrics, analytics, and health checks.

### On this page

ConfigurationBase64LinksTags