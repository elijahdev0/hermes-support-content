---
title: "Quant-UX | Dokploy"
source: "https://docs.dokploy.com/docs/templates/quant-ux"
category: dokploy-docs
created: "2026-06-25T17:21:57.937Z"
---

Quant-UX | Dokploy

# Quant-UX

Copy as Markdown

Quant-UX is an open-source UX design and prototyping tool that allows you to create interactive prototypes, conduct user research, and analyze user behavior.

## Configuration

docker-compose.ymltemplate.toml

```
version: '3'

services:
  mongo:
    restart: always
    image: mongo
    volumes:
      - mongo_data:/data/db
  qux-fe:
    restart: always
    image: klausenschaefersinho/quant-ux
    environment:
      - QUX_PROXY_URL=http://quant-ux-backend:8080
      - QUX_AUTH=${QUX_AUTH}
      - QUX_KEYCLOAK_REALM=${QUX_KEYCLOAK_REALM}
      - QUX_KEYCLOAK_CLIENT=${QUX_KEYCLOAK_CLIENT}
      - QUX_KEYCLOAK_URL=${QUX_KEYCLOAK_URL}
      - QUX_WS_URL=${QUX_WS_URL}
    links:
      - mongo
      - qux-be
    ports:
      - 8082
    depends_on:
      - qux-be

  qux-be:
    restart: always
    image: klausenschaefersinho/quant-ux-backend
    volumes:
      - quant_ux_data:/app-data
    environment:
      - QUX_HTTP_HOST=${QUX_HTTP_HOST}
      - QUX_HTTP_PORT=8080
      - QUX_MONGO_DB_NAME=${QUX_MONGO_DB_NAME}
      - QUX_MONGO_TABLE_PREFIX=${QUX_MONGO_TABLE_PREFIX}
      - QUX_MONGO_CONNECTION_STRING=mongodb://quant-ux-mongo:27017
      - QUX_MAIL_USER=${QUX_MAIL_USER}
      - QUX_MAIL_PASSWORD=${QUX_MAIL_PASSWORD}
      - QUX_MAIL_HOST=${QUX_MAIL_HOST}
      - QUX_JWT_PASSWORD=${QUX_JWT_PASSWORD}
      - QUX_IMAGE_FOLDER_USER=/app-data/qux-images
      - QUX_IMAGE_FOLDER_APPS=/app-data/qux-image-apps
      - TZ=${TZ}
      - QUX_AUTH_SERVICE=${QUX_AUTH_SERVICE}
      - QUX_KEYCLOAK_SERVER=${QUX_KEYCLOAK_SERVER}
      - QUX_KEYCLOAK_REALM=${QUX_KEYCLOAK_REALM}
      - QUX_USER_ALLOW_SIGNUP=${QUX_USER_ALLOW_SIGNUP}
      - QUX_USER_ALLOWED_DOMAINS=${QUX_USER_ALLOWED_DOMAINS}
    depends_on:
      - mongo

  qux-ws:
    restart: always
    image: klausenschaefersinho/quant-ux-websocket
    environment:
      - QUX_SERVER=http://quant-ux-backend:8080/
      - QUX_SERVER_PORT=8086
    ports:
      - 8086
    links:
      - qux-be
    depends_on:
      - qux-be

volumes:
  mongo_data:
  quant_ux_data:
```

