---
title: "BigCapital | Dokploy"
source: "https://docs.dokploy.com/docs/templates/bigcapital"
category: dokploy-docs
created: "2026-06-25T17:21:42.676Z"
---

BigCapital | Dokploy

# BigCapital

Copy as Markdown

BigCapital is a great open source alternative to QuickBooks. A comprehensive accounting and financial management system for businesses.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  webapp:
    image: bigcapitalhq/webapp:latest
    restart: unless-stopped
    depends_on:
      - server
    ports:
      - '80'

  server:
    image: bigcapitalhq/server:latest
    restart: unless-stopped
    depends_on:
      mysql:
        condition: service_healthy
      mongo:
        condition: service_started
      redis:
        condition: service_started
    ports:
      - '3000'

    environment:
      # Mail
      - MAIL_HOST=${MAIL_HOST}
      - MAIL_USERNAME=${MAIL_USERNAME}
      - MAIL_PASSWORD=${MAIL_PASSWORD}
      - MAIL_PORT=${MAIL_PORT}
      - MAIL_SECURE=${MAIL_SECURE}
      - MAIL_FROM_NAME=${MAIL_FROM_NAME}
      - MAIL_FROM_ADDRESS=${MAIL_FROM_ADDRESS}
      # Database
      - DB_HOST=mysql
      - DB_USER=${DB_USER}
      - DB_PASSWORD=${DB_PASSWORD}
      - DB_CHARSET=${DB_CHARSET}
      # System database
      - SYSTEM_DB_NAME=${SYSTEM_DB_NAME}
      # Tenants databases
      - TENANT_DB_NAME_PERFIX=${TENANT_DB_NAME_PERFIX}
      # Authentication
      - JWT_SECRET=${JWT_SECRET}
      # MongoDB
      - MONGODB_DATABASE_URL=mongodb://mongo/bigcapital
      # Application
      - BASE_URL=${BASE_URL}
      # Agendash
      - AGENDASH_AUTH_USER=${AGENDASH_AUTH_USER}
      - AGENDASH_AUTH_PASSWORD=${AGENDASH_AUTH_PASSWORD}
      # Sign-up restrictions
      - SIGNUP_DISABLED=${SIGNUP_DISABLED}
      - SIGNUP_ALLOWED_DOMAINS=${SIGNUP_ALLOWED_DOMAINS}
      - SIGNUP_ALLOWED_EMAILS=${SIGNUP_ALLOWED_EMAILS}
      # Sign-up email confirmation
      - SIGNUP_EMAIL_CONFIRMATION=${SIGNUP_EMAIL_CONFIRMATION}
      # Gotenberg (Pdf generator)
      - GOTENBERG_URL=${GOTENBERG_URL}
      - GOTENBERG_DOCS_URL=${GOTENBERG_DOCS_URL}
      # Exchange Rate
      - EXCHANGE_RATE_SERVICE=${EXCHANGE_RATE_SERVICE}
      - OPEN_EXCHANGE_RATE_APP_ID=${OPEN_EXCHANGE_RATE_APP_ID}
      # Bank Sync
      - BANKING_CONNECT=${BANKING_CONNECT}
      # Plaid
      - PLAID_ENV=${PLAID_ENV}
      - PLAID_CLIENT_ID=${PLAID_CLIENT_ID}
      - PLAID_SECRET=${PLAID_SECRET}
      - PLAID_LINK_WEBHOOK=${PLAID_LINK_WEBHOOK}
      # Lemon Squeez
      - LEMONSQUEEZY_API_KEY=${LEMONSQUEEZY_API_KEY}
      - LEMONSQUEEZY_STORE_ID=${LEMONSQUEEZY_STORE_ID}
      - LEMONSQUEEZY_WEBHOOK_SECRET=${LEMONSQUEEZY_WEBHOOK_SECRET}
      - HOSTED_ON_BIGCAPITAL_CLOUD=${HOSTED_ON_BIGCAPITAL_CLOUD}
      # New Relic metrics tracking
      - NEW_RELIC_DISTRIBUTED_TRACING_ENABLED=${NEW_RELIC_DISTRIBUTED_TRACING_ENABLED}
      - NEW_RELIC_LOG=${NEW_RELIC_LOG}
      - NEW_RELIC_AI_MONITORING_ENABLED=${NEW_RELIC_AI_MONITORING_ENABLED}
      - NEW_RELIC_CUSTOM_INSIGHTS_EVENTS_MAX_SAMPLES_STORED=${NEW_RELIC_CUSTOM_INSIGHTS_EVENTS_MAX_SAMPLES_STORED}
      - NEW_RELIC_SPAN_EVENTS_MAX_SAMPLES_STORED=${NEW_RELIC_SPAN_EVENTS_MAX_SAMPLES_STORED}
      - NEW_RELIC_LICENSE_KEY=${NEW_RELIC_LICENSE_KEY}
      - NEW_RELIC_APP_NAME=${NEW_RELIC_APP_NAME}
      # S3
      - S3_REGION=${S3_REGION}
      - S3_ACCESS_KEY_ID=${S3_ACCESS_KEY_ID}
      - S3_SECRET_ACCESS_KEY=${S3_SECRET_ACCESS_KEY}
      - S3_ENDPOINT=${S3_ENDPOINT}
      - S3_BUCKET=${S3_BUCKET}

  mysql:
    image: mariadb:10.11
    restart: unless-stopped
    environment:
      - MYSQL_DATABASE=${SYSTEM_DB_NAME}
      - MYSQL_USER=${DB_USER}
      - MYSQL_PASSWORD=${DB_PASSWORD}
      - MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD}
    volumes:
      - mysql:/var/lib/mysql
    ports:
      - '3306'

    healthcheck:
      test: ["CMD-SHELL", "mysqladmin ping -h localhost -u root -p$$MYSQL_ROOT_PASSWORD || exit 1"]
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 30s

  mongo:
    image: mongo:7
    restart: unless-stopped
    ports:
      - '27017'
    volumes:
      - mongo:/data/db

  redis:
    image: redis:7-alpine
    restart: unless-stopped
    ports:
      - '6379'
    volumes:
      - redis:/data

    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5

  gotenberg:
    image: gotenberg/gotenberg:7
    restart: unless-stopped
    ports:
      - '9000'

