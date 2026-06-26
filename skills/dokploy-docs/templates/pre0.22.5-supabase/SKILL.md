---
title: "SupaBase | Dokploy"
source: "https://docs.dokploy.com/docs/templates/pre0.22.5-supabase"
category: dokploy-docs
created: "2026-06-25T17:21:56.648Z"
---

SupaBase | Dokploy

# SupaBase

Copy as Markdown

The open source Firebase alternative. Supabase gives you a dedicated Postgres database to build your web, mobile, and AI applications. This is for dokploy version < 0.22.5.

## Configuration

docker-compose.ymltemplate.toml

```
# Usage
#   Start:              docker compose up
#   With helpers:       docker compose -f docker-compose.yml -f ./dev/docker-compose.dev.yml up
#   Stop:               docker compose down
#   Destroy:            docker compose -f docker-compose.yml -f ./dev/docker-compose.dev.yml down -v --remove-orphans
#   Reset everything:  ./reset.sh

name: supabase

services:

  studio:
    container_name: ${CONTAINER_PREFIX}-studio
    image: supabase/studio:2025.04.21-sha-173cc56
    restart: unless-stopped
    healthcheck:
      test:
        [
          "CMD",
          "node",
          "-e",
          "fetch('http://studio:3000/api/platform/profile').then((r) => {if (r.status !== 200) throw new Error(r.status)})"
        ]
      timeout: 10s
      interval: 5s
      retries: 3
    depends_on:
      analytics:
        condition: service_healthy
    environment:
      STUDIO_PG_META_URL: http://meta:8080
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}

      DEFAULT_ORGANIZATION_NAME: ${STUDIO_DEFAULT_ORGANIZATION}
      DEFAULT_PROJECT_NAME: ${STUDIO_DEFAULT_PROJECT}
      OPENAI_API_KEY: ${OPENAI_API_KEY:-}

      SUPABASE_URL: ${SUPABASE_PUBLIC_URL}
      SUPABASE_PUBLIC_URL: ${SUPABASE_PUBLIC_URL}
      SUPABASE_ANON_KEY: ${ANON_KEY}
      SUPABASE_SERVICE_KEY: ${SERVICE_ROLE_KEY}
      AUTH_JWT_SECRET: ${JWT_SECRET}

      LOGFLARE_API_KEY: ${LOGFLARE_API_KEY}
      LOGFLARE_URL: http://analytics:4000
      NEXT_PUBLIC_ENABLE_LOGS: true
      # Comment to use Big Query backend for analytics
      NEXT_ANALYTICS_BACKEND_PROVIDER: postgres
      # Uncomment to use Big Query backend for analytics
      # NEXT_ANALYTICS_BACKEND_PROVIDER: bigquery

  kong:
    container_name: ${CONTAINER_PREFIX}-kong
    image: kong:2.8.1
    restart: unless-stopped
    # ports:
    #   - ${KONG_HTTP_PORT}:8000/tcp
    #   - ${KONG_HTTPS_PORT}:8443/tcp
    expose:
      - 8000
      - 8443
    volumes:
      # https://github.com/supabase/supabase/issues/12661
      - ../files/volumes/api/kong.yml:/home/kong/temp.yml:ro,z
    depends_on:
      analytics:
        condition: service_healthy
    environment:
      KONG_DATABASE: "off"
      KONG_DECLARATIVE_CONFIG: /home/kong/kong.yml
      # https://github.com/supabase/cli/issues/14
      KONG_DNS_ORDER: LAST,A,CNAME
      KONG_PLUGINS: request-transformer,cors,key-auth,acl,basic-auth
      KONG_NGINX_PROXY_PROXY_BUFFER_SIZE: 160k
      KONG_NGINX_PROXY_PROXY_BUFFERS: 64 160k
      SUPABASE_ANON_KEY: ${ANON_KEY}
      SUPABASE_SERVICE_KEY: ${SERVICE_ROLE_KEY}
      DASHBOARD_USERNAME: ${DASHBOARD_USERNAME}
      DASHBOARD_PASSWORD: ${DASHBOARD_PASSWORD}
    # https://unix.stackexchange.com/a/294837
    entrypoint: bash -c 'eval "echo \"$$(cat ~/temp.yml)\"" > ~/kong.yml && /docker-entrypoint.sh kong docker-start'

  auth:
    container_name: ${CONTAINER_PREFIX}-auth
    image: supabase/gotrue:v2.171.0
    restart: unless-stopped
    healthcheck:
      test:
        [
          "CMD",
          "wget",
          "--no-verbose",
          "--tries=1",
          "--spider",
          "http://localhost:9999/health"
        ]
      timeout: 5s
      interval: 5s
      retries: 3
    depends_on:
      db:
        # Disable this if you are using an external Postgres database
        condition: service_healthy
      analytics:
        condition: service_healthy
    environment:
      # the next line seems required if you want to be able to send mails from the supabase GUI
      GOTRUE_MAILER_EXTERNAL_HOSTS: kong,${SUPABASE_HOST}
      GOTRUE_API_HOST: 0.0.0.0
      GOTRUE_API_PORT: 9999
      API_EXTERNAL_URL: ${API_EXTERNAL_URL}

      GOTRUE_DB_DRIVER: postgres
      GOTRUE_DB_DATABASE_URL: postgres://supabase_auth_admin:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}

      GOTRUE_SITE_URL: ${SITE_URL}
      GOTRUE_URI_ALLOW_LIST: ${ADDITIONAL_REDIRECT_URLS}
      GOTRUE_DISABLE_SIGNUP: ${DISABLE_SIGNUP}

      GOTRUE_JWT_ADMIN_ROLES: service_role
      GOTRUE_JWT_AUD: authenticated
      GOTRUE_JWT_DEFAULT_GROUP_NAME: authenticated
      GOTRUE_JWT_EXP: ${JWT_EXPIRY}
      GOTRUE_JWT_SECRET: ${JWT_SECRET}

      GOTRUE_EXTERNAL_EMAIL_ENABLED: ${ENABLE_EMAIL_SIGNUP}
      GOTRUE_EXTERNAL_ANONYMOUS_USERS_ENABLED: ${ENABLE_ANONYMOUS_USERS}
      GOTRUE_MAILER_AUTOCONFIRM: ${ENABLE_EMAIL_AUTOCONFIRM}

      # Uncomment to bypass nonce check in ID Token flow. Commonly set to true when using Google Sign In on mobile.
      # GOTRUE_EXTERNAL_SKIP_NONCE_CHECK: true

      # GOTRUE_MAILER_SECURE_EMAIL_CHANGE_ENABLED: true
      # GOTRUE_SMTP_MAX_FREQUENCY: 1s
      GOTRUE_SMTP_ADMIN_EMAIL: ${SMTP_ADMIN_EMAIL}
      GOTRUE_SMTP_HOST: ${SMTP_HOST}
      GOTRUE_SMTP_PORT: ${SMTP_PORT}
      GOTRUE_SMTP_USER: ${SMTP_USER}
      GOTRUE_SMTP_PASS: ${SMTP_PASS}
      GOTRUE_SMTP_SENDER_NAME: ${SMTP_SENDER_NAME}
      GOTRUE_MAILER_URLPATHS_INVITE: ${MAILER_URLPATHS_INVITE}
      GOTRUE_MAILER_URLPATHS_CONFIRMATION: ${MAILER_URLPATHS_CONFIRMATION}
      GOTRUE_MAILER_URLPATHS_RECOVERY: ${MAILER_URLPATHS_RECOVERY}
      GOTRUE_MAILER_URLPATHS_EMAIL_CHANGE: ${MAILER_URLPATHS_EMAIL_CHANGE}

      GOTRUE_EXTERNAL_PHONE_ENABLED: ${ENABLE_PHONE_SIGNUP}
      GOTRUE_SMS_AUTOCONFIRM: ${ENABLE_PHONE_AUTOCONFIRM}
      # Uncomment to enable custom access token hook. Please see: https://supabase.com/docs/guides/auth/auth-hooks for full list of hooks and additional details about custom_access_token_hook

      # GOTRUE_HOOK_CUSTOM_ACCESS_TOKEN_ENABLED: "true"
      # GOTRUE_HOOK_CUSTOM_ACCESS_TOKEN_URI: "pg-functions://postgres/public/custom_access_token_hook"
      # GOTRUE_HOOK_CUSTOM_ACCESS_TOKEN_SECRETS: "<standard-base64-secret>"

      # GOTRUE_HOOK_MFA_VERIFICATION_ATTEMPT_ENABLED: "true"
      # GOTRUE_HOOK_MFA_VERIFICATION_ATTEMPT_URI: "pg-functions://postgres/public/mfa_verification_attempt"

      # GOTRUE_HOOK_PASSWORD_VERIFICATION_ATTEMPT_ENABLED: "true"
      # GOTRUE_HOOK_PASSWORD_VERIFICATION_ATTEMPT_URI: "pg-functions://postgres/public/password_verification_attempt"

      # GOTRUE_HOOK_SEND_SMS_ENABLED: "false"
      # GOTRUE_HOOK_SEND_SMS_URI: "pg-functions://postgres/public/custom_access_token_hook"
      # GOTRUE_HOOK_SEND_SMS_SECRETS: "v1,whsec_VGhpcyBpcyBhbiBleGFtcGxlIG9mIGEgc2hvcnRlciBCYXNlNjQgc3RyaW5n"

      # GOTRUE_HOOK_SEND_EMAIL_ENABLED: "false"
      # GOTRUE_HOOK_SEND_EMAIL_URI: "http://host.docker.internal:54321/functions/v1/email_sender"
      # GOTRUE_HOOK_SEND_EMAIL_SECRETS: "v1,whsec_VGhpcyBpcyBhbiBleGFtcGxlIG9mIGEgc2hvcnRlciBCYXNlNjQgc3RyaW5n"

  rest:
    container_name: ${CONTAINER_PREFIX}-rest
    image: postgrest/postgrest:v12.2.11
    restart: unless-stopped
    depends_on:
      db:
        # Disable this if you are using an external Postgres database
        condition: service_healthy
      analytics:
        condition: service_healthy
    environment:
      PGRST_DB_URI: postgres://authenticator:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}
      PGRST_DB_SCHEMAS: ${PGRST_DB_SCHEMAS}
      PGRST_DB_ANON_ROLE: anon
      PGRST_JWT_SECRET: ${JWT_SECRET}
      PGRST_DB_USE_LEGACY_GUCS: "false"
      PGRST_APP_SETTINGS_JWT_SECRET: ${JWT_SECRET}
      PGRST_APP_SETTINGS_JWT_EXP: ${JWT_EXPIRY}
    command:
      [
        "postgrest"
      ]

  realtime:
    # This container name looks inconsistent but is correct because realtime constructs tenant id by parsing the subdomain
    container_name: realtime-dev.${CONTAINER_PREFIX}-realtime
    image: supabase/realtime:v2.34.47
    restart: unless-stopped
    depends_on:
      db:
        # Disable this if you are using an external Postgres database
        condition: service_healthy
      analytics:
        condition: service_healthy
    healthcheck:
      test:
        [
          "CMD",
          "curl",
          "-sSfL",
          "--head",
          "-o",
          "/dev/null",
          "-H",
          "Authorization: Bearer ${ANON_KEY}",
          "http://localhost:4000/api/tenants/realtime-dev/health"
        ]
      timeout: 5s
      interval: 5s
      retries: 3
    environment:
      PORT: 4000
      DB_HOST: ${POSTGRES_HOST}
      DB_PORT: ${POSTGRES_PORT}
      DB_USER: supabase_admin
      DB_PASSWORD: ${POSTGRES_PASSWORD}
      DB_NAME: ${POSTGRES_DB}
      DB_AFTER_CONNECT_QUERY: 'SET search_path TO _realtime'
      DB_ENC_KEY: supabaserealtime
      API_JWT_SECRET: ${JWT_SECRET}
      SECRET_KEY_BASE: ${SECRET_KEY_BASE}
      ERL_AFLAGS: -proto_dist inet_tcp
      DNS_NODES: "''"
      RLIMIT_NOFILE: "10000"
      APP_NAME: realtime
      SEED_SELF_HOST: true
      RUN_JANITOR: true

  # To use S3 backed storage: docker compose -f docker-compose.yml -f docker-compose.s3.yml up
  storage:
    container_name: ${CONTAINER_PREFIX}-storage
    image: supabase/storage-api:v1.22.7
    restart: unless-stopped
    volumes:
      - ../files/volumes/storage:/var/lib/storage:z
    healthcheck:
      test:
        [
          "CMD",
          "wget",
          "--no-verbose",
          "--tries=1",
          "--spider",
          "http://storage:5000/status"
        ]
      timeout: 5s
      interval: 5s
      retries: 3
    depends_on:
      db:
        # Disable this if you are using an external Postgres database
        condition: service_healthy
      rest:
        condition: service_started
      imgproxy:
        condition: service_started
    environment:
      ANON_KEY: ${ANON_KEY}
      SERVICE_KEY: ${SERVICE_ROLE_KEY}
      POSTGREST_URL: http://rest:3000
      PGRST_JWT_SECRET: ${JWT_SECRET}
      DATABASE_URL: postgres://supabase_storage_admin:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}
      FILE_SIZE_LIMIT: 52428800
      STORAGE_BACKEND: file
      FILE_STORAGE_BACKEND_PATH: /var/lib/storage
      TENANT_ID: stub
      # TODO: https://github.com/supabase/storage-api/issues/55
      REGION: stub
      GLOBAL_S3_BUCKET: stub
      ENABLE_IMAGE_TRANSFORMATION: "true"
      IMGPROXY_URL: http://imgproxy:5001

  imgproxy:
    container_name: ${CONTAINER_PREFIX}-imgproxy
    image: darthsim/imgproxy:v3.8.0
    restart: unless-stopped
    volumes:
      - ../files/volumes/storage:/var/lib/storage:z
    healthcheck:
      test:
        [
          "CMD",
          "imgproxy",
          "health"
        ]
      timeout: 5s
      interval: 5s
      retries: 3
    environment:
      IMGPROXY_BIND: ":5001"
      IMGPROXY_LOCAL_FILESYSTEM_ROOT: /
      IMGPROXY_USE_ETAG: "true"
      IMGPROXY_ENABLE_WEBP_DETECTION: ${IMGPROXY_ENABLE_WEBP_DETECTION}

  meta:
    container_name: ${CONTAINER_PREFIX}-meta
    image: supabase/postgres-meta:v0.88.9
    restart: unless-stopped
    depends_on:
      db:
        # Disable this if you are using an external Postgres database
        condition: service_healthy
      analytics:
        condition: service_healthy
    environment:
      PG_META_PORT: 8080
      PG_META_DB_HOST: ${POSTGRES_HOST}
      PG_META_DB_PORT: ${POSTGRES_PORT}
      PG_META_DB_NAME: ${POSTGRES_DB}
      PG_META_DB_USER: supabase_admin
      PG_META_DB_PASSWORD: ${POSTGRES_PASSWORD}

  functions:
    container_name: ${CONTAINER_PREFIX}-edge-functions
    image: supabase/edge-runtime:v1.67.4
    restart: unless-stopped
    volumes:
      - ../files/volumes/functions:/home/deno/functions:Z
    depends_on:
      analytics:
        condition: service_healthy
    environment:
      JWT_SECRET: ${JWT_SECRET}
      SUPABASE_URL: http://kong:8000
      SUPABASE_ANON_KEY: ${ANON_KEY}
      SUPABASE_SERVICE_ROLE_KEY: ${SERVICE_ROLE_KEY}
      SUPABASE_DB_URL: postgresql://postgres:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}
      # TODO: Allow configuring VERIFY_JWT per function. This PR might help: https://github.com/supabase/cli/pull/786
      VERIFY_JWT: "${FUNCTIONS_VERIFY_JWT}"
    command:
      [
        "start",
        "--main-service",
        "/home/deno/functions/main"
      ]

  analytics:
    container_name: ${CONTAINER_PREFIX}-analytics
    image: supabase/logflare:1.12.0
    restart: unless-stopped
    # ports:
    #   - 4000:4000
    expose:
      - 4000
    # Uncomment to use Big Query backend for analytics
    # volumes:
    #   - type: bind
    #     source: ${PWD}/gcloud.json
    #     target: /opt/app/rel/logflare/bin/gcloud.json
    #     read_only: true
    healthcheck:
      test:
        [
          "CMD",
          "curl",
          "http://localhost:4000/health"
        ]
      timeout: 5s
      interval: 5s
      retries: 10
    depends_on:
      db:
        # Disable this if you are using an external Postgres database
        condition: service_healthy
    environment:
      LOGFLARE_NODE_HOST: 127.0.0.1
      DB_USERNAME: supabase_admin
      DB_DATABASE: _supabase
      DB_HOSTNAME: ${POSTGRES_HOST}
      DB_PORT: ${POSTGRES_PORT}
      DB_PASSWORD: ${POSTGRES_PASSWORD}
      DB_SCHEMA: _analytics
      LOGFLARE_API_KEY: ${LOGFLARE_API_KEY}
      LOGFLARE_SINGLE_TENANT: true
      LOGFLARE_SUPABASE_MODE: true
      LOGFLARE_MIN_CLUSTER_SIZE: 1

      # Comment variables to use Big Query backend for analytics
      POSTGRES_BACKEND_URL: postgresql://supabase_admin:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/_supabase
      POSTGRES_BACKEND_SCHEMA: _analytics
      LOGFLARE_FEATURE_FLAG_OVERRIDE: multibackend=true
      # Uncomment to use Big Query backend for analytics
      # GOOGLE_PROJECT_ID: ${GOOGLE_PROJECT_ID}
      # GOOGLE_PROJECT_NUMBER: ${GOOGLE_PROJECT_NUMBER}

  # Comment out everything below this point if you are using an external Postgres database
  db:
    container_name: ${CONTAINER_PREFIX}-db
    image: supabase/postgres:15.8.1.060
    restart: unless-stopped
    volumes:
      - ../files/volumes/db/realtime.sql:/docker-entrypoint-initdb.d/migrations/99-realtime.sql:Z
      # Must be superuser to create event trigger
      - ../files/volumes/db/webhooks.sql:/docker-entrypoint-initdb.d/init-scripts/98-webhooks.sql:Z
      # Must be superuser to alter reserved role
      - ../files/volumes/db/roles.sql:/docker-entrypoint-initdb.d/init-scripts/99-roles.sql:Z
      # Initialize the database settings with JWT_SECRET and JWT_EXP
      - ../files/volumes/db/jwt.sql:/docker-entrypoint-initdb.d/init-scripts/99-jwt.sql:Z
      # PGDATA directory is persisted between restarts
      - ../files/volumes/db/data:/var/lib/postgresql/data:Z
      # Changes required for internal supabase data such as _analytics
      - ../files/volumes/db/_supabase.sql:/docker-entrypoint-initdb.d/migrations/97-_supabase.sql:Z
      # Changes required for Analytics support
      - ../files/volumes/db/logs.sql:/docker-entrypoint-initdb.d/migrations/99-logs.sql:Z
      # Changes required for Pooler support
      - ../files/volumes/db/pooler.sql:/docker-entrypoint-initdb.d/migrations/99-pooler.sql:Z
      # Use named volume to persist pgsodium decryption key between restarts
      - db-config:/etc/postgresql-custom
    healthcheck:
      test:
        [
        "CMD",
        "pg_isready",
        "-U",
        "postgres",
        "-h",
        "localhost"
        ]
      interval: 5s
      timeout: 5s
      retries: 10
    depends_on:
      vector:
        condition: service_healthy
    environment:
      POSTGRES_HOST: /var/run/postgresql
      PGPORT: ${POSTGRES_PORT}
      POSTGRES_PORT: ${POSTGRES_PORT}
      PGPASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      PGDATABASE: ${POSTGRES_DB}
      POSTGRES_DB: ${POSTGRES_DB}
      JWT_SECRET: ${JWT_SECRET}
      JWT_EXP: ${JWT_EXPIRY}
    command:
      [
        "postgres",
        "-c",
        "config_file=/etc/postgresql/postgresql.conf",
        "-c",
        "log_min_messages=fatal" # prevents Realtime polling queries from appearing in logs
      ]

  vector:
    container_name: ${CONTAINER_PREFIX}-vector
    image: timberio/vector:0.28.1-alpine
    restart: unless-stopped
    volumes:
      - ../files/volumes/logs/vector.yml:/etc/vector/vector.yml:ro,z
      - ${DOCKER_SOCKET_LOCATION}:/var/run/docker.sock:ro,z
    healthcheck:
      test:
        [
          "CMD",
          "wget",
          "--no-verbose",
          "--tries=1",
          "--spider",
          "http://vector:9001/health"
        ]
      timeout: 5s
      interval: 5s
      retries: 3
    environment:
      LOGFLARE_API_KEY: ${LOGFLARE_API_KEY}
    command:
      [
        "--config",
        "/etc/vector/vector.yml"
      ]
    security_opt:
      - "label=disable"

  # Update the DATABASE_URL if you are using an external Postgres database
  supavisor:
    container_name: ${CONTAINER_PREFIX}-pooler
    image: supabase/supavisor:2.5.1
    restart: unless-stopped
    ports: # expose supavisor to the host to enable db pooler connection
      - ${POSTGRES_PORT}:5432
      - ${POOLER_PROXY_PORT_TRANSACTION}:6543
    volumes:
      - ../files/volumes/pooler/pooler.exs:/etc/pooler/pooler.exs:ro,z
    healthcheck:
      test:
        [
          "CMD",
          "curl",
          "-sSfL",
          "--head",
          "-o",
          "/dev/null",
          "http://127.0.0.1:4000/api/health"
        ]
      interval: 10s
      timeout: 5s
      retries: 5
    depends_on:
      db:
        condition: service_healthy
      analytics:
        condition: service_healthy
    environment:
      PORT: 4000
      POSTGRES_PORT: ${POSTGRES_PORT}
      POSTGRES_DB: ${POSTGRES_DB}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      DATABASE_URL: ecto://supabase_admin:${POSTGRES_PASSWORD}@db:${POSTGRES_PORT}/_supabase
      CLUSTER_POSTGRES: true
      SECRET_KEY_BASE: ${SECRET_KEY_BASE}
      VAULT_ENC_KEY: ${VAULT_ENC_KEY}
      API_JWT_SECRET: ${JWT_SECRET}
      METRICS_JWT_SECRET: ${JWT_SECRET}
      REGION: local
      ERL_AFLAGS: -proto_dist inet_tcp
      POOLER_TENANT_ID: ${POOLER_TENANT_ID}
      POOLER_DEFAULT_POOL_SIZE: ${POOLER_DEFAULT_POOL_SIZE}
      POOLER_MAX_CLIENT_CONN: ${POOLER_MAX_CLIENT_CONN}
      POOLER_POOL_MODE: transaction
    command:
      [
        "/bin/sh",
        "-c",
        "/app/bin/migrate && /app/bin/supavisor eval \"$$(cat /etc/pooler/pooler.exs)\" && /app/bin/server"
      ]

volumes:
  db-config:
```

