---
title: "Appwrite | Dokploy"
source: "https://docs.dokploy.com/docs/templates/appwrite"
category: dokploy-docs
created: "2026-06-25T17:21:41.528Z"
---

Appwrite | Dokploy

# Appwrite

Copy as Markdown

Appwrite is an end-to-end platform for building Web, Mobile, Native, or Backend apps, packaged as a set of Docker microservices. It includes both a backend server and a fully integrated hosting solution for deploying static and server-side rendered frontends. Appwrite abstracts the complexity and repetitiveness required to build modern apps from scratch and allows you to build secure, full-stack applications faster. Using Appwrite, you can easily integrate your app with user authentication and multiple sign-in methods, a database for storing and querying users and team data, storage and file management, image manipulation, Cloud Functions, messaging, and more services.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

x-logging: &x-logging
  logging:
    driver: "json-file"
    options:
      max-file: "5"
      max-size: "10m"
services:
  appwrite:
    image: appwrite/appwrite:1.8.0
    <<: *x-logging
    restart: unless-stopped
    labels:
      - traefik.enable=true
      - traefik.constraint-label-stack=appwrite
    volumes:
      - appwrite-uploads:/storage/uploads:rw
      - appwrite-imports:/storage/imports:rw
      - appwrite-cache:/storage/cache:rw
      - appwrite-config:/storage/config:rw
      - appwrite-certificates:/storage/certificates:rw
      - appwrite-functions:/storage/functions:rw
      - appwrite-sites:/storage/sites:rw
      - appwrite-builds:/storage/builds:rw
    depends_on:
      - mariadb
      - redis
    #      - clamav
    environment:
      - _APP_ENV
      - _APP_WORKER_PER_CORE
      - _APP_LOCALE
      - _APP_COMPRESSION_MIN_SIZE_BYTES
      - _APP_CONSOLE_WHITELIST_ROOT
      - _APP_CONSOLE_WHITELIST_EMAILS
      - _APP_CONSOLE_SESSION_ALERTS
      - _APP_CONSOLE_WHITELIST_IPS
      - _APP_CONSOLE_HOSTNAMES
      - _APP_SYSTEM_EMAIL_NAME
      - _APP_SYSTEM_EMAIL_ADDRESS
      - _APP_EMAIL_SECURITY
      - _APP_SYSTEM_RESPONSE_FORMAT
      - _APP_OPTIONS_ABUSE
      - _APP_OPTIONS_ROUTER_PROTECTION
      - _APP_OPTIONS_FORCE_HTTPS
      - _APP_OPTIONS_ROUTER_FORCE_HTTPS
      - _APP_OPENSSL_KEY_V1
      - _APP_DOMAIN
      - _APP_DOMAIN_TARGET_CNAME
      - _APP_DOMAIN_TARGET_AAAA
      - _APP_DOMAIN_TARGET_A
      - _APP_DOMAIN_TARGET_CAA
      - _APP_DNS
      - _APP_DOMAIN_FUNCTIONS
      - _APP_REDIS_HOST
      - _APP_REDIS_PORT
      - _APP_REDIS_USER
      - _APP_REDIS_PASS
      - _APP_DB_HOST
      - _APP_DB_PORT
      - _APP_DB_SCHEMA
      - _APP_DB_USER
      - _APP_DB_PASS
      - _APP_SMTP_HOST
      - _APP_SMTP_PORT
      - _APP_SMTP_SECURE
      - _APP_SMTP_USERNAME
      - _APP_SMTP_PASSWORD
      - _APP_USAGE_STATS
      - _APP_STORAGE_LIMIT
      - _APP_STORAGE_PREVIEW_LIMIT
      - _APP_STORAGE_ANTIVIRUS
      - _APP_STORAGE_ANTIVIRUS_HOST
      - _APP_STORAGE_ANTIVIRUS_PORT
      - _APP_STORAGE_DEVICE
      - _APP_STORAGE_S3_ACCESS_KEY
      - _APP_STORAGE_S3_SECRET
      - _APP_STORAGE_S3_REGION
      - _APP_STORAGE_S3_BUCKET
      - _APP_STORAGE_S3_ENDPOINT
      - _APP_STORAGE_DO_SPACES_ACCESS_KEY
      - _APP_STORAGE_DO_SPACES_SECRET
      - _APP_STORAGE_DO_SPACES_REGION
      - _APP_STORAGE_DO_SPACES_BUCKET
      - _APP_STORAGE_BACKBLAZE_ACCESS_KEY
      - _APP_STORAGE_BACKBLAZE_SECRET
      - _APP_STORAGE_BACKBLAZE_REGION
      - _APP_STORAGE_BACKBLAZE_BUCKET
      - _APP_STORAGE_LINODE_ACCESS_KEY
      - _APP_STORAGE_LINODE_SECRET
      - _APP_STORAGE_LINODE_REGION
      - _APP_STORAGE_LINODE_BUCKET
      - _APP_STORAGE_WASABI_ACCESS_KEY
      - _APP_STORAGE_WASABI_SECRET
      - _APP_STORAGE_WASABI_REGION
      - _APP_STORAGE_WASABI_BUCKET
      - _APP_COMPUTE_SIZE_LIMIT
      - _APP_FUNCTIONS_TIMEOUT
      - _APP_SITES_TIMEOUT
      - _APP_COMPUTE_BUILD_TIMEOUT
      - _APP_COMPUTE_CPUS
      - _APP_COMPUTE_MEMORY
      - _APP_FUNCTIONS_RUNTIMES
      - _APP_SITES_RUNTIMES
      - _APP_DOMAIN_SITES
      - _APP_EXECUTOR_SECRET
      - _APP_EXECUTOR_HOST
      - _APP_LOGGING_CONFIG
      - _APP_MAINTENANCE_INTERVAL
      - _APP_MAINTENANCE_DELAY
      - _APP_MAINTENANCE_START_TIME
      - _APP_MAINTENANCE_RETENTION_EXECUTION
      - _APP_MAINTENANCE_RETENTION_CACHE
      - _APP_MAINTENANCE_RETENTION_ABUSE
      - _APP_MAINTENANCE_RETENTION_AUDIT
      - _APP_MAINTENANCE_RETENTION_AUDIT_CONSOLE
      - _APP_MAINTENANCE_RETENTION_USAGE_HOURLY
      - _APP_MAINTENANCE_RETENTION_SCHEDULES
      - _APP_SMS_PROVIDER
      - _APP_SMS_FROM
      - _APP_GRAPHQL_MAX_BATCH_SIZE
      - _APP_GRAPHQL_MAX_COMPLEXITY
      - _APP_GRAPHQL_MAX_DEPTH
      - _APP_VCS_GITHUB_APP_NAME
      - _APP_VCS_GITHUB_PRIVATE_KEY
      - _APP_VCS_GITHUB_APP_ID
      - _APP_VCS_GITHUB_WEBHOOK_SECRET
      - _APP_VCS_GITHUB_CLIENT_SECRET
      - _APP_VCS_GITHUB_CLIENT_ID
      - _APP_MIGRATIONS_FIREBASE_CLIENT_ID
      - _APP_MIGRATIONS_FIREBASE_CLIENT_SECRET
      - _APP_ASSISTANT_OPENAI_API_KEY
  appwrite-console:
    <<: *x-logging
    image: appwrite/console:7.4.7
    restart: unless-stopped
    labels:
      - "traefik.enable=true"
      - "traefik.constraint-label-stack=appwrite"

  appwrite-realtime:
    image: appwrite/appwrite:1.8.0
    entrypoint: realtime
    <<: *x-logging
    restart: unless-stopped
    labels:
      - "traefik.enable=true"
      - "traefik.constraint-label-stack=appwrite"
    depends_on:
      - mariadb
      - redis
    environment:
      - _APP_ENV
      - _APP_WORKER_PER_CORE
      - _APP_OPTIONS_ABUSE
      - _APP_OPTIONS_ROUTER_PROTECTION
      - _APP_OPENSSL_KEY_V1
      - _APP_REDIS_HOST
      - _APP_REDIS_PORT
      - _APP_REDIS_USER
      - _APP_REDIS_PASS
      - _APP_DB_HOST
      - _APP_DB_PORT
      - _APP_DB_SCHEMA
      - _APP_DB_USER
      - _APP_DB_PASS
      - _APP_USAGE_STATS
      - _APP_LOGGING_CONFIG

  appwrite-worker-audits:
    image: appwrite/appwrite:1.8.0
    entrypoint: worker-audits
    <<: *x-logging
    restart: unless-stopped
    depends_on:
      - redis
      - mariadb
    environment:
      - _APP_ENV
      - _APP_WORKER_PER_CORE
      - _APP_OPENSSL_KEY_V1
      - _APP_REDIS_HOST
      - _APP_REDIS_PORT
      - _APP_REDIS_USER
      - _APP_REDIS_PASS
      - _APP_DB_HOST
      - _APP_DB_PORT
      - _APP_DB_SCHEMA
      - _APP_DB_USER
      - _APP_DB_PASS
      - _APP_LOGGING_CONFIG

  appwrite-worker-webhooks:
    image: appwrite/appwrite:1.8.0
    entrypoint: worker-webhooks
    <<: *x-logging
    restart: unless-stopped
    depends_on:
      - redis
      - mariadb
    environment:
      - _APP_ENV
      - _APP_WORKER_PER_CORE
      - _APP_OPENSSL_KEY_V1
      - _APP_EMAIL_SECURITY
      - _APP_SYSTEM_SECURITY_EMAIL_ADDRESS
      - _APP_DB_HOST
      - _APP_DB_PORT
      - _APP_DB_SCHEMA
      - _APP_DB_USER
      - _APP_DB_PASS
      - _APP_REDIS_HOST
      - _APP_REDIS_PORT
      - _APP_REDIS_USER
      - _APP_REDIS_PASS
      - _APP_LOGGING_CONFIG

  appwrite-worker-deletes:
    image: appwrite/appwrite:1.8.0
    entrypoint: worker-deletes
    <<: *x-logging
    restart: unless-stopped
    depends_on:
      - redis
      - mariadb
    volumes:
      - appwrite-uploads:/storage/uploads:rw
      - appwrite-cache:/storage/cache:rw
      - appwrite-functions:/storage/functions:rw
      - appwrite-sites:/storage/sites:rw
      - appwrite-builds:/storage/builds:rw
      - appwrite-certificates:/storage/certificates:rw
    environment:
      - _APP_ENV
      - _APP_WORKER_PER_CORE
      - _APP_OPENSSL_KEY_V1
      - _APP_REDIS_HOST
      - _APP_REDIS_PORT
      - _APP_REDIS_USER
      - _APP_REDIS_PASS
      - _APP_DB_HOST
      - _APP_DB_PORT
      - _APP_DB_SCHEMA
      - _APP_DB_USER
      - _APP_DB_PASS
      - _APP_STORAGE_DEVICE
      - _APP_STORAGE_S3_ACCESS_KEY
      - _APP_STORAGE_S3_SECRET
      - _APP_STORAGE_S3_REGION
      - _APP_STORAGE_S3_BUCKET
      - _APP_STORAGE_S3_ENDPOINT
      - _APP_STORAGE_DO_SPACES_ACCESS_KEY
      - _APP_STORAGE_DO_SPACES_SECRET
      - _APP_STORAGE_DO_SPACES_REGION
      - _APP_STORAGE_DO_SPACES_BUCKET
      - _APP_STORAGE_BACKBLAZE_ACCESS_KEY
      - _APP_STORAGE_BACKBLAZE_SECRET
      - _APP_STORAGE_BACKBLAZE_REGION
      - _APP_STORAGE_BACKBLAZE_BUCKET
      - _APP_STORAGE_LINODE_ACCESS_KEY
      - _APP_STORAGE_LINODE_SECRET
      - _APP_STORAGE_LINODE_REGION
      - _APP_STORAGE_LINODE_BUCKET
      - _APP_STORAGE_WASABI_ACCESS_KEY
      - _APP_STORAGE_WASABI_SECRET
      - _APP_STORAGE_WASABI_REGION
      - _APP_STORAGE_WASABI_BUCKET
      - _APP_LOGGING_CONFIG
      - _APP_EXECUTOR_SECRET
      - _APP_EXECUTOR_HOST
      - _APP_MAINTENANCE_RETENTION_ABUSE
      - _APP_MAINTENANCE_RETENTION_AUDIT
      - _APP_MAINTENANCE_RETENTION_AUDIT_CONSOLE
      - _APP_MAINTENANCE_RETENTION_EXECUTION
      - _APP_SYSTEM_SECURITY_EMAIL_ADDRESS
      - _APP_EMAIL_CERTIFICATES

  appwrite-worker-databases:
    image: appwrite/appwrite:1.8.0
    entrypoint: worker-databases
    <<: *x-logging
    restart: unless-stopped
    depends_on:
      - redis
      - mariadb
    environment:
      - _APP_ENV
      - _APP_WORKER_PER_CORE
      - _APP_OPENSSL_KEY_V1
      - _APP_REDIS_HOST
      - _APP_REDIS_PORT
      - _APP_REDIS_USER
      - _APP_REDIS_PASS
      - _APP_DB_HOST
      - _APP_DB_PORT
      - _APP_DB_SCHEMA
      - _APP_DB_USER
      - _APP_DB_PASS
      - _APP_LOGGING_CONFIG

  appwrite-worker-builds:
    image: appwrite/appwrite:1.8.0
    entrypoint: worker-builds
    <<: *x-logging
    restart: unless-stopped
    depends_on:
      - redis
      - mariadb
    volumes:
      - appwrite-functions:/storage/functions:rw
      - appwrite-sites:/storage/sites:rw
      - appwrite-builds:/storage/builds:rw
      - appwrite-uploads:/storage/uploads:rw
    environment:
      - _APP_ENV
      - _APP_WORKER_PER_CORE
      - _APP_OPENSSL_KEY_V1
      - _APP_EXECUTOR_SECRET
      - _APP_EXECUTOR_HOST
      - _APP_REDIS_HOST
      - _APP_REDIS_PORT
      - _APP_REDIS_USER
      - _APP_REDIS_PASS
      - _APP_DB_HOST
      - _APP_DB_PORT
      - _APP_DB_SCHEMA
      - _APP_DB_USER
      - _APP_DB_PASS
      - _APP_LOGGING_CONFIG
      - _APP_VCS_GITHUB_APP_NAME
      - _APP_VCS_GITHUB_PRIVATE_KEY
      - _APP_VCS_GITHUB_APP_ID
      - _APP_FUNCTIONS_TIMEOUT
      - _APP_SITES_TIMEOUT
      - _APP_COMPUTE_BUILD_TIMEOUT
      - _APP_COMPUTE_CPUS
      - _APP_COMPUTE_MEMORY
      - _APP_COMPUTE_SIZE_LIMIT
      - _APP_OPTIONS_FORCE_HTTPS
      - _APP_OPTIONS_ROUTER_FORCE_HTTPS
      - _APP_DOMAIN
      - _APP_STORAGE_DEVICE
      - _APP_STORAGE_S3_ACCESS_KEY
      - _APP_STORAGE_S3_SECRET
      - _APP_STORAGE_S3_REGION
      - _APP_STORAGE_S3_BUCKET
      - _APP_STORAGE_S3_ENDPOINT
      - _APP_STORAGE_DO_SPACES_ACCESS_KEY
      - _APP_STORAGE_DO_SPACES_SECRET
      - _APP_STORAGE_DO_SPACES_REGION
      - _APP_STORAGE_DO_SPACES_BUCKET
      - _APP_STORAGE_BACKBLAZE_ACCESS_KEY
      - _APP_STORAGE_BACKBLAZE_SECRET
      - _APP_STORAGE_BACKBLAZE_REGION
      - _APP_STORAGE_BACKBLAZE_BUCKET
      - _APP_STORAGE_LINODE_ACCESS_KEY
      - _APP_STORAGE_LINODE_SECRET
      - _APP_STORAGE_LINODE_REGION
      - _APP_STORAGE_LINODE_BUCKET
      - _APP_STORAGE_WASABI_ACCESS_KEY
      - _APP_STORAGE_WASABI_SECRET
      - _APP_STORAGE_WASABI_REGION
      - _APP_STORAGE_WASABI_BUCKET
      - _APP_DOMAIN_SITES

  appwrite-worker-certificates:
    image: appwrite/appwrite:1.8.0
    entrypoint: worker-certificates
    <<: *x-logging
    restart: unless-stopped
    depends_on:
      - redis
      - mariadb
    volumes:
      - appwrite-config:/storage/config:rw
      - appwrite-certificates:/storage/certificates:rw
    environment:
      - _APP_ENV
      - _APP_WORKER_PER_CORE
      - _APP_OPENSSL_KEY_V1
      - _APP_DOMAIN
      - _APP_DOMAIN_TARGET_CNAME
      - _APP_DOMAIN_TARGET_AAAA
      - _APP_DOMAIN_TARGET_A
      - _APP_DOMAIN_TARGET_CAA
      - _APP_DNS
      - _APP_DOMAIN_FUNCTIONS
      - _APP_EMAIL_CERTIFICATES
      - _APP_REDIS_HOST
      - _APP_REDIS_PORT
      - _APP_REDIS_USER
      - _APP_REDIS_PASS
      - _APP_DB_HOST
      - _APP_DB_PORT
      - _APP_DB_SCHEMA
      - _APP_DB_USER
      - _APP_DB_PASS
      - _APP_LOGGING_CONFIG

  appwrite-worker-functions:
    image: appwrite/appwrite:1.8.0
    entrypoint: worker-functions
    <<: *x-logging
    restart: unless-stopped
    depends_on:
      - redis
      - mariadb
      - openruntimes-executor
    environment:
      - _APP_ENV
      - _APP_WORKER_PER_CORE
      - _APP_OPENSSL_KEY_V1
      - _APP_DOMAIN
      - _APP_OPTIONS_FORCE_HTTPS
      - _APP_REDIS_HOST
      - _APP_REDIS_PORT
      - _APP_REDIS_USER
      - _APP_REDIS_PASS
      - _APP_DB_HOST
      - _APP_DB_PORT
      - _APP_DB_SCHEMA
      - _APP_DB_USER
      - _APP_DB_PASS
      - _APP_FUNCTIONS_TIMEOUT
      - _APP_SITES_TIMEOUT
      - _APP_COMPUTE_BUILD_TIMEOUT
      - _APP_COMPUTE_CPUS
      - _APP_COMPUTE_MEMORY
      - _APP_EXECUTOR_SECRET
      - _APP_EXECUTOR_HOST
      - _APP_USAGE_STATS
      - _APP_DOCKER_HUB_USERNAME
      - _APP_DOCKER_HUB_PASSWORD
      - _APP_LOGGING_CONFIG

  appwrite-worker-mails:
    image: appwrite/appwrite:1.8.0
    entrypoint: worker-mails
    <<: *x-logging
    restart: unless-stopped
    depends_on:
      - redis
    environment:
      - _APP_ENV
      - _APP_WORKER_PER_CORE
      - _APP_OPENSSL_KEY_V1
      - _APP_SYSTEM_EMAIL_NAME
      - _APP_SYSTEM_EMAIL_ADDRESS
      - _APP_DB_HOST
      - _APP_DB_PORT
      - _APP_DB_SCHEMA
      - _APP_DB_USER
      - _APP_DB_PASS
      - _APP_REDIS_HOST
      - _APP_REDIS_PORT
      - _APP_REDIS_USER
      - _APP_REDIS_PASS
      - _APP_SMTP_HOST
      - _APP_SMTP_PORT
      - _APP_SMTP_SECURE
      - _APP_SMTP_USERNAME
      - _APP_SMTP_PASSWORD
      - _APP_LOGGING_CONFIG
      - _APP_DOMAIN
      - _APP_OPTIONS_FORCE_HTTPS

  appwrite-worker-messaging:
    image: appwrite/appwrite:1.8.0
    entrypoint: worker-messaging
    <<: *x-logging
    restart: unless-stopped
    volumes:
      - appwrite-uploads:/storage/uploads:rw
    depends_on:
      - redis
    environment:
      - _APP_ENV
      - _APP_WORKER_PER_CORE
      - _APP_OPENSSL_KEY_V1
      - _APP_REDIS_HOST
      - _APP_REDIS_PORT
      - _APP_REDIS_USER
      - _APP_REDIS_PASS
      - _APP_DB_HOST
      - _APP_DB_PORT
      - _APP_DB_SCHEMA
      - _APP_DB_USER
      - _APP_DB_PASS
      - _APP_LOGGING_CONFIG
      - _APP_SMS_FROM
      - _APP_SMS_PROVIDER
      - _APP_STORAGE_DEVICE
      - _APP_STORAGE_S3_ACCESS_KEY
      - _APP_STORAGE_S3_SECRET
      - _APP_STORAGE_S3_REGION
      - _APP_STORAGE_S3_BUCKET
      - _APP_STORAGE_S3_ENDPOINT
      - _APP_STORAGE_DO_SPACES_ACCESS_KEY
      - _APP_STORAGE_DO_SPACES_SECRET
      - _APP_STORAGE_DO_SPACES_REGION
      - _APP_STORAGE_DO_SPACES_BUCKET
      - _APP_STORAGE_BACKBLAZE_ACCESS_KEY
      - _APP_STORAGE_BACKBLAZE_SECRET
      - _APP_STORAGE_BACKBLAZE_REGION
      - _APP_STORAGE_BACKBLAZE_BUCKET
      - _APP_STORAGE_LINODE_ACCESS_KEY
      - _APP_STORAGE_LINODE_SECRET
      - _APP_STORAGE_LINODE_REGION
      - _APP_STORAGE_LINODE_BUCKET
      - _APP_STORAGE_WASABI_ACCESS_KEY
      - _APP_STORAGE_WASABI_SECRET
      - _APP_STORAGE_WASABI_REGION
      - _APP_STORAGE_WASABI_BUCKET

  appwrite-worker-migrations:
    image: appwrite/appwrite:1.8.0
    entrypoint: worker-migrations
    <<: *x-logging
    restart: unless-stopped
    volumes:
      - appwrite-imports:/storage/imports:rw
    depends_on:
      - mariadb
    environment:
      - _APP_ENV
      - _APP_WORKER_PER_CORE
      - _APP_OPENSSL_KEY_V1
      - _APP_DOMAIN
      - _APP_DOMAIN_TARGET_CNAME
      - _APP_DOMAIN_TARGET_AAAA
      - _APP_DOMAIN_TARGET_A
      - _APP_DOMAIN_TARGET_CAA
      - _APP_DNS
      - _APP_EMAIL_SECURITY
      - _APP_REDIS_HOST
      - _APP_REDIS_PORT
      - _APP_REDIS_USER
      - _APP_REDIS_PASS
      - _APP_DB_HOST
      - _APP_DB_PORT
      - _APP_DB_SCHEMA
      - _APP_DB_USER
      - _APP_DB_PASS
      - _APP_LOGGING_CONFIG
      - _APP_MIGRATIONS_FIREBASE_CLIENT_ID
      - _APP_MIGRATIONS_FIREBASE_CLIENT_SECRET

  appwrite-task-maintenance:
    image: appwrite/appwrite:1.8.0
    entrypoint: maintenance
    <<: *x-logging
    restart: unless-stopped
    depends_on:
      - redis
    environment:
      - _APP_ENV
      - _APP_WORKER_PER_CORE
      - _APP_DOMAIN
      - _APP_DOMAIN_TARGET_CNAME
      - _APP_DOMAIN_TARGET_AAAA
      - _APP_DOMAIN_TARGET_A
      - _APP_DOMAIN_TARGET_CAA
      - _APP_DNS
      - _APP_DOMAIN_FUNCTIONS
      - _APP_OPENSSL_KEY_V1
      - _APP_REDIS_HOST
      - _APP_REDIS_PORT
      - _APP_REDIS_USER
      - _APP_REDIS_PASS
      - _APP_DB_HOST
      - _APP_DB_PORT
      - _APP_DB_SCHEMA
      - _APP_DB_USER
      - _APP_DB_PASS
      - _APP_MAINTENANCE_INTERVAL
      - _APP_MAINTENANCE_RETENTION_EXECUTION
      - _APP_MAINTENANCE_RETENTION_CACHE
      - _APP_MAINTENANCE_RETENTION_ABUSE
      - _APP_MAINTENANCE_RETENTION_AUDIT
      - _APP_MAINTENANCE_RETENTION_AUDIT_CONSOLE
      - _APP_MAINTENANCE_RETENTION_USAGE_HOURLY
      - _APP_MAINTENANCE_RETENTION_SCHEDULES

  appwrite-task-stats-resources:
    image: appwrite/appwrite:1.8.0
    entrypoint: stats-resources
    <<: *x-logging
    restart: unless-stopped
    depends_on:
      - redis
      - mariadb
    environment:
      - _APP_ENV
      - _APP_WORKER_PER_CORE
      - _APP_OPENSSL_KEY_V1
      - _APP_DB_HOST
      - _APP_DB_PORT
      - _APP_DB_SCHEMA
      - _APP_DB_USER
      - _APP_DB_PASS
      - _APP_REDIS_HOST
      - _APP_REDIS_PORT
      - _APP_REDIS_USER
      - _APP_REDIS_PASS
      - _APP_USAGE_STATS
      - _APP_LOGGING_CONFIG
      - _APP_DATABASE_SHARED_TABLES
      - _APP_STATS_RESOURCES_INTERVAL

  appwrite-worker-stats-resources:
    image: appwrite/appwrite:1.8.0
    entrypoint: worker-stats-resources
    <<: *x-logging
    restart: unless-stopped
    depends_on:
      - redis
      - mariadb
    environment:
      - _APP_ENV
      - _APP_WORKER_PER_CORE
      - _APP_OPENSSL_KEY_V1
      - _APP_DB_HOST
      - _APP_DB_PORT
      - _APP_DB_SCHEMA
      - _APP_DB_USER
      - _APP_DB_PASS
      - _APP_REDIS_HOST
      - _APP_REDIS_PORT
      - _APP_REDIS_USER
      - _APP_REDIS_PASS
      - _APP_USAGE_STATS
      - _APP_LOGGING_CONFIG
      - _APP_STATS_RESOURCES_INTERVAL

  appwrite-worker-stats-usage:
    image: appwrite/appwrite:1.8.0
    entrypoint: worker-stats-usage
    <<: *x-logging
    restart: unless-stopped
    depends_on:
      - redis
      - mariadb
    environment:
      - _APP_ENV
      - _APP_WORKER_PER_CORE
      - _APP_OPENSSL_KEY_V1
      - _APP_DB_HOST
      - _APP_DB_PORT
      - _APP_DB_SCHEMA
      - _APP_DB_USER
      - _APP_DB_PASS
      - _APP_REDIS_HOST
      - _APP_REDIS_PORT
      - _APP_REDIS_USER
      - _APP_REDIS_PASS
      - _APP_USAGE_STATS
      - _APP_LOGGING_CONFIG
      - _APP_USAGE_AGGREGATION_INTERVAL

  appwrite-task-scheduler-functions:
    image: appwrite/appwrite:1.8.0
    entrypoint: schedule-functions
    <<: *x-logging
    restart: unless-stopped
    depends_on:
      - mariadb
      - redis
    environment:
      - _APP_ENV
      - _APP_WORKER_PER_CORE
      - _APP_OPENSSL_KEY_V1
      - _APP_REDIS_HOST
      - _APP_REDIS_PORT
      - _APP_REDIS_USER
      - _APP_REDIS_PASS
      - _APP_DB_HOST
      - _APP_DB_PORT
      - _APP_DB_SCHEMA
      - _APP_DB_USER
      - _APP_DB_PASS

  appwrite-task-scheduler-executions:
    image: appwrite/appwrite:1.8.0
    entrypoint: schedule-executions
    <<: *x-logging
    restart: unless-stopped
    depends_on:
      - mariadb
      - redis
    environment:
      - _APP_ENV
      - _APP_WORKER_PER_CORE
      - _APP_OPENSSL_KEY_V1
      - _APP_REDIS_HOST
      - _APP_REDIS_PORT
      - _APP_REDIS_USER
      - _APP_REDIS_PASS
      - _APP_DB_HOST
      - _APP_DB_PORT
      - _APP_DB_SCHEMA
      - _APP_DB_USER
      - _APP_DB_PASS

  appwrite-task-scheduler-messages:
    image: appwrite/appwrite:1.8.0
    entrypoint: schedule-messages
    <<: *x-logging
    restart: unless-stopped
    depends_on:
      - mariadb
      - redis
    environment:
      - _APP_ENV
      - _APP_WORKER_PER_CORE
      - _APP_OPENSSL_KEY_V1
      - _APP_REDIS_HOST
      - _APP_REDIS_PORT
      - _APP_REDIS_USER
      - _APP_REDIS_PASS
      - _APP_DB_HOST
      - _APP_DB_PORT
      - _APP_DB_SCHEMA
      - _APP_DB_USER
      - _APP_DB_PASS

  appwrite-assistant:
    image: appwrite/assistant:0.8.3
    <<: *x-logging
    restart: unless-stopped
    environment:
      - _APP_ASSISTANT_OPENAI_API_KEY

  appwrite-browser:
    image: appwrite/browser:0.2.4
    <<: *x-logging
    restart: unless-stopped

  openruntimes-executor:
    hostname: exc1
    <<: *x-logging
    restart: unless-stopped
    stop_signal: SIGINT
    image: openruntimes/executor:0.7.22
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - appwrite-builds:/storage/builds:rw
      - appwrite-functions:/storage/functions:rw
      - appwrite-sites:/storage/sites:rw
      # Host mount necessary to share files between executor and runtimes.
      # It's not possible to share mount file between 2 containers without host mount (copying is too slow)
      - /tmp:/tmp:rw
    environment:
      - OPR_EXECUTOR_INACTIVE_TRESHOLD=$_APP_COMPUTE_INACTIVE_THRESHOLD
      - OPR_EXECUTOR_MAINTENANCE_INTERVAL=$_APP_COMPUTE_MAINTENANCE_INTERVAL
      - OPR_EXECUTOR_NETWORK=$_APP_COMPUTE_RUNTIMES_NETWORK
      - OPR_EXECUTOR_DOCKER_HUB_USERNAME=$_APP_DOCKER_HUB_USERNAME
      - OPR_EXECUTOR_DOCKER_HUB_PASSWORD=$_APP_DOCKER_HUB_PASSWORD
      - OPR_EXECUTOR_ENV=$_APP_ENV
      - OPR_EXECUTOR_RUNTIMES=$_APP_FUNCTIONS_RUNTIMES,$_APP_SITES_RUNTIMES
      - OPR_EXECUTOR_SECRET=$_APP_EXECUTOR_SECRET
      - OPR_EXECUTOR_RUNTIME_VERSIONS=v5
      - OPR_EXECUTOR_LOGGING_CONFIG=$_APP_LOGGING_CONFIG
      - OPR_EXECUTOR_STORAGE_DEVICE=$_APP_STORAGE_DEVICE
      - OPR_EXECUTOR_STORAGE_S3_ACCESS_KEY=$_APP_STORAGE_S3_ACCESS_KEY
      - OPR_EXECUTOR_STORAGE_S3_SECRET=$_APP_STORAGE_S3_SECRET
      - OPR_EXECUTOR_STORAGE_S3_REGION=$_APP_STORAGE_S3_REGION
      - OPR_EXECUTOR_STORAGE_S3_BUCKET=$_APP_STORAGE_S3_BUCKET
      - OPR_EXECUTOR_STORAGE_S3_ENDPOINT=$_APP_STORAGE_S3_ENDPOINT
      - OPR_EXECUTOR_STORAGE_DO_SPACES_ACCESS_KEY=$_APP_STORAGE_DO_SPACES_ACCESS_KEY
      - OPR_EXECUTOR_STORAGE_DO_SPACES_SECRET=$_APP_STORAGE_DO_SPACES_SECRET
      - OPR_EXECUTOR_STORAGE_DO_SPACES_REGION=$_APP_STORAGE_DO_SPACES_REGION
      - OPR_EXECUTOR_STORAGE_DO_SPACES_BUCKET=$_APP_STORAGE_DO_SPACES_BUCKET
      - OPR_EXECUTOR_STORAGE_BACKBLAZE_ACCESS_KEY=$_APP_STORAGE_BACKBLAZE_ACCESS_KEY
      - OPR_EXECUTOR_STORAGE_BACKBLAZE_SECRET=$_APP_STORAGE_BACKBLAZE_SECRET
      - OPR_EXECUTOR_STORAGE_BACKBLAZE_REGION=$_APP_STORAGE_BACKBLAZE_REGION
      - OPR_EXECUTOR_STORAGE_BACKBLAZE_BUCKET=$_APP_STORAGE_BACKBLAZE_BUCKET
      - OPR_EXECUTOR_STORAGE_LINODE_ACCESS_KEY=$_APP_STORAGE_LINODE_ACCESS_KEY
      - OPR_EXECUTOR_STORAGE_LINODE_SECRET=$_APP_STORAGE_LINODE_SECRET
      - OPR_EXECUTOR_STORAGE_LINODE_REGION=$_APP_STORAGE_LINODE_REGION
      - OPR_EXECUTOR_STORAGE_LINODE_BUCKET=$_APP_STORAGE_LINODE_BUCKET
      - OPR_EXECUTOR_STORAGE_WASABI_ACCESS_KEY=$_APP_STORAGE_WASABI_ACCESS_KEY
      - OPR_EXECUTOR_STORAGE_WASABI_SECRET=$_APP_STORAGE_WASABI_SECRET
      - OPR_EXECUTOR_STORAGE_WASABI_REGION=$_APP_STORAGE_WASABI_REGION
      - OPR_EXECUTOR_STORAGE_WASABI_BUCKET=$_APP_STORAGE_WASABI_BUCKET

  mariadb:
    image: mariadb:10.11 # fix issues when upgrading using: mysql_upgrade -u root -p
    <<: *x-logging
    restart: unless-stopped
    volumes:
      - appwrite-mariadb:/var/lib/mysql:rw
    environment:
      - MYSQL_ROOT_PASSWORD=${_APP_DB_ROOT_PASS}
      - MYSQL_DATABASE=${_APP_DB_SCHEMA}
      - MYSQL_USER=${_APP_DB_USER}
      - MYSQL_PASSWORD=${_APP_DB_PASS}
      - MARIADB_AUTO_UPGRADE=1
    command: "mysqld --innodb-flush-method=fsync"

  redis:
    image: redis:7.2.4-alpine
    <<: *x-logging
    restart: unless-stopped
    command: >
      redis-server
      --maxmemory            512mb
      --maxmemory-policy     allkeys-lru
      --maxmemory-samples    5
    volumes:
      - appwrite-redis:/data:rw

  # clamav:
  #   image: appwrite/clamav:1.2.0
  #   restart: unless-stopped
  #   volumes:
  #     - appwrite-uploads:/storage/uploads

