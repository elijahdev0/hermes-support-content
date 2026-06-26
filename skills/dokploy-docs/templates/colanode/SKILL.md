---
title: "Colanode Server | Dokploy"
source: "https://docs.dokploy.com/docs/templates/colanode"
category: dokploy-docs
created: "2026-06-25T17:21:45.076Z"
---

Colanode Server | Dokploy

# Colanode Server

Copy as Markdown

Open-source and local-first Slack and Notion alternative that puts you in control of your data

## Configuration

docker-compose.ymltemplate.toml

```
services:
  postgres:
    image: pgvector/pgvector:pg17
    restart: always
    environment:
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: ${POSTGRES_DB}
    volumes:
      - postgres_data:/var/lib/postgresql/data

  valkey:
    image: valkey/valkey:8.1
    restart: always
    command: ["valkey-server", "--requirepass", "${VALKEY_PASSWORD}"]
    volumes:
      - valkey_data:/data

  minio:
    image: minio/minio:RELEASE.2025-04-08T15-41-24Z
    restart: always
    environment:
      MINIO_ROOT_USER: ${MINIO_ROOT_USER}
      MINIO_ROOT_PASSWORD: ${MINIO_ROOT_PASSWORD}
      MINIO_BROWSER: "on"
      MINIO_DOMAIN: minio
      MINIO_ADDRESS: ":9000"
      MINIO_CONSOLE_ADDRESS: ":9001"
    volumes:
      - minio_data:/data
    entrypoint: sh
    command: -c 'mkdir -p /data/colanode-avatars /data/colanode-files && minio server /data --address ":9000" --console-address ":9001"'

  server:
    image: ghcr.io/colanode/server:latest
    restart: always
    depends_on:
      - postgres
      - valkey
      - minio
    environment:
      # ---------------------------------------------------------------
      # General Node/Server Config
      # ---------------------------------------------------------------
      NODE_ENV: production
      PORT: 3000

      # The server requires a name and avatar URL which will be displayed in the desktop app login screen.
      SERVER_NAME: ${SERVER_NAME}
      SERVER_AVATAR: ${SERVER_AVATAR}
      # Possible values for SERVER_MODE: 'standalone', 'cluster'
      SERVER_MODE: "standalone"

      # ---------------------------------------------------------------
      # Account Configuration
      # ---------------------------------------------------------------
      # Possible values for ACCOUNT_VERIFICATION_TYPE: 'automatic', 'manual', 'email'
      ACCOUNT_VERIFICATION_TYPE: "automatic"
      ACCOUNT_OTP_TIMEOUT: "600" # in seconds
      ACCOUNT_ALLOW_GOOGLE_LOGIN: "false"

      # ---------------------------------------------------------------
      # User Configuration
      # ---------------------------------------------------------------
      USER_STORAGE_LIMIT: "10737418240" # 10 GB
      USER_MAX_FILE_SIZE: "104857600" # 100 MB

      # ---------------------------------------------------------------
      # PostgreSQL Configuration
      # ---------------------------------------------------------------
      # The server expects a PostgreSQL database with the pgvector extension installed.
      POSTGRES_URL: "postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@postgres:5432/${POSTGRES_DB}"

      # Optional variables for SSL connection to the database
      # POSTGRES_SSL_REJECT_UNAUTHORIZED: 'false'
      # POSTGRES_SSL_CA: ''
      # POSTGRES_SSL_KEY: ''
      # POSTGRES_SSL_CERT: ''

      # ---------------------------------------------------------------
      # Redis Configuration
      # ---------------------------------------------------------------
      REDIS_URL: "redis://:${VALKEY_PASSWORD}@valkey:6379/0"
      REDIS_DB: "0"
      # Optional variables:
      REDIS_JOBS_QUEUE_NAME: "jobs"
      REDIS_JOBS_QUEUE_PREFIX: "colanode"
      REDIS_EVENTS_CHANNEL: "events"

      # ---------------------------------------------------------------
      # S3 Configuration for Avatars
      # ---------------------------------------------------------------
      S3_AVATARS_ENDPOINT: "http://minio:9000"
      S3_AVATARS_ACCESS_KEY: ${MINIO_ROOT_USER}
      S3_AVATARS_SECRET_KEY: ${MINIO_ROOT_PASSWORD}
      S3_AVATARS_BUCKET_NAME: "colanode-avatars"
      S3_AVATARS_REGION: "us-east-1"
      S3_AVATARS_FORCE_PATH_STYLE: "true"

      # ---------------------------------------------------------------
      # S3 Configuration for Files
      # ---------------------------------------------------------------
      STORAGE_S3_ENDPOINT: "http://minio:9000"
      STORAGE_S3_ACCESS_KEY: ${MINIO_ROOT_USER}
      STORAGE_S3_SECRET_KEY: ${MINIO_ROOT_PASSWORD}
      STORAGE_S3_BUCKET: "colanode-files"
      STORAGE_S3_REGION: "us-east-1"
      STORAGE_S3_FORCE_PATH_STYLE: "true"

      # ---------------------------------------------------------------
      # SMTP configuration
      # ---------------------------------------------------------------
      SMTP_ENABLED: ${SMTP_ENABLED}
      SMTP_HOST: ${SMTP_HOST}
      SMTP_PORT: ${SMTP_PORT}
      SMTP_USER: ${SMTP_USER}
      SMTP_PASSWORD: ${SMTP_PASSWORD}
      SMTP_EMAIL_FROM: ${SMTP_EMAIL_FROM}
      SMTP_EMAIL_FROM_NAME: ${SMTP_EMAIL_FROM_NAME}

      # ---------------------------------------------------------------
      # AI Configuration
      # ---------------------------------------------------------------
      # The AI integration is in experimental mode yet and we don't
      # recommend using it.
      # ---------------------------------------------------------------
      AI_ENABLED: "false"
      # ---------------------------------------------------------------

volumes:
  postgres_data:
  valkey_data:
  minio_data:
```