volumes:
  mysql:
    name: bigcapital_mysql
    driver: local
  mongo:
    name: bigcapital_mongo
    driver: local
  redis:
    name: bigcapital_redis
    driver: local
```

```
[variables]
main_domain = "${domain}"
base_url = "https://${main_domain}"

# Database configuration
db_user = "bigcapital"
db_password = "${password:32}"
db_root_password = "${password:32}"
db_charset = "utf8mb4"
system_db_name = "bigcapital"
tenant_db_name_prefix = "bigcapital_tenant_"

# JWT Secret
jwt_secret = "${hash:64}"

# Mail configuration (optional - can be left empty)
mail_host = ""
mail_username = ""
mail_password = ""
mail_port = "587"
mail_secure = "false"
mail_from_name = "BigCapital"
mail_from_address = "noreply@${main_domain}"

# Agendash authentication
agendash_auth_user = "admin"
agendash_auth_password = "${password:24}"

# Sign-up configuration
signup_disabled = "false"
signup_allowed_domains = ""
signup_allowed_emails = ""
signup_email_confirmation = "false"

# Gotenberg configuration
gotenberg_url = "http://gotenberg:9000"
gotenberg_docs_url = "http://gotenberg:9000"

# Exchange Rate Service
exchange_rate_service = "openexchangerates"
open_exchange_rate_app_id = ""

# Banking Connect
banking_connect = "false"

# Plaid configuration (optional)
plaid_env = "sandbox"
plaid_client_id = ""
plaid_secret = ""
plaid_link_webhook = ""

# Lemon Squeezy configuration (optional)
lemonsqueezy_api_key = ""
lemonsqueezy_store_id = ""
lemonsqueezy_webhook_secret = ""
hosted_on_bigcapital_cloud = "false"

# New Relic configuration (optional)
new_relic_distributed_tracing_enabled = "false"
new_relic_log = "false"
new_relic_ai_monitoring_enabled = "false"
new_relic_custom_insights_events_max_samples_stored = "10000"
new_relic_span_events_max_samples_stored = "10000"
new_relic_license_key = ""
new_relic_app_name = "BigCapital"

# S3 configuration (optional)
s3_region = ""
s3_access_key_id = ""
s3_secret_access_key = ""
s3_endpoint = ""
s3_bucket = ""

[config]

[[config.domains]]
serviceName = "webapp"
port = 80
host = "${main_domain}"

[config.env]
# Mail
MAIL_HOST = "${mail_host}"
MAIL_USERNAME = "${mail_username}"
MAIL_PASSWORD = "${mail_password}"
MAIL_PORT = "${mail_port}"
MAIL_SECURE = "${mail_secure}"
MAIL_FROM_NAME = "${mail_from_name}"
MAIL_FROM_ADDRESS = "${mail_from_address}"

# Database
DB_HOST = "mysql"
DB_USER = "${db_user}"
DB_PASSWORD = "${db_password}"
DB_CHARSET = "${db_charset}"

# System database
SYSTEM_DB_NAME = "${system_db_name}"

# Tenants databases
TENANT_DB_NAME_PERFIX = "${tenant_db_name_prefix}"

# Authentication
JWT_SECRET = "${jwt_secret}"

# MongoDB
MONGODB_DATABASE_URL = "mongodb://mongo/bigcapital"

# Application
BASE_URL = "${base_url}"

# Agendash
AGENDASH_AUTH_USER = "${agendash_auth_user}"
AGENDASH_AUTH_PASSWORD = "${agendash_auth_password}"

# Sign-up restrictions
SIGNUP_DISABLED = "${signup_disabled}"
SIGNUP_ALLOWED_DOMAINS = "${signup_allowed_domains}"
SIGNUP_ALLOWED_EMAILS = "${signup_allowed_emails}"

# Sign-up email confirmation
SIGNUP_EMAIL_CONFIRMATION = "${signup_email_confirmation}"

