---
title: "Wordpress | Dokploy"
source: "https://docs.dokploy.com/docs/templates/wordpress"
category: dokploy-docs
created: "2026-06-25T17:22:01.421Z"
---

Wordpress | Dokploy

# Wordpress

Copy as Markdown

Wordpress is a free and open source content management system (CMS) for publishing and managing websites.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  wordpress:
    image: wordpress:latest
    volumes:
      - wp_app:/var/www/html
      - ../files/uploads.ini:/usr/local/etc/php/conf.d/uploads.ini
    environment:
      WORDPRESS_DB_HOST: wp_db
      WORDPRESS_DB_NAME: $DB_NAME
      WORDPRESS_DB_USER: root
      WORDPRESS_DB_PASSWORD: $DB_PASSWORD
      WORDPRESS_DEBUG: ${WORDPRESS_DEBUG:-0}
      WORDPRESS_CONFIG_EXTRA: |
        define('WP_MEMORY_LIMIT', '256M');
        define('DISALLOW_FILE_EDIT', true);
    depends_on:
      wp_db:
        condition: service_healthy
    restart: unless-stopped

  wp_db:
    image: mysql:8.4
    restart: unless-stopped
    volumes:
      - wp_data:/var/lib/mysql
    environment:
      MYSQL_ROOT_PASSWORD: $DB_PASSWORD
      MYSQL_DATABASE: $DB_NAME
    healthcheck:
      test: ["CMD-SHELL", "exit | mysql -h localhost -P 3306 -u root -p$$MYSQL_ROOT_PASSWORD"]
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 30s

volumes:
  wp_app:
  wp_data:
```

```
[variables]
main_domain = "${domain}"
db_name = "wordpress"
db_user = "wordpress"
db_password = "${password:32}"

[config]
env = [
  "WORDPRESS_DEBUG=0",
  "DB_NAME=${db_name}",
  "DB_USER=${db_user}",
  "DB_PASSWORD=${db_password}"
]

[[config.domains]]
serviceName = "wordpress"
port = 80
host = "${main_domain}"

[[config.mounts]]
filePath = "uploads.ini"
content = """upload_max_filesize = 64M
post_max_size = 64M
memory_limit = 256M
max_execution_time = 300
max_input_vars = 3000
"""
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICB3b3JkcHJlc3M6XG4gICAgaW1hZ2U6IHdvcmRwcmVzczpsYXRlc3RcbiAgICB2b2x1bWVzOlxuICAgICAgLSB3cF9hcHA6L3Zhci93d3cvaHRtbFxuICAgICAgLSAuLi9maWxlcy91cGxvYWRzLmluaTovdXNyL2xvY2FsL2V0Yy9waHAvY29uZi5kL3VwbG9hZHMuaW5pXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBXT1JEUFJFU1NfREJfSE9TVDogd3BfZGJcbiAgICAgIFdPUkRQUkVTU19EQl9OQU1FOiAkREJfTkFNRVxuICAgICAgV09SRFBSRVNTX0RCX1VTRVI6IHJvb3RcbiAgICAgIFdPUkRQUkVTU19EQl9QQVNTV09SRDogJERCX1BBU1NXT1JEXG4gICAgICBXT1JEUFJFU1NfREVCVUc6ICR7V09SRFBSRVNTX0RFQlVHOi0wfVxuICAgICAgV09SRFBSRVNTX0NPTkZJR19FWFRSQTogfFxuICAgICAgICBkZWZpbmUoJ1dQX01FTU9SWV9MSU1JVCcsICcyNTZNJyk7XG4gICAgICAgIGRlZmluZSgnRElTQUxMT1dfRklMRV9FRElUJywgdHJ1ZSk7XG4gICAgZGVwZW5kc19vbjpcbiAgICAgIHdwX2RiOlxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2VfaGVhbHRoeVxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG5cbiAgd3BfZGI6XG4gICAgaW1hZ2U6IG15c3FsOjguNFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgdm9sdW1lczpcbiAgICAgIC0gd3BfZGF0YTovdmFyL2xpYi9teXNxbFxuICAgIGVudmlyb25tZW50OlxuICAgICAgTVlTUUxfUk9PVF9QQVNTV09SRDogJERCX1BBU1NXT1JEXG4gICAgICBNWVNRTF9EQVRBQkFTRTogJERCX05BTUVcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6IFtcIkNNRC1TSEVMTFwiLCBcImV4aXQgfCBteXNxbCAtaCBsb2NhbGhvc3QgLVAgMzMwNiAtdSByb290IC1wJCRNWVNRTF9ST09UX1BBU1NXT1JEXCJdXG4gICAgICBpbnRlcnZhbDogMTBzXG4gICAgICB0aW1lb3V0OiA1c1xuICAgICAgcmV0cmllczogNVxuICAgICAgc3RhcnRfcGVyaW9kOiAzMHNcblxudm9sdW1lczpcbiAgd3BfYXBwOlxuICB3cF9kYXRhOlxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbmRiX25hbWUgPSBcIndvcmRwcmVzc1wiXG5kYl91c2VyID0gXCJ3b3JkcHJlc3NcIlxuZGJfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcblxuW2NvbmZpZ11cbmVudiA9IFtcbiAgXCJXT1JEUFJFU1NfREVCVUc9MFwiLFxuICBcIkRCX05BTUU9JHtkYl9uYW1lfVwiLFxuICBcIkRCX1VTRVI9JHtkYl91c2VyfVwiLFxuICBcIkRCX1BBU1NXT1JEPSR7ZGJfcGFzc3dvcmR9XCJcbl1cblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwid29yZHByZXNzXCJcbnBvcnQgPSA4MFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bW2NvbmZpZy5tb3VudHNdXVxuZmlsZVBhdGggPSBcInVwbG9hZHMuaW5pXCJcbmNvbnRlbnQgPSBcIlwiXCJ1cGxvYWRfbWF4X2ZpbGVzaXplID0gNjRNXG5wb3N0X21heF9zaXplID0gNjRNXG5tZW1vcnlfbGltaXQgPSAyNTZNXG5tYXhfZXhlY3V0aW9uX3RpbWUgPSAzMDBcbm1heF9pbnB1dF92YXJzID0gMzAwMFxuXCJcIlwiICIKfQ==
```

## Links

`cms`

---

Version:`latest`

Windows (dockerized)Windows inside a Docker container.

WuzAPIA RESTful API service for WhatsApp with multiple device support and concurrent sessions.

### On this page

ConfigurationBase64LinksTags