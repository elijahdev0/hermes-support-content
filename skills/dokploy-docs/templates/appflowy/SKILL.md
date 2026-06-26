---
title: "App Flowy | Dokploy"
source: "https://docs.dokploy.com/docs/templates/appflowy"
category: dokploy-docs
created: "2026-06-25T17:21:40.415Z"
---

App Flowy | Dokploy

# App Flowy

Copy as Markdown

AppFlowy is an open-source alternative to Notion. You are in charge of your data and customizations.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  nginx:
    restart: on-failure
    image: nginx
    volumes:
      - ../files/nginx/nginx.conf:/etc/nginx/nginx.conf

  minio:
    restart: on-failure
    image: minio/minio
    environment:
      - MINIO_BROWSER_REDIRECT_URL=${APPFLOWY_BASE_URL}/minio
      - MINIO_ROOT_USER=${APPFLOWY_S3_ACCESS_KEY:-minioadmin}
      - MINIO_ROOT_PASSWORD=${APPFLOWY_S3_SECRET_KEY:-minioadmin}
    command: server /data --console-address ":9001"
    volumes:
      - minio_data:/data

  postgres:
    restart: on-failure
    image: pgvector/pgvector:pg16
    environment:
      - POSTGRES_USER=${POSTGRES_USER:-postgres}
      - POSTGRES_DB=${POSTGRES_DB:-postgres}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD:-password}
      - POSTGRES_HOST=${POSTGRES_HOST:-postgres}
    healthcheck:
      test: ["CMD", "pg_isready", "-U", "${POSTGRES_USER}", "-d", "${POSTGRES_DB}"]
      interval: 5s
      timeout: 5s
      retries: 12
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./files/volumes/postgres/:/docker-entrypoint-initdb.d/

  redis:
    restart: on-failure
    image: redis

  gotrue:
    restart: on-failure
    image: appflowyinc/gotrue:${GOTRUE_VERSION:-latest}
    depends_on:
      postgres:
        condition: service_healthy
    healthcheck:
      test: ["CMD", "curl", "--fail", "http://127.0.0.1:9999/health"]
      interval: 5s
      timeout: 5s
      retries: 12
    environment:
      # Admin Configuration
      - GOTRUE_ADMIN_EMAIL=${GOTRUE_ADMIN_EMAIL}
      - GOTRUE_ADMIN_PASSWORD=${GOTRUE_ADMIN_PASSWORD}
      - GOTRUE_DISABLE_SIGNUP=${GOTRUE_DISABLE_SIGNUP:-false}

      # Site Configuration
      - GOTRUE_SITE_URL=appflowy-flutter://
      - GOTRUE_URI_ALLOW_LIST=${GOTRUE_URI_ALLOW_LIST:-**}
      - API_EXTERNAL_URL=${API_EXTERNAL_URL}

      # JWT Configuration
      - GOTRUE_JWT_SECRET=${GOTRUE_JWT_SECRET}
      - GOTRUE_JWT_EXP=${GOTRUE_JWT_EXP:-7200}
      - GOTRUE_JWT_ADMIN_GROUP_NAME=supabase_admin

      # Database Configuration
      - GOTRUE_DB_DRIVER=postgres
      - DATABASE_URL=${GOTRUE_DATABASE_URL}
      - PORT=9999

      # Email Configuration
      - GOTRUE_SMTP_HOST=${GOTRUE_SMTP_HOST}
      - GOTRUE_SMTP_PORT=${GOTRUE_SMTP_PORT}
      - GOTRUE_SMTP_USER=${GOTRUE_SMTP_USER}
      - GOTRUE_SMTP_PASS=${GOTRUE_SMTP_PASS}
      - GOTRUE_SMTP_ADMIN_EMAIL=${GOTRUE_SMTP_ADMIN_EMAIL}
      - GOTRUE_SMTP_MAX_FREQUENCY=${GOTRUE_SMTP_MAX_FREQUENCY:-1ns}
      - GOTRUE_RATE_LIMIT_EMAIL_SENT=${GOTRUE_RATE_LIMIT_EMAIL_SENT:-100}
      - GOTRUE_MAILER_AUTOCONFIRM=${GOTRUE_MAILER_AUTOCONFIRM:-true}

      # Email Templates
      - GOTRUE_MAILER_URLPATHS_CONFIRMATION=/gotrue/verify
      - GOTRUE_MAILER_URLPATHS_INVITE=/gotrue/verify
      - GOTRUE_MAILER_URLPATHS_RECOVERY=/gotrue/verify
      - GOTRUE_MAILER_URLPATHS_EMAIL_CHANGE=/gotrue/verify
      - GOTRUE_MAILER_TEMPLATES_MAGIC_LINK=${GOTRUE_MAILER_TEMPLATES_MAGIC_LINK}

      # OAuth Providers
      - GOTRUE_EXTERNAL_GOOGLE_ENABLED=${GOTRUE_EXTERNAL_GOOGLE_ENABLED:-false}
      - GOTRUE_EXTERNAL_GOOGLE_CLIENT_ID=${GOTRUE_EXTERNAL_GOOGLE_CLIENT_ID}
      - GOTRUE_EXTERNAL_GOOGLE_SECRET=${GOTRUE_EXTERNAL_GOOGLE_SECRET}
      - GOTRUE_EXTERNAL_GOOGLE_REDIRECT_URI=${GOTRUE_EXTERNAL_GOOGLE_REDIRECT_URI}

      - GOTRUE_EXTERNAL_GITHUB_ENABLED=${GOTRUE_EXTERNAL_GITHUB_ENABLED:-false}
      - GOTRUE_EXTERNAL_GITHUB_CLIENT_ID=${GOTRUE_EXTERNAL_GITHUB_CLIENT_ID}
      - GOTRUE_EXTERNAL_GITHUB_SECRET=${GOTRUE_EXTERNAL_GITHUB_SECRET}
      - GOTRUE_EXTERNAL_GITHUB_REDIRECT_URI=${GOTRUE_EXTERNAL_GITHUB_REDIRECT_URI}

      - GOTRUE_EXTERNAL_DISCORD_ENABLED=${GOTRUE_EXTERNAL_DISCORD_ENABLED:-false}
      - GOTRUE_EXTERNAL_DISCORD_CLIENT_ID=${GOTRUE_EXTERNAL_DISCORD_CLIENT_ID}
      - GOTRUE_EXTERNAL_DISCORD_SECRET=${GOTRUE_EXTERNAL_DISCORD_SECRET}
      - GOTRUE_EXTERNAL_DISCORD_REDIRECT_URI=${GOTRUE_EXTERNAL_DISCORD_REDIRECT_URI}

      # SAML Configuration
      - GOTRUE_SAML_ENABLED=${GOTRUE_SAML_ENABLED:-false}
      - GOTRUE_SAML_PRIVATE_KEY=${GOTRUE_SAML_PRIVATE_KEY}

  appflowy_cloud:
    restart: on-failure
    image: appflowyinc/appflowy_cloud:${APPFLOWY_CLOUD_VERSION:-latest}
    depends_on:
      gotrue:
        condition: service_healthy
    environment:
      # Core Configuration
      - RUST_LOG=${RUST_LOG:-info}
      - APPFLOWY_ENVIRONMENT=production
      - APPFLOWY_DATABASE_URL=${APPFLOWY_DATABASE_URL}
      - APPFLOWY_REDIS_URI=${APPFLOWY_REDIS_URI}
      - APPFLOWY_WEB_URL=${APPFLOWY_WEB_URL}

      # Authentication Configuration
      - APPFLOWY_GOTRUE_JWT_SECRET=${GOTRUE_JWT_SECRET}
      - APPFLOWY_GOTRUE_JWT_EXP=${GOTRUE_JWT_EXP:-7200}
      - APPFLOWY_GOTRUE_BASE_URL=${APPFLOWY_GOTRUE_BASE_URL}

      # File Storage Configuration
      - APPFLOWY_S3_CREATE_BUCKET=${APPFLOWY_S3_CREATE_BUCKET:-true}
      - APPFLOWY_S3_USE_MINIO=${APPFLOWY_S3_USE_MINIO:-true}
      - APPFLOWY_S3_MINIO_URL=${APPFLOWY_S3_MINIO_URL}
      - APPFLOWY_S3_ACCESS_KEY=${APPFLOWY_S3_ACCESS_KEY}
      - APPFLOWY_S3_SECRET_KEY=${APPFLOWY_S3_SECRET_KEY}
      - APPFLOWY_S3_BUCKET=${APPFLOWY_S3_BUCKET:-appflowy}
      - APPFLOWY_S3_REGION=${APPFLOWY_S3_REGION:-us-east-1}
      - APPFLOWY_S3_PRESIGNED_URL_ENDPOINT=${APPFLOWY_S3_PRESIGNED_URL_ENDPOINT}

      # Email Configuration
      - APPFLOWY_MAILER_SMTP_HOST=${APPFLOWY_MAILER_SMTP_HOST}
      - APPFLOWY_MAILER_SMTP_PORT=${APPFLOWY_MAILER_SMTP_PORT}
      - APPFLOWY_MAILER_SMTP_USERNAME=${APPFLOWY_MAILER_SMTP_USERNAME}
      - APPFLOWY_MAILER_SMTP_EMAIL=${APPFLOWY_MAILER_SMTP_EMAIL}
      - APPFLOWY_MAILER_SMTP_PASSWORD=${APPFLOWY_MAILER_SMTP_PASSWORD}
      - APPFLOWY_MAILER_SMTP_TLS_KIND=${APPFLOWY_MAILER_SMTP_TLS_KIND:-wrapper}

      # Access Control and Performance
      - APPFLOWY_ACCESS_CONTROL=${APPFLOWY_ACCESS_CONTROL:-true}
      - APPFLOWY_DATABASE_MAX_CONNECTIONS=${APPFLOWY_DATABASE_MAX_CONNECTIONS:-40}
      - APPFLOWY_WEBSOCKET_MAILBOX_SIZE=${APPFLOWY_WEBSOCKET_MAILBOX_SIZE:-6000}

      # AI Configuration
      - AI_SERVER_HOST=${AI_SERVER_HOST:-ai}
      - AI_SERVER_PORT=${AI_SERVER_PORT:-5001}
      - AI_OPENAI_API_KEY=${AI_OPENAI_API_KEY}

  admin_frontend:
    restart: on-failure
    image: appflowyinc/admin_frontend:${APPFLOWY_ADMIN_FRONTEND_VERSION:-latest}
    depends_on:
      gotrue:
        condition: service_healthy
      appflowy_cloud:
        condition: service_started
    environment:
      - RUST_LOG=${RUST_LOG:-info}
      - ADMIN_FRONTEND_REDIS_URL=${ADMIN_FRONTEND_REDIS_URL}
      - ADMIN_FRONTEND_GOTRUE_URL=${ADMIN_FRONTEND_GOTRUE_URL}
      - ADMIN_FRONTEND_APPFLOWY_CLOUD_URL=${ADMIN_FRONTEND_APPFLOWY_CLOUD_URL}
      - ADMIN_FRONTEND_PATH_PREFIX=${ADMIN_FRONTEND_PATH_PREFIX:-/console}

  ai:
    restart: on-failure
    image: appflowyinc/appflowy_ai:${APPFLOWY_AI_VERSION:-latest}
    depends_on:
      postgres:
        condition: service_healthy
      appflowy_cloud:
        condition: service_started
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:5001/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
    environment:
      # Core AI Configuration
      - AI_SERVER_PORT=${AI_SERVER_PORT:-5001}
      - OPENAI_API_KEY=${AI_OPENAI_API_KEY}
      - DEFAULT_AI_MODEL=${DEFAULT_AI_MODEL:-gpt-4o-mini}
      - DEFAULT_AI_COMPLETION_MODEL=${DEFAULT_AI_COMPLETION_MODEL:-gpt-4o-mini}

      # Azure OpenAI (optional)
      - AZURE_OPENAI_API_KEY=${AZURE_OPENAI_API_KEY}
      - AZURE_OPENAI_ENDPOINT=${AZURE_OPENAI_ENDPOINT}
      - AZURE_OPENAI_API_VERSION=${AZURE_OPENAI_API_VERSION}

      # Database and Cache
      - AI_DATABASE_URL=${APPFLOWY_DATABASE_URL}
      - AI_REDIS_URL=${APPFLOWY_REDIS_URI}

      # File Storage for AI
      - APPFLOWY_S3_ACCESS_KEY=${APPFLOWY_S3_ACCESS_KEY}
      - APPFLOWY_S3_SECRET_KEY=${APPFLOWY_S3_SECRET_KEY}
      - APPFLOWY_S3_BUCKET=${APPFLOWY_S3_BUCKET:-appflowy}
      - APPFLOWY_S3_REGION=${APPFLOWY_S3_REGION:-us-east-1}
      - AI_USE_MINIO=${APPFLOWY_S3_USE_MINIO:-true}
      - AI_MINIO_URL=${APPFLOWY_S3_MINIO_URL}

      # Integration
      - AI_APPFLOWY_HOST=${APPFLOWY_BASE_URL}
      - APPFLOWY_GOTRUE_JWT_SECRET=${GOTRUE_JWT_SECRET}

  appflowy_worker:
    restart: on-failure
    image: appflowyinc/appflowy_worker:${APPFLOWY_WORKER_VERSION:-latest}
    depends_on:
      postgres:
        condition: service_healthy
    environment:
      # Core Configuration
      - RUST_LOG=${RUST_LOG:-info}
      - APPFLOWY_ENVIRONMENT=production
      - APPFLOWY_WORKER_REDIS_URL=${APPFLOWY_WORKER_REDIS_URL}
      - APPFLOWY_WORKER_ENVIRONMENT=production
      - APPFLOWY_WORKER_DATABASE_URL=${APPFLOWY_WORKER_DATABASE_URL}
      - APPFLOWY_WORKER_DATABASE_NAME=${APPFLOWY_WORKER_DATABASE_NAME}
      - APPFLOWY_WORKER_IMPORT_TICK_INTERVAL=${APPFLOWY_WORKER_IMPORT_TICK_INTERVAL:-30}

      # File Storage Configuration
      - APPFLOWY_S3_USE_MINIO=${APPFLOWY_S3_USE_MINIO:-true}
      - APPFLOWY_S3_MINIO_URL=${APPFLOWY_S3_MINIO_URL}
      - APPFLOWY_S3_ACCESS_KEY=${APPFLOWY_S3_ACCESS_KEY}
      - APPFLOWY_S3_SECRET_KEY=${APPFLOWY_S3_SECRET_KEY}
      - APPFLOWY_S3_BUCKET=${APPFLOWY_S3_BUCKET:-appflowy}
      - APPFLOWY_S3_REGION=${APPFLOWY_S3_REGION:-us-east-1}

      # Email Configuration
      - APPFLOWY_MAILER_SMTP_HOST=${APPFLOWY_MAILER_SMTP_HOST}
      - APPFLOWY_MAILER_SMTP_PORT=${APPFLOWY_MAILER_SMTP_PORT}
      - APPFLOWY_MAILER_SMTP_USERNAME=${APPFLOWY_MAILER_SMTP_USERNAME}
      - APPFLOWY_MAILER_SMTP_EMAIL=${APPFLOWY_MAILER_SMTP_EMAIL}
      - APPFLOWY_MAILER_SMTP_PASSWORD=${APPFLOWY_MAILER_SMTP_PASSWORD}
      - APPFLOWY_MAILER_SMTP_TLS_KIND=${APPFLOWY_MAILER_SMTP_TLS_KIND:-wrapper}

  appflowy_web:
    restart: on-failure
    image: appflowyinc/appflowy_web:${APPFLOWY_WEB_VERSION:-latest}
    depends_on:
      - appflowy_cloud
    environment:
      - AF_BASE_URL=${APPFLOWY_BASE_URL}
      - AF_GOTRUE_URL=${APPFLOWY_BASE_URL}/gotrue
      - AF_WS_V2_URL=${APPFLOWY_WEBSOCKET_BASE_URL}

