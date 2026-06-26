---
title: "Mautic | Dokploy"
source: "https://docs.dokploy.com/docs/templates/mautic"
category: dokploy-docs
created: "2026-06-25T17:21:53.154Z"
---

Mautic | Dokploy

# Mautic

Copy as Markdown

Mautic is the world's largest open-source marketing automation project. It allows you to automate the process of finding and nurturing contacts through landing pages and forms, sending email, text messages, web notifications, and tracking your contacts.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  # -------------------------------------------------------------------------
  # Service 1: Database
  # -------------------------------------------------------------------------
  mysql:
    image: mysql:8.0
    command: --default-authentication-plugin=mysql_native_password
    restart: unless-stopped
    environment:
      MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD}
      MYSQL_DATABASE: ${MAUTIC_DB_DATABASE}
      MYSQL_USER: ${MAUTIC_DB_USER}
      MYSQL_PASSWORD: ${MAUTIC_DB_PASSWORD}
    volumes:
      - mysql_data:/var/lib/mysql
    healthcheck:
      test: ["CMD", "mysqladmin", "ping", "-h", "localhost"]
      interval: 10s
      timeout: 5s
      retries: 5

  # -------------------------------------------------------------------------
  # Service 2: Mautic Web (The Leader)
  # -------------------------------------------------------------------------
  mautic:
    image: mautic/mautic:5.1.1-apache
    restart: unless-stopped
    depends_on:
      mysql:
        condition: service_healthy
    ports:
      - 80
    environment:
      - DOCKER_MAUTIC_ROLE=mautic_web
      - DOCKER_MAUTIC_RUN_MIGRATIONS=true
      - MAUTIC_DB_HOST=${MAUTIC_DB_HOST}
      - MAUTIC_DB_PORT=${MAUTIC_DB_PORT}
      - MAUTIC_DB_DATABASE=${MAUTIC_DB_DATABASE}
      - MAUTIC_DB_USER=${MAUTIC_DB_USER}
      - MAUTIC_DB_PASSWORD=${MAUTIC_DB_PASSWORD}
      - MAUTIC_URL=${MAUTIC_URL}
      - MAUTIC_TRUSTED_PROXIES=${MAUTIC_TRUSTED_PROXIES}
      - MAUTIC_MESSENGER_DSN_EMAIL=${MAUTIC_MESSENGER_DSN_EMAIL}
      - MAUTIC_MESSENGER_DSN_HIT=${MAUTIC_MESSENGER_DSN_HIT}
      - PHP_INI_DATE_TIMEZONE=${PHP_INI_DATE_TIMEZONE}
      - PHP_MEMORY_LIMIT=${PHP_MEMORY_LIMIT}
    volumes:
      - mautic_data:/var/www/html
    # AUTOMATION FIX 1: Force permissions to be correct on every start
    entrypoint: ["/bin/sh", "-c", "chown -R www-data:www-data /var/www/html && /entrypoint.sh apache2-foreground"]
    # AUTOMATION FIX 2: Check if the CONFIG FILE exists. If not, report 'unhealthy'.
    # This signals the other containers to keep waiting.
    healthcheck:
      test: ["CMD-SHELL", "test -f /var/www/html/config/local.php || exit 1"]
      interval: 10s
      timeout: 5s
      retries: 3
      start_period: 300s # Give you 5 mins to run the installer before marking failed

  # -------------------------------------------------------------------------
  # Service 3: Mautic Cron (Waits for Install)
  # -------------------------------------------------------------------------
  mautic-cron:
    image: mautic/mautic:5.1.1-apache
    restart: unless-stopped
    depends_on:
      mautic:
        condition: service_healthy # AUTOMATION FIX 3: Do not start until config file exists
    environment:
      - DOCKER_MAUTIC_ROLE=mautic_cron
      - MAUTIC_DB_HOST=${MAUTIC_DB_HOST}
      - MAUTIC_DB_PORT=${MAUTIC_DB_PORT}
      - MAUTIC_DB_DATABASE=${MAUTIC_DB_DATABASE}
      - MAUTIC_DB_USER=${MAUTIC_DB_USER}
      - MAUTIC_DB_PASSWORD=${MAUTIC_DB_PASSWORD}
      - MAUTIC_URL=${MAUTIC_URL}
      - PHP_INI_DATE_TIMEZONE=${PHP_INI_DATE_TIMEZONE}
    volumes:
      - mautic_data:/var/www/html

  # -------------------------------------------------------------------------
  # Service 4: Mautic Worker (Waits for Install)
  # -------------------------------------------------------------------------
  mautic-worker:
    image: mautic/mautic:5.1.1-apache
    restart: unless-stopped
    depends_on:
      mautic:
        condition: service_healthy # AUTOMATION FIX 3: Do not start until config file exists
    deploy:
      resources:
        limits:
          memory: 512M
    environment:
      - DOCKER_MAUTIC_ROLE=mautic_worker
      - DOCKER_MAUTIC_WORKERS_CONSUME_EMAIL=2
      - DOCKER_MAUTIC_WORKERS_CONSUME_HIT=2
      - DOCKER_MAUTIC_WORKERS_CONSUME_FAILED=2
      - MAUTIC_DB_HOST=${MAUTIC_DB_HOST}
      - MAUTIC_DB_PORT=${MAUTIC_DB_PORT}
      - MAUTIC_DB_DATABASE=${MAUTIC_DB_DATABASE}
      - MAUTIC_DB_USER=${MAUTIC_DB_USER}
      - MAUTIC_DB_PASSWORD=${MAUTIC_DB_PASSWORD}
      - MAUTIC_URL=${MAUTIC_URL}
      - MAUTIC_MESSENGER_DSN_EMAIL=${MAUTIC_MESSENGER_DSN_EMAIL}
      - MAUTIC_MESSENGER_DSN_HIT=${MAUTIC_MESSENGER_DSN_HIT}
      - PHP_INI_DATE_TIMEZONE=${PHP_INI_DATE_TIMEZONE}
    volumes:
      - mautic_data:/var/www/html

  # -------------------------------------------------------------------------
  # Service 5: phpMyAdmin
  # -------------------------------------------------------------------------
  phpmyadmin:
    image: phpmyadmin/phpmyadmin
    restart: unless-stopped
    depends_on:
      mysql:
        condition: service_healthy
    environment:
      PMA_HOST: mysql
      PMA_PORT: 3306
      UPLOAD_LIMIT: 64M
    ports:
      - 80

