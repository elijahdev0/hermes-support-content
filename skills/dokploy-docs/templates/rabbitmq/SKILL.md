---
title: "RabbitMQ | Dokploy"
source: "https://docs.dokploy.com/docs/templates/rabbitmq"
category: dokploy-docs
created: "2026-06-25T17:21:57.937Z"
---

RabbitMQ | Dokploy

# RabbitMQ

Copy as Markdown

RabbitMQ is an open source multi-protocol messaging broker.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  rabbitmq:
    image: rabbitmq:4.1-management
    hostname: rabbitmq
    restart: unless-stopped
    environment:
      - RABBITMQ_DEFAULT_USER=${RABBITMQ_DEFAULT_USER}
      - RABBITMQ_DEFAULT_PASS=${RABBITMQ_DEFAULT_PASS}
      - RABBITMQ_SERVER_ADDITIONAL_ERL_ARGS=-rabbit log_levels [{connection,error},{default,error}] disk_free_limit ${RABBITMQ_DISK_FREE_LIMIT}
    volumes:
      - rabbitmq-data:/var/lib/rabbitmq
    ports:
      - 15672
      - 5672

volumes:
  rabbitmq-data: {}
```

```
[variables]
main_domain = "${domain}"
management_domain="${domain}"
default_user = "admin"
default_pass = "${password:8}"
disk_free_limit="2147483648"

[config]
env = [
    "RABBITMQ_DEFAULT_USER=${default_user}",
    "RABBITMQ_DEFAULT_PASS=${default_pass}",
    "RABBITMQ_DISK_FREE_LIMIT=${disk_free_limit}"
]

[[config.domains]]
serviceName = "rabbitmq"
port = 15_672
host = "${main_domain}"
path = "/"

[[config.domains]]
serviceName = "rabbitmq"
port = 5_672
host = "${management_domain}"
path = "/"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICByYWJiaXRtcTpcbiAgICBpbWFnZTogcmFiYml0bXE6NC4xLW1hbmFnZW1lbnRcbiAgICBob3N0bmFtZTogcmFiYml0bXFcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBSQUJCSVRNUV9ERUZBVUxUX1VTRVI9JHtSQUJCSVRNUV9ERUZBVUxUX1VTRVJ9XG4gICAgICAtIFJBQkJJVE1RX0RFRkFVTFRfUEFTUz0ke1JBQkJJVE1RX0RFRkFVTFRfUEFTU31cbiAgICAgIC0gUkFCQklUTVFfU0VSVkVSX0FERElUSU9OQUxfRVJMX0FSR1M9LXJhYmJpdCBsb2dfbGV2ZWxzIFt7Y29ubmVjdGlvbixlcnJvcn0se2RlZmF1bHQsZXJyb3J9XSBkaXNrX2ZyZWVfbGltaXQgJHtSQUJCSVRNUV9ESVNLX0ZSRUVfTElNSVR9XG4gICAgdm9sdW1lczpcbiAgICAgIC0gcmFiYml0bXEtZGF0YTovdmFyL2xpYi9yYWJiaXRtcVxuICAgIHBvcnRzOlxuICAgICAgLSAxNTY3MlxuICAgICAgLSA1NjcyXG5cbnZvbHVtZXM6XG4gIHJhYmJpdG1xLWRhdGE6IHt9IiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbm1hbmFnZW1lbnRfZG9tYWluPVwiJHtkb21haW59XCJcbmRlZmF1bHRfdXNlciA9IFwiYWRtaW5cIlxuZGVmYXVsdF9wYXNzID0gXCIke3Bhc3N3b3JkOjh9XCJcbmRpc2tfZnJlZV9saW1pdD1cIjIxNDc0ODM2NDhcIlxuXG5bY29uZmlnXVxuZW52ID0gW1xuICAgIFwiUkFCQklUTVFfREVGQVVMVF9VU0VSPSR7ZGVmYXVsdF91c2VyfVwiLFxuICAgIFwiUkFCQklUTVFfREVGQVVMVF9QQVNTPSR7ZGVmYXVsdF9wYXNzfVwiLFxuICAgIFwiUkFCQklUTVFfRElTS19GUkVFX0xJTUlUPSR7ZGlza19mcmVlX2xpbWl0fVwiXG5dXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcInJhYmJpdG1xXCJcbnBvcnQgPSAxNV82NzJcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcbnBhdGggPSBcIi9cIlxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJyYWJiaXRtcVwiXG5wb3J0ID0gNV82NzJcbmhvc3QgPSBcIiR7bWFuYWdlbWVudF9kb21haW59XCJcbnBhdGggPSBcIi9cIlxuIgp9
```

## Links

`message-broker`,`queue`,`rabbitmq`

---

Version:`4.1-management`

Quant-UXQuant-UX is an open-source UX design and prototyping tool that allows you to create interactive prototypes, conduct user research, and analyze user behavior.

Reactive ResumeA free and open-source resume builder that simplifies the process of creating, updating, and sharing your resume.

### On this page

ConfigurationBase64LinksTags