```
[variables]
main_domain = "${domain}"
postgres_password = "${password:32}"
dashboard_password = "${password:32}"
logflare_api_key = "${password:32}"
container_name_prefix = "supabase-${hash:4}"

[[config.domains]]
serviceName = "kong"
port = 8_000
host = "${main_domain}"

[config]
env = [
'############',
'# To get a proper working configuration you should at least take a look at:',
'# - SUPABASE_PUBLIC_URL, API_EXTERNAL_URL should point to your supabase domain with correct http/https scheme',
'# - SMTP_* are required for auth mail sending',
'# - ADDITIONAL_REDIRECT_URLS, SITE_URL should point to application using supabase for authentication',
'#   They are used for redirecting after login/signup and gotrue will check them before sending emails',
'# - POSTGRES_PORT, POOLER_PROXY_PORT_TRANSACTION should be changed if you are already running other instances of supabase',
'# and CHANGE: JWT-SECRET, ANON_KEY, SERVICE_ROLE_KEY, SECRET_KEY_BASE, VAULT_ENC_KEY',
'#',
'# Supabase uses container names in part of its configuration so it is important to keep them',
'# This template generates a random prefix for the container names to avoid conflicts',
'# If you change it you will need to update routes in the vector.yml file in advanced->mounts section',
'############',
'CONTAINER_PREFIX=${container_name_prefix}',
'',
'############',
'# Secrets',
'# YOU MUST CHANGE THESE BEFORE GOING INTO PRODUCTION',
'# https://supabase.com/docs/guides/self-hosting/docker#securing-your-services',
'# They are default values from supabase so really do not use them in exposed environments',
'# Go to https://supabase.com/docs/guides/self-hosting for more information',
'############',
'',
'SUPABASE_HOST=${main_domain}',
'POSTGRES_PASSWORD=${postgres_password}',
'JWT_SECRET=your-super-secret-jwt-token-with-at-least-32-characters-long',
'ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyAgCiAgICAicm9sZSI6ICJhbm9uIiwKICAgICJpc3MiOiAic3VwYWJhc2UtZGVtbyIsCiAgICAiaWF0IjogMTY0MTc2OTIwMCwKICAgICJleHAiOiAxNzk5NTM1NjAwCn0.dc_X5iR_VP_qT0zsiyj_I_OZ2T9FtRU2BBNWN8Bu4GE',
'SERVICE_ROLE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyAgCiAgICAicm9sZSI6ICJzZXJ2aWNlX3JvbGUiLAogICAgImlzcyI6ICJzdXBhYmFzZS1kZW1vIiwKICAgICJpYXQiOiAxNjQxNzY5MjAwLAogICAgImV4cCI6IDE3OTk1MzU2MDAKfQ.DaYlNEoUrrEn2Ig7tqibS-PHK5vgusbcbo7X36XVt4Q',
'DASHBOARD_USERNAME=supabase',
'DASHBOARD_PASSWORD=${dashboard_password}',
'SECRET_KEY_BASE=UpNVntn3cDxHJpq99YMc1T1AQgQpc8kfYTuRgBiYa15BLrx8etQoXz3gZv1/u2oq',
'VAULT_ENC_KEY=your-encryption-key-32-chars-min',
'',
'',
'############',
'# Database - You can change these to any PostgreSQL database that has logical replication enabled.',
'############',
'',
'POSTGRES_HOST=db',
'POSTGRES_DB=postgres',
'POSTGRES_PORT=5432',
'# default user is postgres',
'',
'',
'############',
'# Supavisor -- Database pooler',
'############',
'POOLER_PROXY_PORT_TRANSACTION=6543',
'POOLER_DEFAULT_POOL_SIZE=20',
'POOLER_MAX_CLIENT_CONN=100',
'POOLER_TENANT_ID=your-tenant-id',
'',
'',
'############',
'# API Proxy - Configuration for the Kong Reverse proxy.',
'# Following ports should not be changed for a dokploy config unless you know what you are doing.',
'############',
'',
'KONG_HTTP_PORT=8000',
'KONG_HTTPS_PORT=8443',
'',
'',
'############',
'# API - Configuration for PostgREST.',
'############',
'',
'PGRST_DB_SCHEMAS=public,storage,graphql_public',
'',
'',
'############',
'# Auth - Configuration for the GoTrue authentication server.',
'############',
'',
'## General',
'SITE_URL=http://localhost:3000',
'ADDITIONAL_REDIRECT_URLS=http://${main_domain}/*,http://localhost:3000/*',
'JWT_EXPIRY=3600',
'DISABLE_SIGNUP=false',
'API_EXTERNAL_URL=http://${main_domain}',
'',
'## Mailer Config',
'MAILER_URLPATHS_CONFIRMATION="/auth/v1/verify"',
'MAILER_URLPATHS_INVITE="/auth/v1/verify"',
'MAILER_URLPATHS_RECOVERY="/auth/v1/verify"',
'MAILER_URLPATHS_EMAIL_CHANGE="/auth/v1/verify"',
'',
'## Email auth',
'ENABLE_EMAIL_SIGNUP=true',
'ENABLE_EMAIL_AUTOCONFIRM=false',
'[email protected]',
'SMTP_HOST=supabase-mail',
'SMTP_PORT=2500',
'SMTP_USER=fake_mail_user',
'SMTP_PASS=fake_mail_password',
'SMTP_SENDER_NAME=fake_sender',
'ENABLE_ANONYMOUS_USERS=false',
'',
'## Phone auth',
'ENABLE_PHONE_SIGNUP=true',
'ENABLE_PHONE_AUTOCONFIRM=true',
'',
'',
'############',
'# Studio - Configuration for the Dashboard',
'############',
'',
'STUDIO_DEFAULT_ORGANIZATION=Default Organization',
'STUDIO_DEFAULT_PROJECT=Default Project',
'',
'STUDIO_PORT=3000',
'# replace if you intend to use Studio outside of localhost',
'SUPABASE_PUBLIC_URL=http://${main_domain}',
'',
'# Enable webp support',
'IMGPROXY_ENABLE_WEBP_DETECTION=true',
'',
'# Add your OpenAI API key to enable SQL Editor Assistant',
'OPENAI_API_KEY=',
'',
'',
'############',
'# Functions - Configuration for Functions',
'############',
'# NOTE: VERIFY_JWT applies to all functions. Per-function VERIFY_JWT is not supported yet.',
'FUNCTIONS_VERIFY_JWT=false',
'',
'',
'############',
'# Logs - Configuration for Logflare',
'# Please refer to https://supabase.com/docs/reference/self-hosting-analytics/introduction',
'############',
'',
'LOGFLARE_LOGGER_BACKEND_API_KEY=your-super-secret-and-long-logflare-key',
'',
'# Change vector.toml sinks to reflect this change',
'LOGFLARE_API_KEY=${logflare_api_key}',
'',
'# Docker socket location - this value will differ depending on your OS',
'DOCKER_SOCKET_LOCATION=/var/run/docker.sock',
'',
'# Google Cloud Project details',
'GOOGLE_PROJECT_ID=GOOGLE_PROJECT_ID',
'GOOGLE_PROJECT_NUMBER=GOOGLE_PROJECT_NUMBER']

[[config.mounts]]
filePath = "/volumes/api/kong.yml"
content = """_format_version: '2.1'
_transform: true

###
### Consumers / Users
###
consumers:
  - username: DASHBOARD
  - username: anon
    keyauth_credentials:
      - key: $SUPABASE_ANON_KEY
  - username: service_role
    keyauth_credentials:
      - key: $SUPABASE_SERVICE_KEY

###
### Access Control List
###
acls:
  - consumer: anon
    group: anon
  - consumer: service_role
    group: admin

###
### Dashboard credentials
###
basicauth_credentials:
  - consumer: DASHBOARD
    username: $DASHBOARD_USERNAME
    password: $DASHBOARD_PASSWORD

###
### API Routes
###
services:
  ## Open Auth routes
  - name: auth-v1-open
    url: http://auth:9999/verify
    routes:
      - name: auth-v1-open
        strip_path: true
        paths:
          - /auth/v1/verify
    plugins:
      - name: cors
  - name: auth-v1-open-callback
    url: http://auth:9999/callback
    routes:
      - name: auth-v1-open-callback
        strip_path: true
        paths:
          - /auth/v1/callback
    plugins:
      - name: cors
  - name: auth-v1-open-authorize
    url: http://auth:9999/authorize
    routes:
      - name: auth-v1-open-authorize
        strip_path: true
        paths:
          - /auth/v1/authorize
    plugins:
      - name: cors

  ## Secure Auth routes
  - name: auth-v1
    _comment: 'GoTrue: /auth/v1/* -> http://auth:9999/*'
    url: http://auth:9999/
    routes:
      - name: auth-v1-all
        strip_path: true
        paths:
          - /auth/v1/
    plugins:
      - name: cors
      - name: key-auth
        config:
          hide_credentials: false
      - name: acl
        config:
          hide_groups_header: true
          allow:
            - admin
            - anon

  ## Secure REST routes
  - name: rest-v1
    _comment: 'PostgREST: /rest/v1/* -> http://rest:3000/*'
    url: http://rest:3000/
    routes:
      - name: rest-v1-all
        strip_path: true
        paths:
          - /rest/v1/
    plugins:
      - name: cors
      - name: key-auth
        config:
          hide_credentials: true
      - name: acl
        config:
          hide_groups_header: true
          allow:
            - admin
            - anon

  ## Secure GraphQL routes
  - name: graphql-v1
    _comment: 'PostgREST: /graphql/v1/* -> http://rest:3000/rpc/graphql'
    url: http://rest:3000/rpc/graphql
    routes:
      - name: graphql-v1-all
        strip_path: true
        paths:
          - /graphql/v1
    plugins:
      - name: cors
      - name: key-auth
        config:
          hide_credentials: true
      - name: request-transformer
        config:
          add:
            headers:
              - Content-Profile:graphql_public
      - name: acl
        config:
          hide_groups_header: true
          allow:
            - admin
            - anon

  ## Secure Realtime routes
  - name: realtime-v1-ws
    _comment: 'Realtime: /realtime/v1/* -> ws://realtime:4000/socket/*'
    url: http://realtime-dev.supabase-realtime:4000/socket
    protocol: ws
    routes:
      - name: realtime-v1-ws
        strip_path: true
        paths:
          - /realtime/v1/
    plugins:
      - name: cors
      - name: key-auth
        config:
          hide_credentials: false
      - name: acl
        config:
          hide_groups_header: true
          allow:
            - admin
            - anon
  - name: realtime-v1-rest
    _comment: 'Realtime: /realtime/v1/* -> ws://realtime:4000/socket/*'
    url: http://realtime-dev.supabase-realtime:4000/api
    protocol: http
    routes:
      - name: realtime-v1-rest
        strip_path: true
        paths:
          - /realtime/v1/api
    plugins:
      - name: cors
      - name: key-auth
        config:
          hide_credentials: false
      - name: acl
        config:
          hide_groups_header: true
          allow:
            - admin
            - anon
  ## Storage routes: the storage server manages its own auth
  - name: storage-v1
    _comment: 'Storage: /storage/v1/* -> http://storage:5000/*'
    url: http://storage:5000/
    routes:
      - name: storage-v1-all
        strip_path: true
        paths:
          - /storage/v1/
    plugins:
      - name: cors

  ## Edge Functions routes
  - name: functions-v1
    _comment: 'Edge Functions: /functions/v1/* -> http://functions:9000/*'
    url: http://functions:9000/
    routes:
      - name: functions-v1-all
        strip_path: true
        paths:
          - /functions/v1/
    plugins:
      - name: cors

  ## Analytics routes
  - name: analytics-v1
    _comment: 'Analytics: /analytics/v1/* -> http://logflare:4000/*'
    url: http://analytics:4000/
    routes:
      - name: analytics-v1-all
        strip_path: true
        paths:
          - /analytics/v1/

  ## Secure Database routes
  - name: meta
    _comment: 'pg-meta: /pg/* -> http://pg-meta:8080/*'
    url: http://meta:8080/
    routes:
      - name: meta-all
        strip_path: true
        paths:
          - /pg/
    plugins:
      - name: key-auth
        config:
          hide_credentials: false
      - name: acl
        config:
          hide_groups_header: true
          allow:
            - admin

  ## Protected Dashboard - catch all remaining routes
  - name: dashboard
    _comment: 'Studio: /* -> http://studio:3000/*'
    url: http://studio:3000/
    routes:
      - name: dashboard-all
        strip_path: true
        paths:
          - /
    plugins:
      - name: cors
      - name: basic-auth
        config:
          hide_credentials: true
"""

[[config.mounts]]
filePath = "/volumes/db/init/data.sql"
content = ""

[[config.mounts]]
filePath = "/volumes/db/_supabase.sql"
content = """\\set pguser `echo "$POSTGRES_USER"`

CREATE DATABASE _supabase WITH OWNER :pguser;
"""

[[config.mounts]]
filePath = "/volumes/db/jwt.sql"
content = """
\\set jwt_secret `echo "$JWT_SECRET"`
\\set jwt_exp `echo "$JWT_EXP"`

ALTER DATABASE postgres SET "app.settings.jwt_secret" TO :'jwt_secret';
ALTER DATABASE postgres SET "app.settings.jwt_exp" TO :'jwt_exp';
"""

[[config.mounts]]
filePath = "/volumes/db/logs.sql"
content = """
\\set pguser `echo "$POSTGRES_USER"`

\\c _supabase
create schema if not exists _analytics;
alter schema _analytics owner to :pguser;
\\c postgres
"""

[[config.mounts]]
filePath = "/volumes/db/pooler.sql"
content = """
\\set pguser `echo "$POSTGRES_USER"`

\\c _supabase
create schema if not exists _supavisor;
alter schema _supavisor owner to :pguser;
\\c postgres
"""

[[config.mounts]]
filePath = "/volumes/db/realtime.sql"
content = """
\\set pguser `echo "$POSTGRES_USER"`

create schema if not exists _realtime;
alter schema _realtime owner to :pguser;
"""

[[config.mounts]]
filePath = "/volumes/db/roles.sql"
content = """
-- NOTE: change to your own passwords for production environments
\\set pgpass `echo "$POSTGRES_PASSWORD"`

ALTER USER authenticator WITH PASSWORD :'pgpass';
ALTER USER pgbouncer WITH PASSWORD :'pgpass';
ALTER USER supabase_auth_admin WITH PASSWORD :'pgpass';
ALTER USER supabase_functions_admin WITH PASSWORD :'pgpass';
ALTER USER supabase_storage_admin WITH PASSWORD :'pgpass';
"""

[[config.mounts]]
filePath = "/volumes/db/webhooks.sql"
content = """
BEGIN;
  -- Create pg_net extension
  CREATE EXTENSION IF NOT EXISTS pg_net SCHEMA extensions;
  -- Create supabase_functions schema
  CREATE SCHEMA supabase_functions AUTHORIZATION supabase_admin;
  GRANT USAGE ON SCHEMA supabase_functions TO postgres, anon, authenticated, service_role;
  ALTER DEFAULT PRIVILEGES IN SCHEMA supabase_functions GRANT ALL ON TABLES TO postgres, anon, authenticated, service_role;
  ALTER DEFAULT PRIVILEGES IN SCHEMA supabase_functions GRANT ALL ON FUNCTIONS TO postgres, anon, authenticated, service_role;
  ALTER DEFAULT PRIVILEGES IN SCHEMA supabase_functions GRANT ALL ON SEQUENCES TO postgres, anon, authenticated, service_role;
  -- supabase_functions.migrations definition
  CREATE TABLE supabase_functions.migrations (
    version text PRIMARY KEY,
    inserted_at timestamptz NOT NULL DEFAULT NOW()
  );
  -- Initial supabase_functions migration
  INSERT INTO supabase_functions.migrations (version) VALUES ('initial');
  -- supabase_functions.hooks definition
  CREATE TABLE supabase_functions.hooks (
    id bigserial PRIMARY KEY,
    hook_table_id integer NOT NULL,
    hook_name text NOT NULL,
    created_at timestamptz NOT NULL DEFAULT NOW(),
    request_id bigint
  );
  CREATE INDEX supabase_functions_hooks_request_id_idx ON supabase_functions.hooks USING btree (request_id);
  CREATE INDEX supabase_functions_hooks_h_table_id_h_name_idx ON supabase_functions.hooks USING btree (hook_table_id, hook_name);
  COMMENT ON TABLE supabase_functions.hooks IS 'Supabase Functions Hooks: Audit trail for triggered hooks.';
  CREATE FUNCTION supabase_functions.http_request()
    RETURNS trigger
    LANGUAGE plpgsql
    AS $function$
    DECLARE
      request_id bigint;
      payload jsonb;
      url text := TG_ARGV[0]::text;
      method text := TG_ARGV[1]::text;
      headers jsonb DEFAULT '{}'::jsonb;
      params jsonb DEFAULT '{}'::jsonb;
      timeout_ms integer DEFAULT 1000;
    BEGIN
      IF url IS NULL OR url = 'null' THEN
        RAISE EXCEPTION 'url argument is missing';
      END IF;

      IF method IS NULL OR method = 'null' THEN
        RAISE EXCEPTION 'method argument is missing';
      END IF;

      IF TG_ARGV[2] IS NULL OR TG_ARGV[2] = 'null' THEN
        headers = '{"Content-Type": "application/json"}'::jsonb;
      ELSE
        headers = TG_ARGV[2]::jsonb;
      END IF;

      IF TG_ARGV[3] IS NULL OR TG_ARGV[3] = 'null' THEN
        params = '{}'::jsonb;
      ELSE
        params = TG_ARGV[3]::jsonb;
      END IF;

      IF TG_ARGV[4] IS NULL OR TG_ARGV[4] = 'null' THEN
        timeout_ms = 1000;
      ELSE
        timeout_ms = TG_ARGV[4]::integer;
      END IF;

      CASE
        WHEN method = 'GET' THEN
          SELECT http_get INTO request_id FROM net.http_get(
            url,
            params,
            headers,
            timeout_ms
          );
        WHEN method = 'POST' THEN
          payload = jsonb_build_object(
            'old_record', OLD,
            'record', NEW,
            'type', TG_OP,
            'table', TG_TABLE_NAME,
            'schema', TG_TABLE_SCHEMA
          );

          SELECT http_post INTO request_id FROM net.http_post(
            url,
            payload,
            params,
            headers,
            timeout_ms
          );
        ELSE
          RAISE EXCEPTION 'method argument % is invalid', method;
      END CASE;

      INSERT INTO supabase_functions.hooks
        (hook_table_id, hook_name, request_id)
      VALUES
        (TG_RELID, TG_NAME, request_id);

      RETURN NEW;
    END
  $function$;
  -- Supabase super admin
  DO
  $$
  BEGIN
    IF NOT EXISTS (
      SELECT 1
      FROM pg_roles
      WHERE rolname = 'supabase_functions_admin'
    )
    THEN
      CREATE USER supabase_functions_admin NOINHERIT CREATEROLE LOGIN NOREPLICATION;
    END IF;
  END
  $$;
  GRANT ALL PRIVILEGES ON SCHEMA supabase_functions TO supabase_functions_admin;
  GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA supabase_functions TO supabase_functions_admin;
  GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA supabase_functions TO supabase_functions_admin;
  ALTER USER supabase_functions_admin SET search_path = "supabase_functions";
  ALTER table "supabase_functions".migrations OWNER TO supabase_functions_admin;
  ALTER table "supabase_functions".hooks OWNER TO supabase_functions_admin;
  ALTER function "supabase_functions".http_request() OWNER TO supabase_functions_admin;
  GRANT supabase_functions_admin TO postgres;
  -- Remove unused supabase_pg_net_admin role
  DO
  $$
  BEGIN
    IF EXISTS (
      SELECT 1
      FROM pg_roles
      WHERE rolname = 'supabase_pg_net_admin'
    )
    THEN
      REASSIGN OWNED BY supabase_pg_net_admin TO supabase_admin;
      DROP OWNED BY supabase_pg_net_admin;
      DROP ROLE supabase_pg_net_admin;
    END IF;
  END
  $$;
  -- pg_net grants when extension is already enabled
  DO
  $$
  BEGIN
    IF EXISTS (
      SELECT 1
      FROM pg_extension
      WHERE extname = 'pg_net'
    )
    THEN
      GRANT USAGE ON SCHEMA net TO supabase_functions_admin, postgres, anon, authenticated, service_role;
      ALTER function net.http_get(url text, params jsonb, headers jsonb, timeout_milliseconds integer) SECURITY DEFINER;
      ALTER function net.http_post(url text, body jsonb, params jsonb, headers jsonb, timeout_milliseconds integer) SECURITY DEFINER;
      ALTER function net.http_get(url text, params jsonb, headers jsonb, timeout_milliseconds integer) SET search_path = net;
      ALTER function net.http_post(url text, body jsonb, params jsonb, headers jsonb, timeout_milliseconds integer) SET search_path = net;
      REVOKE ALL ON FUNCTION net.http_get(url text, params jsonb, headers jsonb, timeout_milliseconds integer) FROM PUBLIC;
      REVOKE ALL ON FUNCTION net.http_post(url text, body jsonb, params jsonb, headers jsonb, timeout_milliseconds integer) FROM PUBLIC;
      GRANT EXECUTE ON FUNCTION net.http_get(url text, params jsonb, headers jsonb, timeout_milliseconds integer) TO supabase_functions_admin, postgres, anon, authenticated, service_role;
      GRANT EXECUTE ON FUNCTION net.http_post(url text, body jsonb, params jsonb, headers jsonb, timeout_milliseconds integer) TO supabase_functions_admin, postgres, anon, authenticated, service_role;
    END IF;
  END
  $$;
  -- Event trigger for pg_net
  CREATE OR REPLACE FUNCTION extensions.grant_pg_net_access()
  RETURNS event_trigger
  LANGUAGE plpgsql
  AS $$
  BEGIN
    IF EXISTS (
      SELECT 1
      FROM pg_event_trigger_ddl_commands() AS ev
      JOIN pg_extension AS ext
      ON ev.objid = ext.oid
      WHERE ext.extname = 'pg_net'
    )
    THEN
      GRANT USAGE ON SCHEMA net TO supabase_functions_admin, postgres, anon, authenticated, service_role;
      ALTER function net.http_get(url text, params jsonb, headers jsonb, timeout_milliseconds integer) SECURITY DEFINER;
      ALTER function net.http_post(url text, body jsonb, params jsonb, headers jsonb, timeout_milliseconds integer) SECURITY DEFINER;
      ALTER function net.http_get(url text, params jsonb, headers jsonb, timeout_milliseconds integer) SET search_path = net;
      ALTER function net.http_post(url text, body jsonb, params jsonb, headers jsonb, timeout_milliseconds integer) SET search_path = net;
      REVOKE ALL ON FUNCTION net.http_get(url text, params jsonb, headers jsonb, timeout_milliseconds integer) FROM PUBLIC;
      REVOKE ALL ON FUNCTION net.http_post(url text, body jsonb, params jsonb, headers jsonb, timeout_milliseconds integer) FROM PUBLIC;
      GRANT EXECUTE ON FUNCTION net.http_get(url text, params jsonb, headers jsonb, timeout_milliseconds integer) TO supabase_functions_admin, postgres, anon, authenticated, service_role;
      GRANT EXECUTE ON FUNCTION net.http_post(url text, body jsonb, params jsonb, headers jsonb, timeout_milliseconds integer) TO supabase_functions_admin, postgres, anon, authenticated, service_role;
    END IF;
  END;
  $$;
  COMMENT ON FUNCTION extensions.grant_pg_net_access IS 'Grants access to pg_net';
  DO
  $$
  BEGIN
    IF NOT EXISTS (
      SELECT 1
      FROM pg_event_trigger
      WHERE evtname = 'issue_pg_net_access'
    ) THEN
      CREATE EVENT TRIGGER issue_pg_net_access ON ddl_command_end WHEN TAG IN ('CREATE EXTENSION')
      EXECUTE PROCEDURE extensions.grant_pg_net_access();
    END IF;
  END
  $$;
  INSERT INTO supabase_functions.migrations (version) VALUES ('20210809183423_update_grants');
  ALTER function supabase_functions.http_request() SECURITY DEFINER;
  ALTER function supabase_functions.http_request() SET search_path = supabase_functions;
  REVOKE ALL ON FUNCTION supabase_functions.http_request() FROM PUBLIC;
  GRANT EXECUTE ON FUNCTION supabase_functions.http_request() TO postgres, anon, authenticated, service_role;
COMMIT;
"""

[[config.mounts]]
filePath = "/volumes/functions/hello/index.ts"
content = """
// Follow this setup guide to integrate the Deno language server with your editor:
// https://deno.land/manual/getting_started/setup_your_environment
// This enables autocomplete, go to definition, etc.

import { serve } from "https://deno.land/[email protected]/http/server.ts"

serve(async () => {
  return new Response(
    `"Hello from Edge Functions!"`,
    { headers: { "Content-Type": "application/json" } },
  )
})

// To invoke:
// curl 'http://localhost:<KONG_HTTP_PORT>/functions/v1/hello' \
//   --header 'Authorization: Bearer <anon/service_role API key>'
"""

[[config.mounts]]
filePath = "/volumes/functions/main/index.ts"
content = """import { serve } from 'https://deno.land/[email protected]/http/server.ts'
import * as jose from 'https://deno.land/x/[email protected]/index.ts'

console.log('main function started')

const JWT_SECRET = Deno.env.get('JWT_SECRET')
const VERIFY_JWT = Deno.env.get('VERIFY_JWT') === 'true'

function getAuthToken(req: Request) {
  const authHeader = req.headers.get('authorization')
  if (!authHeader) {
    throw new Error('Missing authorization header')
  }
  const [bearer, token] = authHeader.split(' ')
  if (bearer !== 'Bearer') {
    throw new Error(`Auth header is not 'Bearer {token}'`)
  }
  return token
}

async function verifyJWT(jwt: string): Promise<boolean> {
  const encoder = new TextEncoder()
  const secretKey = encoder.encode(JWT_SECRET)
  try {
    await jose.jwtVerify(jwt, secretKey)
  } catch (err) {
    console.error(err)
    return false
  }
  return true
}

serve(async (req: Request) => {
  if (req.method !== 'OPTIONS' && VERIFY_JWT) {
    try {
      const token = getAuthToken(req)
      const isValidJWT = await verifyJWT(token)

      if (!isValidJWT) {
        return new Response(JSON.stringify({ msg: 'Invalid JWT' }), {
          status: 401,
          headers: { 'Content-Type': 'application/json' },
        })
      }
    } catch (e) {
      console.error(e)
      return new Response(JSON.stringify({ msg: e.toString() }), {
        status: 401,
        headers: { 'Content-Type': 'application/json' },
      })
    }
  }

  const url = new URL(req.url)
  const { pathname } = url
  const path_parts = pathname.split('/')
  const service_name = path_parts[1]

  if (!service_name || service_name === '') {
    const error = { msg: 'missing function name in request' }
    return new Response(JSON.stringify(error), {
      status: 400,
      headers: { 'Content-Type': 'application/json' },
    })
  }

  const servicePath = `/home/deno/functions/${service_name}`
  console.error(`serving the request with ${servicePath}`)

  const memoryLimitMb = 150
  const workerTimeoutMs = 1 * 60 * 1000
  const noModuleCache = false
  const importMapPath = null
  const envVarsObj = Deno.env.toObject()
  const envVars = Object.keys(envVarsObj).map((k) => [k, envVarsObj[k]])

  try {
    const worker = await EdgeRuntime.userWorkers.create({
      servicePath,
      memoryLimitMb,
      workerTimeoutMs,
      noModuleCache,
      importMapPath,
      envVars,
    })
    return await worker.fetch(req)
  } catch (e) {
    const error = { msg: e.toString() }
    return new Response(JSON.stringify(error), {
      status: 500,
      headers: { 'Content-Type': 'application/json' },
    })
  }
})
"""

[[config.mounts]]
filePath = "/volumes/logs/vector.yml"
content = """api:
  enabled: true
  address: 0.0.0.0:9001

sources:
  docker_host:
    type: docker_logs
    exclude_containers:
      - ${container_name_prefix}-vector

transforms:
  project_logs:
    type: remap
    inputs:
      - docker_host
    source: |-
      .project = "default"
      .event_message = del(.message)
      .appname = replace!(del(.container_name), "${container_name_prefix}", "supabase")
      del(.container_created_at)
      del(.container_id)
      del(.source_type)
      del(.stream)
      del(.label)
      del(.image)
      del(.host)
      del(.stream)
  router:
    type: route
    inputs:
      - project_logs
    route:
      kong: '.appname == "supabase-kong"'
      auth: '.appname == "supabase-auth"'
      rest: '.appname == "supabase-rest"'
      realtime: '.appname == "realtime-dev.supabase-realtime"'
      storage: '.appname == "supabase-storage"'
      functions: '.appname == "supabase-edge-functions"'
      db: '.appname == "supabase-db"'
  # Ignores non nginx errors since they are related with kong booting up
  kong_logs:
    type: remap
    inputs:
      - router.kong
    source: |-
      req, err = parse_nginx_log(.event_message, "combined")
      if err == null {
          .timestamp = req.timestamp
          .metadata.request.headers.referer = req.referer
          .metadata.request.headers.user_agent = req.agent
          .metadata.request.headers.cf_connecting_ip = req.client
          .metadata.request.method = req.method
          .metadata.request.path = req.path
          .metadata.request.protocol = req.protocol
          .metadata.response.status_code = req.status
      }
      if err != null {
        abort
      }
  # Ignores non nginx errors since they are related with kong booting up
  kong_err:
    type: remap
    inputs:
      - router.kong
    source: |-
      .metadata.request.method = "GET"
      .metadata.response.status_code = 200
      parsed, err = parse_nginx_log(.event_message, "error")
      if err == null {
          .timestamp = parsed.timestamp
          .severity = parsed.severity
          .metadata.request.host = parsed.host
          .metadata.request.headers.cf_connecting_ip = parsed.client
          url, err = split(parsed.request, " ")
          if err == null {
              .metadata.request.method = url[0]
              .metadata.request.path = url[1]
              .metadata.request.protocol = url[2]
          }
      }
      if err != null {
        abort
      }
  # Gotrue logs are structured json strings which frontend parses directly. But we keep metadata for consistency.
  auth_logs:
    type: remap
    inputs:
      - router.auth
    source: |-
      parsed, err = parse_json(.event_message)
      if err == null {
          .metadata.timestamp = parsed.time
          .metadata = merge!(.metadata, parsed)
      }
  # PostgREST logs are structured so we separate timestamp from message using regex
  rest_logs:
    type: remap
    inputs:
      - router.rest
    source: |-
      parsed, err = parse_regex(.event_message, r'^(?P<time>.*): (?P<msg>.*)$')
      if err == null {
          .event_message = parsed.msg
          .timestamp = to_timestamp!(parsed.time)
          .metadata.host = .project
      }
  # Realtime logs are structured so we parse the severity level using regex (ignore time because it has no date)
  realtime_logs:
    type: remap
    inputs:
      - router.realtime
    source: |-
      .metadata.project = del(.project)
      .metadata.external_id = .metadata.project
      parsed, err = parse_regex(.event_message, r'^(?P<time>\\d+:\\d+:\\d+\\.\\d+) \\[(?P<level>\\w+)\\] (?P<msg>.*)$')
      if err == null {
          .event_message = parsed.msg
          .metadata.level = parsed.level
      }
  # Storage logs may contain json objects so we parse them for completeness
  storage_logs:
    type: remap
    inputs:
      - router.storage
    source: |-
      .metadata.project = del(.project)
      .metadata.tenantId = .metadata.project
      parsed, err = parse_json(.event_message)
      if err == null {
          .event_message = parsed.msg
          .metadata.level = parsed.level
          .metadata.timestamp = parsed.time
          .metadata.context[0].host = parsed.hostname
          .metadata.context[0].pid = parsed.pid
      }
  # Postgres logs some messages to stderr which we map to warning severity level
  db_logs:
    type: remap
    inputs:
      - router.db
    source: |-
      .metadata.host = "db-default"
      .metadata.parsed.timestamp = .timestamp

      parsed, err = parse_regex(.event_message, r'.*(?P<level>INFO|NOTICE|WARNING|ERROR|LOG|FATAL|PANIC?):.*', numeric_groups: true)

      if err != null || parsed == null {
        .metadata.parsed.error_severity = "info"
      }
      if parsed != null {
       .metadata.parsed.error_severity = parsed.level
      }
      if .metadata.parsed.error_severity == "info" {
          .metadata.parsed.error_severity = "log"
      }
      .metadata.parsed.error_severity = upcase!(.metadata.parsed.error_severity)

sinks:
  logflare_auth:
    type: 'http'
    inputs:
      - auth_logs
    encoding:
      codec: 'json'
    method: 'post'
    request:
      retry_max_duration_secs: 10
    uri: 'http://analytics:4000/api/logs?source_name=gotrue.logs.prod&api_key=${LOGFLARE_API_KEY?LOGFLARE_API_KEY is required}'
  logflare_realtime:
    type: 'http'
    inputs:
      - realtime_logs
    encoding:
      codec: 'json'
    method: 'post'
    request:
      retry_max_duration_secs: 10
    uri: 'http://analytics:4000/api/logs?source_name=realtime.logs.prod&api_key=${LOGFLARE_API_KEY?LOGFLARE_API_KEY is required}'
  logflare_rest:
    type: 'http'
    inputs:
      - rest_logs
    encoding:
      codec: 'json'
    method: 'post'
    request:
      retry_max_duration_secs: 10
    uri: 'http://analytics:4000/api/logs?source_name=postgREST.logs.prod&api_key=${LOGFLARE_API_KEY?LOGFLARE_API_KEY is required}'
  logflare_db:
    type: 'http'
    inputs:
      - db_logs
    encoding:
      codec: 'json'
    method: 'post'
    request:
      retry_max_duration_secs: 10
    # We must route the sink through kong because ingesting logs before logflare is fully initialised will
    # lead to broken queries from studio. This works by the assumption that containers are started in the
    # following order: vector > db > logflare > kong
    uri: 'http://kong:8000/analytics/v1/api/logs?source_name=postgres.logs&api_key=${LOGFLARE_API_KEY?LOGFLARE_API_KEY is required}'
  logflare_functions:
    type: 'http'
    inputs:
      - router.functions
    encoding:
      codec: 'json'
    method: 'post'
    request:
      retry_max_duration_secs: 10
    uri: 'http://analytics:4000/api/logs?source_name=deno-relay-logs&api_key=${LOGFLARE_API_KEY?LOGFLARE_API_KEY is required}'
  logflare_storage:
    type: 'http'
    inputs:
      - storage_logs
    encoding:
      codec: 'json'
    method: 'post'
    request:
      retry_max_duration_secs: 10
    uri: 'http://analytics:4000/api/logs?source_name=storage.logs.prod.2&api_key=${LOGFLARE_API_KEY?LOGFLARE_API_KEY is required}'
  logflare_kong:
    type: 'http'
    inputs:
      - kong_logs
      - kong_err
    encoding:
      codec: 'json'
    method: 'post'
    request:
      retry_max_duration_secs: 10
    uri: 'http://analytics:4000/api/logs?source_name=cloudflare.logs.prod&api_key=${LOGFLARE_API_KEY?LOGFLARE_API_KEY is required}'
"""

[[config.mounts]]
filePath = "/volumes/pooler/pooler.exs"
content = """{:ok, _} = Application.ensure_all_started(:supavisor)

{:ok, version} =
  case Supavisor.Repo.query!("select version()") do
    %{rows: [[ver]]} -> Supavisor.Helpers.parse_pg_version(ver)
    _ -> nil
  end

params = %{
  "external_id" => System.get_env("POOLER_TENANT_ID"),
  "db_host" => "db",
  "db_port" => System.get_env("POSTGRES_PORT"),
  "db_database" => System.get_env("POSTGRES_DB"),
  "require_user" => false,
  "auth_query" => "SELECT * FROM pgbouncer.get_auth($1)",
  "default_max_clients" => System.get_env("POOLER_MAX_CLIENT_CONN"),
  "default_pool_size" => System.get_env("POOLER_DEFAULT_POOL_SIZE"),
  "default_parameter_status" => %{"server_version" => version},
  "users" => [%{
    "db_user" => "pgbouncer",
    "db_password" => System.get_env("POSTGRES_PASSWORD"),
    "mode_type" => System.get_env("POOLER_POOL_MODE"),
    "pool_size" => System.get_env("POOLER_DEFAULT_POOL_SIZE"),
    "is_manager" => true
  }]
}

if !Supavisor.Tenants.get_tenant_by_external_id(params["external_id"]) do
  {:ok, _} = Supavisor.Tenants.create_tenant(params)
end
"""
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogIiMgVXNhZ2VcbiMgICBTdGFydDogICAgICAgICAgICAgIGRvY2tlciBjb21wb3NlIHVwXG4jICAgV2l0aCBoZWxwZXJzOiAgICAgICBkb2NrZXIgY29tcG9zZSAtZiBkb2NrZXItY29tcG9zZS55bWwgLWYgLi9kZXYvZG9ja2VyLWNvbXBvc2UuZGV2LnltbCB1cFxuIyAgIFN0b3A6ICAgICAgICAgICAgICAgZG9ja2VyIGNvbXBvc2UgZG93blxuIyAgIERlc3Ryb3k6ICAgICAgICAgICAgZG9ja2VyIGNvbXBvc2UgLWYgZG9ja2VyLWNvbXBvc2UueW1sIC1mIC4vZGV2L2RvY2tlci1jb21wb3NlLmRldi55bWwgZG93biAtdiAtLXJlbW92ZS1vcnBoYW5zXG4jICAgUmVzZXQgZXZlcnl0aGluZzogIC4vcmVzZXQuc2hcblxubmFtZTogc3VwYWJhc2Vcblxuc2VydmljZXM6XG5cbiAgc3R1ZGlvOlxuICAgIGNvbnRhaW5lcl9uYW1lOiAke0NPTlRBSU5FUl9QUkVGSVh9LXN0dWRpb1xuICAgIGltYWdlOiBzdXBhYmFzZS9zdHVkaW86MjAyNS4wNC4yMS1zaGEtMTczY2M1NlxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OlxuICAgICAgICBbXG4gICAgICAgICAgXCJDTURcIixcbiAgICAgICAgICBcIm5vZGVcIixcbiAgICAgICAgICBcIi1lXCIsXG4gICAgICAgICAgXCJmZXRjaCgnaHR0cDovL3N0dWRpbzozMDAwL2FwaS9wbGF0Zm9ybS9wcm9maWxlJykudGhlbigocikgPT4ge2lmIChyLnN0YXR1cyAhPT0gMjAwKSB0aHJvdyBuZXcgRXJyb3Ioci5zdGF0dXMpfSlcIlxuICAgICAgICBdXG4gICAgICB0aW1lb3V0OiAxMHNcbiAgICAgIGludGVydmFsOiA1c1xuICAgICAgcmV0cmllczogM1xuICAgIGRlcGVuZHNfb246XG4gICAgICBhbmFseXRpY3M6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9oZWFsdGh5XG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBTVFVESU9fUEdfTUVUQV9VUkw6IGh0dHA6Ly9tZXRhOjgwODBcbiAgICAgIFBPU1RHUkVTX1BBU1NXT1JEOiAke1BPU1RHUkVTX1BBU1NXT1JEfVxuXG4gICAgICBERUZBVUxUX09SR0FOSVpBVElPTl9OQU1FOiAke1NUVURJT19ERUZBVUxUX09SR0FOSVpBVElPTn1cbiAgICAgIERFRkFVTFRfUFJPSkVDVF9OQU1FOiAke1NUVURJT19ERUZBVUxUX1BST0pFQ1R9XG4gICAgICBPUEVOQUlfQVBJX0tFWTogJHtPUEVOQUlfQVBJX0tFWTotfVxuXG4gICAgICBTVVBBQkFTRV9VUkw6ICR7U1VQQUJBU0VfUFVCTElDX1VSTH1cbiAgICAgIFNVUEFCQVNFX1BVQkxJQ19VUkw6ICR7U1VQQUJBU0VfUFVCTElDX1VSTH1cbiAgICAgIFNVUEFCQVNFX0FOT05fS0VZOiAke0FOT05fS0VZfVxuICAgICAgU1VQQUJBU0VfU0VSVklDRV9LRVk6ICR7U0VSVklDRV9ST0xFX0tFWX1cbiAgICAgIEFVVEhfSldUX1NFQ1JFVDogJHtKV1RfU0VDUkVUfVxuXG4gICAgICBMT0dGTEFSRV9BUElfS0VZOiAke0xPR0ZMQVJFX0FQSV9LRVl9XG4gICAgICBMT0dGTEFSRV9VUkw6IGh0dHA6Ly9hbmFseXRpY3M6NDAwMFxuICAgICAgTkVYVF9QVUJMSUNfRU5BQkxFX0xPR1M6IHRydWVcbiAgICAgICMgQ29tbWVudCB0byB1c2UgQmlnIFF1ZXJ5IGJhY2tlbmQgZm9yIGFuYWx5dGljc1xuICAgICAgTkVYVF9BTkFMWVRJQ1NfQkFDS0VORF9QUk9WSURFUjogcG9zdGdyZXNcbiAgICAgICMgVW5jb21tZW50IHRvIHVzZSBCaWcgUXVlcnkgYmFja2VuZCBmb3IgYW5hbHl0aWNzXG4gICAgICAjIE5FWFRfQU5BTFlUSUNTX0JBQ0tFTkRfUFJPVklERVI6IGJpZ3F1ZXJ5XG5cbiAga29uZzpcbiAgICBjb250YWluZXJfbmFtZTogJHtDT05UQUlORVJfUFJFRklYfS1rb25nXG4gICAgaW1hZ2U6IGtvbmc6Mi44LjFcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgICMgcG9ydHM6XG4gICAgIyAgIC0gJHtLT05HX0hUVFBfUE9SVH06ODAwMC90Y3BcbiAgICAjICAgLSAke0tPTkdfSFRUUFNfUE9SVH06ODQ0My90Y3BcbiAgICBleHBvc2U6XG4gICAgICAtIDgwMDBcbiAgICAgIC0gODQ0M1xuICAgIHZvbHVtZXM6XG4gICAgICAjIGh0dHBzOi8vZ2l0aHViLmNvbS9zdXBhYmFzZS9zdXBhYmFzZS9pc3N1ZXMvMTI2NjFcbiAgICAgIC0gLi4vZmlsZXMvdm9sdW1lcy9hcGkva29uZy55bWw6L2hvbWUva29uZy90ZW1wLnltbDpybyx6XG4gICAgZGVwZW5kc19vbjpcbiAgICAgIGFuYWx5dGljczpcbiAgICAgICAgY29uZGl0aW9uOiBzZXJ2aWNlX2hlYWx0aHlcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIEtPTkdfREFUQUJBU0U6IFwib2ZmXCJcbiAgICAgIEtPTkdfREVDTEFSQVRJVkVfQ09ORklHOiAvaG9tZS9rb25nL2tvbmcueW1sXG4gICAgICAjIGh0dHBzOi8vZ2l0aHViLmNvbS9zdXBhYmFzZS9jbGkvaXNzdWVzLzE0XG4gICAgICBLT05HX0ROU19PUkRFUjogTEFTVCxBLENOQU1FXG4gICAgICBLT05HX1BMVUdJTlM6IHJlcXVlc3QtdHJhbnNmb3JtZXIsY29ycyxrZXktYXV0aCxhY2wsYmFzaWMtYXV0aFxuICAgICAgS09OR19OR0lOWF9QUk9YWV9QUk9YWV9CVUZGRVJfU0laRTogMTYwa1xuICAgICAgS09OR19OR0lOWF9QUk9YWV9QUk9YWV9CVUZGRVJTOiA2NCAxNjBrXG4gICAgICBTVVBBQkFTRV9BTk9OX0tFWTogJHtBTk9OX0tFWX1cbiAgICAgIFNVUEFCQVNFX1NFUlZJQ0VfS0VZOiAke1NFUlZJQ0VfUk9MRV9LRVl9XG4gICAgICBEQVNIQk9BUkRfVVNFUk5BTUU6ICR7REFTSEJPQVJEX1VTRVJOQU1FfVxuICAgICAgREFTSEJPQVJEX1BBU1NXT1JEOiAke0RBU0hCT0FSRF9QQVNTV09SRH1cbiAgICAjIGh0dHBzOi8vdW5peC5zdGFja2V4Y2hhbmdlLmNvbS9hLzI5NDgzN1xuICAgIGVudHJ5cG9pbnQ6IGJhc2ggLWMgJ2V2YWwgXCJlY2hvIFxcXCIkJChjYXQgfi90ZW1wLnltbClcXFwiXCIgPiB+L2tvbmcueW1sICYmIC9kb2NrZXItZW50cnlwb2ludC5zaCBrb25nIGRvY2tlci1zdGFydCdcblxuICBhdXRoOlxuICAgIGNvbnRhaW5lcl9uYW1lOiAke0NPTlRBSU5FUl9QUkVGSVh9LWF1dGhcbiAgICBpbWFnZTogc3VwYWJhc2UvZ290cnVlOnYyLjE3MS4wXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6XG4gICAgICAgIFtcbiAgICAgICAgICBcIkNNRFwiLFxuICAgICAgICAgIFwid2dldFwiLFxuICAgICAgICAgIFwiLS1uby12ZXJib3NlXCIsXG4gICAgICAgICAgXCItLXRyaWVzPTFcIixcbiAgICAgICAgICBcIi0tc3BpZGVyXCIsXG4gICAgICAgICAgXCJodHRwOi8vbG9jYWxob3N0Ojk5OTkvaGVhbHRoXCJcbiAgICAgICAgXVxuICAgICAgdGltZW91dDogNXNcbiAgICAgIGludGVydmFsOiA1c1xuICAgICAgcmV0cmllczogM1xuICAgIGRlcGVuZHNfb246XG4gICAgICBkYjpcbiAgICAgICAgIyBEaXNhYmxlIHRoaXMgaWYgeW91IGFyZSB1c2luZyBhbiBleHRlcm5hbCBQb3N0Z3JlcyBkYXRhYmFzZVxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2VfaGVhbHRoeVxuICAgICAgYW5hbHl0aWNzOlxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2VfaGVhbHRoeVxuICAgIGVudmlyb25tZW50OlxuICAgICAgIyB0aGUgbmV4dCBsaW5lIHNlZW1zIHJlcXVpcmVkIGlmIHlvdSB3YW50IHRvIGJlIGFibGUgdG8gc2VuZCBtYWlscyBmcm9tIHRoZSBzdXBhYmFzZSBHVUlcbiAgICAgIEdPVFJVRV9NQUlMRVJfRVhURVJOQUxfSE9TVFM6IGtvbmcsJHtTVVBBQkFTRV9IT1NUfVxuICAgICAgR09UUlVFX0FQSV9IT1NUOiAwLjAuMC4wXG4gICAgICBHT1RSVUVfQVBJX1BPUlQ6IDk5OTlcbiAgICAgIEFQSV9FWFRFUk5BTF9VUkw6ICR7QVBJX0VYVEVSTkFMX1VSTH1cblxuICAgICAgR09UUlVFX0RCX0RSSVZFUjogcG9zdGdyZXNcbiAgICAgIEdPVFJVRV9EQl9EQVRBQkFTRV9VUkw6IHBvc3RncmVzOi8vc3VwYWJhc2VfYXV0aF9hZG1pbjoke1BPU1RHUkVTX1BBU1NXT1JEfUAke1BPU1RHUkVTX0hPU1R9OiR7UE9TVEdSRVNfUE9SVH0vJHtQT1NUR1JFU19EQn1cblxuICAgICAgR09UUlVFX1NJVEVfVVJMOiAke1NJVEVfVVJMfVxuICAgICAgR09UUlVFX1VSSV9BTExPV19MSVNUOiAke0FERElUSU9OQUxfUkVESVJFQ1RfVVJMU31cbiAgICAgIEdPVFJVRV9ESVNBQkxFX1NJR05VUDogJHtESVNBQkxFX1NJR05VUH1cblxuICAgICAgR09UUlVFX0pXVF9BRE1JTl9ST0xFUzogc2VydmljZV9yb2xlXG4gICAgICBHT1RSVUVfSldUX0FVRDogYXV0aGVudGljYXRlZFxuICAgICAgR09UUlVFX0pXVF9ERUZBVUxUX0dST1VQX05BTUU6IGF1dGhlbnRpY2F0ZWRcbiAgICAgIEdPVFJVRV9KV1RfRVhQOiAke0pXVF9FWFBJUll9XG4gICAgICBHT1RSVUVfSldUX1NFQ1JFVDogJHtKV1RfU0VDUkVUfVxuXG4gICAgICBHT1RSVUVfRVhURVJOQUxfRU1BSUxfRU5BQkxFRDogJHtFTkFCTEVfRU1BSUxfU0lHTlVQfVxuICAgICAgR09UUlVFX0VYVEVSTkFMX0FOT05ZTU9VU19VU0VSU19FTkFCTEVEOiAke0VOQUJMRV9BTk9OWU1PVVNfVVNFUlN9XG4gICAgICBHT1RSVUVfTUFJTEVSX0FVVE9DT05GSVJNOiAke0VOQUJMRV9FTUFJTF9BVVRPQ09ORklSTX1cblxuICAgICAgIyBVbmNvbW1lbnQgdG8gYnlwYXNzIG5vbmNlIGNoZWNrIGluIElEIFRva2VuIGZsb3cuIENvbW1vbmx5IHNldCB0byB0cnVlIHdoZW4gdXNpbmcgR29vZ2xlIFNpZ24gSW4gb24gbW9iaWxlLlxuICAgICAgIyBHT1RSVUVfRVhURVJOQUxfU0tJUF9OT05DRV9DSEVDSzogdHJ1ZVxuXG4gICAgICAjIEdPVFJVRV9NQUlMRVJfU0VDVVJFX0VNQUlMX0NIQU5HRV9FTkFCTEVEOiB0cnVlXG4gICAgICAjIEdPVFJVRV9TTVRQX01BWF9GUkVRVUVOQ1k6IDFzXG4gICAgICBHT1RSVUVfU01UUF9BRE1JTl9FTUFJTDogJHtTTVRQX0FETUlOX0VNQUlMfVxuICAgICAgR09UUlVFX1NNVFBfSE9TVDogJHtTTVRQX0hPU1R9XG4gICAgICBHT1RSVUVfU01UUF9QT1JUOiAke1NNVFBfUE9SVH1cbiAgICAgIEdPVFJVRV9TTVRQX1VTRVI6ICR7U01UUF9VU0VSfVxuICAgICAgR09UUlVFX1NNVFBfUEFTUzogJHtTTVRQX1BBU1N9XG4gICAgICBHT1RSVUVfU01UUF9TRU5ERVJfTkFNRTogJHtTTVRQX1NFTkRFUl9OQU1FfVxuICAgICAgR09UUlVFX01BSUxFUl9VUkxQQVRIU19JTlZJVEU6ICR7TUFJTEVSX1VSTFBBVEhTX0lOVklURX1cbiAgICAgIEdPVFJVRV9NQUlMRVJfVVJMUEFUSFNfQ09ORklSTUFUSU9OOiAke01BSUxFUl9VUkxQQVRIU19DT05GSVJNQVRJT059XG4gICAgICBHT1RSVUVfTUFJTEVSX1VSTFBBVEhTX1JFQ09WRVJZOiAke01BSUxFUl9VUkxQQVRIU19SRUNPVkVSWX1cbiAgICAgIEdPVFJVRV9NQUlMRVJfVVJMUEFUSFNfRU1BSUxfQ0hBTkdFOiAke01BSUxFUl9VUkxQQVRIU19FTUFJTF9DSEFOR0V9XG5cbiAgICAgIEdPVFJVRV9FWFRFUk5BTF9QSE9ORV9FTkFCTEVEOiAke0VOQUJMRV9QSE9ORV9TSUdOVVB9XG4gICAgICBHT1RSVUVfU01TX0FVVE9DT05GSVJNOiAke0VOQUJMRV9QSE9ORV9BVVRPQ09ORklSTX1cbiAgICAgICMgVW5jb21tZW50IHRvIGVuYWJsZSBjdXN0b20gYWNjZXNzIHRva2VuIGhvb2suIFBsZWFzZSBzZWU6IGh0dHBzOi8vc3VwYWJhc2UuY29tL2RvY3MvZ3VpZGVzL2F1dGgvYXV0aC1ob29rcyBmb3IgZnVsbCBsaXN0IG9mIGhvb2tzIGFuZCBhZGRpdGlvbmFsIGRldGFpbHMgYWJvdXQgY3VzdG9tX2FjY2Vzc190b2tlbl9ob29rXG5cbiAgICAgICMgR09UUlVFX0hPT0tfQ1VTVE9NX0FDQ0VTU19UT0tFTl9FTkFCTEVEOiBcInRydWVcIlxuICAgICAgIyBHT1RSVUVfSE9PS19DVVNUT01fQUNDRVNTX1RPS0VOX1VSSTogXCJwZy1mdW5jdGlvbnM6Ly9wb3N0Z3Jlcy9wdWJsaWMvY3VzdG9tX2FjY2Vzc190b2tlbl9ob29rXCJcbiAgICAgICMgR09UUlVFX0hPT0tfQ1VTVE9NX0FDQ0VTU19UT0tFTl9TRUNSRVRTOiBcIjxzdGFuZGFyZC1iYXNlNjQtc2VjcmV0PlwiXG5cbiAgICAgICMgR09UUlVFX0hPT0tfTUZBX1ZFUklGSUNBVElPTl9BVFRFTVBUX0VOQUJMRUQ6IFwidHJ1ZVwiXG4gICAgICAjIEdPVFJVRV9IT09LX01GQV9WRVJJRklDQVRJT05fQVRURU1QVF9VUkk6IFwicGctZnVuY3Rpb25zOi8vcG9zdGdyZXMvcHVibGljL21mYV92ZXJpZmljYXRpb25fYXR0ZW1wdFwiXG5cbiAgICAgICMgR09UUlVFX0hPT0tfUEFTU1dPUkRfVkVSSUZJQ0FUSU9OX0FUVEVNUFRfRU5BQkxFRDogXCJ0cnVlXCJcbiAgICAgICMgR09UUlVFX0hPT0tfUEFTU1dPUkRfVkVSSUZJQ0FUSU9OX0FUVEVNUFRfVVJJOiBcInBnLWZ1bmN0aW9uczovL3Bvc3RncmVzL3B1YmxpYy9wYXNzd29yZF92ZXJpZmljYXRpb25fYXR0ZW1wdFwiXG5cbiAgICAgICMgR09UUlVFX0hPT0tfU0VORF9TTVNfRU5BQkxFRDogXCJmYWxzZVwiXG4gICAgICAjIEdPVFJVRV9IT09LX1NFTkRfU01TX1VSSTogXCJwZy1mdW5jdGlvbnM6Ly9wb3N0Z3Jlcy9wdWJsaWMvY3VzdG9tX2FjY2Vzc190b2tlbl9ob29rXCJcbiAgICAgICMgR09UUlVFX0hPT0tfU0VORF9TTVNfU0VDUkVUUzogXCJ2MSx3aHNlY19WR2hwY3lCcGN5QmhiaUJsZUdGdGNHeGxJRzltSUdFZ2MyaHZjblJsY2lCQ1lYTmxOalFnYzNSeWFXNW5cIlxuXG4gICAgICAjIEdPVFJVRV9IT09LX1NFTkRfRU1BSUxfRU5BQkxFRDogXCJmYWxzZVwiXG4gICAgICAjIEdPVFJVRV9IT09LX1NFTkRfRU1BSUxfVVJJOiBcImh0dHA6Ly9ob3N0LmRvY2tlci5pbnRlcm5hbDo1NDMyMS9mdW5jdGlvbnMvdjEvZW1haWxfc2VuZGVyXCJcbiAgICAgICMgR09UUlVFX0hPT0tfU0VORF9FTUFJTF9TRUNSRVRTOiBcInYxLHdoc2VjX1ZHaHBjeUJwY3lCaGJpQmxlR0Z0Y0d4bElHOW1JR0VnYzJodmNuUmxjaUJDWVhObE5qUWdjM1J5YVc1blwiXG5cbiAgcmVzdDpcbiAgICBjb250YWluZXJfbmFtZTogJHtDT05UQUlORVJfUFJFRklYfS1yZXN0XG4gICAgaW1hZ2U6IHBvc3RncmVzdC9wb3N0Z3Jlc3Q6djEyLjIuMTFcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGRlcGVuZHNfb246XG4gICAgICBkYjpcbiAgICAgICAgIyBEaXNhYmxlIHRoaXMgaWYgeW91IGFyZSB1c2luZyBhbiBleHRlcm5hbCBQb3N0Z3JlcyBkYXRhYmFzZVxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2VfaGVhbHRoeVxuICAgICAgYW5hbHl0aWNzOlxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2VfaGVhbHRoeVxuICAgIGVudmlyb25tZW50OlxuICAgICAgUEdSU1RfREJfVVJJOiBwb3N0Z3JlczovL2F1dGhlbnRpY2F0b3I6JHtQT1NUR1JFU19QQVNTV09SRH1AJHtQT1NUR1JFU19IT1NUfToke1BPU1RHUkVTX1BPUlR9LyR7UE9TVEdSRVNfREJ9XG4gICAgICBQR1JTVF9EQl9TQ0hFTUFTOiAke1BHUlNUX0RCX1NDSEVNQVN9XG4gICAgICBQR1JTVF9EQl9BTk9OX1JPTEU6IGFub25cbiAgICAgIFBHUlNUX0pXVF9TRUNSRVQ6ICR7SldUX1NFQ1JFVH1cbiAgICAgIFBHUlNUX0RCX1VTRV9MRUdBQ1lfR1VDUzogXCJmYWxzZVwiXG4gICAgICBQR1JTVF9BUFBfU0VUVElOR1NfSldUX1NFQ1JFVDogJHtKV1RfU0VDUkVUfVxuICAgICAgUEdSU1RfQVBQX1NFVFRJTkdTX0pXVF9FWFA6ICR7SldUX0VYUElSWX1cbiAgICBjb21tYW5kOlxuICAgICAgW1xuICAgICAgICBcInBvc3RncmVzdFwiXG4gICAgICBdXG5cbiAgcmVhbHRpbWU6XG4gICAgIyBUaGlzIGNvbnRhaW5lciBuYW1lIGxvb2tzIGluY29uc2lzdGVudCBidXQgaXMgY29ycmVjdCBiZWNhdXNlIHJlYWx0aW1lIGNvbnN0cnVjdHMgdGVuYW50IGlkIGJ5IHBhcnNpbmcgdGhlIHN1YmRvbWFpblxuICAgIGNvbnRhaW5lcl9uYW1lOiByZWFsdGltZS1kZXYuJHtDT05UQUlORVJfUFJFRklYfS1yZWFsdGltZVxuICAgIGltYWdlOiBzdXBhYmFzZS9yZWFsdGltZTp2Mi4zNC40N1xuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIGRiOlxuICAgICAgICAjIERpc2FibGUgdGhpcyBpZiB5b3UgYXJlIHVzaW5nIGFuIGV4dGVybmFsIFBvc3RncmVzIGRhdGFiYXNlXG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9oZWFsdGh5XG4gICAgICBhbmFseXRpY3M6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9oZWFsdGh5XG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OlxuICAgICAgICBbXG4gICAgICAgICAgXCJDTURcIixcbiAgICAgICAgICBcImN1cmxcIixcbiAgICAgICAgICBcIi1zU2ZMXCIsXG4gICAgICAgICAgXCItLWhlYWRcIixcbiAgICAgICAgICBcIi1vXCIsXG4gICAgICAgICAgXCIvZGV2L251bGxcIixcbiAgICAgICAgICBcIi1IXCIsXG4gICAgICAgICAgXCJBdXRob3JpemF0aW9uOiBCZWFyZXIgJHtBTk9OX0tFWX1cIixcbiAgICAgICAgICBcImh0dHA6Ly9sb2NhbGhvc3Q6NDAwMC9hcGkvdGVuYW50cy9yZWFsdGltZS1kZXYvaGVhbHRoXCJcbiAgICAgICAgXVxuICAgICAgdGltZW91dDogNXNcbiAgICAgIGludGVydmFsOiA1c1xuICAgICAgcmV0cmllczogM1xuICAgIGVudmlyb25tZW50OlxuICAgICAgUE9SVDogNDAwMFxuICAgICAgREJfSE9TVDogJHtQT1NUR1JFU19IT1NUfVxuICAgICAgREJfUE9SVDogJHtQT1NUR1JFU19QT1JUfVxuICAgICAgREJfVVNFUjogc3VwYWJhc2VfYWRtaW5cbiAgICAgIERCX1BBU1NXT1JEOiAke1BPU1RHUkVTX1BBU1NXT1JEfVxuICAgICAgREJfTkFNRTogJHtQT1NUR1JFU19EQn1cbiAgICAgIERCX0FGVEVSX0NPTk5FQ1RfUVVFUlk6ICdTRVQgc2VhcmNoX3BhdGggVE8gX3JlYWx0aW1lJ1xuICAgICAgREJfRU5DX0tFWTogc3VwYWJhc2VyZWFsdGltZVxuICAgICAgQVBJX0pXVF9TRUNSRVQ6ICR7SldUX1NFQ1JFVH1cbiAgICAgIFNFQ1JFVF9LRVlfQkFTRTogJHtTRUNSRVRfS0VZX0JBU0V9XG4gICAgICBFUkxfQUZMQUdTOiAtcHJvdG9fZGlzdCBpbmV0X3RjcFxuICAgICAgRE5TX05PREVTOiBcIicnXCJcbiAgICAgIFJMSU1JVF9OT0ZJTEU6IFwiMTAwMDBcIlxuICAgICAgQVBQX05BTUU6IHJlYWx0aW1lXG4gICAgICBTRUVEX1NFTEZfSE9TVDogdHJ1ZVxuICAgICAgUlVOX0pBTklUT1I6IHRydWVcblxuICAjIFRvIHVzZSBTMyBiYWNrZWQgc3RvcmFnZTogZG9ja2VyIGNvbXBvc2UgLWYgZG9ja2VyLWNvbXBvc2UueW1sIC1mIGRvY2tlci1jb21wb3NlLnMzLnltbCB1cFxuICBzdG9yYWdlOlxuICAgIGNvbnRhaW5lcl9uYW1lOiAke0NPTlRBSU5FUl9QUkVGSVh9LXN0b3JhZ2VcbiAgICBpbWFnZTogc3VwYWJhc2Uvc3RvcmFnZS1hcGk6djEuMjIuN1xuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgdm9sdW1lczpcbiAgICAgIC0gLi4vZmlsZXMvdm9sdW1lcy9zdG9yYWdlOi92YXIvbGliL3N0b3JhZ2U6elxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDpcbiAgICAgICAgW1xuICAgICAgICAgIFwiQ01EXCIsXG4gICAgICAgICAgXCJ3Z2V0XCIsXG4gICAgICAgICAgXCItLW5vLXZlcmJvc2VcIixcbiAgICAgICAgICBcIi0tdHJpZXM9MVwiLFxuICAgICAgICAgIFwiLS1zcGlkZXJcIixcbiAgICAgICAgICBcImh0dHA6Ly9zdG9yYWdlOjUwMDAvc3RhdHVzXCJcbiAgICAgICAgXVxuICAgICAgdGltZW91dDogNXNcbiAgICAgIGludGVydmFsOiA1c1xuICAgICAgcmV0cmllczogM1xuICAgIGRlcGVuZHNfb246XG4gICAgICBkYjpcbiAgICAgICAgIyBEaXNhYmxlIHRoaXMgaWYgeW91IGFyZSB1c2luZyBhbiBleHRlcm5hbCBQb3N0Z3JlcyBkYXRhYmFzZVxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2VfaGVhbHRoeVxuICAgICAgcmVzdDpcbiAgICAgICAgY29uZGl0aW9uOiBzZXJ2aWNlX3N0YXJ0ZWRcbiAgICAgIGltZ3Byb3h5OlxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2Vfc3RhcnRlZFxuICAgIGVudmlyb25tZW50OlxuICAgICAgQU5PTl9LRVk6ICR7QU5PTl9LRVl9XG4gICAgICBTRVJWSUNFX0tFWTogJHtTRVJWSUNFX1JPTEVfS0VZfVxuICAgICAgUE9TVEdSRVNUX1VSTDogaHR0cDovL3Jlc3Q6MzAwMFxuICAgICAgUEdSU1RfSldUX1NFQ1JFVDogJHtKV1RfU0VDUkVUfVxuICAgICAgREFUQUJBU0VfVVJMOiBwb3N0Z3JlczovL3N1cGFiYXNlX3N0b3JhZ2VfYWRtaW46JHtQT1NUR1JFU19QQVNTV09SRH1AJHtQT1NUR1JFU19IT1NUfToke1BPU1RHUkVTX1BPUlR9LyR7UE9TVEdSRVNfREJ9XG4gICAgICBGSUxFX1NJWkVfTElNSVQ6IDUyNDI4ODAwXG4gICAgICBTVE9SQUdFX0JBQ0tFTkQ6IGZpbGVcbiAgICAgIEZJTEVfU1RPUkFHRV9CQUNLRU5EX1BBVEg6IC92YXIvbGliL3N0b3JhZ2VcbiAgICAgIFRFTkFOVF9JRDogc3R1YlxuICAgICAgIyBUT0RPOiBodHRwczovL2dpdGh1Yi5jb20vc3VwYWJhc2Uvc3RvcmFnZS1hcGkvaXNzdWVzLzU1XG4gICAgICBSRUdJT046IHN0dWJcbiAgICAgIEdMT0JBTF9TM19CVUNLRVQ6IHN0dWJcbiAgICAgIEVOQUJMRV9JTUFHRV9UUkFOU0ZPUk1BVElPTjogXCJ0cnVlXCJcbiAgICAgIElNR1BST1hZX1VSTDogaHR0cDovL2ltZ3Byb3h5OjUwMDFcblxuICBpbWdwcm94eTpcbiAgICBjb250YWluZXJfbmFtZTogJHtDT05UQUlORVJfUFJFRklYfS1pbWdwcm94eVxuICAgIGltYWdlOiBkYXJ0aHNpbS9pbWdwcm94eTp2My44LjBcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIHZvbHVtZXM6XG4gICAgICAtIC4uL2ZpbGVzL3ZvbHVtZXMvc3RvcmFnZTovdmFyL2xpYi9zdG9yYWdlOnpcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6XG4gICAgICAgIFtcbiAgICAgICAgICBcIkNNRFwiLFxuICAgICAgICAgIFwiaW1ncHJveHlcIixcbiAgICAgICAgICBcImhlYWx0aFwiXG4gICAgICAgIF1cbiAgICAgIHRpbWVvdXQ6IDVzXG4gICAgICBpbnRlcnZhbDogNXNcbiAgICAgIHJldHJpZXM6IDNcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIElNR1BST1hZX0JJTkQ6IFwiOjUwMDFcIlxuICAgICAgSU1HUFJPWFlfTE9DQUxfRklMRVNZU1RFTV9ST09UOiAvXG4gICAgICBJTUdQUk9YWV9VU0VfRVRBRzogXCJ0cnVlXCJcbiAgICAgIElNR1BST1hZX0VOQUJMRV9XRUJQX0RFVEVDVElPTjogJHtJTUdQUk9YWV9FTkFCTEVfV0VCUF9ERVRFQ1RJT059XG5cbiAgbWV0YTpcbiAgICBjb250YWluZXJfbmFtZTogJHtDT05UQUlORVJfUFJFRklYfS1tZXRhXG4gICAgaW1hZ2U6IHN1cGFiYXNlL3Bvc3RncmVzLW1ldGE6djAuODguOVxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIGRiOlxuICAgICAgICAjIERpc2FibGUgdGhpcyBpZiB5b3UgYXJlIHVzaW5nIGFuIGV4dGVybmFsIFBvc3RncmVzIGRhdGFiYXNlXG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9oZWFsdGh5XG4gICAgICBhbmFseXRpY3M6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9oZWFsdGh5XG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBQR19NRVRBX1BPUlQ6IDgwODBcbiAgICAgIFBHX01FVEFfREJfSE9TVDogJHtQT1NUR1JFU19IT1NUfVxuICAgICAgUEdfTUVUQV9EQl9QT1JUOiAke1BPU1RHUkVTX1BPUlR9XG4gICAgICBQR19NRVRBX0RCX05BTUU6ICR7UE9TVEdSRVNfREJ9XG4gICAgICBQR19NRVRBX0RCX1VTRVI6IHN1cGFiYXNlX2FkbWluXG4gICAgICBQR19NRVRBX0RCX1BBU1NXT1JEOiAke1BPU1RHUkVTX1BBU1NXT1JEfVxuXG4gIGZ1bmN0aW9uczpcbiAgICBjb250YWluZXJfbmFtZTogJHtDT05UQUlORVJfUFJFRklYfS1lZGdlLWZ1bmN0aW9uc1xuICAgIGltYWdlOiBzdXBhYmFzZS9lZGdlLXJ1bnRpbWU6djEuNjcuNFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgdm9sdW1lczpcbiAgICAgIC0gLi4vZmlsZXMvdm9sdW1lcy9mdW5jdGlvbnM6L2hvbWUvZGVuby9mdW5jdGlvbnM6WlxuICAgIGRlcGVuZHNfb246XG4gICAgICBhbmFseXRpY3M6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9oZWFsdGh5XG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBKV1RfU0VDUkVUOiAke0pXVF9TRUNSRVR9XG4gICAgICBTVVBBQkFTRV9VUkw6IGh0dHA6Ly9rb25nOjgwMDBcbiAgICAgIFNVUEFCQVNFX0FOT05fS0VZOiAke0FOT05fS0VZfVxuICAgICAgU1VQQUJBU0VfU0VSVklDRV9ST0xFX0tFWTogJHtTRVJWSUNFX1JPTEVfS0VZfVxuICAgICAgU1VQQUJBU0VfREJfVVJMOiBwb3N0Z3Jlc3FsOi8vcG9zdGdyZXM6JHtQT1NUR1JFU19QQVNTV09SRH1AJHtQT1NUR1JFU19IT1NUfToke1BPU1RHUkVTX1BPUlR9LyR7UE9TVEdSRVNfREJ9XG4gICAgICAjIFRPRE86IEFsbG93IGNvbmZpZ3VyaW5nIFZFUklGWV9KV1QgcGVyIGZ1bmN0aW9uLiBUaGlzIFBSIG1pZ2h0IGhlbHA6IGh0dHBzOi8vZ2l0aHViLmNvbS9zdXBhYmFzZS9jbGkvcHVsbC83ODZcbiAgICAgIFZFUklGWV9KV1Q6IFwiJHtGVU5DVElPTlNfVkVSSUZZX0pXVH1cIlxuICAgIGNvbW1hbmQ6XG4gICAgICBbXG4gICAgICAgIFwic3RhcnRcIixcbiAgICAgICAgXCItLW1haW4tc2VydmljZVwiLFxuICAgICAgICBcIi9ob21lL2Rlbm8vZnVuY3Rpb25zL21haW5cIlxuICAgICAgXVxuXG4gIGFuYWx5dGljczpcbiAgICBjb250YWluZXJfbmFtZTogJHtDT05UQUlORVJfUFJFRklYfS1hbmFseXRpY3NcbiAgICBpbWFnZTogc3VwYWJhc2UvbG9nZmxhcmU6MS4xMi4wXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICAjIHBvcnRzOlxuICAgICMgICAtIDQwMDA6NDAwMFxuICAgIGV4cG9zZTpcbiAgICAgIC0gNDAwMFxuICAgICMgVW5jb21tZW50IHRvIHVzZSBCaWcgUXVlcnkgYmFja2VuZCBmb3IgYW5hbHl0aWNzXG4gICAgIyB2b2x1bWVzOlxuICAgICMgICAtIHR5cGU6IGJpbmRcbiAgICAjICAgICBzb3VyY2U6ICR7UFdEfS9nY2xvdWQuanNvblxuICAgICMgICAgIHRhcmdldDogL29wdC9hcHAvcmVsL2xvZ2ZsYXJlL2Jpbi9nY2xvdWQuanNvblxuICAgICMgICAgIHJlYWRfb25seTogdHJ1ZVxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDpcbiAgICAgICAgW1xuICAgICAgICAgIFwiQ01EXCIsXG4gICAgICAgICAgXCJjdXJsXCIsXG4gICAgICAgICAgXCJodHRwOi8vbG9jYWxob3N0OjQwMDAvaGVhbHRoXCJcbiAgICAgICAgXVxuICAgICAgdGltZW91dDogNXNcbiAgICAgIGludGVydmFsOiA1c1xuICAgICAgcmV0cmllczogMTBcbiAgICBkZXBlbmRzX29uOlxuICAgICAgZGI6XG4gICAgICAgICMgRGlzYWJsZSB0aGlzIGlmIHlvdSBhcmUgdXNpbmcgYW4gZXh0ZXJuYWwgUG9zdGdyZXMgZGF0YWJhc2VcbiAgICAgICAgY29uZGl0aW9uOiBzZXJ2aWNlX2hlYWx0aHlcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIExPR0ZMQVJFX05PREVfSE9TVDogMTI3LjAuMC4xXG4gICAgICBEQl9VU0VSTkFNRTogc3VwYWJhc2VfYWRtaW5cbiAgICAgIERCX0RBVEFCQVNFOiBfc3VwYWJhc2VcbiAgICAgIERCX0hPU1ROQU1FOiAke1BPU1RHUkVTX0hPU1R9XG4gICAgICBEQl9QT1JUOiAke1BPU1RHUkVTX1BPUlR9XG4gICAgICBEQl9QQVNTV09SRDogJHtQT1NUR1JFU19QQVNTV09SRH1cbiAgICAgIERCX1NDSEVNQTogX2FuYWx5dGljc1xuICAgICAgTE9HRkxBUkVfQVBJX0tFWTogJHtMT0dGTEFSRV9BUElfS0VZfVxuICAgICAgTE9HRkxBUkVfU0lOR0xFX1RFTkFOVDogdHJ1ZVxuICAgICAgTE9HRkxBUkVfU1VQQUJBU0VfTU9ERTogdHJ1ZVxuICAgICAgTE9HRkxBUkVfTUlOX0NMVVNURVJfU0laRTogMVxuXG4gICAgICAjIENvbW1lbnQgdmFyaWFibGVzIHRvIHVzZSBCaWcgUXVlcnkgYmFja2VuZCBmb3IgYW5hbHl0aWNzXG4gICAgICBQT1NUR1JFU19CQUNLRU5EX1VSTDogcG9zdGdyZXNxbDovL3N1cGFiYXNlX2FkbWluOiR7UE9TVEdSRVNfUEFTU1dPUkR9QCR7UE9TVEdSRVNfSE9TVH06JHtQT1NUR1JFU19QT1JUfS9fc3VwYWJhc2VcbiAgICAgIFBPU1RHUkVTX0JBQ0tFTkRfU0NIRU1BOiBfYW5hbHl0aWNzXG4gICAgICBMT0dGTEFSRV9GRUFUVVJFX0ZMQUdfT1ZFUlJJREU6IG11bHRpYmFja2VuZD10cnVlXG4gICAgICAjIFVuY29tbWVudCB0byB1c2UgQmlnIFF1ZXJ5IGJhY2tlbmQgZm9yIGFuYWx5dGljc1xuICAgICAgIyBHT09HTEVfUFJPSkVDVF9JRDogJHtHT09HTEVfUFJPSkVDVF9JRH1cbiAgICAgICMgR09PR0xFX1BST0pFQ1RfTlVNQkVSOiAke0dPT0dMRV9QUk9KRUNUX05VTUJFUn1cblxuICAjIENvbW1lbnQgb3V0IGV2ZXJ5dGhpbmcgYmVsb3cgdGhpcyBwb2ludCBpZiB5b3UgYXJlIHVzaW5nIGFuIGV4dGVybmFsIFBvc3RncmVzIGRhdGFiYXNlXG4gIGRiOlxuICAgIGNvbnRhaW5lcl9uYW1lOiAke0NPTlRBSU5FUl9QUkVGSVh9LWRiXG4gICAgaW1hZ2U6IHN1cGFiYXNlL3Bvc3RncmVzOjE1LjguMS4wNjBcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIHZvbHVtZXM6XG4gICAgICAtIC4uL2ZpbGVzL3ZvbHVtZXMvZGIvcmVhbHRpbWUuc3FsOi9kb2NrZXItZW50cnlwb2ludC1pbml0ZGIuZC9taWdyYXRpb25zLzk5LXJlYWx0aW1lLnNxbDpaXG4gICAgICAjIE11c3QgYmUgc3VwZXJ1c2VyIHRvIGNyZWF0ZSBldmVudCB0cmlnZ2VyXG4gICAgICAtIC4uL2ZpbGVzL3ZvbHVtZXMvZGIvd2ViaG9va3Muc3FsOi9kb2NrZXItZW50cnlwb2ludC1pbml0ZGIuZC9pbml0LXNjcmlwdHMvOTgtd2ViaG9va3Muc3FsOlpcbiAgICAgICMgTXVzdCBiZSBzdXBlcnVzZXIgdG8gYWx0ZXIgcmVzZXJ2ZWQgcm9sZVxuICAgICAgLSAuLi9maWxlcy92b2x1bWVzL2RiL3JvbGVzLnNxbDovZG9ja2VyLWVudHJ5cG9pbnQtaW5pdGRiLmQvaW5pdC1zY3JpcHRzLzk5LXJvbGVzLnNxbDpaXG4gICAgICAjIEluaXRpYWxpemUgdGhlIGRhdGFiYXNlIHNldHRpbmdzIHdpdGggSldUX1NFQ1JFVCBhbmQgSldUX0VYUFxuICAgICAgLSAuLi9maWxlcy92b2x1bWVzL2RiL2p3dC5zcWw6L2RvY2tlci1lbnRyeXBvaW50LWluaXRkYi5kL2luaXQtc2NyaXB0cy85OS1qd3Quc3FsOlpcbiAgICAgICMgUEdEQVRBIGRpcmVjdG9yeSBpcyBwZXJzaXN0ZWQgYmV0d2VlbiByZXN0YXJ0c1xuICAgICAgLSAuLi9maWxlcy92b2x1bWVzL2RiL2RhdGE6L3Zhci9saWIvcG9zdGdyZXNxbC9kYXRhOlpcbiAgICAgICMgQ2hhbmdlcyByZXF1aXJlZCBmb3IgaW50ZXJuYWwgc3VwYWJhc2UgZGF0YSBzdWNoIGFzIF9hbmFseXRpY3NcbiAgICAgIC0gLi4vZmlsZXMvdm9sdW1lcy9kYi9fc3VwYWJhc2Uuc3FsOi9kb2NrZXItZW50cnlwb2ludC1pbml0ZGIuZC9taWdyYXRpb25zLzk3LV9zdXBhYmFzZS5zcWw6WlxuICAgICAgIyBDaGFuZ2VzIHJlcXVpcmVkIGZvciBBbmFseXRpY3Mgc3VwcG9ydFxuICAgICAgLSAuLi9maWxlcy92b2x1bWVzL2RiL2xvZ3Muc3FsOi9kb2NrZXItZW50cnlwb2ludC1pbml0ZGIuZC9taWdyYXRpb25zLzk5LWxvZ3Muc3FsOlpcbiAgICAgICMgQ2hhbmdlcyByZXF1aXJlZCBmb3IgUG9vbGVyIHN1cHBvcnRcbiAgICAgIC0gLi4vZmlsZXMvdm9sdW1lcy9kYi9wb29sZXIuc3FsOi9kb2NrZXItZW50cnlwb2ludC1pbml0ZGIuZC9taWdyYXRpb25zLzk5LXBvb2xlci5zcWw6WlxuICAgICAgIyBVc2UgbmFtZWQgdm9sdW1lIHRvIHBlcnNpc3QgcGdzb2RpdW0gZGVjcnlwdGlvbiBrZXkgYmV0d2VlbiByZXN0YXJ0c1xuICAgICAgLSBkYi1jb25maWc6L2V0Yy9wb3N0Z3Jlc3FsLWN1c3RvbVxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDpcbiAgICAgICAgW1xuICAgICAgICBcIkNNRFwiLFxuICAgICAgICBcInBnX2lzcmVhZHlcIixcbiAgICAgICAgXCItVVwiLFxuICAgICAgICBcInBvc3RncmVzXCIsXG4gICAgICAgIFwiLWhcIixcbiAgICAgICAgXCJsb2NhbGhvc3RcIlxuICAgICAgICBdXG4gICAgICBpbnRlcnZhbDogNXNcbiAgICAgIHRpbWVvdXQ6IDVzXG4gICAgICByZXRyaWVzOiAxMFxuICAgIGRlcGVuZHNfb246XG4gICAgICB2ZWN0b3I6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9oZWFsdGh5XG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBQT1NUR1JFU19IT1NUOiAvdmFyL3J1bi9wb3N0Z3Jlc3FsXG4gICAgICBQR1BPUlQ6ICR7UE9TVEdSRVNfUE9SVH1cbiAgICAgIFBPU1RHUkVTX1BPUlQ6ICR7UE9TVEdSRVNfUE9SVH1cbiAgICAgIFBHUEFTU1dPUkQ6ICR7UE9TVEdSRVNfUEFTU1dPUkR9XG4gICAgICBQT1NUR1JFU19QQVNTV09SRDogJHtQT1NUR1JFU19QQVNTV09SRH1cbiAgICAgIFBHREFUQUJBU0U6ICR7UE9TVEdSRVNfREJ9XG4gICAgICBQT1NUR1JFU19EQjogJHtQT1NUR1JFU19EQn1cbiAgICAgIEpXVF9TRUNSRVQ6ICR7SldUX1NFQ1JFVH1cbiAgICAgIEpXVF9FWFA6ICR7SldUX0VYUElSWX1cbiAgICBjb21tYW5kOlxuICAgICAgW1xuICAgICAgICBcInBvc3RncmVzXCIsXG4gICAgICAgIFwiLWNcIixcbiAgICAgICAgXCJjb25maWdfZmlsZT0vZXRjL3Bvc3RncmVzcWwvcG9zdGdyZXNxbC5jb25mXCIsXG4gICAgICAgIFwiLWNcIixcbiAgICAgICAgXCJsb2dfbWluX21lc3NhZ2VzPWZhdGFsXCIgIyBwcmV2ZW50cyBSZWFsdGltZSBwb2xsaW5nIHF1ZXJpZXMgZnJvbSBhcHBlYXJpbmcgaW4gbG9nc1xuICAgICAgXVxuXG4gIHZlY3RvcjpcbiAgICBjb250YWluZXJfbmFtZTogJHtDT05UQUlORVJfUFJFRklYfS12ZWN0b3JcbiAgICBpbWFnZTogdGltYmVyaW8vdmVjdG9yOjAuMjguMS1hbHBpbmVcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIHZvbHVtZXM6XG4gICAgICAtIC4uL2ZpbGVzL3ZvbHVtZXMvbG9ncy92ZWN0b3IueW1sOi9ldGMvdmVjdG9yL3ZlY3Rvci55bWw6cm8selxuICAgICAgLSAke0RPQ0tFUl9TT0NLRVRfTE9DQVRJT059Oi92YXIvcnVuL2RvY2tlci5zb2NrOnJvLHpcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6XG4gICAgICAgIFtcbiAgICAgICAgICBcIkNNRFwiLFxuICAgICAgICAgIFwid2dldFwiLFxuICAgICAgICAgIFwiLS1uby12ZXJib3NlXCIsXG4gICAgICAgICAgXCItLXRyaWVzPTFcIixcbiAgICAgICAgICBcIi0tc3BpZGVyXCIsXG4gICAgICAgICAgXCJodHRwOi8vdmVjdG9yOjkwMDEvaGVhbHRoXCJcbiAgICAgICAgXVxuICAgICAgdGltZW91dDogNXNcbiAgICAgIGludGVydmFsOiA1c1xuICAgICAgcmV0cmllczogM1xuICAgIGVudmlyb25tZW50OlxuICAgICAgTE9HRkxBUkVfQVBJX0tFWTogJHtMT0dGTEFSRV9BUElfS0VZfVxuICAgIGNvbW1hbmQ6XG4gICAgICBbXG4gICAgICAgIFwiLS1jb25maWdcIixcbiAgICAgICAgXCIvZXRjL3ZlY3Rvci92ZWN0b3IueW1sXCJcbiAgICAgIF1cbiAgICBzZWN1cml0eV9vcHQ6XG4gICAgICAtIFwibGFiZWw9ZGlzYWJsZVwiXG5cbiAgIyBVcGRhdGUgdGhlIERBVEFCQVNFX1VSTCBpZiB5b3UgYXJlIHVzaW5nIGFuIGV4dGVybmFsIFBvc3RncmVzIGRhdGFiYXNlXG4gIHN1cGF2aXNvcjpcbiAgICBjb250YWluZXJfbmFtZTogJHtDT05UQUlORVJfUFJFRklYfS1wb29sZXJcbiAgICBpbWFnZTogc3VwYWJhc2Uvc3VwYXZpc29yOjIuNS4xXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBwb3J0czogIyBleHBvc2Ugc3VwYXZpc29yIHRvIHRoZSBob3N0IHRvIGVuYWJsZSBkYiBwb29sZXIgY29ubmVjdGlvblxuICAgICAgLSAke1BPU1RHUkVTX1BPUlR9OjU0MzJcbiAgICAgIC0gJHtQT09MRVJfUFJPWFlfUE9SVF9UUkFOU0FDVElPTn06NjU0M1xuICAgIHZvbHVtZXM6XG4gICAgICAtIC4uL2ZpbGVzL3ZvbHVtZXMvcG9vbGVyL3Bvb2xlci5leHM6L2V0Yy9wb29sZXIvcG9vbGVyLmV4czpybyx6XG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OlxuICAgICAgICBbXG4gICAgICAgICAgXCJDTURcIixcbiAgICAgICAgICBcImN1cmxcIixcbiAgICAgICAgICBcIi1zU2ZMXCIsXG4gICAgICAgICAgXCItLWhlYWRcIixcbiAgICAgICAgICBcIi1vXCIsXG4gICAgICAgICAgXCIvZGV2L251bGxcIixcbiAgICAgICAgICBcImh0dHA6Ly8xMjcuMC4wLjE6NDAwMC9hcGkvaGVhbHRoXCJcbiAgICAgICAgXVxuICAgICAgaW50ZXJ2YWw6IDEwc1xuICAgICAgdGltZW91dDogNXNcbiAgICAgIHJldHJpZXM6IDVcbiAgICBkZXBlbmRzX29uOlxuICAgICAgZGI6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9oZWFsdGh5XG4gICAgICBhbmFseXRpY3M6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9oZWFsdGh5XG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBQT1JUOiA0MDAwXG4gICAgICBQT1NUR1JFU19QT1JUOiAke1BPU1RHUkVTX1BPUlR9XG4gICAgICBQT1NUR1JFU19EQjogJHtQT1NUR1JFU19EQn1cbiAgICAgIFBPU1RHUkVTX1BBU1NXT1JEOiAke1BPU1RHUkVTX1BBU1NXT1JEfVxuICAgICAgREFUQUJBU0VfVVJMOiBlY3RvOi8vc3VwYWJhc2VfYWRtaW46JHtQT1NUR1JFU19QQVNTV09SRH1AZGI6JHtQT1NUR1JFU19QT1JUfS9fc3VwYWJhc2VcbiAgICAgIENMVVNURVJfUE9TVEdSRVM6IHRydWVcbiAgICAgIFNFQ1JFVF9LRVlfQkFTRTogJHtTRUNSRVRfS0VZX0JBU0V9XG4gICAgICBWQVVMVF9FTkNfS0VZOiAke1ZBVUxUX0VOQ19LRVl9XG4gICAgICBBUElfSldUX1NFQ1JFVDogJHtKV1RfU0VDUkVUfVxuICAgICAgTUVUUklDU19KV1RfU0VDUkVUOiAke0pXVF9TRUNSRVR9XG4gICAgICBSRUdJT046IGxvY2FsXG4gICAgICBFUkxfQUZMQUdTOiAtcHJvdG9fZGlzdCBpbmV0X3RjcFxuICAgICAgUE9PTEVSX1RFTkFOVF9JRDogJHtQT09MRVJfVEVOQU5UX0lEfVxuICAgICAgUE9PTEVSX0RFRkFVTFRfUE9PTF9TSVpFOiAke1BPT0xFUl9ERUZBVUxUX1BPT0xfU0laRX1cbiAgICAgIFBPT0xFUl9NQVhfQ0xJRU5UX0NPTk46ICR7UE9PTEVSX01BWF9DTElFTlRfQ09OTn1cbiAgICAgIFBPT0xFUl9QT09MX01PREU6IHRyYW5zYWN0aW9uXG4gICAgY29tbWFuZDpcbiAgICAgIFtcbiAgICAgICAgXCIvYmluL3NoXCIsXG4gICAgICAgIFwiLWNcIixcbiAgICAgICAgXCIvYXBwL2Jpbi9taWdyYXRlICYmIC9hcHAvYmluL3N1cGF2aXNvciBldmFsIFxcXCIkJChjYXQgL2V0Yy9wb29sZXIvcG9vbGVyLmV4cylcXFwiICYmIC9hcHAvYmluL3NlcnZlclwiXG4gICAgICBdXG5cbnZvbHVtZXM6XG4gIGRiLWNvbmZpZzpcbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5wb3N0Z3Jlc19wYXNzd29yZCA9IFwiJHtwYXNzd29yZDozMn1cIlxuZGFzaGJvYXJkX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5sb2dmbGFyZV9hcGlfa2V5ID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5jb250YWluZXJfbmFtZV9wcmVmaXggPSBcInN1cGFiYXNlLSR7aGFzaDo0fVwiXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImtvbmdcIlxucG9ydCA9IDhfMDAwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltjb25maWddXG5lbnYgPSBbXG4nIyMjIyMjIyMjIyMjJyxcbicjIFRvIGdldCBhIHByb3BlciB3b3JraW5nIGNvbmZpZ3VyYXRpb24geW91IHNob3VsZCBhdCBsZWFzdCB0YWtlIGEgbG9vayBhdDonLFxuJyMgLSBTVVBBQkFTRV9QVUJMSUNfVVJMLCBBUElfRVhURVJOQUxfVVJMIHNob3VsZCBwb2ludCB0byB5b3VyIHN1cGFiYXNlIGRvbWFpbiB3aXRoIGNvcnJlY3QgaHR0cC9odHRwcyBzY2hlbWUnLFxuJyMgLSBTTVRQXyogYXJlIHJlcXVpcmVkIGZvciBhdXRoIG1haWwgc2VuZGluZycsXG4nIyAtIEFERElUSU9OQUxfUkVESVJFQ1RfVVJMUywgU0lURV9VUkwgc2hvdWxkIHBvaW50IHRvIGFwcGxpY2F0aW9uIHVzaW5nIHN1cGFiYXNlIGZvciBhdXRoZW50aWNhdGlvbicsXG4nIyAgIFRoZXkgYXJlIHVzZWQgZm9yIHJlZGlyZWN0aW5nIGFmdGVyIGxvZ2luL3NpZ251cCBhbmQgZ290cnVlIHdpbGwgY2hlY2sgdGhlbSBiZWZvcmUgc2VuZGluZyBlbWFpbHMnLFxuJyMgLSBQT1NUR1JFU19QT1JULCBQT09MRVJfUFJPWFlfUE9SVF9UUkFOU0FDVElPTiBzaG91bGQgYmUgY2hhbmdlZCBpZiB5b3UgYXJlIGFscmVhZHkgcnVubmluZyBvdGhlciBpbnN0YW5jZXMgb2Ygc3VwYWJhc2UnLFxuJyMgYW5kIENIQU5HRTogSldULVNFQ1JFVCwgQU5PTl9LRVksIFNFUlZJQ0VfUk9MRV9LRVksIFNFQ1JFVF9LRVlfQkFTRSwgVkFVTFRfRU5DX0tFWScsXG4nIycsXG4nIyBTdXBhYmFzZSB1c2VzIGNvbnRhaW5lciBuYW1lcyBpbiBwYXJ0IG9mIGl0cyBjb25maWd1cmF0aW9uIHNvIGl0IGlzIGltcG9ydGFudCB0byBrZWVwIHRoZW0nLFxuJyMgVGhpcyB0ZW1wbGF0ZSBnZW5lcmF0ZXMgYSByYW5kb20gcHJlZml4IGZvciB0aGUgY29udGFpbmVyIG5hbWVzIHRvIGF2b2lkIGNvbmZsaWN0cycsXG4nIyBJZiB5b3UgY2hhbmdlIGl0IHlvdSB3aWxsIG5lZWQgdG8gdXBkYXRlIHJvdXRlcyBpbiB0aGUgdmVjdG9yLnltbCBmaWxlIGluIGFkdmFuY2VkLT5tb3VudHMgc2VjdGlvbicsXG4nIyMjIyMjIyMjIyMjJyxcbidDT05UQUlORVJfUFJFRklYPSR7Y29udGFpbmVyX25hbWVfcHJlZml4fScsXG4nJyxcbicjIyMjIyMjIyMjIyMnLFxuJyMgU2VjcmV0cycsXG4nIyBZT1UgTVVTVCBDSEFOR0UgVEhFU0UgQkVGT1JFIEdPSU5HIElOVE8gUFJPRFVDVElPTicsXG4nIyBodHRwczovL3N1cGFiYXNlLmNvbS9kb2NzL2d1aWRlcy9zZWxmLWhvc3RpbmcvZG9ja2VyI3NlY3VyaW5nLXlvdXItc2VydmljZXMnLFxuJyMgVGhleSBhcmUgZGVmYXVsdCB2YWx1ZXMgZnJvbSBzdXBhYmFzZSBzbyByZWFsbHkgZG8gbm90IHVzZSB0aGVtIGluIGV4cG9zZWQgZW52aXJvbm1lbnRzJyxcbicjIEdvIHRvIGh0dHBzOi8vc3VwYWJhc2UuY29tL2RvY3MvZ3VpZGVzL3NlbGYtaG9zdGluZyBmb3IgbW9yZSBpbmZvcm1hdGlvbicsXG4nIyMjIyMjIyMjIyMjJyxcbicnLFxuJ1NVUEFCQVNFX0hPU1Q9JHttYWluX2RvbWFpbn0nLFxuJ1BPU1RHUkVTX1BBU1NXT1JEPSR7cG9zdGdyZXNfcGFzc3dvcmR9JyxcbidKV1RfU0VDUkVUPXlvdXItc3VwZXItc2VjcmV0LWp3dC10b2tlbi13aXRoLWF0LWxlYXN0LTMyLWNoYXJhY3RlcnMtbG9uZycsXG4nQU5PTl9LRVk9ZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5QWdDaUFnSUNBaWNtOXNaU0k2SUNKaGJtOXVJaXdLSUNBZ0lDSnBjM01pT2lBaWMzVndZV0poYzJVdFpHVnRieUlzQ2lBZ0lDQWlhV0YwSWpvZ01UWTBNVGMyT1RJd01Dd0tJQ0FnSUNKbGVIQWlPaUF4TnprNU5UTTFOakF3Q24wLmRjX1g1aVJfVlBfcVQwenNpeWpfSV9PWjJUOUZ0UlUyQkJOV044QnU0R0UnLFxuJ1NFUlZJQ0VfUk9MRV9LRVk9ZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5QWdDaUFnSUNBaWNtOXNaU0k2SUNKelpYSjJhV05sWDNKdmJHVWlMQW9nSUNBZ0ltbHpjeUk2SUNKemRYQmhZbUZ6WlMxa1pXMXZJaXdLSUNBZ0lDSnBZWFFpT2lBeE5qUXhOelk1TWpBd0xBb2dJQ0FnSW1WNGNDSTZJREUzT1RrMU16VTJNREFLZlEuRGFZbE5Fb1VyckVuMklnN3RxaWJTLVBISzV2Z3VzYmNibzdYMzZYVnQ0UScsXG4nREFTSEJPQVJEX1VTRVJOQU1FPXN1cGFiYXNlJyxcbidEQVNIQk9BUkRfUEFTU1dPUkQ9JHtkYXNoYm9hcmRfcGFzc3dvcmR9JyxcbidTRUNSRVRfS0VZX0JBU0U9VXBOVm50bjNjRHhISnBxOTlZTWMxVDFBUWdRcGM4a2ZZVHVSZ0JpWWExNUJMcng4ZXRRb1h6M2dadjEvdTJvcScsXG4nVkFVTFRfRU5DX0tFWT15b3VyLWVuY3J5cHRpb24ta2V5LTMyLWNoYXJzLW1pbicsXG4nJyxcbicnLFxuJyMjIyMjIyMjIyMjIycsXG4nIyBEYXRhYmFzZSAtIFlvdSBjYW4gY2hhbmdlIHRoZXNlIHRvIGFueSBQb3N0Z3JlU1FMIGRhdGFiYXNlIHRoYXQgaGFzIGxvZ2ljYWwgcmVwbGljYXRpb24gZW5hYmxlZC4nLFxuJyMjIyMjIyMjIyMjIycsXG4nJyxcbidQT1NUR1JFU19IT1NUPWRiJyxcbidQT1NUR1JFU19EQj1wb3N0Z3JlcycsXG4nUE9TVEdSRVNfUE9SVD01NDMyJyxcbicjIGRlZmF1bHQgdXNlciBpcyBwb3N0Z3JlcycsXG4nJyxcbicnLFxuJyMjIyMjIyMjIyMjIycsXG4nIyBTdXBhdmlzb3IgLS0gRGF0YWJhc2UgcG9vbGVyJyxcbicjIyMjIyMjIyMjIyMnLFxuJ1BPT0xFUl9QUk9YWV9QT1JUX1RSQU5TQUNUSU9OPTY1NDMnLFxuJ1BPT0xFUl9ERUZBVUxUX1BPT0xfU0laRT0yMCcsXG4nUE9PTEVSX01BWF9DTElFTlRfQ09OTj0xMDAnLFxuJ1BPT0xFUl9URU5BTlRfSUQ9eW91ci10ZW5hbnQtaWQnLFxuJycsXG4nJyxcbicjIyMjIyMjIyMjIyMnLFxuJyMgQVBJIFByb3h5IC0gQ29uZmlndXJhdGlvbiBmb3IgdGhlIEtvbmcgUmV2ZXJzZSBwcm94eS4nLFxuJyMgRm9sbG93aW5nIHBvcnRzIHNob3VsZCBub3QgYmUgY2hhbmdlZCBmb3IgYSBkb2twbG95IGNvbmZpZyB1bmxlc3MgeW91IGtub3cgd2hhdCB5b3UgYXJlIGRvaW5nLicsXG4nIyMjIyMjIyMjIyMjJyxcbicnLFxuJ0tPTkdfSFRUUF9QT1JUPTgwMDAnLFxuJ0tPTkdfSFRUUFNfUE9SVD04NDQzJyxcbicnLFxuJycsXG4nIyMjIyMjIyMjIyMjJyxcbicjIEFQSSAtIENvbmZpZ3VyYXRpb24gZm9yIFBvc3RnUkVTVC4nLFxuJyMjIyMjIyMjIyMjIycsXG4nJyxcbidQR1JTVF9EQl9TQ0hFTUFTPXB1YmxpYyxzdG9yYWdlLGdyYXBocWxfcHVibGljJyxcbicnLFxuJycsXG4nIyMjIyMjIyMjIyMjJyxcbicjIEF1dGggLSBDb25maWd1cmF0aW9uIGZvciB0aGUgR29UcnVlIGF1dGhlbnRpY2F0aW9uIHNlcnZlci4nLFxuJyMjIyMjIyMjIyMjIycsXG4nJyxcbicjIyBHZW5lcmFsJyxcbidTSVRFX1VSTD1odHRwOi8vbG9jYWxob3N0OjMwMDAnLFxuJ0FERElUSU9OQUxfUkVESVJFQ1RfVVJMUz1odHRwOi8vJHttYWluX2RvbWFpbn0vKixodHRwOi8vbG9jYWxob3N0OjMwMDAvKicsXG4nSldUX0VYUElSWT0zNjAwJyxcbidESVNBQkxFX1NJR05VUD1mYWxzZScsXG4nQVBJX0VYVEVSTkFMX1VSTD1odHRwOi8vJHttYWluX2RvbWFpbn0nLFxuJycsXG4nIyMgTWFpbGVyIENvbmZpZycsXG4nTUFJTEVSX1VSTFBBVEhTX0NPTkZJUk1BVElPTj1cIi9hdXRoL3YxL3ZlcmlmeVwiJyxcbidNQUlMRVJfVVJMUEFUSFNfSU5WSVRFPVwiL2F1dGgvdjEvdmVyaWZ5XCInLFxuJ01BSUxFUl9VUkxQQVRIU19SRUNPVkVSWT1cIi9hdXRoL3YxL3ZlcmlmeVwiJyxcbidNQUlMRVJfVVJMUEFUSFNfRU1BSUxfQ0hBTkdFPVwiL2F1dGgvdjEvdmVyaWZ5XCInLFxuJycsXG4nIyMgRW1haWwgYXV0aCcsXG4nRU5BQkxFX0VNQUlMX1NJR05VUD10cnVlJyxcbidFTkFCTEVfRU1BSUxfQVVUT0NPTkZJUk09ZmFsc2UnLFxuJ1NNVFBfQURNSU5fRU1BSUw9YWRtaW5AZXhhbXBsZS5jb20nLFxuJ1NNVFBfSE9TVD1zdXBhYmFzZS1tYWlsJyxcbidTTVRQX1BPUlQ9MjUwMCcsXG4nU01UUF9VU0VSPWZha2VfbWFpbF91c2VyJyxcbidTTVRQX1BBU1M9ZmFrZV9tYWlsX3Bhc3N3b3JkJyxcbidTTVRQX1NFTkRFUl9OQU1FPWZha2Vfc2VuZGVyJyxcbidFTkFCTEVfQU5PTllNT1VTX1VTRVJTPWZhbHNlJyxcbicnLFxuJyMjIFBob25lIGF1dGgnLFxuJ0VOQUJMRV9QSE9ORV9TSUdOVVA9dHJ1ZScsXG4nRU5BQkxFX1BIT05FX0FVVE9DT05GSVJNPXRydWUnLFxuJycsXG4nJyxcbicjIyMjIyMjIyMjIyMnLFxuJyMgU3R1ZGlvIC0gQ29uZmlndXJhdGlvbiBmb3IgdGhlIERhc2hib2FyZCcsXG4nIyMjIyMjIyMjIyMjJyxcbicnLFxuJ1NUVURJT19ERUZBVUxUX09SR0FOSVpBVElPTj1EZWZhdWx0IE9yZ2FuaXphdGlvbicsXG4nU1RVRElPX0RFRkFVTFRfUFJPSkVDVD1EZWZhdWx0IFByb2plY3QnLFxuJycsXG4nU1RVRElPX1BPUlQ9MzAwMCcsXG4nIyByZXBsYWNlIGlmIHlvdSBpbnRlbmQgdG8gdXNlIFN0dWRpbyBvdXRzaWRlIG9mIGxvY2FsaG9zdCcsXG4nU1VQQUJBU0VfUFVCTElDX1VSTD1odHRwOi8vJHttYWluX2RvbWFpbn0nLFxuJycsXG4nIyBFbmFibGUgd2VicCBzdXBwb3J0JyxcbidJTUdQUk9YWV9FTkFCTEVfV0VCUF9ERVRFQ1RJT049dHJ1ZScsXG4nJyxcbicjIEFkZCB5b3VyIE9wZW5BSSBBUEkga2V5IHRvIGVuYWJsZSBTUUwgRWRpdG9yIEFzc2lzdGFudCcsXG4nT1BFTkFJX0FQSV9LRVk9JyxcbicnLFxuJycsXG4nIyMjIyMjIyMjIyMjJyxcbicjIEZ1bmN0aW9ucyAtIENvbmZpZ3VyYXRpb24gZm9yIEZ1bmN0aW9ucycsXG4nIyMjIyMjIyMjIyMjJyxcbicjIE5PVEU6IFZFUklGWV9KV1QgYXBwbGllcyB0byBhbGwgZnVuY3Rpb25zLiBQZXItZnVuY3Rpb24gVkVSSUZZX0pXVCBpcyBub3Qgc3VwcG9ydGVkIHlldC4nLFxuJ0ZVTkNUSU9OU19WRVJJRllfSldUPWZhbHNlJyxcbicnLFxuJycsXG4nIyMjIyMjIyMjIyMjJyxcbicjIExvZ3MgLSBDb25maWd1cmF0aW9uIGZvciBMb2dmbGFyZScsXG4nIyBQbGVhc2UgcmVmZXIgdG8gaHR0cHM6Ly9zdXBhYmFzZS5jb20vZG9jcy9yZWZlcmVuY2Uvc2VsZi1ob3N0aW5nLWFuYWx5dGljcy9pbnRyb2R1Y3Rpb24nLFxuJyMjIyMjIyMjIyMjIycsXG4nJyxcbidMT0dGTEFSRV9MT0dHRVJfQkFDS0VORF9BUElfS0VZPXlvdXItc3VwZXItc2VjcmV0LWFuZC1sb25nLWxvZ2ZsYXJlLWtleScsXG4nJyxcbicjIENoYW5nZSB2ZWN0b3IudG9tbCBzaW5rcyB0byByZWZsZWN0IHRoaXMgY2hhbmdlJyxcbidMT0dGTEFSRV9BUElfS0VZPSR7bG9nZmxhcmVfYXBpX2tleX0nLFxuJycsXG4nIyBEb2NrZXIgc29ja2V0IGxvY2F0aW9uIC0gdGhpcyB2YWx1ZSB3aWxsIGRpZmZlciBkZXBlbmRpbmcgb24geW91ciBPUycsXG4nRE9DS0VSX1NPQ0tFVF9MT0NBVElPTj0vdmFyL3J1bi9kb2NrZXIuc29jaycsXG4nJyxcbicjIEdvb2dsZSBDbG91ZCBQcm9qZWN0IGRldGFpbHMnLFxuJ0dPT0dMRV9QUk9KRUNUX0lEPUdPT0dMRV9QUk9KRUNUX0lEJyxcbidHT09HTEVfUFJPSkVDVF9OVU1CRVI9R09PR0xFX1BST0pFQ1RfTlVNQkVSJ11cblxuW1tjb25maWcubW91bnRzXV1cbmZpbGVQYXRoID0gXCIvdm9sdW1lcy9hcGkva29uZy55bWxcIlxuY29udGVudCA9IFwiXCJcIl9mb3JtYXRfdmVyc2lvbjogJzIuMSdcbl90cmFuc2Zvcm06IHRydWVcblxuIyMjXG4jIyMgQ29uc3VtZXJzIC8gVXNlcnNcbiMjI1xuY29uc3VtZXJzOlxuICAtIHVzZXJuYW1lOiBEQVNIQk9BUkRcbiAgLSB1c2VybmFtZTogYW5vblxuICAgIGtleWF1dGhfY3JlZGVudGlhbHM6XG4gICAgICAtIGtleTogJFNVUEFCQVNFX0FOT05fS0VZXG4gIC0gdXNlcm5hbWU6IHNlcnZpY2Vfcm9sZVxuICAgIGtleWF1dGhfY3JlZGVudGlhbHM6XG4gICAgICAtIGtleTogJFNVUEFCQVNFX1NFUlZJQ0VfS0VZXG5cbiMjI1xuIyMjIEFjY2VzcyBDb250cm9sIExpc3RcbiMjI1xuYWNsczpcbiAgLSBjb25zdW1lcjogYW5vblxuICAgIGdyb3VwOiBhbm9uXG4gIC0gY29uc3VtZXI6IHNlcnZpY2Vfcm9sZVxuICAgIGdyb3VwOiBhZG1pblxuXG4jIyNcbiMjIyBEYXNoYm9hcmQgY3JlZGVudGlhbHNcbiMjI1xuYmFzaWNhdXRoX2NyZWRlbnRpYWxzOlxuICAtIGNvbnN1bWVyOiBEQVNIQk9BUkRcbiAgICB1c2VybmFtZTogJERBU0hCT0FSRF9VU0VSTkFNRVxuICAgIHBhc3N3b3JkOiAkREFTSEJPQVJEX1BBU1NXT1JEXG5cbiMjI1xuIyMjIEFQSSBSb3V0ZXNcbiMjI1xuc2VydmljZXM6XG4gICMjIE9wZW4gQXV0aCByb3V0ZXNcbiAgLSBuYW1lOiBhdXRoLXYxLW9wZW5cbiAgICB1cmw6IGh0dHA6Ly9hdXRoOjk5OTkvdmVyaWZ5XG4gICAgcm91dGVzOlxuICAgICAgLSBuYW1lOiBhdXRoLXYxLW9wZW5cbiAgICAgICAgc3RyaXBfcGF0aDogdHJ1ZVxuICAgICAgICBwYXRoczpcbiAgICAgICAgICAtIC9hdXRoL3YxL3ZlcmlmeVxuICAgIHBsdWdpbnM6XG4gICAgICAtIG5hbWU6IGNvcnNcbiAgLSBuYW1lOiBhdXRoLXYxLW9wZW4tY2FsbGJhY2tcbiAgICB1cmw6IGh0dHA6Ly9hdXRoOjk5OTkvY2FsbGJhY2tcbiAgICByb3V0ZXM6XG4gICAgICAtIG5hbWU6IGF1dGgtdjEtb3Blbi1jYWxsYmFja1xuICAgICAgICBzdHJpcF9wYXRoOiB0cnVlXG4gICAgICAgIHBhdGhzOlxuICAgICAgICAgIC0gL2F1dGgvdjEvY2FsbGJhY2tcbiAgICBwbHVnaW5zOlxuICAgICAgLSBuYW1lOiBjb3JzXG4gIC0gbmFtZTogYXV0aC12MS1vcGVuLWF1dGhvcml6ZVxuICAgIHVybDogaHR0cDovL2F1dGg6OTk5OS9hdXRob3JpemVcbiAgICByb3V0ZXM6XG4gICAgICAtIG5hbWU6IGF1dGgtdjEtb3Blbi1hdXRob3JpemVcbiAgICAgICAgc3RyaXBfcGF0aDogdHJ1ZVxuICAgICAgICBwYXRoczpcbiAgICAgICAgICAtIC9hdXRoL3YxL2F1dGhvcml6ZVxuICAgIHBsdWdpbnM6XG4gICAgICAtIG5hbWU6IGNvcnNcblxuICAjIyBTZWN1cmUgQXV0aCByb3V0ZXNcbiAgLSBuYW1lOiBhdXRoLXYxXG4gICAgX2NvbW1lbnQ6ICdHb1RydWU6IC9hdXRoL3YxLyogLT4gaHR0cDovL2F1dGg6OTk5OS8qJ1xuICAgIHVybDogaHR0cDovL2F1dGg6OTk5OS9cbiAgICByb3V0ZXM6XG4gICAgICAtIG5hbWU6IGF1dGgtdjEtYWxsXG4gICAgICAgIHN0cmlwX3BhdGg6IHRydWVcbiAgICAgICAgcGF0aHM6XG4gICAgICAgICAgLSAvYXV0aC92MS9cbiAgICBwbHVnaW5zOlxuICAgICAgLSBuYW1lOiBjb3JzXG4gICAgICAtIG5hbWU6IGtleS1hdXRoXG4gICAgICAgIGNvbmZpZzpcbiAgICAgICAgICBoaWRlX2NyZWRlbnRpYWxzOiBmYWxzZVxuICAgICAgLSBuYW1lOiBhY2xcbiAgICAgICAgY29uZmlnOlxuICAgICAgICAgIGhpZGVfZ3JvdXBzX2hlYWRlcjogdHJ1ZVxuICAgICAgICAgIGFsbG93OlxuICAgICAgICAgICAgLSBhZG1pblxuICAgICAgICAgICAgLSBhbm9uXG5cbiAgIyMgU2VjdXJlIFJFU1Qgcm91dGVzXG4gIC0gbmFtZTogcmVzdC12MVxuICAgIF9jb21tZW50OiAnUG9zdGdSRVNUOiAvcmVzdC92MS8qIC0+IGh0dHA6Ly9yZXN0OjMwMDAvKidcbiAgICB1cmw6IGh0dHA6Ly9yZXN0OjMwMDAvXG4gICAgcm91dGVzOlxuICAgICAgLSBuYW1lOiByZXN0LXYxLWFsbFxuICAgICAgICBzdHJpcF9wYXRoOiB0cnVlXG4gICAgICAgIHBhdGhzOlxuICAgICAgICAgIC0gL3Jlc3QvdjEvXG4gICAgcGx1Z2luczpcbiAgICAgIC0gbmFtZTogY29yc1xuICAgICAgLSBuYW1lOiBrZXktYXV0aFxuICAgICAgICBjb25maWc6XG4gICAgICAgICAgaGlkZV9jcmVkZW50aWFsczogdHJ1ZVxuICAgICAgLSBuYW1lOiBhY2xcbiAgICAgICAgY29uZmlnOlxuICAgICAgICAgIGhpZGVfZ3JvdXBzX2hlYWRlcjogdHJ1ZVxuICAgICAgICAgIGFsbG93OlxuICAgICAgICAgICAgLSBhZG1pblxuICAgICAgICAgICAgLSBhbm9uXG5cbiAgIyMgU2VjdXJlIEdyYXBoUUwgcm91dGVzXG4gIC0gbmFtZTogZ3JhcGhxbC12MVxuICAgIF9jb21tZW50OiAnUG9zdGdSRVNUOiAvZ3JhcGhxbC92MS8qIC0+IGh0dHA6Ly9yZXN0OjMwMDAvcnBjL2dyYXBocWwnXG4gICAgdXJsOiBodHRwOi8vcmVzdDozMDAwL3JwYy9ncmFwaHFsXG4gICAgcm91dGVzOlxuICAgICAgLSBuYW1lOiBncmFwaHFsLXYxLWFsbFxuICAgICAgICBzdHJpcF9wYXRoOiB0cnVlXG4gICAgICAgIHBhdGhzOlxuICAgICAgICAgIC0gL2dyYXBocWwvdjFcbiAgICBwbHVnaW5zOlxuICAgICAgLSBuYW1lOiBjb3JzXG4gICAgICAtIG5hbWU6IGtleS1hdXRoXG4gICAgICAgIGNvbmZpZzpcbiAgICAgICAgICBoaWRlX2NyZWRlbnRpYWxzOiB0cnVlXG4gICAgICAtIG5hbWU6IHJlcXVlc3QtdHJhbnNmb3JtZXJcbiAgICAgICAgY29uZmlnOlxuICAgICAgICAgIGFkZDpcbiAgICAgICAgICAgIGhlYWRlcnM6XG4gICAgICAgICAgICAgIC0gQ29udGVudC1Qcm9maWxlOmdyYXBocWxfcHVibGljXG4gICAgICAtIG5hbWU6IGFjbFxuICAgICAgICBjb25maWc6XG4gICAgICAgICAgaGlkZV9ncm91cHNfaGVhZGVyOiB0cnVlXG4gICAgICAgICAgYWxsb3c6XG4gICAgICAgICAgICAtIGFkbWluXG4gICAgICAgICAgICAtIGFub25cblxuICAjIyBTZWN1cmUgUmVhbHRpbWUgcm91dGVzXG4gIC0gbmFtZTogcmVhbHRpbWUtdjEtd3NcbiAgICBfY29tbWVudDogJ1JlYWx0aW1lOiAvcmVhbHRpbWUvdjEvKiAtPiB3czovL3JlYWx0aW1lOjQwMDAvc29ja2V0LyonXG4gICAgdXJsOiBodHRwOi8vcmVhbHRpbWUtZGV2LnN1cGFiYXNlLXJlYWx0aW1lOjQwMDAvc29ja2V0XG4gICAgcHJvdG9jb2w6IHdzXG4gICAgcm91dGVzOlxuICAgICAgLSBuYW1lOiByZWFsdGltZS12MS13c1xuICAgICAgICBzdHJpcF9wYXRoOiB0cnVlXG4gICAgICAgIHBhdGhzOlxuICAgICAgICAgIC0gL3JlYWx0aW1lL3YxL1xuICAgIHBsdWdpbnM6XG4gICAgICAtIG5hbWU6IGNvcnNcbiAgICAgIC0gbmFtZToga2V5LWF1dGhcbiAgICAgICAgY29uZmlnOlxuICAgICAgICAgIGhpZGVfY3JlZGVudGlhbHM6IGZhbHNlXG4gICAgICAtIG5hbWU6IGFjbFxuICAgICAgICBjb25maWc6XG4gICAgICAgICAgaGlkZV9ncm91cHNfaGVhZGVyOiB0cnVlXG4gICAgICAgICAgYWxsb3c6XG4gICAgICAgICAgICAtIGFkbWluXG4gICAgICAgICAgICAtIGFub25cbiAgLSBuYW1lOiByZWFsdGltZS12MS1yZXN0XG4gICAgX2NvbW1lbnQ6ICdSZWFsdGltZTogL3JlYWx0aW1lL3YxLyogLT4gd3M6Ly9yZWFsdGltZTo0MDAwL3NvY2tldC8qJ1xuICAgIHVybDogaHR0cDovL3JlYWx0aW1lLWRldi5zdXBhYmFzZS1yZWFsdGltZTo0MDAwL2FwaVxuICAgIHByb3RvY29sOiBodHRwXG4gICAgcm91dGVzOlxuICAgICAgLSBuYW1lOiByZWFsdGltZS12MS1yZXN0XG4gICAgICAgIHN0cmlwX3BhdGg6IHRydWVcbiAgICAgICAgcGF0aHM6XG4gICAgICAgICAgLSAvcmVhbHRpbWUvdjEvYXBpXG4gICAgcGx1Z2luczpcbiAgICAgIC0gbmFtZTogY29yc1xuICAgICAgLSBuYW1lOiBrZXktYXV0aFxuICAgICAgICBjb25maWc6XG4gICAgICAgICAgaGlkZV9jcmVkZW50aWFsczogZmFsc2VcbiAgICAgIC0gbmFtZTogYWNsXG4gICAgICAgIGNvbmZpZzpcbiAgICAgICAgICBoaWRlX2dyb3Vwc19oZWFkZXI6IHRydWVcbiAgICAgICAgICBhbGxvdzpcbiAgICAgICAgICAgIC0gYWRtaW5cbiAgICAgICAgICAgIC0gYW5vblxuICAjIyBTdG9yYWdlIHJvdXRlczogdGhlIHN0b3JhZ2Ugc2VydmVyIG1hbmFnZXMgaXRzIG93biBhdXRoXG4gIC0gbmFtZTogc3RvcmFnZS12MVxuICAgIF9jb21tZW50OiAnU3RvcmFnZTogL3N0b3JhZ2UvdjEvKiAtPiBodHRwOi8vc3RvcmFnZTo1MDAwLyonXG4gICAgdXJsOiBodHRwOi8vc3RvcmFnZTo1MDAwL1xuICAgIHJvdXRlczpcbiAgICAgIC0gbmFtZTogc3RvcmFnZS12MS1hbGxcbiAgICAgICAgc3RyaXBfcGF0aDogdHJ1ZVxuICAgICAgICBwYXRoczpcbiAgICAgICAgICAtIC9zdG9yYWdlL3YxL1xuICAgIHBsdWdpbnM6XG4gICAgICAtIG5hbWU6IGNvcnNcblxuICAjIyBFZGdlIEZ1bmN0aW9ucyByb3V0ZXNcbiAgLSBuYW1lOiBmdW5jdGlvbnMtdjFcbiAgICBfY29tbWVudDogJ0VkZ2UgRnVuY3Rpb25zOiAvZnVuY3Rpb25zL3YxLyogLT4gaHR0cDovL2Z1bmN0aW9uczo5MDAwLyonXG4gICAgdXJsOiBodHRwOi8vZnVuY3Rpb25zOjkwMDAvXG4gICAgcm91dGVzOlxuICAgICAgLSBuYW1lOiBmdW5jdGlvbnMtdjEtYWxsXG4gICAgICAgIHN0cmlwX3BhdGg6IHRydWVcbiAgICAgICAgcGF0aHM6XG4gICAgICAgICAgLSAvZnVuY3Rpb25zL3YxL1xuICAgIHBsdWdpbnM6XG4gICAgICAtIG5hbWU6IGNvcnNcblxuICAjIyBBbmFseXRpY3Mgcm91dGVzXG4gIC0gbmFtZTogYW5hbHl0aWNzLXYxXG4gICAgX2NvbW1lbnQ6ICdBbmFseXRpY3M6IC9hbmFseXRpY3MvdjEvKiAtPiBodHRwOi8vbG9nZmxhcmU6NDAwMC8qJ1xuICAgIHVybDogaHR0cDovL2FuYWx5dGljczo0MDAwL1xuICAgIHJvdXRlczpcbiAgICAgIC0gbmFtZTogYW5hbHl0aWNzLXYxLWFsbFxuICAgICAgICBzdHJpcF9wYXRoOiB0cnVlXG4gICAgICAgIHBhdGhzOlxuICAgICAgICAgIC0gL2FuYWx5dGljcy92MS9cblxuICAjIyBTZWN1cmUgRGF0YWJhc2Ugcm91dGVzXG4gIC0gbmFtZTogbWV0YVxuICAgIF9jb21tZW50OiAncGctbWV0YTogL3BnLyogLT4gaHR0cDovL3BnLW1ldGE6ODA4MC8qJ1xuICAgIHVybDogaHR0cDovL21ldGE6ODA4MC9cbiAgICByb3V0ZXM6XG4gICAgICAtIG5hbWU6IG1ldGEtYWxsXG4gICAgICAgIHN0cmlwX3BhdGg6IHRydWVcbiAgICAgICAgcGF0aHM6XG4gICAgICAgICAgLSAvcGcvXG4gICAgcGx1Z2luczpcbiAgICAgIC0gbmFtZToga2V5LWF1dGhcbiAgICAgICAgY29uZmlnOlxuICAgICAgICAgIGhpZGVfY3JlZGVudGlhbHM6IGZhbHNlXG4gICAgICAtIG5hbWU6IGFjbFxuICAgICAgICBjb25maWc6XG4gICAgICAgICAgaGlkZV9ncm91cHNfaGVhZGVyOiB0cnVlXG4gICAgICAgICAgYWxsb3c6XG4gICAgICAgICAgICAtIGFkbWluXG5cbiAgIyMgUHJvdGVjdGVkIERhc2hib2FyZCAtIGNhdGNoIGFsbCByZW1haW5pbmcgcm91dGVzXG4gIC0gbmFtZTogZGFzaGJvYXJkXG4gICAgX2NvbW1lbnQ6ICdTdHVkaW86IC8qIC0+IGh0dHA6Ly9zdHVkaW86MzAwMC8qJ1xuICAgIHVybDogaHR0cDovL3N0dWRpbzozMDAwL1xuICAgIHJvdXRlczpcbiAgICAgIC0gbmFtZTogZGFzaGJvYXJkLWFsbFxuICAgICAgICBzdHJpcF9wYXRoOiB0cnVlXG4gICAgICAgIHBhdGhzOlxuICAgICAgICAgIC0gL1xuICAgIHBsdWdpbnM6XG4gICAgICAtIG5hbWU6IGNvcnNcbiAgICAgIC0gbmFtZTogYmFzaWMtYXV0aFxuICAgICAgICBjb25maWc6XG4gICAgICAgICAgaGlkZV9jcmVkZW50aWFsczogdHJ1ZVxuXCJcIlwiXG5cbltbY29uZmlnLm1vdW50c11dXG5maWxlUGF0aCA9IFwiL3ZvbHVtZXMvZGIvaW5pdC9kYXRhLnNxbFwiXG5jb250ZW50ID0gXCJcIlxuXG5bW2NvbmZpZy5tb3VudHNdXVxuZmlsZVBhdGggPSBcIi92b2x1bWVzL2RiL19zdXBhYmFzZS5zcWxcIlxuY29udGVudCA9IFwiXCJcIlxcXFxzZXQgcGd1c2VyIGBlY2hvIFwiJFBPU1RHUkVTX1VTRVJcImBcblxuQ1JFQVRFIERBVEFCQVNFIF9zdXBhYmFzZSBXSVRIIE9XTkVSIDpwZ3VzZXI7XG5cIlwiXCJcblxuW1tjb25maWcubW91bnRzXV1cbmZpbGVQYXRoID0gXCIvdm9sdW1lcy9kYi9qd3Quc3FsXCJcbmNvbnRlbnQgPSBcIlwiXCJcblxcXFxzZXQgand0X3NlY3JldCBgZWNobyBcIiRKV1RfU0VDUkVUXCJgXG5cXFxcc2V0IGp3dF9leHAgYGVjaG8gXCIkSldUX0VYUFwiYFxuXG5BTFRFUiBEQVRBQkFTRSBwb3N0Z3JlcyBTRVQgXCJhcHAuc2V0dGluZ3Muand0X3NlY3JldFwiIFRPIDonand0X3NlY3JldCc7XG5BTFRFUiBEQVRBQkFTRSBwb3N0Z3JlcyBTRVQgXCJhcHAuc2V0dGluZ3Muand0X2V4cFwiIFRPIDonand0X2V4cCc7XG5cIlwiXCJcblxuW1tjb25maWcubW91bnRzXV1cbmZpbGVQYXRoID0gXCIvdm9sdW1lcy9kYi9sb2dzLnNxbFwiXG5jb250ZW50ID0gXCJcIlwiXG5cXFxcc2V0IHBndXNlciBgZWNobyBcIiRQT1NUR1JFU19VU0VSXCJgXG5cblxcXFxjIF9zdXBhYmFzZVxuY3JlYXRlIHNjaGVtYSBpZiBub3QgZXhpc3RzIF9hbmFseXRpY3M7XG5hbHRlciBzY2hlbWEgX2FuYWx5dGljcyBvd25lciB0byA6cGd1c2VyO1xuXFxcXGMgcG9zdGdyZXNcblwiXCJcIlxuXG5bW2NvbmZpZy5tb3VudHNdXVxuZmlsZVBhdGggPSBcIi92b2x1bWVzL2RiL3Bvb2xlci5zcWxcIlxuY29udGVudCA9IFwiXCJcIlxuXFxcXHNldCBwZ3VzZXIgYGVjaG8gXCIkUE9TVEdSRVNfVVNFUlwiYFxuXG5cXFxcYyBfc3VwYWJhc2VcbmNyZWF0ZSBzY2hlbWEgaWYgbm90IGV4aXN0cyBfc3VwYXZpc29yO1xuYWx0ZXIgc2NoZW1hIF9zdXBhdmlzb3Igb3duZXIgdG8gOnBndXNlcjtcblxcXFxjIHBvc3RncmVzXG5cIlwiXCJcblxuW1tjb25maWcubW91bnRzXV1cbmZpbGVQYXRoID0gXCIvdm9sdW1lcy9kYi9yZWFsdGltZS5zcWxcIlxuY29udGVudCA9IFwiXCJcIlxuXFxcXHNldCBwZ3VzZXIgYGVjaG8gXCIkUE9TVEdSRVNfVVNFUlwiYFxuXG5jcmVhdGUgc2NoZW1hIGlmIG5vdCBleGlzdHMgX3JlYWx0aW1lO1xuYWx0ZXIgc2NoZW1hIF9yZWFsdGltZSBvd25lciB0byA6cGd1c2VyO1xuXCJcIlwiXG5cbltbY29uZmlnLm1vdW50c11dXG5maWxlUGF0aCA9IFwiL3ZvbHVtZXMvZGIvcm9sZXMuc3FsXCJcbmNvbnRlbnQgPSBcIlwiXCJcbi0tIE5PVEU6IGNoYW5nZSB0byB5b3VyIG93biBwYXNzd29yZHMgZm9yIHByb2R1Y3Rpb24gZW52aXJvbm1lbnRzXG5cXFxcc2V0IHBncGFzcyBgZWNobyBcIiRQT1NUR1JFU19QQVNTV09SRFwiYFxuXG5BTFRFUiBVU0VSIGF1dGhlbnRpY2F0b3IgV0lUSCBQQVNTV09SRCA6J3BncGFzcyc7XG5BTFRFUiBVU0VSIHBnYm91bmNlciBXSVRIIFBBU1NXT1JEIDoncGdwYXNzJztcbkFMVEVSIFVTRVIgc3VwYWJhc2VfYXV0aF9hZG1pbiBXSVRIIFBBU1NXT1JEIDoncGdwYXNzJztcbkFMVEVSIFVTRVIgc3VwYWJhc2VfZnVuY3Rpb25zX2FkbWluIFdJVEggUEFTU1dPUkQgOidwZ3Bhc3MnO1xuQUxURVIgVVNFUiBzdXBhYmFzZV9zdG9yYWdlX2FkbWluIFdJVEggUEFTU1dPUkQgOidwZ3Bhc3MnO1xuXCJcIlwiXG5cbltbY29uZmlnLm1vdW50c11dXG5maWxlUGF0aCA9IFwiL3ZvbHVtZXMvZGIvd2ViaG9va3Muc3FsXCJcbmNvbnRlbnQgPSBcIlwiXCJcbkJFR0lOO1xuICAtLSBDcmVhdGUgcGdfbmV0IGV4dGVuc2lvblxuICBDUkVBVEUgRVhURU5TSU9OIElGIE5PVCBFWElTVFMgcGdfbmV0IFNDSEVNQSBleHRlbnNpb25zO1xuICAtLSBDcmVhdGUgc3VwYWJhc2VfZnVuY3Rpb25zIHNjaGVtYVxuICBDUkVBVEUgU0NIRU1BIHN1cGFiYXNlX2Z1bmN0aW9ucyBBVVRIT1JJWkFUSU9OIHN1cGFiYXNlX2FkbWluO1xuICBHUkFOVCBVU0FHRSBPTiBTQ0hFTUEgc3VwYWJhc2VfZnVuY3Rpb25zIFRPIHBvc3RncmVzLCBhbm9uLCBhdXRoZW50aWNhdGVkLCBzZXJ2aWNlX3JvbGU7XG4gIEFMVEVSIERFRkFVTFQgUFJJVklMRUdFUyBJTiBTQ0hFTUEgc3VwYWJhc2VfZnVuY3Rpb25zIEdSQU5UIEFMTCBPTiBUQUJMRVMgVE8gcG9zdGdyZXMsIGFub24sIGF1dGhlbnRpY2F0ZWQsIHNlcnZpY2Vfcm9sZTtcbiAgQUxURVIgREVGQVVMVCBQUklWSUxFR0VTIElOIFNDSEVNQSBzdXBhYmFzZV9mdW5jdGlvbnMgR1JBTlQgQUxMIE9OIEZVTkNUSU9OUyBUTyBwb3N0Z3JlcywgYW5vbiwgYXV0aGVudGljYXRlZCwgc2VydmljZV9yb2xlO1xuICBBTFRFUiBERUZBVUxUIFBSSVZJTEVHRVMgSU4gU0NIRU1BIHN1cGFiYXNlX2Z1bmN0aW9ucyBHUkFOVCBBTEwgT04gU0VRVUVOQ0VTIFRPIHBvc3RncmVzLCBhbm9uLCBhdXRoZW50aWNhdGVkLCBzZXJ2aWNlX3JvbGU7XG4gIC0tIHN1cGFiYXNlX2Z1bmN0aW9ucy5taWdyYXRpb25zIGRlZmluaXRpb25cbiAgQ1JFQVRFIFRBQkxFIHN1cGFiYXNlX2Z1bmN0aW9ucy5taWdyYXRpb25zIChcbiAgICB2ZXJzaW9uIHRleHQgUFJJTUFSWSBLRVksXG4gICAgaW5zZXJ0ZWRfYXQgdGltZXN0YW1wdHogTk9UIE5VTEwgREVGQVVMVCBOT1coKVxuICApO1xuICAtLSBJbml0aWFsIHN1cGFiYXNlX2Z1bmN0aW9ucyBtaWdyYXRpb25cbiAgSU5TRVJUIElOVE8gc3VwYWJhc2VfZnVuY3Rpb25zLm1pZ3JhdGlvbnMgKHZlcnNpb24pIFZBTFVFUyAoJ2luaXRpYWwnKTtcbiAgLS0gc3VwYWJhc2VfZnVuY3Rpb25zLmhvb2tzIGRlZmluaXRpb25cbiAgQ1JFQVRFIFRBQkxFIHN1cGFiYXNlX2Z1bmN0aW9ucy5ob29rcyAoXG4gICAgaWQgYmlnc2VyaWFsIFBSSU1BUlkgS0VZLFxuICAgIGhvb2tfdGFibGVfaWQgaW50ZWdlciBOT1QgTlVMTCxcbiAgICBob29rX25hbWUgdGV4dCBOT1QgTlVMTCxcbiAgICBjcmVhdGVkX2F0IHRpbWVzdGFtcHR6IE5PVCBOVUxMIERFRkFVTFQgTk9XKCksXG4gICAgcmVxdWVzdF9pZCBiaWdpbnRcbiAgKTtcbiAgQ1JFQVRFIElOREVYIHN1cGFiYXNlX2Z1bmN0aW9uc19ob29rc19yZXF1ZXN0X2lkX2lkeCBPTiBzdXBhYmFzZV9mdW5jdGlvbnMuaG9va3MgVVNJTkcgYnRyZWUgKHJlcXVlc3RfaWQpO1xuICBDUkVBVEUgSU5ERVggc3VwYWJhc2VfZnVuY3Rpb25zX2hvb2tzX2hfdGFibGVfaWRfaF9uYW1lX2lkeCBPTiBzdXBhYmFzZV9mdW5jdGlvbnMuaG9va3MgVVNJTkcgYnRyZWUgKGhvb2tfdGFibGVfaWQsIGhvb2tfbmFtZSk7XG4gIENPTU1FTlQgT04gVEFCTEUgc3VwYWJhc2VfZnVuY3Rpb25zLmhvb2tzIElTICdTdXBhYmFzZSBGdW5jdGlvbnMgSG9va3M6IEF1ZGl0IHRyYWlsIGZvciB0cmlnZ2VyZWQgaG9va3MuJztcbiAgQ1JFQVRFIEZVTkNUSU9OIHN1cGFiYXNlX2Z1bmN0aW9ucy5odHRwX3JlcXVlc3QoKVxuICAgIFJFVFVSTlMgdHJpZ2dlclxuICAgIExBTkdVQUdFIHBscGdzcWxcbiAgICBBUyAkZnVuY3Rpb24kXG4gICAgREVDTEFSRVxuICAgICAgcmVxdWVzdF9pZCBiaWdpbnQ7XG4gICAgICBwYXlsb2FkIGpzb25iO1xuICAgICAgdXJsIHRleHQgOj0gVEdfQVJHVlswXTo6dGV4dDtcbiAgICAgIG1ldGhvZCB0ZXh0IDo9IFRHX0FSR1ZbMV06OnRleHQ7XG4gICAgICBoZWFkZXJzIGpzb25iIERFRkFVTFQgJ3t9Jzo6anNvbmI7XG4gICAgICBwYXJhbXMganNvbmIgREVGQVVMVCAne30nOjpqc29uYjtcbiAgICAgIHRpbWVvdXRfbXMgaW50ZWdlciBERUZBVUxUIDEwMDA7XG4gICAgQkVHSU5cbiAgICAgIElGIHVybCBJUyBOVUxMIE9SIHVybCA9ICdudWxsJyBUSEVOXG4gICAgICAgIFJBSVNFIEVYQ0VQVElPTiAndXJsIGFyZ3VtZW50IGlzIG1pc3NpbmcnO1xuICAgICAgRU5EIElGO1xuXG4gICAgICBJRiBtZXRob2QgSVMgTlVMTCBPUiBtZXRob2QgPSAnbnVsbCcgVEhFTlxuICAgICAgICBSQUlTRSBFWENFUFRJT04gJ21ldGhvZCBhcmd1bWVudCBpcyBtaXNzaW5nJztcbiAgICAgIEVORCBJRjtcblxuICAgICAgSUYgVEdfQVJHVlsyXSBJUyBOVUxMIE9SIFRHX0FSR1ZbMl0gPSAnbnVsbCcgVEhFTlxuICAgICAgICBoZWFkZXJzID0gJ3tcIkNvbnRlbnQtVHlwZVwiOiBcImFwcGxpY2F0aW9uL2pzb25cIn0nOjpqc29uYjtcbiAgICAgIEVMU0VcbiAgICAgICAgaGVhZGVycyA9IFRHX0FSR1ZbMl06Ompzb25iO1xuICAgICAgRU5EIElGO1xuXG4gICAgICBJRiBUR19BUkdWWzNdIElTIE5VTEwgT1IgVEdfQVJHVlszXSA9ICdudWxsJyBUSEVOXG4gICAgICAgIHBhcmFtcyA9ICd7fSc6Ompzb25iO1xuICAgICAgRUxTRVxuICAgICAgICBwYXJhbXMgPSBUR19BUkdWWzNdOjpqc29uYjtcbiAgICAgIEVORCBJRjtcblxuICAgICAgSUYgVEdfQVJHVls0XSBJUyBOVUxMIE9SIFRHX0FSR1ZbNF0gPSAnbnVsbCcgVEhFTlxuICAgICAgICB0aW1lb3V0X21zID0gMTAwMDtcbiAgICAgIEVMU0VcbiAgICAgICAgdGltZW91dF9tcyA9IFRHX0FSR1ZbNF06OmludGVnZXI7XG4gICAgICBFTkQgSUY7XG5cbiAgICAgIENBU0VcbiAgICAgICAgV0hFTiBtZXRob2QgPSAnR0VUJyBUSEVOXG4gICAgICAgICAgU0VMRUNUIGh0dHBfZ2V0IElOVE8gcmVxdWVzdF9pZCBGUk9NIG5ldC5odHRwX2dldChcbiAgICAgICAgICAgIHVybCxcbiAgICAgICAgICAgIHBhcmFtcyxcbiAgICAgICAgICAgIGhlYWRlcnMsXG4gICAgICAgICAgICB0aW1lb3V0X21zXG4gICAgICAgICAgKTtcbiAgICAgICAgV0hFTiBtZXRob2QgPSAnUE9TVCcgVEhFTlxuICAgICAgICAgIHBheWxvYWQgPSBqc29uYl9idWlsZF9vYmplY3QoXG4gICAgICAgICAgICAnb2xkX3JlY29yZCcsIE9MRCxcbiAgICAgICAgICAgICdyZWNvcmQnLCBORVcsXG4gICAgICAgICAgICAndHlwZScsIFRHX09QLFxuICAgICAgICAgICAgJ3RhYmxlJywgVEdfVEFCTEVfTkFNRSxcbiAgICAgICAgICAgICdzY2hlbWEnLCBUR19UQUJMRV9TQ0hFTUFcbiAgICAgICAgICApO1xuXG4gICAgICAgICAgU0VMRUNUIGh0dHBfcG9zdCBJTlRPIHJlcXVlc3RfaWQgRlJPTSBuZXQuaHR0cF9wb3N0KFxuICAgICAgICAgICAgdXJsLFxuICAgICAgICAgICAgcGF5bG9hZCxcbiAgICAgICAgICAgIHBhcmFtcyxcbiAgICAgICAgICAgIGhlYWRlcnMsXG4gICAgICAgICAgICB0aW1lb3V0X21zXG4gICAgICAgICAgKTtcbiAgICAgICAgRUxTRVxuICAgICAgICAgIFJBSVNFIEVYQ0VQVElPTiAnbWV0aG9kIGFyZ3VtZW50ICUgaXMgaW52YWxpZCcsIG1ldGhvZDtcbiAgICAgIEVORCBDQVNFO1xuXG4gICAgICBJTlNFUlQgSU5UTyBzdXBhYmFzZV9mdW5jdGlvbnMuaG9va3NcbiAgICAgICAgKGhvb2tfdGFibGVfaWQsIGhvb2tfbmFtZSwgcmVxdWVzdF9pZClcbiAgICAgIFZBTFVFU1xuICAgICAgICAoVEdfUkVMSUQsIFRHX05BTUUsIHJlcXVlc3RfaWQpO1xuXG4gICAgICBSRVRVUk4gTkVXO1xuICAgIEVORFxuICAkZnVuY3Rpb24kO1xuICAtLSBTdXBhYmFzZSBzdXBlciBhZG1pblxuICBET1xuICAkJFxuICBCRUdJTlxuICAgIElGIE5PVCBFWElTVFMgKFxuICAgICAgU0VMRUNUIDFcbiAgICAgIEZST00gcGdfcm9sZXNcbiAgICAgIFdIRVJFIHJvbG5hbWUgPSAnc3VwYWJhc2VfZnVuY3Rpb25zX2FkbWluJ1xuICAgIClcbiAgICBUSEVOXG4gICAgICBDUkVBVEUgVVNFUiBzdXBhYmFzZV9mdW5jdGlvbnNfYWRtaW4gTk9JTkhFUklUIENSRUFURVJPTEUgTE9HSU4gTk9SRVBMSUNBVElPTjtcbiAgICBFTkQgSUY7XG4gIEVORFxuICAkJDtcbiAgR1JBTlQgQUxMIFBSSVZJTEVHRVMgT04gU0NIRU1BIHN1cGFiYXNlX2Z1bmN0aW9ucyBUTyBzdXBhYmFzZV9mdW5jdGlvbnNfYWRtaW47XG4gIEdSQU5UIEFMTCBQUklWSUxFR0VTIE9OIEFMTCBUQUJMRVMgSU4gU0NIRU1BIHN1cGFiYXNlX2Z1bmN0aW9ucyBUTyBzdXBhYmFzZV9mdW5jdGlvbnNfYWRtaW47XG4gIEdSQU5UIEFMTCBQUklWSUxFR0VTIE9OIEFMTCBTRVFVRU5DRVMgSU4gU0NIRU1BIHN1cGFiYXNlX2Z1bmN0aW9ucyBUTyBzdXBhYmFzZV9mdW5jdGlvbnNfYWRtaW47XG4gIEFMVEVSIFVTRVIgc3VwYWJhc2VfZnVuY3Rpb25zX2FkbWluIFNFVCBzZWFyY2hfcGF0aCA9IFwic3VwYWJhc2VfZnVuY3Rpb25zXCI7XG4gIEFMVEVSIHRhYmxlIFwic3VwYWJhc2VfZnVuY3Rpb25zXCIubWlncmF0aW9ucyBPV05FUiBUTyBzdXBhYmFzZV9mdW5jdGlvbnNfYWRtaW47XG4gIEFMVEVSIHRhYmxlIFwic3VwYWJhc2VfZnVuY3Rpb25zXCIuaG9va3MgT1dORVIgVE8gc3VwYWJhc2VfZnVuY3Rpb25zX2FkbWluO1xuICBBTFRFUiBmdW5jdGlvbiBcInN1cGFiYXNlX2Z1bmN0aW9uc1wiLmh0dHBfcmVxdWVzdCgpIE9XTkVSIFRPIHN1cGFiYXNlX2Z1bmN0aW9uc19hZG1pbjtcbiAgR1JBTlQgc3VwYWJhc2VfZnVuY3Rpb25zX2FkbWluIFRPIHBvc3RncmVzO1xuICAtLSBSZW1vdmUgdW51c2VkIHN1cGFiYXNlX3BnX25ldF9hZG1pbiByb2xlXG4gIERPXG4gICQkXG4gIEJFR0lOXG4gICAgSUYgRVhJU1RTIChcbiAgICAgIFNFTEVDVCAxXG4gICAgICBGUk9NIHBnX3JvbGVzXG4gICAgICBXSEVSRSByb2xuYW1lID0gJ3N1cGFiYXNlX3BnX25ldF9hZG1pbidcbiAgICApXG4gICAgVEhFTlxuICAgICAgUkVBU1NJR04gT1dORUQgQlkgc3VwYWJhc2VfcGdfbmV0X2FkbWluIFRPIHN1cGFiYXNlX2FkbWluO1xuICAgICAgRFJPUCBPV05FRCBCWSBzdXBhYmFzZV9wZ19uZXRfYWRtaW47XG4gICAgICBEUk9QIFJPTEUgc3VwYWJhc2VfcGdfbmV0X2FkbWluO1xuICAgIEVORCBJRjtcbiAgRU5EXG4gICQkO1xuICAtLSBwZ19uZXQgZ3JhbnRzIHdoZW4gZXh0ZW5zaW9uIGlzIGFscmVhZHkgZW5hYmxlZFxuICBET1xuICAkJFxuICBCRUdJTlxuICAgIElGIEVYSVNUUyAoXG4gICAgICBTRUxFQ1QgMVxuICAgICAgRlJPTSBwZ19leHRlbnNpb25cbiAgICAgIFdIRVJFIGV4dG5hbWUgPSAncGdfbmV0J1xuICAgIClcbiAgICBUSEVOXG4gICAgICBHUkFOVCBVU0FHRSBPTiBTQ0hFTUEgbmV0IFRPIHN1cGFiYXNlX2Z1bmN0aW9uc19hZG1pbiwgcG9zdGdyZXMsIGFub24sIGF1dGhlbnRpY2F0ZWQsIHNlcnZpY2Vfcm9sZTtcbiAgICAgIEFMVEVSIGZ1bmN0aW9uIG5ldC5odHRwX2dldCh1cmwgdGV4dCwgcGFyYW1zIGpzb25iLCBoZWFkZXJzIGpzb25iLCB0aW1lb3V0X21pbGxpc2Vjb25kcyBpbnRlZ2VyKSBTRUNVUklUWSBERUZJTkVSO1xuICAgICAgQUxURVIgZnVuY3Rpb24gbmV0Lmh0dHBfcG9zdCh1cmwgdGV4dCwgYm9keSBqc29uYiwgcGFyYW1zIGpzb25iLCBoZWFkZXJzIGpzb25iLCB0aW1lb3V0X21pbGxpc2Vjb25kcyBpbnRlZ2VyKSBTRUNVUklUWSBERUZJTkVSO1xuICAgICAgQUxURVIgZnVuY3Rpb24gbmV0Lmh0dHBfZ2V0KHVybCB0ZXh0LCBwYXJhbXMganNvbmIsIGhlYWRlcnMganNvbmIsIHRpbWVvdXRfbWlsbGlzZWNvbmRzIGludGVnZXIpIFNFVCBzZWFyY2hfcGF0aCA9IG5ldDtcbiAgICAgIEFMVEVSIGZ1bmN0aW9uIG5ldC5odHRwX3Bvc3QodXJsIHRleHQsIGJvZHkganNvbmIsIHBhcmFtcyBqc29uYiwgaGVhZGVycyBqc29uYiwgdGltZW91dF9taWxsaXNlY29uZHMgaW50ZWdlcikgU0VUIHNlYXJjaF9wYXRoID0gbmV0O1xuICAgICAgUkVWT0tFIEFMTCBPTiBGVU5DVElPTiBuZXQuaHR0cF9nZXQodXJsIHRleHQsIHBhcmFtcyBqc29uYiwgaGVhZGVycyBqc29uYiwgdGltZW91dF9taWxsaXNlY29uZHMgaW50ZWdlcikgRlJPTSBQVUJMSUM7XG4gICAgICBSRVZPS0UgQUxMIE9OIEZVTkNUSU9OIG5ldC5odHRwX3Bvc3QodXJsIHRleHQsIGJvZHkganNvbmIsIHBhcmFtcyBqc29uYiwgaGVhZGVycyBqc29uYiwgdGltZW91dF9taWxsaXNlY29uZHMgaW50ZWdlcikgRlJPTSBQVUJMSUM7XG4gICAgICBHUkFOVCBFWEVDVVRFIE9OIEZVTkNUSU9OIG5ldC5odHRwX2dldCh1cmwgdGV4dCwgcGFyYW1zIGpzb25iLCBoZWFkZXJzIGpzb25iLCB0aW1lb3V0X21pbGxpc2Vjb25kcyBpbnRlZ2VyKSBUTyBzdXBhYmFzZV9mdW5jdGlvbnNfYWRtaW4sIHBvc3RncmVzLCBhbm9uLCBhdXRoZW50aWNhdGVkLCBzZXJ2aWNlX3JvbGU7XG4gICAgICBHUkFOVCBFWEVDVVRFIE9OIEZVTkNUSU9OIG5ldC5odHRwX3Bvc3QodXJsIHRleHQsIGJvZHkganNvbmIsIHBhcmFtcyBqc29uYiwgaGVhZGVycyBqc29uYiwgdGltZW91dF9taWxsaXNlY29uZHMgaW50ZWdlcikgVE8gc3VwYWJhc2VfZnVuY3Rpb25zX2FkbWluLCBwb3N0Z3JlcywgYW5vbiwgYXV0aGVudGljYXRlZCwgc2VydmljZV9yb2xlO1xuICAgIEVORCBJRjtcbiAgRU5EXG4gICQkO1xuICAtLSBFdmVudCB0cmlnZ2VyIGZvciBwZ19uZXRcbiAgQ1JFQVRFIE9SIFJFUExBQ0UgRlVOQ1RJT04gZXh0ZW5zaW9ucy5ncmFudF9wZ19uZXRfYWNjZXNzKClcbiAgUkVUVVJOUyBldmVudF90cmlnZ2VyXG4gIExBTkdVQUdFIHBscGdzcWxcbiAgQVMgJCRcbiAgQkVHSU5cbiAgICBJRiBFWElTVFMgKFxuICAgICAgU0VMRUNUIDFcbiAgICAgIEZST00gcGdfZXZlbnRfdHJpZ2dlcl9kZGxfY29tbWFuZHMoKSBBUyBldlxuICAgICAgSk9JTiBwZ19leHRlbnNpb24gQVMgZXh0XG4gICAgICBPTiBldi5vYmppZCA9IGV4dC5vaWRcbiAgICAgIFdIRVJFIGV4dC5leHRuYW1lID0gJ3BnX25ldCdcbiAgICApXG4gICAgVEhFTlxuICAgICAgR1JBTlQgVVNBR0UgT04gU0NIRU1BIG5ldCBUTyBzdXBhYmFzZV9mdW5jdGlvbnNfYWRtaW4sIHBvc3RncmVzLCBhbm9uLCBhdXRoZW50aWNhdGVkLCBzZXJ2aWNlX3JvbGU7XG4gICAgICBBTFRFUiBmdW5jdGlvbiBuZXQuaHR0cF9nZXQodXJsIHRleHQsIHBhcmFtcyBqc29uYiwgaGVhZGVycyBqc29uYiwgdGltZW91dF9taWxsaXNlY29uZHMgaW50ZWdlcikgU0VDVVJJVFkgREVGSU5FUjtcbiAgICAgIEFMVEVSIGZ1bmN0aW9uIG5ldC5odHRwX3Bvc3QodXJsIHRleHQsIGJvZHkganNvbmIsIHBhcmFtcyBqc29uYiwgaGVhZGVycyBqc29uYiwgdGltZW91dF9taWxsaXNlY29uZHMgaW50ZWdlcikgU0VDVVJJVFkgREVGSU5FUjtcbiAgICAgIEFMVEVSIGZ1bmN0aW9uIG5ldC5odHRwX2dldCh1cmwgdGV4dCwgcGFyYW1zIGpzb25iLCBoZWFkZXJzIGpzb25iLCB0aW1lb3V0X21pbGxpc2Vjb25kcyBpbnRlZ2VyKSBTRVQgc2VhcmNoX3BhdGggPSBuZXQ7XG4gICAgICBBTFRFUiBmdW5jdGlvbiBuZXQuaHR0cF9wb3N0KHVybCB0ZXh0LCBib2R5IGpzb25iLCBwYXJhbXMganNvbmIsIGhlYWRlcnMganNvbmIsIHRpbWVvdXRfbWlsbGlzZWNvbmRzIGludGVnZXIpIFNFVCBzZWFyY2hfcGF0aCA9IG5ldDtcbiAgICAgIFJFVk9LRSBBTEwgT04gRlVOQ1RJT04gbmV0Lmh0dHBfZ2V0KHVybCB0ZXh0LCBwYXJhbXMganNvbmIsIGhlYWRlcnMganNvbmIsIHRpbWVvdXRfbWlsbGlzZWNvbmRzIGludGVnZXIpIEZST00gUFVCTElDO1xuICAgICAgUkVWT0tFIEFMTCBPTiBGVU5DVElPTiBuZXQuaHR0cF9wb3N0KHVybCB0ZXh0LCBib2R5IGpzb25iLCBwYXJhbXMganNvbmIsIGhlYWRlcnMganNvbmIsIHRpbWVvdXRfbWlsbGlzZWNvbmRzIGludGVnZXIpIEZST00gUFVCTElDO1xuICAgICAgR1JBTlQgRVhFQ1VURSBPTiBGVU5DVElPTiBuZXQuaHR0cF9nZXQodXJsIHRleHQsIHBhcmFtcyBqc29uYiwgaGVhZGVycyBqc29uYiwgdGltZW91dF9taWxsaXNlY29uZHMgaW50ZWdlcikgVE8gc3VwYWJhc2VfZnVuY3Rpb25zX2FkbWluLCBwb3N0Z3JlcywgYW5vbiwgYXV0aGVudGljYXRlZCwgc2VydmljZV9yb2xlO1xuICAgICAgR1JBTlQgRVhFQ1VURSBPTiBGVU5DVElPTiBuZXQuaHR0cF9wb3N0KHVybCB0ZXh0LCBib2R5IGpzb25iLCBwYXJhbXMganNvbmIsIGhlYWRlcnMganNvbmIsIHRpbWVvdXRfbWlsbGlzZWNvbmRzIGludGVnZXIpIFRPIHN1cGFiYXNlX2Z1bmN0aW9uc19hZG1pbiwgcG9zdGdyZXMsIGFub24sIGF1dGhlbnRpY2F0ZWQsIHNlcnZpY2Vfcm9sZTtcbiAgICBFTkQgSUY7XG4gIEVORDtcbiAgJCQ7XG4gIENPTU1FTlQgT04gRlVOQ1RJT04gZXh0ZW5zaW9ucy5ncmFudF9wZ19uZXRfYWNjZXNzIElTICdHcmFudHMgYWNjZXNzIHRvIHBnX25ldCc7XG4gIERPXG4gICQkXG4gIEJFR0lOXG4gICAgSUYgTk9UIEVYSVNUUyAoXG4gICAgICBTRUxFQ1QgMVxuICAgICAgRlJPTSBwZ19ldmVudF90cmlnZ2VyXG4gICAgICBXSEVSRSBldnRuYW1lID0gJ2lzc3VlX3BnX25ldF9hY2Nlc3MnXG4gICAgKSBUSEVOXG4gICAgICBDUkVBVEUgRVZFTlQgVFJJR0dFUiBpc3N1ZV9wZ19uZXRfYWNjZXNzIE9OIGRkbF9jb21tYW5kX2VuZCBXSEVOIFRBRyBJTiAoJ0NSRUFURSBFWFRFTlNJT04nKVxuICAgICAgRVhFQ1VURSBQUk9DRURVUkUgZXh0ZW5zaW9ucy5ncmFudF9wZ19uZXRfYWNjZXNzKCk7XG4gICAgRU5EIElGO1xuICBFTkRcbiAgJCQ7XG4gIElOU0VSVCBJTlRPIHN1cGFiYXNlX2Z1bmN0aW9ucy5taWdyYXRpb25zICh2ZXJzaW9uKSBWQUxVRVMgKCcyMDIxMDgwOTE4MzQyM191cGRhdGVfZ3JhbnRzJyk7XG4gIEFMVEVSIGZ1bmN0aW9uIHN1cGFiYXNlX2Z1bmN0aW9ucy5odHRwX3JlcXVlc3QoKSBTRUNVUklUWSBERUZJTkVSO1xuICBBTFRFUiBmdW5jdGlvbiBzdXBhYmFzZV9mdW5jdGlvbnMuaHR0cF9yZXF1ZXN0KCkgU0VUIHNlYXJjaF9wYXRoID0gc3VwYWJhc2VfZnVuY3Rpb25zO1xuICBSRVZPS0UgQUxMIE9OIEZVTkNUSU9OIHN1cGFiYXNlX2Z1bmN0aW9ucy5odHRwX3JlcXVlc3QoKSBGUk9NIFBVQkxJQztcbiAgR1JBTlQgRVhFQ1VURSBPTiBGVU5DVElPTiBzdXBhYmFzZV9mdW5jdGlvbnMuaHR0cF9yZXF1ZXN0KCkgVE8gcG9zdGdyZXMsIGFub24sIGF1dGhlbnRpY2F0ZWQsIHNlcnZpY2Vfcm9sZTtcbkNPTU1JVDtcblwiXCJcIlxuXG5bW2NvbmZpZy5tb3VudHNdXVxuZmlsZVBhdGggPSBcIi92b2x1bWVzL2Z1bmN0aW9ucy9oZWxsby9pbmRleC50c1wiXG5jb250ZW50ID0gXCJcIlwiXG4vLyBGb2xsb3cgdGhpcyBzZXR1cCBndWlkZSB0byBpbnRlZ3JhdGUgdGhlIERlbm8gbGFuZ3VhZ2Ugc2VydmVyIHdpdGggeW91ciBlZGl0b3I6XG4vLyBodHRwczovL2Rlbm8ubGFuZC9tYW51YWwvZ2V0dGluZ19zdGFydGVkL3NldHVwX3lvdXJfZW52aXJvbm1lbnRcbi8vIFRoaXMgZW5hYmxlcyBhdXRvY29tcGxldGUsIGdvIHRvIGRlZmluaXRpb24sIGV0Yy5cblxuaW1wb3J0IHsgc2VydmUgfSBmcm9tIFwiaHR0cHM6Ly9kZW5vLmxhbmQvc3RkQDAuMTc3LjEvaHR0cC9zZXJ2ZXIudHNcIlxuXG5zZXJ2ZShhc3luYyAoKSA9PiB7XG4gIHJldHVybiBuZXcgUmVzcG9uc2UoXG4gICAgYFwiSGVsbG8gZnJvbSBFZGdlIEZ1bmN0aW9ucyFcImAsXG4gICAgeyBoZWFkZXJzOiB7IFwiQ29udGVudC1UeXBlXCI6IFwiYXBwbGljYXRpb24vanNvblwiIH0gfSxcbiAgKVxufSlcblxuLy8gVG8gaW52b2tlOlxuLy8gY3VybCAnaHR0cDovL2xvY2FsaG9zdDo8S09OR19IVFRQX1BPUlQ+L2Z1bmN0aW9ucy92MS9oZWxsbycgXFxcbi8vICAgLS1oZWFkZXIgJ0F1dGhvcml6YXRpb246IEJlYXJlciA8YW5vbi9zZXJ2aWNlX3JvbGUgQVBJIGtleT4nXG5cIlwiXCJcblxuW1tjb25maWcubW91bnRzXV1cbmZpbGVQYXRoID0gXCIvdm9sdW1lcy9mdW5jdGlvbnMvbWFpbi9pbmRleC50c1wiXG5jb250ZW50ID0gXCJcIlwiaW1wb3J0IHsgc2VydmUgfSBmcm9tICdodHRwczovL2Rlbm8ubGFuZC9zdGRAMC4xMzEuMC9odHRwL3NlcnZlci50cydcbmltcG9ydCAqIGFzIGpvc2UgZnJvbSAnaHR0cHM6Ly9kZW5vLmxhbmQveC9qb3NlQHY0LjE0LjQvaW5kZXgudHMnXG5cbmNvbnNvbGUubG9nKCdtYWluIGZ1bmN0aW9uIHN0YXJ0ZWQnKVxuXG5jb25zdCBKV1RfU0VDUkVUID0gRGVuby5lbnYuZ2V0KCdKV1RfU0VDUkVUJylcbmNvbnN0IFZFUklGWV9KV1QgPSBEZW5vLmVudi5nZXQoJ1ZFUklGWV9KV1QnKSA9PT0gJ3RydWUnXG5cbmZ1bmN0aW9uIGdldEF1dGhUb2tlbihyZXE6IFJlcXVlc3QpIHtcbiAgY29uc3QgYXV0aEhlYWRlciA9IHJlcS5oZWFkZXJzLmdldCgnYXV0aG9yaXphdGlvbicpXG4gIGlmICghYXV0aEhlYWRlcikge1xuICAgIHRocm93IG5ldyBFcnJvcignTWlzc2luZyBhdXRob3JpemF0aW9uIGhlYWRlcicpXG4gIH1cbiAgY29uc3QgW2JlYXJlciwgdG9rZW5dID0gYXV0aEhlYWRlci5zcGxpdCgnICcpXG4gIGlmIChiZWFyZXIgIT09ICdCZWFyZXInKSB7XG4gICAgdGhyb3cgbmV3IEVycm9yKGBBdXRoIGhlYWRlciBpcyBub3QgJ0JlYXJlciB7dG9rZW59J2ApXG4gIH1cbiAgcmV0dXJuIHRva2VuXG59XG5cbmFzeW5jIGZ1bmN0aW9uIHZlcmlmeUpXVChqd3Q6IHN0cmluZyk6IFByb21pc2U8Ym9vbGVhbj4ge1xuICBjb25zdCBlbmNvZGVyID0gbmV3IFRleHRFbmNvZGVyKClcbiAgY29uc3Qgc2VjcmV0S2V5ID0gZW5jb2Rlci5lbmNvZGUoSldUX1NFQ1JFVClcbiAgdHJ5IHtcbiAgICBhd2FpdCBqb3NlLmp3dFZlcmlmeShqd3QsIHNlY3JldEtleSlcbiAgfSBjYXRjaCAoZXJyKSB7XG4gICAgY29uc29sZS5lcnJvcihlcnIpXG4gICAgcmV0dXJuIGZhbHNlXG4gIH1cbiAgcmV0dXJuIHRydWVcbn1cblxuc2VydmUoYXN5bmMgKHJlcTogUmVxdWVzdCkgPT4ge1xuICBpZiAocmVxLm1ldGhvZCAhPT0gJ09QVElPTlMnICYmIFZFUklGWV9KV1QpIHtcbiAgICB0cnkge1xuICAgICAgY29uc3QgdG9rZW4gPSBnZXRBdXRoVG9rZW4ocmVxKVxuICAgICAgY29uc3QgaXNWYWxpZEpXVCA9IGF3YWl0IHZlcmlmeUpXVCh0b2tlbilcblxuICAgICAgaWYgKCFpc1ZhbGlkSldUKSB7XG4gICAgICAgIHJldHVybiBuZXcgUmVzcG9uc2UoSlNPTi5zdHJpbmdpZnkoeyBtc2c6ICdJbnZhbGlkIEpXVCcgfSksIHtcbiAgICAgICAgICBzdGF0dXM6IDQwMSxcbiAgICAgICAgICBoZWFkZXJzOiB7ICdDb250ZW50LVR5cGUnOiAnYXBwbGljYXRpb24vanNvbicgfSxcbiAgICAgICAgfSlcbiAgICAgIH1cbiAgICB9IGNhdGNoIChlKSB7XG4gICAgICBjb25zb2xlLmVycm9yKGUpXG4gICAgICByZXR1cm4gbmV3IFJlc3BvbnNlKEpTT04uc3RyaW5naWZ5KHsgbXNnOiBlLnRvU3RyaW5nKCkgfSksIHtcbiAgICAgICAgc3RhdHVzOiA0MDEsXG4gICAgICAgIGhlYWRlcnM6IHsgJ0NvbnRlbnQtVHlwZSc6ICdhcHBsaWNhdGlvbi9qc29uJyB9LFxuICAgICAgfSlcbiAgICB9XG4gIH1cblxuICBjb25zdCB1cmwgPSBuZXcgVVJMKHJlcS51cmwpXG4gIGNvbnN0IHsgcGF0aG5hbWUgfSA9IHVybFxuICBjb25zdCBwYXRoX3BhcnRzID0gcGF0aG5hbWUuc3BsaXQoJy8nKVxuICBjb25zdCBzZXJ2aWNlX25hbWUgPSBwYXRoX3BhcnRzWzFdXG5cbiAgaWYgKCFzZXJ2aWNlX25hbWUgfHwgc2VydmljZV9uYW1lID09PSAnJykge1xuICAgIGNvbnN0IGVycm9yID0geyBtc2c6ICdtaXNzaW5nIGZ1bmN0aW9uIG5hbWUgaW4gcmVxdWVzdCcgfVxuICAgIHJldHVybiBuZXcgUmVzcG9uc2UoSlNPTi5zdHJpbmdpZnkoZXJyb3IpLCB7XG4gICAgICBzdGF0dXM6IDQwMCxcbiAgICAgIGhlYWRlcnM6IHsgJ0NvbnRlbnQtVHlwZSc6ICdhcHBsaWNhdGlvbi9qc29uJyB9LFxuICAgIH0pXG4gIH1cblxuICBjb25zdCBzZXJ2aWNlUGF0aCA9IGAvaG9tZS9kZW5vL2Z1bmN0aW9ucy8ke3NlcnZpY2VfbmFtZX1gXG4gIGNvbnNvbGUuZXJyb3IoYHNlcnZpbmcgdGhlIHJlcXVlc3Qgd2l0aCAke3NlcnZpY2VQYXRofWApXG5cbiAgY29uc3QgbWVtb3J5TGltaXRNYiA9IDE1MFxuICBjb25zdCB3b3JrZXJUaW1lb3V0TXMgPSAxICogNjAgKiAxMDAwXG4gIGNvbnN0IG5vTW9kdWxlQ2FjaGUgPSBmYWxzZVxuICBjb25zdCBpbXBvcnRNYXBQYXRoID0gbnVsbFxuICBjb25zdCBlbnZWYXJzT2JqID0gRGVuby5lbnYudG9PYmplY3QoKVxuICBjb25zdCBlbnZWYXJzID0gT2JqZWN0LmtleXMoZW52VmFyc09iaikubWFwKChrKSA9PiBbaywgZW52VmFyc09ialtrXV0pXG5cbiAgdHJ5IHtcbiAgICBjb25zdCB3b3JrZXIgPSBhd2FpdCBFZGdlUnVudGltZS51c2VyV29ya2Vycy5jcmVhdGUoe1xuICAgICAgc2VydmljZVBhdGgsXG4gICAgICBtZW1vcnlMaW1pdE1iLFxuICAgICAgd29ya2VyVGltZW91dE1zLFxuICAgICAgbm9Nb2R1bGVDYWNoZSxcbiAgICAgIGltcG9ydE1hcFBhdGgsXG4gICAgICBlbnZWYXJzLFxuICAgIH0pXG4gICAgcmV0dXJuIGF3YWl0IHdvcmtlci5mZXRjaChyZXEpXG4gIH0gY2F0Y2ggKGUpIHtcbiAgICBjb25zdCBlcnJvciA9IHsgbXNnOiBlLnRvU3RyaW5nKCkgfVxuICAgIHJldHVybiBuZXcgUmVzcG9uc2UoSlNPTi5zdHJpbmdpZnkoZXJyb3IpLCB7XG4gICAgICBzdGF0dXM6IDUwMCxcbiAgICAgIGhlYWRlcnM6IHsgJ0NvbnRlbnQtVHlwZSc6ICdhcHBsaWNhdGlvbi9qc29uJyB9LFxuICAgIH0pXG4gIH1cbn0pXG5cIlwiXCJcblxuW1tjb25maWcubW91bnRzXV1cbmZpbGVQYXRoID0gXCIvdm9sdW1lcy9sb2dzL3ZlY3Rvci55bWxcIlxuY29udGVudCA9IFwiXCJcImFwaTpcbiAgZW5hYmxlZDogdHJ1ZVxuICBhZGRyZXNzOiAwLjAuMC4wOjkwMDFcblxuc291cmNlczpcbiAgZG9ja2VyX2hvc3Q6XG4gICAgdHlwZTogZG9ja2VyX2xvZ3NcbiAgICBleGNsdWRlX2NvbnRhaW5lcnM6XG4gICAgICAtICR7Y29udGFpbmVyX25hbWVfcHJlZml4fS12ZWN0b3JcblxudHJhbnNmb3JtczpcbiAgcHJvamVjdF9sb2dzOlxuICAgIHR5cGU6IHJlbWFwXG4gICAgaW5wdXRzOlxuICAgICAgLSBkb2NrZXJfaG9zdFxuICAgIHNvdXJjZTogfC1cbiAgICAgIC5wcm9qZWN0ID0gXCJkZWZhdWx0XCJcbiAgICAgIC5ldmVudF9tZXNzYWdlID0gZGVsKC5tZXNzYWdlKVxuICAgICAgLmFwcG5hbWUgPSByZXBsYWNlIShkZWwoLmNvbnRhaW5lcl9uYW1lKSwgXCIke2NvbnRhaW5lcl9uYW1lX3ByZWZpeH1cIiwgXCJzdXBhYmFzZVwiKVxuICAgICAgZGVsKC5jb250YWluZXJfY3JlYXRlZF9hdClcbiAgICAgIGRlbCguY29udGFpbmVyX2lkKVxuICAgICAgZGVsKC5zb3VyY2VfdHlwZSlcbiAgICAgIGRlbCguc3RyZWFtKVxuICAgICAgZGVsKC5sYWJlbClcbiAgICAgIGRlbCguaW1hZ2UpXG4gICAgICBkZWwoLmhvc3QpXG4gICAgICBkZWwoLnN0cmVhbSlcbiAgcm91dGVyOlxuICAgIHR5cGU6IHJvdXRlXG4gICAgaW5wdXRzOlxuICAgICAgLSBwcm9qZWN0X2xvZ3NcbiAgICByb3V0ZTpcbiAgICAgIGtvbmc6ICcuYXBwbmFtZSA9PSBcInN1cGFiYXNlLWtvbmdcIidcbiAgICAgIGF1dGg6ICcuYXBwbmFtZSA9PSBcInN1cGFiYXNlLWF1dGhcIidcbiAgICAgIHJlc3Q6ICcuYXBwbmFtZSA9PSBcInN1cGFiYXNlLXJlc3RcIidcbiAgICAgIHJlYWx0aW1lOiAnLmFwcG5hbWUgPT0gXCJyZWFsdGltZS1kZXYuc3VwYWJhc2UtcmVhbHRpbWVcIidcbiAgICAgIHN0b3JhZ2U6ICcuYXBwbmFtZSA9PSBcInN1cGFiYXNlLXN0b3JhZ2VcIidcbiAgICAgIGZ1bmN0aW9uczogJy5hcHBuYW1lID09IFwic3VwYWJhc2UtZWRnZS1mdW5jdGlvbnNcIidcbiAgICAgIGRiOiAnLmFwcG5hbWUgPT0gXCJzdXBhYmFzZS1kYlwiJ1xuICAjIElnbm9yZXMgbm9uIG5naW54IGVycm9ycyBzaW5jZSB0aGV5IGFyZSByZWxhdGVkIHdpdGgga29uZyBib290aW5nIHVwXG4gIGtvbmdfbG9nczpcbiAgICB0eXBlOiByZW1hcFxuICAgIGlucHV0czpcbiAgICAgIC0gcm91dGVyLmtvbmdcbiAgICBzb3VyY2U6IHwtXG4gICAgICByZXEsIGVyciA9IHBhcnNlX25naW54X2xvZyguZXZlbnRfbWVzc2FnZSwgXCJjb21iaW5lZFwiKVxuICAgICAgaWYgZXJyID09IG51bGwge1xuICAgICAgICAgIC50aW1lc3RhbXAgPSByZXEudGltZXN0YW1wXG4gICAgICAgICAgLm1ldGFkYXRhLnJlcXVlc3QuaGVhZGVycy5yZWZlcmVyID0gcmVxLnJlZmVyZXJcbiAgICAgICAgICAubWV0YWRhdGEucmVxdWVzdC5oZWFkZXJzLnVzZXJfYWdlbnQgPSByZXEuYWdlbnRcbiAgICAgICAgICAubWV0YWRhdGEucmVxdWVzdC5oZWFkZXJzLmNmX2Nvbm5lY3RpbmdfaXAgPSByZXEuY2xpZW50XG4gICAgICAgICAgLm1ldGFkYXRhLnJlcXVlc3QubWV0aG9kID0gcmVxLm1ldGhvZFxuICAgICAgICAgIC5tZXRhZGF0YS5yZXF1ZXN0LnBhdGggPSByZXEucGF0aFxuICAgICAgICAgIC5tZXRhZGF0YS5yZXF1ZXN0LnByb3RvY29sID0gcmVxLnByb3RvY29sXG4gICAgICAgICAgLm1ldGFkYXRhLnJlc3BvbnNlLnN0YXR1c19jb2RlID0gcmVxLnN0YXR1c1xuICAgICAgfVxuICAgICAgaWYgZXJyICE9IG51bGwge1xuICAgICAgICBhYm9ydFxuICAgICAgfVxuICAjIElnbm9yZXMgbm9uIG5naW54IGVycm9ycyBzaW5jZSB0aGV5IGFyZSByZWxhdGVkIHdpdGgga29uZyBib290aW5nIHVwXG4gIGtvbmdfZXJyOlxuICAgIHR5cGU6IHJlbWFwXG4gICAgaW5wdXRzOlxuICAgICAgLSByb3V0ZXIua29uZ1xuICAgIHNvdXJjZTogfC1cbiAgICAgIC5tZXRhZGF0YS5yZXF1ZXN0Lm1ldGhvZCA9IFwiR0VUXCJcbiAgICAgIC5tZXRhZGF0YS5yZXNwb25zZS5zdGF0dXNfY29kZSA9IDIwMFxuICAgICAgcGFyc2VkLCBlcnIgPSBwYXJzZV9uZ2lueF9sb2coLmV2ZW50X21lc3NhZ2UsIFwiZXJyb3JcIilcbiAgICAgIGlmIGVyciA9PSBudWxsIHtcbiAgICAgICAgICAudGltZXN0YW1wID0gcGFyc2VkLnRpbWVzdGFtcFxuICAgICAgICAgIC5zZXZlcml0eSA9IHBhcnNlZC5zZXZlcml0eVxuICAgICAgICAgIC5tZXRhZGF0YS5yZXF1ZXN0Lmhvc3QgPSBwYXJzZWQuaG9zdFxuICAgICAgICAgIC5tZXRhZGF0YS5yZXF1ZXN0LmhlYWRlcnMuY2ZfY29ubmVjdGluZ19pcCA9IHBhcnNlZC5jbGllbnRcbiAgICAgICAgICB1cmwsIGVyciA9IHNwbGl0KHBhcnNlZC5yZXF1ZXN0LCBcIiBcIilcbiAgICAgICAgICBpZiBlcnIgPT0gbnVsbCB7XG4gICAgICAgICAgICAgIC5tZXRhZGF0YS5yZXF1ZXN0Lm1ldGhvZCA9IHVybFswXVxuICAgICAgICAgICAgICAubWV0YWRhdGEucmVxdWVzdC5wYXRoID0gdXJsWzFdXG4gICAgICAgICAgICAgIC5tZXRhZGF0YS5yZXF1ZXN0LnByb3RvY29sID0gdXJsWzJdXG4gICAgICAgICAgfVxuICAgICAgfVxuICAgICAgaWYgZXJyICE9IG51bGwge1xuICAgICAgICBhYm9ydFxuICAgICAgfVxuICAjIEdvdHJ1ZSBsb2dzIGFyZSBzdHJ1Y3R1cmVkIGpzb24gc3RyaW5ncyB3aGljaCBmcm9udGVuZCBwYXJzZXMgZGlyZWN0bHkuIEJ1dCB3ZSBrZWVwIG1ldGFkYXRhIGZvciBjb25zaXN0ZW5jeS5cbiAgYXV0aF9sb2dzOlxuICAgIHR5cGU6IHJlbWFwXG4gICAgaW5wdXRzOlxuICAgICAgLSByb3V0ZXIuYXV0aFxuICAgIHNvdXJjZTogfC1cbiAgICAgIHBhcnNlZCwgZXJyID0gcGFyc2VfanNvbiguZXZlbnRfbWVzc2FnZSlcbiAgICAgIGlmIGVyciA9PSBudWxsIHtcbiAgICAgICAgICAubWV0YWRhdGEudGltZXN0YW1wID0gcGFyc2VkLnRpbWVcbiAgICAgICAgICAubWV0YWRhdGEgPSBtZXJnZSEoLm1ldGFkYXRhLCBwYXJzZWQpXG4gICAgICB9XG4gICMgUG9zdGdSRVNUIGxvZ3MgYXJlIHN0cnVjdHVyZWQgc28gd2Ugc2VwYXJhdGUgdGltZXN0YW1wIGZyb20gbWVzc2FnZSB1c2luZyByZWdleFxuICByZXN0X2xvZ3M6XG4gICAgdHlwZTogcmVtYXBcbiAgICBpbnB1dHM6XG4gICAgICAtIHJvdXRlci5yZXN0XG4gICAgc291cmNlOiB8LVxuICAgICAgcGFyc2VkLCBlcnIgPSBwYXJzZV9yZWdleCguZXZlbnRfbWVzc2FnZSwgcideKD9QPHRpbWU+LiopOiAoP1A8bXNnPi4qKSQnKVxuICAgICAgaWYgZXJyID09IG51bGwge1xuICAgICAgICAgIC5ldmVudF9tZXNzYWdlID0gcGFyc2VkLm1zZ1xuICAgICAgICAgIC50aW1lc3RhbXAgPSB0b190aW1lc3RhbXAhKHBhcnNlZC50aW1lKVxuICAgICAgICAgIC5tZXRhZGF0YS5ob3N0ID0gLnByb2plY3RcbiAgICAgIH1cbiAgIyBSZWFsdGltZSBsb2dzIGFyZSBzdHJ1Y3R1cmVkIHNvIHdlIHBhcnNlIHRoZSBzZXZlcml0eSBsZXZlbCB1c2luZyByZWdleCAoaWdub3JlIHRpbWUgYmVjYXVzZSBpdCBoYXMgbm8gZGF0ZSlcbiAgcmVhbHRpbWVfbG9nczpcbiAgICB0eXBlOiByZW1hcFxuICAgIGlucHV0czpcbiAgICAgIC0gcm91dGVyLnJlYWx0aW1lXG4gICAgc291cmNlOiB8LVxuICAgICAgLm1ldGFkYXRhLnByb2plY3QgPSBkZWwoLnByb2plY3QpXG4gICAgICAubWV0YWRhdGEuZXh0ZXJuYWxfaWQgPSAubWV0YWRhdGEucHJvamVjdFxuICAgICAgcGFyc2VkLCBlcnIgPSBwYXJzZV9yZWdleCguZXZlbnRfbWVzc2FnZSwgcideKD9QPHRpbWU+XFxcXGQrOlxcXFxkKzpcXFxcZCtcXFxcLlxcXFxkKykgXFxcXFsoP1A8bGV2ZWw+XFxcXHcrKVxcXFxdICg/UDxtc2c+LiopJCcpXG4gICAgICBpZiBlcnIgPT0gbnVsbCB7XG4gICAgICAgICAgLmV2ZW50X21lc3NhZ2UgPSBwYXJzZWQubXNnXG4gICAgICAgICAgLm1ldGFkYXRhLmxldmVsID0gcGFyc2VkLmxldmVsXG4gICAgICB9XG4gICMgU3RvcmFnZSBsb2dzIG1heSBjb250YWluIGpzb24gb2JqZWN0cyBzbyB3ZSBwYXJzZSB0aGVtIGZvciBjb21wbGV0ZW5lc3NcbiAgc3RvcmFnZV9sb2dzOlxuICAgIHR5cGU6IHJlbWFwXG4gICAgaW5wdXRzOlxuICAgICAgLSByb3V0ZXIuc3RvcmFnZVxuICAgIHNvdXJjZTogfC1cbiAgICAgIC5tZXRhZGF0YS5wcm9qZWN0ID0gZGVsKC5wcm9qZWN0KVxuICAgICAgLm1ldGFkYXRhLnRlbmFudElkID0gLm1ldGFkYXRhLnByb2plY3RcbiAgICAgIHBhcnNlZCwgZXJyID0gcGFyc2VfanNvbiguZXZlbnRfbWVzc2FnZSlcbiAgICAgIGlmIGVyciA9PSBudWxsIHtcbiAgICAgICAgICAuZXZlbnRfbWVzc2FnZSA9IHBhcnNlZC5tc2dcbiAgICAgICAgICAubWV0YWRhdGEubGV2ZWwgPSBwYXJzZWQubGV2ZWxcbiAgICAgICAgICAubWV0YWRhdGEudGltZXN0YW1wID0gcGFyc2VkLnRpbWVcbiAgICAgICAgICAubWV0YWRhdGEuY29udGV4dFswXS5ob3N0ID0gcGFyc2VkLmhvc3RuYW1lXG4gICAgICAgICAgLm1ldGFkYXRhLmNvbnRleHRbMF0ucGlkID0gcGFyc2VkLnBpZFxuICAgICAgfVxuICAjIFBvc3RncmVzIGxvZ3Mgc29tZSBtZXNzYWdlcyB0byBzdGRlcnIgd2hpY2ggd2UgbWFwIHRvIHdhcm5pbmcgc2V2ZXJpdHkgbGV2ZWxcbiAgZGJfbG9nczpcbiAgICB0eXBlOiByZW1hcFxuICAgIGlucHV0czpcbiAgICAgIC0gcm91dGVyLmRiXG4gICAgc291cmNlOiB8LVxuICAgICAgLm1ldGFkYXRhLmhvc3QgPSBcImRiLWRlZmF1bHRcIlxuICAgICAgLm1ldGFkYXRhLnBhcnNlZC50aW1lc3RhbXAgPSAudGltZXN0YW1wXG5cbiAgICAgIHBhcnNlZCwgZXJyID0gcGFyc2VfcmVnZXgoLmV2ZW50X21lc3NhZ2UsIHInLiooP1A8bGV2ZWw+SU5GT3xOT1RJQ0V8V0FSTklOR3xFUlJPUnxMT0d8RkFUQUx8UEFOSUM/KTouKicsIG51bWVyaWNfZ3JvdXBzOiB0cnVlKVxuXG4gICAgICBpZiBlcnIgIT0gbnVsbCB8fCBwYXJzZWQgPT0gbnVsbCB7XG4gICAgICAgIC5tZXRhZGF0YS5wYXJzZWQuZXJyb3Jfc2V2ZXJpdHkgPSBcImluZm9cIlxuICAgICAgfVxuICAgICAgaWYgcGFyc2VkICE9IG51bGwge1xuICAgICAgIC5tZXRhZGF0YS5wYXJzZWQuZXJyb3Jfc2V2ZXJpdHkgPSBwYXJzZWQubGV2ZWxcbiAgICAgIH1cbiAgICAgIGlmIC5tZXRhZGF0YS5wYXJzZWQuZXJyb3Jfc2V2ZXJpdHkgPT0gXCJpbmZvXCIge1xuICAgICAgICAgIC5tZXRhZGF0YS5wYXJzZWQuZXJyb3Jfc2V2ZXJpdHkgPSBcImxvZ1wiXG4gICAgICB9XG4gICAgICAubWV0YWRhdGEucGFyc2VkLmVycm9yX3NldmVyaXR5ID0gdXBjYXNlISgubWV0YWRhdGEucGFyc2VkLmVycm9yX3NldmVyaXR5KVxuXG5zaW5rczpcbiAgbG9nZmxhcmVfYXV0aDpcbiAgICB0eXBlOiAnaHR0cCdcbiAgICBpbnB1dHM6XG4gICAgICAtIGF1dGhfbG9nc1xuICAgIGVuY29kaW5nOlxuICAgICAgY29kZWM6ICdqc29uJ1xuICAgIG1ldGhvZDogJ3Bvc3QnXG4gICAgcmVxdWVzdDpcbiAgICAgIHJldHJ5X21heF9kdXJhdGlvbl9zZWNzOiAxMFxuICAgIHVyaTogJ2h0dHA6Ly9hbmFseXRpY3M6NDAwMC9hcGkvbG9ncz9zb3VyY2VfbmFtZT1nb3RydWUubG9ncy5wcm9kJmFwaV9rZXk9JHtMT0dGTEFSRV9BUElfS0VZP0xPR0ZMQVJFX0FQSV9LRVkgaXMgcmVxdWlyZWR9J1xuICBsb2dmbGFyZV9yZWFsdGltZTpcbiAgICB0eXBlOiAnaHR0cCdcbiAgICBpbnB1dHM6XG4gICAgICAtIHJlYWx0aW1lX2xvZ3NcbiAgICBlbmNvZGluZzpcbiAgICAgIGNvZGVjOiAnanNvbidcbiAgICBtZXRob2Q6ICdwb3N0J1xuICAgIHJlcXVlc3Q6XG4gICAgICByZXRyeV9tYXhfZHVyYXRpb25fc2VjczogMTBcbiAgICB1cmk6ICdodHRwOi8vYW5hbHl0aWNzOjQwMDAvYXBpL2xvZ3M/c291cmNlX25hbWU9cmVhbHRpbWUubG9ncy5wcm9kJmFwaV9rZXk9JHtMT0dGTEFSRV9BUElfS0VZP0xPR0ZMQVJFX0FQSV9LRVkgaXMgcmVxdWlyZWR9J1xuICBsb2dmbGFyZV9yZXN0OlxuICAgIHR5cGU6ICdodHRwJ1xuICAgIGlucHV0czpcbiAgICAgIC0gcmVzdF9sb2dzXG4gICAgZW5jb2Rpbmc6XG4gICAgICBjb2RlYzogJ2pzb24nXG4gICAgbWV0aG9kOiAncG9zdCdcbiAgICByZXF1ZXN0OlxuICAgICAgcmV0cnlfbWF4X2R1cmF0aW9uX3NlY3M6IDEwXG4gICAgdXJpOiAnaHR0cDovL2FuYWx5dGljczo0MDAwL2FwaS9sb2dzP3NvdXJjZV9uYW1lPXBvc3RnUkVTVC5sb2dzLnByb2QmYXBpX2tleT0ke0xPR0ZMQVJFX0FQSV9LRVk/TE9HRkxBUkVfQVBJX0tFWSBpcyByZXF1aXJlZH0nXG4gIGxvZ2ZsYXJlX2RiOlxuICAgIHR5cGU6ICdodHRwJ1xuICAgIGlucHV0czpcbiAgICAgIC0gZGJfbG9nc1xuICAgIGVuY29kaW5nOlxuICAgICAgY29kZWM6ICdqc29uJ1xuICAgIG1ldGhvZDogJ3Bvc3QnXG4gICAgcmVxdWVzdDpcbiAgICAgIHJldHJ5X21heF9kdXJhdGlvbl9zZWNzOiAxMFxuICAgICMgV2UgbXVzdCByb3V0ZSB0aGUgc2luayB0aHJvdWdoIGtvbmcgYmVjYXVzZSBpbmdlc3RpbmcgbG9ncyBiZWZvcmUgbG9nZmxhcmUgaXMgZnVsbHkgaW5pdGlhbGlzZWQgd2lsbFxuICAgICMgbGVhZCB0byBicm9rZW4gcXVlcmllcyBmcm9tIHN0dWRpby4gVGhpcyB3b3JrcyBieSB0aGUgYXNzdW1wdGlvbiB0aGF0IGNvbnRhaW5lcnMgYXJlIHN0YXJ0ZWQgaW4gdGhlXG4gICAgIyBmb2xsb3dpbmcgb3JkZXI6IHZlY3RvciA+IGRiID4gbG9nZmxhcmUgPiBrb25nXG4gICAgdXJpOiAnaHR0cDovL2tvbmc6ODAwMC9hbmFseXRpY3MvdjEvYXBpL2xvZ3M/c291cmNlX25hbWU9cG9zdGdyZXMubG9ncyZhcGlfa2V5PSR7TE9HRkxBUkVfQVBJX0tFWT9MT0dGTEFSRV9BUElfS0VZIGlzIHJlcXVpcmVkfSdcbiAgbG9nZmxhcmVfZnVuY3Rpb25zOlxuICAgIHR5cGU6ICdodHRwJ1xuICAgIGlucHV0czpcbiAgICAgIC0gcm91dGVyLmZ1bmN0aW9uc1xuICAgIGVuY29kaW5nOlxuICAgICAgY29kZWM6ICdqc29uJ1xuICAgIG1ldGhvZDogJ3Bvc3QnXG4gICAgcmVxdWVzdDpcbiAgICAgIHJldHJ5X21heF9kdXJhdGlvbl9zZWNzOiAxMFxuICAgIHVyaTogJ2h0dHA6Ly9hbmFseXRpY3M6NDAwMC9hcGkvbG9ncz9zb3VyY2VfbmFtZT1kZW5vLXJlbGF5LWxvZ3MmYXBpX2tleT0ke0xPR0ZMQVJFX0FQSV9LRVk/TE9HRkxBUkVfQVBJX0tFWSBpcyByZXF1aXJlZH0nXG4gIGxvZ2ZsYXJlX3N0b3JhZ2U6XG4gICAgdHlwZTogJ2h0dHAnXG4gICAgaW5wdXRzOlxuICAgICAgLSBzdG9yYWdlX2xvZ3NcbiAgICBlbmNvZGluZzpcbiAgICAgIGNvZGVjOiAnanNvbidcbiAgICBtZXRob2Q6ICdwb3N0J1xuICAgIHJlcXVlc3Q6XG4gICAgICByZXRyeV9tYXhfZHVyYXRpb25fc2VjczogMTBcbiAgICB1cmk6ICdodHRwOi8vYW5hbHl0aWNzOjQwMDAvYXBpL2xvZ3M/c291cmNlX25hbWU9c3RvcmFnZS5sb2dzLnByb2QuMiZhcGlfa2V5PSR7TE9HRkxBUkVfQVBJX0tFWT9MT0dGTEFSRV9BUElfS0VZIGlzIHJlcXVpcmVkfSdcbiAgbG9nZmxhcmVfa29uZzpcbiAgICB0eXBlOiAnaHR0cCdcbiAgICBpbnB1dHM6XG4gICAgICAtIGtvbmdfbG9nc1xuICAgICAgLSBrb25nX2VyclxuICAgIGVuY29kaW5nOlxuICAgICAgY29kZWM6ICdqc29uJ1xuICAgIG1ldGhvZDogJ3Bvc3QnXG4gICAgcmVxdWVzdDpcbiAgICAgIHJldHJ5X21heF9kdXJhdGlvbl9zZWNzOiAxMFxuICAgIHVyaTogJ2h0dHA6Ly9hbmFseXRpY3M6NDAwMC9hcGkvbG9ncz9zb3VyY2VfbmFtZT1jbG91ZGZsYXJlLmxvZ3MucHJvZCZhcGlfa2V5PSR7TE9HRkxBUkVfQVBJX0tFWT9MT0dGTEFSRV9BUElfS0VZIGlzIHJlcXVpcmVkfSdcblwiXCJcIlxuXG5bW2NvbmZpZy5tb3VudHNdXVxuZmlsZVBhdGggPSBcIi92b2x1bWVzL3Bvb2xlci9wb29sZXIuZXhzXCJcbmNvbnRlbnQgPSBcIlwiXCJ7Om9rLCBffSA9IEFwcGxpY2F0aW9uLmVuc3VyZV9hbGxfc3RhcnRlZCg6c3VwYXZpc29yKVxuXG57Om9rLCB2ZXJzaW9ufSA9XG4gIGNhc2UgU3VwYXZpc29yLlJlcG8ucXVlcnkhKFwic2VsZWN0IHZlcnNpb24oKVwiKSBkb1xuICAgICV7cm93czogW1t2ZXJdXX0gLT4gU3VwYXZpc29yLkhlbHBlcnMucGFyc2VfcGdfdmVyc2lvbih2ZXIpXG4gICAgXyAtPiBuaWxcbiAgZW5kXG5cbnBhcmFtcyA9ICV7XG4gIFwiZXh0ZXJuYWxfaWRcIiA9PiBTeXN0ZW0uZ2V0X2VudihcIlBPT0xFUl9URU5BTlRfSURcIiksXG4gIFwiZGJfaG9zdFwiID0+IFwiZGJcIixcbiAgXCJkYl9wb3J0XCIgPT4gU3lzdGVtLmdldF9lbnYoXCJQT1NUR1JFU19QT1JUXCIpLFxuICBcImRiX2RhdGFiYXNlXCIgPT4gU3lzdGVtLmdldF9lbnYoXCJQT1NUR1JFU19EQlwiKSxcbiAgXCJyZXF1aXJlX3VzZXJcIiA9PiBmYWxzZSxcbiAgXCJhdXRoX3F1ZXJ5XCIgPT4gXCJTRUxFQ1QgKiBGUk9NIHBnYm91bmNlci5nZXRfYXV0aCgkMSlcIixcbiAgXCJkZWZhdWx0X21heF9jbGllbnRzXCIgPT4gU3lzdGVtLmdldF9lbnYoXCJQT09MRVJfTUFYX0NMSUVOVF9DT05OXCIpLFxuICBcImRlZmF1bHRfcG9vbF9zaXplXCIgPT4gU3lzdGVtLmdldF9lbnYoXCJQT09MRVJfREVGQVVMVF9QT09MX1NJWkVcIiksXG4gIFwiZGVmYXVsdF9wYXJhbWV0ZXJfc3RhdHVzXCIgPT4gJXtcInNlcnZlcl92ZXJzaW9uXCIgPT4gdmVyc2lvbn0sXG4gIFwidXNlcnNcIiA9PiBbJXtcbiAgICBcImRiX3VzZXJcIiA9PiBcInBnYm91bmNlclwiLFxuICAgIFwiZGJfcGFzc3dvcmRcIiA9PiBTeXN0ZW0uZ2V0X2VudihcIlBPU1RHUkVTX1BBU1NXT1JEXCIpLFxuICAgIFwibW9kZV90eXBlXCIgPT4gU3lzdGVtLmdldF9lbnYoXCJQT09MRVJfUE9PTF9NT0RFXCIpLFxuICAgIFwicG9vbF9zaXplXCIgPT4gU3lzdGVtLmdldF9lbnYoXCJQT09MRVJfREVGQVVMVF9QT09MX1NJWkVcIiksXG4gICAgXCJpc19tYW5hZ2VyXCIgPT4gdHJ1ZVxuICB9XVxufVxuXG5pZiAhU3VwYXZpc29yLlRlbmFudHMuZ2V0X3RlbmFudF9ieV9leHRlcm5hbF9pZChwYXJhbXNbXCJleHRlcm5hbF9pZFwiXSkgZG9cbiAgezpvaywgX30gPSBTdXBhdmlzb3IuVGVuYW50cy5jcmVhdGVfdGVuYW50KHBhcmFtcylcbmVuZFxuXCJcIlwiXG4iCn0=
```

## Links

`database`,`firebase`,`postgres`

---

Version:`1.25.04 / dokploy < 0.22.5`

PostizPostiz is a modern, open-source platform for managing and publishing content across multiple channels.

PrometheusPrometheus is an open-source monitoring and alerting toolkit designed for reliability and scalability.

### On this page

ConfigurationBase64LinksTags