volumes:
  mysql_data:
  mautic_data:
```

```
[variables]
# Domain 1: For the main Mautic Application
mautic_domain = "${domain}"

# Domain 2: For phpMyAdmin (Database Manager)
pma_domain = "${domain}"

# Security: Random passwords
db_password = "${password:32}"
root_password = "${password:32}"

[config]

# --- Service 1: Mautic Web ---
[[config.domains]]
serviceName = "mautic"
port = 80
host = "${mautic_domain}"
path = "/"

# --- Service 2: phpMyAdmin ---
[[config.domains]]
serviceName = "phpmyadmin"
port = 80
host = "${pma_domain}"
path = "/"

# --- Shared Environment Variables ---
[config.env]

# URL Configuration
MAUTIC_URL = "https://${mautic_domain}"

# Database Connections
MAUTIC_DB_HOST = "mysql"
MAUTIC_DB_PORT = "3306"
MAUTIC_DB_DATABASE = "mautic"
MAUTIC_DB_USER = "mautic"
MAUTIC_DB_PASSWORD = "${db_password}"
MYSQL_ROOT_PASSWORD = "${root_password}"

# Security & Proxy (JSON ARRAY FIXED)
# We use single quotes '...' so TOML treats the inner [...] as a string
MAUTIC_TRUSTED_PROXIES = '["0.0.0.0/0"]'

