---
title: "XSSHunter | Dokploy"
source: "https://docs.dokploy.com/docs/templates/xsshunter"
category: dokploy-docs
created: "2026-06-25T17:22:02.523Z"
---

XSSHunter | Dokploy

# XSSHunter

Copy as Markdown

XSSHunter is an open-source platform designed to identify and exploit blind Cross-Site Scripting (XSS) vulnerabilities. It provides security researchers, bug bounty hunters, and penetration testers with a comprehensive toolkit for detecting XSS flaws that are otherwise difficult to discover through traditional testing methods.

## Configuration

docker-compose.ymltemplate.toml

```
#version: '3.8'

services:
  xsshunterexpress-db:
    image: postgres:15-alpine
    restart: unless-stopped
    environment:
      POSTGRES_DB: ${POSTGRES_DB:-xsshunterexpress}
      POSTGRES_USER: ${POSTGRES_USER:-xsshunterexpress}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD:-xsshunterexpress}
      PGDATA: /var/lib/postgresql/data/pgdata
      POSTGRES_HOST_AUTH_METHOD: trust
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER:-xsshunterexpress}"]
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 30s
    volumes:
      - postgres_data:/var/lib/postgresql/data/pgdata

  xsshunterexpress-service:
    build: https://github.com/rs-loves-bugs/xsshunter.git
    restart: unless-stopped
    environment:
      # Core Configuration
      SESSION_SECRET_KEY: ${SESSION_SECRET_KEY}
      HOSTNAME: ${HOSTNAME}
      XSS_HOSTNAME: ${XSS_HOSTNAME}

      # Panel Configuration
      PANEL_LOGIN: ${PANEL_LOGIN:-true}
      PANEL_USERNAME: ${PANEL_USERNAME}
      PANEL_PASSWORD: ${PANEL_PASSWORD}
      ALLOW_EMPTY_USERPATH: ${ALLOW_EMPTY_USERPATH:-true}

      # OAuth Configuration
      OAUTH_LOGIN: ${OAUTH_LOGIN:-false}
      CLIENT_ID: ${CLIENT_ID:-}
      CLIENT_SECRET: ${CLIENT_SECRET:-}
      GMAIL_ACCOUNTS: ${GMAIL_ACCOUNTS:-}

      # Email Configuration
      EMAIL_NOTIFICATIONS_ENABLED: ${EMAIL_NOTIFICATIONS_ENABLED:-false}
      EMAIL_FROM: ${EMAIL_FROM:-}
      SENDGRID_API_KEY: ${SENDGRID_API_KEY:-}
      SENDGRID_UNSUBSRIBE_GROUP_ID: ${SENDGRID_UNSUBSRIBE_GROUP_ID:-}

      # Database Configuration
      DATABASE_HOST: xsshunterexpress-db
      POSTGRES_DB: ${POSTGRES_DB:-xsshunterexpress}
      POSTGRES_USER: ${POSTGRES_USER:-xsshunterexpress}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD:-xsshunterexpress}

      # Application Configuration
      NODE_ENV: ${NODE_ENV:-production}
      PORT: ${PORT}
      CONTROL_PANEL_ENABLED: ${CONTROL_PANEL_ENABLED:-true}
      SCREENSHOTS_DIR: /app/payload-fire-images
      TRUFFLEHOG_URL: http://${TRUFFLEHOG_HOST:-xsshunterexpress-trufflehog}:${TRUFFLEHOG_PORT:-8000}/trufflehog

      # Optional Services
      SENTRY_DSN: ${SENTRY_DSN:-}
      SENTRY_ENABLED: ${SENTRY_ENABLED:-false}
      USE_CLOUD_STORAGE: ${USE_CLOUD_STORAGE:-false}
      BUCKET_NAME: ${BUCKET_NAME:-}
    expose:
      - ${PORT:-8080}
    volumes:
      - payload_images:/app/payload-fire-images
    depends_on:
      xsshunterexpress-db:
        condition: service_healthy

  xsshunterexpress-trufflehog:
    build:
      context: https://github.com/rs-loves-bugs/xsshunter.git
      dockerfile: Dockerfile.trufflehog
    restart: unless-stopped
    expose:
      - ${TRUFFLEHOG_PORT:-8000}

volumes:
  postgres_data:
    driver: local
  payload_images:
    driver: local
```

