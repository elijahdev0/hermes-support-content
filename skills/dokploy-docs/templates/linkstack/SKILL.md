---
title: "LinkStack | Dokploy"
source: "https://docs.dokploy.com/docs/templates/linkstack"
category: dokploy-docs
created: "2026-06-25T17:21:52.046Z"
---

LinkStack | Dokploy

# LinkStack

Copy as Markdown

LinkStack is an open-source link-in-bio platform for sharing multiple links using a customizable landing page.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  linkstack:
    image: linkstackorg/linkstack:latest
    environment:
      TZ: "Europe/Berlin"
      SERVER_ADMIN: "${admin_email}"
      HTTP_SERVER_NAME: "${main_domain}"
      HTTPS_SERVER_NAME: "${main_domain}"
      LOG_LEVEL: "info"
      PHP_MEMORY_LIMIT: "256M"
      UPLOAD_MAX_FILESIZE: "8M"
    volumes:
      - linkstack-data:/htdocs
    restart: unless-stopped
    depends_on:
      - mysql

  mysql:
    image: mysql:8
    environment:
      MYSQL_ROOT_PASSWORD: ${mysql_root_password}
    volumes:
      - mysql-data:/var/lib/mysql
    restart: unless-stopped

volumes:
  linkstack-data: {}
  mysql-data: {}
```

```
[variables]
main_domain = "${domain}"
admin_email = "${email}"
mysql_root_password = "${password:32}"

[config]
[[config.domains]]
serviceName = "linkstack"
port = 80
host = "${main_domain}"

[config.env]
TZ = "Europe/Berlin"
SERVER_ADMIN = "${admin_email}"
HTTP_SERVER_NAME = "${main_domain}"
HTTPS_SERVER_NAME = "${main_domain}"
LOG_LEVEL = "info"
PHP_MEMORY_LIMIT = "256M"
UPLOAD_MAX_FILESIZE = "8M"
MYSQL_ROOT_PASSWORD = "${mysql_root_password}"

[[config.mounts]]
volume = "linkstack-data"
target = "/htdocs"

[[config.mounts]]
volume = "mysql-data"
target = "/var/lib/mysql"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIGxpbmtzdGFjazpcbiAgICBpbWFnZTogbGlua3N0YWNrb3JnL2xpbmtzdGFjazpsYXRlc3RcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIFRaOiBcIkV1cm9wZS9CZXJsaW5cIlxuICAgICAgU0VSVkVSX0FETUlOOiBcIiR7YWRtaW5fZW1haWx9XCJcbiAgICAgIEhUVFBfU0VSVkVSX05BTUU6IFwiJHttYWluX2RvbWFpbn1cIlxuICAgICAgSFRUUFNfU0VSVkVSX05BTUU6IFwiJHttYWluX2RvbWFpbn1cIlxuICAgICAgTE9HX0xFVkVMOiBcImluZm9cIlxuICAgICAgUEhQX01FTU9SWV9MSU1JVDogXCIyNTZNXCJcbiAgICAgIFVQTE9BRF9NQVhfRklMRVNJWkU6IFwiOE1cIlxuICAgIHZvbHVtZXM6XG4gICAgICAtIGxpbmtzdGFjay1kYXRhOi9odGRvY3NcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGRlcGVuZHNfb246XG4gICAgICAtIG15c3FsXG5cbiAgbXlzcWw6XG4gICAgaW1hZ2U6IG15c3FsOjhcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIE1ZU1FMX1JPT1RfUEFTU1dPUkQ6ICR7bXlzcWxfcm9vdF9wYXNzd29yZH1cbiAgICB2b2x1bWVzOlxuICAgICAgLSBteXNxbC1kYXRhOi92YXIvbGliL215c3FsXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcblxudm9sdW1lczpcbiAgbGlua3N0YWNrLWRhdGE6IHt9XG4gIG15c3FsLWRhdGE6IHt9XG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuYWRtaW5fZW1haWwgPSBcIiR7ZW1haWx9XCJcbm15c3FsX3Jvb3RfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcblxuW2NvbmZpZ11cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImxpbmtzdGFja1wiXG5wb3J0ID0gODBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5UWiA9IFwiRXVyb3BlL0JlcmxpblwiXG5TRVJWRVJfQURNSU4gPSBcIiR7YWRtaW5fZW1haWx9XCJcbkhUVFBfU0VSVkVSX05BTUUgPSBcIiR7bWFpbl9kb21haW59XCJcbkhUVFBTX1NFUlZFUl9OQU1FID0gXCIke21haW5fZG9tYWlufVwiXG5MT0dfTEVWRUwgPSBcImluZm9cIlxuUEhQX01FTU9SWV9MSU1JVCA9IFwiMjU2TVwiXG5VUExPQURfTUFYX0ZJTEVTSVpFID0gXCI4TVwiXG5NWVNRTF9ST09UX1BBU1NXT1JEID0gXCIke215c3FsX3Jvb3RfcGFzc3dvcmR9XCJcblxuW1tjb25maWcubW91bnRzXV1cbnZvbHVtZSA9IFwibGlua3N0YWNrLWRhdGFcIlxudGFyZ2V0ID0gXCIvaHRkb2NzXCJcblxuW1tjb25maWcubW91bnRzXV1cbnZvbHVtZSA9IFwibXlzcWwtZGF0YVwiXG50YXJnZXQgPSBcIi92YXIvbGliL215c3FsXCJcbiIKfQ==
```

## Links

`bio`,`personal`,`cms`,`php`

---

Version:`latest`

LinkdingLinkding is a self-hosted bookmark manager with a clean and simple interface.

LinkwardenSelf-hosted, open-source collaborative bookmark manager to collect, organize and archive webpages.

### On this page

ConfigurationBase64LinksTags