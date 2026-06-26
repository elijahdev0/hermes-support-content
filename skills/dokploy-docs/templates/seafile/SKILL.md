---
title: "Seafile | Dokploy"
source: "https://docs.dokploy.com/docs/templates/seafile"
category: dokploy-docs
created: "2026-06-25T17:21:59.113Z"
---

Seafile | Dokploy

# Seafile

Copy as Markdown

Open source cloud storage system for file sync, share and document collaboration

## Configuration

docker-compose.ymltemplate.toml

```
# https://manual.seafile.com/12.0/setup/setup_ce_by_docker
#
# This Dokploy template for seafile sets the default credentials to:
#   USERNAME: [email protected]
#   PASSWORD: <SECRET GENERATED IN ENVIRONMENT VARIABLES>
#
# !!! IMPORTANT !!!
#     Please look at the environment variable settings and tweak
#     them prior to the first deployment!
#
#     If you have already deployed once, changes to some environment
#     variables may not take effect. For example, initial passwords.

services:
  seafile-db:
    image: mariadb:10.11
    environment:
      - MYSQL_ROOT_PASSWORD=${INIT_SEAFILE_MYSQL_ROOT_PASSWORD:-}
      - MYSQL_LOG_CONSOLE=true
      - MARIADB_AUTO_UPGRADE=1
    volumes:
      - seafile-mysql-db:/var/lib/mysql"
    networks:
      - seafile-net
    healthcheck:
      test:
        [
          "CMD",
          "/usr/local/bin/healthcheck.sh",
          "--connect",
          "--mariadbupgrade",
          "--innodb_initialized",
        ]
      interval: 20s
      start_period: 30s
      timeout: 5s
      retries: 10

  memcached:
    image: memcached:1.6.29
    entrypoint: memcached -m 256
    networks:
      - seafile-net
    healthcheck:
      test:
        [
          "CMD-SHELL",
          'bash -c "echo version | (exec 3<>/dev/tcp/localhost/11211; cat >&3; timeout 0.5 cat <&3; exec 3<&-)"',
        ]
      interval: 20s
      timeout: 5s
      retries: 10

  seafile:
    image: seafileltd/seafile-mc:12.0-latest
    volumes:
      - seafile-data:/shared
    environment:
      - DB_HOST=${SEAFILE_MYSQL_DB_HOST:-seafile-db}
      - DB_PORT=${SEAFILE_MYSQL_DB_PORT:-3306}
      - DB_USER=${SEAFILE_MYSQL_DB_USER:-seafile}
      - DB_ROOT_PASSWD=${INIT_SEAFILE_MYSQL_ROOT_PASSWORD:-}
      - DB_PASSWORD=${SEAFILE_MYSQL_DB_PASSWORD:?Variable is not set or empty}
      - SEAFILE_MYSQL_DB_CCNET_DB_NAME=${SEAFILE_MYSQL_DB_CCNET_DB_NAME:-ccnet_db}
      - SEAFILE_MYSQL_DB_SEAFILE_DB_NAME=${SEAFILE_MYSQL_DB_SEAFILE_DB_NAME:-seafile_db}
      - SEAFILE_MYSQL_DB_SEAHUB_DB_NAME=${SEAFILE_MYSQL_DB_SEAHUB_DB_NAME:-seahub_db}
      - TIME_ZONE=${TIME_ZONE:-Etc/UTC}
      - INIT_SEAFILE_ADMIN_EMAIL=${INIT_SEAFILE_ADMIN_EMAIL:[email protected]}
      - INIT_SEAFILE_ADMIN_PASSWORD=${INIT_SEAFILE_ADMIN_PASSWORD:-asecret}
      - SEAFILE_SERVER_HOSTNAME=${SEAFILE_SERVER_HOSTNAME:?Variable is not set or empty}
      - SEAFILE_SERVER_PROTOCOL=${SEAFILE_SERVER_PROTOCOL:-http}
      - SITE_ROOT=${SITE_ROOT:-/}
      - NON_ROOT=${NON_ROOT:-false}
      - JWT_PRIVATE_KEY=${JWT_PRIVATE_KEY:?Variable is not set or empty}
      - SEAFILE_LOG_TO_STDOUT=${SEAFILE_LOG_TO_STDOUT:-true}
    depends_on:
      seafile-db:
        condition: service_healthy
      memcached:
        condition: service_started
    networks:
      - seafile-net
    healthcheck:
      test: ["CMD", "curl", "-f", "http://127.0.0.1:80/api2/ping"]
      interval: 20s
      timeout: 5s
      retries: 10

networks:
  seafile-net:
    name: seafile-net

volumes:
  seafile-mysql-db:
  seafile-data:
```