```
[variables]
admin_domain = "${domain}"
xss_domain = "${domain}"
session_secret = "${base64:64}"
admin_password = "${password:32}"
db_password = "${password:16}"
postgres_user = "xsshunterexpress"
postgres_db = "xsshunterexpress"

[config]
[[config.domains]]
serviceName = "xsshunterexpress-service"
port = 8080
host = "${admin_domain}"

[[config.domains]]
serviceName = "xsshunterexpress-service"
port = 8080
host = "xss.${admin_domain}"

[config.env]
# Core Configuration
SESSION_SECRET_KEY = "${session_secret}"
HOSTNAME = "${admin_domain}"
XSS_HOSTNAME = "xss.${admin_domain}"

# Panel Configuration
PANEL_LOGIN = "true"
PANEL_USERNAME = "admin@${admin_domain}"
PANEL_PASSWORD = '${admin_password}' # [ use single quote to avoid the problem] just to let you know takecare of the special characters, it will make your password invalid, so make a strong password without special characters
ALLOW_EMPTY_USERPATH = "true"

# OAuth Configuration (disabled by default)
OAUTH_LOGIN = "false"
CLIENT_ID = ""
CLIENT_SECRET = ""
GMAIL_ACCOUNTS = ""

# Email Configuration (disabled by default)
EMAIL_NOTIFICATIONS_ENABLED = "false"
EMAIL_FROM = ""
SENDGRID_API_KEY = ""
SENDGRID_UNSUBSRIBE_GROUP_ID = ""

# Database Configuration
DATABASE_HOST = "xsshunterexpress-db"
POSTGRES_DB = "${postgres_db}"
POSTGRES_USER = "${postgres_user}"
POSTGRES_PASSWORD = "${db_password}"

# Application Configuration
NODE_ENV = "production"
PORT = "8080"
CONTROL_PANEL_ENABLED = "true"
SCREENSHOTS_DIR = "/app/payload-fire-images"
TRUFFLEHOG_URL = "http://${TRUFFLEHOG_HOST}:${TRUFFLEHOG_PORT}/trufflehog"

# Port Configuration
APP_PORT = "8080"
TRUFFLEHOG_HOST = "xsshunterexpress-trufflehog"
TRUFFLEHOG_PORT = "8000"

# Optional Services (disabled by default)
SENTRY_DSN = ""
SENTRY_ENABLED = "false"
USE_CLOUD_STORAGE = "false"
BUCKET_NAME = ""

[[config.mounts]]
filePath = "./payload-fire-images"
content = "Directory for storing XSS payload screenshots and collected data"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogIiN2ZXJzaW9uOiAnMy44J1xuXG5zZXJ2aWNlczpcbiAgeHNzaHVudGVyZXhwcmVzcy1kYjpcbiAgICBpbWFnZTogcG9zdGdyZXM6MTUtYWxwaW5lXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIFBPU1RHUkVTX0RCOiAke1BPU1RHUkVTX0RCOi14c3NodW50ZXJleHByZXNzfVxuICAgICAgUE9TVEdSRVNfVVNFUjogJHtQT1NUR1JFU19VU0VSOi14c3NodW50ZXJleHByZXNzfVxuICAgICAgUE9TVEdSRVNfUEFTU1dPUkQ6ICR7UE9TVEdSRVNfUEFTU1dPUkQ6LXhzc2h1bnRlcmV4cHJlc3N9XG4gICAgICBQR0RBVEE6IC92YXIvbGliL3Bvc3RncmVzcWwvZGF0YS9wZ2RhdGFcbiAgICAgIFBPU1RHUkVTX0hPU1RfQVVUSF9NRVRIT0Q6IHRydXN0XG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OiBbXCJDTUQtU0hFTExcIiwgXCJwZ19pc3JlYWR5IC1VICR7UE9TVEdSRVNfVVNFUjoteHNzaHVudGVyZXhwcmVzc31cIl1cbiAgICAgIGludGVydmFsOiAxMHNcbiAgICAgIHRpbWVvdXQ6IDVzXG4gICAgICByZXRyaWVzOiA1XG4gICAgICBzdGFydF9wZXJpb2Q6IDMwc1xuICAgIHZvbHVtZXM6XG4gICAgICAtIHBvc3RncmVzX2RhdGE6L3Zhci9saWIvcG9zdGdyZXNxbC9kYXRhL3BnZGF0YVxuXG4gIHhzc2h1bnRlcmV4cHJlc3Mtc2VydmljZTpcbiAgICBidWlsZDogaHR0cHM6Ly9naXRodWIuY29tL3JzLWxvdmVzLWJ1Z3MveHNzaHVudGVyLmdpdFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAjIENvcmUgQ29uZmlndXJhdGlvblxuICAgICAgU0VTU0lPTl9TRUNSRVRfS0VZOiAke1NFU1NJT05fU0VDUkVUX0tFWX1cbiAgICAgIEhPU1ROQU1FOiAke0hPU1ROQU1FfVxuICAgICAgWFNTX0hPU1ROQU1FOiAke1hTU19IT1NUTkFNRX1cbiAgICAgIFxuICAgICAgIyBQYW5lbCBDb25maWd1cmF0aW9uXG4gICAgICBQQU5FTF9MT0dJTjogJHtQQU5FTF9MT0dJTjotdHJ1ZX1cbiAgICAgIFBBTkVMX1VTRVJOQU1FOiAke1BBTkVMX1VTRVJOQU1FfVxuICAgICAgUEFORUxfUEFTU1dPUkQ6ICR7UEFORUxfUEFTU1dPUkR9XG4gICAgICBBTExPV19FTVBUWV9VU0VSUEFUSDogJHtBTExPV19FTVBUWV9VU0VSUEFUSDotdHJ1ZX1cbiAgICAgIFxuICAgICAgIyBPQXV0aCBDb25maWd1cmF0aW9uXG4gICAgICBPQVVUSF9MT0dJTjogJHtPQVVUSF9MT0dJTjotZmFsc2V9XG4gICAgICBDTElFTlRfSUQ6ICR7Q0xJRU5UX0lEOi19XG4gICAgICBDTElFTlRfU0VDUkVUOiAke0NMSUVOVF9TRUNSRVQ6LX1cbiAgICAgIEdNQUlMX0FDQ09VTlRTOiAke0dNQUlMX0FDQ09VTlRTOi19XG4gICAgICBcbiAgICAgICMgRW1haWwgQ29uZmlndXJhdGlvblxuICAgICAgRU1BSUxfTk9USUZJQ0FUSU9OU19FTkFCTEVEOiAke0VNQUlMX05PVElGSUNBVElPTlNfRU5BQkxFRDotZmFsc2V9XG4gICAgICBFTUFJTF9GUk9NOiAke0VNQUlMX0ZST006LX1cbiAgICAgIFNFTkRHUklEX0FQSV9LRVk6ICR7U0VOREdSSURfQVBJX0tFWTotfVxuICAgICAgU0VOREdSSURfVU5TVUJTUklCRV9HUk9VUF9JRDogJHtTRU5ER1JJRF9VTlNVQlNSSUJFX0dST1VQX0lEOi19XG4gICAgICBcbiAgICAgICMgRGF0YWJhc2UgQ29uZmlndXJhdGlvblxuICAgICAgREFUQUJBU0VfSE9TVDogeHNzaHVudGVyZXhwcmVzcy1kYlxuICAgICAgUE9TVEdSRVNfREI6ICR7UE9TVEdSRVNfREI6LXhzc2h1bnRlcmV4cHJlc3N9XG4gICAgICBQT1NUR1JFU19VU0VSOiAke1BPU1RHUkVTX1VTRVI6LXhzc2h1bnRlcmV4cHJlc3N9XG4gICAgICBQT1NUR1JFU19QQVNTV09SRDogJHtQT1NUR1JFU19QQVNTV09SRDoteHNzaHVudGVyZXhwcmVzc31cbiAgICAgIFxuICAgICAgIyBBcHBsaWNhdGlvbiBDb25maWd1cmF0aW9uXG4gICAgICBOT0RFX0VOVjogJHtOT0RFX0VOVjotcHJvZHVjdGlvbn1cbiAgICAgIFBPUlQ6ICR7UE9SVH1cbiAgICAgIENPTlRST0xfUEFORUxfRU5BQkxFRDogJHtDT05UUk9MX1BBTkVMX0VOQUJMRUQ6LXRydWV9XG4gICAgICBTQ1JFRU5TSE9UU19ESVI6IC9hcHAvcGF5bG9hZC1maXJlLWltYWdlc1xuICAgICAgVFJVRkZMRUhPR19VUkw6IGh0dHA6Ly8ke1RSVUZGTEVIT0dfSE9TVDoteHNzaHVudGVyZXhwcmVzcy10cnVmZmxlaG9nfToke1RSVUZGTEVIT0dfUE9SVDotODAwMH0vdHJ1ZmZsZWhvZ1xuICAgICAgXG4gICAgICAjIE9wdGlvbmFsIFNlcnZpY2VzXG4gICAgICBTRU5UUllfRFNOOiAke1NFTlRSWV9EU046LX1cbiAgICAgIFNFTlRSWV9FTkFCTEVEOiAke1NFTlRSWV9FTkFCTEVEOi1mYWxzZX1cbiAgICAgIFVTRV9DTE9VRF9TVE9SQUdFOiAke1VTRV9DTE9VRF9TVE9SQUdFOi1mYWxzZX1cbiAgICAgIEJVQ0tFVF9OQU1FOiAke0JVQ0tFVF9OQU1FOi19XG4gICAgZXhwb3NlOlxuICAgICAgLSAke1BPUlQ6LTgwODB9XG4gICAgdm9sdW1lczpcbiAgICAgIC0gcGF5bG9hZF9pbWFnZXM6L2FwcC9wYXlsb2FkLWZpcmUtaW1hZ2VzXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIHhzc2h1bnRlcmV4cHJlc3MtZGI6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9oZWFsdGh5XG5cbiAgeHNzaHVudGVyZXhwcmVzcy10cnVmZmxlaG9nOlxuICAgIGJ1aWxkOlxuICAgICAgY29udGV4dDogaHR0cHM6Ly9naXRodWIuY29tL3JzLWxvdmVzLWJ1Z3MveHNzaHVudGVyLmdpdFxuICAgICAgZG9ja2VyZmlsZTogRG9ja2VyZmlsZS50cnVmZmxlaG9nXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBleHBvc2U6XG4gICAgICAtICR7VFJVRkZMRUhPR19QT1JUOi04MDAwfVxuXG52b2x1bWVzOlxuICBwb3N0Z3Jlc19kYXRhOlxuICAgIGRyaXZlcjogbG9jYWxcbiAgcGF5bG9hZF9pbWFnZXM6XG4gICAgZHJpdmVyOiBsb2NhbFxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5hZG1pbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG54c3NfZG9tYWluID0gXCIke2RvbWFpbn1cIlxuc2Vzc2lvbl9zZWNyZXQgPSBcIiR7YmFzZTY0OjY0fVwiXG5hZG1pbl9wYXNzd29yZCA9IFwiJHtwYXNzd29yZDozMn1cIlxuZGJfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MTZ9XCJcbnBvc3RncmVzX3VzZXIgPSBcInhzc2h1bnRlcmV4cHJlc3NcIlxucG9zdGdyZXNfZGIgPSBcInhzc2h1bnRlcmV4cHJlc3NcIlxuXG5bY29uZmlnXVxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwieHNzaHVudGVyZXhwcmVzcy1zZXJ2aWNlXCJcbnBvcnQgPSA4MDgwXG5ob3N0ID0gXCIke2FkbWluX2RvbWFpbn1cIlxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJ4c3NodW50ZXJleHByZXNzLXNlcnZpY2VcIlxucG9ydCA9IDgwODBcbmhvc3QgPSBcInhzcy4ke2FkbWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cbiMgQ29yZSBDb25maWd1cmF0aW9uXG5TRVNTSU9OX1NFQ1JFVF9LRVkgPSBcIiR7c2Vzc2lvbl9zZWNyZXR9XCJcbkhPU1ROQU1FID0gXCIke2FkbWluX2RvbWFpbn1cIlxuWFNTX0hPU1ROQU1FID0gXCJ4c3MuJHthZG1pbl9kb21haW59XCJcblxuIyBQYW5lbCBDb25maWd1cmF0aW9uXG5QQU5FTF9MT0dJTiA9IFwidHJ1ZVwiXG5QQU5FTF9VU0VSTkFNRSA9IFwiYWRtaW5AJHthZG1pbl9kb21haW59XCJcblBBTkVMX1BBU1NXT1JEID0gJyR7YWRtaW5fcGFzc3dvcmR9JyAjIFsgdXNlIHNpbmdsZSBxdW90ZSB0byBhdm9pZCB0aGUgcHJvYmxlbV0ganVzdCB0byBsZXQgeW91IGtub3cgdGFrZWNhcmUgb2YgdGhlIHNwZWNpYWwgY2hhcmFjdGVycywgaXQgd2lsbCBtYWtlIHlvdXIgcGFzc3dvcmQgaW52YWxpZCwgc28gbWFrZSBhIHN0cm9uZyBwYXNzd29yZCB3aXRob3V0IHNwZWNpYWwgY2hhcmFjdGVyc1xuQUxMT1dfRU1QVFlfVVNFUlBBVEggPSBcInRydWVcIlxuXG4jIE9BdXRoIENvbmZpZ3VyYXRpb24gKGRpc2FibGVkIGJ5IGRlZmF1bHQpXG5PQVVUSF9MT0dJTiA9IFwiZmFsc2VcIlxuQ0xJRU5UX0lEID0gXCJcIlxuQ0xJRU5UX1NFQ1JFVCA9IFwiXCJcbkdNQUlMX0FDQ09VTlRTID0gXCJcIlxuXG4jIEVtYWlsIENvbmZpZ3VyYXRpb24gKGRpc2FibGVkIGJ5IGRlZmF1bHQpXG5FTUFJTF9OT1RJRklDQVRJT05TX0VOQUJMRUQgPSBcImZhbHNlXCJcbkVNQUlMX0ZST00gPSBcIlwiXG5TRU5ER1JJRF9BUElfS0VZID0gXCJcIlxuU0VOREdSSURfVU5TVUJTUklCRV9HUk9VUF9JRCA9IFwiXCJcblxuIyBEYXRhYmFzZSBDb25maWd1cmF0aW9uXG5EQVRBQkFTRV9IT1NUID0gXCJ4c3NodW50ZXJleHByZXNzLWRiXCJcblBPU1RHUkVTX0RCID0gXCIke3Bvc3RncmVzX2RifVwiXG5QT1NUR1JFU19VU0VSID0gXCIke3Bvc3RncmVzX3VzZXJ9XCJcblBPU1RHUkVTX1BBU1NXT1JEID0gXCIke2RiX3Bhc3N3b3JkfVwiXG5cbiMgQXBwbGljYXRpb24gQ29uZmlndXJhdGlvblxuTk9ERV9FTlYgPSBcInByb2R1Y3Rpb25cIlxuUE9SVCA9IFwiODA4MFwiXG5DT05UUk9MX1BBTkVMX0VOQUJMRUQgPSBcInRydWVcIlxuU0NSRUVOU0hPVFNfRElSID0gXCIvYXBwL3BheWxvYWQtZmlyZS1pbWFnZXNcIlxuVFJVRkZMRUhPR19VUkwgPSBcImh0dHA6Ly8ke1RSVUZGTEVIT0dfSE9TVH06JHtUUlVGRkxFSE9HX1BPUlR9L3RydWZmbGVob2dcIlxuXG4jIFBvcnQgQ29uZmlndXJhdGlvblxuQVBQX1BPUlQgPSBcIjgwODBcIlxuVFJVRkZMRUhPR19IT1NUID0gXCJ4c3NodW50ZXJleHByZXNzLXRydWZmbGVob2dcIlxuVFJVRkZMRUhPR19QT1JUID0gXCI4MDAwXCJcblxuIyBPcHRpb25hbCBTZXJ2aWNlcyAoZGlzYWJsZWQgYnkgZGVmYXVsdClcblNFTlRSWV9EU04gPSBcIlwiXG5TRU5UUllfRU5BQkxFRCA9IFwiZmFsc2VcIlxuVVNFX0NMT1VEX1NUT1JBR0UgPSBcImZhbHNlXCJcbkJVQ0tFVF9OQU1FID0gXCJcIlxuXG5bW2NvbmZpZy5tb3VudHNdXVxuZmlsZVBhdGggPSBcIi4vcGF5bG9hZC1maXJlLWltYWdlc1wiXG5jb250ZW50ID0gXCJEaXJlY3RvcnkgZm9yIHN0b3JpbmcgWFNTIHBheWxvYWQgc2NyZWVuc2hvdHMgYW5kIGNvbGxlY3RlZCBkYXRhXCJcbiIKfQ==
```

## Links

`pentest`,`xsshunter`,`bugbounty`

---

Version:`latest`

WuzAPIA RESTful API service for WhatsApp with multiple device support and concurrent sessions.

YamtrackYamtrack is a self-hosted anime and manga tracker with Redis backend support.

### On this page

ConfigurationBase64LinksTags