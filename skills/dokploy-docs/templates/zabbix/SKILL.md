---
title: "Zabbix | Dokploy"
source: "https://docs.dokploy.com/docs/templates/zabbix"
category: dokploy-docs
created: "2026-06-25T17:22:02.523Z"
---

Zabbix | Dokploy

# Zabbix

Copy as Markdown

Zabbix is an open-source enterprise-grade monitoring platform for networks, servers, virtual machines, and cloud services. This template includes PostgreSQL, Nginx frontend, SNMP traps, and Java gateway.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  postgres:
    image: postgres:16-alpine
    restart: unless-stopped
    environment:
      POSTGRES_DB: ${POSTGRES_DB}
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    volumes:
      - zabbix-postgres-data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER} -d ${POSTGRES_DB}"]
      interval: 10s
      timeout: 5s
      retries: 5

  zabbix-java-gateway:
    image: zabbix/zabbix-java-gateway:alpine-7.4-latest
    restart: unless-stopped

  zabbix-snmptraps:
    image: zabbix/zabbix-snmptraps:alpine-7.4-latest
    restart: unless-stopped
    volumes:
      - zabbix-snmptraps:/var/lib/zabbix/snmptraps
      - zabbix-mibs:/var/lib/zabbix/mibs

  zabbix-server-pgsql:
    image: zabbix/zabbix-server-pgsql:alpine-7.4-latest
    restart: unless-stopped
    environment:
      DB_SERVER_HOST: postgres
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: ${POSTGRES_DB}
      ZBX_ENABLE_SNMP_TRAPS: "true"
      ZBX_JAVAGATEWAY: zabbix-java-gateway
    depends_on:
      postgres:
        condition: service_healthy
      zabbix-java-gateway:
        condition: service_started
      zabbix-snmptraps:
        condition: service_started
    volumes:
      - zabbix-server-data:/var/lib/zabbix
      - zabbix-snmptraps:/var/lib/zabbix/snmptraps
      - zabbix-mibs:/var/lib/zabbix/mibs
    expose:
      - 10051
    healthcheck:
      test: ["CMD", "pgrep", "zabbix_server"]
      interval: 10s
      timeout: 5s
      retries: 5

  zabbix-web-nginx-pgsql:
    image: zabbix/zabbix-web-nginx-pgsql:alpine-7.4-latest
    restart: unless-stopped
    environment:
      DB_SERVER_HOST: postgres
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: ${POSTGRES_DB}
      ZBX_SERVER_HOST: zabbix-server-pgsql
      PHP_TZ: ${PHP_TZ}
      ZBX_SERVER_NAME: ${ZBX_SERVER_NAME}
    depends_on:
      zabbix-server-pgsql:
        condition: service_healthy
    expose:
      - 8080
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8080/"]
      interval: 30s
      timeout: 10s
      retries: 3

volumes:
  zabbix-postgres-data:
  zabbix-server-data:
  zabbix-snmptraps:
  zabbix-mibs:
```

```
[variables]
main_domain = "${domain}"
postgres_password = "${password:32}"

[config]

[[config.domains]]
serviceName = "zabbix-web-nginx-pgsql"
port = 8080
host = "${main_domain}"