```
[variables]
main_domain = "${domain}"
ws_domain = "${domain}"
qux_auth = "qux"
qux_jwt_password = "${password:64}"
qux_mongo_db_name = "quantux"
qux_mongo_table_prefix = "quantux"
qux_mail_user = "${email}"
qux_mail_password = "${password:32}"
qux_mail_host = "mail.example.com"
qux_timezone = "America/Chicago"
qux_auth_service = "qux"
qux_user_allow_signup = "true"
qux_user_allowed_domains = "*"
qux_keycloak_realm = ""
qux_keycloak_client = ""
qux_keycloak_url = ""
qux_keycloak_server = ""

[config]
env = [
  "QUX_HTTP_HOST=https://${main_domain}",
  "QUX_AUTH=${qux_auth}",
  "QUX_JWT_PASSWORD=${qux_jwt_password}",
  "QUX_MONGO_DB_NAME=${qux_mongo_db_name}",
  "QUX_MONGO_TABLE_PREFIX=${qux_mongo_table_prefix}",
  "QUX_MAIL_USER=${qux_mail_user}",
  "QUX_MAIL_PASSWORD=${qux_mail_password}",
  "QUX_MAIL_HOST=${qux_mail_host}",
  "TZ=${qux_timezone}",
  "QUX_AUTH_SERVICE=${qux_auth_service}",
  "QUX_KEYCLOAK_SERVER=${qux_keycloak_server}",
  "QUX_KEYCLOAK_REALM=${qux_keycloak_realm}",
  "QUX_KEYCLOAK_CLIENT=${qux_keycloak_client}",
  "QUX_KEYCLOAK_URL=${qux_keycloak_url}",
  "QUX_USER_ALLOW_SIGNUP=${qux_user_allow_signup}",
  "QUX_USER_ALLOWED_DOMAINS=${qux_user_allowed_domains}",
  "QUX_WS_URL=wss://${ws_domain}"
]

[[config.domains]]
serviceName = "qux-fe"
port = 8082
host = "${main_domain}"

[[config.domains]]
serviceName = "qux-ws"
port = 8086
host = "${ws_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246ICczJ1xuXG5zZXJ2aWNlczpcbiAgbW9uZ286XG4gICAgcmVzdGFydDogYWx3YXlzXG4gICAgaW1hZ2U6IG1vbmdvXG4gICAgdm9sdW1lczpcbiAgICAgIC0gbW9uZ29fZGF0YTovZGF0YS9kYlxuICBxdXgtZmU6XG4gICAgcmVzdGFydDogYWx3YXlzXG4gICAgaW1hZ2U6IGtsYXVzZW5zY2hhZWZlcnNpbmhvL3F1YW50LXV4XG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIFFVWF9QUk9YWV9VUkw9aHR0cDovL3F1YW50LXV4LWJhY2tlbmQ6ODA4MFxuICAgICAgLSBRVVhfQVVUSD0ke1FVWF9BVVRIfVxuICAgICAgLSBRVVhfS0VZQ0xPQUtfUkVBTE09JHtRVVhfS0VZQ0xPQUtfUkVBTE19XG4gICAgICAtIFFVWF9LRVlDTE9BS19DTElFTlQ9JHtRVVhfS0VZQ0xPQUtfQ0xJRU5UfVxuICAgICAgLSBRVVhfS0VZQ0xPQUtfVVJMPSR7UVVYX0tFWUNMT0FLX1VSTH1cbiAgICAgIC0gUVVYX1dTX1VSTD0ke1FVWF9XU19VUkx9XG4gICAgbGlua3M6XG4gICAgICAtIG1vbmdvXG4gICAgICAtIHF1eC1iZVxuICAgIHBvcnRzOlxuICAgICAgLSA4MDgyXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIC0gcXV4LWJlXG5cbiAgcXV4LWJlOlxuICAgIHJlc3RhcnQ6IGFsd2F5c1xuICAgIGltYWdlOiBrbGF1c2Vuc2NoYWVmZXJzaW5oby9xdWFudC11eC1iYWNrZW5kXG4gICAgdm9sdW1lczpcbiAgICAgIC0gcXVhbnRfdXhfZGF0YTovYXBwLWRhdGFcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gUVVYX0hUVFBfSE9TVD0ke1FVWF9IVFRQX0hPU1R9XG4gICAgICAtIFFVWF9IVFRQX1BPUlQ9ODA4MFxuICAgICAgLSBRVVhfTU9OR09fREJfTkFNRT0ke1FVWF9NT05HT19EQl9OQU1FfVxuICAgICAgLSBRVVhfTU9OR09fVEFCTEVfUFJFRklYPSR7UVVYX01PTkdPX1RBQkxFX1BSRUZJWH1cbiAgICAgIC0gUVVYX01PTkdPX0NPTk5FQ1RJT05fU1RSSU5HPW1vbmdvZGI6Ly9xdWFudC11eC1tb25nbzoyNzAxN1xuICAgICAgLSBRVVhfTUFJTF9VU0VSPSR7UVVYX01BSUxfVVNFUn1cbiAgICAgIC0gUVVYX01BSUxfUEFTU1dPUkQ9JHtRVVhfTUFJTF9QQVNTV09SRH1cbiAgICAgIC0gUVVYX01BSUxfSE9TVD0ke1FVWF9NQUlMX0hPU1R9XG4gICAgICAtIFFVWF9KV1RfUEFTU1dPUkQ9JHtRVVhfSldUX1BBU1NXT1JEfVxuICAgICAgLSBRVVhfSU1BR0VfRk9MREVSX1VTRVI9L2FwcC1kYXRhL3F1eC1pbWFnZXNcbiAgICAgIC0gUVVYX0lNQUdFX0ZPTERFUl9BUFBTPS9hcHAtZGF0YS9xdXgtaW1hZ2UtYXBwc1xuICAgICAgLSBUWj0ke1RafVxuICAgICAgLSBRVVhfQVVUSF9TRVJWSUNFPSR7UVVYX0FVVEhfU0VSVklDRX1cbiAgICAgIC0gUVVYX0tFWUNMT0FLX1NFUlZFUj0ke1FVWF9LRVlDTE9BS19TRVJWRVJ9XG4gICAgICAtIFFVWF9LRVlDTE9BS19SRUFMTT0ke1FVWF9LRVlDTE9BS19SRUFMTX1cbiAgICAgIC0gUVVYX1VTRVJfQUxMT1dfU0lHTlVQPSR7UVVYX1VTRVJfQUxMT1dfU0lHTlVQfVxuICAgICAgLSBRVVhfVVNFUl9BTExPV0VEX0RPTUFJTlM9JHtRVVhfVVNFUl9BTExPV0VEX0RPTUFJTlN9XG4gICAgZGVwZW5kc19vbjpcbiAgICAgIC0gbW9uZ29cblxuICBxdXgtd3M6XG4gICAgcmVzdGFydDogYWx3YXlzXG4gICAgaW1hZ2U6IGtsYXVzZW5zY2hhZWZlcnNpbmhvL3F1YW50LXV4LXdlYnNvY2tldFxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBRVVhfU0VSVkVSPWh0dHA6Ly9xdWFudC11eC1iYWNrZW5kOjgwODAvXG4gICAgICAtIFFVWF9TRVJWRVJfUE9SVD04MDg2XG4gICAgcG9ydHM6XG4gICAgICAtIDgwODZcbiAgICBsaW5rczpcbiAgICAgIC0gcXV4LWJlXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIC0gcXV4LWJlXG5cbnZvbHVtZXM6XG4gIG1vbmdvX2RhdGE6XG4gIHF1YW50X3V4X2RhdGE6XG5cbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG53c19kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5xdXhfYXV0aCA9IFwicXV4XCJcbnF1eF9qd3RfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6NjR9XCJcbnF1eF9tb25nb19kYl9uYW1lID0gXCJxdWFudHV4XCJcbnF1eF9tb25nb190YWJsZV9wcmVmaXggPSBcInF1YW50dXhcIlxucXV4X21haWxfdXNlciA9IFwiJHtlbWFpbH1cIlxucXV4X21haWxfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcbnF1eF9tYWlsX2hvc3QgPSBcIm1haWwuZXhhbXBsZS5jb21cIlxucXV4X3RpbWV6b25lID0gXCJBbWVyaWNhL0NoaWNhZ29cIlxucXV4X2F1dGhfc2VydmljZSA9IFwicXV4XCJcbnF1eF91c2VyX2FsbG93X3NpZ251cCA9IFwidHJ1ZVwiXG5xdXhfdXNlcl9hbGxvd2VkX2RvbWFpbnMgPSBcIipcIlxucXV4X2tleWNsb2FrX3JlYWxtID0gXCJcIlxucXV4X2tleWNsb2FrX2NsaWVudCA9IFwiXCJcbnF1eF9rZXljbG9ha191cmwgPSBcIlwiXG5xdXhfa2V5Y2xvYWtfc2VydmVyID0gXCJcIlxuXG5bY29uZmlnXVxuZW52ID0gW1xuICBcIlFVWF9IVFRQX0hPU1Q9aHR0cHM6Ly8ke21haW5fZG9tYWlufVwiLFxuICBcIlFVWF9BVVRIPSR7cXV4X2F1dGh9XCIsXG4gIFwiUVVYX0pXVF9QQVNTV09SRD0ke3F1eF9qd3RfcGFzc3dvcmR9XCIsXG4gIFwiUVVYX01PTkdPX0RCX05BTUU9JHtxdXhfbW9uZ29fZGJfbmFtZX1cIixcbiAgXCJRVVhfTU9OR09fVEFCTEVfUFJFRklYPSR7cXV4X21vbmdvX3RhYmxlX3ByZWZpeH1cIixcbiAgXCJRVVhfTUFJTF9VU0VSPSR7cXV4X21haWxfdXNlcn1cIixcbiAgXCJRVVhfTUFJTF9QQVNTV09SRD0ke3F1eF9tYWlsX3Bhc3N3b3JkfVwiLFxuICBcIlFVWF9NQUlMX0hPU1Q9JHtxdXhfbWFpbF9ob3N0fVwiLFxuICBcIlRaPSR7cXV4X3RpbWV6b25lfVwiLFxuICBcIlFVWF9BVVRIX1NFUlZJQ0U9JHtxdXhfYXV0aF9zZXJ2aWNlfVwiLFxuICBcIlFVWF9LRVlDTE9BS19TRVJWRVI9JHtxdXhfa2V5Y2xvYWtfc2VydmVyfVwiLFxuICBcIlFVWF9LRVlDTE9BS19SRUFMTT0ke3F1eF9rZXljbG9ha19yZWFsbX1cIixcbiAgXCJRVVhfS0VZQ0xPQUtfQ0xJRU5UPSR7cXV4X2tleWNsb2FrX2NsaWVudH1cIixcbiAgXCJRVVhfS0VZQ0xPQUtfVVJMPSR7cXV4X2tleWNsb2FrX3VybH1cIixcbiAgXCJRVVhfVVNFUl9BTExPV19TSUdOVVA9JHtxdXhfdXNlcl9hbGxvd19zaWdudXB9XCIsXG4gIFwiUVVYX1VTRVJfQUxMT1dFRF9ET01BSU5TPSR7cXV4X3VzZXJfYWxsb3dlZF9kb21haW5zfVwiLFxuICBcIlFVWF9XU19VUkw9d3NzOi8vJHt3c19kb21haW59XCJcbl1cblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwicXV4LWZlXCJcbnBvcnQgPSA4MDgyXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcInF1eC13c1wiXG5wb3J0ID0gODA4NlxuaG9zdCA9IFwiJHt3c19kb21haW59XCJcblxuIgp9
```

## Links

`design`,`ux`,`prototyping`,`user-research`,`analytics`

---

Version:`latest`

QdrantAn open-source vector database designed for high-performance similarity search and storage of embeddings.

RabbitMQRabbitMQ is an open source multi-protocol messaging broker.

### On this page

ConfigurationBase64LinksTags