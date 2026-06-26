---
title: "Passbolt | Dokploy"
source: "https://docs.dokploy.com/docs/templates/passbolt"
category: dokploy-docs
created: "2026-06-25T17:21:55.477Z"
---

Passbolt | Dokploy

# Passbolt

Copy as Markdown

Passbolt is an open source credential platform for modern teams. A versatile, battle-tested solution to manage and collaborate on passwords, accesses, and secrets. All in one.

## Configuration

docker-compose.ymltemplate.toml

```
# =============================================================================
# PASSBOLT TEMPLATE - SETUP INSTRUCTIONS
# =============================================================================
#
# After successful deployment, you need to create an admin user:
#
# 1. Go to your Dokploy dashboard
# 2. Navigate to your Passbolt application
# 3. Wait for both containers to be healthy - check the "Monitoring" tab
# 4. Go to the "General" tab and click "Open Terminal" button
# 5. In the terminal, run this command to create admin user:
#    su -s /bin/bash -c "/usr/share/php/passbolt/bin/cake passbolt register_user -u [email protected] -f FirstName -l LastName -r admin" www-data
# 6. Replace [email protected], FirstName, LastName with your actual details
# 7. The command will output a registration link - copy and paste it in your browser to complete setup
#
# NOTE: If you change the domain after deployment, you will need to manually
# update the PASSBOLT_APP_FULL_BASE_URL environment variable in the "Environment" tab.
# =============================================================================

services:
  passbolt:
    image: passbolt/passbolt:latest-ce
    environment:
      APP_FULL_BASE_URL: ${PASSBOLT_APP_FULL_BASE_URL}
      DATASOURCES_DEFAULT_HOST: ${PASSBOLT_DB_HOST}
      DATASOURCES_DEFAULT_PORT: ${PASSBOLT_DB_PORT}
      DATASOURCES_DEFAULT_USERNAME: ${PASSBOLT_DB_USER}
      DATASOURCES_DEFAULT_PASSWORD: ${PASSBOLT_DB_PASSWORD}
      DATASOURCES_DEFAULT_DATABASE: ${PASSBOLT_DB_NAME}
      PASSBOLT_PLUGINS_JWT_AUTHENTICATION_ENABLED: ${PASSBOLT_PLUGINS_JWT_AUTHENTICATION_ENABLED}

      EMAIL_DEFAULT_FROM: ${PASSBOLT_EMAIL_FROM}
      EMAIL_TRANSPORT_DEFAULT_HOST: ${PASSBOLT_EMAIL_HOST}
      EMAIL_TRANSPORT_DEFAULT_PORT: ${PASSBOLT_EMAIL_PORT}
      EMAIL_TRANSPORT_DEFAULT_USERNAME: ${PASSBOLT_EMAIL_USER}
      EMAIL_TRANSPORT_DEFAULT_PASSWORD: ${PASSBOLT_EMAIL_PASS}
      EMAIL_TRANSPORT_DEFAULT_TLS: ${PASSBOLT_EMAIL_TLS}

    volumes:
      - gpg_volume:/etc/passbolt/gpg
      - jwt_volume:/etc/passbolt/jwt

    command:
      - /usr/bin/wait-for.sh
      - "-t"
      - "0"
      - "${PASSBOLT_DB_HOST}:${PASSBOLT_DB_PORT}"
      - "--"
      - /docker-entrypoint.sh

    depends_on:
      mariadb:
        condition: service_healthy

    healthcheck:
      test: ["CMD", "curl", "-f", "http://127.0.0.1:80"]
      interval: 5s
      timeout: 20s
      retries: 10

  mariadb:
    image: mariadb:11
    environment:
      MARIADB_ROOT_PASSWORD: ${PASSBOLT_DB_ROOT_PASSWORD}
      MARIADB_DATABASE: ${PASSBOLT_DB_NAME}
      MARIADB_USER: ${PASSBOLT_DB_USER}
      MARIADB_PASSWORD: ${PASSBOLT_DB_PASSWORD}
    volumes:
      - passbolt_mariadb_data:/var/lib/mysql
    healthcheck:
      test: ["CMD", "mariadb-admin", "ping", "-h", "localhost", "--silent"]
      interval: 10s
      timeout: 5s
      retries: 5

volumes:
  gpg_volume: {}
  jwt_volume: {}
  passbolt_mariadb_data: {}
```