# Gotenberg (Pdf generator)
GOTENBERG_URL = "${gotenberg_url}"
GOTENBERG_DOCS_URL = "${gotenberg_docs_url}"

# Exchange Rate
EXCHANGE_RATE_SERVICE = "${exchange_rate_service}"
OPEN_EXCHANGE_RATE_APP_ID = "${open_exchange_rate_app_id}"

# Bank Sync
BANKING_CONNECT = "${banking_connect}"

# Plaid
PLAID_ENV = "${plaid_env}"
PLAID_CLIENT_ID = "${plaid_client_id}"
PLAID_SECRET = "${plaid_secret}"
PLAID_LINK_WEBHOOK = "${plaid_link_webhook}"

# Lemon Squeez
LEMONSQUEEZY_API_KEY = "${lemonsqueezy_api_key}"
LEMONSQUEEZY_STORE_ID = "${lemonsqueezy_store_id}"
LEMONSQUEEZY_WEBHOOK_SECRET = "${lemonsqueezy_webhook_secret}"
HOSTED_ON_BIGCAPITAL_CLOUD = "${hosted_on_bigcapital_cloud}"

# New Relic metrics tracking
NEW_RELIC_DISTRIBUTED_TRACING_ENABLED = "${new_relic_distributed_tracing_enabled}"
NEW_RELIC_LOG = "${new_relic_log}"
NEW_RELIC_AI_MONITORING_ENABLED = "${new_relic_ai_monitoring_enabled}"
NEW_RELIC_CUSTOM_INSIGHTS_EVENTS_MAX_SAMPLES_STORED = "${new_relic_custom_insights_events_max_samples_stored}"
NEW_RELIC_SPAN_EVENTS_MAX_SAMPLES_STORED = "${new_relic_span_events_max_samples_stored}"
NEW_RELIC_LICENSE_KEY = "${new_relic_license_key}"
NEW_RELIC_APP_NAME = "${new_relic_app_name}"

# S3
S3_REGION = "${s3_region}"
S3_ACCESS_KEY_ID = "${s3_access_key_id}"
S3_SECRET_ACCESS_KEY = "${s3_secret_access_key}"
S3_ENDPOINT = "${s3_endpoint}"
S3_BUCKET = "${s3_bucket}"

# MySQL
MYSQL_DATABASE = "${system_db_name}"
MYSQL_USER = "${db_user}"
MYSQL_PASSWORD = "${db_password}"
MYSQL_ROOT_PASSWORD = "${db_root_password}"

