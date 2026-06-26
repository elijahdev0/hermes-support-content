---
title: "Libredesk | Dokploy"
source: "https://docs.dokploy.com/docs/templates/libredesk"
category: dokploy-docs
created: "2026-06-25T17:21:52.046Z"
---

Libredesk | Dokploy

# Libredesk

Copy as Markdown

Open source, self-hosted customer support desk. Single binary app.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  libredesk:
    image: libredesk/libredesk:latest
    restart: unless-stopped
    ports:
      - 9000
    environment:
      # If the password is set during first docker-compose up, the system user password will be set to this value.
      # You can always set system user password later by running `docker exec -it libredesk_app ./libredesk --set-system-user-password`.
      LIBREDESK_SYSTEM_USER_PASSWORD: ${LIBREDESK_SYSTEM_USER_PASSWORD:-}
    depends_on:
      - db
      - redis
    volumes:
      - ../files/uploads:/libredesk/uploads:rw
      - ../files/config.toml:/libredesk/config.toml
    command: [ sh, -c, "./libredesk --install --idempotent-install --yes --config /libredesk/config.toml && ./libredesk --upgrade --yes --config /libredesk/config.toml && ./libredesk --config /libredesk/config.toml" ]

  # PostgreSQL database
  db:
    image: postgres:17-alpine
    restart: unless-stopped
    ports:
      # Only bind on the local interface. To connect to Postgres externally, change this to 0.0.0.0
      - 5432
    environment:
      # Set these environment variables to configure the database, defaults to libredesk.
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: ${POSTGRES_DB}
    healthcheck:
      test: [ "CMD-SHELL", "pg_isready -U ${POSTGRES_USER:-libredesk} -d ${POSTGRES_DB:-libredesk}" ]
      interval: 10s
      timeout: 5s
      retries: 6
    volumes:
      - postgres-data:/var/lib/postgresql/data

  # Redis
  redis:
    image: redis:7-alpine
    restart: unless-stopped
    ports:
      # Only bind on the local interface.
      - 6379
    volumes:
      - redis-data:/data

volumes:
  postgres-data:
  redis-data:
```

```
[variables]
libredesk_domain = "${domain}"

libredesk_system_user_password = "${base64:32}"

pg_username = "${username}"
pg_password = "${password:16}"
pg_database = "libredesk"

[config]
env = [
    "LIBREDESK_SYSTEM_USER_PASSWORD=${libredesk_system_user_password}",
    "POSTGRES_USER=${pg_username}",
    "POSTGRES_PASSWORD=${pg_password}",
    "POSTGRES_DB=${pg_database}",
]

[[config.domains]]
serviceName = "libredesk"
port = 9000
host = "${libredesk_domain}"