# Queue Settings
MAUTIC_MESSENGER_DSN_EMAIL = "doctrine://default"
MAUTIC_MESSENGER_DSN_HIT = "doctrine://default"

# PHP Settings
PHP_INI_DATE_TIMEZONE = "UTC"
PHP_MEMORY_LIMIT = "512M"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gICMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuICAjIFNlcnZpY2UgMTogRGF0YWJhc2VcbiAgIyAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG4gIG15c3FsOlxuICAgIGltYWdlOiBteXNxbDo4LjBcbiAgICBjb21tYW5kOiAtLWRlZmF1bHQtYXV0aGVudGljYXRpb24tcGx1Z2luPW15c3FsX25hdGl2ZV9wYXNzd29yZFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBNWVNRTF9ST09UX1BBU1NXT1JEOiAke01ZU1FMX1JPT1RfUEFTU1dPUkR9XG4gICAgICBNWVNRTF9EQVRBQkFTRTogJHtNQVVUSUNfREJfREFUQUJBU0V9XG4gICAgICBNWVNRTF9VU0VSOiAke01BVVRJQ19EQl9VU0VSfVxuICAgICAgTVlTUUxfUEFTU1dPUkQ6ICR7TUFVVElDX0RCX1BBU1NXT1JEfVxuICAgIHZvbHVtZXM6XG4gICAgICAtIG15c3FsX2RhdGE6L3Zhci9saWIvbXlzcWxcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6IFtcIkNNRFwiLCBcIm15c3FsYWRtaW5cIiwgXCJwaW5nXCIsIFwiLWhcIiwgXCJsb2NhbGhvc3RcIl1cbiAgICAgIGludGVydmFsOiAxMHNcbiAgICAgIHRpbWVvdXQ6IDVzXG4gICAgICByZXRyaWVzOiA1XG5cbiAgIyAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG4gICMgU2VydmljZSAyOiBNYXV0aWMgV2ViIChUaGUgTGVhZGVyKVxuICAjIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cbiAgbWF1dGljOlxuICAgIGltYWdlOiBtYXV0aWMvbWF1dGljOjUuMS4xLWFwYWNoZVxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIG15c3FsOlxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2VfaGVhbHRoeVxuICAgIHBvcnRzOlxuICAgICAgLSA4MFxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBET0NLRVJfTUFVVElDX1JPTEU9bWF1dGljX3dlYlxuICAgICAgLSBET0NLRVJfTUFVVElDX1JVTl9NSUdSQVRJT05TPXRydWVcbiAgICAgIC0gTUFVVElDX0RCX0hPU1Q9JHtNQVVUSUNfREJfSE9TVH1cbiAgICAgIC0gTUFVVElDX0RCX1BPUlQ9JHtNQVVUSUNfREJfUE9SVH1cbiAgICAgIC0gTUFVVElDX0RCX0RBVEFCQVNFPSR7TUFVVElDX0RCX0RBVEFCQVNFfVxuICAgICAgLSBNQVVUSUNfREJfVVNFUj0ke01BVVRJQ19EQl9VU0VSfVxuICAgICAgLSBNQVVUSUNfREJfUEFTU1dPUkQ9JHtNQVVUSUNfREJfUEFTU1dPUkR9XG4gICAgICAtIE1BVVRJQ19VUkw9JHtNQVVUSUNfVVJMfVxuICAgICAgLSBNQVVUSUNfVFJVU1RFRF9QUk9YSUVTPSR7TUFVVElDX1RSVVNURURfUFJPWElFU31cbiAgICAgIC0gTUFVVElDX01FU1NFTkdFUl9EU05fRU1BSUw9JHtNQVVUSUNfTUVTU0VOR0VSX0RTTl9FTUFJTH1cbiAgICAgIC0gTUFVVElDX01FU1NFTkdFUl9EU05fSElUPSR7TUFVVElDX01FU1NFTkdFUl9EU05fSElUfVxuICAgICAgLSBQSFBfSU5JX0RBVEVfVElNRVpPTkU9JHtQSFBfSU5JX0RBVEVfVElNRVpPTkV9XG4gICAgICAtIFBIUF9NRU1PUllfTElNSVQ9JHtQSFBfTUVNT1JZX0xJTUlUfVxuICAgIHZvbHVtZXM6XG4gICAgICAtIG1hdXRpY19kYXRhOi92YXIvd3d3L2h0bWxcbiAgICAjIEFVVE9NQVRJT04gRklYIDE6IEZvcmNlIHBlcm1pc3Npb25zIHRvIGJlIGNvcnJlY3Qgb24gZXZlcnkgc3RhcnRcbiAgICBlbnRyeXBvaW50OiBbXCIvYmluL3NoXCIsIFwiLWNcIiwgXCJjaG93biAtUiB3d3ctZGF0YTp3d3ctZGF0YSAvdmFyL3d3dy9odG1sICYmIC9lbnRyeXBvaW50LnNoIGFwYWNoZTItZm9yZWdyb3VuZFwiXVxuICAgICMgQVVUT01BVElPTiBGSVggMjogQ2hlY2sgaWYgdGhlIENPTkZJRyBGSUxFIGV4aXN0cy4gSWYgbm90LCByZXBvcnQgJ3VuaGVhbHRoeScuXG4gICAgIyBUaGlzIHNpZ25hbHMgdGhlIG90aGVyIGNvbnRhaW5lcnMgdG8ga2VlcCB3YWl0aW5nLlxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDogW1wiQ01ELVNIRUxMXCIsIFwidGVzdCAtZiAvdmFyL3d3dy9odG1sL2NvbmZpZy9sb2NhbC5waHAgfHwgZXhpdCAxXCJdXG4gICAgICBpbnRlcnZhbDogMTBzXG4gICAgICB0aW1lb3V0OiA1c1xuICAgICAgcmV0cmllczogM1xuICAgICAgc3RhcnRfcGVyaW9kOiAzMDBzICMgR2l2ZSB5b3UgNSBtaW5zIHRvIHJ1biB0aGUgaW5zdGFsbGVyIGJlZm9yZSBtYXJraW5nIGZhaWxlZFxuXG4gICMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuICAjIFNlcnZpY2UgMzogTWF1dGljIENyb24gKFdhaXRzIGZvciBJbnN0YWxsKVxuICAjIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cbiAgbWF1dGljLWNyb246XG4gICAgaW1hZ2U6IG1hdXRpYy9tYXV0aWM6NS4xLjEtYXBhY2hlXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBkZXBlbmRzX29uOlxuICAgICAgbWF1dGljOlxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2VfaGVhbHRoeSAjIEFVVE9NQVRJT04gRklYIDM6IERvIG5vdCBzdGFydCB1bnRpbCBjb25maWcgZmlsZSBleGlzdHNcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gRE9DS0VSX01BVVRJQ19ST0xFPW1hdXRpY19jcm9uXG4gICAgICAtIE1BVVRJQ19EQl9IT1NUPSR7TUFVVElDX0RCX0hPU1R9XG4gICAgICAtIE1BVVRJQ19EQl9QT1JUPSR7TUFVVElDX0RCX1BPUlR9XG4gICAgICAtIE1BVVRJQ19EQl9EQVRBQkFTRT0ke01BVVRJQ19EQl9EQVRBQkFTRX1cbiAgICAgIC0gTUFVVElDX0RCX1VTRVI9JHtNQVVUSUNfREJfVVNFUn1cbiAgICAgIC0gTUFVVElDX0RCX1BBU1NXT1JEPSR7TUFVVElDX0RCX1BBU1NXT1JEfVxuICAgICAgLSBNQVVUSUNfVVJMPSR7TUFVVElDX1VSTH1cbiAgICAgIC0gUEhQX0lOSV9EQVRFX1RJTUVaT05FPSR7UEhQX0lOSV9EQVRFX1RJTUVaT05FfVxuICAgIHZvbHVtZXM6XG4gICAgICAtIG1hdXRpY19kYXRhOi92YXIvd3d3L2h0bWxcblxuICAjIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cbiAgIyBTZXJ2aWNlIDQ6IE1hdXRpYyBXb3JrZXIgKFdhaXRzIGZvciBJbnN0YWxsKVxuICAjIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cbiAgbWF1dGljLXdvcmtlcjpcbiAgICBpbWFnZTogbWF1dGljL21hdXRpYzo1LjEuMS1hcGFjaGVcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGRlcGVuZHNfb246XG4gICAgICBtYXV0aWM6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9oZWFsdGh5ICMgQVVUT01BVElPTiBGSVggMzogRG8gbm90IHN0YXJ0IHVudGlsIGNvbmZpZyBmaWxlIGV4aXN0c1xuICAgIGRlcGxveTpcbiAgICAgIHJlc291cmNlczpcbiAgICAgICAgbGltaXRzOlxuICAgICAgICAgIG1lbW9yeTogNTEyTVxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBET0NLRVJfTUFVVElDX1JPTEU9bWF1dGljX3dvcmtlclxuICAgICAgLSBET0NLRVJfTUFVVElDX1dPUktFUlNfQ09OU1VNRV9FTUFJTD0yXG4gICAgICAtIERPQ0tFUl9NQVVUSUNfV09SS0VSU19DT05TVU1FX0hJVD0yXG4gICAgICAtIERPQ0tFUl9NQVVUSUNfV09SS0VSU19DT05TVU1FX0ZBSUxFRD0yXG4gICAgICAtIE1BVVRJQ19EQl9IT1NUPSR7TUFVVElDX0RCX0hPU1R9XG4gICAgICAtIE1BVVRJQ19EQl9QT1JUPSR7TUFVVElDX0RCX1BPUlR9XG4gICAgICAtIE1BVVRJQ19EQl9EQVRBQkFTRT0ke01BVVRJQ19EQl9EQVRBQkFTRX1cbiAgICAgIC0gTUFVVElDX0RCX1VTRVI9JHtNQVVUSUNfREJfVVNFUn1cbiAgICAgIC0gTUFVVElDX0RCX1BBU1NXT1JEPSR7TUFVVElDX0RCX1BBU1NXT1JEfVxuICAgICAgLSBNQVVUSUNfVVJMPSR7TUFVVElDX1VSTH1cbiAgICAgIC0gTUFVVElDX01FU1NFTkdFUl9EU05fRU1BSUw9JHtNQVVUSUNfTUVTU0VOR0VSX0RTTl9FTUFJTH1cbiAgICAgIC0gTUFVVElDX01FU1NFTkdFUl9EU05fSElUPSR7TUFVVElDX01FU1NFTkdFUl9EU05fSElUfVxuICAgICAgLSBQSFBfSU5JX0RBVEVfVElNRVpPTkU9JHtQSFBfSU5JX0RBVEVfVElNRVpPTkV9XG4gICAgdm9sdW1lczpcbiAgICAgIC0gbWF1dGljX2RhdGE6L3Zhci93d3cvaHRtbFxuXG4gICMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuICAjIFNlcnZpY2UgNTogcGhwTXlBZG1pblxuICAjIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cbiAgcGhwbXlhZG1pbjpcbiAgICBpbWFnZTogcGhwbXlhZG1pbi9waHBteWFkbWluXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBkZXBlbmRzX29uOlxuICAgICAgbXlzcWw6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9oZWFsdGh5XG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBQTUFfSE9TVDogbXlzcWxcbiAgICAgIFBNQV9QT1JUOiAzMzA2XG4gICAgICBVUExPQURfTElNSVQ6IDY0TVxuICAgIHBvcnRzOlxuICAgICAgLSA4MFxuXG52b2x1bWVzOlxuICBteXNxbF9kYXRhOlxuICBtYXV0aWNfZGF0YTpcbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxuIyBEb21haW4gMTogRm9yIHRoZSBtYWluIE1hdXRpYyBBcHBsaWNhdGlvblxubWF1dGljX2RvbWFpbiA9IFwiJHtkb21haW59XCJcblxuIyBEb21haW4gMjogRm9yIHBocE15QWRtaW4gKERhdGFiYXNlIE1hbmFnZXIpXG5wbWFfZG9tYWluID0gXCIke2RvbWFpbn1cIlxuXG4jIFNlY3VyaXR5OiBSYW5kb20gcGFzc3dvcmRzXG5kYl9wYXNzd29yZCA9IFwiJHtwYXNzd29yZDozMn1cIlxucm9vdF9wYXNzd29yZCA9IFwiJHtwYXNzd29yZDozMn1cIlxuXG5bY29uZmlnXVxuXG4jIC0tLSBTZXJ2aWNlIDE6IE1hdXRpYyBXZWIgLS0tXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJtYXV0aWNcIlxucG9ydCA9IDgwXG5ob3N0ID0gXCIke21hdXRpY19kb21haW59XCJcbnBhdGggPSBcIi9cIlxuXG4jIC0tLSBTZXJ2aWNlIDI6IHBocE15QWRtaW4gLS0tXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJwaHBteWFkbWluXCJcbnBvcnQgPSA4MFxuaG9zdCA9IFwiJHtwbWFfZG9tYWlufVwiXG5wYXRoID0gXCIvXCJcblxuIyAtLS0gU2hhcmVkIEVudmlyb25tZW50IFZhcmlhYmxlcyAtLS1cbltjb25maWcuZW52XVxuXG4jIFVSTCBDb25maWd1cmF0aW9uXG5NQVVUSUNfVVJMID0gXCJodHRwczovLyR7bWF1dGljX2RvbWFpbn1cIlxuXG4jIERhdGFiYXNlIENvbm5lY3Rpb25zXG5NQVVUSUNfREJfSE9TVCA9IFwibXlzcWxcIlxuTUFVVElDX0RCX1BPUlQgPSBcIjMzMDZcIlxuTUFVVElDX0RCX0RBVEFCQVNFID0gXCJtYXV0aWNcIlxuTUFVVElDX0RCX1VTRVIgPSBcIm1hdXRpY1wiXG5NQVVUSUNfREJfUEFTU1dPUkQgPSBcIiR7ZGJfcGFzc3dvcmR9XCJcbk1ZU1FMX1JPT1RfUEFTU1dPUkQgPSBcIiR7cm9vdF9wYXNzd29yZH1cIlxuXG4jIFNlY3VyaXR5ICYgUHJveHkgKEpTT04gQVJSQVkgRklYRUQpXG4jIFdlIHVzZSBzaW5nbGUgcXVvdGVzICcuLi4nIHNvIFRPTUwgdHJlYXRzIHRoZSBpbm5lciBbLi4uXSBhcyBhIHN0cmluZ1xuTUFVVElDX1RSVVNURURfUFJPWElFUyA9ICdbXCIwLjAuMC4wLzBcIl0nXG5cbiMgUXVldWUgU2V0dGluZ3Ncbk1BVVRJQ19NRVNTRU5HRVJfRFNOX0VNQUlMID0gXCJkb2N0cmluZTovL2RlZmF1bHRcIlxuTUFVVElDX01FU1NFTkdFUl9EU05fSElUID0gXCJkb2N0cmluZTovL2RlZmF1bHRcIlxuXG4jIFBIUCBTZXR0aW5nc1xuUEhQX0lOSV9EQVRFX1RJTUVaT05FID0gXCJVVENcIlxuUEhQX01FTU9SWV9MSU1JVCA9IFwiNTEyTVwiIgp9
```

## Links

`marketing`,`automation`,`email`,`crm`

---

Version:`5.1.1`

MattermostA single point of collaboration. Designed specifically for digital operations.

MaybeMaybe is a self-hosted finance tracking application designed to simplify budgeting and expenses.

### On this page

ConfigurationBase64LinksTags