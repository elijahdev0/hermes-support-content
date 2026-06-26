---
title: "Frappe HR | Dokploy"
source: "https://docs.dokploy.com/docs/templates/frappe-hr"
category: dokploy-docs
created: "2026-06-25T17:21:48.521Z"
---

Frappe HR | Dokploy

# Frappe HR

Copy as Markdown

Feature rich HR & Payroll software. 100% FOSS and customizable.

## Configuration

docker-compose.ymltemplate.toml

```
x-custom-image: &custom_image
  image: ${IMAGE_NAME:-ghcr.io/frappe/hrms}:${VERSION:-version-15}
  pull_policy: ${PULL_POLICY:-always}
  deploy:
    restart_policy:
      condition: always

services:
  backend:
    <<: *custom_image
    volumes:
      - sites:/home/frappe/frappe-bench/sites
    networks:
      - bench-network
    healthcheck:
      test:
        - CMD
        - wait-for-it
        - '0.0.0.0:8000'
      interval: 2s
      timeout: 10s
      retries: 30

  frontend:
    <<: *custom_image
    command:
      - nginx-entrypoint.sh
    depends_on:
      backend:
        condition: service_started
        required: true
      websocket:
        condition: service_started
        required: true
    environment:
      BACKEND: backend:8000
      FRAPPE_SITE_NAME_HEADER: ${FRAPPE_SITE_NAME_HEADER:-$$host}
      SOCKETIO: websocket:9000
      UPSTREAM_REAL_IP_ADDRESS: 127.0.0.1
      UPSTREAM_REAL_IP_HEADER: X-Forwarded-For
      UPSTREAM_REAL_IP_RECURSIVE: "off"
    volumes:
      - sites:/home/frappe/frappe-bench/sites

    networks:
      - bench-network

    healthcheck:
      test:
        - CMD
        - wait-for-it
        - '0.0.0.0:8080'
      interval: 2s
      timeout: 30s
      retries: 30

  queue-default:
    <<: *custom_image
    command:
      - bench
      - worker
      - --queue
      - default
    volumes:
      - sites:/home/frappe/frappe-bench/sites
    networks:
      - bench-network
    healthcheck:
      test:
        - CMD
        - wait-for-it
        - 'redis-queue:6379'
      interval: 2s
      timeout: 10s
      retries: 30
    depends_on:
      configurator:
        condition: service_completed_successfully
        required: true

  queue-long:
    <<: *custom_image
    command:
      - bench
      - worker
      - --queue
      - long
    volumes:
      - sites:/home/frappe/frappe-bench/sites
    networks:
      - bench-network
    healthcheck:
      test:
        - CMD
        - wait-for-it
        - 'redis-queue:6379'
      interval: 2s
      timeout: 10s
      retries: 30
    depends_on:
      configurator:
        condition: service_completed_successfully
        required: true

  queue-short:
    <<: *custom_image
    command:
      - bench
      - worker
      - --queue
      - short
    volumes:
      - sites:/home/frappe/frappe-bench/sites
    networks:
      - bench-network
    healthcheck:
      test:
        - CMD
        - wait-for-it
        - 'redis-queue:6379'
      interval: 2s
      timeout: 10s
      retries: 30
    depends_on:
      configurator:
        condition: service_completed_successfully
        required: true

  scheduler:
    <<: *custom_image
    healthcheck:
      test:
        - CMD
        - wait-for-it
        - 'redis-queue:6379'
      interval: 2s
      timeout: 10s
      retries: 30
    command:
      - bench
      - schedule
    depends_on:
      configurator:
        condition: service_completed_successfully
        required: true
    volumes:
      - sites:/home/frappe/frappe-bench/sites
    networks:
      - bench-network

  websocket:
    <<: *custom_image
    healthcheck:
      test:
        - CMD
        - wait-for-it
        - '0.0.0.0:9000'
      interval: 2s
      timeout: 10s
      retries: 30
    command:
      - node
      - /home/frappe/frappe-bench/apps/frappe/socketio.js
    depends_on:
      configurator:
        condition: service_completed_successfully
        required: true
    volumes:
      - sites:/home/frappe/frappe-bench/sites
    networks:
      - bench-network

  configurator:
    <<: *custom_image
    deploy:
      mode: replicated
      replicas: ${CONFIGURE:-0}
      restart_policy:
        condition: none
    entrypoint: ["bash", "-c"]
    command:
      - >
        [[ $${REGENERATE_APPS_TXT} == "1" ]] && ls -1 apps > sites/apps.txt;
        [[ -n `grep -hs ^ sites/common_site_config.json | jq -r ".db_host // empty"` ]] && exit 0;
        bench set-config -g db_host $$DB_HOST;
        bench set-config -gp db_port $$DB_PORT;
        bench set-config -g redis_cache "redis://$$REDIS_CACHE";
        bench set-config -g redis_queue "redis://$$REDIS_QUEUE";
        bench set-config -g redis_socketio "redis://$$REDIS_QUEUE";
        bench set-config -gp socketio_port $$SOCKETIO_PORT;
    environment:
      DB_HOST: "${DB_HOST:-db}"
      DB_PORT: "3306"
      REDIS_CACHE: redis-cache:6379
      REDIS_QUEUE: redis-queue:6379
      SOCKETIO_PORT: "9000"
      REGENERATE_APPS_TXT: "${REGENERATE_APPS_TXT:-0}"
    volumes:
      - sites:/home/frappe/frappe-bench/sites
    networks:
      - bench-network

  create-site:
    <<: *custom_image
    deploy:
      mode: replicated
      replicas: ${CREATE_SITE:-0}
      restart_policy:
        condition: none
    entrypoint: ["bash", "-c"]
    command:
      - >
        wait-for-it -t 120 $$DB_HOST:$$DB_PORT;
        wait-for-it -t 120 redis-cache:6379;
        wait-for-it -t 120 redis-queue:6379;
        export start=`date +%s`;
        until [[ -n `grep -hs ^ sites/common_site_config.json | jq -r ".db_host // empty"` ]] && \
          [[ -n `grep -hs ^ sites/common_site_config.json | jq -r ".redis_cache // empty"` ]] && \
          [[ -n `grep -hs ^ sites/common_site_config.json | jq -r ".redis_queue // empty"` ]];
        do
          echo "Waiting for sites/common_site_config.json to be created";
          sleep 5;
          if (( `date +%s`-start > 120 )); then
            echo "could not find sites/common_site_config.json with required keys";
            exit 1
          fi
        done;
        echo "sites/common_site_config.json found";
        [[ -d "sites/${SITE_NAME}" ]] && echo "${SITE_NAME} already exists" && exit 0;
        bench new-site --mariadb-user-host-login-scope='%' --admin-password=$${ADMIN_PASSWORD} --db-root-username=root --db-root-password=$${DB_ROOT_PASSWORD} $${INSTALL_APP_ARGS} $${SITE_NAME};
    volumes:
      - sites:/home/frappe/frappe-bench/sites
    environment:
      SITE_NAME: ${SITE_NAME}
      ADMIN_PASSWORD: ${ADMIN_PASSWORD}
      DB_HOST: ${DB_HOST:-db}
      DB_PORT: "${DB_PORT:-3306}"
      DB_ROOT_PASSWORD: ${DB_ROOT_PASSWORD}
      INSTALL_APP_ARGS: ${INSTALL_APP_ARGS}
    networks:
      - bench-network

  migration:
    <<: *custom_image
    deploy:
      mode: replicated
      replicas: ${MIGRATE:-0}
      restart_policy:
        condition: none
    entrypoint: ["bash", "-c"]
    command:
      - >
        curl -f http://${SITE_NAME}:8080/api/method/ping || echo "Site busy" && exit 0;
        bench --site all set-config -p maintenance_mode 1;
        bench --site all set-config -p pause_scheduler 1;
        bench --site all migrate;
        bench --site all set-config -p maintenance_mode 0;
        bench --site all set-config -p pause_scheduler 0;
    volumes:
      - sites:/home/frappe/frappe-bench/sites
    networks:
      - bench-network

  db:
    image: mariadb:10.6
    deploy:
      mode: replicated
      replicas: ${ENABLE_DB:-0}
      restart_policy:
        condition: always
    healthcheck:
      test: mysqladmin ping -h localhost --password=${DB_ROOT_PASSWORD}
      interval: 1s
      retries: 20
    command:
      - --character-set-server=utf8mb4
      - --collation-server=utf8mb4_unicode_ci
      - --skip-character-set-client-handshake
      - --skip-innodb-read-only-compressed
    environment:
      - MYSQL_ROOT_PASSWORD=${DB_ROOT_PASSWORD}
      - MARIADB_ROOT_PASSWORD=${DB_ROOT_PASSWORD}
    volumes:
      - db-data:/var/lib/mysql
    networks:
      - bench-network

  redis-cache:
    deploy:
      restart_policy:
        condition: always
    image: redis:6.2-alpine
    volumes:
      - redis-cache-data:/data
    networks:
      - bench-network
    healthcheck:
      test:
        - CMD
        - redis-cli
        - ping
      interval: 5s
      timeout: 5s
      retries: 3

  redis-queue:
    deploy:
      restart_policy:
        condition: always
    image: redis:6.2-alpine
    volumes:
      - redis-queue-data:/data
    networks:
      - bench-network
    healthcheck:
      test:
        - CMD
        - redis-cli
        - ping
      interval: 5s
      timeout: 5s
      retries: 3

  redis-socketio:
    deploy:
      restart_policy:
        condition: always
    image: redis:6.2-alpine
    volumes:
      - redis-socketio-data:/data
    networks:
      - bench-network
    healthcheck:
      test:
        - CMD
        - redis-cli
        - ping
      interval: 5s
      timeout: 5s
      retries: 3

volumes:
  db-data:
  redis-cache-data:
  redis-queue-data:
  redis-socketio-data:
  sites:
    driver_opts:
      type: "${SITE_VOLUME_TYPE}"
      o: "${SITE_VOLUME_OPTS}"
      device: "${SITE_VOLUME_DEV}"

networks:
  bench-network:
```