volumes:
  appwrite-mariadb:
  appwrite-redis:
  appwrite-cache:
  appwrite-uploads:
  appwrite-imports:
  appwrite-certificates:
  appwrite-functions:
  appwrite-sites:
  appwrite-builds:
  appwrite-config:
```

```
[variables]
main_domain = "${domain}"
functions_domain = "functions.${main_domain}"
sites_domain = "sites.${main_domain}"
openssl_key = "${password:32}"
db_root_pw = "${password:32}"
db_user_pw = "${password:32}"
executor_secret = "${password:32}"

[config]
env = [
  "_APP_ENV=production",
  "_APP_LOCALE=en",
  "_APP_OPTIONS_ABUSE=enabled",
  "_APP_OPTIONS_FORCE_HTTPS=disabled",
  "_APP_OPTIONS_FUNCTIONS_FORCE_HTTPS=disabled",
  "_APP_OPTIONS_ROUTER_FORCE_HTTPS=disabled",
  "_APP_OPTIONS_ROUTER_PROTECTION=disabled",
  "_APP_OPENSSL_KEY_V1=${openssl_key}",
  "_APP_DOMAIN=${main_domain}",
  "_APP_CUSTOM_DOMAIN_DENY_LIST=example.com,test.com,app.example.com",
  "_APP_DOMAIN_FUNCTIONS=${functions_domain}",
  "_APP_DOMAIN_SITES=${sites_domain}",
  "_APP_DOMAIN_TARGET=localhost",
  "_APP_DOMAIN_TARGET_CNAME=localhost",
  "_APP_DOMAIN_TARGET_AAAA=::1",
  "_APP_DOMAIN_TARGET_A=127.0.0.1",
  "_APP_DOMAIN_TARGET_CAA=",
  "_APP_DNS=8.8.8.8",
  "_APP_CONSOLE_WHITELIST_ROOT=enabled",
  "_APP_CONSOLE_WHITELIST_EMAILS=",
  "_APP_CONSOLE_WHITELIST_IPS=",
  "_APP_CONSOLE_HOSTNAMES=",
  "_APP_SYSTEM_EMAIL_NAME=Appwrite",
  "[email protected]",
  "[email protected]",
  "_APP_SYSTEM_RESPONSE_FORMAT=",
  "[email protected]",
  "_APP_EMAIL_SECURITY=",
  "_APP_EMAIL_CERTIFICATES=",
  "_APP_USAGE_STATS=enabled",
  "_APP_LOGGING_PROVIDER=",
  "_APP_LOGGING_CONFIG=",
  "_APP_USAGE_AGGREGATION_INTERVAL=30",
  "_APP_USAGE_TIMESERIES_INTERVAL=30",
  "_APP_USAGE_DATABASE_INTERVAL=900",
  "_APP_WORKER_PER_CORE=6",
  "_APP_CONSOLE_SESSION_ALERTS=disabled",
  "_APP_COMPRESSION_ENABLED=enabled",
  "_APP_COMPRESSION_MIN_SIZE_BYTES=1024",
  "_APP_REDIS_HOST=redis",
  "_APP_REDIS_PORT=6379",
  "_APP_REDIS_USER=",
  "_APP_REDIS_PASS=",
  "_APP_DB_HOST=mariadb",
  "_APP_DB_PORT=3306",
  "_APP_DB_SCHEMA=appwrite",
  "_APP_DB_USER=user",
  "_APP_DB_PASS=${db_user_pw}",
  "_APP_DB_ROOT_PASS=${db_root_pw}",
  "_APP_INFLUXDB_HOST=influxdb",
  "_APP_INFLUXDB_PORT=8086",
  "_APP_STATSD_HOST=telegraf",
  "_APP_STATSD_PORT=8125",
  "_APP_SMTP_HOST=",
  "_APP_SMTP_PORT=",
  "_APP_SMTP_SECURE=",
  "_APP_SMTP_USERNAME=",
  "_APP_SMTP_PASSWORD=",
  "_APP_SMS_PROVIDER=",
  "_APP_SMS_FROM=",
  "_APP_STORAGE_LIMIT=30000000",
  "_APP_STORAGE_PREVIEW_LIMIT=20000000",
  "_APP_STORAGE_ANTIVIRUS=disabled",
  "_APP_STORAGE_ANTIVIRUS_HOST=clamav",
  "_APP_STORAGE_ANTIVIRUS_PORT=3310",
  "_APP_STORAGE_DEVICE=local",
  "_APP_STORAGE_S3_ACCESS_KEY=",
  "_APP_STORAGE_S3_SECRET=",
  "_APP_STORAGE_S3_REGION=us-east-1",
  "_APP_STORAGE_S3_BUCKET=",
  "_APP_STORAGE_S3_ENDPOINT=",
  "_APP_STORAGE_DO_SPACES_ACCESS_KEY=",
  "_APP_STORAGE_DO_SPACES_SECRET=",
  "_APP_STORAGE_DO_SPACES_REGION=us-east-1",
  "_APP_STORAGE_DO_SPACES_BUCKET=",
  "_APP_STORAGE_BACKBLAZE_ACCESS_KEY=",
  "_APP_STORAGE_BACKBLAZE_SECRET=",
  "_APP_STORAGE_BACKBLAZE_REGION=us-west-004",
  "_APP_STORAGE_BACKBLAZE_BUCKET=",
  "_APP_STORAGE_LINODE_ACCESS_KEY=",
  "_APP_STORAGE_LINODE_SECRET=",
  "_APP_STORAGE_LINODE_REGION=eu-central-1",
  "_APP_STORAGE_LINODE_BUCKET=",
  "_APP_STORAGE_WASABI_ACCESS_KEY=",
  "_APP_STORAGE_WASABI_SECRET=",
  "_APP_STORAGE_WASABI_REGION=eu-central-1",
  "_APP_STORAGE_WASABI_BUCKET=",
  "_APP_FUNCTIONS_SIZE_LIMIT=30000000",
  "_APP_COMPUTE_SIZE_LIMIT=30000000",
  "_APP_FUNCTIONS_BUILD_SIZE_LIMIT=2000000000",
  "_APP_FUNCTIONS_TIMEOUT=900",
  "_APP_FUNCTIONS_BUILD_TIMEOUT=900",
  "_APP_COMPUTE_BUILD_TIMEOUT=900",
  "_APP_FUNCTIONS_CONTAINERS=10",
  "_APP_FUNCTIONS_CPUS=0",
  "_APP_COMPUTE_CPUS=0",
  "_APP_FUNCTIONS_MEMORY=0",
  "_APP_COMPUTE_MEMORY=0",
  "_APP_FUNCTIONS_MEMORY_SWAP=0",
  "_APP_FUNCTIONS_RUNTIMES=node-16.0,php-8.0,python-3.9,ruby-3.0",
  "_APP_EXECUTOR_SECRET=${executor_secret}",
  "_APP_EXECUTOR_HOST=http://exc1/v1",
  "_APP_EXECUTOR_RUNTIME_NETWORK=appwrite_runtimes",
  "_APP_FUNCTIONS_ENVS=node-16.0,php-7.4,python-3.9,ruby-3.0",
  "_APP_FUNCTIONS_INACTIVE_THRESHOLD=60",
  "_APP_COMPUTE_INACTIVE_THRESHOLD=60",
  "DOCKERHUB_PULL_USERNAME=",
  "DOCKERHUB_PULL_PASSWORD=",
  "DOCKERHUB_PULL_EMAIL=",
  "OPEN_RUNTIMES_NETWORK=appwrite_runtimes",
  "_APP_FUNCTIONS_RUNTIMES_NETWORK=dokploy-network",
  "_APP_COMPUTE_RUNTIMES_NETWORK=dokploy-network",
  "_APP_DOCKER_HUB_USERNAME=",
  "_APP_DOCKER_HUB_PASSWORD=",
  "_APP_FUNCTIONS_MAINTENANCE_INTERVAL=3600",
  "_APP_COMPUTE_MAINTENANCE_INTERVAL=3600",
  "_APP_SITES_TIMEOUT=900",
  "_APP_SITES_RUNTIMES=static-1,node-22,flutter-3.29",
  "_APP_VCS_GITHUB_APP_NAME=",
  "_APP_VCS_GITHUB_PRIVATE_KEY=",
  "_APP_VCS_GITHUB_APP_ID=",
  "_APP_VCS_GITHUB_CLIENT_ID=",
  "_APP_VCS_GITHUB_CLIENT_SECRET=",
  "_APP_VCS_GITHUB_WEBHOOK_SECRET=",
  "_APP_MAINTENANCE_INTERVAL=86400",
  "_APP_MAINTENANCE_DELAY=0",
  "_APP_MAINTENANCE_START_TIME=00:00",
  "_APP_MAINTENANCE_RETENTION_CACHE=2592000",
  "_APP_MAINTENANCE_RETENTION_EXECUTION=1209600",
  "_APP_MAINTENANCE_RETENTION_AUDIT=1209600",
  "_APP_MAINTENANCE_RETENTION_AUDIT_CONSOLE=15778800",
  "_APP_MAINTENANCE_RETENTION_ABUSE=86400",
  "_APP_MAINTENANCE_RETENTION_USAGE_HOURLY=8640000",
  "_APP_MAINTENANCE_RETENTION_SCHEDULES=86400",
  "_APP_GRAPHQL_MAX_BATCH_SIZE=10",
  "_APP_GRAPHQL_MAX_COMPLEXITY=250",
  "_APP_GRAPHQL_MAX_DEPTH=3",
  "_APP_MIGRATIONS_FIREBASE_CLIENT_ID=",
  "_APP_MIGRATIONS_FIREBASE_CLIENT_SECRET=",
  "_APP_ASSISTANT_OPENAI_API_KEY=",
]
mounts = []