volumes:
  postgres_data:
  minio_data:
```

```
[variables]
main_domain = "${domain}"

[config]
env = [
  # =============================================================================
  # 🌐 CORE DOMAIN CONFIGURATION
  # =============================================================================
  "FQDN=${main_domain}",
  "SCHEME=https",
  "WS_SCHEME=wss",
  "APPFLOWY_BASE_URL=https://${main_domain}",
  "APPFLOWY_WEBSOCKET_BASE_URL=wss://${main_domain}/ws/v2",
  "APPFLOWY_WEB_URL=https://${main_domain}",
  "API_EXTERNAL_URL=https://${main_domain}/gotrue",
  "TZ=UTC",

  # Admin Configuration
  "GOTRUE_ADMIN_EMAIL=${email}",
  "GOTRUE_ADMIN_PASSWORD=${password:16}",
  "GOTRUE_DISABLE_SIGNUP=false",

  # =============================================================================
  # 🗄️ DATABASE & CACHE CONFIGURATION
  # =============================================================================
  "POSTGRES_HOST=postgres",
  "POSTGRES_USER=appflowy",
  "POSTGRES_PASSWORD=${password:64}",
  "POSTGRES_PORT=5432",
  "POSTGRES_DB=appflowy",
  "REDIS_HOST=redis",
  "REDIS_PORT=6379",

  # =============================================================================
  # 🔐 GOTRUE AUTHENTICATION CONFIGURATION
  # =============================================================================

  # JWT Configuration
  "GOTRUE_JWT_SECRET=${password:64}",
  "GOTRUE_JWT_EXP=7200",
  "GOTRUE_JWT_ADMIN_GROUP_NAME=supabase_admin",

  # Database Configuration
  "GOTRUE_DB_DRIVER=postgres",
  "GOTRUE_DATABASE_URL=postgres://appflowy:${POSTGRES_PASSWORD}@postgres:5432/appflowy?search_path=auth",
  "PORT=9999",

  # Site Configuration
  "GOTRUE_SITE_URL=appflowy-flutter://",
  "GOTRUE_URI_ALLOW_LIST=**",

  # Email Configuration (SMTP - Configure for production)
  "GOTRUE_SMTP_HOST=",
  "GOTRUE_SMTP_PORT=465",
  "GOTRUE_SMTP_USER=",
  "GOTRUE_SMTP_PASS=",
  "GOTRUE_SMTP_ADMIN_EMAIL=${GOTRUE_ADMIN_EMAIL}",
  "GOTRUE_SMTP_MAX_FREQUENCY=1ns",
  "GOTRUE_RATE_LIMIT_EMAIL_SENT=100",
  "GOTRUE_MAILER_AUTOCONFIRM=true",

  # Email Templates
  "GOTRUE_MAILER_URLPATHS_CONFIRMATION=/gotrue/verify",
  "GOTRUE_MAILER_URLPATHS_INVITE=/gotrue/verify",
  "GOTRUE_MAILER_URLPATHS_RECOVERY=/gotrue/verify",
  "GOTRUE_MAILER_URLPATHS_EMAIL_CHANGE=/gotrue/verify",
  "GOTRUE_MAILER_TEMPLATES_MAGIC_LINK=",

  # OAuth Providers (Configure as needed)
  "GOTRUE_EXTERNAL_GOOGLE_ENABLED=false",
  "GOTRUE_EXTERNAL_GOOGLE_CLIENT_ID=",
  "GOTRUE_EXTERNAL_GOOGLE_SECRET=",
  "GOTRUE_EXTERNAL_GOOGLE_REDIRECT_URI=https://${main_domain}/gotrue/callback",

  "GOTRUE_EXTERNAL_GITHUB_ENABLED=false",
  "GOTRUE_EXTERNAL_GITHUB_CLIENT_ID=",
  "GOTRUE_EXTERNAL_GITHUB_SECRET=",
  "GOTRUE_EXTERNAL_GITHUB_REDIRECT_URI=https://${main_domain}/gotrue/callback",

  "GOTRUE_EXTERNAL_DISCORD_ENABLED=false",
  "GOTRUE_EXTERNAL_DISCORD_CLIENT_ID=",
  "GOTRUE_EXTERNAL_DISCORD_SECRET=",
  "GOTRUE_EXTERNAL_DISCORD_REDIRECT_URI=https://${main_domain}/gotrue/callback",

  # SAML Configuration
  "GOTRUE_SAML_ENABLED=false",
  "GOTRUE_SAML_PRIVATE_KEY=",

  # =============================================================================
  # ☁️ APPFLOWY CLOUD SERVICE CONFIGURATION
  # =============================================================================
  # Core Configuration
  "RUST_LOG=info",
  "APPFLOWY_ENVIRONMENT=production",
  "APPFLOWY_DATABASE_URL=postgres://appflowy:${POSTGRES_PASSWORD}@postgres:5432/appflowy",
  "APPFLOWY_REDIS_URI=redis://redis:6379",

  # Authentication Integration
  "APPFLOWY_GOTRUE_JWT_SECRET=${GOTRUE_JWT_SECRET}",
  "APPFLOWY_GOTRUE_JWT_EXP=7200",
  "APPFLOWY_GOTRUE_BASE_URL=http://gotrue:9999",

  # Access Control and Performance
  "APPFLOWY_ACCESS_CONTROL=true",
  "APPFLOWY_DATABASE_MAX_CONNECTIONS=40",
  "APPFLOWY_WEBSOCKET_MAILBOX_SIZE=6000",

  # Email Configuration (SMTP)
  "APPFLOWY_MAILER_SMTP_HOST=",
  "APPFLOWY_MAILER_SMTP_PORT=465",
  "APPFLOWY_MAILER_SMTP_USERNAME=",
  "APPFLOWY_MAILER_SMTP_EMAIL=",
  "APPFLOWY_MAILER_SMTP_PASSWORD=",
  "APPFLOWY_MAILER_SMTP_TLS_KIND=wrapper",

  # =============================================================================
  # 💾 FILE STORAGE CONFIGURATION (MinIO/S3)
  # =============================================================================
  # MinIO Configuration
  "MINIO_HOST=minio",
  "MINIO_PORT=9000",
  "APPFLOWY_S3_USE_MINIO=true",
  "APPFLOWY_S3_CREATE_BUCKET=true",
  "APPFLOWY_S3_MINIO_URL=http://minio:9000",

  # Storage Credentials
  "APPFLOWY_S3_ACCESS_KEY=${password:16}",
  "APPFLOWY_S3_SECRET_KEY=${password:32}",

  # Storage Configuration
  "APPFLOWY_S3_BUCKET=appflowy",
  "APPFLOWY_S3_REGION=us-east-1",
  "APPFLOWY_S3_PRESIGNED_URL_ENDPOINT=https://${main_domain}/minio-api",

  # AWS S3 Configuration (Alternative to MinIO)
  # "APPFLOWY_S3_USE_MINIO=false",
  # "APPFLOWY_S3_REGION=us-east-1",

  # =============================================================================
  # 🎛️ ADMIN FRONTEND CONFIGURATION
  # =============================================================================
  "ADMIN_FRONTEND_REDIS_URL=redis://redis:6379",
  "ADMIN_FRONTEND_GOTRUE_URL=http://gotrue:9999",
  "ADMIN_FRONTEND_APPFLOWY_CLOUD_URL=http://appflowy_cloud:8000",
  "ADMIN_FRONTEND_PATH_PREFIX=/console",

  # =============================================================================
  # 🤖 AI FEATURES CONFIGURATION (Optional)
  # =============================================================================
  # OpenAI Configuration
  "AI_OPENAI_API_KEY=",
  "DEFAULT_AI_MODEL=gpt-4o-mini",
  "DEFAULT_AI_COMPLETION_MODEL=gpt-4o-mini",

  # Azure OpenAI (Alternative)
  "AZURE_OPENAI_API_KEY=",
  "AZURE_OPENAI_ENDPOINT=",
  "AZURE_OPENAI_API_VERSION=",

  # AI Service Configuration
  "AI_SERVER_HOST=ai",
  "AI_SERVER_PORT=5001",
  "AI_DATABASE_URL=postgresql+psycopg://appflowy:${POSTGRES_PASSWORD}@postgres:5432/appflowy",
  "AI_REDIS_URL=redis://redis:6379",
  "AI_USE_MINIO=true",
  "AI_MINIO_URL=http://minio:9000",
  "AI_APPFLOWY_HOST=https://${main_domain}",

  # Embedding Configuration
  "APPFLOWY_EMBEDDING_CHUNK_SIZE=2000",
  "APPFLOWY_EMBEDDING_CHUNK_OVERLAP=200",

  # =============================================================================
  # ⚙️ WORKER SERVICES CONFIGURATION
  # =============================================================================
  # AppFlowy Worker
  "APPFLOWY_WORKER_REDIS_URL=redis://redis:6379",
  "APPFLOWY_WORKER_ENVIRONMENT=production",
  "APPFLOWY_WORKER_DATABASE_URL=postgres://appflowy:${POSTGRES_PASSWORD}@postgres:5432/appflowy",
  "APPFLOWY_WORKER_DATABASE_NAME=appflowy",
  "APPFLOWY_WORKER_IMPORT_TICK_INTERVAL=30",

  # Indexer Configuration
  "APPFLOWY_INDEXER_ENABLED=true",
  "APPFLOWY_INDEXER_DATABASE_URL=postgres://appflowy:${POSTGRES_PASSWORD}@postgres:5432/appflowy",
  "APPFLOWY_INDEXER_REDIS_URL=redis://redis:6379",
  "APPFLOWY_INDEXER_EMBEDDING_BUFFER_SIZE=5000",

  # Collaboration Service
  "APPFLOWY_COLLABORATE_MULTI_THREAD=false",
  "APPFLOWY_COLLABORATE_REMOVE_BATCH_SIZE=100",

  # =============================================================================
  # 🌐 NGINX CONFIGURATION
  # =============================================================================
  "NGINX_PORT=80",
  "NGINX_TLS_PORT=443",

  # =============================================================================
  # 🛠️ VERSION TAGS (Easily Configurable)
  # =============================================================================
  "GOTRUE_VERSION=latest",
  "APPFLOWY_CLOUD_VERSION=latest",
  "APPFLOWY_ADMIN_FRONTEND_VERSION=latest",
  "APPFLOWY_AI_VERSION=latest",
  "APPFLOWY_WORKER_VERSION=latest",
  "APPFLOWY_WEB_VERSION=latest",
]

[[config.domains]]
serviceName = "nginx"
port = 80
host = "${main_domain}"