```
[variables]
main_domain = "${domain}"
db_root_password = "${password:32}"
admin_password = "${password:32}"

[config]
env = [
  "SITE_NAME=${main_domain}",
  "ADMIN_PASSWORD=${admin_password}",
  "DB_ROOT_PASSWORD=${db_root_password}",
  "MIGRATE=1",
  "ENABLE_DB=1",
  "DB_HOST=db",
  "CREATE_SITE=1",
  "CONFIGURE=1",
  "REGENERATE_APPS_TXT=1",
  "INSTALL_APP_ARGS=--install-app hrms",
  "IMAGE_NAME=ghcr.io/frappe/hrms",
  "VERSION=version-15",
  "FRAPPE_SITE_NAME_HEADER=",
]
mounts = []

[[config.domains]]
serviceName = "frontend"
port = 8_080
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogIngtY3VzdG9tLWltYWdlOiAmY3VzdG9tX2ltYWdlXG4gIGltYWdlOiAke0lNQUdFX05BTUU6LWdoY3IuaW8vZnJhcHBlL2hybXN9OiR7VkVSU0lPTjotdmVyc2lvbi0xNX1cbiAgcHVsbF9wb2xpY3k6ICR7UFVMTF9QT0xJQ1k6LWFsd2F5c31cbiAgZGVwbG95OlxuICAgIHJlc3RhcnRfcG9saWN5OlxuICAgICAgY29uZGl0aW9uOiBhbHdheXNcblxuc2VydmljZXM6XG4gIGJhY2tlbmQ6XG4gICAgPDw6ICpjdXN0b21faW1hZ2VcbiAgICB2b2x1bWVzOlxuICAgICAgLSBzaXRlczovaG9tZS9mcmFwcGUvZnJhcHBlLWJlbmNoL3NpdGVzXG4gICAgbmV0d29ya3M6XG4gICAgICAtIGJlbmNoLW5ldHdvcmtcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6XG4gICAgICAgIC0gQ01EXG4gICAgICAgIC0gd2FpdC1mb3ItaXRcbiAgICAgICAgLSAnMC4wLjAuMDo4MDAwJ1xuICAgICAgaW50ZXJ2YWw6IDJzXG4gICAgICB0aW1lb3V0OiAxMHNcbiAgICAgIHJldHJpZXM6IDMwXG5cbiAgZnJvbnRlbmQ6XG4gICAgPDw6ICpjdXN0b21faW1hZ2VcbiAgICBjb21tYW5kOlxuICAgICAgLSBuZ2lueC1lbnRyeXBvaW50LnNoXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIGJhY2tlbmQ6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9zdGFydGVkXG4gICAgICAgIHJlcXVpcmVkOiB0cnVlXG4gICAgICB3ZWJzb2NrZXQ6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9zdGFydGVkXG4gICAgICAgIHJlcXVpcmVkOiB0cnVlXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBCQUNLRU5EOiBiYWNrZW5kOjgwMDBcbiAgICAgIEZSQVBQRV9TSVRFX05BTUVfSEVBREVSOiAke0ZSQVBQRV9TSVRFX05BTUVfSEVBREVSOi0kJGhvc3R9XG4gICAgICBTT0NLRVRJTzogd2Vic29ja2V0OjkwMDBcbiAgICAgIFVQU1RSRUFNX1JFQUxfSVBfQUREUkVTUzogMTI3LjAuMC4xXG4gICAgICBVUFNUUkVBTV9SRUFMX0lQX0hFQURFUjogWC1Gb3J3YXJkZWQtRm9yXG4gICAgICBVUFNUUkVBTV9SRUFMX0lQX1JFQ1VSU0lWRTogXCJvZmZcIlxuICAgIHZvbHVtZXM6XG4gICAgICAtIHNpdGVzOi9ob21lL2ZyYXBwZS9mcmFwcGUtYmVuY2gvc2l0ZXNcblxuICAgIG5ldHdvcmtzOlxuICAgICAgLSBiZW5jaC1uZXR3b3JrXG4gICAgXG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OlxuICAgICAgICAtIENNRFxuICAgICAgICAtIHdhaXQtZm9yLWl0XG4gICAgICAgIC0gJzAuMC4wLjA6ODA4MCdcbiAgICAgIGludGVydmFsOiAyc1xuICAgICAgdGltZW91dDogMzBzXG4gICAgICByZXRyaWVzOiAzMFxuXG4gIHF1ZXVlLWRlZmF1bHQ6XG4gICAgPDw6ICpjdXN0b21faW1hZ2VcbiAgICBjb21tYW5kOlxuICAgICAgLSBiZW5jaFxuICAgICAgLSB3b3JrZXJcbiAgICAgIC0gLS1xdWV1ZVxuICAgICAgLSBkZWZhdWx0XG4gICAgdm9sdW1lczpcbiAgICAgIC0gc2l0ZXM6L2hvbWUvZnJhcHBlL2ZyYXBwZS1iZW5jaC9zaXRlc1xuICAgIG5ldHdvcmtzOlxuICAgICAgLSBiZW5jaC1uZXR3b3JrXG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OlxuICAgICAgICAtIENNRFxuICAgICAgICAtIHdhaXQtZm9yLWl0XG4gICAgICAgIC0gJ3JlZGlzLXF1ZXVlOjYzNzknXG4gICAgICBpbnRlcnZhbDogMnNcbiAgICAgIHRpbWVvdXQ6IDEwc1xuICAgICAgcmV0cmllczogMzBcbiAgICBkZXBlbmRzX29uOlxuICAgICAgY29uZmlndXJhdG9yOlxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2VfY29tcGxldGVkX3N1Y2Nlc3NmdWxseVxuICAgICAgICByZXF1aXJlZDogdHJ1ZVxuXG4gIHF1ZXVlLWxvbmc6XG4gICAgPDw6ICpjdXN0b21faW1hZ2VcbiAgICBjb21tYW5kOlxuICAgICAgLSBiZW5jaFxuICAgICAgLSB3b3JrZXJcbiAgICAgIC0gLS1xdWV1ZVxuICAgICAgLSBsb25nXG4gICAgdm9sdW1lczpcbiAgICAgIC0gc2l0ZXM6L2hvbWUvZnJhcHBlL2ZyYXBwZS1iZW5jaC9zaXRlc1xuICAgIG5ldHdvcmtzOlxuICAgICAgLSBiZW5jaC1uZXR3b3JrXG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OlxuICAgICAgICAtIENNRFxuICAgICAgICAtIHdhaXQtZm9yLWl0XG4gICAgICAgIC0gJ3JlZGlzLXF1ZXVlOjYzNzknXG4gICAgICBpbnRlcnZhbDogMnNcbiAgICAgIHRpbWVvdXQ6IDEwc1xuICAgICAgcmV0cmllczogMzBcbiAgICBkZXBlbmRzX29uOlxuICAgICAgY29uZmlndXJhdG9yOlxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2VfY29tcGxldGVkX3N1Y2Nlc3NmdWxseVxuICAgICAgICByZXF1aXJlZDogdHJ1ZVxuXG4gIHF1ZXVlLXNob3J0OlxuICAgIDw8OiAqY3VzdG9tX2ltYWdlXG4gICAgY29tbWFuZDpcbiAgICAgIC0gYmVuY2hcbiAgICAgIC0gd29ya2VyXG4gICAgICAtIC0tcXVldWVcbiAgICAgIC0gc2hvcnRcbiAgICB2b2x1bWVzOlxuICAgICAgLSBzaXRlczovaG9tZS9mcmFwcGUvZnJhcHBlLWJlbmNoL3NpdGVzXG4gICAgbmV0d29ya3M6XG4gICAgICAtIGJlbmNoLW5ldHdvcmtcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6XG4gICAgICAgIC0gQ01EXG4gICAgICAgIC0gd2FpdC1mb3ItaXRcbiAgICAgICAgLSAncmVkaXMtcXVldWU6NjM3OSdcbiAgICAgIGludGVydmFsOiAyc1xuICAgICAgdGltZW91dDogMTBzXG4gICAgICByZXRyaWVzOiAzMFxuICAgIGRlcGVuZHNfb246XG4gICAgICBjb25maWd1cmF0b3I6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9jb21wbGV0ZWRfc3VjY2Vzc2Z1bGx5XG4gICAgICAgIHJlcXVpcmVkOiB0cnVlXG5cbiAgc2NoZWR1bGVyOlxuICAgIDw8OiAqY3VzdG9tX2ltYWdlXG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OlxuICAgICAgICAtIENNRFxuICAgICAgICAtIHdhaXQtZm9yLWl0XG4gICAgICAgIC0gJ3JlZGlzLXF1ZXVlOjYzNzknXG4gICAgICBpbnRlcnZhbDogMnNcbiAgICAgIHRpbWVvdXQ6IDEwc1xuICAgICAgcmV0cmllczogMzBcbiAgICBjb21tYW5kOlxuICAgICAgLSBiZW5jaFxuICAgICAgLSBzY2hlZHVsZVxuICAgIGRlcGVuZHNfb246XG4gICAgICBjb25maWd1cmF0b3I6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9jb21wbGV0ZWRfc3VjY2Vzc2Z1bGx5XG4gICAgICAgIHJlcXVpcmVkOiB0cnVlXG4gICAgdm9sdW1lczpcbiAgICAgIC0gc2l0ZXM6L2hvbWUvZnJhcHBlL2ZyYXBwZS1iZW5jaC9zaXRlc1xuICAgIG5ldHdvcmtzOlxuICAgICAgLSBiZW5jaC1uZXR3b3JrXG5cbiAgd2Vic29ja2V0OlxuICAgIDw8OiAqY3VzdG9tX2ltYWdlXG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OlxuICAgICAgICAtIENNRFxuICAgICAgICAtIHdhaXQtZm9yLWl0XG4gICAgICAgIC0gJzAuMC4wLjA6OTAwMCdcbiAgICAgIGludGVydmFsOiAyc1xuICAgICAgdGltZW91dDogMTBzXG4gICAgICByZXRyaWVzOiAzMFxuICAgIGNvbW1hbmQ6XG4gICAgICAtIG5vZGVcbiAgICAgIC0gL2hvbWUvZnJhcHBlL2ZyYXBwZS1iZW5jaC9hcHBzL2ZyYXBwZS9zb2NrZXRpby5qc1xuICAgIGRlcGVuZHNfb246XG4gICAgICBjb25maWd1cmF0b3I6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9jb21wbGV0ZWRfc3VjY2Vzc2Z1bGx5XG4gICAgICAgIHJlcXVpcmVkOiB0cnVlXG4gICAgdm9sdW1lczpcbiAgICAgIC0gc2l0ZXM6L2hvbWUvZnJhcHBlL2ZyYXBwZS1iZW5jaC9zaXRlc1xuICAgIG5ldHdvcmtzOlxuICAgICAgLSBiZW5jaC1uZXR3b3JrXG5cbiAgY29uZmlndXJhdG9yOlxuICAgIDw8OiAqY3VzdG9tX2ltYWdlXG4gICAgZGVwbG95OlxuICAgICAgbW9kZTogcmVwbGljYXRlZFxuICAgICAgcmVwbGljYXM6ICR7Q09ORklHVVJFOi0wfVxuICAgICAgcmVzdGFydF9wb2xpY3k6XG4gICAgICAgIGNvbmRpdGlvbjogbm9uZVxuICAgIGVudHJ5cG9pbnQ6IFtcImJhc2hcIiwgXCItY1wiXVxuICAgIGNvbW1hbmQ6XG4gICAgICAtID5cbiAgICAgICAgW1sgJCR7UkVHRU5FUkFURV9BUFBTX1RYVH0gPT0gXCIxXCIgXV0gJiYgbHMgLTEgYXBwcyA+IHNpdGVzL2FwcHMudHh0O1xuICAgICAgICBbWyAtbiBgZ3JlcCAtaHMgXiBzaXRlcy9jb21tb25fc2l0ZV9jb25maWcuanNvbiB8IGpxIC1yIFwiLmRiX2hvc3QgLy8gZW1wdHlcImAgXV0gJiYgZXhpdCAwO1xuICAgICAgICBiZW5jaCBzZXQtY29uZmlnIC1nIGRiX2hvc3QgJCREQl9IT1NUO1xuICAgICAgICBiZW5jaCBzZXQtY29uZmlnIC1ncCBkYl9wb3J0ICQkREJfUE9SVDtcbiAgICAgICAgYmVuY2ggc2V0LWNvbmZpZyAtZyByZWRpc19jYWNoZSBcInJlZGlzOi8vJCRSRURJU19DQUNIRVwiO1xuICAgICAgICBiZW5jaCBzZXQtY29uZmlnIC1nIHJlZGlzX3F1ZXVlIFwicmVkaXM6Ly8kJFJFRElTX1FVRVVFXCI7XG4gICAgICAgIGJlbmNoIHNldC1jb25maWcgLWcgcmVkaXNfc29ja2V0aW8gXCJyZWRpczovLyQkUkVESVNfUVVFVUVcIjtcbiAgICAgICAgYmVuY2ggc2V0LWNvbmZpZyAtZ3Agc29ja2V0aW9fcG9ydCAkJFNPQ0tFVElPX1BPUlQ7XG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBEQl9IT1NUOiBcIiR7REJfSE9TVDotZGJ9XCJcbiAgICAgIERCX1BPUlQ6IFwiMzMwNlwiXG4gICAgICBSRURJU19DQUNIRTogcmVkaXMtY2FjaGU6NjM3OVxuICAgICAgUkVESVNfUVVFVUU6IHJlZGlzLXF1ZXVlOjYzNzlcbiAgICAgIFNPQ0tFVElPX1BPUlQ6IFwiOTAwMFwiXG4gICAgICBSRUdFTkVSQVRFX0FQUFNfVFhUOiBcIiR7UkVHRU5FUkFURV9BUFBTX1RYVDotMH1cIlxuICAgIHZvbHVtZXM6XG4gICAgICAtIHNpdGVzOi9ob21lL2ZyYXBwZS9mcmFwcGUtYmVuY2gvc2l0ZXNcbiAgICBuZXR3b3JrczpcbiAgICAgIC0gYmVuY2gtbmV0d29ya1xuXG4gIGNyZWF0ZS1zaXRlOlxuICAgIDw8OiAqY3VzdG9tX2ltYWdlXG4gICAgZGVwbG95OlxuICAgICAgbW9kZTogcmVwbGljYXRlZFxuICAgICAgcmVwbGljYXM6ICR7Q1JFQVRFX1NJVEU6LTB9XG4gICAgICByZXN0YXJ0X3BvbGljeTpcbiAgICAgICAgY29uZGl0aW9uOiBub25lXG4gICAgZW50cnlwb2ludDogW1wiYmFzaFwiLCBcIi1jXCJdXG4gICAgY29tbWFuZDpcbiAgICAgIC0gPlxuICAgICAgICB3YWl0LWZvci1pdCAtdCAxMjAgJCREQl9IT1NUOiQkREJfUE9SVDtcbiAgICAgICAgd2FpdC1mb3ItaXQgLXQgMTIwIHJlZGlzLWNhY2hlOjYzNzk7XG4gICAgICAgIHdhaXQtZm9yLWl0IC10IDEyMCByZWRpcy1xdWV1ZTo2Mzc5O1xuICAgICAgICBleHBvcnQgc3RhcnQ9YGRhdGUgKyVzYDtcbiAgICAgICAgdW50aWwgW1sgLW4gYGdyZXAgLWhzIF4gc2l0ZXMvY29tbW9uX3NpdGVfY29uZmlnLmpzb24gfCBqcSAtciBcIi5kYl9ob3N0IC8vIGVtcHR5XCJgIF1dICYmIFxcXG4gICAgICAgICAgW1sgLW4gYGdyZXAgLWhzIF4gc2l0ZXMvY29tbW9uX3NpdGVfY29uZmlnLmpzb24gfCBqcSAtciBcIi5yZWRpc19jYWNoZSAvLyBlbXB0eVwiYCBdXSAmJiBcXFxuICAgICAgICAgIFtbIC1uIGBncmVwIC1ocyBeIHNpdGVzL2NvbW1vbl9zaXRlX2NvbmZpZy5qc29uIHwganEgLXIgXCIucmVkaXNfcXVldWUgLy8gZW1wdHlcImAgXV07XG4gICAgICAgIGRvXG4gICAgICAgICAgZWNobyBcIldhaXRpbmcgZm9yIHNpdGVzL2NvbW1vbl9zaXRlX2NvbmZpZy5qc29uIHRvIGJlIGNyZWF0ZWRcIjtcbiAgICAgICAgICBzbGVlcCA1O1xuICAgICAgICAgIGlmICgoIGBkYXRlICslc2Atc3RhcnQgPiAxMjAgKSk7IHRoZW5cbiAgICAgICAgICAgIGVjaG8gXCJjb3VsZCBub3QgZmluZCBzaXRlcy9jb21tb25fc2l0ZV9jb25maWcuanNvbiB3aXRoIHJlcXVpcmVkIGtleXNcIjtcbiAgICAgICAgICAgIGV4aXQgMVxuICAgICAgICAgIGZpXG4gICAgICAgIGRvbmU7XG4gICAgICAgIGVjaG8gXCJzaXRlcy9jb21tb25fc2l0ZV9jb25maWcuanNvbiBmb3VuZFwiO1xuICAgICAgICBbWyAtZCBcInNpdGVzLyR7U0lURV9OQU1FfVwiIF1dICYmIGVjaG8gXCIke1NJVEVfTkFNRX0gYWxyZWFkeSBleGlzdHNcIiAmJiBleGl0IDA7XG4gICAgICAgIGJlbmNoIG5ldy1zaXRlIC0tbWFyaWFkYi11c2VyLWhvc3QtbG9naW4tc2NvcGU9JyUnIC0tYWRtaW4tcGFzc3dvcmQ9JCR7QURNSU5fUEFTU1dPUkR9IC0tZGItcm9vdC11c2VybmFtZT1yb290IC0tZGItcm9vdC1wYXNzd29yZD0kJHtEQl9ST09UX1BBU1NXT1JEfSAkJHtJTlNUQUxMX0FQUF9BUkdTfSAkJHtTSVRFX05BTUV9O1xuICAgIHZvbHVtZXM6XG4gICAgICAtIHNpdGVzOi9ob21lL2ZyYXBwZS9mcmFwcGUtYmVuY2gvc2l0ZXNcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIFNJVEVfTkFNRTogJHtTSVRFX05BTUV9XG4gICAgICBBRE1JTl9QQVNTV09SRDogJHtBRE1JTl9QQVNTV09SRH1cbiAgICAgIERCX0hPU1Q6ICR7REJfSE9TVDotZGJ9XG4gICAgICBEQl9QT1JUOiBcIiR7REJfUE9SVDotMzMwNn1cIlxuICAgICAgREJfUk9PVF9QQVNTV09SRDogJHtEQl9ST09UX1BBU1NXT1JEfVxuICAgICAgSU5TVEFMTF9BUFBfQVJHUzogJHtJTlNUQUxMX0FQUF9BUkdTfVxuICAgIG5ldHdvcmtzOlxuICAgICAgLSBiZW5jaC1uZXR3b3JrXG5cbiAgbWlncmF0aW9uOlxuICAgIDw8OiAqY3VzdG9tX2ltYWdlXG4gICAgZGVwbG95OlxuICAgICAgbW9kZTogcmVwbGljYXRlZFxuICAgICAgcmVwbGljYXM6ICR7TUlHUkFURTotMH1cbiAgICAgIHJlc3RhcnRfcG9saWN5OlxuICAgICAgICBjb25kaXRpb246IG5vbmVcbiAgICBlbnRyeXBvaW50OiBbXCJiYXNoXCIsIFwiLWNcIl1cbiAgICBjb21tYW5kOlxuICAgICAgLSA+XG4gICAgICAgIGN1cmwgLWYgaHR0cDovLyR7U0lURV9OQU1FfTo4MDgwL2FwaS9tZXRob2QvcGluZyB8fCBlY2hvIFwiU2l0ZSBidXN5XCIgJiYgZXhpdCAwO1xuICAgICAgICBiZW5jaCAtLXNpdGUgYWxsIHNldC1jb25maWcgLXAgbWFpbnRlbmFuY2VfbW9kZSAxO1xuICAgICAgICBiZW5jaCAtLXNpdGUgYWxsIHNldC1jb25maWcgLXAgcGF1c2Vfc2NoZWR1bGVyIDE7XG4gICAgICAgIGJlbmNoIC0tc2l0ZSBhbGwgbWlncmF0ZTtcbiAgICAgICAgYmVuY2ggLS1zaXRlIGFsbCBzZXQtY29uZmlnIC1wIG1haW50ZW5hbmNlX21vZGUgMDtcbiAgICAgICAgYmVuY2ggLS1zaXRlIGFsbCBzZXQtY29uZmlnIC1wIHBhdXNlX3NjaGVkdWxlciAwO1xuICAgIHZvbHVtZXM6XG4gICAgICAtIHNpdGVzOi9ob21lL2ZyYXBwZS9mcmFwcGUtYmVuY2gvc2l0ZXNcbiAgICBuZXR3b3JrczpcbiAgICAgIC0gYmVuY2gtbmV0d29ya1xuXG4gIGRiOlxuICAgIGltYWdlOiBtYXJpYWRiOjEwLjZcbiAgICBkZXBsb3k6XG4gICAgICBtb2RlOiByZXBsaWNhdGVkXG4gICAgICByZXBsaWNhczogJHtFTkFCTEVfREI6LTB9XG4gICAgICByZXN0YXJ0X3BvbGljeTpcbiAgICAgICAgY29uZGl0aW9uOiBhbHdheXNcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6IG15c3FsYWRtaW4gcGluZyAtaCBsb2NhbGhvc3QgLS1wYXNzd29yZD0ke0RCX1JPT1RfUEFTU1dPUkR9XG4gICAgICBpbnRlcnZhbDogMXNcbiAgICAgIHJldHJpZXM6IDIwXG4gICAgY29tbWFuZDpcbiAgICAgIC0gLS1jaGFyYWN0ZXItc2V0LXNlcnZlcj11dGY4bWI0XG4gICAgICAtIC0tY29sbGF0aW9uLXNlcnZlcj11dGY4bWI0X3VuaWNvZGVfY2lcbiAgICAgIC0gLS1za2lwLWNoYXJhY3Rlci1zZXQtY2xpZW50LWhhbmRzaGFrZVxuICAgICAgLSAtLXNraXAtaW5ub2RiLXJlYWQtb25seS1jb21wcmVzc2VkXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIE1ZU1FMX1JPT1RfUEFTU1dPUkQ9JHtEQl9ST09UX1BBU1NXT1JEfVxuICAgICAgLSBNQVJJQURCX1JPT1RfUEFTU1dPUkQ9JHtEQl9ST09UX1BBU1NXT1JEfVxuICAgIHZvbHVtZXM6XG4gICAgICAtIGRiLWRhdGE6L3Zhci9saWIvbXlzcWxcbiAgICBuZXR3b3JrczpcbiAgICAgIC0gYmVuY2gtbmV0d29ya1xuXG4gIHJlZGlzLWNhY2hlOlxuICAgIGRlcGxveTpcbiAgICAgIHJlc3RhcnRfcG9saWN5OlxuICAgICAgICBjb25kaXRpb246IGFsd2F5c1xuICAgIGltYWdlOiByZWRpczo2LjItYWxwaW5lXG4gICAgdm9sdW1lczpcbiAgICAgIC0gcmVkaXMtY2FjaGUtZGF0YTovZGF0YVxuICAgIG5ldHdvcmtzOlxuICAgICAgLSBiZW5jaC1uZXR3b3JrXG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OlxuICAgICAgICAtIENNRFxuICAgICAgICAtIHJlZGlzLWNsaVxuICAgICAgICAtIHBpbmdcbiAgICAgIGludGVydmFsOiA1c1xuICAgICAgdGltZW91dDogNXNcbiAgICAgIHJldHJpZXM6IDNcblxuICByZWRpcy1xdWV1ZTpcbiAgICBkZXBsb3k6XG4gICAgICByZXN0YXJ0X3BvbGljeTpcbiAgICAgICAgY29uZGl0aW9uOiBhbHdheXNcbiAgICBpbWFnZTogcmVkaXM6Ni4yLWFscGluZVxuICAgIHZvbHVtZXM6XG4gICAgICAtIHJlZGlzLXF1ZXVlLWRhdGE6L2RhdGFcbiAgICBuZXR3b3JrczpcbiAgICAgIC0gYmVuY2gtbmV0d29ya1xuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDpcbiAgICAgICAgLSBDTURcbiAgICAgICAgLSByZWRpcy1jbGlcbiAgICAgICAgLSBwaW5nXG4gICAgICBpbnRlcnZhbDogNXNcbiAgICAgIHRpbWVvdXQ6IDVzXG4gICAgICByZXRyaWVzOiAzXG5cbiAgcmVkaXMtc29ja2V0aW86XG4gICAgZGVwbG95OlxuICAgICAgcmVzdGFydF9wb2xpY3k6XG4gICAgICAgIGNvbmRpdGlvbjogYWx3YXlzXG4gICAgaW1hZ2U6IHJlZGlzOjYuMi1hbHBpbmVcbiAgICB2b2x1bWVzOlxuICAgICAgLSByZWRpcy1zb2NrZXRpby1kYXRhOi9kYXRhXG4gICAgbmV0d29ya3M6XG4gICAgICAtIGJlbmNoLW5ldHdvcmtcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6XG4gICAgICAgIC0gQ01EXG4gICAgICAgIC0gcmVkaXMtY2xpXG4gICAgICAgIC0gcGluZ1xuICAgICAgaW50ZXJ2YWw6IDVzXG4gICAgICB0aW1lb3V0OiA1c1xuICAgICAgcmV0cmllczogM1xuXG52b2x1bWVzOlxuICBkYi1kYXRhOlxuICByZWRpcy1jYWNoZS1kYXRhOlxuICByZWRpcy1xdWV1ZS1kYXRhOlxuICByZWRpcy1zb2NrZXRpby1kYXRhOlxuICBzaXRlczpcbiAgICBkcml2ZXJfb3B0czpcbiAgICAgIHR5cGU6IFwiJHtTSVRFX1ZPTFVNRV9UWVBFfVwiXG4gICAgICBvOiBcIiR7U0lURV9WT0xVTUVfT1BUU31cIlxuICAgICAgZGV2aWNlOiBcIiR7U0lURV9WT0xVTUVfREVWfVwiXG5cbm5ldHdvcmtzOlxuICBiZW5jaC1uZXR3b3JrOiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5kYl9yb290X3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5hZG1pbl9wYXNzd29yZCA9IFwiJHtwYXNzd29yZDozMn1cIlxuXG5bY29uZmlnXVxuZW52ID0gW1xuICBcIlNJVEVfTkFNRT0ke21haW5fZG9tYWlufVwiLFxuICBcIkFETUlOX1BBU1NXT1JEPSR7YWRtaW5fcGFzc3dvcmR9XCIsXG4gIFwiREJfUk9PVF9QQVNTV09SRD0ke2RiX3Jvb3RfcGFzc3dvcmR9XCIsXG4gIFwiTUlHUkFURT0xXCIsXG4gIFwiRU5BQkxFX0RCPTFcIixcbiAgXCJEQl9IT1NUPWRiXCIsXG4gIFwiQ1JFQVRFX1NJVEU9MVwiLFxuICBcIkNPTkZJR1VSRT0xXCIsXG4gIFwiUkVHRU5FUkFURV9BUFBTX1RYVD0xXCIsXG4gIFwiSU5TVEFMTF9BUFBfQVJHUz0tLWluc3RhbGwtYXBwIGhybXNcIixcbiAgXCJJTUFHRV9OQU1FPWdoY3IuaW8vZnJhcHBlL2hybXNcIixcbiAgXCJWRVJTSU9OPXZlcnNpb24tMTVcIixcbiAgXCJGUkFQUEVfU0lURV9OQU1FX0hFQURFUj1cIixcbl1cbm1vdW50cyA9IFtdXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImZyb250ZW5kXCJcbnBvcnQgPSA4XzA4MFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuIgp9
```

## Links

`hrms`,`payroll`,`leaves`,`expenses`,`attendance`,`performace`

---

Version:`version-15`

FormbricksFormbricks is an open-source survey and form platform for collecting user data.

FreeScoutFreeScout is a free open source help desk and shared inbox system. It's a self-hosted alternative to HelpScout, Zendesk, and similar services that allows you to manage customer communications through email and a clean web interface. FreeScout makes it easy to organize support requests, track customer conversations, and collaborate with your team.

### On this page

ConfigurationBase64LinksTags