[config.env]
POSTGRES_DB = "zabbix"
POSTGRES_USER = "zabbix"
POSTGRES_PASSWORD = "${postgres_password}"
PHP_TZ = "UTC"
ZBX_SERVER_NAME = "Dokploy Zabbix Monitoring"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIHBvc3RncmVzOlxuICAgIGltYWdlOiBwb3N0Z3JlczoxNi1hbHBpbmVcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGVudmlyb25tZW50OlxuICAgICAgUE9TVEdSRVNfREI6ICR7UE9TVEdSRVNfREJ9XG4gICAgICBQT1NUR1JFU19VU0VSOiAke1BPU1RHUkVTX1VTRVJ9XG4gICAgICBQT1NUR1JFU19QQVNTV09SRDogJHtQT1NUR1JFU19QQVNTV09SRH1cbiAgICB2b2x1bWVzOlxuICAgICAgLSB6YWJiaXgtcG9zdGdyZXMtZGF0YTovdmFyL2xpYi9wb3N0Z3Jlc3FsL2RhdGFcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6IFtcIkNNRC1TSEVMTFwiLCBcInBnX2lzcmVhZHkgLVUgJHtQT1NUR1JFU19VU0VSfSAtZCAke1BPU1RHUkVTX0RCfVwiXVxuICAgICAgaW50ZXJ2YWw6IDEwc1xuICAgICAgdGltZW91dDogNXNcbiAgICAgIHJldHJpZXM6IDVcblxuICB6YWJiaXgtamF2YS1nYXRld2F5OlxuICAgIGltYWdlOiB6YWJiaXgvemFiYml4LWphdmEtZ2F0ZXdheTphbHBpbmUtNy40LWxhdGVzdFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG5cbiAgemFiYml4LXNubXB0cmFwczpcbiAgICBpbWFnZTogemFiYml4L3phYmJpeC1zbm1wdHJhcHM6YWxwaW5lLTcuNC1sYXRlc3RcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIHZvbHVtZXM6XG4gICAgICAtIHphYmJpeC1zbm1wdHJhcHM6L3Zhci9saWIvemFiYml4L3NubXB0cmFwc1xuICAgICAgLSB6YWJiaXgtbWliczovdmFyL2xpYi96YWJiaXgvbWlic1xuXG4gIHphYmJpeC1zZXJ2ZXItcGdzcWw6XG4gICAgaW1hZ2U6IHphYmJpeC96YWJiaXgtc2VydmVyLXBnc3FsOmFscGluZS03LjQtbGF0ZXN0XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIERCX1NFUlZFUl9IT1NUOiBwb3N0Z3Jlc1xuICAgICAgUE9TVEdSRVNfVVNFUjogJHtQT1NUR1JFU19VU0VSfVxuICAgICAgUE9TVEdSRVNfUEFTU1dPUkQ6ICR7UE9TVEdSRVNfUEFTU1dPUkR9XG4gICAgICBQT1NUR1JFU19EQjogJHtQT1NUR1JFU19EQn1cbiAgICAgIFpCWF9FTkFCTEVfU05NUF9UUkFQUzogXCJ0cnVlXCJcbiAgICAgIFpCWF9KQVZBR0FURVdBWTogemFiYml4LWphdmEtZ2F0ZXdheVxuICAgIGRlcGVuZHNfb246XG4gICAgICBwb3N0Z3JlczpcbiAgICAgICAgY29uZGl0aW9uOiBzZXJ2aWNlX2hlYWx0aHlcbiAgICAgIHphYmJpeC1qYXZhLWdhdGV3YXk6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9zdGFydGVkXG4gICAgICB6YWJiaXgtc25tcHRyYXBzOlxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2Vfc3RhcnRlZFxuICAgIHZvbHVtZXM6XG4gICAgICAtIHphYmJpeC1zZXJ2ZXItZGF0YTovdmFyL2xpYi96YWJiaXhcbiAgICAgIC0gemFiYml4LXNubXB0cmFwczovdmFyL2xpYi96YWJiaXgvc25tcHRyYXBzXG4gICAgICAtIHphYmJpeC1taWJzOi92YXIvbGliL3phYmJpeC9taWJzXG4gICAgZXhwb3NlOlxuICAgICAgLSAxMDA1MVxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDogW1wiQ01EXCIsIFwicGdyZXBcIiwgXCJ6YWJiaXhfc2VydmVyXCJdXG4gICAgICBpbnRlcnZhbDogMTBzXG4gICAgICB0aW1lb3V0OiA1c1xuICAgICAgcmV0cmllczogNVxuXG4gIHphYmJpeC13ZWItbmdpbngtcGdzcWw6XG4gICAgaW1hZ2U6IHphYmJpeC96YWJiaXgtd2ViLW5naW54LXBnc3FsOmFscGluZS03LjQtbGF0ZXN0XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIERCX1NFUlZFUl9IT1NUOiBwb3N0Z3Jlc1xuICAgICAgUE9TVEdSRVNfVVNFUjogJHtQT1NUR1JFU19VU0VSfVxuICAgICAgUE9TVEdSRVNfUEFTU1dPUkQ6ICR7UE9TVEdSRVNfUEFTU1dPUkR9XG4gICAgICBQT1NUR1JFU19EQjogJHtQT1NUR1JFU19EQn1cbiAgICAgIFpCWF9TRVJWRVJfSE9TVDogemFiYml4LXNlcnZlci1wZ3NxbFxuICAgICAgUEhQX1RaOiAke1BIUF9UWn1cbiAgICAgIFpCWF9TRVJWRVJfTkFNRTogJHtaQlhfU0VSVkVSX05BTUV9XG4gICAgZGVwZW5kc19vbjpcbiAgICAgIHphYmJpeC1zZXJ2ZXItcGdzcWw6XG4gICAgICAgIGNvbmRpdGlvbjogc2VydmljZV9oZWFsdGh5XG4gICAgZXhwb3NlOlxuICAgICAgLSA4MDgwXG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OiBbXCJDTURcIiwgXCJjdXJsXCIsIFwiLWZcIiwgXCJodHRwOi8vbG9jYWxob3N0OjgwODAvXCJdXG4gICAgICBpbnRlcnZhbDogMzBzXG4gICAgICB0aW1lb3V0OiAxMHNcbiAgICAgIHJldHJpZXM6IDNcblxudm9sdW1lczpcbiAgemFiYml4LXBvc3RncmVzLWRhdGE6XG4gIHphYmJpeC1zZXJ2ZXItZGF0YTpcbiAgemFiYml4LXNubXB0cmFwczpcbiAgemFiYml4LW1pYnM6XG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxucG9zdGdyZXNfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcblxuW2NvbmZpZ11cblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiemFiYml4LXdlYi1uZ2lueC1wZ3NxbFwiXG5wb3J0ID0gODA4MFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cblBPU1RHUkVTX0RCID0gXCJ6YWJiaXhcIlxuUE9TVEdSRVNfVVNFUiA9IFwiemFiYml4XCJcblBPU1RHUkVTX1BBU1NXT1JEID0gXCIke3Bvc3RncmVzX3Bhc3N3b3JkfVwiXG5QSFBfVFogPSBcIlVUQ1wiXG5aQlhfU0VSVkVSX05BTUUgPSBcIkRva3Bsb3kgWmFiYml4IE1vbml0b3JpbmdcIiIKfQ==
```

## Links

`monitoring`,`infrastructure`,`observability`,`alerting`

---

Version:`7.4`

yt-dlp-webuiyt-dlp-webui is a web interface for yt-dlp, allowing you to download videos and audio from various platforms with a simple web UI.

ZiplineA ShareX/file upload server that is easy to use, packed with features, and with an easy setup!

### On this page

ConfigurationBase64LinksTags