[[config.mounts]]
filePath = "/nginx/nginx.conf"
content = """# Minimal nginx configuration for AppFlowy-Cloud
# Self Hosted AppFlowy Cloud user should alter this file to suit their needs,
# or use the appflowy.site.conf in external_proxy_config/nginx if they are using
# an external proxy.

events {
    worker_connections 1024;
}

http {
    # docker dns resolver
    resolver 127.0.0.11 valid=10s;
    #error_log /var/log/nginx/error.log debug;

    map $http_upgrade $connection_upgrade {
        default upgrade;
        '' close;
    }

    map $http_origin $cors_origin {
        # AppFlowy Web origin
        "~^http://localhost:3000$" $http_origin;
        default "null";
    }

    server {
        listen 8080;

        # https://github.com/nginxinc/nginx-prometheus-exporter
        location = /stub_status {
            stub_status;
        }
    }

    server {

        listen 80;
        client_max_body_size 10M;

        underscores_in_headers on;
        set $appflowy_cloud_backend "http://appflowy_cloud:8000";
        set $gotrue_backend "http://gotrue:9999";
        set $admin_frontend_backend "http://admin_frontend:3000";
        set $appflowy_web_backend "http://appflowy_web:80";
        set $minio_backend "http://minio:9001";
        set $minio_api_backend "http://minio:9000";
        # Host name for minio, used internally within docker compose
        set $minio_internal_host "minio:9000";
        set $pgadmin_backend "http://pgadmin:80";

        # GoTrue
        location /gotrue/ {
            if ($request_method = 'OPTIONS') {
                add_header 'Access-Control-Allow-Origin' $cors_origin always;
                add_header 'Access-Control-Allow-Credentials' 'true' always;
                add_header 'Access-Control-Allow-Headers' '*' always;
                add_header 'Access-Control-Allow-Methods' 'GET, POST, PUT, DELETE, PATCH, OPTIONS' always;
                add_header 'Access-Control-Max-Age' 3600 always;
                add_header 'Content-Type' 'text/plain charset=UTF-8' always;
                add_header 'Content-Length' 0 always;
                return 204;
            }

            proxy_pass $gotrue_backend;

            rewrite ^/gotrue(/.*)$ $1 break;

            # Allow headers like redirect_to to be handed over to the gotrue
            # for correct redirecting
            proxy_set_header Host $http_host;
            proxy_pass_request_headers on;
        }

        # WebSocket
        location /ws {
            proxy_pass $appflowy_cloud_backend;

            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "Upgrade";
            proxy_set_header Host $host;
            proxy_read_timeout 86400s;
        }

        location /api {
            proxy_pass $appflowy_cloud_backend;
            proxy_set_header X-Request-Id $request_id;
            proxy_set_header Host $http_host;

            # Set CORS headers for other requests
            if ($request_method = 'OPTIONS') {
                add_header 'Access-Control-Allow-Origin' $cors_origin always;
                add_header 'Access-Control-Allow-Methods' 'GET, POST, PUT, DELETE, PATCH, OPTIONS' always;
                add_header 'Access-Control-Allow-Headers' 'Content-Type, Authorization, Accept, Client-Version, Device-Id' always;
                add_header 'Access-Control-Max-Age' 3600 always;
                return 204;
            }

            add_header 'Access-Control-Allow-Origin' $cors_origin always;
            add_header 'Access-Control-Allow-Methods' 'GET, POST, PUT, DELETE, PATCH, OPTIONS' always;
            add_header 'Access-Control-Allow-Headers' 'Content-Type, Authorization, Accept, Client-Version, Device-Id' always;
            add_header 'Access-Control-Max-Age' 3600 always;

            location ~* ^/api/workspace/([a-zA-Z0-9_-]+)/publish$ {
                proxy_pass $appflowy_cloud_backend;
                proxy_request_buffering off;
                client_max_body_size 256M;
                if ($request_method = 'OPTIONS') {
                    add_header 'Access-Control-Allow-Origin' $cors_origin always;
                    add_header 'Access-Control-Allow-Methods' 'GET, POST, PUT, DELETE, PATCH, OPTIONS' always;
                    add_header 'Access-Control-Allow-Headers' 'Content-Type, Authorization, Accept, Client-Version, Device-Id' always;
                    add_header 'Access-Control-Max-Age' 3600 always;
                    return 204;
                }

                add_header 'Access-Control-Allow-Origin' $cors_origin always;
                add_header 'Access-Control-Allow-Methods' 'GET, POST, PUT, DELETE, PATCH, OPTIONS' always;
                add_header 'Access-Control-Allow-Headers' 'Content-Type, Authorization, Accept, Client-Version, Device-Id' always;
                add_header 'Access-Control-Max-Age' 3600 always;
            }

            # AppFlowy-Cloud
            location /api/chat {
                proxy_pass $appflowy_cloud_backend;

                proxy_http_version 1.1;
                proxy_set_header Connection "";
                chunked_transfer_encoding on;
                proxy_buffering off;
                proxy_cache off;

                proxy_read_timeout 600s;
                proxy_connect_timeout 600s;
                proxy_send_timeout 600s;
            }

            location /api/import {
                proxy_pass $appflowy_cloud_backend;

                # Set headers
                proxy_set_header X-Request-Id $request_id;
                proxy_set_header Host $http_host;

                # Handle CORS
                add_header 'Access-Control-Allow-Origin' $cors_origin always;
                add_header 'Access-Control-Allow-Methods' 'GET, POST, PUT, DELETE, PATCH, OPTIONS' always;
                add_header 'Access-Control-Allow-Headers' 'Content-Type, Authorization, Accept, Device-Id' always;
                add_header 'Access-Control-Max-Age' 3600 always;

                # Timeouts
                proxy_read_timeout 600s;
                proxy_connect_timeout 600s;
                proxy_send_timeout 600s;

                # Disable buffering for large file uploads
                proxy_request_buffering off;
                proxy_buffering off;
                proxy_cache off;
                client_max_body_size 2G;
            }
        }

        # Minio Web UI
        # Derive from: https://min.io/docs/minio/linux/integrations/setup-nginx-proxy-with-minio.html
        # Optional Module, comment this section if you did not deploy minio in docker-compose.yml
        # This endpoint is meant to be used for the MinIO Web UI, accessible via the admin portal
        location /minio/ {
            proxy_pass $minio_backend;

            rewrite ^/minio/(.*) /$1 break;
            proxy_set_header Host $http_host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_set_header X-NginX-Proxy true;

            ## This is necessary to pass the correct IP to be hashed
            real_ip_header X-Real-IP;

            proxy_connect_timeout 300s;

            ## To support websockets in MinIO versions released after January 2023
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";
            # Some environments may encounter CORS errors (Kubernetes + Nginx Ingress)
            # Uncomment the following line to set the Origin request to an empty string
            # proxy_set_header Origin '';

            chunked_transfer_encoding off;
        }

        # Optional Module, comment this section if you did not deploy minio in docker-compose.yml
        # This is used for presigned url, which is needs to be exposed to the AppFlowy client application.
        location /minio-api/ {
            proxy_pass $minio_api_backend;

            # Set the host to internal host because the presigned url was signed against the internal host
            proxy_set_header Host $minio_internal_host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;

            rewrite ^/minio-api/(.*) /$1 break;

            proxy_connect_timeout 300s;
            # Default is HTTP/1, keepalive is only enabled in HTTP/1.1
            proxy_http_version 1.1;
            proxy_set_header Connection "";
            chunked_transfer_encoding off;
        }

        # PgAdmin
        # Optional Module, comment this section if you did not deploy pgadmin in docker-compose.yml
        location /pgadmin/ {
            set $pgadmin pgadmin;
            proxy_pass $pgadmin_backend;

            proxy_set_header X-Script-Name /pgadmin;
            proxy_set_header X-Scheme $scheme;
            proxy_set_header Host $host;
            proxy_redirect off;
        }

        # Admin Frontend
        # Optional Module, comment this section if you did not deploy admin_frontend in docker-compose.yml
        location /console {
            proxy_pass $admin_frontend_backend;

            proxy_set_header X-Scheme $scheme;
            proxy_set_header Host $host;
        }

        # AppFlowy Web
        location / {
            proxy_pass $appflowy_web_backend;
            proxy_set_header X-Scheme $scheme;
            proxy_set_header Host $host;
        }
    }

}
"""
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBuZ2lueDpcbiAgICByZXN0YXJ0OiBvbi1mYWlsdXJlXG4gICAgaW1hZ2U6IG5naW54XG4gICAgdm9sdW1lczpcbiAgICAgIC0gLi4vZmlsZXMvbmdpbngvbmdpbnguY29uZjovZXRjL25naW54L25naW54LmNvbmZcblxuICBtaW5pbzpcbiAgICByZXN0YXJ0OiBvbi1mYWlsdXJlXG4gICAgaW1hZ2U6IG1pbmlvL21pbmlvXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIE1JTklPX0JST1dTRVJfUkVESVJFQ1RfVVJMPSR7QVBQRkxPV1lfQkFTRV9VUkx9L21pbmlvXG4gICAgICAtIE1JTklPX1JPT1RfVVNFUj0ke0FQUEZMT1dZX1MzX0FDQ0VTU19LRVk6LW1pbmlvYWRtaW59XG4gICAgICAtIE1JTklPX1JPT1RfUEFTU1dPUkQ9JHtBUFBGTE9XWV9TM19TRUNSRVRfS0VZOi1taW5pb2FkbWlufVxuICAgIGNvbW1hbmQ6IHNlcnZlciAvZGF0YSAtLWNvbnNvbGUtYWRkcmVzcyBcIjo5MDAxXCJcbiAgICB2b2x1bWVzOlxuICAgICAgLSBtaW5pb19kYXRhOi9kYXRhXG5cbiAgcG9zdGdyZXM6XG4gICAgcmVzdGFydDogb24tZmFpbHVyZVxuICAgIGltYWdlOiBwZ3ZlY3Rvci9wZ3ZlY3RvcjpwZzE2XG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIFBPU1RHUkVTX1VTRVI9JHtQT1NUR1JFU19VU0VSOi1wb3N0Z3Jlc31cbiAgICAgIC0gUE9TVEdSRVNfREI9JHtQT1NUR1JFU19EQjotcG9zdGdyZXN9XG4gICAgICAtIFBPU1RHUkVTX1BBU1NXT1JEPSR7UE9TVEdSRVNfUEFTU1dPUkQ6LXBhc3N3b3JkfVxuICAgICAgLSBQT1NUR1JFU19IT1NUPSR7UE9TVEdSRVNfSE9TVDotcG9zdGdyZXN9XG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OiBbXCJDTURcIiwgXCJwZ19pc3JlYWR5XCIsIFwiLVVcIiwgXCIke1BPU1RHUkVTX1VTRVJ9XCIsIFwiLWRcIiwgXCIke1BPU1RHUkVTX0RCfVwiXVxuICAgICAgaW50ZXJ2YWw6IDVzXG4gICAgICB0aW1lb3V0OiA1c1xuICAgICAgcmV0cmllczogMTJcbiAgICB2b2x1bWVzOlxuICAgICAgLSBwb3N0Z3Jlc19kYXRhOi92YXIvbGliL3Bvc3RncmVzcWwvZGF0YVxuICAgICAgLSAuL2ZpbGVzL3ZvbHVtZXMvcG9zdGdyZXMvOi9kb2NrZXItZW50cnlwb2ludC1pbml0ZGIuZC9cblxuICByZWRpczpcbiAgICByZXN0YXJ0OiBvbi1mYWlsdXJlXG4gICAgaW1hZ2U6IHJlZGlzXG5cbiAgZ290cnVlOlxuICAgIHJlc3RhcnQ6IG9uLWZhaWx1cmVcbiAgICBpbWFnZTogYXBwZmxvd3lpbmMvZ290cnVlOiR7R09UUlVFX1ZFUlNJT046LWxhdGVzdH1cbiAgICBkZXBlbmRzX29uOlxuICAgICAgcG9zdGdyZXM6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9oZWFsdGh5XG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OiBbXCJDTURcIiwgXCJjdXJsXCIsIFwiLS1mYWlsXCIsIFwiaHR0cDovLzEyNy4wLjAuMTo5OTk5L2hlYWx0aFwiXVxuICAgICAgaW50ZXJ2YWw6IDVzXG4gICAgICB0aW1lb3V0OiA1c1xuICAgICAgcmV0cmllczogMTJcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgICMgQWRtaW4gQ29uZmlndXJhdGlvblxuICAgICAgLSBHT1RSVUVfQURNSU5fRU1BSUw9JHtHT1RSVUVfQURNSU5fRU1BSUx9XG4gICAgICAtIEdPVFJVRV9BRE1JTl9QQVNTV09SRD0ke0dPVFJVRV9BRE1JTl9QQVNTV09SRH1cbiAgICAgIC0gR09UUlVFX0RJU0FCTEVfU0lHTlVQPSR7R09UUlVFX0RJU0FCTEVfU0lHTlVQOi1mYWxzZX1cbiAgICAgIFxuICAgICAgIyBTaXRlIENvbmZpZ3VyYXRpb25cbiAgICAgIC0gR09UUlVFX1NJVEVfVVJMPWFwcGZsb3d5LWZsdXR0ZXI6Ly9cbiAgICAgIC0gR09UUlVFX1VSSV9BTExPV19MSVNUPSR7R09UUlVFX1VSSV9BTExPV19MSVNUOi0qKn1cbiAgICAgIC0gQVBJX0VYVEVSTkFMX1VSTD0ke0FQSV9FWFRFUk5BTF9VUkx9XG4gICAgICBcbiAgICAgICMgSldUIENvbmZpZ3VyYXRpb25cbiAgICAgIC0gR09UUlVFX0pXVF9TRUNSRVQ9JHtHT1RSVUVfSldUX1NFQ1JFVH1cbiAgICAgIC0gR09UUlVFX0pXVF9FWFA9JHtHT1RSVUVfSldUX0VYUDotNzIwMH1cbiAgICAgIC0gR09UUlVFX0pXVF9BRE1JTl9HUk9VUF9OQU1FPXN1cGFiYXNlX2FkbWluXG4gICAgICBcbiAgICAgICMgRGF0YWJhc2UgQ29uZmlndXJhdGlvblxuICAgICAgLSBHT1RSVUVfREJfRFJJVkVSPXBvc3RncmVzXG4gICAgICAtIERBVEFCQVNFX1VSTD0ke0dPVFJVRV9EQVRBQkFTRV9VUkx9XG4gICAgICAtIFBPUlQ9OTk5OVxuICAgICAgXG4gICAgICAjIEVtYWlsIENvbmZpZ3VyYXRpb25cbiAgICAgIC0gR09UUlVFX1NNVFBfSE9TVD0ke0dPVFJVRV9TTVRQX0hPU1R9XG4gICAgICAtIEdPVFJVRV9TTVRQX1BPUlQ9JHtHT1RSVUVfU01UUF9QT1JUfVxuICAgICAgLSBHT1RSVUVfU01UUF9VU0VSPSR7R09UUlVFX1NNVFBfVVNFUn1cbiAgICAgIC0gR09UUlVFX1NNVFBfUEFTUz0ke0dPVFJVRV9TTVRQX1BBU1N9XG4gICAgICAtIEdPVFJVRV9TTVRQX0FETUlOX0VNQUlMPSR7R09UUlVFX1NNVFBfQURNSU5fRU1BSUx9XG4gICAgICAtIEdPVFJVRV9TTVRQX01BWF9GUkVRVUVOQ1k9JHtHT1RSVUVfU01UUF9NQVhfRlJFUVVFTkNZOi0xbnN9XG4gICAgICAtIEdPVFJVRV9SQVRFX0xJTUlUX0VNQUlMX1NFTlQ9JHtHT1RSVUVfUkFURV9MSU1JVF9FTUFJTF9TRU5UOi0xMDB9XG4gICAgICAtIEdPVFJVRV9NQUlMRVJfQVVUT0NPTkZJUk09JHtHT1RSVUVfTUFJTEVSX0FVVE9DT05GSVJNOi10cnVlfVxuICAgICAgXG4gICAgICAjIEVtYWlsIFRlbXBsYXRlc1xuICAgICAgLSBHT1RSVUVfTUFJTEVSX1VSTFBBVEhTX0NPTkZJUk1BVElPTj0vZ290cnVlL3ZlcmlmeVxuICAgICAgLSBHT1RSVUVfTUFJTEVSX1VSTFBBVEhTX0lOVklURT0vZ290cnVlL3ZlcmlmeVxuICAgICAgLSBHT1RSVUVfTUFJTEVSX1VSTFBBVEhTX1JFQ09WRVJZPS9nb3RydWUvdmVyaWZ5XG4gICAgICAtIEdPVFJVRV9NQUlMRVJfVVJMUEFUSFNfRU1BSUxfQ0hBTkdFPS9nb3RydWUvdmVyaWZ5XG4gICAgICAtIEdPVFJVRV9NQUlMRVJfVEVNUExBVEVTX01BR0lDX0xJTks9JHtHT1RSVUVfTUFJTEVSX1RFTVBMQVRFU19NQUdJQ19MSU5LfVxuICAgICAgXG4gICAgICAjIE9BdXRoIFByb3ZpZGVyc1xuICAgICAgLSBHT1RSVUVfRVhURVJOQUxfR09PR0xFX0VOQUJMRUQ9JHtHT1RSVUVfRVhURVJOQUxfR09PR0xFX0VOQUJMRUQ6LWZhbHNlfVxuICAgICAgLSBHT1RSVUVfRVhURVJOQUxfR09PR0xFX0NMSUVOVF9JRD0ke0dPVFJVRV9FWFRFUk5BTF9HT09HTEVfQ0xJRU5UX0lEfVxuICAgICAgLSBHT1RSVUVfRVhURVJOQUxfR09PR0xFX1NFQ1JFVD0ke0dPVFJVRV9FWFRFUk5BTF9HT09HTEVfU0VDUkVUfVxuICAgICAgLSBHT1RSVUVfRVhURVJOQUxfR09PR0xFX1JFRElSRUNUX1VSST0ke0dPVFJVRV9FWFRFUk5BTF9HT09HTEVfUkVESVJFQ1RfVVJJfVxuICAgICAgXG4gICAgICAtIEdPVFJVRV9FWFRFUk5BTF9HSVRIVUJfRU5BQkxFRD0ke0dPVFJVRV9FWFRFUk5BTF9HSVRIVUJfRU5BQkxFRDotZmFsc2V9XG4gICAgICAtIEdPVFJVRV9FWFRFUk5BTF9HSVRIVUJfQ0xJRU5UX0lEPSR7R09UUlVFX0VYVEVSTkFMX0dJVEhVQl9DTElFTlRfSUR9XG4gICAgICAtIEdPVFJVRV9FWFRFUk5BTF9HSVRIVUJfU0VDUkVUPSR7R09UUlVFX0VYVEVSTkFMX0dJVEhVQl9TRUNSRVR9XG4gICAgICAtIEdPVFJVRV9FWFRFUk5BTF9HSVRIVUJfUkVESVJFQ1RfVVJJPSR7R09UUlVFX0VYVEVSTkFMX0dJVEhVQl9SRURJUkVDVF9VUkl9XG4gICAgICBcbiAgICAgIC0gR09UUlVFX0VYVEVSTkFMX0RJU0NPUkRfRU5BQkxFRD0ke0dPVFJVRV9FWFRFUk5BTF9ESVNDT1JEX0VOQUJMRUQ6LWZhbHNlfVxuICAgICAgLSBHT1RSVUVfRVhURVJOQUxfRElTQ09SRF9DTElFTlRfSUQ9JHtHT1RSVUVfRVhURVJOQUxfRElTQ09SRF9DTElFTlRfSUR9XG4gICAgICAtIEdPVFJVRV9FWFRFUk5BTF9ESVNDT1JEX1NFQ1JFVD0ke0dPVFJVRV9FWFRFUk5BTF9ESVNDT1JEX1NFQ1JFVH1cbiAgICAgIC0gR09UUlVFX0VYVEVSTkFMX0RJU0NPUkRfUkVESVJFQ1RfVVJJPSR7R09UUlVFX0VYVEVSTkFMX0RJU0NPUkRfUkVESVJFQ1RfVVJJfVxuICAgICAgXG4gICAgICAjIFNBTUwgQ29uZmlndXJhdGlvblxuICAgICAgLSBHT1RSVUVfU0FNTF9FTkFCTEVEPSR7R09UUlVFX1NBTUxfRU5BQkxFRDotZmFsc2V9XG4gICAgICAtIEdPVFJVRV9TQU1MX1BSSVZBVEVfS0VZPSR7R09UUlVFX1NBTUxfUFJJVkFURV9LRVl9XG5cbiAgYXBwZmxvd3lfY2xvdWQ6XG4gICAgcmVzdGFydDogb24tZmFpbHVyZVxuICAgIGltYWdlOiBhcHBmbG93eWluYy9hcHBmbG93eV9jbG91ZDoke0FQUEZMT1dZX0NMT1VEX1ZFUlNJT046LWxhdGVzdH1cbiAgICBkZXBlbmRzX29uOlxuICAgICAgZ290cnVlOlxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2VfaGVhbHRoeVxuICAgIGVudmlyb25tZW50OlxuICAgICAgIyBDb3JlIENvbmZpZ3VyYXRpb25cbiAgICAgIC0gUlVTVF9MT0c9JHtSVVNUX0xPRzotaW5mb31cbiAgICAgIC0gQVBQRkxPV1lfRU5WSVJPTk1FTlQ9cHJvZHVjdGlvblxuICAgICAgLSBBUFBGTE9XWV9EQVRBQkFTRV9VUkw9JHtBUFBGTE9XWV9EQVRBQkFTRV9VUkx9XG4gICAgICAtIEFQUEZMT1dZX1JFRElTX1VSST0ke0FQUEZMT1dZX1JFRElTX1VSSX1cbiAgICAgIC0gQVBQRkxPV1lfV0VCX1VSTD0ke0FQUEZMT1dZX1dFQl9VUkx9XG4gICAgICBcbiAgICAgICMgQXV0aGVudGljYXRpb24gQ29uZmlndXJhdGlvblxuICAgICAgLSBBUFBGTE9XWV9HT1RSVUVfSldUX1NFQ1JFVD0ke0dPVFJVRV9KV1RfU0VDUkVUfVxuICAgICAgLSBBUFBGTE9XWV9HT1RSVUVfSldUX0VYUD0ke0dPVFJVRV9KV1RfRVhQOi03MjAwfVxuICAgICAgLSBBUFBGTE9XWV9HT1RSVUVfQkFTRV9VUkw9JHtBUFBGTE9XWV9HT1RSVUVfQkFTRV9VUkx9XG4gICAgICBcbiAgICAgICMgRmlsZSBTdG9yYWdlIENvbmZpZ3VyYXRpb25cbiAgICAgIC0gQVBQRkxPV1lfUzNfQ1JFQVRFX0JVQ0tFVD0ke0FQUEZMT1dZX1MzX0NSRUFURV9CVUNLRVQ6LXRydWV9XG4gICAgICAtIEFQUEZMT1dZX1MzX1VTRV9NSU5JTz0ke0FQUEZMT1dZX1MzX1VTRV9NSU5JTzotdHJ1ZX1cbiAgICAgIC0gQVBQRkxPV1lfUzNfTUlOSU9fVVJMPSR7QVBQRkxPV1lfUzNfTUlOSU9fVVJMfVxuICAgICAgLSBBUFBGTE9XWV9TM19BQ0NFU1NfS0VZPSR7QVBQRkxPV1lfUzNfQUNDRVNTX0tFWX1cbiAgICAgIC0gQVBQRkxPV1lfUzNfU0VDUkVUX0tFWT0ke0FQUEZMT1dZX1MzX1NFQ1JFVF9LRVl9XG4gICAgICAtIEFQUEZMT1dZX1MzX0JVQ0tFVD0ke0FQUEZMT1dZX1MzX0JVQ0tFVDotYXBwZmxvd3l9XG4gICAgICAtIEFQUEZMT1dZX1MzX1JFR0lPTj0ke0FQUEZMT1dZX1MzX1JFR0lPTjotdXMtZWFzdC0xfVxuICAgICAgLSBBUFBGTE9XWV9TM19QUkVTSUdORURfVVJMX0VORFBPSU5UPSR7QVBQRkxPV1lfUzNfUFJFU0lHTkVEX1VSTF9FTkRQT0lOVH1cbiAgICAgIFxuICAgICAgIyBFbWFpbCBDb25maWd1cmF0aW9uXG4gICAgICAtIEFQUEZMT1dZX01BSUxFUl9TTVRQX0hPU1Q9JHtBUFBGTE9XWV9NQUlMRVJfU01UUF9IT1NUfVxuICAgICAgLSBBUFBGTE9XWV9NQUlMRVJfU01UUF9QT1JUPSR7QVBQRkxPV1lfTUFJTEVSX1NNVFBfUE9SVH1cbiAgICAgIC0gQVBQRkxPV1lfTUFJTEVSX1NNVFBfVVNFUk5BTUU9JHtBUFBGTE9XWV9NQUlMRVJfU01UUF9VU0VSTkFNRX1cbiAgICAgIC0gQVBQRkxPV1lfTUFJTEVSX1NNVFBfRU1BSUw9JHtBUFBGTE9XWV9NQUlMRVJfU01UUF9FTUFJTH1cbiAgICAgIC0gQVBQRkxPV1lfTUFJTEVSX1NNVFBfUEFTU1dPUkQ9JHtBUFBGTE9XWV9NQUlMRVJfU01UUF9QQVNTV09SRH1cbiAgICAgIC0gQVBQRkxPV1lfTUFJTEVSX1NNVFBfVExTX0tJTkQ9JHtBUFBGTE9XWV9NQUlMRVJfU01UUF9UTFNfS0lORDotd3JhcHBlcn1cbiAgICAgIFxuICAgICAgIyBBY2Nlc3MgQ29udHJvbCBhbmQgUGVyZm9ybWFuY2VcbiAgICAgIC0gQVBQRkxPV1lfQUNDRVNTX0NPTlRST0w9JHtBUFBGTE9XWV9BQ0NFU1NfQ09OVFJPTDotdHJ1ZX1cbiAgICAgIC0gQVBQRkxPV1lfREFUQUJBU0VfTUFYX0NPTk5FQ1RJT05TPSR7QVBQRkxPV1lfREFUQUJBU0VfTUFYX0NPTk5FQ1RJT05TOi00MH1cbiAgICAgIC0gQVBQRkxPV1lfV0VCU09DS0VUX01BSUxCT1hfU0laRT0ke0FQUEZMT1dZX1dFQlNPQ0tFVF9NQUlMQk9YX1NJWkU6LTYwMDB9XG4gICAgICBcbiAgICAgICMgQUkgQ29uZmlndXJhdGlvblxuICAgICAgLSBBSV9TRVJWRVJfSE9TVD0ke0FJX1NFUlZFUl9IT1NUOi1haX1cbiAgICAgIC0gQUlfU0VSVkVSX1BPUlQ9JHtBSV9TRVJWRVJfUE9SVDotNTAwMX1cbiAgICAgIC0gQUlfT1BFTkFJX0FQSV9LRVk9JHtBSV9PUEVOQUlfQVBJX0tFWX1cblxuICBhZG1pbl9mcm9udGVuZDpcbiAgICByZXN0YXJ0OiBvbi1mYWlsdXJlXG4gICAgaW1hZ2U6IGFwcGZsb3d5aW5jL2FkbWluX2Zyb250ZW5kOiR7QVBQRkxPV1lfQURNSU5fRlJPTlRFTkRfVkVSU0lPTjotbGF0ZXN0fVxuICAgIGRlcGVuZHNfb246XG4gICAgICBnb3RydWU6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9oZWFsdGh5XG4gICAgICBhcHBmbG93eV9jbG91ZDpcbiAgICAgICAgY29uZGl0aW9uOiBzZXJ2aWNlX3N0YXJ0ZWRcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gUlVTVF9MT0c9JHtSVVNUX0xPRzotaW5mb31cbiAgICAgIC0gQURNSU5fRlJPTlRFTkRfUkVESVNfVVJMPSR7QURNSU5fRlJPTlRFTkRfUkVESVNfVVJMfVxuICAgICAgLSBBRE1JTl9GUk9OVEVORF9HT1RSVUVfVVJMPSR7QURNSU5fRlJPTlRFTkRfR09UUlVFX1VSTH1cbiAgICAgIC0gQURNSU5fRlJPTlRFTkRfQVBQRkxPV1lfQ0xPVURfVVJMPSR7QURNSU5fRlJPTlRFTkRfQVBQRkxPV1lfQ0xPVURfVVJMfVxuICAgICAgLSBBRE1JTl9GUk9OVEVORF9QQVRIX1BSRUZJWD0ke0FETUlOX0ZST05URU5EX1BBVEhfUFJFRklYOi0vY29uc29sZX1cblxuICBhaTpcbiAgICByZXN0YXJ0OiBvbi1mYWlsdXJlXG4gICAgaW1hZ2U6IGFwcGZsb3d5aW5jL2FwcGZsb3d5X2FpOiR7QVBQRkxPV1lfQUlfVkVSU0lPTjotbGF0ZXN0fVxuICAgIGRlcGVuZHNfb246XG4gICAgICBwb3N0Z3JlczpcbiAgICAgICAgY29uZGl0aW9uOiBzZXJ2aWNlX2hlYWx0aHlcbiAgICAgIGFwcGZsb3d5X2Nsb3VkOlxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2Vfc3RhcnRlZFxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDogW1wiQ01EXCIsIFwiY3VybFwiLCBcIi1mXCIsIFwiaHR0cDovL2xvY2FsaG9zdDo1MDAxL2hlYWx0aFwiXVxuICAgICAgaW50ZXJ2YWw6IDMwc1xuICAgICAgdGltZW91dDogMTBzXG4gICAgICByZXRyaWVzOiAzXG4gICAgICBzdGFydF9wZXJpb2Q6IDQwc1xuICAgIGVudmlyb25tZW50OlxuICAgICAgIyBDb3JlIEFJIENvbmZpZ3VyYXRpb25cbiAgICAgIC0gQUlfU0VSVkVSX1BPUlQ9JHtBSV9TRVJWRVJfUE9SVDotNTAwMX1cbiAgICAgIC0gT1BFTkFJX0FQSV9LRVk9JHtBSV9PUEVOQUlfQVBJX0tFWX1cbiAgICAgIC0gREVGQVVMVF9BSV9NT0RFTD0ke0RFRkFVTFRfQUlfTU9ERUw6LWdwdC00by1taW5pfVxuICAgICAgLSBERUZBVUxUX0FJX0NPTVBMRVRJT05fTU9ERUw9JHtERUZBVUxUX0FJX0NPTVBMRVRJT05fTU9ERUw6LWdwdC00by1taW5pfVxuICAgICAgXG4gICAgICAjIEF6dXJlIE9wZW5BSSAob3B0aW9uYWwpXG4gICAgICAtIEFaVVJFX09QRU5BSV9BUElfS0VZPSR7QVpVUkVfT1BFTkFJX0FQSV9LRVl9XG4gICAgICAtIEFaVVJFX09QRU5BSV9FTkRQT0lOVD0ke0FaVVJFX09QRU5BSV9FTkRQT0lOVH1cbiAgICAgIC0gQVpVUkVfT1BFTkFJX0FQSV9WRVJTSU9OPSR7QVpVUkVfT1BFTkFJX0FQSV9WRVJTSU9OfVxuICAgICAgXG4gICAgICAjIERhdGFiYXNlIGFuZCBDYWNoZVxuICAgICAgLSBBSV9EQVRBQkFTRV9VUkw9JHtBUFBGTE9XWV9EQVRBQkFTRV9VUkx9XG4gICAgICAtIEFJX1JFRElTX1VSTD0ke0FQUEZMT1dZX1JFRElTX1VSSX1cbiAgICAgIFxuICAgICAgIyBGaWxlIFN0b3JhZ2UgZm9yIEFJXG4gICAgICAtIEFQUEZMT1dZX1MzX0FDQ0VTU19LRVk9JHtBUFBGTE9XWV9TM19BQ0NFU1NfS0VZfVxuICAgICAgLSBBUFBGTE9XWV9TM19TRUNSRVRfS0VZPSR7QVBQRkxPV1lfUzNfU0VDUkVUX0tFWX1cbiAgICAgIC0gQVBQRkxPV1lfUzNfQlVDS0VUPSR7QVBQRkxPV1lfUzNfQlVDS0VUOi1hcHBmbG93eX1cbiAgICAgIC0gQVBQRkxPV1lfUzNfUkVHSU9OPSR7QVBQRkxPV1lfUzNfUkVHSU9OOi11cy1lYXN0LTF9XG4gICAgICAtIEFJX1VTRV9NSU5JTz0ke0FQUEZMT1dZX1MzX1VTRV9NSU5JTzotdHJ1ZX1cbiAgICAgIC0gQUlfTUlOSU9fVVJMPSR7QVBQRkxPV1lfUzNfTUlOSU9fVVJMfVxuICAgICAgXG4gICAgICAjIEludGVncmF0aW9uXG4gICAgICAtIEFJX0FQUEZMT1dZX0hPU1Q9JHtBUFBGTE9XWV9CQVNFX1VSTH1cbiAgICAgIC0gQVBQRkxPV1lfR09UUlVFX0pXVF9TRUNSRVQ9JHtHT1RSVUVfSldUX1NFQ1JFVH1cblxuICBhcHBmbG93eV93b3JrZXI6XG4gICAgcmVzdGFydDogb24tZmFpbHVyZVxuICAgIGltYWdlOiBhcHBmbG93eWluYy9hcHBmbG93eV93b3JrZXI6JHtBUFBGTE9XWV9XT1JLRVJfVkVSU0lPTjotbGF0ZXN0fVxuICAgIGRlcGVuZHNfb246XG4gICAgICBwb3N0Z3JlczpcbiAgICAgICAgY29uZGl0aW9uOiBzZXJ2aWNlX2hlYWx0aHlcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgICMgQ29yZSBDb25maWd1cmF0aW9uXG4gICAgICAtIFJVU1RfTE9HPSR7UlVTVF9MT0c6LWluZm99XG4gICAgICAtIEFQUEZMT1dZX0VOVklST05NRU5UPXByb2R1Y3Rpb25cbiAgICAgIC0gQVBQRkxPV1lfV09SS0VSX1JFRElTX1VSTD0ke0FQUEZMT1dZX1dPUktFUl9SRURJU19VUkx9XG4gICAgICAtIEFQUEZMT1dZX1dPUktFUl9FTlZJUk9OTUVOVD1wcm9kdWN0aW9uXG4gICAgICAtIEFQUEZMT1dZX1dPUktFUl9EQVRBQkFTRV9VUkw9JHtBUFBGTE9XWV9XT1JLRVJfREFUQUJBU0VfVVJMfVxuICAgICAgLSBBUFBGTE9XWV9XT1JLRVJfREFUQUJBU0VfTkFNRT0ke0FQUEZMT1dZX1dPUktFUl9EQVRBQkFTRV9OQU1FfVxuICAgICAgLSBBUFBGTE9XWV9XT1JLRVJfSU1QT1JUX1RJQ0tfSU5URVJWQUw9JHtBUFBGTE9XWV9XT1JLRVJfSU1QT1JUX1RJQ0tfSU5URVJWQUw6LTMwfVxuICAgICAgXG4gICAgICAjIEZpbGUgU3RvcmFnZSBDb25maWd1cmF0aW9uXG4gICAgICAtIEFQUEZMT1dZX1MzX1VTRV9NSU5JTz0ke0FQUEZMT1dZX1MzX1VTRV9NSU5JTzotdHJ1ZX1cbiAgICAgIC0gQVBQRkxPV1lfUzNfTUlOSU9fVVJMPSR7QVBQRkxPV1lfUzNfTUlOSU9fVVJMfVxuICAgICAgLSBBUFBGTE9XWV9TM19BQ0NFU1NfS0VZPSR7QVBQRkxPV1lfUzNfQUNDRVNTX0tFWX1cbiAgICAgIC0gQVBQRkxPV1lfUzNfU0VDUkVUX0tFWT0ke0FQUEZMT1dZX1MzX1NFQ1JFVF9LRVl9XG4gICAgICAtIEFQUEZMT1dZX1MzX0JVQ0tFVD0ke0FQUEZMT1dZX1MzX0JVQ0tFVDotYXBwZmxvd3l9XG4gICAgICAtIEFQUEZMT1dZX1MzX1JFR0lPTj0ke0FQUEZMT1dZX1MzX1JFR0lPTjotdXMtZWFzdC0xfVxuICAgICAgXG4gICAgICAjIEVtYWlsIENvbmZpZ3VyYXRpb25cbiAgICAgIC0gQVBQRkxPV1lfTUFJTEVSX1NNVFBfSE9TVD0ke0FQUEZMT1dZX01BSUxFUl9TTVRQX0hPU1R9XG4gICAgICAtIEFQUEZMT1dZX01BSUxFUl9TTVRQX1BPUlQ9JHtBUFBGTE9XWV9NQUlMRVJfU01UUF9QT1JUfVxuICAgICAgLSBBUFBGTE9XWV9NQUlMRVJfU01UUF9VU0VSTkFNRT0ke0FQUEZMT1dZX01BSUxFUl9TTVRQX1VTRVJOQU1FfVxuICAgICAgLSBBUFBGTE9XWV9NQUlMRVJfU01UUF9FTUFJTD0ke0FQUEZMT1dZX01BSUxFUl9TTVRQX0VNQUlMfVxuICAgICAgLSBBUFBGTE9XWV9NQUlMRVJfU01UUF9QQVNTV09SRD0ke0FQUEZMT1dZX01BSUxFUl9TTVRQX1BBU1NXT1JEfVxuICAgICAgLSBBUFBGTE9XWV9NQUlMRVJfU01UUF9UTFNfS0lORD0ke0FQUEZMT1dZX01BSUxFUl9TTVRQX1RMU19LSU5EOi13cmFwcGVyfVxuXG4gIGFwcGZsb3d5X3dlYjpcbiAgICByZXN0YXJ0OiBvbi1mYWlsdXJlXG4gICAgaW1hZ2U6IGFwcGZsb3d5aW5jL2FwcGZsb3d5X3dlYjoke0FQUEZMT1dZX1dFQl9WRVJTSU9OOi1sYXRlc3R9XG4gICAgZGVwZW5kc19vbjpcbiAgICAgIC0gYXBwZmxvd3lfY2xvdWRcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gQUZfQkFTRV9VUkw9JHtBUFBGTE9XWV9CQVNFX1VSTH1cbiAgICAgIC0gQUZfR09UUlVFX1VSTD0ke0FQUEZMT1dZX0JBU0VfVVJMfS9nb3RydWVcbiAgICAgIC0gQUZfV1NfVjJfVVJMPSR7QVBQRkxPV1lfV0VCU09DS0VUX0JBU0VfVVJMfVxuXG52b2x1bWVzOlxuICBwb3N0Z3Jlc19kYXRhOlxuICBtaW5pb19kYXRhOlxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcblxuW2NvbmZpZ11cbmVudiA9IFtcbiAgIyA9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PVxuICAjIPCfjJAgQ09SRSBET01BSU4gQ09ORklHVVJBVElPTlxuICAjID09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09XG4gIFwiRlFETj0ke21haW5fZG9tYWlufVwiLFxuICBcIlNDSEVNRT1odHRwc1wiLFxuICBcIldTX1NDSEVNRT13c3NcIixcbiAgXCJBUFBGTE9XWV9CQVNFX1VSTD1odHRwczovLyR7bWFpbl9kb21haW59XCIsXG4gIFwiQVBQRkxPV1lfV0VCU09DS0VUX0JBU0VfVVJMPXdzczovLyR7bWFpbl9kb21haW59L3dzL3YyXCIsXG4gIFwiQVBQRkxPV1lfV0VCX1VSTD1odHRwczovLyR7bWFpbl9kb21haW59XCIsXG4gIFwiQVBJX0VYVEVSTkFMX1VSTD1odHRwczovLyR7bWFpbl9kb21haW59L2dvdHJ1ZVwiLFxuICBcIlRaPVVUQ1wiLFxuXG4gICMgQWRtaW4gQ29uZmlndXJhdGlvblxuICBcIkdPVFJVRV9BRE1JTl9FTUFJTD0ke2VtYWlsfVwiLFxuICBcIkdPVFJVRV9BRE1JTl9QQVNTV09SRD0ke3Bhc3N3b3JkOjE2fVwiLFxuICBcIkdPVFJVRV9ESVNBQkxFX1NJR05VUD1mYWxzZVwiLFxuXG4gICMgPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT1cbiAgIyDwn5eE77iPIERBVEFCQVNFICYgQ0FDSEUgQ09ORklHVVJBVElPTlxuICAjID09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09XG4gIFwiUE9TVEdSRVNfSE9TVD1wb3N0Z3Jlc1wiLFxuICBcIlBPU1RHUkVTX1VTRVI9YXBwZmxvd3lcIixcbiAgXCJQT1NUR1JFU19QQVNTV09SRD0ke3Bhc3N3b3JkOjY0fVwiLFxuICBcIlBPU1RHUkVTX1BPUlQ9NTQzMlwiLFxuICBcIlBPU1RHUkVTX0RCPWFwcGZsb3d5XCIsXG4gIFwiUkVESVNfSE9TVD1yZWRpc1wiLFxuICBcIlJFRElTX1BPUlQ9NjM3OVwiLFxuXG4gICMgPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT1cbiAgIyDwn5SQIEdPVFJVRSBBVVRIRU5USUNBVElPTiBDT05GSUdVUkFUSU9OXG4gICMgPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT1cblxuICAjIEpXVCBDb25maWd1cmF0aW9uXG4gIFwiR09UUlVFX0pXVF9TRUNSRVQ9JHtwYXNzd29yZDo2NH1cIixcbiAgXCJHT1RSVUVfSldUX0VYUD03MjAwXCIsXG4gIFwiR09UUlVFX0pXVF9BRE1JTl9HUk9VUF9OQU1FPXN1cGFiYXNlX2FkbWluXCIsXG5cbiAgIyBEYXRhYmFzZSBDb25maWd1cmF0aW9uXG4gIFwiR09UUlVFX0RCX0RSSVZFUj1wb3N0Z3Jlc1wiLFxuICBcIkdPVFJVRV9EQVRBQkFTRV9VUkw9cG9zdGdyZXM6Ly9hcHBmbG93eToke1BPU1RHUkVTX1BBU1NXT1JEfUBwb3N0Z3Jlczo1NDMyL2FwcGZsb3d5P3NlYXJjaF9wYXRoPWF1dGhcIixcbiAgXCJQT1JUPTk5OTlcIixcblxuICAjIFNpdGUgQ29uZmlndXJhdGlvblxuICBcIkdPVFJVRV9TSVRFX1VSTD1hcHBmbG93eS1mbHV0dGVyOi8vXCIsXG4gIFwiR09UUlVFX1VSSV9BTExPV19MSVNUPSoqXCIsXG5cbiAgIyBFbWFpbCBDb25maWd1cmF0aW9uIChTTVRQIC0gQ29uZmlndXJlIGZvciBwcm9kdWN0aW9uKVxuICBcIkdPVFJVRV9TTVRQX0hPU1Q9XCIsXG4gIFwiR09UUlVFX1NNVFBfUE9SVD00NjVcIixcbiAgXCJHT1RSVUVfU01UUF9VU0VSPVwiLFxuICBcIkdPVFJVRV9TTVRQX1BBU1M9XCIsXG4gIFwiR09UUlVFX1NNVFBfQURNSU5fRU1BSUw9JHtHT1RSVUVfQURNSU5fRU1BSUx9XCIsXG4gIFwiR09UUlVFX1NNVFBfTUFYX0ZSRVFVRU5DWT0xbnNcIixcbiAgXCJHT1RSVUVfUkFURV9MSU1JVF9FTUFJTF9TRU5UPTEwMFwiLFxuICBcIkdPVFJVRV9NQUlMRVJfQVVUT0NPTkZJUk09dHJ1ZVwiLFxuXG4gICMgRW1haWwgVGVtcGxhdGVzXG4gIFwiR09UUlVFX01BSUxFUl9VUkxQQVRIU19DT05GSVJNQVRJT049L2dvdHJ1ZS92ZXJpZnlcIixcbiAgXCJHT1RSVUVfTUFJTEVSX1VSTFBBVEhTX0lOVklURT0vZ290cnVlL3ZlcmlmeVwiLFxuICBcIkdPVFJVRV9NQUlMRVJfVVJMUEFUSFNfUkVDT1ZFUlk9L2dvdHJ1ZS92ZXJpZnlcIixcbiAgXCJHT1RSVUVfTUFJTEVSX1VSTFBBVEhTX0VNQUlMX0NIQU5HRT0vZ290cnVlL3ZlcmlmeVwiLFxuICBcIkdPVFJVRV9NQUlMRVJfVEVNUExBVEVTX01BR0lDX0xJTks9XCIsXG5cbiAgIyBPQXV0aCBQcm92aWRlcnMgKENvbmZpZ3VyZSBhcyBuZWVkZWQpXG4gIFwiR09UUlVFX0VYVEVSTkFMX0dPT0dMRV9FTkFCTEVEPWZhbHNlXCIsXG4gIFwiR09UUlVFX0VYVEVSTkFMX0dPT0dMRV9DTElFTlRfSUQ9XCIsXG4gIFwiR09UUlVFX0VYVEVSTkFMX0dPT0dMRV9TRUNSRVQ9XCIsXG4gIFwiR09UUlVFX0VYVEVSTkFMX0dPT0dMRV9SRURJUkVDVF9VUkk9aHR0cHM6Ly8ke21haW5fZG9tYWlufS9nb3RydWUvY2FsbGJhY2tcIixcblxuICBcIkdPVFJVRV9FWFRFUk5BTF9HSVRIVUJfRU5BQkxFRD1mYWxzZVwiLFxuICBcIkdPVFJVRV9FWFRFUk5BTF9HSVRIVUJfQ0xJRU5UX0lEPVwiLFxuICBcIkdPVFJVRV9FWFRFUk5BTF9HSVRIVUJfU0VDUkVUPVwiLFxuICBcIkdPVFJVRV9FWFRFUk5BTF9HSVRIVUJfUkVESVJFQ1RfVVJJPWh0dHBzOi8vJHttYWluX2RvbWFpbn0vZ290cnVlL2NhbGxiYWNrXCIsXG5cbiAgXCJHT1RSVUVfRVhURVJOQUxfRElTQ09SRF9FTkFCTEVEPWZhbHNlXCIsXG4gIFwiR09UUlVFX0VYVEVSTkFMX0RJU0NPUkRfQ0xJRU5UX0lEPVwiLFxuICBcIkdPVFJVRV9FWFRFUk5BTF9ESVNDT1JEX1NFQ1JFVD1cIixcbiAgXCJHT1RSVUVfRVhURVJOQUxfRElTQ09SRF9SRURJUkVDVF9VUkk9aHR0cHM6Ly8ke21haW5fZG9tYWlufS9nb3RydWUvY2FsbGJhY2tcIixcblxuICAjIFNBTUwgQ29uZmlndXJhdGlvblxuICBcIkdPVFJVRV9TQU1MX0VOQUJMRUQ9ZmFsc2VcIixcbiAgXCJHT1RSVUVfU0FNTF9QUklWQVRFX0tFWT1cIixcblxuICAjID09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09XG4gICMg4piB77iPIEFQUEZMT1dZIENMT1VEIFNFUlZJQ0UgQ09ORklHVVJBVElPTlxuICAjID09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09XG4gICMgQ29yZSBDb25maWd1cmF0aW9uXG4gIFwiUlVTVF9MT0c9aW5mb1wiLFxuICBcIkFQUEZMT1dZX0VOVklST05NRU5UPXByb2R1Y3Rpb25cIixcbiAgXCJBUFBGTE9XWV9EQVRBQkFTRV9VUkw9cG9zdGdyZXM6Ly9hcHBmbG93eToke1BPU1RHUkVTX1BBU1NXT1JEfUBwb3N0Z3Jlczo1NDMyL2FwcGZsb3d5XCIsXG4gIFwiQVBQRkxPV1lfUkVESVNfVVJJPXJlZGlzOi8vcmVkaXM6NjM3OVwiLFxuXG4gICMgQXV0aGVudGljYXRpb24gSW50ZWdyYXRpb25cbiAgXCJBUFBGTE9XWV9HT1RSVUVfSldUX1NFQ1JFVD0ke0dPVFJVRV9KV1RfU0VDUkVUfVwiLFxuICBcIkFQUEZMT1dZX0dPVFJVRV9KV1RfRVhQPTcyMDBcIixcbiAgXCJBUFBGTE9XWV9HT1RSVUVfQkFTRV9VUkw9aHR0cDovL2dvdHJ1ZTo5OTk5XCIsXG5cbiAgIyBBY2Nlc3MgQ29udHJvbCBhbmQgUGVyZm9ybWFuY2VcbiAgXCJBUFBGTE9XWV9BQ0NFU1NfQ09OVFJPTD10cnVlXCIsXG4gIFwiQVBQRkxPV1lfREFUQUJBU0VfTUFYX0NPTk5FQ1RJT05TPTQwXCIsXG4gIFwiQVBQRkxPV1lfV0VCU09DS0VUX01BSUxCT1hfU0laRT02MDAwXCIsXG5cbiAgIyBFbWFpbCBDb25maWd1cmF0aW9uIChTTVRQKVxuICBcIkFQUEZMT1dZX01BSUxFUl9TTVRQX0hPU1Q9XCIsXG4gIFwiQVBQRkxPV1lfTUFJTEVSX1NNVFBfUE9SVD00NjVcIixcbiAgXCJBUFBGTE9XWV9NQUlMRVJfU01UUF9VU0VSTkFNRT1cIixcbiAgXCJBUFBGTE9XWV9NQUlMRVJfU01UUF9FTUFJTD1cIixcbiAgXCJBUFBGTE9XWV9NQUlMRVJfU01UUF9QQVNTV09SRD1cIixcbiAgXCJBUFBGTE9XWV9NQUlMRVJfU01UUF9UTFNfS0lORD13cmFwcGVyXCIsXG5cbiAgIyA9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PVxuICAjIPCfkr4gRklMRSBTVE9SQUdFIENPTkZJR1VSQVRJT04gKE1pbklPL1MzKVxuICAjID09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09XG4gICMgTWluSU8gQ29uZmlndXJhdGlvblxuICBcIk1JTklPX0hPU1Q9bWluaW9cIixcbiAgXCJNSU5JT19QT1JUPTkwMDBcIixcbiAgXCJBUFBGTE9XWV9TM19VU0VfTUlOSU89dHJ1ZVwiLFxuICBcIkFQUEZMT1dZX1MzX0NSRUFURV9CVUNLRVQ9dHJ1ZVwiLFxuICBcIkFQUEZMT1dZX1MzX01JTklPX1VSTD1odHRwOi8vbWluaW86OTAwMFwiLFxuXG4gICMgU3RvcmFnZSBDcmVkZW50aWFsc1xuICBcIkFQUEZMT1dZX1MzX0FDQ0VTU19LRVk9JHtwYXNzd29yZDoxNn1cIixcbiAgXCJBUFBGTE9XWV9TM19TRUNSRVRfS0VZPSR7cGFzc3dvcmQ6MzJ9XCIsXG5cbiAgIyBTdG9yYWdlIENvbmZpZ3VyYXRpb25cbiAgXCJBUFBGTE9XWV9TM19CVUNLRVQ9YXBwZmxvd3lcIixcbiAgXCJBUFBGTE9XWV9TM19SRUdJT049dXMtZWFzdC0xXCIsXG4gIFwiQVBQRkxPV1lfUzNfUFJFU0lHTkVEX1VSTF9FTkRQT0lOVD1odHRwczovLyR7bWFpbl9kb21haW59L21pbmlvLWFwaVwiLFxuXG4gICMgQVdTIFMzIENvbmZpZ3VyYXRpb24gKEFsdGVybmF0aXZlIHRvIE1pbklPKVxuICAjIFwiQVBQRkxPV1lfUzNfVVNFX01JTklPPWZhbHNlXCIsXG4gICMgXCJBUFBGTE9XWV9TM19SRUdJT049dXMtZWFzdC0xXCIsXG5cbiAgIyA9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PVxuICAjIPCfjpvvuI8gQURNSU4gRlJPTlRFTkQgQ09ORklHVVJBVElPTlxuICAjID09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09XG4gIFwiQURNSU5fRlJPTlRFTkRfUkVESVNfVVJMPXJlZGlzOi8vcmVkaXM6NjM3OVwiLFxuICBcIkFETUlOX0ZST05URU5EX0dPVFJVRV9VUkw9aHR0cDovL2dvdHJ1ZTo5OTk5XCIsXG4gIFwiQURNSU5fRlJPTlRFTkRfQVBQRkxPV1lfQ0xPVURfVVJMPWh0dHA6Ly9hcHBmbG93eV9jbG91ZDo4MDAwXCIsXG4gIFwiQURNSU5fRlJPTlRFTkRfUEFUSF9QUkVGSVg9L2NvbnNvbGVcIixcblxuICAjID09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09XG4gICMg8J+kliBBSSBGRUFUVVJFUyBDT05GSUdVUkFUSU9OIChPcHRpb25hbClcbiAgIyA9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PVxuICAjIE9wZW5BSSBDb25maWd1cmF0aW9uXG4gIFwiQUlfT1BFTkFJX0FQSV9LRVk9XCIsXG4gIFwiREVGQVVMVF9BSV9NT0RFTD1ncHQtNG8tbWluaVwiLFxuICBcIkRFRkFVTFRfQUlfQ09NUExFVElPTl9NT0RFTD1ncHQtNG8tbWluaVwiLFxuXG4gICMgQXp1cmUgT3BlbkFJIChBbHRlcm5hdGl2ZSlcbiAgXCJBWlVSRV9PUEVOQUlfQVBJX0tFWT1cIixcbiAgXCJBWlVSRV9PUEVOQUlfRU5EUE9JTlQ9XCIsXG4gIFwiQVpVUkVfT1BFTkFJX0FQSV9WRVJTSU9OPVwiLFxuXG4gICMgQUkgU2VydmljZSBDb25maWd1cmF0aW9uXG4gIFwiQUlfU0VSVkVSX0hPU1Q9YWlcIixcbiAgXCJBSV9TRVJWRVJfUE9SVD01MDAxXCIsXG4gIFwiQUlfREFUQUJBU0VfVVJMPXBvc3RncmVzcWwrcHN5Y29wZzovL2FwcGZsb3d5OiR7UE9TVEdSRVNfUEFTU1dPUkR9QHBvc3RncmVzOjU0MzIvYXBwZmxvd3lcIixcbiAgXCJBSV9SRURJU19VUkw9cmVkaXM6Ly9yZWRpczo2Mzc5XCIsXG4gIFwiQUlfVVNFX01JTklPPXRydWVcIixcbiAgXCJBSV9NSU5JT19VUkw9aHR0cDovL21pbmlvOjkwMDBcIixcbiAgXCJBSV9BUFBGTE9XWV9IT1NUPWh0dHBzOi8vJHttYWluX2RvbWFpbn1cIixcblxuICAjIEVtYmVkZGluZyBDb25maWd1cmF0aW9uXG4gIFwiQVBQRkxPV1lfRU1CRURESU5HX0NIVU5LX1NJWkU9MjAwMFwiLFxuICBcIkFQUEZMT1dZX0VNQkVERElOR19DSFVOS19PVkVSTEFQPTIwMFwiLFxuXG4gICMgPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT1cbiAgIyDimpnvuI8gV09SS0VSIFNFUlZJQ0VTIENPTkZJR1VSQVRJT05cbiAgIyA9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PVxuICAjIEFwcEZsb3d5IFdvcmtlclxuICBcIkFQUEZMT1dZX1dPUktFUl9SRURJU19VUkw9cmVkaXM6Ly9yZWRpczo2Mzc5XCIsXG4gIFwiQVBQRkxPV1lfV09SS0VSX0VOVklST05NRU5UPXByb2R1Y3Rpb25cIixcbiAgXCJBUFBGTE9XWV9XT1JLRVJfREFUQUJBU0VfVVJMPXBvc3RncmVzOi8vYXBwZmxvd3k6JHtQT1NUR1JFU19QQVNTV09SRH1AcG9zdGdyZXM6NTQzMi9hcHBmbG93eVwiLFxuICBcIkFQUEZMT1dZX1dPUktFUl9EQVRBQkFTRV9OQU1FPWFwcGZsb3d5XCIsXG4gIFwiQVBQRkxPV1lfV09SS0VSX0lNUE9SVF9USUNLX0lOVEVSVkFMPTMwXCIsXG5cbiAgIyBJbmRleGVyIENvbmZpZ3VyYXRpb25cbiAgXCJBUFBGTE9XWV9JTkRFWEVSX0VOQUJMRUQ9dHJ1ZVwiLFxuICBcIkFQUEZMT1dZX0lOREVYRVJfREFUQUJBU0VfVVJMPXBvc3RncmVzOi8vYXBwZmxvd3k6JHtQT1NUR1JFU19QQVNTV09SRH1AcG9zdGdyZXM6NTQzMi9hcHBmbG93eVwiLFxuICBcIkFQUEZMT1dZX0lOREVYRVJfUkVESVNfVVJMPXJlZGlzOi8vcmVkaXM6NjM3OVwiLFxuICBcIkFQUEZMT1dZX0lOREVYRVJfRU1CRURESU5HX0JVRkZFUl9TSVpFPTUwMDBcIixcblxuICAjIENvbGxhYm9yYXRpb24gU2VydmljZVxuICBcIkFQUEZMT1dZX0NPTExBQk9SQVRFX01VTFRJX1RIUkVBRD1mYWxzZVwiLFxuICBcIkFQUEZMT1dZX0NPTExBQk9SQVRFX1JFTU9WRV9CQVRDSF9TSVpFPTEwMFwiLFxuXG4gICMgPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT1cbiAgIyDwn4yQIE5HSU5YIENPTkZJR1VSQVRJT05cbiAgIyA9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PVxuICBcIk5HSU5YX1BPUlQ9ODBcIixcbiAgXCJOR0lOWF9UTFNfUE9SVD00NDNcIixcblxuICAjID09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09XG4gICMg8J+boO+4jyBWRVJTSU9OIFRBR1MgKEVhc2lseSBDb25maWd1cmFibGUpXG4gICMgPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT1cbiAgXCJHT1RSVUVfVkVSU0lPTj1sYXRlc3RcIixcbiAgXCJBUFBGTE9XWV9DTE9VRF9WRVJTSU9OPWxhdGVzdFwiLFxuICBcIkFQUEZMT1dZX0FETUlOX0ZST05URU5EX1ZFUlNJT049bGF0ZXN0XCIsXG4gIFwiQVBQRkxPV1lfQUlfVkVSU0lPTj1sYXRlc3RcIixcbiAgXCJBUFBGTE9XWV9XT1JLRVJfVkVSU0lPTj1sYXRlc3RcIixcbiAgXCJBUFBGTE9XWV9XRUJfVkVSU0lPTj1sYXRlc3RcIixcbl1cblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwibmdpbnhcIlxucG9ydCA9IDgwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cblxuW1tjb25maWcubW91bnRzXV1cbmZpbGVQYXRoID0gXCIvbmdpbngvbmdpbnguY29uZlwiXG5jb250ZW50ID0gXCJcIlwiIyBNaW5pbWFsIG5naW54IGNvbmZpZ3VyYXRpb24gZm9yIEFwcEZsb3d5LUNsb3VkXG4jIFNlbGYgSG9zdGVkIEFwcEZsb3d5IENsb3VkIHVzZXIgc2hvdWxkIGFsdGVyIHRoaXMgZmlsZSB0byBzdWl0IHRoZWlyIG5lZWRzLFxuIyBvciB1c2UgdGhlIGFwcGZsb3d5LnNpdGUuY29uZiBpbiBleHRlcm5hbF9wcm94eV9jb25maWcvbmdpbnggaWYgdGhleSBhcmUgdXNpbmdcbiMgYW4gZXh0ZXJuYWwgcHJveHkuXG5cbmV2ZW50cyB7XG4gICAgd29ya2VyX2Nvbm5lY3Rpb25zIDEwMjQ7XG59XG5cbmh0dHAge1xuICAgICMgZG9ja2VyIGRucyByZXNvbHZlclxuICAgIHJlc29sdmVyIDEyNy4wLjAuMTEgdmFsaWQ9MTBzO1xuICAgICNlcnJvcl9sb2cgL3Zhci9sb2cvbmdpbngvZXJyb3IubG9nIGRlYnVnO1xuXG4gICAgbWFwICRodHRwX3VwZ3JhZGUgJGNvbm5lY3Rpb25fdXBncmFkZSB7XG4gICAgICAgIGRlZmF1bHQgdXBncmFkZTtcbiAgICAgICAgJycgY2xvc2U7XG4gICAgfVxuXG4gICAgbWFwICRodHRwX29yaWdpbiAkY29yc19vcmlnaW4ge1xuICAgICAgICAjIEFwcEZsb3d5IFdlYiBvcmlnaW5cbiAgICAgICAgXCJ+Xmh0dHA6Ly9sb2NhbGhvc3Q6MzAwMCRcIiAkaHR0cF9vcmlnaW47XG4gICAgICAgIGRlZmF1bHQgXCJudWxsXCI7XG4gICAgfVxuXG4gICAgc2VydmVyIHtcbiAgICAgICAgbGlzdGVuIDgwODA7XG5cbiAgICAgICAgIyBodHRwczovL2dpdGh1Yi5jb20vbmdpbnhpbmMvbmdpbngtcHJvbWV0aGV1cy1leHBvcnRlclxuICAgICAgICBsb2NhdGlvbiA9IC9zdHViX3N0YXR1cyB7XG4gICAgICAgICAgICBzdHViX3N0YXR1cztcbiAgICAgICAgfVxuICAgIH1cblxuXG4gICAgc2VydmVyIHtcblxuICAgICAgICBsaXN0ZW4gODA7XG4gICAgICAgIGNsaWVudF9tYXhfYm9keV9zaXplIDEwTTtcblxuICAgICAgICB1bmRlcnNjb3Jlc19pbl9oZWFkZXJzIG9uO1xuICAgICAgICBzZXQgJGFwcGZsb3d5X2Nsb3VkX2JhY2tlbmQgXCJodHRwOi8vYXBwZmxvd3lfY2xvdWQ6ODAwMFwiO1xuICAgICAgICBzZXQgJGdvdHJ1ZV9iYWNrZW5kIFwiaHR0cDovL2dvdHJ1ZTo5OTk5XCI7XG4gICAgICAgIHNldCAkYWRtaW5fZnJvbnRlbmRfYmFja2VuZCBcImh0dHA6Ly9hZG1pbl9mcm9udGVuZDozMDAwXCI7XG4gICAgICAgIHNldCAkYXBwZmxvd3lfd2ViX2JhY2tlbmQgXCJodHRwOi8vYXBwZmxvd3lfd2ViOjgwXCI7XG4gICAgICAgIHNldCAkbWluaW9fYmFja2VuZCBcImh0dHA6Ly9taW5pbzo5MDAxXCI7XG4gICAgICAgIHNldCAkbWluaW9fYXBpX2JhY2tlbmQgXCJodHRwOi8vbWluaW86OTAwMFwiO1xuICAgICAgICAjIEhvc3QgbmFtZSBmb3IgbWluaW8sIHVzZWQgaW50ZXJuYWxseSB3aXRoaW4gZG9ja2VyIGNvbXBvc2VcbiAgICAgICAgc2V0ICRtaW5pb19pbnRlcm5hbF9ob3N0IFwibWluaW86OTAwMFwiO1xuICAgICAgICBzZXQgJHBnYWRtaW5fYmFja2VuZCBcImh0dHA6Ly9wZ2FkbWluOjgwXCI7XG5cbiAgICAgICAgIyBHb1RydWVcbiAgICAgICAgbG9jYXRpb24gL2dvdHJ1ZS8ge1xuICAgICAgICAgICAgaWYgKCRyZXF1ZXN0X21ldGhvZCA9ICdPUFRJT05TJykge1xuICAgICAgICAgICAgICAgIGFkZF9oZWFkZXIgJ0FjY2Vzcy1Db250cm9sLUFsbG93LU9yaWdpbicgJGNvcnNfb3JpZ2luIGFsd2F5cztcbiAgICAgICAgICAgICAgICBhZGRfaGVhZGVyICdBY2Nlc3MtQ29udHJvbC1BbGxvdy1DcmVkZW50aWFscycgJ3RydWUnIGFsd2F5cztcbiAgICAgICAgICAgICAgICBhZGRfaGVhZGVyICdBY2Nlc3MtQ29udHJvbC1BbGxvdy1IZWFkZXJzJyAnKicgYWx3YXlzO1xuICAgICAgICAgICAgICAgIGFkZF9oZWFkZXIgJ0FjY2Vzcy1Db250cm9sLUFsbG93LU1ldGhvZHMnICdHRVQsIFBPU1QsIFBVVCwgREVMRVRFLCBQQVRDSCwgT1BUSU9OUycgYWx3YXlzO1xuICAgICAgICAgICAgICAgIGFkZF9oZWFkZXIgJ0FjY2Vzcy1Db250cm9sLU1heC1BZ2UnIDM2MDAgYWx3YXlzO1xuICAgICAgICAgICAgICAgIGFkZF9oZWFkZXIgJ0NvbnRlbnQtVHlwZScgJ3RleHQvcGxhaW4gY2hhcnNldD1VVEYtOCcgYWx3YXlzO1xuICAgICAgICAgICAgICAgIGFkZF9oZWFkZXIgJ0NvbnRlbnQtTGVuZ3RoJyAwIGFsd2F5cztcbiAgICAgICAgICAgICAgICByZXR1cm4gMjA0O1xuICAgICAgICAgICAgfVxuXG4gICAgICAgICAgICBwcm94eV9wYXNzICRnb3RydWVfYmFja2VuZDtcblxuICAgICAgICAgICAgcmV3cml0ZSBeL2dvdHJ1ZSgvLiopJCAkMSBicmVhaztcblxuICAgICAgICAgICAgIyBBbGxvdyBoZWFkZXJzIGxpa2UgcmVkaXJlY3RfdG8gdG8gYmUgaGFuZGVkIG92ZXIgdG8gdGhlIGdvdHJ1ZVxuICAgICAgICAgICAgIyBmb3IgY29ycmVjdCByZWRpcmVjdGluZ1xuICAgICAgICAgICAgcHJveHlfc2V0X2hlYWRlciBIb3N0ICRodHRwX2hvc3Q7XG4gICAgICAgICAgICBwcm94eV9wYXNzX3JlcXVlc3RfaGVhZGVycyBvbjtcbiAgICAgICAgfVxuXG4gICAgICAgICMgV2ViU29ja2V0XG4gICAgICAgIGxvY2F0aW9uIC93cyB7XG4gICAgICAgICAgICBwcm94eV9wYXNzICRhcHBmbG93eV9jbG91ZF9iYWNrZW5kO1xuXG4gICAgICAgICAgICBwcm94eV9odHRwX3ZlcnNpb24gMS4xO1xuICAgICAgICAgICAgcHJveHlfc2V0X2hlYWRlciBVcGdyYWRlICRodHRwX3VwZ3JhZGU7XG4gICAgICAgICAgICBwcm94eV9zZXRfaGVhZGVyIENvbm5lY3Rpb24gXCJVcGdyYWRlXCI7XG4gICAgICAgICAgICBwcm94eV9zZXRfaGVhZGVyIEhvc3QgJGhvc3Q7XG4gICAgICAgICAgICBwcm94eV9yZWFkX3RpbWVvdXQgODY0MDBzO1xuICAgICAgICB9XG5cbiAgICAgICAgbG9jYXRpb24gL2FwaSB7XG4gICAgICAgICAgICBwcm94eV9wYXNzICRhcHBmbG93eV9jbG91ZF9iYWNrZW5kO1xuICAgICAgICAgICAgcHJveHlfc2V0X2hlYWRlciBYLVJlcXVlc3QtSWQgJHJlcXVlc3RfaWQ7XG4gICAgICAgICAgICBwcm94eV9zZXRfaGVhZGVyIEhvc3QgJGh0dHBfaG9zdDtcblxuICAgICAgICAgICAgIyBTZXQgQ09SUyBoZWFkZXJzIGZvciBvdGhlciByZXF1ZXN0c1xuICAgICAgICAgICAgaWYgKCRyZXF1ZXN0X21ldGhvZCA9ICdPUFRJT05TJykge1xuICAgICAgICAgICAgICAgIGFkZF9oZWFkZXIgJ0FjY2Vzcy1Db250cm9sLUFsbG93LU9yaWdpbicgJGNvcnNfb3JpZ2luIGFsd2F5cztcbiAgICAgICAgICAgICAgICBhZGRfaGVhZGVyICdBY2Nlc3MtQ29udHJvbC1BbGxvdy1NZXRob2RzJyAnR0VULCBQT1NULCBQVVQsIERFTEVURSwgUEFUQ0gsIE9QVElPTlMnIGFsd2F5cztcbiAgICAgICAgICAgICAgICBhZGRfaGVhZGVyICdBY2Nlc3MtQ29udHJvbC1BbGxvdy1IZWFkZXJzJyAnQ29udGVudC1UeXBlLCBBdXRob3JpemF0aW9uLCBBY2NlcHQsIENsaWVudC1WZXJzaW9uLCBEZXZpY2UtSWQnIGFsd2F5cztcbiAgICAgICAgICAgICAgICBhZGRfaGVhZGVyICdBY2Nlc3MtQ29udHJvbC1NYXgtQWdlJyAzNjAwIGFsd2F5cztcbiAgICAgICAgICAgICAgICByZXR1cm4gMjA0O1xuICAgICAgICAgICAgfVxuXG4gICAgICAgICAgICBhZGRfaGVhZGVyICdBY2Nlc3MtQ29udHJvbC1BbGxvdy1PcmlnaW4nICRjb3JzX29yaWdpbiBhbHdheXM7XG4gICAgICAgICAgICBhZGRfaGVhZGVyICdBY2Nlc3MtQ29udHJvbC1BbGxvdy1NZXRob2RzJyAnR0VULCBQT1NULCBQVVQsIERFTEVURSwgUEFUQ0gsIE9QVElPTlMnIGFsd2F5cztcbiAgICAgICAgICAgIGFkZF9oZWFkZXIgJ0FjY2Vzcy1Db250cm9sLUFsbG93LUhlYWRlcnMnICdDb250ZW50LVR5cGUsIEF1dGhvcml6YXRpb24sIEFjY2VwdCwgQ2xpZW50LVZlcnNpb24sIERldmljZS1JZCcgYWx3YXlzO1xuICAgICAgICAgICAgYWRkX2hlYWRlciAnQWNjZXNzLUNvbnRyb2wtTWF4LUFnZScgMzYwMCBhbHdheXM7XG5cbiAgICAgICAgICAgIGxvY2F0aW9uIH4qIF4vYXBpL3dvcmtzcGFjZS8oW2EtekEtWjAtOV8tXSspL3B1Ymxpc2gkIHtcbiAgICAgICAgICAgICAgICBwcm94eV9wYXNzICRhcHBmbG93eV9jbG91ZF9iYWNrZW5kO1xuICAgICAgICAgICAgICAgIHByb3h5X3JlcXVlc3RfYnVmZmVyaW5nIG9mZjtcbiAgICAgICAgICAgICAgICBjbGllbnRfbWF4X2JvZHlfc2l6ZSAyNTZNO1xuICAgICAgICAgICAgICAgIGlmICgkcmVxdWVzdF9tZXRob2QgPSAnT1BUSU9OUycpIHtcbiAgICAgICAgICAgICAgICAgICAgYWRkX2hlYWRlciAnQWNjZXNzLUNvbnRyb2wtQWxsb3ctT3JpZ2luJyAkY29yc19vcmlnaW4gYWx3YXlzO1xuICAgICAgICAgICAgICAgICAgICBhZGRfaGVhZGVyICdBY2Nlc3MtQ29udHJvbC1BbGxvdy1NZXRob2RzJyAnR0VULCBQT1NULCBQVVQsIERFTEVURSwgUEFUQ0gsIE9QVElPTlMnIGFsd2F5cztcbiAgICAgICAgICAgICAgICAgICAgYWRkX2hlYWRlciAnQWNjZXNzLUNvbnRyb2wtQWxsb3ctSGVhZGVycycgJ0NvbnRlbnQtVHlwZSwgQXV0aG9yaXphdGlvbiwgQWNjZXB0LCBDbGllbnQtVmVyc2lvbiwgRGV2aWNlLUlkJyBhbHdheXM7XG4gICAgICAgICAgICAgICAgICAgIGFkZF9oZWFkZXIgJ0FjY2Vzcy1Db250cm9sLU1heC1BZ2UnIDM2MDAgYWx3YXlzO1xuICAgICAgICAgICAgICAgICAgICByZXR1cm4gMjA0O1xuICAgICAgICAgICAgICAgIH1cblxuICAgICAgICAgICAgICAgIGFkZF9oZWFkZXIgJ0FjY2Vzcy1Db250cm9sLUFsbG93LU9yaWdpbicgJGNvcnNfb3JpZ2luIGFsd2F5cztcbiAgICAgICAgICAgICAgICBhZGRfaGVhZGVyICdBY2Nlc3MtQ29udHJvbC1BbGxvdy1NZXRob2RzJyAnR0VULCBQT1NULCBQVVQsIERFTEVURSwgUEFUQ0gsIE9QVElPTlMnIGFsd2F5cztcbiAgICAgICAgICAgICAgICBhZGRfaGVhZGVyICdBY2Nlc3MtQ29udHJvbC1BbGxvdy1IZWFkZXJzJyAnQ29udGVudC1UeXBlLCBBdXRob3JpemF0aW9uLCBBY2NlcHQsIENsaWVudC1WZXJzaW9uLCBEZXZpY2UtSWQnIGFsd2F5cztcbiAgICAgICAgICAgICAgICBhZGRfaGVhZGVyICdBY2Nlc3MtQ29udHJvbC1NYXgtQWdlJyAzNjAwIGFsd2F5cztcbiAgICAgICAgICAgIH1cblxuICAgICAgICAgICAgIyBBcHBGbG93eS1DbG91ZFxuICAgICAgICAgICAgbG9jYXRpb24gL2FwaS9jaGF0IHtcbiAgICAgICAgICAgICAgICBwcm94eV9wYXNzICRhcHBmbG93eV9jbG91ZF9iYWNrZW5kO1xuXG4gICAgICAgICAgICAgICAgcHJveHlfaHR0cF92ZXJzaW9uIDEuMTtcbiAgICAgICAgICAgICAgICBwcm94eV9zZXRfaGVhZGVyIENvbm5lY3Rpb24gXCJcIjtcbiAgICAgICAgICAgICAgICBjaHVua2VkX3RyYW5zZmVyX2VuY29kaW5nIG9uO1xuICAgICAgICAgICAgICAgIHByb3h5X2J1ZmZlcmluZyBvZmY7XG4gICAgICAgICAgICAgICAgcHJveHlfY2FjaGUgb2ZmO1xuXG4gICAgICAgICAgICAgICAgcHJveHlfcmVhZF90aW1lb3V0IDYwMHM7XG4gICAgICAgICAgICAgICAgcHJveHlfY29ubmVjdF90aW1lb3V0IDYwMHM7XG4gICAgICAgICAgICAgICAgcHJveHlfc2VuZF90aW1lb3V0IDYwMHM7XG4gICAgICAgICAgICB9XG5cbiAgICAgICAgICAgIGxvY2F0aW9uIC9hcGkvaW1wb3J0IHtcbiAgICAgICAgICAgICAgICBwcm94eV9wYXNzICRhcHBmbG93eV9jbG91ZF9iYWNrZW5kO1xuXG4gICAgICAgICAgICAgICAgIyBTZXQgaGVhZGVyc1xuICAgICAgICAgICAgICAgIHByb3h5X3NldF9oZWFkZXIgWC1SZXF1ZXN0LUlkICRyZXF1ZXN0X2lkO1xuICAgICAgICAgICAgICAgIHByb3h5X3NldF9oZWFkZXIgSG9zdCAkaHR0cF9ob3N0O1xuXG4gICAgICAgICAgICAgICAgIyBIYW5kbGUgQ09SU1xuICAgICAgICAgICAgICAgIGFkZF9oZWFkZXIgJ0FjY2Vzcy1Db250cm9sLUFsbG93LU9yaWdpbicgJGNvcnNfb3JpZ2luIGFsd2F5cztcbiAgICAgICAgICAgICAgICBhZGRfaGVhZGVyICdBY2Nlc3MtQ29udHJvbC1BbGxvdy1NZXRob2RzJyAnR0VULCBQT1NULCBQVVQsIERFTEVURSwgUEFUQ0gsIE9QVElPTlMnIGFsd2F5cztcbiAgICAgICAgICAgICAgICBhZGRfaGVhZGVyICdBY2Nlc3MtQ29udHJvbC1BbGxvdy1IZWFkZXJzJyAnQ29udGVudC1UeXBlLCBBdXRob3JpemF0aW9uLCBBY2NlcHQsIERldmljZS1JZCcgYWx3YXlzO1xuICAgICAgICAgICAgICAgIGFkZF9oZWFkZXIgJ0FjY2Vzcy1Db250cm9sLU1heC1BZ2UnIDM2MDAgYWx3YXlzO1xuXG4gICAgICAgICAgICAgICAgIyBUaW1lb3V0c1xuICAgICAgICAgICAgICAgIHByb3h5X3JlYWRfdGltZW91dCA2MDBzO1xuICAgICAgICAgICAgICAgIHByb3h5X2Nvbm5lY3RfdGltZW91dCA2MDBzO1xuICAgICAgICAgICAgICAgIHByb3h5X3NlbmRfdGltZW91dCA2MDBzO1xuXG4gICAgICAgICAgICAgICAgIyBEaXNhYmxlIGJ1ZmZlcmluZyBmb3IgbGFyZ2UgZmlsZSB1cGxvYWRzXG4gICAgICAgICAgICAgICAgcHJveHlfcmVxdWVzdF9idWZmZXJpbmcgb2ZmO1xuICAgICAgICAgICAgICAgIHByb3h5X2J1ZmZlcmluZyBvZmY7XG4gICAgICAgICAgICAgICAgcHJveHlfY2FjaGUgb2ZmO1xuICAgICAgICAgICAgICAgIGNsaWVudF9tYXhfYm9keV9zaXplIDJHO1xuICAgICAgICAgICAgfVxuICAgICAgICB9XG5cbiAgICAgICAgIyBNaW5pbyBXZWIgVUlcbiAgICAgICAgIyBEZXJpdmUgZnJvbTogaHR0cHM6Ly9taW4uaW8vZG9jcy9taW5pby9saW51eC9pbnRlZ3JhdGlvbnMvc2V0dXAtbmdpbngtcHJveHktd2l0aC1taW5pby5odG1sXG4gICAgICAgICMgT3B0aW9uYWwgTW9kdWxlLCBjb21tZW50IHRoaXMgc2VjdGlvbiBpZiB5b3UgZGlkIG5vdCBkZXBsb3kgbWluaW8gaW4gZG9ja2VyLWNvbXBvc2UueW1sXG4gICAgICAgICMgVGhpcyBlbmRwb2ludCBpcyBtZWFudCB0byBiZSB1c2VkIGZvciB0aGUgTWluSU8gV2ViIFVJLCBhY2Nlc3NpYmxlIHZpYSB0aGUgYWRtaW4gcG9ydGFsXG4gICAgICAgIGxvY2F0aW9uIC9taW5pby8ge1xuICAgICAgICAgICAgcHJveHlfcGFzcyAkbWluaW9fYmFja2VuZDtcblxuICAgICAgICAgICAgcmV3cml0ZSBeL21pbmlvLyguKikgLyQxIGJyZWFrO1xuICAgICAgICAgICAgcHJveHlfc2V0X2hlYWRlciBIb3N0ICRodHRwX2hvc3Q7XG4gICAgICAgICAgICBwcm94eV9zZXRfaGVhZGVyIFgtUmVhbC1JUCAkcmVtb3RlX2FkZHI7XG4gICAgICAgICAgICBwcm94eV9zZXRfaGVhZGVyIFgtRm9yd2FyZGVkLUZvciAkcHJveHlfYWRkX3hfZm9yd2FyZGVkX2ZvcjtcbiAgICAgICAgICAgIHByb3h5X3NldF9oZWFkZXIgWC1Gb3J3YXJkZWQtUHJvdG8gJHNjaGVtZTtcbiAgICAgICAgICAgIHByb3h5X3NldF9oZWFkZXIgWC1OZ2luWC1Qcm94eSB0cnVlO1xuXG4gICAgICAgICAgICAjIyBUaGlzIGlzIG5lY2Vzc2FyeSB0byBwYXNzIHRoZSBjb3JyZWN0IElQIHRvIGJlIGhhc2hlZFxuICAgICAgICAgICAgcmVhbF9pcF9oZWFkZXIgWC1SZWFsLUlQO1xuXG4gICAgICAgICAgICBwcm94eV9jb25uZWN0X3RpbWVvdXQgMzAwcztcblxuICAgICAgICAgICAgIyMgVG8gc3VwcG9ydCB3ZWJzb2NrZXRzIGluIE1pbklPIHZlcnNpb25zIHJlbGVhc2VkIGFmdGVyIEphbnVhcnkgMjAyM1xuICAgICAgICAgICAgcHJveHlfaHR0cF92ZXJzaW9uIDEuMTtcbiAgICAgICAgICAgIHByb3h5X3NldF9oZWFkZXIgVXBncmFkZSAkaHR0cF91cGdyYWRlO1xuICAgICAgICAgICAgcHJveHlfc2V0X2hlYWRlciBDb25uZWN0aW9uIFwidXBncmFkZVwiO1xuICAgICAgICAgICAgIyBTb21lIGVudmlyb25tZW50cyBtYXkgZW5jb3VudGVyIENPUlMgZXJyb3JzIChLdWJlcm5ldGVzICsgTmdpbnggSW5ncmVzcylcbiAgICAgICAgICAgICMgVW5jb21tZW50IHRoZSBmb2xsb3dpbmcgbGluZSB0byBzZXQgdGhlIE9yaWdpbiByZXF1ZXN0IHRvIGFuIGVtcHR5IHN0cmluZ1xuICAgICAgICAgICAgIyBwcm94eV9zZXRfaGVhZGVyIE9yaWdpbiAnJztcblxuICAgICAgICAgICAgY2h1bmtlZF90cmFuc2Zlcl9lbmNvZGluZyBvZmY7XG4gICAgICAgIH1cblxuICAgICAgICAjIE9wdGlvbmFsIE1vZHVsZSwgY29tbWVudCB0aGlzIHNlY3Rpb24gaWYgeW91IGRpZCBub3QgZGVwbG95IG1pbmlvIGluIGRvY2tlci1jb21wb3NlLnltbFxuICAgICAgICAjIFRoaXMgaXMgdXNlZCBmb3IgcHJlc2lnbmVkIHVybCwgd2hpY2ggaXMgbmVlZHMgdG8gYmUgZXhwb3NlZCB0byB0aGUgQXBwRmxvd3kgY2xpZW50IGFwcGxpY2F0aW9uLlxuICAgICAgICBsb2NhdGlvbiAvbWluaW8tYXBpLyB7XG4gICAgICAgICAgICBwcm94eV9wYXNzICRtaW5pb19hcGlfYmFja2VuZDtcblxuICAgICAgICAgICAgIyBTZXQgdGhlIGhvc3QgdG8gaW50ZXJuYWwgaG9zdCBiZWNhdXNlIHRoZSBwcmVzaWduZWQgdXJsIHdhcyBzaWduZWQgYWdhaW5zdCB0aGUgaW50ZXJuYWwgaG9zdFxuICAgICAgICAgICAgcHJveHlfc2V0X2hlYWRlciBIb3N0ICRtaW5pb19pbnRlcm5hbF9ob3N0O1xuICAgICAgICAgICAgcHJveHlfc2V0X2hlYWRlciBYLVJlYWwtSVAgJHJlbW90ZV9hZGRyO1xuICAgICAgICAgICAgcHJveHlfc2V0X2hlYWRlciBYLUZvcndhcmRlZC1Gb3IgJHByb3h5X2FkZF94X2ZvcndhcmRlZF9mb3I7XG4gICAgICAgICAgICBwcm94eV9zZXRfaGVhZGVyIFgtRm9yd2FyZGVkLVByb3RvICRzY2hlbWU7XG5cbiAgICAgICAgICAgIHJld3JpdGUgXi9taW5pby1hcGkvKC4qKSAvJDEgYnJlYWs7XG5cbiAgICAgICAgICAgIHByb3h5X2Nvbm5lY3RfdGltZW91dCAzMDBzO1xuICAgICAgICAgICAgIyBEZWZhdWx0IGlzIEhUVFAvMSwga2VlcGFsaXZlIGlzIG9ubHkgZW5hYmxlZCBpbiBIVFRQLzEuMVxuICAgICAgICAgICAgcHJveHlfaHR0cF92ZXJzaW9uIDEuMTtcbiAgICAgICAgICAgIHByb3h5X3NldF9oZWFkZXIgQ29ubmVjdGlvbiBcIlwiO1xuICAgICAgICAgICAgY2h1bmtlZF90cmFuc2Zlcl9lbmNvZGluZyBvZmY7XG4gICAgICAgIH1cblxuICAgICAgICAjIFBnQWRtaW5cbiAgICAgICAgIyBPcHRpb25hbCBNb2R1bGUsIGNvbW1lbnQgdGhpcyBzZWN0aW9uIGlmIHlvdSBkaWQgbm90IGRlcGxveSBwZ2FkbWluIGluIGRvY2tlci1jb21wb3NlLnltbFxuICAgICAgICBsb2NhdGlvbiAvcGdhZG1pbi8ge1xuICAgICAgICAgICAgc2V0ICRwZ2FkbWluIHBnYWRtaW47XG4gICAgICAgICAgICBwcm94eV9wYXNzICRwZ2FkbWluX2JhY2tlbmQ7XG5cbiAgICAgICAgICAgIHByb3h5X3NldF9oZWFkZXIgWC1TY3JpcHQtTmFtZSAvcGdhZG1pbjtcbiAgICAgICAgICAgIHByb3h5X3NldF9oZWFkZXIgWC1TY2hlbWUgJHNjaGVtZTtcbiAgICAgICAgICAgIHByb3h5X3NldF9oZWFkZXIgSG9zdCAkaG9zdDtcbiAgICAgICAgICAgIHByb3h5X3JlZGlyZWN0IG9mZjtcbiAgICAgICAgfVxuXG4gICAgICAgICMgQWRtaW4gRnJvbnRlbmRcbiAgICAgICAgIyBPcHRpb25hbCBNb2R1bGUsIGNvbW1lbnQgdGhpcyBzZWN0aW9uIGlmIHlvdSBkaWQgbm90IGRlcGxveSBhZG1pbl9mcm9udGVuZCBpbiBkb2NrZXItY29tcG9zZS55bWxcbiAgICAgICAgbG9jYXRpb24gL2NvbnNvbGUge1xuICAgICAgICAgICAgcHJveHlfcGFzcyAkYWRtaW5fZnJvbnRlbmRfYmFja2VuZDtcblxuICAgICAgICAgICAgcHJveHlfc2V0X2hlYWRlciBYLVNjaGVtZSAkc2NoZW1lO1xuICAgICAgICAgICAgcHJveHlfc2V0X2hlYWRlciBIb3N0ICRob3N0O1xuICAgICAgICB9XG5cbiAgICAgICAgIyBBcHBGbG93eSBXZWJcbiAgICAgICAgbG9jYXRpb24gLyB7XG4gICAgICAgICAgICBwcm94eV9wYXNzICRhcHBmbG93eV93ZWJfYmFja2VuZDtcbiAgICAgICAgICAgIHByb3h5X3NldF9oZWFkZXIgWC1TY2hlbWUgJHNjaGVtZTtcbiAgICAgICAgICAgIHByb3h5X3NldF9oZWFkZXIgSG9zdCAkaG9zdDtcbiAgICAgICAgfVxuICAgIH1cblxufVxuXCJcIlwiXG4iCn0=
```

## Links

`productivity`,`self-hosted`,`notes`,`knowledge-base`,`notion-alternative`

---

Version:`0.9.3`

AnytypeAnytype is a personal knowledge base—your digital brain—that lets you gather, connect and remix all kinds of information. Create pages, tasks, wikis, journals—even entire apps—and define your own data model while your data stays offline-first, private and encrypted across devices. After installation, you can view the Anytype client configuration by running `cat /data/client-config.yml` inside the service container.

Apprise APIApprise API provides a simple interface for sending notifications to almost all of the most popular notification services available to us today.

### On this page

ConfigurationBase64LinksTags