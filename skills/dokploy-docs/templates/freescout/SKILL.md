---
title: "FreeScout | Dokploy"
source: "https://docs.dokploy.com/docs/templates/freescout"
category: dokploy-docs
created: "2026-06-25T17:21:48.521Z"
---

FreeScout | Dokploy

# FreeScout

Copy as Markdown

FreeScout is a free open source help desk and shared inbox system. It's a self-hosted alternative to HelpScout, Zendesk, and similar services that allows you to manage customer communications through email and a clean web interface. FreeScout makes it easy to organize support requests, track customer conversations, and collaborate with your team.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  freescout-db:
    image: mariadb:10.6
    volumes:
      - freescout-db-data:/var/lib/mysql
    environment:
      MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD}
      MYSQL_DATABASE: ${DB_NAME}
      MYSQL_USER: ${DB_USER}
      MYSQL_PASSWORD: ${DB_PASS}
    healthcheck:
      test:
        [
          "CMD",
          "mysqladmin",
          "ping",
          "-h",
          "localhost",
          "-u",
          "root",
          "-p${MYSQL_ROOT_PASSWORD}",
        ]
      interval: 10s
      timeout: 5s
      retries: 5
    restart: unless-stopped

  freescout:
    image: tiredofit/freescout:latest
    volumes:
      - freescout-data:/data
      - freescout-html:/www/html
      - freescout-logs:/www/logs
    depends_on:
      freescout-db:
        condition: service_healthy
    environment:
      - ADMIN_EMAIL=${ADMIN_EMAIL}
      - ADMIN_PASS=${ADMIN_PASS}
      - ADMIN_FIRST_NAME=${ADMIN_FIRST_NAME}
      - ADMIN_LAST_NAME=${ADMIN_LAST_NAME}
      - SITE_URL=${SITE_URL}
      - DB_HOST=freescout-db
      - DB_PORT=3306
      - DB_TYPE=mysql
      - DB_NAME=${DB_NAME}
      - DB_USER=${DB_USER}
      - DB_PASS=${DB_PASS}
      - APPLICATION_NAME=${APPLICATION_NAME}
      - SETUP_TYPE=AUTO
      - ENABLE_AUTO_UPDATE=TRUE
      - DISPLAY_ERRORS=FALSE
      - APP_PROXY=${APP_PROXY}
      - APP_TRUSTED_PROXIES=${APP_TRUSTED_PROXIES}
    restart: unless-stopped

volumes:
  freescout-db-data:
  freescout-data:
  freescout-html:
  freescout-logs:
```

```
[variables]
main_domain = "${domain}"
mysql_root_password = "${password:16}"
admin_email = "${email}"
admin_password = "${password:16}"
db_name = "freescout"
db_user = "freescout_user"
db_pass = "${password:16}"

[config]
mounts = []

[[config.domains]]
serviceName = "freescout"
port = 80
host = "${main_domain}"

