---
title: "Dolibarr | Dokploy"
source: "https://docs.dokploy.com/docs/templates/dolibarr"
category: dokploy-docs
created: "2026-06-25T17:21:46.245Z"
---

Dolibarr | Dokploy

# Dolibarr

Copy as Markdown

Dolibarr ERP & CRM is a modern software package that helps manage your organization's activities (contacts, quotes, invoices, orders, stocks, agenda, human resources, ecm, manufacturing).

## Configuration

docker-compose.ymltemplate.toml

```
services:
  dolibarr:
    image: dolibarr/dolibarr:21.0.0
    restart: always
    environment:
      DOLI_DB_HOST: db
      DOLI_DB_NAME: $DB_NAME
      DOLI_DB_USER: $DB_USER
      DOLI_DB_PASSWORD: $DB_PASSWORD
      DOLI_URL_ROOT: ${DOLIBARR_HOST}
      DOLI_ADMIN_LOGIN: admin
      DOLI_ADMIN_PASSWORD: $ADMIN_PASSWORD
    volumes:
      - dolibarr_documents:/var/www/documents
      - dolibarr_html:/var/www/html
    depends_on:
      db:
        condition: service_healthy

  db:
    image: mariadb:10.11
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: $DB_ROOT_PASSWORD
      MYSQL_DATABASE: $DB_NAME
      MYSQL_USER: $DB_USER
      MYSQL_PASSWORD: $DB_PASSWORD
    volumes:
      - db_data:/var/lib/mysql
    healthcheck:
      test: ["CMD-SHELL", "healthcheck.sh --connect --innodb_initialized"]
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 30s

volumes:
  dolibarr_documents:
  dolibarr_html:
  db_data:
```

```
[variables]
main_domain = "${domain}"
db_name = "dolibarr"
db_user = "dolibarr"
db_password = "${password:32}"
db_root_password = "${password:32}"
admin_password = "${password:32}"

[config]
env = [
  "DOLIBARR_HOST=${main_domain}",
  "DB_NAME=${db_name}",
  "DB_USER=${db_user}",
  "DB_PASSWORD=${db_password}",
  "DB_ROOT_PASSWORD=${db_root_password}",
  "ADMIN_PASSWORD=${admin_password}"
]
mounts = []

[[config.domains]]
serviceName = "dolibarr"
port = 80
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBkb2xpYmFycjpcbiAgICBpbWFnZTogZG9saWJhcnIvZG9saWJhcnI6MjEuMC4wXG4gICAgcmVzdGFydDogYWx3YXlzXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBET0xJX0RCX0hPU1Q6IGRiXG4gICAgICBET0xJX0RCX05BTUU6ICREQl9OQU1FXG4gICAgICBET0xJX0RCX1VTRVI6ICREQl9VU0VSXG4gICAgICBET0xJX0RCX1BBU1NXT1JEOiAkREJfUEFTU1dPUkRcbiAgICAgIERPTElfVVJMX1JPT1Q6ICR7RE9MSUJBUlJfSE9TVH1cbiAgICAgIERPTElfQURNSU5fTE9HSU46IGFkbWluXG4gICAgICBET0xJX0FETUlOX1BBU1NXT1JEOiAkQURNSU5fUEFTU1dPUkRcbiAgICB2b2x1bWVzOlxuICAgICAgLSBkb2xpYmFycl9kb2N1bWVudHM6L3Zhci93d3cvZG9jdW1lbnRzXG4gICAgICAtIGRvbGliYXJyX2h0bWw6L3Zhci93d3cvaHRtbFxuICAgIGRlcGVuZHNfb246XG4gICAgICBkYjpcbiAgICAgICAgY29uZGl0aW9uOiBzZXJ2aWNlX2hlYWx0aHlcblxuICBkYjpcbiAgICBpbWFnZTogbWFyaWFkYjoxMC4xMVxuICAgIHJlc3RhcnQ6IGFsd2F5c1xuICAgIGVudmlyb25tZW50OlxuICAgICAgTVlTUUxfUk9PVF9QQVNTV09SRDogJERCX1JPT1RfUEFTU1dPUkRcbiAgICAgIE1ZU1FMX0RBVEFCQVNFOiAkREJfTkFNRVxuICAgICAgTVlTUUxfVVNFUjogJERCX1VTRVJcbiAgICAgIE1ZU1FMX1BBU1NXT1JEOiAkREJfUEFTU1dPUkRcbiAgICB2b2x1bWVzOlxuICAgICAgLSBkYl9kYXRhOi92YXIvbGliL215c3FsXG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OiBbXCJDTUQtU0hFTExcIiwgXCJoZWFsdGhjaGVjay5zaCAtLWNvbm5lY3QgLS1pbm5vZGJfaW5pdGlhbGl6ZWRcIl1cbiAgICAgIGludGVydmFsOiAxMHNcbiAgICAgIHRpbWVvdXQ6IDVzXG4gICAgICByZXRyaWVzOiA1XG4gICAgICBzdGFydF9wZXJpb2Q6IDMwc1xuXG52b2x1bWVzOlxuICBkb2xpYmFycl9kb2N1bWVudHM6XG4gIGRvbGliYXJyX2h0bWw6XG4gIGRiX2RhdGE6XG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuZGJfbmFtZSA9IFwiZG9saWJhcnJcIlxuZGJfdXNlciA9IFwiZG9saWJhcnJcIlxuZGJfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcbmRiX3Jvb3RfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcbmFkbWluX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5cbltjb25maWddXG5lbnYgPSBbXG4gIFwiRE9MSUJBUlJfSE9TVD0ke21haW5fZG9tYWlufVwiLFxuICBcIkRCX05BTUU9JHtkYl9uYW1lfVwiLFxuICBcIkRCX1VTRVI9JHtkYl91c2VyfVwiLFxuICBcIkRCX1BBU1NXT1JEPSR7ZGJfcGFzc3dvcmR9XCIsXG4gIFwiREJfUk9PVF9QQVNTV09SRD0ke2RiX3Jvb3RfcGFzc3dvcmR9XCIsXG4gIFwiQURNSU5fUEFTU1dPUkQ9JHthZG1pbl9wYXNzd29yZH1cIlxuXVxubW91bnRzID0gW11cblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiZG9saWJhcnJcIlxucG9ydCA9IDgwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG4iCn0=
```

## Links

`erp`,`crm`,`business`,`management`,`invoicing`

---

Version:`21.0.0`

Dokploy Prometheus Monitoring ExtensionDokploy monitoring extension with Prometheus metrics export for external monitoring systems like Grafana Cloud. Tracks server and container metrics with configurable thresholds and alerting.

Domain LockerDomain Locker is an open-source tool for tracking domain expirations and sending renewal reminders.

### On this page

ConfigurationBase64LinksTags