```
[variables]
main_domain = "${domain}"
mysql_root_password = "${password:32}"
mysql_user_password = "${password:32}"
admin_password = "${password:32}"
jwt_private_key = "${password:32}"

[[config.domains]]
serviceName = "seafile"
port = 80
host = "${main_domain}"

[config.env]
SEAFILE_MYSQL_DB_HOST = "seafile-db"
SEAFILE_MYSQL_DB_USER = "seafile"
SEAFILE_MYSQL_DB_PASSWORD = "${mysql_user_password}"
INIT_SEAFILE_MYSQL_ROOT_PASSWORD = "${mysql_root_password}"

TIME_ZONE = "Etc/UTC"
JWT_PRIVATE_KEY = "${jwt_private_key}"
SEAFILE_SERVER_PROTOCOL = "https"
SEAFILE_SERVER_HOSTNAME = "${main_domain}"
INIT_SEAFILE_ADMIN_EMAIL = "[email protected]"
INIT_SEAFILE_ADMIN_PASSWORD = "${admin_password}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogIiMgaHR0cHM6Ly9tYW51YWwuc2VhZmlsZS5jb20vMTIuMC9zZXR1cC9zZXR1cF9jZV9ieV9kb2NrZXJcbiNcbiMgVGhpcyBEb2twbG95IHRlbXBsYXRlIGZvciBzZWFmaWxlIHNldHMgdGhlIGRlZmF1bHQgY3JlZGVudGlhbHMgdG86XG4jICAgVVNFUk5BTUU6IGFkbWluQGV4YW1wbGUuY29tXG4jICAgUEFTU1dPUkQ6IDxTRUNSRVQgR0VORVJBVEVEIElOIEVOVklST05NRU5UIFZBUklBQkxFUz5cbiNcbiMgISEhIElNUE9SVEFOVCAhISFcbiMgICAgIFBsZWFzZSBsb29rIGF0IHRoZSBlbnZpcm9ubWVudCB2YXJpYWJsZSBzZXR0aW5ncyBhbmQgdHdlYWtcbiMgICAgIHRoZW0gcHJpb3IgdG8gdGhlIGZpcnN0IGRlcGxveW1lbnQhXG4jXG4jICAgICBJZiB5b3UgaGF2ZSBhbHJlYWR5IGRlcGxveWVkIG9uY2UsIGNoYW5nZXMgdG8gc29tZSBlbnZpcm9ubWVudFxuIyAgICAgdmFyaWFibGVzIG1heSBub3QgdGFrZSBlZmZlY3QuIEZvciBleGFtcGxlLCBpbml0aWFsIHBhc3N3b3Jkcy5cblxuc2VydmljZXM6XG4gIHNlYWZpbGUtZGI6XG4gICAgaW1hZ2U6IG1hcmlhZGI6MTAuMTFcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gTVlTUUxfUk9PVF9QQVNTV09SRD0ke0lOSVRfU0VBRklMRV9NWVNRTF9ST09UX1BBU1NXT1JEOi19XG4gICAgICAtIE1ZU1FMX0xPR19DT05TT0xFPXRydWVcbiAgICAgIC0gTUFSSUFEQl9BVVRPX1VQR1JBREU9MVxuICAgIHZvbHVtZXM6XG4gICAgICAtIHNlYWZpbGUtbXlzcWwtZGI6L3Zhci9saWIvbXlzcWxcIlxuICAgIG5ldHdvcmtzOlxuICAgICAgLSBzZWFmaWxlLW5ldFxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDpcbiAgICAgICAgW1xuICAgICAgICAgIFwiQ01EXCIsXG4gICAgICAgICAgXCIvdXNyL2xvY2FsL2Jpbi9oZWFsdGhjaGVjay5zaFwiLFxuICAgICAgICAgIFwiLS1jb25uZWN0XCIsXG4gICAgICAgICAgXCItLW1hcmlhZGJ1cGdyYWRlXCIsXG4gICAgICAgICAgXCItLWlubm9kYl9pbml0aWFsaXplZFwiLFxuICAgICAgICBdXG4gICAgICBpbnRlcnZhbDogMjBzXG4gICAgICBzdGFydF9wZXJpb2Q6IDMwc1xuICAgICAgdGltZW91dDogNXNcbiAgICAgIHJldHJpZXM6IDEwXG5cbiAgbWVtY2FjaGVkOlxuICAgIGltYWdlOiBtZW1jYWNoZWQ6MS42LjI5XG4gICAgZW50cnlwb2ludDogbWVtY2FjaGVkIC1tIDI1NlxuICAgIG5ldHdvcmtzOlxuICAgICAgLSBzZWFmaWxlLW5ldFxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDpcbiAgICAgICAgW1xuICAgICAgICAgIFwiQ01ELVNIRUxMXCIsXG4gICAgICAgICAgJ2Jhc2ggLWMgXCJlY2hvIHZlcnNpb24gfCAoZXhlYyAzPD4vZGV2L3RjcC9sb2NhbGhvc3QvMTEyMTE7IGNhdCA+JjM7IHRpbWVvdXQgMC41IGNhdCA8JjM7IGV4ZWMgMzwmLSlcIicsXG4gICAgICAgIF1cbiAgICAgIGludGVydmFsOiAyMHNcbiAgICAgIHRpbWVvdXQ6IDVzXG4gICAgICByZXRyaWVzOiAxMFxuXG4gIHNlYWZpbGU6XG4gICAgaW1hZ2U6IHNlYWZpbGVsdGQvc2VhZmlsZS1tYzoxMi4wLWxhdGVzdFxuICAgIHZvbHVtZXM6XG4gICAgICAtIHNlYWZpbGUtZGF0YTovc2hhcmVkXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIERCX0hPU1Q9JHtTRUFGSUxFX01ZU1FMX0RCX0hPU1Q6LXNlYWZpbGUtZGJ9XG4gICAgICAtIERCX1BPUlQ9JHtTRUFGSUxFX01ZU1FMX0RCX1BPUlQ6LTMzMDZ9XG4gICAgICAtIERCX1VTRVI9JHtTRUFGSUxFX01ZU1FMX0RCX1VTRVI6LXNlYWZpbGV9XG4gICAgICAtIERCX1JPT1RfUEFTU1dEPSR7SU5JVF9TRUFGSUxFX01ZU1FMX1JPT1RfUEFTU1dPUkQ6LX1cbiAgICAgIC0gREJfUEFTU1dPUkQ9JHtTRUFGSUxFX01ZU1FMX0RCX1BBU1NXT1JEOj9WYXJpYWJsZSBpcyBub3Qgc2V0IG9yIGVtcHR5fVxuICAgICAgLSBTRUFGSUxFX01ZU1FMX0RCX0NDTkVUX0RCX05BTUU9JHtTRUFGSUxFX01ZU1FMX0RCX0NDTkVUX0RCX05BTUU6LWNjbmV0X2RifVxuICAgICAgLSBTRUFGSUxFX01ZU1FMX0RCX1NFQUZJTEVfREJfTkFNRT0ke1NFQUZJTEVfTVlTUUxfREJfU0VBRklMRV9EQl9OQU1FOi1zZWFmaWxlX2RifVxuICAgICAgLSBTRUFGSUxFX01ZU1FMX0RCX1NFQUhVQl9EQl9OQU1FPSR7U0VBRklMRV9NWVNRTF9EQl9TRUFIVUJfREJfTkFNRTotc2VhaHViX2RifVxuICAgICAgLSBUSU1FX1pPTkU9JHtUSU1FX1pPTkU6LUV0Yy9VVEN9XG4gICAgICAtIElOSVRfU0VBRklMRV9BRE1JTl9FTUFJTD0ke0lOSVRfU0VBRklMRV9BRE1JTl9FTUFJTDotbWVAZXhhbXBsZS5jb219XG4gICAgICAtIElOSVRfU0VBRklMRV9BRE1JTl9QQVNTV09SRD0ke0lOSVRfU0VBRklMRV9BRE1JTl9QQVNTV09SRDotYXNlY3JldH1cbiAgICAgIC0gU0VBRklMRV9TRVJWRVJfSE9TVE5BTUU9JHtTRUFGSUxFX1NFUlZFUl9IT1NUTkFNRTo/VmFyaWFibGUgaXMgbm90IHNldCBvciBlbXB0eX1cbiAgICAgIC0gU0VBRklMRV9TRVJWRVJfUFJPVE9DT0w9JHtTRUFGSUxFX1NFUlZFUl9QUk9UT0NPTDotaHR0cH1cbiAgICAgIC0gU0lURV9ST09UPSR7U0lURV9ST09UOi0vfVxuICAgICAgLSBOT05fUk9PVD0ke05PTl9ST09UOi1mYWxzZX1cbiAgICAgIC0gSldUX1BSSVZBVEVfS0VZPSR7SldUX1BSSVZBVEVfS0VZOj9WYXJpYWJsZSBpcyBub3Qgc2V0IG9yIGVtcHR5fVxuICAgICAgLSBTRUFGSUxFX0xPR19UT19TVERPVVQ9JHtTRUFGSUxFX0xPR19UT19TVERPVVQ6LXRydWV9XG4gICAgZGVwZW5kc19vbjpcbiAgICAgIHNlYWZpbGUtZGI6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9oZWFsdGh5XG4gICAgICBtZW1jYWNoZWQ6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9zdGFydGVkXG4gICAgbmV0d29ya3M6XG4gICAgICAtIHNlYWZpbGUtbmV0XG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OiBbXCJDTURcIiwgXCJjdXJsXCIsIFwiLWZcIiwgXCJodHRwOi8vMTI3LjAuMC4xOjgwL2FwaTIvcGluZ1wiXVxuICAgICAgaW50ZXJ2YWw6IDIwc1xuICAgICAgdGltZW91dDogNXNcbiAgICAgIHJldHJpZXM6IDEwXG5cbm5ldHdvcmtzOlxuICBzZWFmaWxlLW5ldDpcbiAgICBuYW1lOiBzZWFmaWxlLW5ldFxuXG52b2x1bWVzOlxuICBzZWFmaWxlLW15c3FsLWRiOlxuICBzZWFmaWxlLWRhdGE6XG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxubXlzcWxfcm9vdF9wYXNzd29yZCA9IFwiJHtwYXNzd29yZDozMn1cIlxubXlzcWxfdXNlcl9wYXNzd29yZCA9IFwiJHtwYXNzd29yZDozMn1cIlxuYWRtaW5fcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcbmp3dF9wcml2YXRlX2tleSA9IFwiJHtwYXNzd29yZDozMn1cIlxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJzZWFmaWxlXCJcbnBvcnQgPSA4MFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cblNFQUZJTEVfTVlTUUxfREJfSE9TVCA9IFwic2VhZmlsZS1kYlwiXG5TRUFGSUxFX01ZU1FMX0RCX1VTRVIgPSBcInNlYWZpbGVcIlxuU0VBRklMRV9NWVNRTF9EQl9QQVNTV09SRCA9IFwiJHtteXNxbF91c2VyX3Bhc3N3b3JkfVwiXG5JTklUX1NFQUZJTEVfTVlTUUxfUk9PVF9QQVNTV09SRCA9IFwiJHtteXNxbF9yb290X3Bhc3N3b3JkfVwiXG5cblRJTUVfWk9ORSA9IFwiRXRjL1VUQ1wiXG5KV1RfUFJJVkFURV9LRVkgPSBcIiR7and0X3ByaXZhdGVfa2V5fVwiXG5TRUFGSUxFX1NFUlZFUl9QUk9UT0NPTCA9IFwiaHR0cHNcIlxuU0VBRklMRV9TRVJWRVJfSE9TVE5BTUUgPSBcIiR7bWFpbl9kb21haW59XCJcbklOSVRfU0VBRklMRV9BRE1JTl9FTUFJTCA9IFwiYWRtaW5AZXhhbXBsZS5jb21cIlxuSU5JVF9TRUFGSUxFX0FETUlOX1BBU1NXT1JEID0gXCIke2FkbWluX3Bhc3N3b3JkfVwiXG4iCn0=
```

## Links

`file-manager`,`file-sharing`,`storage`

---

Version:`12.0-latest`

ScryptedScrypted is a home automation platform that integrates with various smart home devices and provides NVR capabilities for video surveillance.

SearXNGSearXNG is a privacy-respecting, hackable metasearch engine that aggregates results from various search engines without tracking users.

### On this page

ConfigurationBase64LinksTags