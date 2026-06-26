---
title: "ERPNext | Dokploy"
source: "https://docs.dokploy.com/docs/templates/erpnext"
category: dokploy-docs
created: "2026-06-25T17:21:47.358Z"
---

ERPNext | Dokploy

# ERPNext

Copy as Markdown

100% Open Source and highly customizable ERP software.

## Configuration

docker-compose.ymltemplate.toml

```
x-custom-image: &custom_image
  image: ${IMAGE_NAME:-docker.io/frappe/erpnext}:${VERSION:-version-15}
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
  "INSTALL_APP_ARGS=--install-app erpnext",
  "IMAGE_NAME=docker.io/frappe/erpnext",
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
ewogICJjb21wb3NlIjogIngtY3VzdG9tLWltYWdlOiAmY3VzdG9tX2ltYWdlXG4gIGltYWdlOiAke0lNQUdFX05BTUU6LWRvY2tlci5pby9mcmFwcGUvZXJwbmV4dH06JHtWRVJTSU9OOi12ZXJzaW9uLTE1fVxuICBwdWxsX3BvbGljeTogJHtQVUxMX1BPTElDWTotYWx3YXlzfVxuICBkZXBsb3k6XG4gICAgcmVzdGFydF9wb2xpY3k6XG4gICAgICBjb25kaXRpb246IGFsd2F5c1xuXG5zZXJ2aWNlczpcbiAgYmFja2VuZDpcbiAgICA8PDogKmN1c3RvbV9pbWFnZVxuICAgIHZvbHVtZXM6XG4gICAgICAtIHNpdGVzOi9ob21lL2ZyYXBwZS9mcmFwcGUtYmVuY2gvc2l0ZXNcbiAgICBuZXR3b3JrczpcbiAgICAgIC0gYmVuY2gtbmV0d29ya1xuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDpcbiAgICAgICAgLSBDTURcbiAgICAgICAgLSB3YWl0LWZvci1pdFxuICAgICAgICAtICcwLjAuMC4wOjgwMDAnXG4gICAgICBpbnRlcnZhbDogMnNcbiAgICAgIHRpbWVvdXQ6IDEwc1xuICAgICAgcmV0cmllczogMzBcblxuICBmcm9udGVuZDpcbiAgICA8PDogKmN1c3RvbV9pbWFnZVxuICAgIGNvbW1hbmQ6XG4gICAgICAtIG5naW54LWVudHJ5cG9pbnQuc2hcbiAgICBkZXBlbmRzX29uOlxuICAgICAgYmFja2VuZDpcbiAgICAgICAgY29uZGl0aW9uOiBzZXJ2aWNlX3N0YXJ0ZWRcbiAgICAgICAgcmVxdWlyZWQ6IHRydWVcbiAgICAgIHdlYnNvY2tldDpcbiAgICAgICAgY29uZGl0aW9uOiBzZXJ2aWNlX3N0YXJ0ZWRcbiAgICAgICAgcmVxdWlyZWQ6IHRydWVcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIEJBQ0tFTkQ6IGJhY2tlbmQ6ODAwMFxuICAgICAgRlJBUFBFX1NJVEVfTkFNRV9IRUFERVI6ICR7RlJBUFBFX1NJVEVfTkFNRV9IRUFERVI6LSQkaG9zdH1cbiAgICAgIFNPQ0tFVElPOiB3ZWJzb2NrZXQ6OTAwMFxuICAgICAgVVBTVFJFQU1fUkVBTF9JUF9BRERSRVNTOiAxMjcuMC4wLjFcbiAgICAgIFVQU1RSRUFNX1JFQUxfSVBfSEVBREVSOiBYLUZvcndhcmRlZC1Gb3JcbiAgICAgIFVQU1RSRUFNX1JFQUxfSVBfUkVDVVJTSVZFOiBcIm9mZlwiXG4gICAgdm9sdW1lczpcbiAgICAgIC0gc2l0ZXM6L2hvbWUvZnJhcHBlL2ZyYXBwZS1iZW5jaC9zaXRlc1xuXG4gICAgbmV0d29ya3M6XG4gICAgICAtIGJlbmNoLW5ldHdvcmtcbiAgICBcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6XG4gICAgICAgIC0gQ01EXG4gICAgICAgIC0gd2FpdC1mb3ItaXRcbiAgICAgICAgLSAnMC4wLjAuMDo4MDgwJ1xuICAgICAgaW50ZXJ2YWw6IDJzXG4gICAgICB0aW1lb3V0OiAzMHNcbiAgICAgIHJldHJpZXM6IDMwXG5cbiAgcXVldWUtZGVmYXVsdDpcbiAgICA8PDogKmN1c3RvbV9pbWFnZVxuICAgIGNvbW1hbmQ6XG4gICAgICAtIGJlbmNoXG4gICAgICAtIHdvcmtlclxuICAgICAgLSAtLXF1ZXVlXG4gICAgICAtIGRlZmF1bHRcbiAgICB2b2x1bWVzOlxuICAgICAgLSBzaXRlczovaG9tZS9mcmFwcGUvZnJhcHBlLWJlbmNoL3NpdGVzXG4gICAgbmV0d29ya3M6XG4gICAgICAtIGJlbmNoLW5ldHdvcmtcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6XG4gICAgICAgIC0gQ01EXG4gICAgICAgIC0gd2FpdC1mb3ItaXRcbiAgICAgICAgLSAncmVkaXMtcXVldWU6NjM3OSdcbiAgICAgIGludGVydmFsOiAyc1xuICAgICAgdGltZW91dDogMTBzXG4gICAgICByZXRyaWVzOiAzMFxuICAgIGRlcGVuZHNfb246XG4gICAgICBjb25maWd1cmF0b3I6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9jb21wbGV0ZWRfc3VjY2Vzc2Z1bGx5XG4gICAgICAgIHJlcXVpcmVkOiB0cnVlXG5cbiAgcXVldWUtbG9uZzpcbiAgICA8PDogKmN1c3RvbV9pbWFnZVxuICAgIGNvbW1hbmQ6XG4gICAgICAtIGJlbmNoXG4gICAgICAtIHdvcmtlclxuICAgICAgLSAtLXF1ZXVlXG4gICAgICAtIGxvbmdcbiAgICB2b2x1bWVzOlxuICAgICAgLSBzaXRlczovaG9tZS9mcmFwcGUvZnJhcHBlLWJlbmNoL3NpdGVzXG4gICAgbmV0d29ya3M6XG4gICAgICAtIGJlbmNoLW5ldHdvcmtcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6XG4gICAgICAgIC0gQ01EXG4gICAgICAgIC0gd2FpdC1mb3ItaXRcbiAgICAgICAgLSAncmVkaXMtcXVldWU6NjM3OSdcbiAgICAgIGludGVydmFsOiAyc1xuICAgICAgdGltZW91dDogMTBzXG4gICAgICByZXRyaWVzOiAzMFxuICAgIGRlcGVuZHNfb246XG4gICAgICBjb25maWd1cmF0b3I6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9jb21wbGV0ZWRfc3VjY2Vzc2Z1bGx5XG4gICAgICAgIHJlcXVpcmVkOiB0cnVlXG5cbiAgcXVldWUtc2hvcnQ6XG4gICAgPDw6ICpjdXN0b21faW1hZ2VcbiAgICBjb21tYW5kOlxuICAgICAgLSBiZW5jaFxuICAgICAgLSB3b3JrZXJcbiAgICAgIC0gLS1xdWV1ZVxuICAgICAgLSBzaG9ydFxuICAgIHZvbHVtZXM6XG4gICAgICAtIHNpdGVzOi9ob21lL2ZyYXBwZS9mcmFwcGUtYmVuY2gvc2l0ZXNcbiAgICBuZXR3b3JrczpcbiAgICAgIC0gYmVuY2gtbmV0d29ya1xuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDpcbiAgICAgICAgLSBDTURcbiAgICAgICAgLSB3YWl0LWZvci1pdFxuICAgICAgICAtICdyZWRpcy1xdWV1ZTo2Mzc5J1xuICAgICAgaW50ZXJ2YWw6IDJzXG4gICAgICB0aW1lb3V0OiAxMHNcbiAgICAgIHJldHJpZXM6IDMwXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIGNvbmZpZ3VyYXRvcjpcbiAgICAgICAgY29uZGl0aW9uOiBzZXJ2aWNlX2NvbXBsZXRlZF9zdWNjZXNzZnVsbHlcbiAgICAgICAgcmVxdWlyZWQ6IHRydWVcblxuICBzY2hlZHVsZXI6XG4gICAgPDw6ICpjdXN0b21faW1hZ2VcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6XG4gICAgICAgIC0gQ01EXG4gICAgICAgIC0gd2FpdC1mb3ItaXRcbiAgICAgICAgLSAncmVkaXMtcXVldWU6NjM3OSdcbiAgICAgIGludGVydmFsOiAyc1xuICAgICAgdGltZW91dDogMTBzXG4gICAgICByZXRyaWVzOiAzMFxuICAgIGNvbW1hbmQ6XG4gICAgICAtIGJlbmNoXG4gICAgICAtIHNjaGVkdWxlXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIGNvbmZpZ3VyYXRvcjpcbiAgICAgICAgY29uZGl0aW9uOiBzZXJ2aWNlX2NvbXBsZXRlZF9zdWNjZXNzZnVsbHlcbiAgICAgICAgcmVxdWlyZWQ6IHRydWVcbiAgICB2b2x1bWVzOlxuICAgICAgLSBzaXRlczovaG9tZS9mcmFwcGUvZnJhcHBlLWJlbmNoL3NpdGVzXG4gICAgbmV0d29ya3M6XG4gICAgICAtIGJlbmNoLW5ldHdvcmtcblxuICB3ZWJzb2NrZXQ6XG4gICAgPDw6ICpjdXN0b21faW1hZ2VcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6XG4gICAgICAgIC0gQ01EXG4gICAgICAgIC0gd2FpdC1mb3ItaXRcbiAgICAgICAgLSAnMC4wLjAuMDo5MDAwJ1xuICAgICAgaW50ZXJ2YWw6IDJzXG4gICAgICB0aW1lb3V0OiAxMHNcbiAgICAgIHJldHJpZXM6IDMwXG4gICAgY29tbWFuZDpcbiAgICAgIC0gbm9kZVxuICAgICAgLSAvaG9tZS9mcmFwcGUvZnJhcHBlLWJlbmNoL2FwcHMvZnJhcHBlL3NvY2tldGlvLmpzXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIGNvbmZpZ3VyYXRvcjpcbiAgICAgICAgY29uZGl0aW9uOiBzZXJ2aWNlX2NvbXBsZXRlZF9zdWNjZXNzZnVsbHlcbiAgICAgICAgcmVxdWlyZWQ6IHRydWVcbiAgICB2b2x1bWVzOlxuICAgICAgLSBzaXRlczovaG9tZS9mcmFwcGUvZnJhcHBlLWJlbmNoL3NpdGVzXG4gICAgbmV0d29ya3M6XG4gICAgICAtIGJlbmNoLW5ldHdvcmtcblxuICBjb25maWd1cmF0b3I6XG4gICAgPDw6ICpjdXN0b21faW1hZ2VcbiAgICBkZXBsb3k6XG4gICAgICBtb2RlOiByZXBsaWNhdGVkXG4gICAgICByZXBsaWNhczogJHtDT05GSUdVUkU6LTB9XG4gICAgICByZXN0YXJ0X3BvbGljeTpcbiAgICAgICAgY29uZGl0aW9uOiBub25lXG4gICAgZW50cnlwb2ludDogW1wiYmFzaFwiLCBcIi1jXCJdXG4gICAgY29tbWFuZDpcbiAgICAgIC0gPlxuICAgICAgICBbWyAkJHtSRUdFTkVSQVRFX0FQUFNfVFhUfSA9PSBcIjFcIiBdXSAmJiBscyAtMSBhcHBzID4gc2l0ZXMvYXBwcy50eHQ7XG4gICAgICAgIFtbIC1uIGBncmVwIC1ocyBeIHNpdGVzL2NvbW1vbl9zaXRlX2NvbmZpZy5qc29uIHwganEgLXIgXCIuZGJfaG9zdCAvLyBlbXB0eVwiYCBdXSAmJiBleGl0IDA7XG4gICAgICAgIGJlbmNoIHNldC1jb25maWcgLWcgZGJfaG9zdCAkJERCX0hPU1Q7XG4gICAgICAgIGJlbmNoIHNldC1jb25maWcgLWdwIGRiX3BvcnQgJCREQl9QT1JUO1xuICAgICAgICBiZW5jaCBzZXQtY29uZmlnIC1nIHJlZGlzX2NhY2hlIFwicmVkaXM6Ly8kJFJFRElTX0NBQ0hFXCI7XG4gICAgICAgIGJlbmNoIHNldC1jb25maWcgLWcgcmVkaXNfcXVldWUgXCJyZWRpczovLyQkUkVESVNfUVVFVUVcIjtcbiAgICAgICAgYmVuY2ggc2V0LWNvbmZpZyAtZyByZWRpc19zb2NrZXRpbyBcInJlZGlzOi8vJCRSRURJU19RVUVVRVwiO1xuICAgICAgICBiZW5jaCBzZXQtY29uZmlnIC1ncCBzb2NrZXRpb19wb3J0ICQkU09DS0VUSU9fUE9SVDtcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIERCX0hPU1Q6IFwiJHtEQl9IT1NUOi1kYn1cIlxuICAgICAgREJfUE9SVDogXCIzMzA2XCJcbiAgICAgIFJFRElTX0NBQ0hFOiByZWRpcy1jYWNoZTo2Mzc5XG4gICAgICBSRURJU19RVUVVRTogcmVkaXMtcXVldWU6NjM3OVxuICAgICAgU09DS0VUSU9fUE9SVDogXCI5MDAwXCJcbiAgICAgIFJFR0VORVJBVEVfQVBQU19UWFQ6IFwiJHtSRUdFTkVSQVRFX0FQUFNfVFhUOi0wfVwiXG4gICAgdm9sdW1lczpcbiAgICAgIC0gc2l0ZXM6L2hvbWUvZnJhcHBlL2ZyYXBwZS1iZW5jaC9zaXRlc1xuICAgIG5ldHdvcmtzOlxuICAgICAgLSBiZW5jaC1uZXR3b3JrXG5cbiAgY3JlYXRlLXNpdGU6XG4gICAgPDw6ICpjdXN0b21faW1hZ2VcbiAgICBkZXBsb3k6XG4gICAgICBtb2RlOiByZXBsaWNhdGVkXG4gICAgICByZXBsaWNhczogJHtDUkVBVEVfU0lURTotMH1cbiAgICAgIHJlc3RhcnRfcG9saWN5OlxuICAgICAgICBjb25kaXRpb246IG5vbmVcbiAgICBlbnRyeXBvaW50OiBbXCJiYXNoXCIsIFwiLWNcIl1cbiAgICBjb21tYW5kOlxuICAgICAgLSA+XG4gICAgICAgIHdhaXQtZm9yLWl0IC10IDEyMCAkJERCX0hPU1Q6JCREQl9QT1JUO1xuICAgICAgICB3YWl0LWZvci1pdCAtdCAxMjAgcmVkaXMtY2FjaGU6NjM3OTtcbiAgICAgICAgd2FpdC1mb3ItaXQgLXQgMTIwIHJlZGlzLXF1ZXVlOjYzNzk7XG4gICAgICAgIGV4cG9ydCBzdGFydD1gZGF0ZSArJXNgO1xuICAgICAgICB1bnRpbCBbWyAtbiBgZ3JlcCAtaHMgXiBzaXRlcy9jb21tb25fc2l0ZV9jb25maWcuanNvbiB8IGpxIC1yIFwiLmRiX2hvc3QgLy8gZW1wdHlcImAgXV0gJiYgXFxcbiAgICAgICAgICBbWyAtbiBgZ3JlcCAtaHMgXiBzaXRlcy9jb21tb25fc2l0ZV9jb25maWcuanNvbiB8IGpxIC1yIFwiLnJlZGlzX2NhY2hlIC8vIGVtcHR5XCJgIF1dICYmIFxcXG4gICAgICAgICAgW1sgLW4gYGdyZXAgLWhzIF4gc2l0ZXMvY29tbW9uX3NpdGVfY29uZmlnLmpzb24gfCBqcSAtciBcIi5yZWRpc19xdWV1ZSAvLyBlbXB0eVwiYCBdXTtcbiAgICAgICAgZG9cbiAgICAgICAgICBlY2hvIFwiV2FpdGluZyBmb3Igc2l0ZXMvY29tbW9uX3NpdGVfY29uZmlnLmpzb24gdG8gYmUgY3JlYXRlZFwiO1xuICAgICAgICAgIHNsZWVwIDU7XG4gICAgICAgICAgaWYgKCggYGRhdGUgKyVzYC1zdGFydCA+IDEyMCApKTsgdGhlblxuICAgICAgICAgICAgZWNobyBcImNvdWxkIG5vdCBmaW5kIHNpdGVzL2NvbW1vbl9zaXRlX2NvbmZpZy5qc29uIHdpdGggcmVxdWlyZWQga2V5c1wiO1xuICAgICAgICAgICAgZXhpdCAxXG4gICAgICAgICAgZmlcbiAgICAgICAgZG9uZTtcbiAgICAgICAgZWNobyBcInNpdGVzL2NvbW1vbl9zaXRlX2NvbmZpZy5qc29uIGZvdW5kXCI7XG4gICAgICAgIFtbIC1kIFwic2l0ZXMvJHtTSVRFX05BTUV9XCIgXV0gJiYgZWNobyBcIiR7U0lURV9OQU1FfSBhbHJlYWR5IGV4aXN0c1wiICYmIGV4aXQgMDtcbiAgICAgICAgYmVuY2ggbmV3LXNpdGUgLS1tYXJpYWRiLXVzZXItaG9zdC1sb2dpbi1zY29wZT0nJScgLS1hZG1pbi1wYXNzd29yZD0kJHtBRE1JTl9QQVNTV09SRH0gLS1kYi1yb290LXVzZXJuYW1lPXJvb3QgLS1kYi1yb290LXBhc3N3b3JkPSQke0RCX1JPT1RfUEFTU1dPUkR9ICQke0lOU1RBTExfQVBQX0FSR1N9ICQke1NJVEVfTkFNRX07XG4gICAgdm9sdW1lczpcbiAgICAgIC0gc2l0ZXM6L2hvbWUvZnJhcHBlL2ZyYXBwZS1iZW5jaC9zaXRlc1xuICAgIGVudmlyb25tZW50OlxuICAgICAgU0lURV9OQU1FOiAke1NJVEVfTkFNRX1cbiAgICAgIEFETUlOX1BBU1NXT1JEOiAke0FETUlOX1BBU1NXT1JEfVxuICAgICAgREJfSE9TVDogJHtEQl9IT1NUOi1kYn1cbiAgICAgIERCX1BPUlQ6IFwiJHtEQl9QT1JUOi0zMzA2fVwiXG4gICAgICBEQl9ST09UX1BBU1NXT1JEOiAke0RCX1JPT1RfUEFTU1dPUkR9XG4gICAgICBJTlNUQUxMX0FQUF9BUkdTOiAke0lOU1RBTExfQVBQX0FSR1N9XG4gICAgbmV0d29ya3M6XG4gICAgICAtIGJlbmNoLW5ldHdvcmtcblxuICBtaWdyYXRpb246XG4gICAgPDw6ICpjdXN0b21faW1hZ2VcbiAgICBkZXBsb3k6XG4gICAgICBtb2RlOiByZXBsaWNhdGVkXG4gICAgICByZXBsaWNhczogJHtNSUdSQVRFOi0wfVxuICAgICAgcmVzdGFydF9wb2xpY3k6XG4gICAgICAgIGNvbmRpdGlvbjogbm9uZVxuICAgIGVudHJ5cG9pbnQ6IFtcImJhc2hcIiwgXCItY1wiXVxuICAgIGNvbW1hbmQ6XG4gICAgICAtID5cbiAgICAgICAgY3VybCAtZiBodHRwOi8vJHtTSVRFX05BTUV9OjgwODAvYXBpL21ldGhvZC9waW5nIHx8IGVjaG8gXCJTaXRlIGJ1c3lcIiAmJiBleGl0IDA7XG4gICAgICAgIGJlbmNoIC0tc2l0ZSBhbGwgc2V0LWNvbmZpZyAtcCBtYWludGVuYW5jZV9tb2RlIDE7XG4gICAgICAgIGJlbmNoIC0tc2l0ZSBhbGwgc2V0LWNvbmZpZyAtcCBwYXVzZV9zY2hlZHVsZXIgMTtcbiAgICAgICAgYmVuY2ggLS1zaXRlIGFsbCBtaWdyYXRlO1xuICAgICAgICBiZW5jaCAtLXNpdGUgYWxsIHNldC1jb25maWcgLXAgbWFpbnRlbmFuY2VfbW9kZSAwO1xuICAgICAgICBiZW5jaCAtLXNpdGUgYWxsIHNldC1jb25maWcgLXAgcGF1c2Vfc2NoZWR1bGVyIDA7XG4gICAgdm9sdW1lczpcbiAgICAgIC0gc2l0ZXM6L2hvbWUvZnJhcHBlL2ZyYXBwZS1iZW5jaC9zaXRlc1xuICAgIG5ldHdvcmtzOlxuICAgICAgLSBiZW5jaC1uZXR3b3JrXG5cbiAgZGI6XG4gICAgaW1hZ2U6IG1hcmlhZGI6MTAuNlxuICAgIGRlcGxveTpcbiAgICAgIG1vZGU6IHJlcGxpY2F0ZWRcbiAgICAgIHJlcGxpY2FzOiAke0VOQUJMRV9EQjotMH1cbiAgICAgIHJlc3RhcnRfcG9saWN5OlxuICAgICAgICBjb25kaXRpb246IGFsd2F5c1xuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDogbXlzcWxhZG1pbiBwaW5nIC1oIGxvY2FsaG9zdCAtLXBhc3N3b3JkPSR7REJfUk9PVF9QQVNTV09SRH1cbiAgICAgIGludGVydmFsOiAxc1xuICAgICAgcmV0cmllczogMjBcbiAgICBjb21tYW5kOlxuICAgICAgLSAtLWNoYXJhY3Rlci1zZXQtc2VydmVyPXV0ZjhtYjRcbiAgICAgIC0gLS1jb2xsYXRpb24tc2VydmVyPXV0ZjhtYjRfdW5pY29kZV9jaVxuICAgICAgLSAtLXNraXAtY2hhcmFjdGVyLXNldC1jbGllbnQtaGFuZHNoYWtlXG4gICAgICAtIC0tc2tpcC1pbm5vZGItcmVhZC1vbmx5LWNvbXByZXNzZWRcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gTVlTUUxfUk9PVF9QQVNTV09SRD0ke0RCX1JPT1RfUEFTU1dPUkR9XG4gICAgICAtIE1BUklBREJfUk9PVF9QQVNTV09SRD0ke0RCX1JPT1RfUEFTU1dPUkR9XG4gICAgdm9sdW1lczpcbiAgICAgIC0gZGItZGF0YTovdmFyL2xpYi9teXNxbFxuICAgIG5ldHdvcmtzOlxuICAgICAgLSBiZW5jaC1uZXR3b3JrXG5cbiAgcmVkaXMtY2FjaGU6XG4gICAgZGVwbG95OlxuICAgICAgcmVzdGFydF9wb2xpY3k6XG4gICAgICAgIGNvbmRpdGlvbjogYWx3YXlzXG4gICAgaW1hZ2U6IHJlZGlzOjYuMi1hbHBpbmVcbiAgICB2b2x1bWVzOlxuICAgICAgLSByZWRpcy1jYWNoZS1kYXRhOi9kYXRhXG4gICAgbmV0d29ya3M6XG4gICAgICAtIGJlbmNoLW5ldHdvcmtcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6XG4gICAgICAgIC0gQ01EXG4gICAgICAgIC0gcmVkaXMtY2xpXG4gICAgICAgIC0gcGluZ1xuICAgICAgaW50ZXJ2YWw6IDVzXG4gICAgICB0aW1lb3V0OiA1c1xuICAgICAgcmV0cmllczogM1xuXG4gIHJlZGlzLXF1ZXVlOlxuICAgIGRlcGxveTpcbiAgICAgIHJlc3RhcnRfcG9saWN5OlxuICAgICAgICBjb25kaXRpb246IGFsd2F5c1xuICAgIGltYWdlOiByZWRpczo2LjItYWxwaW5lXG4gICAgdm9sdW1lczpcbiAgICAgIC0gcmVkaXMtcXVldWUtZGF0YTovZGF0YVxuICAgIG5ldHdvcmtzOlxuICAgICAgLSBiZW5jaC1uZXR3b3JrXG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OlxuICAgICAgICAtIENNRFxuICAgICAgICAtIHJlZGlzLWNsaVxuICAgICAgICAtIHBpbmdcbiAgICAgIGludGVydmFsOiA1c1xuICAgICAgdGltZW91dDogNXNcbiAgICAgIHJldHJpZXM6IDNcblxuICByZWRpcy1zb2NrZXRpbzpcbiAgICBkZXBsb3k6XG4gICAgICByZXN0YXJ0X3BvbGljeTpcbiAgICAgICAgY29uZGl0aW9uOiBhbHdheXNcbiAgICBpbWFnZTogcmVkaXM6Ni4yLWFscGluZVxuICAgIHZvbHVtZXM6XG4gICAgICAtIHJlZGlzLXNvY2tldGlvLWRhdGE6L2RhdGFcbiAgICBuZXR3b3JrczpcbiAgICAgIC0gYmVuY2gtbmV0d29ya1xuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDpcbiAgICAgICAgLSBDTURcbiAgICAgICAgLSByZWRpcy1jbGlcbiAgICAgICAgLSBwaW5nXG4gICAgICBpbnRlcnZhbDogNXNcbiAgICAgIHRpbWVvdXQ6IDVzXG4gICAgICByZXRyaWVzOiAzXG5cbnZvbHVtZXM6XG4gIGRiLWRhdGE6XG4gIHJlZGlzLWNhY2hlLWRhdGE6XG4gIHJlZGlzLXF1ZXVlLWRhdGE6XG4gIHJlZGlzLXNvY2tldGlvLWRhdGE6XG4gIHNpdGVzOlxuICAgIGRyaXZlcl9vcHRzOlxuICAgICAgdHlwZTogXCIke1NJVEVfVk9MVU1FX1RZUEV9XCJcbiAgICAgIG86IFwiJHtTSVRFX1ZPTFVNRV9PUFRTfVwiXG4gICAgICBkZXZpY2U6IFwiJHtTSVRFX1ZPTFVNRV9ERVZ9XCJcblxubmV0d29ya3M6XG4gIGJlbmNoLW5ldHdvcms6IiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbmRiX3Jvb3RfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcbmFkbWluX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5cbltjb25maWddXG5lbnYgPSBbXG4gIFwiU0lURV9OQU1FPSR7bWFpbl9kb21haW59XCIsXG4gIFwiQURNSU5fUEFTU1dPUkQ9JHthZG1pbl9wYXNzd29yZH1cIixcbiAgXCJEQl9ST09UX1BBU1NXT1JEPSR7ZGJfcm9vdF9wYXNzd29yZH1cIixcbiAgXCJNSUdSQVRFPTFcIixcbiAgXCJFTkFCTEVfREI9MVwiLFxuICBcIkRCX0hPU1Q9ZGJcIixcbiAgXCJDUkVBVEVfU0lURT0xXCIsXG4gIFwiQ09ORklHVVJFPTFcIixcbiAgXCJSRUdFTkVSQVRFX0FQUFNfVFhUPTFcIixcbiAgXCJJTlNUQUxMX0FQUF9BUkdTPS0taW5zdGFsbC1hcHAgZXJwbmV4dFwiLFxuICBcIklNQUdFX05BTUU9ZG9ja2VyLmlvL2ZyYXBwZS9lcnBuZXh0XCIsXG4gIFwiVkVSU0lPTj12ZXJzaW9uLTE1XCIsXG4gIFwiRlJBUFBFX1NJVEVfTkFNRV9IRUFERVI9XCIsXG5dXG5tb3VudHMgPSBbXVxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJmcm9udGVuZFwiXG5wb3J0ID0gOF8wODBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcbiIKfQ==
```

## Links

`erp`,`accounts`,`manufacturing`,`retail`,`sales`,`pos`,`hrms`

---

Version:`version-15`

EnshroudedEnshrouded steam dedicated server.

EtherpadEtherpad is a real-time collaborative text editor that allows multiple users to edit documents simultaneously.

### On this page

ConfigurationBase64LinksTags