```
[variables]
main_domain = "${domain}"

[config]
mounts = []

[[config.domains]]
serviceName = "server"
port = 3000
host = "${main_domain}"

[config.env]
SERVER_NAME = "My Colanode"
SERVER_AVATAR = "https://colanode.com/assets/logo-black.png"

POSTGRES_USER = "colanode_user"
POSTGRES_PASSWORD = "your_postgres_password"
POSTGRES_DB = "colanode_db"

VALKEY_PASSWORD = "your_valkey_password"

MINIO_ROOT_USER = "admin"
MINIO_ROOT_PASSWORD = "your_minio_password"

SMTP_ENABLED = "false"
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = "587"
SMTP_USER = "your_smtp_username"
SMTP_PASSWORD = "your_smtp_password"
SMTP_EMAIL_FROM = "[email protected]"
SMTP_EMAIL_FROM_NAME = "Colanode"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBwb3N0Z3JlczpcbiAgICBpbWFnZTogcGd2ZWN0b3IvcGd2ZWN0b3I6cGcxN1xuICAgIHJlc3RhcnQ6IGFsd2F5c1xuICAgIGVudmlyb25tZW50OlxuICAgICAgUE9TVEdSRVNfVVNFUjogJHtQT1NUR1JFU19VU0VSfVxuICAgICAgUE9TVEdSRVNfUEFTU1dPUkQ6ICR7UE9TVEdSRVNfUEFTU1dPUkR9XG4gICAgICBQT1NUR1JFU19EQjogJHtQT1NUR1JFU19EQn1cbiAgICB2b2x1bWVzOlxuICAgICAgLSBwb3N0Z3Jlc19kYXRhOi92YXIvbGliL3Bvc3RncmVzcWwvZGF0YVxuXG4gIHZhbGtleTpcbiAgICBpbWFnZTogdmFsa2V5L3ZhbGtleTo4LjFcbiAgICByZXN0YXJ0OiBhbHdheXNcbiAgICBjb21tYW5kOiBbXCJ2YWxrZXktc2VydmVyXCIsIFwiLS1yZXF1aXJlcGFzc1wiLCBcIiR7VkFMS0VZX1BBU1NXT1JEfVwiXVxuICAgIHZvbHVtZXM6XG4gICAgICAtIHZhbGtleV9kYXRhOi9kYXRhXG5cbiAgbWluaW86XG4gICAgaW1hZ2U6IG1pbmlvL21pbmlvOlJFTEVBU0UuMjAyNS0wNC0wOFQxNS00MS0yNFpcbiAgICByZXN0YXJ0OiBhbHdheXNcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIE1JTklPX1JPT1RfVVNFUjogJHtNSU5JT19ST09UX1VTRVJ9XG4gICAgICBNSU5JT19ST09UX1BBU1NXT1JEOiAke01JTklPX1JPT1RfUEFTU1dPUkR9XG4gICAgICBNSU5JT19CUk9XU0VSOiBcIm9uXCJcbiAgICAgIE1JTklPX0RPTUFJTjogbWluaW9cbiAgICAgIE1JTklPX0FERFJFU1M6IFwiOjkwMDBcIlxuICAgICAgTUlOSU9fQ09OU09MRV9BRERSRVNTOiBcIjo5MDAxXCJcbiAgICB2b2x1bWVzOlxuICAgICAgLSBtaW5pb19kYXRhOi9kYXRhXG4gICAgZW50cnlwb2ludDogc2hcbiAgICBjb21tYW5kOiAtYyAnbWtkaXIgLXAgL2RhdGEvY29sYW5vZGUtYXZhdGFycyAvZGF0YS9jb2xhbm9kZS1maWxlcyAmJiBtaW5pbyBzZXJ2ZXIgL2RhdGEgLS1hZGRyZXNzIFwiOjkwMDBcIiAtLWNvbnNvbGUtYWRkcmVzcyBcIjo5MDAxXCInXG5cbiAgc2VydmVyOlxuICAgIGltYWdlOiBnaGNyLmlvL2NvbGFub2RlL3NlcnZlcjpsYXRlc3RcbiAgICByZXN0YXJ0OiBhbHdheXNcbiAgICBkZXBlbmRzX29uOlxuICAgICAgLSBwb3N0Z3Jlc1xuICAgICAgLSB2YWxrZXlcbiAgICAgIC0gbWluaW9cbiAgICBlbnZpcm9ubWVudDpcbiAgICAgICMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG4gICAgICAjIEdlbmVyYWwgTm9kZS9TZXJ2ZXIgQ29uZmlnXG4gICAgICAjIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuICAgICAgTk9ERV9FTlY6IHByb2R1Y3Rpb25cbiAgICAgIFBPUlQ6IDMwMDBcblxuICAgICAgIyBUaGUgc2VydmVyIHJlcXVpcmVzIGEgbmFtZSBhbmQgYXZhdGFyIFVSTCB3aGljaCB3aWxsIGJlIGRpc3BsYXllZCBpbiB0aGUgZGVza3RvcCBhcHAgbG9naW4gc2NyZWVuLlxuICAgICAgU0VSVkVSX05BTUU6ICR7U0VSVkVSX05BTUV9XG4gICAgICBTRVJWRVJfQVZBVEFSOiAke1NFUlZFUl9BVkFUQVJ9XG4gICAgICAjIFBvc3NpYmxlIHZhbHVlcyBmb3IgU0VSVkVSX01PREU6ICdzdGFuZGFsb25lJywgJ2NsdXN0ZXInXG4gICAgICBTRVJWRVJfTU9ERTogXCJzdGFuZGFsb25lXCJcblxuICAgICAgIyAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cbiAgICAgICMgQWNjb3VudCBDb25maWd1cmF0aW9uXG4gICAgICAjIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuICAgICAgIyBQb3NzaWJsZSB2YWx1ZXMgZm9yIEFDQ09VTlRfVkVSSUZJQ0FUSU9OX1RZUEU6ICdhdXRvbWF0aWMnLCAnbWFudWFsJywgJ2VtYWlsJ1xuICAgICAgQUNDT1VOVF9WRVJJRklDQVRJT05fVFlQRTogXCJhdXRvbWF0aWNcIlxuICAgICAgQUNDT1VOVF9PVFBfVElNRU9VVDogXCI2MDBcIiAjIGluIHNlY29uZHNcbiAgICAgIEFDQ09VTlRfQUxMT1dfR09PR0xFX0xPR0lOOiBcImZhbHNlXCJcblxuICAgICAgIyAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cbiAgICAgICMgVXNlciBDb25maWd1cmF0aW9uXG4gICAgICAjIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuICAgICAgVVNFUl9TVE9SQUdFX0xJTUlUOiBcIjEwNzM3NDE4MjQwXCIgIyAxMCBHQlxuICAgICAgVVNFUl9NQVhfRklMRV9TSVpFOiBcIjEwNDg1NzYwMFwiICMgMTAwIE1CXG5cbiAgICAgICMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG4gICAgICAjIFBvc3RncmVTUUwgQ29uZmlndXJhdGlvblxuICAgICAgIyAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cbiAgICAgICMgVGhlIHNlcnZlciBleHBlY3RzIGEgUG9zdGdyZVNRTCBkYXRhYmFzZSB3aXRoIHRoZSBwZ3ZlY3RvciBleHRlbnNpb24gaW5zdGFsbGVkLlxuICAgICAgUE9TVEdSRVNfVVJMOiBcInBvc3RncmVzOi8vJHtQT1NUR1JFU19VU0VSfToke1BPU1RHUkVTX1BBU1NXT1JEfUBwb3N0Z3Jlczo1NDMyLyR7UE9TVEdSRVNfREJ9XCJcblxuICAgICAgIyBPcHRpb25hbCB2YXJpYWJsZXMgZm9yIFNTTCBjb25uZWN0aW9uIHRvIHRoZSBkYXRhYmFzZVxuICAgICAgIyBQT1NUR1JFU19TU0xfUkVKRUNUX1VOQVVUSE9SSVpFRDogJ2ZhbHNlJ1xuICAgICAgIyBQT1NUR1JFU19TU0xfQ0E6ICcnXG4gICAgICAjIFBPU1RHUkVTX1NTTF9LRVk6ICcnXG4gICAgICAjIFBPU1RHUkVTX1NTTF9DRVJUOiAnJ1xuXG4gICAgICAjIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuICAgICAgIyBSZWRpcyBDb25maWd1cmF0aW9uXG4gICAgICAjIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuICAgICAgUkVESVNfVVJMOiBcInJlZGlzOi8vOiR7VkFMS0VZX1BBU1NXT1JEfUB2YWxrZXk6NjM3OS8wXCJcbiAgICAgIFJFRElTX0RCOiBcIjBcIlxuICAgICAgIyBPcHRpb25hbCB2YXJpYWJsZXM6XG4gICAgICBSRURJU19KT0JTX1FVRVVFX05BTUU6IFwiam9ic1wiXG4gICAgICBSRURJU19KT0JTX1FVRVVFX1BSRUZJWDogXCJjb2xhbm9kZVwiXG4gICAgICBSRURJU19FVkVOVFNfQ0hBTk5FTDogXCJldmVudHNcIlxuXG4gICAgICAjIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuICAgICAgIyBTMyBDb25maWd1cmF0aW9uIGZvciBBdmF0YXJzXG4gICAgICAjIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuICAgICAgUzNfQVZBVEFSU19FTkRQT0lOVDogXCJodHRwOi8vbWluaW86OTAwMFwiXG4gICAgICBTM19BVkFUQVJTX0FDQ0VTU19LRVk6ICR7TUlOSU9fUk9PVF9VU0VSfVxuICAgICAgUzNfQVZBVEFSU19TRUNSRVRfS0VZOiAke01JTklPX1JPT1RfUEFTU1dPUkR9XG4gICAgICBTM19BVkFUQVJTX0JVQ0tFVF9OQU1FOiBcImNvbGFub2RlLWF2YXRhcnNcIlxuICAgICAgUzNfQVZBVEFSU19SRUdJT046IFwidXMtZWFzdC0xXCJcbiAgICAgIFMzX0FWQVRBUlNfRk9SQ0VfUEFUSF9TVFlMRTogXCJ0cnVlXCJcblxuICAgICAgIyAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cbiAgICAgICMgUzMgQ29uZmlndXJhdGlvbiBmb3IgRmlsZXNcbiAgICAgICMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG4gICAgICBTVE9SQUdFX1MzX0VORFBPSU5UOiBcImh0dHA6Ly9taW5pbzo5MDAwXCJcbiAgICAgIFNUT1JBR0VfUzNfQUNDRVNTX0tFWTogJHtNSU5JT19ST09UX1VTRVJ9XG4gICAgICBTVE9SQUdFX1MzX1NFQ1JFVF9LRVk6ICR7TUlOSU9fUk9PVF9QQVNTV09SRH1cbiAgICAgIFNUT1JBR0VfUzNfQlVDS0VUOiBcImNvbGFub2RlLWZpbGVzXCJcbiAgICAgIFNUT1JBR0VfUzNfUkVHSU9OOiBcInVzLWVhc3QtMVwiXG4gICAgICBTVE9SQUdFX1MzX0ZPUkNFX1BBVEhfU1RZTEU6IFwidHJ1ZVwiXG5cbiAgICAgICMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG4gICAgICAjIFNNVFAgY29uZmlndXJhdGlvblxuICAgICAgIyAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cbiAgICAgIFNNVFBfRU5BQkxFRDogJHtTTVRQX0VOQUJMRUR9XG4gICAgICBTTVRQX0hPU1Q6ICR7U01UUF9IT1NUfVxuICAgICAgU01UUF9QT1JUOiAke1NNVFBfUE9SVH1cbiAgICAgIFNNVFBfVVNFUjogJHtTTVRQX1VTRVJ9XG4gICAgICBTTVRQX1BBU1NXT1JEOiAke1NNVFBfUEFTU1dPUkR9XG4gICAgICBTTVRQX0VNQUlMX0ZST006ICR7U01UUF9FTUFJTF9GUk9NfVxuICAgICAgU01UUF9FTUFJTF9GUk9NX05BTUU6ICR7U01UUF9FTUFJTF9GUk9NX05BTUV9XG5cbiAgICAgICMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG4gICAgICAjIEFJIENvbmZpZ3VyYXRpb25cbiAgICAgICMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG4gICAgICAjIFRoZSBBSSBpbnRlZ3JhdGlvbiBpcyBpbiBleHBlcmltZW50YWwgbW9kZSB5ZXQgYW5kIHdlIGRvbid0XG4gICAgICAjIHJlY29tbWVuZCB1c2luZyBpdC5cbiAgICAgICMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG4gICAgICBBSV9FTkFCTEVEOiBcImZhbHNlXCJcbiAgICAgICMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG5cbnZvbHVtZXM6XG4gIHBvc3RncmVzX2RhdGE6XG4gIHZhbGtleV9kYXRhOlxuICBtaW5pb19kYXRhOlxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcblxuW2NvbmZpZ11cbm1vdW50cyA9IFtdXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcInNlcnZlclwiXG5wb3J0ID0gMzAwMFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cblNFUlZFUl9OQU1FID0gXCJNeSBDb2xhbm9kZVwiXG5TRVJWRVJfQVZBVEFSID0gXCJodHRwczovL2NvbGFub2RlLmNvbS9hc3NldHMvbG9nby1ibGFjay5wbmdcIlxuXG5QT1NUR1JFU19VU0VSID0gXCJjb2xhbm9kZV91c2VyXCJcblBPU1RHUkVTX1BBU1NXT1JEID0gXCJ5b3VyX3Bvc3RncmVzX3Bhc3N3b3JkXCJcblBPU1RHUkVTX0RCID0gXCJjb2xhbm9kZV9kYlwiXG5cblZBTEtFWV9QQVNTV09SRCA9IFwieW91cl92YWxrZXlfcGFzc3dvcmRcIlxuXG5NSU5JT19ST09UX1VTRVIgPSBcImFkbWluXCJcbk1JTklPX1JPT1RfUEFTU1dPUkQgPSBcInlvdXJfbWluaW9fcGFzc3dvcmRcIlxuXG5TTVRQX0VOQUJMRUQgPSBcImZhbHNlXCJcblNNVFBfSE9TVCA9IFwic210cC5nbWFpbC5jb21cIlxuU01UUF9QT1JUID0gXCI1ODdcIlxuU01UUF9VU0VSID0gXCJ5b3VyX3NtdHBfdXNlcm5hbWVcIlxuU01UUF9QQVNTV09SRCA9IFwieW91cl9zbXRwX3Bhc3N3b3JkXCJcblNNVFBfRU1BSUxfRlJPTSA9IFwieW91cl9lbWFpbEBleGFtcGxlLmNvbVwiXG5TTVRQX0VNQUlMX0ZST01fTkFNRSA9IFwiQ29sYW5vZGVcIlxuIgp9
```

## Links

`documentation`,`knowledge-base`,`collaboration`

---

Version:`v0.1.6`

CodeX DocsCodeX is a comprehensive platform that brings together passionate engineers, designers, and specialists to create high-quality open-source projects. It includes Editor.js, Hawk.so, CodeX Notes, and more.

Collabora OfficeCollabora Online is a powerful, flexible, and secure online office suite designed to break free from vendor lock-in and put you in full control of your documents.

### On this page

ConfigurationBase64LinksTags