[[config.mounts]]
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICB3ZWJhcHA6XG4gICAgaW1hZ2U6IGJpZ2NhcGl0YWxocS93ZWJhcHA6bGF0ZXN0XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBkZXBlbmRzX29uOlxuICAgICAgLSBzZXJ2ZXJcbiAgICBwb3J0czpcbiAgICAgIC0gJzgwJ1xuXG5cbiAgc2VydmVyOlxuICAgIGltYWdlOiBiaWdjYXBpdGFsaHEvc2VydmVyOmxhdGVzdFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIG15c3FsOlxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2VfaGVhbHRoeVxuICAgICAgbW9uZ286XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9zdGFydGVkXG4gICAgICByZWRpczpcbiAgICAgICAgY29uZGl0aW9uOiBzZXJ2aWNlX3N0YXJ0ZWRcbiAgICBwb3J0czpcbiAgICAgIC0gJzMwMDAnXG5cbiAgICBlbnZpcm9ubWVudDpcbiAgICAgICMgTWFpbFxuICAgICAgLSBNQUlMX0hPU1Q9JHtNQUlMX0hPU1R9XG4gICAgICAtIE1BSUxfVVNFUk5BTUU9JHtNQUlMX1VTRVJOQU1FfVxuICAgICAgLSBNQUlMX1BBU1NXT1JEPSR7TUFJTF9QQVNTV09SRH1cbiAgICAgIC0gTUFJTF9QT1JUPSR7TUFJTF9QT1JUfVxuICAgICAgLSBNQUlMX1NFQ1VSRT0ke01BSUxfU0VDVVJFfVxuICAgICAgLSBNQUlMX0ZST01fTkFNRT0ke01BSUxfRlJPTV9OQU1FfVxuICAgICAgLSBNQUlMX0ZST01fQUREUkVTUz0ke01BSUxfRlJPTV9BRERSRVNTfVxuICAgICAgIyBEYXRhYmFzZVxuICAgICAgLSBEQl9IT1NUPW15c3FsXG4gICAgICAtIERCX1VTRVI9JHtEQl9VU0VSfVxuICAgICAgLSBEQl9QQVNTV09SRD0ke0RCX1BBU1NXT1JEfVxuICAgICAgLSBEQl9DSEFSU0VUPSR7REJfQ0hBUlNFVH1cbiAgICAgICMgU3lzdGVtIGRhdGFiYXNlXG4gICAgICAtIFNZU1RFTV9EQl9OQU1FPSR7U1lTVEVNX0RCX05BTUV9XG4gICAgICAjIFRlbmFudHMgZGF0YWJhc2VzXG4gICAgICAtIFRFTkFOVF9EQl9OQU1FX1BFUkZJWD0ke1RFTkFOVF9EQl9OQU1FX1BFUkZJWH1cbiAgICAgICMgQXV0aGVudGljYXRpb25cbiAgICAgIC0gSldUX1NFQ1JFVD0ke0pXVF9TRUNSRVR9XG4gICAgICAjIE1vbmdvREJcbiAgICAgIC0gTU9OR09EQl9EQVRBQkFTRV9VUkw9bW9uZ29kYjovL21vbmdvL2JpZ2NhcGl0YWxcbiAgICAgICMgQXBwbGljYXRpb25cbiAgICAgIC0gQkFTRV9VUkw9JHtCQVNFX1VSTH1cbiAgICAgICMgQWdlbmRhc2hcbiAgICAgIC0gQUdFTkRBU0hfQVVUSF9VU0VSPSR7QUdFTkRBU0hfQVVUSF9VU0VSfVxuICAgICAgLSBBR0VOREFTSF9BVVRIX1BBU1NXT1JEPSR7QUdFTkRBU0hfQVVUSF9QQVNTV09SRH1cbiAgICAgICMgU2lnbi11cCByZXN0cmljdGlvbnNcbiAgICAgIC0gU0lHTlVQX0RJU0FCTEVEPSR7U0lHTlVQX0RJU0FCTEVEfVxuICAgICAgLSBTSUdOVVBfQUxMT1dFRF9ET01BSU5TPSR7U0lHTlVQX0FMTE9XRURfRE9NQUlOU31cbiAgICAgIC0gU0lHTlVQX0FMTE9XRURfRU1BSUxTPSR7U0lHTlVQX0FMTE9XRURfRU1BSUxTfVxuICAgICAgIyBTaWduLXVwIGVtYWlsIGNvbmZpcm1hdGlvblxuICAgICAgLSBTSUdOVVBfRU1BSUxfQ09ORklSTUFUSU9OPSR7U0lHTlVQX0VNQUlMX0NPTkZJUk1BVElPTn1cbiAgICAgICMgR290ZW5iZXJnIChQZGYgZ2VuZXJhdG9yKVxuICAgICAgLSBHT1RFTkJFUkdfVVJMPSR7R09URU5CRVJHX1VSTH1cbiAgICAgIC0gR09URU5CRVJHX0RPQ1NfVVJMPSR7R09URU5CRVJHX0RPQ1NfVVJMfVxuICAgICAgIyBFeGNoYW5nZSBSYXRlXG4gICAgICAtIEVYQ0hBTkdFX1JBVEVfU0VSVklDRT0ke0VYQ0hBTkdFX1JBVEVfU0VSVklDRX1cbiAgICAgIC0gT1BFTl9FWENIQU5HRV9SQVRFX0FQUF9JRD0ke09QRU5fRVhDSEFOR0VfUkFURV9BUFBfSUR9XG4gICAgICAjIEJhbmsgU3luY1xuICAgICAgLSBCQU5LSU5HX0NPTk5FQ1Q9JHtCQU5LSU5HX0NPTk5FQ1R9XG4gICAgICAjIFBsYWlkXG4gICAgICAtIFBMQUlEX0VOVj0ke1BMQUlEX0VOVn1cbiAgICAgIC0gUExBSURfQ0xJRU5UX0lEPSR7UExBSURfQ0xJRU5UX0lEfVxuICAgICAgLSBQTEFJRF9TRUNSRVQ9JHtQTEFJRF9TRUNSRVR9XG4gICAgICAtIFBMQUlEX0xJTktfV0VCSE9PSz0ke1BMQUlEX0xJTktfV0VCSE9PS31cbiAgICAgICMgTGVtb24gU3F1ZWV6XG4gICAgICAtIExFTU9OU1FVRUVaWV9BUElfS0VZPSR7TEVNT05TUVVFRVpZX0FQSV9LRVl9XG4gICAgICAtIExFTU9OU1FVRUVaWV9TVE9SRV9JRD0ke0xFTU9OU1FVRUVaWV9TVE9SRV9JRH1cbiAgICAgIC0gTEVNT05TUVVFRVpZX1dFQkhPT0tfU0VDUkVUPSR7TEVNT05TUVVFRVpZX1dFQkhPT0tfU0VDUkVUfVxuICAgICAgLSBIT1NURURfT05fQklHQ0FQSVRBTF9DTE9VRD0ke0hPU1RFRF9PTl9CSUdDQVBJVEFMX0NMT1VEfVxuICAgICAgIyBOZXcgUmVsaWMgbWV0cmljcyB0cmFja2luZ1xuICAgICAgLSBORVdfUkVMSUNfRElTVFJJQlVURURfVFJBQ0lOR19FTkFCTEVEPSR7TkVXX1JFTElDX0RJU1RSSUJVVEVEX1RSQUNJTkdfRU5BQkxFRH1cbiAgICAgIC0gTkVXX1JFTElDX0xPRz0ke05FV19SRUxJQ19MT0d9XG4gICAgICAtIE5FV19SRUxJQ19BSV9NT05JVE9SSU5HX0VOQUJMRUQ9JHtORVdfUkVMSUNfQUlfTU9OSVRPUklOR19FTkFCTEVEfVxuICAgICAgLSBORVdfUkVMSUNfQ1VTVE9NX0lOU0lHSFRTX0VWRU5UU19NQVhfU0FNUExFU19TVE9SRUQ9JHtORVdfUkVMSUNfQ1VTVE9NX0lOU0lHSFRTX0VWRU5UU19NQVhfU0FNUExFU19TVE9SRUR9XG4gICAgICAtIE5FV19SRUxJQ19TUEFOX0VWRU5UU19NQVhfU0FNUExFU19TVE9SRUQ9JHtORVdfUkVMSUNfU1BBTl9FVkVOVFNfTUFYX1NBTVBMRVNfU1RPUkVEfVxuICAgICAgLSBORVdfUkVMSUNfTElDRU5TRV9LRVk9JHtORVdfUkVMSUNfTElDRU5TRV9LRVl9XG4gICAgICAtIE5FV19SRUxJQ19BUFBfTkFNRT0ke05FV19SRUxJQ19BUFBfTkFNRX1cbiAgICAgICMgUzNcbiAgICAgIC0gUzNfUkVHSU9OPSR7UzNfUkVHSU9OfVxuICAgICAgLSBTM19BQ0NFU1NfS0VZX0lEPSR7UzNfQUNDRVNTX0tFWV9JRH1cbiAgICAgIC0gUzNfU0VDUkVUX0FDQ0VTU19LRVk9JHtTM19TRUNSRVRfQUNDRVNTX0tFWX1cbiAgICAgIC0gUzNfRU5EUE9JTlQ9JHtTM19FTkRQT0lOVH1cbiAgICAgIC0gUzNfQlVDS0VUPSR7UzNfQlVDS0VUfVxuXG4gIG15c3FsOlxuICAgIGltYWdlOiBtYXJpYWRiOjEwLjExXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gTVlTUUxfREFUQUJBU0U9JHtTWVNURU1fREJfTkFNRX1cbiAgICAgIC0gTVlTUUxfVVNFUj0ke0RCX1VTRVJ9XG4gICAgICAtIE1ZU1FMX1BBU1NXT1JEPSR7REJfUEFTU1dPUkR9XG4gICAgICAtIE1ZU1FMX1JPT1RfUEFTU1dPUkQ9JHtNWVNRTF9ST09UX1BBU1NXT1JEfVxuICAgIHZvbHVtZXM6XG4gICAgICAtIG15c3FsOi92YXIvbGliL215c3FsXG4gICAgcG9ydHM6XG4gICAgICAtICczMzA2J1xuXG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OiBbXCJDTUQtU0hFTExcIiwgXCJteXNxbGFkbWluIHBpbmcgLWggbG9jYWxob3N0IC11IHJvb3QgLXAkJE1ZU1FMX1JPT1RfUEFTU1dPUkQgfHwgZXhpdCAxXCJdXG4gICAgICBpbnRlcnZhbDogMTBzXG4gICAgICB0aW1lb3V0OiA1c1xuICAgICAgcmV0cmllczogNVxuICAgICAgc3RhcnRfcGVyaW9kOiAzMHNcblxuICBtb25nbzpcbiAgICBpbWFnZTogbW9uZ286N1xuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgcG9ydHM6XG4gICAgICAtICcyNzAxNydcbiAgICB2b2x1bWVzOlxuICAgICAgLSBtb25nbzovZGF0YS9kYlxuXG5cbiAgcmVkaXM6XG4gICAgaW1hZ2U6IHJlZGlzOjctYWxwaW5lXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBwb3J0czpcbiAgICAgIC0gJzYzNzknXG4gICAgdm9sdW1lczpcbiAgICAgIC0gcmVkaXM6L2RhdGFcblxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDogW1wiQ01EXCIsIFwicmVkaXMtY2xpXCIsIFwicGluZ1wiXVxuICAgICAgaW50ZXJ2YWw6IDEwc1xuICAgICAgdGltZW91dDogNXNcbiAgICAgIHJldHJpZXM6IDVcblxuICBnb3RlbmJlcmc6XG4gICAgaW1hZ2U6IGdvdGVuYmVyZy9nb3RlbmJlcmc6N1xuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgcG9ydHM6XG4gICAgICAtICc5MDAwJ1xuXG5cbnZvbHVtZXM6XG4gIG15c3FsOlxuICAgIG5hbWU6IGJpZ2NhcGl0YWxfbXlzcWxcbiAgICBkcml2ZXI6IGxvY2FsXG4gIG1vbmdvOlxuICAgIG5hbWU6IGJpZ2NhcGl0YWxfbW9uZ29cbiAgICBkcml2ZXI6IGxvY2FsXG4gIHJlZGlzOlxuICAgIG5hbWU6IGJpZ2NhcGl0YWxfcmVkaXNcbiAgICBkcml2ZXI6IGxvY2FsXG5cblxuXG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuYmFzZV91cmwgPSBcImh0dHBzOi8vJHttYWluX2RvbWFpbn1cIlxuXG4jIERhdGFiYXNlIGNvbmZpZ3VyYXRpb25cbmRiX3VzZXIgPSBcImJpZ2NhcGl0YWxcIlxuZGJfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcbmRiX3Jvb3RfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcbmRiX2NoYXJzZXQgPSBcInV0ZjhtYjRcIlxuc3lzdGVtX2RiX25hbWUgPSBcImJpZ2NhcGl0YWxcIlxudGVuYW50X2RiX25hbWVfcHJlZml4ID0gXCJiaWdjYXBpdGFsX3RlbmFudF9cIlxuXG4jIEpXVCBTZWNyZXRcbmp3dF9zZWNyZXQgPSBcIiR7aGFzaDo2NH1cIlxuXG4jIE1haWwgY29uZmlndXJhdGlvbiAob3B0aW9uYWwgLSBjYW4gYmUgbGVmdCBlbXB0eSlcbm1haWxfaG9zdCA9IFwiXCJcbm1haWxfdXNlcm5hbWUgPSBcIlwiXG5tYWlsX3Bhc3N3b3JkID0gXCJcIlxubWFpbF9wb3J0ID0gXCI1ODdcIlxubWFpbF9zZWN1cmUgPSBcImZhbHNlXCJcbm1haWxfZnJvbV9uYW1lID0gXCJCaWdDYXBpdGFsXCJcbm1haWxfZnJvbV9hZGRyZXNzID0gXCJub3JlcGx5QCR7bWFpbl9kb21haW59XCJcblxuIyBBZ2VuZGFzaCBhdXRoZW50aWNhdGlvblxuYWdlbmRhc2hfYXV0aF91c2VyID0gXCJhZG1pblwiXG5hZ2VuZGFzaF9hdXRoX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkOjI0fVwiXG5cbiMgU2lnbi11cCBjb25maWd1cmF0aW9uXG5zaWdudXBfZGlzYWJsZWQgPSBcImZhbHNlXCJcbnNpZ251cF9hbGxvd2VkX2RvbWFpbnMgPSBcIlwiXG5zaWdudXBfYWxsb3dlZF9lbWFpbHMgPSBcIlwiXG5zaWdudXBfZW1haWxfY29uZmlybWF0aW9uID0gXCJmYWxzZVwiXG5cbiMgR290ZW5iZXJnIGNvbmZpZ3VyYXRpb25cbmdvdGVuYmVyZ191cmwgPSBcImh0dHA6Ly9nb3RlbmJlcmc6OTAwMFwiXG5nb3RlbmJlcmdfZG9jc191cmwgPSBcImh0dHA6Ly9nb3RlbmJlcmc6OTAwMFwiXG5cbiMgRXhjaGFuZ2UgUmF0ZSBTZXJ2aWNlXG5leGNoYW5nZV9yYXRlX3NlcnZpY2UgPSBcIm9wZW5leGNoYW5nZXJhdGVzXCJcbm9wZW5fZXhjaGFuZ2VfcmF0ZV9hcHBfaWQgPSBcIlwiXG5cbiMgQmFua2luZyBDb25uZWN0XG5iYW5raW5nX2Nvbm5lY3QgPSBcImZhbHNlXCJcblxuIyBQbGFpZCBjb25maWd1cmF0aW9uIChvcHRpb25hbClcbnBsYWlkX2VudiA9IFwic2FuZGJveFwiXG5wbGFpZF9jbGllbnRfaWQgPSBcIlwiXG5wbGFpZF9zZWNyZXQgPSBcIlwiXG5wbGFpZF9saW5rX3dlYmhvb2sgPSBcIlwiXG5cbiMgTGVtb24gU3F1ZWV6eSBjb25maWd1cmF0aW9uIChvcHRpb25hbClcbmxlbW9uc3F1ZWV6eV9hcGlfa2V5ID0gXCJcIlxubGVtb25zcXVlZXp5X3N0b3JlX2lkID0gXCJcIlxubGVtb25zcXVlZXp5X3dlYmhvb2tfc2VjcmV0ID0gXCJcIlxuaG9zdGVkX29uX2JpZ2NhcGl0YWxfY2xvdWQgPSBcImZhbHNlXCJcblxuIyBOZXcgUmVsaWMgY29uZmlndXJhdGlvbiAob3B0aW9uYWwpXG5uZXdfcmVsaWNfZGlzdHJpYnV0ZWRfdHJhY2luZ19lbmFibGVkID0gXCJmYWxzZVwiXG5uZXdfcmVsaWNfbG9nID0gXCJmYWxzZVwiXG5uZXdfcmVsaWNfYWlfbW9uaXRvcmluZ19lbmFibGVkID0gXCJmYWxzZVwiXG5uZXdfcmVsaWNfY3VzdG9tX2luc2lnaHRzX2V2ZW50c19tYXhfc2FtcGxlc19zdG9yZWQgPSBcIjEwMDAwXCJcbm5ld19yZWxpY19zcGFuX2V2ZW50c19tYXhfc2FtcGxlc19zdG9yZWQgPSBcIjEwMDAwXCJcbm5ld19yZWxpY19saWNlbnNlX2tleSA9IFwiXCJcbm5ld19yZWxpY19hcHBfbmFtZSA9IFwiQmlnQ2FwaXRhbFwiXG5cbiMgUzMgY29uZmlndXJhdGlvbiAob3B0aW9uYWwpXG5zM19yZWdpb24gPSBcIlwiXG5zM19hY2Nlc3Nfa2V5X2lkID0gXCJcIlxuczNfc2VjcmV0X2FjY2Vzc19rZXkgPSBcIlwiXG5zM19lbmRwb2ludCA9IFwiXCJcbnMzX2J1Y2tldCA9IFwiXCJcblxuW2NvbmZpZ11cblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwid2ViYXBwXCJcbnBvcnQgPSA4MFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cbiMgTWFpbFxuTUFJTF9IT1NUID0gXCIke21haWxfaG9zdH1cIlxuTUFJTF9VU0VSTkFNRSA9IFwiJHttYWlsX3VzZXJuYW1lfVwiXG5NQUlMX1BBU1NXT1JEID0gXCIke21haWxfcGFzc3dvcmR9XCJcbk1BSUxfUE9SVCA9IFwiJHttYWlsX3BvcnR9XCJcbk1BSUxfU0VDVVJFID0gXCIke21haWxfc2VjdXJlfVwiXG5NQUlMX0ZST01fTkFNRSA9IFwiJHttYWlsX2Zyb21fbmFtZX1cIlxuTUFJTF9GUk9NX0FERFJFU1MgPSBcIiR7bWFpbF9mcm9tX2FkZHJlc3N9XCJcblxuIyBEYXRhYmFzZVxuREJfSE9TVCA9IFwibXlzcWxcIlxuREJfVVNFUiA9IFwiJHtkYl91c2VyfVwiXG5EQl9QQVNTV09SRCA9IFwiJHtkYl9wYXNzd29yZH1cIlxuREJfQ0hBUlNFVCA9IFwiJHtkYl9jaGFyc2V0fVwiXG5cbiMgU3lzdGVtIGRhdGFiYXNlXG5TWVNURU1fREJfTkFNRSA9IFwiJHtzeXN0ZW1fZGJfbmFtZX1cIlxuXG4jIFRlbmFudHMgZGF0YWJhc2VzXG5URU5BTlRfREJfTkFNRV9QRVJGSVggPSBcIiR7dGVuYW50X2RiX25hbWVfcHJlZml4fVwiXG5cbiMgQXV0aGVudGljYXRpb25cbkpXVF9TRUNSRVQgPSBcIiR7and0X3NlY3JldH1cIlxuXG4jIE1vbmdvREJcbk1PTkdPREJfREFUQUJBU0VfVVJMID0gXCJtb25nb2RiOi8vbW9uZ28vYmlnY2FwaXRhbFwiXG5cbiMgQXBwbGljYXRpb25cbkJBU0VfVVJMID0gXCIke2Jhc2VfdXJsfVwiXG5cbiMgQWdlbmRhc2hcbkFHRU5EQVNIX0FVVEhfVVNFUiA9IFwiJHthZ2VuZGFzaF9hdXRoX3VzZXJ9XCJcbkFHRU5EQVNIX0FVVEhfUEFTU1dPUkQgPSBcIiR7YWdlbmRhc2hfYXV0aF9wYXNzd29yZH1cIlxuXG4jIFNpZ24tdXAgcmVzdHJpY3Rpb25zXG5TSUdOVVBfRElTQUJMRUQgPSBcIiR7c2lnbnVwX2Rpc2FibGVkfVwiXG5TSUdOVVBfQUxMT1dFRF9ET01BSU5TID0gXCIke3NpZ251cF9hbGxvd2VkX2RvbWFpbnN9XCJcblNJR05VUF9BTExPV0VEX0VNQUlMUyA9IFwiJHtzaWdudXBfYWxsb3dlZF9lbWFpbHN9XCJcblxuIyBTaWduLXVwIGVtYWlsIGNvbmZpcm1hdGlvblxuU0lHTlVQX0VNQUlMX0NPTkZJUk1BVElPTiA9IFwiJHtzaWdudXBfZW1haWxfY29uZmlybWF0aW9ufVwiXG5cbiMgR290ZW5iZXJnIChQZGYgZ2VuZXJhdG9yKVxuR09URU5CRVJHX1VSTCA9IFwiJHtnb3RlbmJlcmdfdXJsfVwiXG5HT1RFTkJFUkdfRE9DU19VUkwgPSBcIiR7Z290ZW5iZXJnX2RvY3NfdXJsfVwiXG5cbiMgRXhjaGFuZ2UgUmF0ZVxuRVhDSEFOR0VfUkFURV9TRVJWSUNFID0gXCIke2V4Y2hhbmdlX3JhdGVfc2VydmljZX1cIlxuT1BFTl9FWENIQU5HRV9SQVRFX0FQUF9JRCA9IFwiJHtvcGVuX2V4Y2hhbmdlX3JhdGVfYXBwX2lkfVwiXG5cbiMgQmFuayBTeW5jXG5CQU5LSU5HX0NPTk5FQ1QgPSBcIiR7YmFua2luZ19jb25uZWN0fVwiXG5cbiMgUGxhaWRcblBMQUlEX0VOViA9IFwiJHtwbGFpZF9lbnZ9XCJcblBMQUlEX0NMSUVOVF9JRCA9IFwiJHtwbGFpZF9jbGllbnRfaWR9XCJcblBMQUlEX1NFQ1JFVCA9IFwiJHtwbGFpZF9zZWNyZXR9XCJcblBMQUlEX0xJTktfV0VCSE9PSyA9IFwiJHtwbGFpZF9saW5rX3dlYmhvb2t9XCJcblxuIyBMZW1vbiBTcXVlZXpcbkxFTU9OU1FVRUVaWV9BUElfS0VZID0gXCIke2xlbW9uc3F1ZWV6eV9hcGlfa2V5fVwiXG5MRU1PTlNRVUVFWllfU1RPUkVfSUQgPSBcIiR7bGVtb25zcXVlZXp5X3N0b3JlX2lkfVwiXG5MRU1PTlNRVUVFWllfV0VCSE9PS19TRUNSRVQgPSBcIiR7bGVtb25zcXVlZXp5X3dlYmhvb2tfc2VjcmV0fVwiXG5IT1NURURfT05fQklHQ0FQSVRBTF9DTE9VRCA9IFwiJHtob3N0ZWRfb25fYmlnY2FwaXRhbF9jbG91ZH1cIlxuXG4jIE5ldyBSZWxpYyBtZXRyaWNzIHRyYWNraW5nXG5ORVdfUkVMSUNfRElTVFJJQlVURURfVFJBQ0lOR19FTkFCTEVEID0gXCIke25ld19yZWxpY19kaXN0cmlidXRlZF90cmFjaW5nX2VuYWJsZWR9XCJcbk5FV19SRUxJQ19MT0cgPSBcIiR7bmV3X3JlbGljX2xvZ31cIlxuTkVXX1JFTElDX0FJX01PTklUT1JJTkdfRU5BQkxFRCA9IFwiJHtuZXdfcmVsaWNfYWlfbW9uaXRvcmluZ19lbmFibGVkfVwiXG5ORVdfUkVMSUNfQ1VTVE9NX0lOU0lHSFRTX0VWRU5UU19NQVhfU0FNUExFU19TVE9SRUQgPSBcIiR7bmV3X3JlbGljX2N1c3RvbV9pbnNpZ2h0c19ldmVudHNfbWF4X3NhbXBsZXNfc3RvcmVkfVwiXG5ORVdfUkVMSUNfU1BBTl9FVkVOVFNfTUFYX1NBTVBMRVNfU1RPUkVEID0gXCIke25ld19yZWxpY19zcGFuX2V2ZW50c19tYXhfc2FtcGxlc19zdG9yZWR9XCJcbk5FV19SRUxJQ19MSUNFTlNFX0tFWSA9IFwiJHtuZXdfcmVsaWNfbGljZW5zZV9rZXl9XCJcbk5FV19SRUxJQ19BUFBfTkFNRSA9IFwiJHtuZXdfcmVsaWNfYXBwX25hbWV9XCJcblxuIyBTM1xuUzNfUkVHSU9OID0gXCIke3MzX3JlZ2lvbn1cIlxuUzNfQUNDRVNTX0tFWV9JRCA9IFwiJHtzM19hY2Nlc3Nfa2V5X2lkfVwiXG5TM19TRUNSRVRfQUNDRVNTX0tFWSA9IFwiJHtzM19zZWNyZXRfYWNjZXNzX2tleX1cIlxuUzNfRU5EUE9JTlQgPSBcIiR7czNfZW5kcG9pbnR9XCJcblMzX0JVQ0tFVCA9IFwiJHtzM19idWNrZXR9XCJcblxuIyBNeVNRTFxuTVlTUUxfREFUQUJBU0UgPSBcIiR7c3lzdGVtX2RiX25hbWV9XCJcbk1ZU1FMX1VTRVIgPSBcIiR7ZGJfdXNlcn1cIlxuTVlTUUxfUEFTU1dPUkQgPSBcIiR7ZGJfcGFzc3dvcmR9XCJcbk1ZU1FMX1JPT1RfUEFTU1dPUkQgPSBcIiR7ZGJfcm9vdF9wYXNzd29yZH1cIlxuXG5bW2NvbmZpZy5tb3VudHNdXVxuXG4iCn0=
```

## Links

`accounting`,`finance`,`bookkeeping`,`quickbooks`,`erp`,`business`

---

Version:`latest`

BeszelA lightweight server monitoring hub with historical data, docker stats, and alerts.

BlenderBlender is a free and open-source 3D creation suite. It supports the entire 3D pipeline—modeling, rigging, animation, simulation, rendering, compositing and motion tracking, video editing and 2D animation pipeline.

### On this page

ConfigurationBase64LinksTags