```
[variables]
main_domain = "${domain}"
db_password = "${password:32}"
db_root_password = "${password:32}"
email_host = "smtp.example.com"
email_user = "[email protected]"
email_pass = "${password:16}"

[config]
[[config.domains]]
serviceName = "passbolt"
port = 80
host = "${main_domain}"

[config.env]
PASSBOLT_APP_FULL_BASE_URL = "http://${main_domain}"
PASSBOLT_DB_HOST = "mariadb"
PASSBOLT_DB_PORT = "3306"
PASSBOLT_DB_NAME = "passbolt"
PASSBOLT_DB_USER = "passbolt"
PASSBOLT_DB_PASSWORD = "${db_password}"
PASSBOLT_DB_ROOT_PASSWORD = "${db_root_password}"
PASSBOLT_PLUGINS_JWT_AUTHENTICATION_ENABLED = "true"
PASSBOLT_EMAIL_FROM = "passbolt@${main_domain}"
PASSBOLT_EMAIL_HOST = "${email_host}"
PASSBOLT_EMAIL_PORT = "587"
PASSBOLT_EMAIL_USER = "${email_user}"
PASSBOLT_EMAIL_PASS = "${email_pass}"
PASSBOLT_EMAIL_TLS = "true"

[[config.mounts]]
volume = "gpg_volume"
target = "/etc/passbolt/gpg"

[[config.mounts]]
volume = "jwt_volume"
target = "/etc/passbolt/jwt"

[[config.mounts]]
volume = "passbolt_mariadb_data"
target = "/var/lib/mysql"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogIiMgPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT1cbiMgUEFTU0JPTFQgVEVNUExBVEUgLSBTRVRVUCBJTlNUUlVDVElPTlNcbiMgPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT1cbiNcbiMgQWZ0ZXIgc3VjY2Vzc2Z1bCBkZXBsb3ltZW50LCB5b3UgbmVlZCB0byBjcmVhdGUgYW4gYWRtaW4gdXNlcjpcbiNcbiMgMS4gR28gdG8geW91ciBEb2twbG95IGRhc2hib2FyZFxuIyAyLiBOYXZpZ2F0ZSB0byB5b3VyIFBhc3Nib2x0IGFwcGxpY2F0aW9uXG4jIDMuIFdhaXQgZm9yIGJvdGggY29udGFpbmVycyB0byBiZSBoZWFsdGh5IC0gY2hlY2sgdGhlIFwiTW9uaXRvcmluZ1wiIHRhYlxuIyA0LiBHbyB0byB0aGUgXCJHZW5lcmFsXCIgdGFiIGFuZCBjbGljayBcIk9wZW4gVGVybWluYWxcIiBidXR0b25cbiMgNS4gSW4gdGhlIHRlcm1pbmFsLCBydW4gdGhpcyBjb21tYW5kIHRvIGNyZWF0ZSBhZG1pbiB1c2VyOlxuIyAgICBzdSAtcyAvYmluL2Jhc2ggLWMgXCIvdXNyL3NoYXJlL3BocC9wYXNzYm9sdC9iaW4vY2FrZSBwYXNzYm9sdCByZWdpc3Rlcl91c2VyIC11IHlvdXJlbWFpbEBleGFtcGxlLmNvbSAtZiBGaXJzdE5hbWUgLWwgTGFzdE5hbWUgLXIgYWRtaW5cIiB3d3ctZGF0YVxuIyA2LiBSZXBsYWNlIHlvdXJlbWFpbEBleGFtcGxlLmNvbSwgRmlyc3ROYW1lLCBMYXN0TmFtZSB3aXRoIHlvdXIgYWN0dWFsIGRldGFpbHNcbiMgNy4gVGhlIGNvbW1hbmQgd2lsbCBvdXRwdXQgYSByZWdpc3RyYXRpb24gbGluayAtIGNvcHkgYW5kIHBhc3RlIGl0IGluIHlvdXIgYnJvd3NlciB0byBjb21wbGV0ZSBzZXR1cFxuI1xuIyBOT1RFOiBJZiB5b3UgY2hhbmdlIHRoZSBkb21haW4gYWZ0ZXIgZGVwbG95bWVudCwgeW91IHdpbGwgbmVlZCB0byBtYW51YWxseVxuIyB1cGRhdGUgdGhlIFBBU1NCT0xUX0FQUF9GVUxMX0JBU0VfVVJMIGVudmlyb25tZW50IHZhcmlhYmxlIGluIHRoZSBcIkVudmlyb25tZW50XCIgdGFiLlxuIyA9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PVxuXG5zZXJ2aWNlczpcbiAgcGFzc2JvbHQ6XG4gICAgaW1hZ2U6IHBhc3Nib2x0L3Bhc3Nib2x0OmxhdGVzdC1jZVxuICAgIGVudmlyb25tZW50OlxuICAgICAgQVBQX0ZVTExfQkFTRV9VUkw6ICR7UEFTU0JPTFRfQVBQX0ZVTExfQkFTRV9VUkx9XG4gICAgICBEQVRBU09VUkNFU19ERUZBVUxUX0hPU1Q6ICR7UEFTU0JPTFRfREJfSE9TVH1cbiAgICAgIERBVEFTT1VSQ0VTX0RFRkFVTFRfUE9SVDogJHtQQVNTQk9MVF9EQl9QT1JUfVxuICAgICAgREFUQVNPVVJDRVNfREVGQVVMVF9VU0VSTkFNRTogJHtQQVNTQk9MVF9EQl9VU0VSfVxuICAgICAgREFUQVNPVVJDRVNfREVGQVVMVF9QQVNTV09SRDogJHtQQVNTQk9MVF9EQl9QQVNTV09SRH1cbiAgICAgIERBVEFTT1VSQ0VTX0RFRkFVTFRfREFUQUJBU0U6ICR7UEFTU0JPTFRfREJfTkFNRX1cbiAgICAgIFBBU1NCT0xUX1BMVUdJTlNfSldUX0FVVEhFTlRJQ0FUSU9OX0VOQUJMRUQ6ICR7UEFTU0JPTFRfUExVR0lOU19KV1RfQVVUSEVOVElDQVRJT05fRU5BQkxFRH1cblxuICAgICAgRU1BSUxfREVGQVVMVF9GUk9NOiAke1BBU1NCT0xUX0VNQUlMX0ZST019XG4gICAgICBFTUFJTF9UUkFOU1BPUlRfREVGQVVMVF9IT1NUOiAke1BBU1NCT0xUX0VNQUlMX0hPU1R9XG4gICAgICBFTUFJTF9UUkFOU1BPUlRfREVGQVVMVF9QT1JUOiAke1BBU1NCT0xUX0VNQUlMX1BPUlR9XG4gICAgICBFTUFJTF9UUkFOU1BPUlRfREVGQVVMVF9VU0VSTkFNRTogJHtQQVNTQk9MVF9FTUFJTF9VU0VSfVxuICAgICAgRU1BSUxfVFJBTlNQT1JUX0RFRkFVTFRfUEFTU1dPUkQ6ICR7UEFTU0JPTFRfRU1BSUxfUEFTU31cbiAgICAgIEVNQUlMX1RSQU5TUE9SVF9ERUZBVUxUX1RMUzogJHtQQVNTQk9MVF9FTUFJTF9UTFN9XG5cbiAgICB2b2x1bWVzOlxuICAgICAgLSBncGdfdm9sdW1lOi9ldGMvcGFzc2JvbHQvZ3BnXG4gICAgICAtIGp3dF92b2x1bWU6L2V0Yy9wYXNzYm9sdC9qd3RcblxuICAgIGNvbW1hbmQ6XG4gICAgICAtIC91c3IvYmluL3dhaXQtZm9yLnNoXG4gICAgICAtIFwiLXRcIlxuICAgICAgLSBcIjBcIlxuICAgICAgLSBcIiR7UEFTU0JPTFRfREJfSE9TVH06JHtQQVNTQk9MVF9EQl9QT1JUfVwiXG4gICAgICAtIFwiLS1cIlxuICAgICAgLSAvZG9ja2VyLWVudHJ5cG9pbnQuc2hcblxuICAgIGRlcGVuZHNfb246XG4gICAgICBtYXJpYWRiOlxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2VfaGVhbHRoeVxuXG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OiBbXCJDTURcIiwgXCJjdXJsXCIsIFwiLWZcIiwgXCJodHRwOi8vMTI3LjAuMC4xOjgwXCJdXG4gICAgICBpbnRlcnZhbDogNXNcbiAgICAgIHRpbWVvdXQ6IDIwc1xuICAgICAgcmV0cmllczogMTBcblxuICBtYXJpYWRiOlxuICAgIGltYWdlOiBtYXJpYWRiOjExXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBNQVJJQURCX1JPT1RfUEFTU1dPUkQ6ICR7UEFTU0JPTFRfREJfUk9PVF9QQVNTV09SRH1cbiAgICAgIE1BUklBREJfREFUQUJBU0U6ICR7UEFTU0JPTFRfREJfTkFNRX1cbiAgICAgIE1BUklBREJfVVNFUjogJHtQQVNTQk9MVF9EQl9VU0VSfVxuICAgICAgTUFSSUFEQl9QQVNTV09SRDogJHtQQVNTQk9MVF9EQl9QQVNTV09SRH1cbiAgICB2b2x1bWVzOlxuICAgICAgLSBwYXNzYm9sdF9tYXJpYWRiX2RhdGE6L3Zhci9saWIvbXlzcWxcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6IFtcIkNNRFwiLCBcIm1hcmlhZGItYWRtaW5cIiwgXCJwaW5nXCIsIFwiLWhcIiwgXCJsb2NhbGhvc3RcIiwgXCItLXNpbGVudFwiXVxuICAgICAgaW50ZXJ2YWw6IDEwc1xuICAgICAgdGltZW91dDogNXNcbiAgICAgIHJldHJpZXM6IDVcblxudm9sdW1lczpcbiAgZ3BnX3ZvbHVtZToge31cbiAgand0X3ZvbHVtZToge31cbiAgcGFzc2JvbHRfbWFyaWFkYl9kYXRhOiB7fVxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbmRiX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5kYl9yb290X3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5lbWFpbF9ob3N0ID0gXCJzbXRwLmV4YW1wbGUuY29tXCJcbmVtYWlsX3VzZXIgPSBcIm5vcmVwbHlAZXhhbXBsZS5jb21cIlxuZW1haWxfcGFzcyA9IFwiJHtwYXNzd29yZDoxNn1cIlxuXG5bY29uZmlnXVxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwicGFzc2JvbHRcIlxucG9ydCA9IDgwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuUEFTU0JPTFRfQVBQX0ZVTExfQkFTRV9VUkwgPSBcImh0dHA6Ly8ke21haW5fZG9tYWlufVwiXG5QQVNTQk9MVF9EQl9IT1NUID0gXCJtYXJpYWRiXCJcblBBU1NCT0xUX0RCX1BPUlQgPSBcIjMzMDZcIlxuUEFTU0JPTFRfREJfTkFNRSA9IFwicGFzc2JvbHRcIlxuUEFTU0JPTFRfREJfVVNFUiA9IFwicGFzc2JvbHRcIlxuUEFTU0JPTFRfREJfUEFTU1dPUkQgPSBcIiR7ZGJfcGFzc3dvcmR9XCJcblBBU1NCT0xUX0RCX1JPT1RfUEFTU1dPUkQgPSBcIiR7ZGJfcm9vdF9wYXNzd29yZH1cIlxuUEFTU0JPTFRfUExVR0lOU19KV1RfQVVUSEVOVElDQVRJT05fRU5BQkxFRCA9IFwidHJ1ZVwiXG5QQVNTQk9MVF9FTUFJTF9GUk9NID0gXCJwYXNzYm9sdEAke21haW5fZG9tYWlufVwiXG5QQVNTQk9MVF9FTUFJTF9IT1NUID0gXCIke2VtYWlsX2hvc3R9XCJcblBBU1NCT0xUX0VNQUlMX1BPUlQgPSBcIjU4N1wiXG5QQVNTQk9MVF9FTUFJTF9VU0VSID0gXCIke2VtYWlsX3VzZXJ9XCJcblBBU1NCT0xUX0VNQUlMX1BBU1MgPSBcIiR7ZW1haWxfcGFzc31cIlxuUEFTU0JPTFRfRU1BSUxfVExTID0gXCJ0cnVlXCJcblxuW1tjb25maWcubW91bnRzXV1cbnZvbHVtZSA9IFwiZ3BnX3ZvbHVtZVwiXG50YXJnZXQgPSBcIi9ldGMvcGFzc2JvbHQvZ3BnXCJcblxuW1tjb25maWcubW91bnRzXV1cbnZvbHVtZSA9IFwiand0X3ZvbHVtZVwiXG50YXJnZXQgPSBcIi9ldGMvcGFzc2JvbHQvand0XCJcblxuW1tjb25maWcubW91bnRzXV1cbnZvbHVtZSA9IFwicGFzc2JvbHRfbWFyaWFkYl9kYXRhXCJcbnRhcmdldCA9IFwiL3Zhci9saWIvbXlzcWxcIiIKfQ==
```

## Links

`password-manager`,`security`,`team-collaboration`,`encryption`

---

Version:`latest-ce`

ParseableFast observability and log analytics platform on object storage

PastefyPastefy is an open-source pastebin with support for syntax highlighting and OAuth2 authentication.

### On this page

ConfigurationBase64LinksTags