[config.env]
MYSQL_ROOT_PASSWORD = "${mysql_root_password}"
DB_NAME = "${db_name}"
DB_USER = "${db_user}"
DB_PASS = "${db_pass}"
ADMIN_EMAIL = "${admin_email}"
ADMIN_PASS = "${admin_password}"
ADMIN_FIRST_NAME = "Admin"
ADMIN_LAST_NAME = "User"
SITE_URL = "http://${main_domain}"
APPLICATION_NAME = "Customer Support"
APP_PROXY = ""
APP_TRUSTED_PROXIES = "172.16.0.0/12,192.168.0.0/16,10.0.0.0/8"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBmcmVlc2NvdXQtZGI6XG4gICAgaW1hZ2U6IG1hcmlhZGI6MTAuNlxuICAgIHZvbHVtZXM6XG4gICAgICAtIGZyZWVzY291dC1kYi1kYXRhOi92YXIvbGliL215c3FsXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBNWVNRTF9ST09UX1BBU1NXT1JEOiAke01ZU1FMX1JPT1RfUEFTU1dPUkR9XG4gICAgICBNWVNRTF9EQVRBQkFTRTogJHtEQl9OQU1FfVxuICAgICAgTVlTUUxfVVNFUjogJHtEQl9VU0VSfVxuICAgICAgTVlTUUxfUEFTU1dPUkQ6ICR7REJfUEFTU31cbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6XG4gICAgICAgIFtcbiAgICAgICAgICBcIkNNRFwiLFxuICAgICAgICAgIFwibXlzcWxhZG1pblwiLFxuICAgICAgICAgIFwicGluZ1wiLFxuICAgICAgICAgIFwiLWhcIixcbiAgICAgICAgICBcImxvY2FsaG9zdFwiLFxuICAgICAgICAgIFwiLXVcIixcbiAgICAgICAgICBcInJvb3RcIixcbiAgICAgICAgICBcIi1wJHtNWVNRTF9ST09UX1BBU1NXT1JEfVwiLFxuICAgICAgICBdXG4gICAgICBpbnRlcnZhbDogMTBzXG4gICAgICB0aW1lb3V0OiA1c1xuICAgICAgcmV0cmllczogNVxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG5cbiAgZnJlZXNjb3V0OlxuICAgIGltYWdlOiB0aXJlZG9maXQvZnJlZXNjb3V0OmxhdGVzdFxuICAgIHZvbHVtZXM6XG4gICAgICAtIGZyZWVzY291dC1kYXRhOi9kYXRhXG4gICAgICAtIGZyZWVzY291dC1odG1sOi93d3cvaHRtbFxuICAgICAgLSBmcmVlc2NvdXQtbG9nczovd3d3L2xvZ3NcbiAgICBkZXBlbmRzX29uOlxuICAgICAgZnJlZXNjb3V0LWRiOlxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2VfaGVhbHRoeVxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBBRE1JTl9FTUFJTD0ke0FETUlOX0VNQUlMfVxuICAgICAgLSBBRE1JTl9QQVNTPSR7QURNSU5fUEFTU31cbiAgICAgIC0gQURNSU5fRklSU1RfTkFNRT0ke0FETUlOX0ZJUlNUX05BTUV9XG4gICAgICAtIEFETUlOX0xBU1RfTkFNRT0ke0FETUlOX0xBU1RfTkFNRX1cbiAgICAgIC0gU0lURV9VUkw9JHtTSVRFX1VSTH1cbiAgICAgIC0gREJfSE9TVD1mcmVlc2NvdXQtZGJcbiAgICAgIC0gREJfUE9SVD0zMzA2XG4gICAgICAtIERCX1RZUEU9bXlzcWxcbiAgICAgIC0gREJfTkFNRT0ke0RCX05BTUV9XG4gICAgICAtIERCX1VTRVI9JHtEQl9VU0VSfVxuICAgICAgLSBEQl9QQVNTPSR7REJfUEFTU31cbiAgICAgIC0gQVBQTElDQVRJT05fTkFNRT0ke0FQUExJQ0FUSU9OX05BTUV9XG4gICAgICAtIFNFVFVQX1RZUEU9QVVUT1xuICAgICAgLSBFTkFCTEVfQVVUT19VUERBVEU9VFJVRVxuICAgICAgLSBESVNQTEFZX0VSUk9SUz1GQUxTRVxuICAgICAgLSBBUFBfUFJPWFk9JHtBUFBfUFJPWFl9XG4gICAgICAtIEFQUF9UUlVTVEVEX1BST1hJRVM9JHtBUFBfVFJVU1RFRF9QUk9YSUVTfVxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG5cbnZvbHVtZXM6XG4gIGZyZWVzY291dC1kYi1kYXRhOlxuICBmcmVlc2NvdXQtZGF0YTpcbiAgZnJlZXNjb3V0LWh0bWw6XG4gIGZyZWVzY291dC1sb2dzOlxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbm15c3FsX3Jvb3RfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MTZ9XCJcbmFkbWluX2VtYWlsID0gXCIke2VtYWlsfVwiXG5hZG1pbl9wYXNzd29yZCA9IFwiJHtwYXNzd29yZDoxNn1cIlxuZGJfbmFtZSA9IFwiZnJlZXNjb3V0XCJcbmRiX3VzZXIgPSBcImZyZWVzY291dF91c2VyXCJcbmRiX3Bhc3MgPSBcIiR7cGFzc3dvcmQ6MTZ9XCJcblxuW2NvbmZpZ11cbm1vdW50cyA9IFtdXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImZyZWVzY291dFwiXG5wb3J0ID0gODBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5NWVNRTF9ST09UX1BBU1NXT1JEID0gXCIke215c3FsX3Jvb3RfcGFzc3dvcmR9XCJcbkRCX05BTUUgPSBcIiR7ZGJfbmFtZX1cIlxuREJfVVNFUiA9IFwiJHtkYl91c2VyfVwiXG5EQl9QQVNTID0gXCIke2RiX3Bhc3N9XCJcbkFETUlOX0VNQUlMID0gXCIke2FkbWluX2VtYWlsfVwiXG5BRE1JTl9QQVNTID0gXCIke2FkbWluX3Bhc3N3b3JkfVwiXG5BRE1JTl9GSVJTVF9OQU1FID0gXCJBZG1pblwiXG5BRE1JTl9MQVNUX05BTUUgPSBcIlVzZXJcIlxuU0lURV9VUkwgPSBcImh0dHA6Ly8ke21haW5fZG9tYWlufVwiXG5BUFBMSUNBVElPTl9OQU1FID0gXCJDdXN0b21lciBTdXBwb3J0XCJcbkFQUF9QUk9YWSA9IFwiXCJcbkFQUF9UUlVTVEVEX1BST1hJRVMgPSBcIjE3Mi4xNi4wLjAvMTIsMTkyLjE2OC4wLjAvMTYsMTAuMC4wLjAvOFwiXG4iCn0=
```

## Links

`helpdesk`,`support`,`email`,`customer-service`,`self-hosted`

---

Version:`latest`

Frappe HRFeature rich HR & Payroll software. 100% FOSS and customizable.

FreshRSSA free, self-hostable RSS and Atom feed aggregator. Lightweight, easy to work with, powerful, and customizable with themes and extensions.

### On this page

ConfigurationBase64LinksTags