[[config.mounts]]
filePath = "config.toml"
content = """

[app]
# Log level: info, debug, warn, error, fatal
log_level = "debug"
# Environment: dev, prod.
# Setting to "dev" will enable color logging in terminal.
env = "dev"
# Whether to automatically check for application updates on start up, app updates are shown as a banner in the admin panel.
check_updates = true

# HTTP server.
[app.server]
# Address to bind the HTTP server to.
address = "0.0.0.0:9000"
# Unix socket path (leave empty to use TCP address instead)
socket = ""
# Do NOT disable secure cookies in production environment if you don't know exactly what you're doing!
disable_secure_cookies = false
# Request read and write timeouts.
read_timeout = "5s"
write_timeout = "5s"
# Maximum request body size in bytes (100MB)
# If you are using proxy, you may need to configure them to allow larger request bodies.
max_body_size = 104857600
# Size of the read buffer for incoming requests
read_buffer_size = 4096
# Keepalive settings.
keepalive_timeout = "10s"

# File upload provider to use, either `fs` or `s3`.
[upload]
provider = "fs"

# Filesystem provider.
[upload.fs]
# Directory where uploaded files are stored, make sure this directory exists and is writable by the application.
upload_path = 'uploads'

# S3 provider.
[upload.s3]
# S3 endpoint URL (required only for non-AWS S3-compatible providers like MinIO).
# Leave empty to use default AWS endpoints.
url = ""

# AWS S3 credentials, keep empty to use attached IAM roles.
access_key = ""
secret_key = ""

# AWS region, e.g., "us-east-1", "eu-west-1", etc.
region = "ap-south-1"
# S3 bucket name where files will be stored.
bucket = "bucket-name"
# Optional prefix path within the S3 bucket where files will be stored.
# Example, if set to "uploads/media", files will be stored under that path.
# Useful for organizing files inside a shared bucket.
bucket_path = ""
# S3 signed URL expiry duration (e.g., "30m", "1h")
expiry = "30m"

# Postgres.
[db]
# If running locally, use `localhost`.
host = "db"
# Database port, default is 5432.
port = 5432
# Update the following values with your database credentials.
user = "${pg_username}"
password = "${pg_password}"
database = "${pg_database}"
ssl_mode = "disable"
# Maximum number of open database connections
max_open = 30
# Maximum number of idle connections in the pool
max_idle = 30
# Maximum time a connection can be reused before being closed
max_lifetime = "300s"

# Redis.
[redis]
# If running locally, use `localhost:6379`.
address = "redis:6379"
password = ""
db = 0

[message]
# Number of workers processing outgoing message queue
outgoing_queue_workers = 10
# Number of workers processing incoming message queue
incoming_queue_workers = 10
# How often to scan for outgoing messages to process, keep it low to process messages quickly.
message_outgoing_scan_interval = "50ms"
# Maximum number of messages that can be queued for incoming processing
incoming_queue_size = 5000
# Maximum number of messages that can be queued for outgoing processing
outgoing_queue_size = 5000

[notification]
# Number of concurrent notification workers
concurrency = 2
# Maximum number of notifications that can be queued
queue_size = 2000

[automation]
# Number of workers processing automation rules
worker_count = 10

[autoassigner]
# How often to run automatic conversation assignment
autoassign_interval = "5m"

[webhook]
# Number of webhook delivery workers
workers = 5
# Maximum number of webhook deliveries that can be queued
queue_size = 10000
# HTTP timeout for webhook requests
timeout = "15s"

[conversation]
# How often to check for conversations to unsnooze
unsnooze_interval = "5m"

[sla]
# How often to evaluate SLA compliance for conversations
evaluation_interval = "5m"

"""
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBsaWJyZWRlc2s6XG4gICAgaW1hZ2U6IGxpYnJlZGVzay9saWJyZWRlc2s6bGF0ZXN0XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBwb3J0czpcbiAgICAgIC0gOTAwMFxuICAgIGVudmlyb25tZW50OlxuICAgICAgIyBJZiB0aGUgcGFzc3dvcmQgaXMgc2V0IGR1cmluZyBmaXJzdCBkb2NrZXItY29tcG9zZSB1cCwgdGhlIHN5c3RlbSB1c2VyIHBhc3N3b3JkIHdpbGwgYmUgc2V0IHRvIHRoaXMgdmFsdWUuXG4gICAgICAjIFlvdSBjYW4gYWx3YXlzIHNldCBzeXN0ZW0gdXNlciBwYXNzd29yZCBsYXRlciBieSBydW5uaW5nIGBkb2NrZXIgZXhlYyAtaXQgbGlicmVkZXNrX2FwcCAuL2xpYnJlZGVzayAtLXNldC1zeXN0ZW0tdXNlci1wYXNzd29yZGAuXG4gICAgICBMSUJSRURFU0tfU1lTVEVNX1VTRVJfUEFTU1dPUkQ6ICR7TElCUkVERVNLX1NZU1RFTV9VU0VSX1BBU1NXT1JEOi19XG4gICAgZGVwZW5kc19vbjpcbiAgICAgIC0gZGJcbiAgICAgIC0gcmVkaXNcbiAgICB2b2x1bWVzOlxuICAgICAgLSAuLi9maWxlcy91cGxvYWRzOi9saWJyZWRlc2svdXBsb2Fkczpyd1xuICAgICAgLSAuLi9maWxlcy9jb25maWcudG9tbDovbGlicmVkZXNrL2NvbmZpZy50b21sXG4gICAgY29tbWFuZDogWyBzaCwgLWMsIFwiLi9saWJyZWRlc2sgLS1pbnN0YWxsIC0taWRlbXBvdGVudC1pbnN0YWxsIC0teWVzIC0tY29uZmlnIC9saWJyZWRlc2svY29uZmlnLnRvbWwgJiYgLi9saWJyZWRlc2sgLS11cGdyYWRlIC0teWVzIC0tY29uZmlnIC9saWJyZWRlc2svY29uZmlnLnRvbWwgJiYgLi9saWJyZWRlc2sgLS1jb25maWcgL2xpYnJlZGVzay9jb25maWcudG9tbFwiIF1cblxuICAjIFBvc3RncmVTUUwgZGF0YWJhc2VcbiAgZGI6XG4gICAgaW1hZ2U6IHBvc3RncmVzOjE3LWFscGluZVxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgcG9ydHM6XG4gICAgICAjIE9ubHkgYmluZCBvbiB0aGUgbG9jYWwgaW50ZXJmYWNlLiBUbyBjb25uZWN0IHRvIFBvc3RncmVzIGV4dGVybmFsbHksIGNoYW5nZSB0aGlzIHRvIDAuMC4wLjBcbiAgICAgIC0gNTQzMlxuICAgIGVudmlyb25tZW50OlxuICAgICAgIyBTZXQgdGhlc2UgZW52aXJvbm1lbnQgdmFyaWFibGVzIHRvIGNvbmZpZ3VyZSB0aGUgZGF0YWJhc2UsIGRlZmF1bHRzIHRvIGxpYnJlZGVzay5cbiAgICAgIFBPU1RHUkVTX1VTRVI6ICR7UE9TVEdSRVNfVVNFUn1cbiAgICAgIFBPU1RHUkVTX1BBU1NXT1JEOiAke1BPU1RHUkVTX1BBU1NXT1JEfVxuICAgICAgUE9TVEdSRVNfREI6ICR7UE9TVEdSRVNfREJ9XG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OiBbIFwiQ01ELVNIRUxMXCIsIFwicGdfaXNyZWFkeSAtVSAke1BPU1RHUkVTX1VTRVI6LWxpYnJlZGVza30gLWQgJHtQT1NUR1JFU19EQjotbGlicmVkZXNrfVwiIF1cbiAgICAgIGludGVydmFsOiAxMHNcbiAgICAgIHRpbWVvdXQ6IDVzXG4gICAgICByZXRyaWVzOiA2XG4gICAgdm9sdW1lczpcbiAgICAgIC0gcG9zdGdyZXMtZGF0YTovdmFyL2xpYi9wb3N0Z3Jlc3FsL2RhdGFcblxuICAjIFJlZGlzXG4gIHJlZGlzOlxuICAgIGltYWdlOiByZWRpczo3LWFscGluZVxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgcG9ydHM6XG4gICAgICAjIE9ubHkgYmluZCBvbiB0aGUgbG9jYWwgaW50ZXJmYWNlLlxuICAgICAgLSA2Mzc5XG4gICAgdm9sdW1lczpcbiAgICAgIC0gcmVkaXMtZGF0YTovZGF0YVxuXG52b2x1bWVzOlxuICBwb3N0Z3Jlcy1kYXRhOlxuICByZWRpcy1kYXRhOiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubGlicmVkZXNrX2RvbWFpbiA9IFwiJHtkb21haW59XCJcblxubGlicmVkZXNrX3N5c3RlbV91c2VyX3Bhc3N3b3JkID0gXCIke2Jhc2U2NDozMn1cIlxuXG5wZ191c2VybmFtZSA9IFwiJHt1c2VybmFtZX1cIlxucGdfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MTZ9XCJcbnBnX2RhdGFiYXNlID0gXCJsaWJyZWRlc2tcIlxuXG5bY29uZmlnXVxuZW52ID0gW1xuICAgIFwiTElCUkVERVNLX1NZU1RFTV9VU0VSX1BBU1NXT1JEPSR7bGlicmVkZXNrX3N5c3RlbV91c2VyX3Bhc3N3b3JkfVwiLFxuICAgIFwiUE9TVEdSRVNfVVNFUj0ke3BnX3VzZXJuYW1lfVwiLFxuICAgIFwiUE9TVEdSRVNfUEFTU1dPUkQ9JHtwZ19wYXNzd29yZH1cIixcbiAgICBcIlBPU1RHUkVTX0RCPSR7cGdfZGF0YWJhc2V9XCIsXG5dXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImxpYnJlZGVza1wiXG5wb3J0ID0gOTAwMFxuaG9zdCA9IFwiJHtsaWJyZWRlc2tfZG9tYWlufVwiXG5cbltbY29uZmlnLm1vdW50c11dXG5maWxlUGF0aCA9IFwiY29uZmlnLnRvbWxcIlxuY29udGVudCA9IFwiXCJcIlxuXG5bYXBwXVxuIyBMb2cgbGV2ZWw6IGluZm8sIGRlYnVnLCB3YXJuLCBlcnJvciwgZmF0YWxcbmxvZ19sZXZlbCA9IFwiZGVidWdcIlxuIyBFbnZpcm9ubWVudDogZGV2LCBwcm9kLlxuIyBTZXR0aW5nIHRvIFwiZGV2XCIgd2lsbCBlbmFibGUgY29sb3IgbG9nZ2luZyBpbiB0ZXJtaW5hbC5cbmVudiA9IFwiZGV2XCJcbiMgV2hldGhlciB0byBhdXRvbWF0aWNhbGx5IGNoZWNrIGZvciBhcHBsaWNhdGlvbiB1cGRhdGVzIG9uIHN0YXJ0IHVwLCBhcHAgdXBkYXRlcyBhcmUgc2hvd24gYXMgYSBiYW5uZXIgaW4gdGhlIGFkbWluIHBhbmVsLlxuY2hlY2tfdXBkYXRlcyA9IHRydWVcblxuIyBIVFRQIHNlcnZlci5cblthcHAuc2VydmVyXVxuIyBBZGRyZXNzIHRvIGJpbmQgdGhlIEhUVFAgc2VydmVyIHRvLlxuYWRkcmVzcyA9IFwiMC4wLjAuMDo5MDAwXCJcbiMgVW5peCBzb2NrZXQgcGF0aCAobGVhdmUgZW1wdHkgdG8gdXNlIFRDUCBhZGRyZXNzIGluc3RlYWQpXG5zb2NrZXQgPSBcIlwiXG4jIERvIE5PVCBkaXNhYmxlIHNlY3VyZSBjb29raWVzIGluIHByb2R1Y3Rpb24gZW52aXJvbm1lbnQgaWYgeW91IGRvbid0IGtub3cgZXhhY3RseSB3aGF0IHlvdSdyZSBkb2luZyFcbmRpc2FibGVfc2VjdXJlX2Nvb2tpZXMgPSBmYWxzZVxuIyBSZXF1ZXN0IHJlYWQgYW5kIHdyaXRlIHRpbWVvdXRzLlxucmVhZF90aW1lb3V0ID0gXCI1c1wiXG53cml0ZV90aW1lb3V0ID0gXCI1c1wiXG4jIE1heGltdW0gcmVxdWVzdCBib2R5IHNpemUgaW4gYnl0ZXMgKDEwME1CKVxuIyBJZiB5b3UgYXJlIHVzaW5nIHByb3h5LCB5b3UgbWF5IG5lZWQgdG8gY29uZmlndXJlIHRoZW0gdG8gYWxsb3cgbGFyZ2VyIHJlcXVlc3QgYm9kaWVzLlxubWF4X2JvZHlfc2l6ZSA9IDEwNDg1NzYwMFxuIyBTaXplIG9mIHRoZSByZWFkIGJ1ZmZlciBmb3IgaW5jb21pbmcgcmVxdWVzdHNcbnJlYWRfYnVmZmVyX3NpemUgPSA0MDk2XG4jIEtlZXBhbGl2ZSBzZXR0aW5ncy5cbmtlZXBhbGl2ZV90aW1lb3V0ID0gXCIxMHNcIlxuXG4jIEZpbGUgdXBsb2FkIHByb3ZpZGVyIHRvIHVzZSwgZWl0aGVyIGBmc2Agb3IgYHMzYC5cblt1cGxvYWRdXG5wcm92aWRlciA9IFwiZnNcIlxuXG4jIEZpbGVzeXN0ZW0gcHJvdmlkZXIuXG5bdXBsb2FkLmZzXVxuIyBEaXJlY3Rvcnkgd2hlcmUgdXBsb2FkZWQgZmlsZXMgYXJlIHN0b3JlZCwgbWFrZSBzdXJlIHRoaXMgZGlyZWN0b3J5IGV4aXN0cyBhbmQgaXMgd3JpdGFibGUgYnkgdGhlIGFwcGxpY2F0aW9uLlxudXBsb2FkX3BhdGggPSAndXBsb2FkcydcblxuIyBTMyBwcm92aWRlci5cblt1cGxvYWQuczNdXG4jIFMzIGVuZHBvaW50IFVSTCAocmVxdWlyZWQgb25seSBmb3Igbm9uLUFXUyBTMy1jb21wYXRpYmxlIHByb3ZpZGVycyBsaWtlIE1pbklPKS5cbiMgTGVhdmUgZW1wdHkgdG8gdXNlIGRlZmF1bHQgQVdTIGVuZHBvaW50cy5cbnVybCA9IFwiXCJcblxuIyBBV1MgUzMgY3JlZGVudGlhbHMsIGtlZXAgZW1wdHkgdG8gdXNlIGF0dGFjaGVkIElBTSByb2xlcy5cbmFjY2Vzc19rZXkgPSBcIlwiXG5zZWNyZXRfa2V5ID0gXCJcIlxuXG4jIEFXUyByZWdpb24sIGUuZy4sIFwidXMtZWFzdC0xXCIsIFwiZXUtd2VzdC0xXCIsIGV0Yy5cbnJlZ2lvbiA9IFwiYXAtc291dGgtMVwiXG4jIFMzIGJ1Y2tldCBuYW1lIHdoZXJlIGZpbGVzIHdpbGwgYmUgc3RvcmVkLlxuYnVja2V0ID0gXCJidWNrZXQtbmFtZVwiXG4jIE9wdGlvbmFsIHByZWZpeCBwYXRoIHdpdGhpbiB0aGUgUzMgYnVja2V0IHdoZXJlIGZpbGVzIHdpbGwgYmUgc3RvcmVkLlxuIyBFeGFtcGxlLCBpZiBzZXQgdG8gXCJ1cGxvYWRzL21lZGlhXCIsIGZpbGVzIHdpbGwgYmUgc3RvcmVkIHVuZGVyIHRoYXQgcGF0aC5cbiMgVXNlZnVsIGZvciBvcmdhbml6aW5nIGZpbGVzIGluc2lkZSBhIHNoYXJlZCBidWNrZXQuXG5idWNrZXRfcGF0aCA9IFwiXCJcbiMgUzMgc2lnbmVkIFVSTCBleHBpcnkgZHVyYXRpb24gKGUuZy4sIFwiMzBtXCIsIFwiMWhcIilcbmV4cGlyeSA9IFwiMzBtXCJcblxuIyBQb3N0Z3Jlcy5cbltkYl1cbiMgSWYgcnVubmluZyBsb2NhbGx5LCB1c2UgYGxvY2FsaG9zdGAuXG5ob3N0ID0gXCJkYlwiXG4jIERhdGFiYXNlIHBvcnQsIGRlZmF1bHQgaXMgNTQzMi5cbnBvcnQgPSA1NDMyXG4jIFVwZGF0ZSB0aGUgZm9sbG93aW5nIHZhbHVlcyB3aXRoIHlvdXIgZGF0YWJhc2UgY3JlZGVudGlhbHMuXG51c2VyID0gXCIke3BnX3VzZXJuYW1lfVwiXG5wYXNzd29yZCA9IFwiJHtwZ19wYXNzd29yZH1cIlxuZGF0YWJhc2UgPSBcIiR7cGdfZGF0YWJhc2V9XCJcbnNzbF9tb2RlID0gXCJkaXNhYmxlXCJcbiMgTWF4aW11bSBudW1iZXIgb2Ygb3BlbiBkYXRhYmFzZSBjb25uZWN0aW9uc1xubWF4X29wZW4gPSAzMFxuIyBNYXhpbXVtIG51bWJlciBvZiBpZGxlIGNvbm5lY3Rpb25zIGluIHRoZSBwb29sXG5tYXhfaWRsZSA9IDMwXG4jIE1heGltdW0gdGltZSBhIGNvbm5lY3Rpb24gY2FuIGJlIHJldXNlZCBiZWZvcmUgYmVpbmcgY2xvc2VkXG5tYXhfbGlmZXRpbWUgPSBcIjMwMHNcIlxuXG4jIFJlZGlzLlxuW3JlZGlzXVxuIyBJZiBydW5uaW5nIGxvY2FsbHksIHVzZSBgbG9jYWxob3N0OjYzNzlgLlxuYWRkcmVzcyA9IFwicmVkaXM6NjM3OVwiXG5wYXNzd29yZCA9IFwiXCJcbmRiID0gMFxuXG5bbWVzc2FnZV1cbiMgTnVtYmVyIG9mIHdvcmtlcnMgcHJvY2Vzc2luZyBvdXRnb2luZyBtZXNzYWdlIHF1ZXVlXG5vdXRnb2luZ19xdWV1ZV93b3JrZXJzID0gMTBcbiMgTnVtYmVyIG9mIHdvcmtlcnMgcHJvY2Vzc2luZyBpbmNvbWluZyBtZXNzYWdlIHF1ZXVlXG5pbmNvbWluZ19xdWV1ZV93b3JrZXJzID0gMTBcbiMgSG93IG9mdGVuIHRvIHNjYW4gZm9yIG91dGdvaW5nIG1lc3NhZ2VzIHRvIHByb2Nlc3MsIGtlZXAgaXQgbG93IHRvIHByb2Nlc3MgbWVzc2FnZXMgcXVpY2tseS5cbm1lc3NhZ2Vfb3V0Z29pbmdfc2Nhbl9pbnRlcnZhbCA9IFwiNTBtc1wiXG4jIE1heGltdW0gbnVtYmVyIG9mIG1lc3NhZ2VzIHRoYXQgY2FuIGJlIHF1ZXVlZCBmb3IgaW5jb21pbmcgcHJvY2Vzc2luZ1xuaW5jb21pbmdfcXVldWVfc2l6ZSA9IDUwMDBcbiMgTWF4aW11bSBudW1iZXIgb2YgbWVzc2FnZXMgdGhhdCBjYW4gYmUgcXVldWVkIGZvciBvdXRnb2luZyBwcm9jZXNzaW5nXG5vdXRnb2luZ19xdWV1ZV9zaXplID0gNTAwMFxuXG5bbm90aWZpY2F0aW9uXVxuIyBOdW1iZXIgb2YgY29uY3VycmVudCBub3RpZmljYXRpb24gd29ya2Vyc1xuY29uY3VycmVuY3kgPSAyXG4jIE1heGltdW0gbnVtYmVyIG9mIG5vdGlmaWNhdGlvbnMgdGhhdCBjYW4gYmUgcXVldWVkXG5xdWV1ZV9zaXplID0gMjAwMFxuXG5bYXV0b21hdGlvbl1cbiMgTnVtYmVyIG9mIHdvcmtlcnMgcHJvY2Vzc2luZyBhdXRvbWF0aW9uIHJ1bGVzXG53b3JrZXJfY291bnQgPSAxMFxuXG5bYXV0b2Fzc2lnbmVyXVxuIyBIb3cgb2Z0ZW4gdG8gcnVuIGF1dG9tYXRpYyBjb252ZXJzYXRpb24gYXNzaWdubWVudFxuYXV0b2Fzc2lnbl9pbnRlcnZhbCA9IFwiNW1cIlxuXG5bd2ViaG9va11cbiMgTnVtYmVyIG9mIHdlYmhvb2sgZGVsaXZlcnkgd29ya2Vyc1xud29ya2VycyA9IDVcbiMgTWF4aW11bSBudW1iZXIgb2Ygd2ViaG9vayBkZWxpdmVyaWVzIHRoYXQgY2FuIGJlIHF1ZXVlZFxucXVldWVfc2l6ZSA9IDEwMDAwXG4jIEhUVFAgdGltZW91dCBmb3Igd2ViaG9vayByZXF1ZXN0c1xudGltZW91dCA9IFwiMTVzXCJcblxuW2NvbnZlcnNhdGlvbl1cbiMgSG93IG9mdGVuIHRvIGNoZWNrIGZvciBjb252ZXJzYXRpb25zIHRvIHVuc25vb3plXG51bnNub296ZV9pbnRlcnZhbCA9IFwiNW1cIlxuXG5bc2xhXVxuIyBIb3cgb2Z0ZW4gdG8gZXZhbHVhdGUgU0xBIGNvbXBsaWFuY2UgZm9yIGNvbnZlcnNhdGlvbnNcbmV2YWx1YXRpb25faW50ZXJ2YWwgPSBcIjVtXCJcblxuXCJcIlwiIgp9
```

## Links

`storage`,`object-storage`

---

Version:`latest`

LibreChatLibreChat is the ultimate open-source app for all your AI conversations, fully customizable and compatible with any AI provider (Openai, Ollama, Google etc.) — all in one sleek interface.

LibreTranslateLibreTranslate is a free and open-source machine translation API, powered by Argos Translate. Self-hosted, no external dependencies, and supports multiple languages.

### On this page

ConfigurationBase64LinksTags