[[config.domains]]
serviceName = "appwrite"
port = 80
host = "${main_domain}"
path = "/"

[[config.domains]]
serviceName = "appwrite"
port = 80
host = "${sites_domain}"
path = "/"

[[config.domains]]
serviceName = "appwrite"
port = 80
host = "${functions_domain}"
path = "/"

[[config.domains]]
serviceName = "appwrite-console"
port = 80
host = "${main_domain}"
path = "/console"

[[config.domains]]
serviceName = "appwrite-realtime"
port = 80
host = "${main_domain}"
path = "/v1/realtime"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxueC1sb2dnaW5nOiAmeC1sb2dnaW5nXG4gIGxvZ2dpbmc6XG4gICAgZHJpdmVyOiBcImpzb24tZmlsZVwiXG4gICAgb3B0aW9uczpcbiAgICAgIG1heC1maWxlOiBcIjVcIlxuICAgICAgbWF4LXNpemU6IFwiMTBtXCJcbnNlcnZpY2VzOlxuICBhcHB3cml0ZTpcbiAgICBpbWFnZTogYXBwd3JpdGUvYXBwd3JpdGU6MS44LjBcbiAgICA8PDogKngtbG9nZ2luZ1xuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgbGFiZWxzOlxuICAgICAgLSB0cmFlZmlrLmVuYWJsZT10cnVlXG4gICAgICAtIHRyYWVmaWsuY29uc3RyYWludC1sYWJlbC1zdGFjaz1hcHB3cml0ZVxuICAgIHZvbHVtZXM6XG4gICAgICAtIGFwcHdyaXRlLXVwbG9hZHM6L3N0b3JhZ2UvdXBsb2Fkczpyd1xuICAgICAgLSBhcHB3cml0ZS1pbXBvcnRzOi9zdG9yYWdlL2ltcG9ydHM6cndcbiAgICAgIC0gYXBwd3JpdGUtY2FjaGU6L3N0b3JhZ2UvY2FjaGU6cndcbiAgICAgIC0gYXBwd3JpdGUtY29uZmlnOi9zdG9yYWdlL2NvbmZpZzpyd1xuICAgICAgLSBhcHB3cml0ZS1jZXJ0aWZpY2F0ZXM6L3N0b3JhZ2UvY2VydGlmaWNhdGVzOnJ3XG4gICAgICAtIGFwcHdyaXRlLWZ1bmN0aW9uczovc3RvcmFnZS9mdW5jdGlvbnM6cndcbiAgICAgIC0gYXBwd3JpdGUtc2l0ZXM6L3N0b3JhZ2Uvc2l0ZXM6cndcbiAgICAgIC0gYXBwd3JpdGUtYnVpbGRzOi9zdG9yYWdlL2J1aWxkczpyd1xuICAgIGRlcGVuZHNfb246XG4gICAgICAtIG1hcmlhZGJcbiAgICAgIC0gcmVkaXNcbiAgICAjICAgICAgLSBjbGFtYXZcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gX0FQUF9FTlZcbiAgICAgIC0gX0FQUF9XT1JLRVJfUEVSX0NPUkVcbiAgICAgIC0gX0FQUF9MT0NBTEVcbiAgICAgIC0gX0FQUF9DT01QUkVTU0lPTl9NSU5fU0laRV9CWVRFU1xuICAgICAgLSBfQVBQX0NPTlNPTEVfV0hJVEVMSVNUX1JPT1RcbiAgICAgIC0gX0FQUF9DT05TT0xFX1dISVRFTElTVF9FTUFJTFNcbiAgICAgIC0gX0FQUF9DT05TT0xFX1NFU1NJT05fQUxFUlRTXG4gICAgICAtIF9BUFBfQ09OU09MRV9XSElURUxJU1RfSVBTXG4gICAgICAtIF9BUFBfQ09OU09MRV9IT1NUTkFNRVNcbiAgICAgIC0gX0FQUF9TWVNURU1fRU1BSUxfTkFNRVxuICAgICAgLSBfQVBQX1NZU1RFTV9FTUFJTF9BRERSRVNTXG4gICAgICAtIF9BUFBfRU1BSUxfU0VDVVJJVFlcbiAgICAgIC0gX0FQUF9TWVNURU1fUkVTUE9OU0VfRk9STUFUXG4gICAgICAtIF9BUFBfT1BUSU9OU19BQlVTRVxuICAgICAgLSBfQVBQX09QVElPTlNfUk9VVEVSX1BST1RFQ1RJT05cbiAgICAgIC0gX0FQUF9PUFRJT05TX0ZPUkNFX0hUVFBTXG4gICAgICAtIF9BUFBfT1BUSU9OU19ST1VURVJfRk9SQ0VfSFRUUFNcbiAgICAgIC0gX0FQUF9PUEVOU1NMX0tFWV9WMVxuICAgICAgLSBfQVBQX0RPTUFJTlxuICAgICAgLSBfQVBQX0RPTUFJTl9UQVJHRVRfQ05BTUVcbiAgICAgIC0gX0FQUF9ET01BSU5fVEFSR0VUX0FBQUFcbiAgICAgIC0gX0FQUF9ET01BSU5fVEFSR0VUX0FcbiAgICAgIC0gX0FQUF9ET01BSU5fVEFSR0VUX0NBQVxuICAgICAgLSBfQVBQX0ROU1xuICAgICAgLSBfQVBQX0RPTUFJTl9GVU5DVElPTlNcbiAgICAgIC0gX0FQUF9SRURJU19IT1NUXG4gICAgICAtIF9BUFBfUkVESVNfUE9SVFxuICAgICAgLSBfQVBQX1JFRElTX1VTRVJcbiAgICAgIC0gX0FQUF9SRURJU19QQVNTXG4gICAgICAtIF9BUFBfREJfSE9TVFxuICAgICAgLSBfQVBQX0RCX1BPUlRcbiAgICAgIC0gX0FQUF9EQl9TQ0hFTUFcbiAgICAgIC0gX0FQUF9EQl9VU0VSXG4gICAgICAtIF9BUFBfREJfUEFTU1xuICAgICAgLSBfQVBQX1NNVFBfSE9TVFxuICAgICAgLSBfQVBQX1NNVFBfUE9SVFxuICAgICAgLSBfQVBQX1NNVFBfU0VDVVJFXG4gICAgICAtIF9BUFBfU01UUF9VU0VSTkFNRVxuICAgICAgLSBfQVBQX1NNVFBfUEFTU1dPUkRcbiAgICAgIC0gX0FQUF9VU0FHRV9TVEFUU1xuICAgICAgLSBfQVBQX1NUT1JBR0VfTElNSVRcbiAgICAgIC0gX0FQUF9TVE9SQUdFX1BSRVZJRVdfTElNSVRcbiAgICAgIC0gX0FQUF9TVE9SQUdFX0FOVElWSVJVU1xuICAgICAgLSBfQVBQX1NUT1JBR0VfQU5USVZJUlVTX0hPU1RcbiAgICAgIC0gX0FQUF9TVE9SQUdFX0FOVElWSVJVU19QT1JUXG4gICAgICAtIF9BUFBfU1RPUkFHRV9ERVZJQ0VcbiAgICAgIC0gX0FQUF9TVE9SQUdFX1MzX0FDQ0VTU19LRVlcbiAgICAgIC0gX0FQUF9TVE9SQUdFX1MzX1NFQ1JFVFxuICAgICAgLSBfQVBQX1NUT1JBR0VfUzNfUkVHSU9OXG4gICAgICAtIF9BUFBfU1RPUkFHRV9TM19CVUNLRVRcbiAgICAgIC0gX0FQUF9TVE9SQUdFX1MzX0VORFBPSU5UXG4gICAgICAtIF9BUFBfU1RPUkFHRV9ET19TUEFDRVNfQUNDRVNTX0tFWVxuICAgICAgLSBfQVBQX1NUT1JBR0VfRE9fU1BBQ0VTX1NFQ1JFVFxuICAgICAgLSBfQVBQX1NUT1JBR0VfRE9fU1BBQ0VTX1JFR0lPTlxuICAgICAgLSBfQVBQX1NUT1JBR0VfRE9fU1BBQ0VTX0JVQ0tFVFxuICAgICAgLSBfQVBQX1NUT1JBR0VfQkFDS0JMQVpFX0FDQ0VTU19LRVlcbiAgICAgIC0gX0FQUF9TVE9SQUdFX0JBQ0tCTEFaRV9TRUNSRVRcbiAgICAgIC0gX0FQUF9TVE9SQUdFX0JBQ0tCTEFaRV9SRUdJT05cbiAgICAgIC0gX0FQUF9TVE9SQUdFX0JBQ0tCTEFaRV9CVUNLRVRcbiAgICAgIC0gX0FQUF9TVE9SQUdFX0xJTk9ERV9BQ0NFU1NfS0VZXG4gICAgICAtIF9BUFBfU1RPUkFHRV9MSU5PREVfU0VDUkVUXG4gICAgICAtIF9BUFBfU1RPUkFHRV9MSU5PREVfUkVHSU9OXG4gICAgICAtIF9BUFBfU1RPUkFHRV9MSU5PREVfQlVDS0VUXG4gICAgICAtIF9BUFBfU1RPUkFHRV9XQVNBQklfQUNDRVNTX0tFWVxuICAgICAgLSBfQVBQX1NUT1JBR0VfV0FTQUJJX1NFQ1JFVFxuICAgICAgLSBfQVBQX1NUT1JBR0VfV0FTQUJJX1JFR0lPTlxuICAgICAgLSBfQVBQX1NUT1JBR0VfV0FTQUJJX0JVQ0tFVFxuICAgICAgLSBfQVBQX0NPTVBVVEVfU0laRV9MSU1JVFxuICAgICAgLSBfQVBQX0ZVTkNUSU9OU19USU1FT1VUXG4gICAgICAtIF9BUFBfU0lURVNfVElNRU9VVFxuICAgICAgLSBfQVBQX0NPTVBVVEVfQlVJTERfVElNRU9VVFxuICAgICAgLSBfQVBQX0NPTVBVVEVfQ1BVU1xuICAgICAgLSBfQVBQX0NPTVBVVEVfTUVNT1JZXG4gICAgICAtIF9BUFBfRlVOQ1RJT05TX1JVTlRJTUVTXG4gICAgICAtIF9BUFBfU0lURVNfUlVOVElNRVNcbiAgICAgIC0gX0FQUF9ET01BSU5fU0lURVNcbiAgICAgIC0gX0FQUF9FWEVDVVRPUl9TRUNSRVRcbiAgICAgIC0gX0FQUF9FWEVDVVRPUl9IT1NUXG4gICAgICAtIF9BUFBfTE9HR0lOR19DT05GSUdcbiAgICAgIC0gX0FQUF9NQUlOVEVOQU5DRV9JTlRFUlZBTFxuICAgICAgLSBfQVBQX01BSU5URU5BTkNFX0RFTEFZXG4gICAgICAtIF9BUFBfTUFJTlRFTkFOQ0VfU1RBUlRfVElNRVxuICAgICAgLSBfQVBQX01BSU5URU5BTkNFX1JFVEVOVElPTl9FWEVDVVRJT05cbiAgICAgIC0gX0FQUF9NQUlOVEVOQU5DRV9SRVRFTlRJT05fQ0FDSEVcbiAgICAgIC0gX0FQUF9NQUlOVEVOQU5DRV9SRVRFTlRJT05fQUJVU0VcbiAgICAgIC0gX0FQUF9NQUlOVEVOQU5DRV9SRVRFTlRJT05fQVVESVRcbiAgICAgIC0gX0FQUF9NQUlOVEVOQU5DRV9SRVRFTlRJT05fQVVESVRfQ09OU09MRVxuICAgICAgLSBfQVBQX01BSU5URU5BTkNFX1JFVEVOVElPTl9VU0FHRV9IT1VSTFlcbiAgICAgIC0gX0FQUF9NQUlOVEVOQU5DRV9SRVRFTlRJT05fU0NIRURVTEVTXG4gICAgICAtIF9BUFBfU01TX1BST1ZJREVSXG4gICAgICAtIF9BUFBfU01TX0ZST01cbiAgICAgIC0gX0FQUF9HUkFQSFFMX01BWF9CQVRDSF9TSVpFXG4gICAgICAtIF9BUFBfR1JBUEhRTF9NQVhfQ09NUExFWElUWVxuICAgICAgLSBfQVBQX0dSQVBIUUxfTUFYX0RFUFRIXG4gICAgICAtIF9BUFBfVkNTX0dJVEhVQl9BUFBfTkFNRVxuICAgICAgLSBfQVBQX1ZDU19HSVRIVUJfUFJJVkFURV9LRVlcbiAgICAgIC0gX0FQUF9WQ1NfR0lUSFVCX0FQUF9JRFxuICAgICAgLSBfQVBQX1ZDU19HSVRIVUJfV0VCSE9PS19TRUNSRVRcbiAgICAgIC0gX0FQUF9WQ1NfR0lUSFVCX0NMSUVOVF9TRUNSRVRcbiAgICAgIC0gX0FQUF9WQ1NfR0lUSFVCX0NMSUVOVF9JRFxuICAgICAgLSBfQVBQX01JR1JBVElPTlNfRklSRUJBU0VfQ0xJRU5UX0lEXG4gICAgICAtIF9BUFBfTUlHUkFUSU9OU19GSVJFQkFTRV9DTElFTlRfU0VDUkVUXG4gICAgICAtIF9BUFBfQVNTSVNUQU5UX09QRU5BSV9BUElfS0VZXG4gIGFwcHdyaXRlLWNvbnNvbGU6XG4gICAgPDw6ICp4LWxvZ2dpbmdcbiAgICBpbWFnZTogYXBwd3JpdGUvY29uc29sZTo3LjQuN1xuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgbGFiZWxzOlxuICAgICAgLSBcInRyYWVmaWsuZW5hYmxlPXRydWVcIlxuICAgICAgLSBcInRyYWVmaWsuY29uc3RyYWludC1sYWJlbC1zdGFjaz1hcHB3cml0ZVwiXG5cbiAgYXBwd3JpdGUtcmVhbHRpbWU6XG4gICAgaW1hZ2U6IGFwcHdyaXRlL2FwcHdyaXRlOjEuOC4wXG4gICAgZW50cnlwb2ludDogcmVhbHRpbWVcbiAgICA8PDogKngtbG9nZ2luZ1xuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgbGFiZWxzOlxuICAgICAgLSBcInRyYWVmaWsuZW5hYmxlPXRydWVcIlxuICAgICAgLSBcInRyYWVmaWsuY29uc3RyYWludC1sYWJlbC1zdGFjaz1hcHB3cml0ZVwiXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIC0gbWFyaWFkYlxuICAgICAgLSByZWRpc1xuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBfQVBQX0VOVlxuICAgICAgLSBfQVBQX1dPUktFUl9QRVJfQ09SRVxuICAgICAgLSBfQVBQX09QVElPTlNfQUJVU0VcbiAgICAgIC0gX0FQUF9PUFRJT05TX1JPVVRFUl9QUk9URUNUSU9OXG4gICAgICAtIF9BUFBfT1BFTlNTTF9LRVlfVjFcbiAgICAgIC0gX0FQUF9SRURJU19IT1NUXG4gICAgICAtIF9BUFBfUkVESVNfUE9SVFxuICAgICAgLSBfQVBQX1JFRElTX1VTRVJcbiAgICAgIC0gX0FQUF9SRURJU19QQVNTXG4gICAgICAtIF9BUFBfREJfSE9TVFxuICAgICAgLSBfQVBQX0RCX1BPUlRcbiAgICAgIC0gX0FQUF9EQl9TQ0hFTUFcbiAgICAgIC0gX0FQUF9EQl9VU0VSXG4gICAgICAtIF9BUFBfREJfUEFTU1xuICAgICAgLSBfQVBQX1VTQUdFX1NUQVRTXG4gICAgICAtIF9BUFBfTE9HR0lOR19DT05GSUdcblxuICBhcHB3cml0ZS13b3JrZXItYXVkaXRzOlxuICAgIGltYWdlOiBhcHB3cml0ZS9hcHB3cml0ZToxLjguMFxuICAgIGVudHJ5cG9pbnQ6IHdvcmtlci1hdWRpdHNcbiAgICA8PDogKngtbG9nZ2luZ1xuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIC0gcmVkaXNcbiAgICAgIC0gbWFyaWFkYlxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBfQVBQX0VOVlxuICAgICAgLSBfQVBQX1dPUktFUl9QRVJfQ09SRVxuICAgICAgLSBfQVBQX09QRU5TU0xfS0VZX1YxXG4gICAgICAtIF9BUFBfUkVESVNfSE9TVFxuICAgICAgLSBfQVBQX1JFRElTX1BPUlRcbiAgICAgIC0gX0FQUF9SRURJU19VU0VSXG4gICAgICAtIF9BUFBfUkVESVNfUEFTU1xuICAgICAgLSBfQVBQX0RCX0hPU1RcbiAgICAgIC0gX0FQUF9EQl9QT1JUXG4gICAgICAtIF9BUFBfREJfU0NIRU1BXG4gICAgICAtIF9BUFBfREJfVVNFUlxuICAgICAgLSBfQVBQX0RCX1BBU1NcbiAgICAgIC0gX0FQUF9MT0dHSU5HX0NPTkZJR1xuXG4gIGFwcHdyaXRlLXdvcmtlci13ZWJob29rczpcbiAgICBpbWFnZTogYXBwd3JpdGUvYXBwd3JpdGU6MS44LjBcbiAgICBlbnRyeXBvaW50OiB3b3JrZXItd2ViaG9va3NcbiAgICA8PDogKngtbG9nZ2luZ1xuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIC0gcmVkaXNcbiAgICAgIC0gbWFyaWFkYlxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBfQVBQX0VOVlxuICAgICAgLSBfQVBQX1dPUktFUl9QRVJfQ09SRVxuICAgICAgLSBfQVBQX09QRU5TU0xfS0VZX1YxXG4gICAgICAtIF9BUFBfRU1BSUxfU0VDVVJJVFlcbiAgICAgIC0gX0FQUF9TWVNURU1fU0VDVVJJVFlfRU1BSUxfQUREUkVTU1xuICAgICAgLSBfQVBQX0RCX0hPU1RcbiAgICAgIC0gX0FQUF9EQl9QT1JUXG4gICAgICAtIF9BUFBfREJfU0NIRU1BXG4gICAgICAtIF9BUFBfREJfVVNFUlxuICAgICAgLSBfQVBQX0RCX1BBU1NcbiAgICAgIC0gX0FQUF9SRURJU19IT1NUXG4gICAgICAtIF9BUFBfUkVESVNfUE9SVFxuICAgICAgLSBfQVBQX1JFRElTX1VTRVJcbiAgICAgIC0gX0FQUF9SRURJU19QQVNTXG4gICAgICAtIF9BUFBfTE9HR0lOR19DT05GSUdcblxuICBhcHB3cml0ZS13b3JrZXItZGVsZXRlczpcbiAgICBpbWFnZTogYXBwd3JpdGUvYXBwd3JpdGU6MS44LjBcbiAgICBlbnRyeXBvaW50OiB3b3JrZXItZGVsZXRlc1xuICAgIDw8OiAqeC1sb2dnaW5nXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBkZXBlbmRzX29uOlxuICAgICAgLSByZWRpc1xuICAgICAgLSBtYXJpYWRiXG4gICAgdm9sdW1lczpcbiAgICAgIC0gYXBwd3JpdGUtdXBsb2Fkczovc3RvcmFnZS91cGxvYWRzOnJ3XG4gICAgICAtIGFwcHdyaXRlLWNhY2hlOi9zdG9yYWdlL2NhY2hlOnJ3XG4gICAgICAtIGFwcHdyaXRlLWZ1bmN0aW9uczovc3RvcmFnZS9mdW5jdGlvbnM6cndcbiAgICAgIC0gYXBwd3JpdGUtc2l0ZXM6L3N0b3JhZ2Uvc2l0ZXM6cndcbiAgICAgIC0gYXBwd3JpdGUtYnVpbGRzOi9zdG9yYWdlL2J1aWxkczpyd1xuICAgICAgLSBhcHB3cml0ZS1jZXJ0aWZpY2F0ZXM6L3N0b3JhZ2UvY2VydGlmaWNhdGVzOnJ3XG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIF9BUFBfRU5WXG4gICAgICAtIF9BUFBfV09SS0VSX1BFUl9DT1JFXG4gICAgICAtIF9BUFBfT1BFTlNTTF9LRVlfVjFcbiAgICAgIC0gX0FQUF9SRURJU19IT1NUXG4gICAgICAtIF9BUFBfUkVESVNfUE9SVFxuICAgICAgLSBfQVBQX1JFRElTX1VTRVJcbiAgICAgIC0gX0FQUF9SRURJU19QQVNTXG4gICAgICAtIF9BUFBfREJfSE9TVFxuICAgICAgLSBfQVBQX0RCX1BPUlRcbiAgICAgIC0gX0FQUF9EQl9TQ0hFTUFcbiAgICAgIC0gX0FQUF9EQl9VU0VSXG4gICAgICAtIF9BUFBfREJfUEFTU1xuICAgICAgLSBfQVBQX1NUT1JBR0VfREVWSUNFXG4gICAgICAtIF9BUFBfU1RPUkFHRV9TM19BQ0NFU1NfS0VZXG4gICAgICAtIF9BUFBfU1RPUkFHRV9TM19TRUNSRVRcbiAgICAgIC0gX0FQUF9TVE9SQUdFX1MzX1JFR0lPTlxuICAgICAgLSBfQVBQX1NUT1JBR0VfUzNfQlVDS0VUXG4gICAgICAtIF9BUFBfU1RPUkFHRV9TM19FTkRQT0lOVFxuICAgICAgLSBfQVBQX1NUT1JBR0VfRE9fU1BBQ0VTX0FDQ0VTU19LRVlcbiAgICAgIC0gX0FQUF9TVE9SQUdFX0RPX1NQQUNFU19TRUNSRVRcbiAgICAgIC0gX0FQUF9TVE9SQUdFX0RPX1NQQUNFU19SRUdJT05cbiAgICAgIC0gX0FQUF9TVE9SQUdFX0RPX1NQQUNFU19CVUNLRVRcbiAgICAgIC0gX0FQUF9TVE9SQUdFX0JBQ0tCTEFaRV9BQ0NFU1NfS0VZXG4gICAgICAtIF9BUFBfU1RPUkFHRV9CQUNLQkxBWkVfU0VDUkVUXG4gICAgICAtIF9BUFBfU1RPUkFHRV9CQUNLQkxBWkVfUkVHSU9OXG4gICAgICAtIF9BUFBfU1RPUkFHRV9CQUNLQkxBWkVfQlVDS0VUXG4gICAgICAtIF9BUFBfU1RPUkFHRV9MSU5PREVfQUNDRVNTX0tFWVxuICAgICAgLSBfQVBQX1NUT1JBR0VfTElOT0RFX1NFQ1JFVFxuICAgICAgLSBfQVBQX1NUT1JBR0VfTElOT0RFX1JFR0lPTlxuICAgICAgLSBfQVBQX1NUT1JBR0VfTElOT0RFX0JVQ0tFVFxuICAgICAgLSBfQVBQX1NUT1JBR0VfV0FTQUJJX0FDQ0VTU19LRVlcbiAgICAgIC0gX0FQUF9TVE9SQUdFX1dBU0FCSV9TRUNSRVRcbiAgICAgIC0gX0FQUF9TVE9SQUdFX1dBU0FCSV9SRUdJT05cbiAgICAgIC0gX0FQUF9TVE9SQUdFX1dBU0FCSV9CVUNLRVRcbiAgICAgIC0gX0FQUF9MT0dHSU5HX0NPTkZJR1xuICAgICAgLSBfQVBQX0VYRUNVVE9SX1NFQ1JFVFxuICAgICAgLSBfQVBQX0VYRUNVVE9SX0hPU1RcbiAgICAgIC0gX0FQUF9NQUlOVEVOQU5DRV9SRVRFTlRJT05fQUJVU0VcbiAgICAgIC0gX0FQUF9NQUlOVEVOQU5DRV9SRVRFTlRJT05fQVVESVRcbiAgICAgIC0gX0FQUF9NQUlOVEVOQU5DRV9SRVRFTlRJT05fQVVESVRfQ09OU09MRVxuICAgICAgLSBfQVBQX01BSU5URU5BTkNFX1JFVEVOVElPTl9FWEVDVVRJT05cbiAgICAgIC0gX0FQUF9TWVNURU1fU0VDVVJJVFlfRU1BSUxfQUREUkVTU1xuICAgICAgLSBfQVBQX0VNQUlMX0NFUlRJRklDQVRFU1xuXG4gIGFwcHdyaXRlLXdvcmtlci1kYXRhYmFzZXM6XG4gICAgaW1hZ2U6IGFwcHdyaXRlL2FwcHdyaXRlOjEuOC4wXG4gICAgZW50cnlwb2ludDogd29ya2VyLWRhdGFiYXNlc1xuICAgIDw8OiAqeC1sb2dnaW5nXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBkZXBlbmRzX29uOlxuICAgICAgLSByZWRpc1xuICAgICAgLSBtYXJpYWRiXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIF9BUFBfRU5WXG4gICAgICAtIF9BUFBfV09SS0VSX1BFUl9DT1JFXG4gICAgICAtIF9BUFBfT1BFTlNTTF9LRVlfVjFcbiAgICAgIC0gX0FQUF9SRURJU19IT1NUXG4gICAgICAtIF9BUFBfUkVESVNfUE9SVFxuICAgICAgLSBfQVBQX1JFRElTX1VTRVJcbiAgICAgIC0gX0FQUF9SRURJU19QQVNTXG4gICAgICAtIF9BUFBfREJfSE9TVFxuICAgICAgLSBfQVBQX0RCX1BPUlRcbiAgICAgIC0gX0FQUF9EQl9TQ0hFTUFcbiAgICAgIC0gX0FQUF9EQl9VU0VSXG4gICAgICAtIF9BUFBfREJfUEFTU1xuICAgICAgLSBfQVBQX0xPR0dJTkdfQ09ORklHXG5cbiAgYXBwd3JpdGUtd29ya2VyLWJ1aWxkczpcbiAgICBpbWFnZTogYXBwd3JpdGUvYXBwd3JpdGU6MS44LjBcbiAgICBlbnRyeXBvaW50OiB3b3JrZXItYnVpbGRzXG4gICAgPDw6ICp4LWxvZ2dpbmdcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGRlcGVuZHNfb246XG4gICAgICAtIHJlZGlzXG4gICAgICAtIG1hcmlhZGJcbiAgICB2b2x1bWVzOlxuICAgICAgLSBhcHB3cml0ZS1mdW5jdGlvbnM6L3N0b3JhZ2UvZnVuY3Rpb25zOnJ3XG4gICAgICAtIGFwcHdyaXRlLXNpdGVzOi9zdG9yYWdlL3NpdGVzOnJ3XG4gICAgICAtIGFwcHdyaXRlLWJ1aWxkczovc3RvcmFnZS9idWlsZHM6cndcbiAgICAgIC0gYXBwd3JpdGUtdXBsb2Fkczovc3RvcmFnZS91cGxvYWRzOnJ3XG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIF9BUFBfRU5WXG4gICAgICAtIF9BUFBfV09SS0VSX1BFUl9DT1JFXG4gICAgICAtIF9BUFBfT1BFTlNTTF9LRVlfVjFcbiAgICAgIC0gX0FQUF9FWEVDVVRPUl9TRUNSRVRcbiAgICAgIC0gX0FQUF9FWEVDVVRPUl9IT1NUXG4gICAgICAtIF9BUFBfUkVESVNfSE9TVFxuICAgICAgLSBfQVBQX1JFRElTX1BPUlRcbiAgICAgIC0gX0FQUF9SRURJU19VU0VSXG4gICAgICAtIF9BUFBfUkVESVNfUEFTU1xuICAgICAgLSBfQVBQX0RCX0hPU1RcbiAgICAgIC0gX0FQUF9EQl9QT1JUXG4gICAgICAtIF9BUFBfREJfU0NIRU1BXG4gICAgICAtIF9BUFBfREJfVVNFUlxuICAgICAgLSBfQVBQX0RCX1BBU1NcbiAgICAgIC0gX0FQUF9MT0dHSU5HX0NPTkZJR1xuICAgICAgLSBfQVBQX1ZDU19HSVRIVUJfQVBQX05BTUVcbiAgICAgIC0gX0FQUF9WQ1NfR0lUSFVCX1BSSVZBVEVfS0VZXG4gICAgICAtIF9BUFBfVkNTX0dJVEhVQl9BUFBfSURcbiAgICAgIC0gX0FQUF9GVU5DVElPTlNfVElNRU9VVFxuICAgICAgLSBfQVBQX1NJVEVTX1RJTUVPVVRcbiAgICAgIC0gX0FQUF9DT01QVVRFX0JVSUxEX1RJTUVPVVRcbiAgICAgIC0gX0FQUF9DT01QVVRFX0NQVVNcbiAgICAgIC0gX0FQUF9DT01QVVRFX01FTU9SWVxuICAgICAgLSBfQVBQX0NPTVBVVEVfU0laRV9MSU1JVFxuICAgICAgLSBfQVBQX09QVElPTlNfRk9SQ0VfSFRUUFNcbiAgICAgIC0gX0FQUF9PUFRJT05TX1JPVVRFUl9GT1JDRV9IVFRQU1xuICAgICAgLSBfQVBQX0RPTUFJTlxuICAgICAgLSBfQVBQX1NUT1JBR0VfREVWSUNFXG4gICAgICAtIF9BUFBfU1RPUkFHRV9TM19BQ0NFU1NfS0VZXG4gICAgICAtIF9BUFBfU1RPUkFHRV9TM19TRUNSRVRcbiAgICAgIC0gX0FQUF9TVE9SQUdFX1MzX1JFR0lPTlxuICAgICAgLSBfQVBQX1NUT1JBR0VfUzNfQlVDS0VUXG4gICAgICAtIF9BUFBfU1RPUkFHRV9TM19FTkRQT0lOVFxuICAgICAgLSBfQVBQX1NUT1JBR0VfRE9fU1BBQ0VTX0FDQ0VTU19LRVlcbiAgICAgIC0gX0FQUF9TVE9SQUdFX0RPX1NQQUNFU19TRUNSRVRcbiAgICAgIC0gX0FQUF9TVE9SQUdFX0RPX1NQQUNFU19SRUdJT05cbiAgICAgIC0gX0FQUF9TVE9SQUdFX0RPX1NQQUNFU19CVUNLRVRcbiAgICAgIC0gX0FQUF9TVE9SQUdFX0JBQ0tCTEFaRV9BQ0NFU1NfS0VZXG4gICAgICAtIF9BUFBfU1RPUkFHRV9CQUNLQkxBWkVfU0VDUkVUXG4gICAgICAtIF9BUFBfU1RPUkFHRV9CQUNLQkxBWkVfUkVHSU9OXG4gICAgICAtIF9BUFBfU1RPUkFHRV9CQUNLQkxBWkVfQlVDS0VUXG4gICAgICAtIF9BUFBfU1RPUkFHRV9MSU5PREVfQUNDRVNTX0tFWVxuICAgICAgLSBfQVBQX1NUT1JBR0VfTElOT0RFX1NFQ1JFVFxuICAgICAgLSBfQVBQX1NUT1JBR0VfTElOT0RFX1JFR0lPTlxuICAgICAgLSBfQVBQX1NUT1JBR0VfTElOT0RFX0JVQ0tFVFxuICAgICAgLSBfQVBQX1NUT1JBR0VfV0FTQUJJX0FDQ0VTU19LRVlcbiAgICAgIC0gX0FQUF9TVE9SQUdFX1dBU0FCSV9TRUNSRVRcbiAgICAgIC0gX0FQUF9TVE9SQUdFX1dBU0FCSV9SRUdJT05cbiAgICAgIC0gX0FQUF9TVE9SQUdFX1dBU0FCSV9CVUNLRVRcbiAgICAgIC0gX0FQUF9ET01BSU5fU0lURVNcblxuICBhcHB3cml0ZS13b3JrZXItY2VydGlmaWNhdGVzOlxuICAgIGltYWdlOiBhcHB3cml0ZS9hcHB3cml0ZToxLjguMFxuICAgIGVudHJ5cG9pbnQ6IHdvcmtlci1jZXJ0aWZpY2F0ZXNcbiAgICA8PDogKngtbG9nZ2luZ1xuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIC0gcmVkaXNcbiAgICAgIC0gbWFyaWFkYlxuICAgIHZvbHVtZXM6XG4gICAgICAtIGFwcHdyaXRlLWNvbmZpZzovc3RvcmFnZS9jb25maWc6cndcbiAgICAgIC0gYXBwd3JpdGUtY2VydGlmaWNhdGVzOi9zdG9yYWdlL2NlcnRpZmljYXRlczpyd1xuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBfQVBQX0VOVlxuICAgICAgLSBfQVBQX1dPUktFUl9QRVJfQ09SRVxuICAgICAgLSBfQVBQX09QRU5TU0xfS0VZX1YxXG4gICAgICAtIF9BUFBfRE9NQUlOXG4gICAgICAtIF9BUFBfRE9NQUlOX1RBUkdFVF9DTkFNRVxuICAgICAgLSBfQVBQX0RPTUFJTl9UQVJHRVRfQUFBQVxuICAgICAgLSBfQVBQX0RPTUFJTl9UQVJHRVRfQVxuICAgICAgLSBfQVBQX0RPTUFJTl9UQVJHRVRfQ0FBXG4gICAgICAtIF9BUFBfRE5TXG4gICAgICAtIF9BUFBfRE9NQUlOX0ZVTkNUSU9OU1xuICAgICAgLSBfQVBQX0VNQUlMX0NFUlRJRklDQVRFU1xuICAgICAgLSBfQVBQX1JFRElTX0hPU1RcbiAgICAgIC0gX0FQUF9SRURJU19QT1JUXG4gICAgICAtIF9BUFBfUkVESVNfVVNFUlxuICAgICAgLSBfQVBQX1JFRElTX1BBU1NcbiAgICAgIC0gX0FQUF9EQl9IT1NUXG4gICAgICAtIF9BUFBfREJfUE9SVFxuICAgICAgLSBfQVBQX0RCX1NDSEVNQVxuICAgICAgLSBfQVBQX0RCX1VTRVJcbiAgICAgIC0gX0FQUF9EQl9QQVNTXG4gICAgICAtIF9BUFBfTE9HR0lOR19DT05GSUdcblxuICBhcHB3cml0ZS13b3JrZXItZnVuY3Rpb25zOlxuICAgIGltYWdlOiBhcHB3cml0ZS9hcHB3cml0ZToxLjguMFxuICAgIGVudHJ5cG9pbnQ6IHdvcmtlci1mdW5jdGlvbnNcbiAgICA8PDogKngtbG9nZ2luZ1xuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIC0gcmVkaXNcbiAgICAgIC0gbWFyaWFkYlxuICAgICAgLSBvcGVucnVudGltZXMtZXhlY3V0b3JcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gX0FQUF9FTlZcbiAgICAgIC0gX0FQUF9XT1JLRVJfUEVSX0NPUkVcbiAgICAgIC0gX0FQUF9PUEVOU1NMX0tFWV9WMVxuICAgICAgLSBfQVBQX0RPTUFJTlxuICAgICAgLSBfQVBQX09QVElPTlNfRk9SQ0VfSFRUUFNcbiAgICAgIC0gX0FQUF9SRURJU19IT1NUXG4gICAgICAtIF9BUFBfUkVESVNfUE9SVFxuICAgICAgLSBfQVBQX1JFRElTX1VTRVJcbiAgICAgIC0gX0FQUF9SRURJU19QQVNTXG4gICAgICAtIF9BUFBfREJfSE9TVFxuICAgICAgLSBfQVBQX0RCX1BPUlRcbiAgICAgIC0gX0FQUF9EQl9TQ0hFTUFcbiAgICAgIC0gX0FQUF9EQl9VU0VSXG4gICAgICAtIF9BUFBfREJfUEFTU1xuICAgICAgLSBfQVBQX0ZVTkNUSU9OU19USU1FT1VUXG4gICAgICAtIF9BUFBfU0lURVNfVElNRU9VVFxuICAgICAgLSBfQVBQX0NPTVBVVEVfQlVJTERfVElNRU9VVFxuICAgICAgLSBfQVBQX0NPTVBVVEVfQ1BVU1xuICAgICAgLSBfQVBQX0NPTVBVVEVfTUVNT1JZXG4gICAgICAtIF9BUFBfRVhFQ1VUT1JfU0VDUkVUXG4gICAgICAtIF9BUFBfRVhFQ1VUT1JfSE9TVFxuICAgICAgLSBfQVBQX1VTQUdFX1NUQVRTXG4gICAgICAtIF9BUFBfRE9DS0VSX0hVQl9VU0VSTkFNRVxuICAgICAgLSBfQVBQX0RPQ0tFUl9IVUJfUEFTU1dPUkRcbiAgICAgIC0gX0FQUF9MT0dHSU5HX0NPTkZJR1xuXG4gIGFwcHdyaXRlLXdvcmtlci1tYWlsczpcbiAgICBpbWFnZTogYXBwd3JpdGUvYXBwd3JpdGU6MS44LjBcbiAgICBlbnRyeXBvaW50OiB3b3JrZXItbWFpbHNcbiAgICA8PDogKngtbG9nZ2luZ1xuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIC0gcmVkaXNcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gX0FQUF9FTlZcbiAgICAgIC0gX0FQUF9XT1JLRVJfUEVSX0NPUkVcbiAgICAgIC0gX0FQUF9PUEVOU1NMX0tFWV9WMVxuICAgICAgLSBfQVBQX1NZU1RFTV9FTUFJTF9OQU1FXG4gICAgICAtIF9BUFBfU1lTVEVNX0VNQUlMX0FERFJFU1NcbiAgICAgIC0gX0FQUF9EQl9IT1NUXG4gICAgICAtIF9BUFBfREJfUE9SVFxuICAgICAgLSBfQVBQX0RCX1NDSEVNQVxuICAgICAgLSBfQVBQX0RCX1VTRVJcbiAgICAgIC0gX0FQUF9EQl9QQVNTXG4gICAgICAtIF9BUFBfUkVESVNfSE9TVFxuICAgICAgLSBfQVBQX1JFRElTX1BPUlRcbiAgICAgIC0gX0FQUF9SRURJU19VU0VSXG4gICAgICAtIF9BUFBfUkVESVNfUEFTU1xuICAgICAgLSBfQVBQX1NNVFBfSE9TVFxuICAgICAgLSBfQVBQX1NNVFBfUE9SVFxuICAgICAgLSBfQVBQX1NNVFBfU0VDVVJFXG4gICAgICAtIF9BUFBfU01UUF9VU0VSTkFNRVxuICAgICAgLSBfQVBQX1NNVFBfUEFTU1dPUkRcbiAgICAgIC0gX0FQUF9MT0dHSU5HX0NPTkZJR1xuICAgICAgLSBfQVBQX0RPTUFJTlxuICAgICAgLSBfQVBQX09QVElPTlNfRk9SQ0VfSFRUUFNcblxuICBhcHB3cml0ZS13b3JrZXItbWVzc2FnaW5nOlxuICAgIGltYWdlOiBhcHB3cml0ZS9hcHB3cml0ZToxLjguMFxuICAgIGVudHJ5cG9pbnQ6IHdvcmtlci1tZXNzYWdpbmdcbiAgICA8PDogKngtbG9nZ2luZ1xuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgdm9sdW1lczpcbiAgICAgIC0gYXBwd3JpdGUtdXBsb2Fkczovc3RvcmFnZS91cGxvYWRzOnJ3XG4gICAgZGVwZW5kc19vbjpcbiAgICAgIC0gcmVkaXNcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gX0FQUF9FTlZcbiAgICAgIC0gX0FQUF9XT1JLRVJfUEVSX0NPUkVcbiAgICAgIC0gX0FQUF9PUEVOU1NMX0tFWV9WMVxuICAgICAgLSBfQVBQX1JFRElTX0hPU1RcbiAgICAgIC0gX0FQUF9SRURJU19QT1JUXG4gICAgICAtIF9BUFBfUkVESVNfVVNFUlxuICAgICAgLSBfQVBQX1JFRElTX1BBU1NcbiAgICAgIC0gX0FQUF9EQl9IT1NUXG4gICAgICAtIF9BUFBfREJfUE9SVFxuICAgICAgLSBfQVBQX0RCX1NDSEVNQVxuICAgICAgLSBfQVBQX0RCX1VTRVJcbiAgICAgIC0gX0FQUF9EQl9QQVNTXG4gICAgICAtIF9BUFBfTE9HR0lOR19DT05GSUdcbiAgICAgIC0gX0FQUF9TTVNfRlJPTVxuICAgICAgLSBfQVBQX1NNU19QUk9WSURFUlxuICAgICAgLSBfQVBQX1NUT1JBR0VfREVWSUNFXG4gICAgICAtIF9BUFBfU1RPUkFHRV9TM19BQ0NFU1NfS0VZXG4gICAgICAtIF9BUFBfU1RPUkFHRV9TM19TRUNSRVRcbiAgICAgIC0gX0FQUF9TVE9SQUdFX1MzX1JFR0lPTlxuICAgICAgLSBfQVBQX1NUT1JBR0VfUzNfQlVDS0VUXG4gICAgICAtIF9BUFBfU1RPUkFHRV9TM19FTkRQT0lOVFxuICAgICAgLSBfQVBQX1NUT1JBR0VfRE9fU1BBQ0VTX0FDQ0VTU19LRVlcbiAgICAgIC0gX0FQUF9TVE9SQUdFX0RPX1NQQUNFU19TRUNSRVRcbiAgICAgIC0gX0FQUF9TVE9SQUdFX0RPX1NQQUNFU19SRUdJT05cbiAgICAgIC0gX0FQUF9TVE9SQUdFX0RPX1NQQUNFU19CVUNLRVRcbiAgICAgIC0gX0FQUF9TVE9SQUdFX0JBQ0tCTEFaRV9BQ0NFU1NfS0VZXG4gICAgICAtIF9BUFBfU1RPUkFHRV9CQUNLQkxBWkVfU0VDUkVUXG4gICAgICAtIF9BUFBfU1RPUkFHRV9CQUNLQkxBWkVfUkVHSU9OXG4gICAgICAtIF9BUFBfU1RPUkFHRV9CQUNLQkxBWkVfQlVDS0VUXG4gICAgICAtIF9BUFBfU1RPUkFHRV9MSU5PREVfQUNDRVNTX0tFWVxuICAgICAgLSBfQVBQX1NUT1JBR0VfTElOT0RFX1NFQ1JFVFxuICAgICAgLSBfQVBQX1NUT1JBR0VfTElOT0RFX1JFR0lPTlxuICAgICAgLSBfQVBQX1NUT1JBR0VfTElOT0RFX0JVQ0tFVFxuICAgICAgLSBfQVBQX1NUT1JBR0VfV0FTQUJJX0FDQ0VTU19LRVlcbiAgICAgIC0gX0FQUF9TVE9SQUdFX1dBU0FCSV9TRUNSRVRcbiAgICAgIC0gX0FQUF9TVE9SQUdFX1dBU0FCSV9SRUdJT05cbiAgICAgIC0gX0FQUF9TVE9SQUdFX1dBU0FCSV9CVUNLRVRcblxuICBhcHB3cml0ZS13b3JrZXItbWlncmF0aW9uczpcbiAgICBpbWFnZTogYXBwd3JpdGUvYXBwd3JpdGU6MS44LjBcbiAgICBlbnRyeXBvaW50OiB3b3JrZXItbWlncmF0aW9uc1xuICAgIDw8OiAqeC1sb2dnaW5nXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICB2b2x1bWVzOlxuICAgICAgLSBhcHB3cml0ZS1pbXBvcnRzOi9zdG9yYWdlL2ltcG9ydHM6cndcbiAgICBkZXBlbmRzX29uOlxuICAgICAgLSBtYXJpYWRiXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIF9BUFBfRU5WXG4gICAgICAtIF9BUFBfV09SS0VSX1BFUl9DT1JFXG4gICAgICAtIF9BUFBfT1BFTlNTTF9LRVlfVjFcbiAgICAgIC0gX0FQUF9ET01BSU5cbiAgICAgIC0gX0FQUF9ET01BSU5fVEFSR0VUX0NOQU1FXG4gICAgICAtIF9BUFBfRE9NQUlOX1RBUkdFVF9BQUFBXG4gICAgICAtIF9BUFBfRE9NQUlOX1RBUkdFVF9BXG4gICAgICAtIF9BUFBfRE9NQUlOX1RBUkdFVF9DQUFcbiAgICAgIC0gX0FQUF9ETlNcbiAgICAgIC0gX0FQUF9FTUFJTF9TRUNVUklUWVxuICAgICAgLSBfQVBQX1JFRElTX0hPU1RcbiAgICAgIC0gX0FQUF9SRURJU19QT1JUXG4gICAgICAtIF9BUFBfUkVESVNfVVNFUlxuICAgICAgLSBfQVBQX1JFRElTX1BBU1NcbiAgICAgIC0gX0FQUF9EQl9IT1NUXG4gICAgICAtIF9BUFBfREJfUE9SVFxuICAgICAgLSBfQVBQX0RCX1NDSEVNQVxuICAgICAgLSBfQVBQX0RCX1VTRVJcbiAgICAgIC0gX0FQUF9EQl9QQVNTXG4gICAgICAtIF9BUFBfTE9HR0lOR19DT05GSUdcbiAgICAgIC0gX0FQUF9NSUdSQVRJT05TX0ZJUkVCQVNFX0NMSUVOVF9JRFxuICAgICAgLSBfQVBQX01JR1JBVElPTlNfRklSRUJBU0VfQ0xJRU5UX1NFQ1JFVFxuXG4gIGFwcHdyaXRlLXRhc2stbWFpbnRlbmFuY2U6XG4gICAgaW1hZ2U6IGFwcHdyaXRlL2FwcHdyaXRlOjEuOC4wXG4gICAgZW50cnlwb2ludDogbWFpbnRlbmFuY2VcbiAgICA8PDogKngtbG9nZ2luZ1xuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIC0gcmVkaXNcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gX0FQUF9FTlZcbiAgICAgIC0gX0FQUF9XT1JLRVJfUEVSX0NPUkVcbiAgICAgIC0gX0FQUF9ET01BSU5cbiAgICAgIC0gX0FQUF9ET01BSU5fVEFSR0VUX0NOQU1FXG4gICAgICAtIF9BUFBfRE9NQUlOX1RBUkdFVF9BQUFBXG4gICAgICAtIF9BUFBfRE9NQUlOX1RBUkdFVF9BXG4gICAgICAtIF9BUFBfRE9NQUlOX1RBUkdFVF9DQUFcbiAgICAgIC0gX0FQUF9ETlNcbiAgICAgIC0gX0FQUF9ET01BSU5fRlVOQ1RJT05TXG4gICAgICAtIF9BUFBfT1BFTlNTTF9LRVlfVjFcbiAgICAgIC0gX0FQUF9SRURJU19IT1NUXG4gICAgICAtIF9BUFBfUkVESVNfUE9SVFxuICAgICAgLSBfQVBQX1JFRElTX1VTRVJcbiAgICAgIC0gX0FQUF9SRURJU19QQVNTXG4gICAgICAtIF9BUFBfREJfSE9TVFxuICAgICAgLSBfQVBQX0RCX1BPUlRcbiAgICAgIC0gX0FQUF9EQl9TQ0hFTUFcbiAgICAgIC0gX0FQUF9EQl9VU0VSXG4gICAgICAtIF9BUFBfREJfUEFTU1xuICAgICAgLSBfQVBQX01BSU5URU5BTkNFX0lOVEVSVkFMXG4gICAgICAtIF9BUFBfTUFJTlRFTkFOQ0VfUkVURU5USU9OX0VYRUNVVElPTlxuICAgICAgLSBfQVBQX01BSU5URU5BTkNFX1JFVEVOVElPTl9DQUNIRVxuICAgICAgLSBfQVBQX01BSU5URU5BTkNFX1JFVEVOVElPTl9BQlVTRVxuICAgICAgLSBfQVBQX01BSU5URU5BTkNFX1JFVEVOVElPTl9BVURJVFxuICAgICAgLSBfQVBQX01BSU5URU5BTkNFX1JFVEVOVElPTl9BVURJVF9DT05TT0xFXG4gICAgICAtIF9BUFBfTUFJTlRFTkFOQ0VfUkVURU5USU9OX1VTQUdFX0hPVVJMWVxuICAgICAgLSBfQVBQX01BSU5URU5BTkNFX1JFVEVOVElPTl9TQ0hFRFVMRVNcblxuICBhcHB3cml0ZS10YXNrLXN0YXRzLXJlc291cmNlczpcbiAgICBpbWFnZTogYXBwd3JpdGUvYXBwd3JpdGU6MS44LjBcbiAgICBlbnRyeXBvaW50OiBzdGF0cy1yZXNvdXJjZXNcbiAgICA8PDogKngtbG9nZ2luZ1xuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIC0gcmVkaXNcbiAgICAgIC0gbWFyaWFkYlxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBfQVBQX0VOVlxuICAgICAgLSBfQVBQX1dPUktFUl9QRVJfQ09SRVxuICAgICAgLSBfQVBQX09QRU5TU0xfS0VZX1YxXG4gICAgICAtIF9BUFBfREJfSE9TVFxuICAgICAgLSBfQVBQX0RCX1BPUlRcbiAgICAgIC0gX0FQUF9EQl9TQ0hFTUFcbiAgICAgIC0gX0FQUF9EQl9VU0VSXG4gICAgICAtIF9BUFBfREJfUEFTU1xuICAgICAgLSBfQVBQX1JFRElTX0hPU1RcbiAgICAgIC0gX0FQUF9SRURJU19QT1JUXG4gICAgICAtIF9BUFBfUkVESVNfVVNFUlxuICAgICAgLSBfQVBQX1JFRElTX1BBU1NcbiAgICAgIC0gX0FQUF9VU0FHRV9TVEFUU1xuICAgICAgLSBfQVBQX0xPR0dJTkdfQ09ORklHXG4gICAgICAtIF9BUFBfREFUQUJBU0VfU0hBUkVEX1RBQkxFU1xuICAgICAgLSBfQVBQX1NUQVRTX1JFU09VUkNFU19JTlRFUlZBTFxuXG4gIGFwcHdyaXRlLXdvcmtlci1zdGF0cy1yZXNvdXJjZXM6XG4gICAgaW1hZ2U6IGFwcHdyaXRlL2FwcHdyaXRlOjEuOC4wXG4gICAgZW50cnlwb2ludDogd29ya2VyLXN0YXRzLXJlc291cmNlc1xuICAgIDw8OiAqeC1sb2dnaW5nXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBkZXBlbmRzX29uOlxuICAgICAgLSByZWRpc1xuICAgICAgLSBtYXJpYWRiXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIF9BUFBfRU5WXG4gICAgICAtIF9BUFBfV09SS0VSX1BFUl9DT1JFXG4gICAgICAtIF9BUFBfT1BFTlNTTF9LRVlfVjFcbiAgICAgIC0gX0FQUF9EQl9IT1NUXG4gICAgICAtIF9BUFBfREJfUE9SVFxuICAgICAgLSBfQVBQX0RCX1NDSEVNQVxuICAgICAgLSBfQVBQX0RCX1VTRVJcbiAgICAgIC0gX0FQUF9EQl9QQVNTXG4gICAgICAtIF9BUFBfUkVESVNfSE9TVFxuICAgICAgLSBfQVBQX1JFRElTX1BPUlRcbiAgICAgIC0gX0FQUF9SRURJU19VU0VSXG4gICAgICAtIF9BUFBfUkVESVNfUEFTU1xuICAgICAgLSBfQVBQX1VTQUdFX1NUQVRTXG4gICAgICAtIF9BUFBfTE9HR0lOR19DT05GSUdcbiAgICAgIC0gX0FQUF9TVEFUU19SRVNPVVJDRVNfSU5URVJWQUxcblxuICBhcHB3cml0ZS13b3JrZXItc3RhdHMtdXNhZ2U6XG4gICAgaW1hZ2U6IGFwcHdyaXRlL2FwcHdyaXRlOjEuOC4wXG4gICAgZW50cnlwb2ludDogd29ya2VyLXN0YXRzLXVzYWdlXG4gICAgPDw6ICp4LWxvZ2dpbmdcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGRlcGVuZHNfb246XG4gICAgICAtIHJlZGlzXG4gICAgICAtIG1hcmlhZGJcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gX0FQUF9FTlZcbiAgICAgIC0gX0FQUF9XT1JLRVJfUEVSX0NPUkVcbiAgICAgIC0gX0FQUF9PUEVOU1NMX0tFWV9WMVxuICAgICAgLSBfQVBQX0RCX0hPU1RcbiAgICAgIC0gX0FQUF9EQl9QT1JUXG4gICAgICAtIF9BUFBfREJfU0NIRU1BXG4gICAgICAtIF9BUFBfREJfVVNFUlxuICAgICAgLSBfQVBQX0RCX1BBU1NcbiAgICAgIC0gX0FQUF9SRURJU19IT1NUXG4gICAgICAtIF9BUFBfUkVESVNfUE9SVFxuICAgICAgLSBfQVBQX1JFRElTX1VTRVJcbiAgICAgIC0gX0FQUF9SRURJU19QQVNTXG4gICAgICAtIF9BUFBfVVNBR0VfU1RBVFNcbiAgICAgIC0gX0FQUF9MT0dHSU5HX0NPTkZJR1xuICAgICAgLSBfQVBQX1VTQUdFX0FHR1JFR0FUSU9OX0lOVEVSVkFMXG5cbiAgYXBwd3JpdGUtdGFzay1zY2hlZHVsZXItZnVuY3Rpb25zOlxuICAgIGltYWdlOiBhcHB3cml0ZS9hcHB3cml0ZToxLjguMFxuICAgIGVudHJ5cG9pbnQ6IHNjaGVkdWxlLWZ1bmN0aW9uc1xuICAgIDw8OiAqeC1sb2dnaW5nXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBkZXBlbmRzX29uOlxuICAgICAgLSBtYXJpYWRiXG4gICAgICAtIHJlZGlzXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIF9BUFBfRU5WXG4gICAgICAtIF9BUFBfV09SS0VSX1BFUl9DT1JFXG4gICAgICAtIF9BUFBfT1BFTlNTTF9LRVlfVjFcbiAgICAgIC0gX0FQUF9SRURJU19IT1NUXG4gICAgICAtIF9BUFBfUkVESVNfUE9SVFxuICAgICAgLSBfQVBQX1JFRElTX1VTRVJcbiAgICAgIC0gX0FQUF9SRURJU19QQVNTXG4gICAgICAtIF9BUFBfREJfSE9TVFxuICAgICAgLSBfQVBQX0RCX1BPUlRcbiAgICAgIC0gX0FQUF9EQl9TQ0hFTUFcbiAgICAgIC0gX0FQUF9EQl9VU0VSXG4gICAgICAtIF9BUFBfREJfUEFTU1xuXG4gIGFwcHdyaXRlLXRhc2stc2NoZWR1bGVyLWV4ZWN1dGlvbnM6XG4gICAgaW1hZ2U6IGFwcHdyaXRlL2FwcHdyaXRlOjEuOC4wXG4gICAgZW50cnlwb2ludDogc2NoZWR1bGUtZXhlY3V0aW9uc1xuICAgIDw8OiAqeC1sb2dnaW5nXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBkZXBlbmRzX29uOlxuICAgICAgLSBtYXJpYWRiXG4gICAgICAtIHJlZGlzXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIF9BUFBfRU5WXG4gICAgICAtIF9BUFBfV09SS0VSX1BFUl9DT1JFXG4gICAgICAtIF9BUFBfT1BFTlNTTF9LRVlfVjFcbiAgICAgIC0gX0FQUF9SRURJU19IT1NUXG4gICAgICAtIF9BUFBfUkVESVNfUE9SVFxuICAgICAgLSBfQVBQX1JFRElTX1VTRVJcbiAgICAgIC0gX0FQUF9SRURJU19QQVNTXG4gICAgICAtIF9BUFBfREJfSE9TVFxuICAgICAgLSBfQVBQX0RCX1BPUlRcbiAgICAgIC0gX0FQUF9EQl9TQ0hFTUFcbiAgICAgIC0gX0FQUF9EQl9VU0VSXG4gICAgICAtIF9BUFBfREJfUEFTU1xuXG4gIGFwcHdyaXRlLXRhc2stc2NoZWR1bGVyLW1lc3NhZ2VzOlxuICAgIGltYWdlOiBhcHB3cml0ZS9hcHB3cml0ZToxLjguMFxuICAgIGVudHJ5cG9pbnQ6IHNjaGVkdWxlLW1lc3NhZ2VzXG4gICAgPDw6ICp4LWxvZ2dpbmdcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGRlcGVuZHNfb246XG4gICAgICAtIG1hcmlhZGJcbiAgICAgIC0gcmVkaXNcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gX0FQUF9FTlZcbiAgICAgIC0gX0FQUF9XT1JLRVJfUEVSX0NPUkVcbiAgICAgIC0gX0FQUF9PUEVOU1NMX0tFWV9WMVxuICAgICAgLSBfQVBQX1JFRElTX0hPU1RcbiAgICAgIC0gX0FQUF9SRURJU19QT1JUXG4gICAgICAtIF9BUFBfUkVESVNfVVNFUlxuICAgICAgLSBfQVBQX1JFRElTX1BBU1NcbiAgICAgIC0gX0FQUF9EQl9IT1NUXG4gICAgICAtIF9BUFBfREJfUE9SVFxuICAgICAgLSBfQVBQX0RCX1NDSEVNQVxuICAgICAgLSBfQVBQX0RCX1VTRVJcbiAgICAgIC0gX0FQUF9EQl9QQVNTXG5cbiAgYXBwd3JpdGUtYXNzaXN0YW50OlxuICAgIGltYWdlOiBhcHB3cml0ZS9hc3Npc3RhbnQ6MC44LjNcbiAgICA8PDogKngtbG9nZ2luZ1xuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIF9BUFBfQVNTSVNUQU5UX09QRU5BSV9BUElfS0VZXG5cbiAgYXBwd3JpdGUtYnJvd3NlcjpcbiAgICBpbWFnZTogYXBwd3JpdGUvYnJvd3NlcjowLjIuNFxuICAgIDw8OiAqeC1sb2dnaW5nXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcblxuICBvcGVucnVudGltZXMtZXhlY3V0b3I6XG4gICAgaG9zdG5hbWU6IGV4YzFcbiAgICA8PDogKngtbG9nZ2luZ1xuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgc3RvcF9zaWduYWw6IFNJR0lOVFxuICAgIGltYWdlOiBvcGVucnVudGltZXMvZXhlY3V0b3I6MC43LjIyXG4gICAgdm9sdW1lczpcbiAgICAgIC0gL3Zhci9ydW4vZG9ja2VyLnNvY2s6L3Zhci9ydW4vZG9ja2VyLnNvY2tcbiAgICAgIC0gYXBwd3JpdGUtYnVpbGRzOi9zdG9yYWdlL2J1aWxkczpyd1xuICAgICAgLSBhcHB3cml0ZS1mdW5jdGlvbnM6L3N0b3JhZ2UvZnVuY3Rpb25zOnJ3XG4gICAgICAtIGFwcHdyaXRlLXNpdGVzOi9zdG9yYWdlL3NpdGVzOnJ3XG4gICAgICAjIEhvc3QgbW91bnQgbmVjZXNzYXJ5IHRvIHNoYXJlIGZpbGVzIGJldHdlZW4gZXhlY3V0b3IgYW5kIHJ1bnRpbWVzLlxuICAgICAgIyBJdCdzIG5vdCBwb3NzaWJsZSB0byBzaGFyZSBtb3VudCBmaWxlIGJldHdlZW4gMiBjb250YWluZXJzIHdpdGhvdXQgaG9zdCBtb3VudCAoY29weWluZyBpcyB0b28gc2xvdylcbiAgICAgIC0gL3RtcDovdG1wOnJ3XG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIE9QUl9FWEVDVVRPUl9JTkFDVElWRV9UUkVTSE9MRD0kX0FQUF9DT01QVVRFX0lOQUNUSVZFX1RIUkVTSE9MRFxuICAgICAgLSBPUFJfRVhFQ1VUT1JfTUFJTlRFTkFOQ0VfSU5URVJWQUw9JF9BUFBfQ09NUFVURV9NQUlOVEVOQU5DRV9JTlRFUlZBTFxuICAgICAgLSBPUFJfRVhFQ1VUT1JfTkVUV09SSz0kX0FQUF9DT01QVVRFX1JVTlRJTUVTX05FVFdPUktcbiAgICAgIC0gT1BSX0VYRUNVVE9SX0RPQ0tFUl9IVUJfVVNFUk5BTUU9JF9BUFBfRE9DS0VSX0hVQl9VU0VSTkFNRVxuICAgICAgLSBPUFJfRVhFQ1VUT1JfRE9DS0VSX0hVQl9QQVNTV09SRD0kX0FQUF9ET0NLRVJfSFVCX1BBU1NXT1JEXG4gICAgICAtIE9QUl9FWEVDVVRPUl9FTlY9JF9BUFBfRU5WXG4gICAgICAtIE9QUl9FWEVDVVRPUl9SVU5USU1FUz0kX0FQUF9GVU5DVElPTlNfUlVOVElNRVMsJF9BUFBfU0lURVNfUlVOVElNRVNcbiAgICAgIC0gT1BSX0VYRUNVVE9SX1NFQ1JFVD0kX0FQUF9FWEVDVVRPUl9TRUNSRVRcbiAgICAgIC0gT1BSX0VYRUNVVE9SX1JVTlRJTUVfVkVSU0lPTlM9djVcbiAgICAgIC0gT1BSX0VYRUNVVE9SX0xPR0dJTkdfQ09ORklHPSRfQVBQX0xPR0dJTkdfQ09ORklHXG4gICAgICAtIE9QUl9FWEVDVVRPUl9TVE9SQUdFX0RFVklDRT0kX0FQUF9TVE9SQUdFX0RFVklDRVxuICAgICAgLSBPUFJfRVhFQ1VUT1JfU1RPUkFHRV9TM19BQ0NFU1NfS0VZPSRfQVBQX1NUT1JBR0VfUzNfQUNDRVNTX0tFWVxuICAgICAgLSBPUFJfRVhFQ1VUT1JfU1RPUkFHRV9TM19TRUNSRVQ9JF9BUFBfU1RPUkFHRV9TM19TRUNSRVRcbiAgICAgIC0gT1BSX0VYRUNVVE9SX1NUT1JBR0VfUzNfUkVHSU9OPSRfQVBQX1NUT1JBR0VfUzNfUkVHSU9OXG4gICAgICAtIE9QUl9FWEVDVVRPUl9TVE9SQUdFX1MzX0JVQ0tFVD0kX0FQUF9TVE9SQUdFX1MzX0JVQ0tFVFxuICAgICAgLSBPUFJfRVhFQ1VUT1JfU1RPUkFHRV9TM19FTkRQT0lOVD0kX0FQUF9TVE9SQUdFX1MzX0VORFBPSU5UXG4gICAgICAtIE9QUl9FWEVDVVRPUl9TVE9SQUdFX0RPX1NQQUNFU19BQ0NFU1NfS0VZPSRfQVBQX1NUT1JBR0VfRE9fU1BBQ0VTX0FDQ0VTU19LRVlcbiAgICAgIC0gT1BSX0VYRUNVVE9SX1NUT1JBR0VfRE9fU1BBQ0VTX1NFQ1JFVD0kX0FQUF9TVE9SQUdFX0RPX1NQQUNFU19TRUNSRVRcbiAgICAgIC0gT1BSX0VYRUNVVE9SX1NUT1JBR0VfRE9fU1BBQ0VTX1JFR0lPTj0kX0FQUF9TVE9SQUdFX0RPX1NQQUNFU19SRUdJT05cbiAgICAgIC0gT1BSX0VYRUNVVE9SX1NUT1JBR0VfRE9fU1BBQ0VTX0JVQ0tFVD0kX0FQUF9TVE9SQUdFX0RPX1NQQUNFU19CVUNLRVRcbiAgICAgIC0gT1BSX0VYRUNVVE9SX1NUT1JBR0VfQkFDS0JMQVpFX0FDQ0VTU19LRVk9JF9BUFBfU1RPUkFHRV9CQUNLQkxBWkVfQUNDRVNTX0tFWVxuICAgICAgLSBPUFJfRVhFQ1VUT1JfU1RPUkFHRV9CQUNLQkxBWkVfU0VDUkVUPSRfQVBQX1NUT1JBR0VfQkFDS0JMQVpFX1NFQ1JFVFxuICAgICAgLSBPUFJfRVhFQ1VUT1JfU1RPUkFHRV9CQUNLQkxBWkVfUkVHSU9OPSRfQVBQX1NUT1JBR0VfQkFDS0JMQVpFX1JFR0lPTlxuICAgICAgLSBPUFJfRVhFQ1VUT1JfU1RPUkFHRV9CQUNLQkxBWkVfQlVDS0VUPSRfQVBQX1NUT1JBR0VfQkFDS0JMQVpFX0JVQ0tFVFxuICAgICAgLSBPUFJfRVhFQ1VUT1JfU1RPUkFHRV9MSU5PREVfQUNDRVNTX0tFWT0kX0FQUF9TVE9SQUdFX0xJTk9ERV9BQ0NFU1NfS0VZXG4gICAgICAtIE9QUl9FWEVDVVRPUl9TVE9SQUdFX0xJTk9ERV9TRUNSRVQ9JF9BUFBfU1RPUkFHRV9MSU5PREVfU0VDUkVUXG4gICAgICAtIE9QUl9FWEVDVVRPUl9TVE9SQUdFX0xJTk9ERV9SRUdJT049JF9BUFBfU1RPUkFHRV9MSU5PREVfUkVHSU9OXG4gICAgICAtIE9QUl9FWEVDVVRPUl9TVE9SQUdFX0xJTk9ERV9CVUNLRVQ9JF9BUFBfU1RPUkFHRV9MSU5PREVfQlVDS0VUXG4gICAgICAtIE9QUl9FWEVDVVRPUl9TVE9SQUdFX1dBU0FCSV9BQ0NFU1NfS0VZPSRfQVBQX1NUT1JBR0VfV0FTQUJJX0FDQ0VTU19LRVlcbiAgICAgIC0gT1BSX0VYRUNVVE9SX1NUT1JBR0VfV0FTQUJJX1NFQ1JFVD0kX0FQUF9TVE9SQUdFX1dBU0FCSV9TRUNSRVRcbiAgICAgIC0gT1BSX0VYRUNVVE9SX1NUT1JBR0VfV0FTQUJJX1JFR0lPTj0kX0FQUF9TVE9SQUdFX1dBU0FCSV9SRUdJT05cbiAgICAgIC0gT1BSX0VYRUNVVE9SX1NUT1JBR0VfV0FTQUJJX0JVQ0tFVD0kX0FQUF9TVE9SQUdFX1dBU0FCSV9CVUNLRVRcblxuICBtYXJpYWRiOlxuICAgIGltYWdlOiBtYXJpYWRiOjEwLjExICMgZml4IGlzc3VlcyB3aGVuIHVwZ3JhZGluZyB1c2luZzogbXlzcWxfdXBncmFkZSAtdSByb290IC1wXG4gICAgPDw6ICp4LWxvZ2dpbmdcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIHZvbHVtZXM6XG4gICAgICAtIGFwcHdyaXRlLW1hcmlhZGI6L3Zhci9saWIvbXlzcWw6cndcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gTVlTUUxfUk9PVF9QQVNTV09SRD0ke19BUFBfREJfUk9PVF9QQVNTfVxuICAgICAgLSBNWVNRTF9EQVRBQkFTRT0ke19BUFBfREJfU0NIRU1BfVxuICAgICAgLSBNWVNRTF9VU0VSPSR7X0FQUF9EQl9VU0VSfVxuICAgICAgLSBNWVNRTF9QQVNTV09SRD0ke19BUFBfREJfUEFTU31cbiAgICAgIC0gTUFSSUFEQl9BVVRPX1VQR1JBREU9MVxuICAgIGNvbW1hbmQ6IFwibXlzcWxkIC0taW5ub2RiLWZsdXNoLW1ldGhvZD1mc3luY1wiXG5cbiAgcmVkaXM6XG4gICAgaW1hZ2U6IHJlZGlzOjcuMi40LWFscGluZVxuICAgIDw8OiAqeC1sb2dnaW5nXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBjb21tYW5kOiA+XG4gICAgICByZWRpcy1zZXJ2ZXJcbiAgICAgIC0tbWF4bWVtb3J5ICAgICAgICAgICAgNTEybWJcbiAgICAgIC0tbWF4bWVtb3J5LXBvbGljeSAgICAgYWxsa2V5cy1scnVcbiAgICAgIC0tbWF4bWVtb3J5LXNhbXBsZXMgICAgNVxuICAgIHZvbHVtZXM6XG4gICAgICAtIGFwcHdyaXRlLXJlZGlzOi9kYXRhOnJ3XG5cbiAgIyBjbGFtYXY6XG4gICMgICBpbWFnZTogYXBwd3JpdGUvY2xhbWF2OjEuMi4wXG4gICMgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAjICAgdm9sdW1lczpcbiAgIyAgICAgLSBhcHB3cml0ZS11cGxvYWRzOi9zdG9yYWdlL3VwbG9hZHNcblxudm9sdW1lczpcbiAgYXBwd3JpdGUtbWFyaWFkYjpcbiAgYXBwd3JpdGUtcmVkaXM6XG4gIGFwcHdyaXRlLWNhY2hlOlxuICBhcHB3cml0ZS11cGxvYWRzOlxuICBhcHB3cml0ZS1pbXBvcnRzOlxuICBhcHB3cml0ZS1jZXJ0aWZpY2F0ZXM6XG4gIGFwcHdyaXRlLWZ1bmN0aW9uczpcbiAgYXBwd3JpdGUtc2l0ZXM6XG4gIGFwcHdyaXRlLWJ1aWxkczpcbiAgYXBwd3JpdGUtY29uZmlnOlxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbmZ1bmN0aW9uc19kb21haW4gPSBcImZ1bmN0aW9ucy4ke21haW5fZG9tYWlufVwiXG5zaXRlc19kb21haW4gPSBcInNpdGVzLiR7bWFpbl9kb21haW59XCJcbm9wZW5zc2xfa2V5ID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5kYl9yb290X3B3ID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5kYl91c2VyX3B3ID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5leGVjdXRvcl9zZWNyZXQgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcblxuW2NvbmZpZ11cbmVudiA9IFtcbiAgXCJfQVBQX0VOVj1wcm9kdWN0aW9uXCIsXG4gIFwiX0FQUF9MT0NBTEU9ZW5cIixcbiAgXCJfQVBQX09QVElPTlNfQUJVU0U9ZW5hYmxlZFwiLFxuICBcIl9BUFBfT1BUSU9OU19GT1JDRV9IVFRQUz1kaXNhYmxlZFwiLFxuICBcIl9BUFBfT1BUSU9OU19GVU5DVElPTlNfRk9SQ0VfSFRUUFM9ZGlzYWJsZWRcIixcbiAgXCJfQVBQX09QVElPTlNfUk9VVEVSX0ZPUkNFX0hUVFBTPWRpc2FibGVkXCIsXG4gIFwiX0FQUF9PUFRJT05TX1JPVVRFUl9QUk9URUNUSU9OPWRpc2FibGVkXCIsXG4gIFwiX0FQUF9PUEVOU1NMX0tFWV9WMT0ke29wZW5zc2xfa2V5fVwiLFxuICBcIl9BUFBfRE9NQUlOPSR7bWFpbl9kb21haW59XCIsXG4gIFwiX0FQUF9DVVNUT01fRE9NQUlOX0RFTllfTElTVD1leGFtcGxlLmNvbSx0ZXN0LmNvbSxhcHAuZXhhbXBsZS5jb21cIixcbiAgXCJfQVBQX0RPTUFJTl9GVU5DVElPTlM9JHtmdW5jdGlvbnNfZG9tYWlufVwiLFxuICBcIl9BUFBfRE9NQUlOX1NJVEVTPSR7c2l0ZXNfZG9tYWlufVwiLFxuICBcIl9BUFBfRE9NQUlOX1RBUkdFVD1sb2NhbGhvc3RcIixcbiAgXCJfQVBQX0RPTUFJTl9UQVJHRVRfQ05BTUU9bG9jYWxob3N0XCIsXG4gIFwiX0FQUF9ET01BSU5fVEFSR0VUX0FBQUE9OjoxXCIsXG4gIFwiX0FQUF9ET01BSU5fVEFSR0VUX0E9MTI3LjAuMC4xXCIsXG4gIFwiX0FQUF9ET01BSU5fVEFSR0VUX0NBQT1cIixcbiAgXCJfQVBQX0ROUz04LjguOC44XCIsXG4gIFwiX0FQUF9DT05TT0xFX1dISVRFTElTVF9ST09UPWVuYWJsZWRcIixcbiAgXCJfQVBQX0NPTlNPTEVfV0hJVEVMSVNUX0VNQUlMUz1cIixcbiAgXCJfQVBQX0NPTlNPTEVfV0hJVEVMSVNUX0lQUz1cIixcbiAgXCJfQVBQX0NPTlNPTEVfSE9TVE5BTUVTPVwiLFxuICBcIl9BUFBfU1lTVEVNX0VNQUlMX05BTUU9QXBwd3JpdGVcIixcbiAgXCJfQVBQX1NZU1RFTV9FTUFJTF9BRERSRVNTPW5vcmVwbHlAYXBwd3JpdGUuaW9cIixcbiAgXCJfQVBQX1NZU1RFTV9URUFNX0VNQUlMPXRlYW1AYXBwd3JpdGUuaW9cIixcbiAgXCJfQVBQX1NZU1RFTV9SRVNQT05TRV9GT1JNQVQ9XCIsXG4gIFwiX0FQUF9TWVNURU1fU0VDVVJJVFlfRU1BSUxfQUREUkVTUz1jZXJ0c0BhcHB3cml0ZS5pb1wiLFxuICBcIl9BUFBfRU1BSUxfU0VDVVJJVFk9XCIsXG4gIFwiX0FQUF9FTUFJTF9DRVJUSUZJQ0FURVM9XCIsXG4gIFwiX0FQUF9VU0FHRV9TVEFUUz1lbmFibGVkXCIsXG4gIFwiX0FQUF9MT0dHSU5HX1BST1ZJREVSPVwiLFxuICBcIl9BUFBfTE9HR0lOR19DT05GSUc9XCIsXG4gIFwiX0FQUF9VU0FHRV9BR0dSRUdBVElPTl9JTlRFUlZBTD0zMFwiLFxuICBcIl9BUFBfVVNBR0VfVElNRVNFUklFU19JTlRFUlZBTD0zMFwiLFxuICBcIl9BUFBfVVNBR0VfREFUQUJBU0VfSU5URVJWQUw9OTAwXCIsXG4gIFwiX0FQUF9XT1JLRVJfUEVSX0NPUkU9NlwiLFxuICBcIl9BUFBfQ09OU09MRV9TRVNTSU9OX0FMRVJUUz1kaXNhYmxlZFwiLFxuICBcIl9BUFBfQ09NUFJFU1NJT05fRU5BQkxFRD1lbmFibGVkXCIsXG4gIFwiX0FQUF9DT01QUkVTU0lPTl9NSU5fU0laRV9CWVRFUz0xMDI0XCIsXG4gIFwiX0FQUF9SRURJU19IT1NUPXJlZGlzXCIsXG4gIFwiX0FQUF9SRURJU19QT1JUPTYzNzlcIixcbiAgXCJfQVBQX1JFRElTX1VTRVI9XCIsXG4gIFwiX0FQUF9SRURJU19QQVNTPVwiLFxuICBcIl9BUFBfREJfSE9TVD1tYXJpYWRiXCIsXG4gIFwiX0FQUF9EQl9QT1JUPTMzMDZcIixcbiAgXCJfQVBQX0RCX1NDSEVNQT1hcHB3cml0ZVwiLFxuICBcIl9BUFBfREJfVVNFUj11c2VyXCIsXG4gIFwiX0FQUF9EQl9QQVNTPSR7ZGJfdXNlcl9wd31cIixcbiAgXCJfQVBQX0RCX1JPT1RfUEFTUz0ke2RiX3Jvb3RfcHd9XCIsXG4gIFwiX0FQUF9JTkZMVVhEQl9IT1NUPWluZmx1eGRiXCIsXG4gIFwiX0FQUF9JTkZMVVhEQl9QT1JUPTgwODZcIixcbiAgXCJfQVBQX1NUQVRTRF9IT1NUPXRlbGVncmFmXCIsXG4gIFwiX0FQUF9TVEFUU0RfUE9SVD04MTI1XCIsXG4gIFwiX0FQUF9TTVRQX0hPU1Q9XCIsXG4gIFwiX0FQUF9TTVRQX1BPUlQ9XCIsXG4gIFwiX0FQUF9TTVRQX1NFQ1VSRT1cIixcbiAgXCJfQVBQX1NNVFBfVVNFUk5BTUU9XCIsXG4gIFwiX0FQUF9TTVRQX1BBU1NXT1JEPVwiLFxuICBcIl9BUFBfU01TX1BST1ZJREVSPVwiLFxuICBcIl9BUFBfU01TX0ZST009XCIsXG4gIFwiX0FQUF9TVE9SQUdFX0xJTUlUPTMwMDAwMDAwXCIsXG4gIFwiX0FQUF9TVE9SQUdFX1BSRVZJRVdfTElNSVQ9MjAwMDAwMDBcIixcbiAgXCJfQVBQX1NUT1JBR0VfQU5USVZJUlVTPWRpc2FibGVkXCIsXG4gIFwiX0FQUF9TVE9SQUdFX0FOVElWSVJVU19IT1NUPWNsYW1hdlwiLFxuICBcIl9BUFBfU1RPUkFHRV9BTlRJVklSVVNfUE9SVD0zMzEwXCIsXG4gIFwiX0FQUF9TVE9SQUdFX0RFVklDRT1sb2NhbFwiLFxuICBcIl9BUFBfU1RPUkFHRV9TM19BQ0NFU1NfS0VZPVwiLFxuICBcIl9BUFBfU1RPUkFHRV9TM19TRUNSRVQ9XCIsXG4gIFwiX0FQUF9TVE9SQUdFX1MzX1JFR0lPTj11cy1lYXN0LTFcIixcbiAgXCJfQVBQX1NUT1JBR0VfUzNfQlVDS0VUPVwiLFxuICBcIl9BUFBfU1RPUkFHRV9TM19FTkRQT0lOVD1cIixcbiAgXCJfQVBQX1NUT1JBR0VfRE9fU1BBQ0VTX0FDQ0VTU19LRVk9XCIsXG4gIFwiX0FQUF9TVE9SQUdFX0RPX1NQQUNFU19TRUNSRVQ9XCIsXG4gIFwiX0FQUF9TVE9SQUdFX0RPX1NQQUNFU19SRUdJT049dXMtZWFzdC0xXCIsXG4gIFwiX0FQUF9TVE9SQUdFX0RPX1NQQUNFU19CVUNLRVQ9XCIsXG4gIFwiX0FQUF9TVE9SQUdFX0JBQ0tCTEFaRV9BQ0NFU1NfS0VZPVwiLFxuICBcIl9BUFBfU1RPUkFHRV9CQUNLQkxBWkVfU0VDUkVUPVwiLFxuICBcIl9BUFBfU1RPUkFHRV9CQUNLQkxBWkVfUkVHSU9OPXVzLXdlc3QtMDA0XCIsXG4gIFwiX0FQUF9TVE9SQUdFX0JBQ0tCTEFaRV9CVUNLRVQ9XCIsXG4gIFwiX0FQUF9TVE9SQUdFX0xJTk9ERV9BQ0NFU1NfS0VZPVwiLFxuICBcIl9BUFBfU1RPUkFHRV9MSU5PREVfU0VDUkVUPVwiLFxuICBcIl9BUFBfU1RPUkFHRV9MSU5PREVfUkVHSU9OPWV1LWNlbnRyYWwtMVwiLFxuICBcIl9BUFBfU1RPUkFHRV9MSU5PREVfQlVDS0VUPVwiLFxuICBcIl9BUFBfU1RPUkFHRV9XQVNBQklfQUNDRVNTX0tFWT1cIixcbiAgXCJfQVBQX1NUT1JBR0VfV0FTQUJJX1NFQ1JFVD1cIixcbiAgXCJfQVBQX1NUT1JBR0VfV0FTQUJJX1JFR0lPTj1ldS1jZW50cmFsLTFcIixcbiAgXCJfQVBQX1NUT1JBR0VfV0FTQUJJX0JVQ0tFVD1cIixcbiAgXCJfQVBQX0ZVTkNUSU9OU19TSVpFX0xJTUlUPTMwMDAwMDAwXCIsXG4gIFwiX0FQUF9DT01QVVRFX1NJWkVfTElNSVQ9MzAwMDAwMDBcIixcbiAgXCJfQVBQX0ZVTkNUSU9OU19CVUlMRF9TSVpFX0xJTUlUPTIwMDAwMDAwMDBcIixcbiAgXCJfQVBQX0ZVTkNUSU9OU19USU1FT1VUPTkwMFwiLFxuICBcIl9BUFBfRlVOQ1RJT05TX0JVSUxEX1RJTUVPVVQ9OTAwXCIsXG4gIFwiX0FQUF9DT01QVVRFX0JVSUxEX1RJTUVPVVQ9OTAwXCIsXG4gIFwiX0FQUF9GVU5DVElPTlNfQ09OVEFJTkVSUz0xMFwiLFxuICBcIl9BUFBfRlVOQ1RJT05TX0NQVVM9MFwiLFxuICBcIl9BUFBfQ09NUFVURV9DUFVTPTBcIixcbiAgXCJfQVBQX0ZVTkNUSU9OU19NRU1PUlk9MFwiLFxuICBcIl9BUFBfQ09NUFVURV9NRU1PUlk9MFwiLFxuICBcIl9BUFBfRlVOQ1RJT05TX01FTU9SWV9TV0FQPTBcIixcbiAgXCJfQVBQX0ZVTkNUSU9OU19SVU5USU1FUz1ub2RlLTE2LjAscGhwLTguMCxweXRob24tMy45LHJ1YnktMy4wXCIsXG4gIFwiX0FQUF9FWEVDVVRPUl9TRUNSRVQ9JHtleGVjdXRvcl9zZWNyZXR9XCIsXG4gIFwiX0FQUF9FWEVDVVRPUl9IT1NUPWh0dHA6Ly9leGMxL3YxXCIsXG4gIFwiX0FQUF9FWEVDVVRPUl9SVU5USU1FX05FVFdPUks9YXBwd3JpdGVfcnVudGltZXNcIixcbiAgXCJfQVBQX0ZVTkNUSU9OU19FTlZTPW5vZGUtMTYuMCxwaHAtNy40LHB5dGhvbi0zLjkscnVieS0zLjBcIixcbiAgXCJfQVBQX0ZVTkNUSU9OU19JTkFDVElWRV9USFJFU0hPTEQ9NjBcIixcbiAgXCJfQVBQX0NPTVBVVEVfSU5BQ1RJVkVfVEhSRVNIT0xEPTYwXCIsXG4gIFwiRE9DS0VSSFVCX1BVTExfVVNFUk5BTUU9XCIsXG4gIFwiRE9DS0VSSFVCX1BVTExfUEFTU1dPUkQ9XCIsXG4gIFwiRE9DS0VSSFVCX1BVTExfRU1BSUw9XCIsXG4gIFwiT1BFTl9SVU5USU1FU19ORVRXT1JLPWFwcHdyaXRlX3J1bnRpbWVzXCIsXG4gIFwiX0FQUF9GVU5DVElPTlNfUlVOVElNRVNfTkVUV09SSz1kb2twbG95LW5ldHdvcmtcIixcbiAgXCJfQVBQX0NPTVBVVEVfUlVOVElNRVNfTkVUV09SSz1kb2twbG95LW5ldHdvcmtcIixcbiAgXCJfQVBQX0RPQ0tFUl9IVUJfVVNFUk5BTUU9XCIsXG4gIFwiX0FQUF9ET0NLRVJfSFVCX1BBU1NXT1JEPVwiLFxuICBcIl9BUFBfRlVOQ1RJT05TX01BSU5URU5BTkNFX0lOVEVSVkFMPTM2MDBcIixcbiAgXCJfQVBQX0NPTVBVVEVfTUFJTlRFTkFOQ0VfSU5URVJWQUw9MzYwMFwiLFxuICBcIl9BUFBfU0lURVNfVElNRU9VVD05MDBcIixcbiAgXCJfQVBQX1NJVEVTX1JVTlRJTUVTPXN0YXRpYy0xLG5vZGUtMjIsZmx1dHRlci0zLjI5XCIsXG4gIFwiX0FQUF9WQ1NfR0lUSFVCX0FQUF9OQU1FPVwiLFxuICBcIl9BUFBfVkNTX0dJVEhVQl9QUklWQVRFX0tFWT1cIixcbiAgXCJfQVBQX1ZDU19HSVRIVUJfQVBQX0lEPVwiLFxuICBcIl9BUFBfVkNTX0dJVEhVQl9DTElFTlRfSUQ9XCIsXG4gIFwiX0FQUF9WQ1NfR0lUSFVCX0NMSUVOVF9TRUNSRVQ9XCIsXG4gIFwiX0FQUF9WQ1NfR0lUSFVCX1dFQkhPT0tfU0VDUkVUPVwiLFxuICBcIl9BUFBfTUFJTlRFTkFOQ0VfSU5URVJWQUw9ODY0MDBcIixcbiAgXCJfQVBQX01BSU5URU5BTkNFX0RFTEFZPTBcIixcbiAgXCJfQVBQX01BSU5URU5BTkNFX1NUQVJUX1RJTUU9MDA6MDBcIixcbiAgXCJfQVBQX01BSU5URU5BTkNFX1JFVEVOVElPTl9DQUNIRT0yNTkyMDAwXCIsXG4gIFwiX0FQUF9NQUlOVEVOQU5DRV9SRVRFTlRJT05fRVhFQ1VUSU9OPTEyMDk2MDBcIixcbiAgXCJfQVBQX01BSU5URU5BTkNFX1JFVEVOVElPTl9BVURJVD0xMjA5NjAwXCIsXG4gIFwiX0FQUF9NQUlOVEVOQU5DRV9SRVRFTlRJT05fQVVESVRfQ09OU09MRT0xNTc3ODgwMFwiLFxuICBcIl9BUFBfTUFJTlRFTkFOQ0VfUkVURU5USU9OX0FCVVNFPTg2NDAwXCIsXG4gIFwiX0FQUF9NQUlOVEVOQU5DRV9SRVRFTlRJT05fVVNBR0VfSE9VUkxZPTg2NDAwMDBcIixcbiAgXCJfQVBQX01BSU5URU5BTkNFX1JFVEVOVElPTl9TQ0hFRFVMRVM9ODY0MDBcIixcbiAgXCJfQVBQX0dSQVBIUUxfTUFYX0JBVENIX1NJWkU9MTBcIixcbiAgXCJfQVBQX0dSQVBIUUxfTUFYX0NPTVBMRVhJVFk9MjUwXCIsXG4gIFwiX0FQUF9HUkFQSFFMX01BWF9ERVBUSD0zXCIsXG4gIFwiX0FQUF9NSUdSQVRJT05TX0ZJUkVCQVNFX0NMSUVOVF9JRD1cIixcbiAgXCJfQVBQX01JR1JBVElPTlNfRklSRUJBU0VfQ0xJRU5UX1NFQ1JFVD1cIixcbiAgXCJfQVBQX0FTU0lTVEFOVF9PUEVOQUlfQVBJX0tFWT1cIixcbl1cbm1vdW50cyA9IFtdXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImFwcHdyaXRlXCJcbnBvcnQgPSA4MFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxucGF0aCA9IFwiL1wiXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImFwcHdyaXRlXCJcbnBvcnQgPSA4MFxuaG9zdCA9IFwiJHtzaXRlc19kb21haW59XCJcbnBhdGggPSBcIi9cIlxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJhcHB3cml0ZVwiXG5wb3J0ID0gODBcbmhvc3QgPSBcIiR7ZnVuY3Rpb25zX2RvbWFpbn1cIlxucGF0aCA9IFwiL1wiXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImFwcHdyaXRlLWNvbnNvbGVcIlxucG9ydCA9IDgwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5wYXRoID0gXCIvY29uc29sZVwiXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImFwcHdyaXRlLXJlYWx0aW1lXCJcbnBvcnQgPSA4MFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxucGF0aCA9IFwiL3YxL3JlYWx0aW1lXCJcbiIKfQ==
```

## Links

`database`,`firebase`,`mariadb`,`hosting`,`self-hosted`

---

Version:`1.8.0`

AppsmithAppsmith is a free and open source platform for building internal tools and applications.

AptabaseAptabase is a self-hosted web analytics platform that lets you track website traffic and user behavior.

### On this page

ConfigurationBase64LinksTags