---
title: "Bluesky PDS | Dokploy"
source: "https://docs.dokploy.com/docs/templates/bluesky-pds"
category: dokploy-docs
created: "2026-06-25T17:21:42.676Z"
---

Bluesky PDS | Dokploy

# Bluesky PDS

Copy as Markdown

Bluesky PDS is a personal data server for Bluesky.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  pds:
    image: 'ghcr.io/bluesky-social/pds:0.4.182'
    volumes:
      - pds-data:/pds
    environment:
      - SERVICE_URL_PDS_3000
      - PDS_HOSTNAME
      - PDS_JWT_SECRET
      - PDS_ADMIN_PASSWORD
      - 'PDS_ADMIN_EMAIL=${PDS_ADMIN_EMAIL}'
      - PDS_PLC_ROTATION_KEY_K256_PRIVATE_KEY_HEX
      - 'PDS_DATA_DIRECTORY=${PDS_DATA_DIRECTORY:-/pds}'
      - 'PDS_BLOBSTORE_DISK_LOCATION=${PDS_DATA_DIRECTORY:-/pds}/blocks'
      - 'PDS_BLOB_UPLOAD_LIMIT=${PDS_BLOB_UPLOAD_LIMIT:-104857600}'
      - 'PDS_DID_PLC_URL=${PDS_DID_PLC_URL:-https://plc.directory}'
      - 'PDS_EMAIL_FROM_ADDRESS=${PDS_EMAIL_FROM_ADDRESS}'
      - 'PDS_EMAIL_SMTP_URL=${PDS_EMAIL_SMTP_URL}'
      - 'PDS_BSKY_APP_VIEW_URL=${PDS_BSKY_APP_VIEW_URL:-https://api.bsky.app}'
      - 'PDS_BSKY_APP_VIEW_DID=${PDS_BSKY_APP_VIEW_DID:-did:web:api.bsky.app}'
      - 'PDS_REPORT_SERVICE_URL=${PDS_REPORT_SERVICE_URL:-https://mod.bsky.app/xrpc/com.atproto.moderation.createReport}'
      - 'PDS_REPORT_SERVICE_DID=${PDS_REPORT_SERVICE_DID:-did:plc:ar7c4by46qjdydhdevvrndac}'
      - 'PDS_CRAWLERS=${PDS_CRAWLERS:-https://bsky.network}'
      - 'LOG_ENABLED=${LOG_ENABLED:-true}'
    command: |
      sh -c '
        set -euo pipefail
        echo "Installing required packages and pdsadmin..."
        apk add --no-cache openssl curl bash jq coreutils gnupg util-linux-misc >/dev/null
        curl -o /usr/local/bin/pdsadmin.sh https://raw.githubusercontent.com/bluesky-social/pds/main/pdsadmin.sh
        chmod 700 /usr/local/bin/pdsadmin.sh
        ln -sf /usr/local/bin/pdsadmin.sh /usr/local/bin/pdsadmin
        echo "Creating an empty pds.env file so pdsadmin works..."
        touch /pds/pds.env
        echo "Launching PDS, enjoy!..."
        exec node --enable-source-maps index.js
      '
    healthcheck:
      test:
        - CMD
        - wget
        - '--spider'
        - 'http://127.0.0.1:3000/xrpc/_health'
      interval: 5s
      timeout: 10s
      retries: 10
volumes:
  pds-data:
```

```
[variables]
main_domain = "${domain}"
admin_password = "${password:32}"
jwt_secret = "${jwt:32}"
rotation_key = "${jwt:32}"
data_directory = "/pds"
blob_upload_limit = "104857600"
log_enabled = "true"

[config]
mounts = []
env = [
    "PDS_ADMIN_PASSWORD=${admin_password}",
    "PDS_HOSTNAME=${main_domain}",
    "PDS_JWT_SECRET=${jwt_secret}",
    "PDS_PLC_ROTATION_KEY_K256_PRIVATE_KEY_HEX=${rotation_key}",
    "PDS_ADMIN_EMAIL=",
    "PDS_EMAIL_FROM_ADDRESS=",
    "PDS_EMAIL_SMTP_URL=",
    "PDS_DATA_DIRECTORY=${data_directory}",
    "PDS_BLOBSTORE_DISK_LOCATION=${data_directory}/blocks",
    "PDS_BLOB_UPLOAD_LIMIT=${blob_upload_limit}",
    "PDS_DID_PLC_URL=https://plc.directory",
    "PDS_BSKY_APP_VIEW_URL=https://api.bsky.app",
    "PDS_BSKY_APP_VIEW_DID=did:web:api.bsky.app",
    "PDS_REPORT_SERVICE_URL=https://mod.bsky.app/xrpc/com.atproto.moderation.createReport",
    "PDS_REPORT_SERVICE_DID=did:plc:ar7c4by46qjdydhdevvrndac",
    "PDS_CRAWLERS=https://bsky.network",
    "LOG_ENABLED=${log_enabled}"
]

[[config.domains]]
serviceName = "pds"
port = 3000
host = "${main_domain}"
path = "/"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBwZHM6XG4gICAgaW1hZ2U6ICdnaGNyLmlvL2JsdWVza3ktc29jaWFsL3BkczowLjQuMTgyJ1xuICAgIHZvbHVtZXM6XG4gICAgICAtIHBkcy1kYXRhOi9wZHNcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gU0VSVklDRV9VUkxfUERTXzMwMDBcbiAgICAgIC0gUERTX0hPU1ROQU1FXG4gICAgICAtIFBEU19KV1RfU0VDUkVUXG4gICAgICAtIFBEU19BRE1JTl9QQVNTV09SRFxuICAgICAgLSAnUERTX0FETUlOX0VNQUlMPSR7UERTX0FETUlOX0VNQUlMfSdcbiAgICAgIC0gUERTX1BMQ19ST1RBVElPTl9LRVlfSzI1Nl9QUklWQVRFX0tFWV9IRVhcbiAgICAgIC0gJ1BEU19EQVRBX0RJUkVDVE9SWT0ke1BEU19EQVRBX0RJUkVDVE9SWTotL3Bkc30nXG4gICAgICAtICdQRFNfQkxPQlNUT1JFX0RJU0tfTE9DQVRJT049JHtQRFNfREFUQV9ESVJFQ1RPUlk6LS9wZHN9L2Jsb2NrcydcbiAgICAgIC0gJ1BEU19CTE9CX1VQTE9BRF9MSU1JVD0ke1BEU19CTE9CX1VQTE9BRF9MSU1JVDotMTA0ODU3NjAwfSdcbiAgICAgIC0gJ1BEU19ESURfUExDX1VSTD0ke1BEU19ESURfUExDX1VSTDotaHR0cHM6Ly9wbGMuZGlyZWN0b3J5fSdcbiAgICAgIC0gJ1BEU19FTUFJTF9GUk9NX0FERFJFU1M9JHtQRFNfRU1BSUxfRlJPTV9BRERSRVNTfSdcbiAgICAgIC0gJ1BEU19FTUFJTF9TTVRQX1VSTD0ke1BEU19FTUFJTF9TTVRQX1VSTH0nXG4gICAgICAtICdQRFNfQlNLWV9BUFBfVklFV19VUkw9JHtQRFNfQlNLWV9BUFBfVklFV19VUkw6LWh0dHBzOi8vYXBpLmJza3kuYXBwfSdcbiAgICAgIC0gJ1BEU19CU0tZX0FQUF9WSUVXX0RJRD0ke1BEU19CU0tZX0FQUF9WSUVXX0RJRDotZGlkOndlYjphcGkuYnNreS5hcHB9J1xuICAgICAgLSAnUERTX1JFUE9SVF9TRVJWSUNFX1VSTD0ke1BEU19SRVBPUlRfU0VSVklDRV9VUkw6LWh0dHBzOi8vbW9kLmJza3kuYXBwL3hycGMvY29tLmF0cHJvdG8ubW9kZXJhdGlvbi5jcmVhdGVSZXBvcnR9J1xuICAgICAgLSAnUERTX1JFUE9SVF9TRVJWSUNFX0RJRD0ke1BEU19SRVBPUlRfU0VSVklDRV9ESUQ6LWRpZDpwbGM6YXI3YzRieTQ2cWpkeWRoZGV2dnJuZGFjfSdcbiAgICAgIC0gJ1BEU19DUkFXTEVSUz0ke1BEU19DUkFXTEVSUzotaHR0cHM6Ly9ic2t5Lm5ldHdvcmt9J1xuICAgICAgLSAnTE9HX0VOQUJMRUQ9JHtMT0dfRU5BQkxFRDotdHJ1ZX0nXG4gICAgY29tbWFuZDogfFxuICAgICAgc2ggLWMgJ1xuICAgICAgICBzZXQgLWV1byBwaXBlZmFpbFxuICAgICAgICBlY2hvIFwiSW5zdGFsbGluZyByZXF1aXJlZCBwYWNrYWdlcyBhbmQgcGRzYWRtaW4uLi5cIlxuICAgICAgICBhcGsgYWRkIC0tbm8tY2FjaGUgb3BlbnNzbCBjdXJsIGJhc2gganEgY29yZXV0aWxzIGdudXBnIHV0aWwtbGludXgtbWlzYyA+L2Rldi9udWxsXG4gICAgICAgIGN1cmwgLW8gL3Vzci9sb2NhbC9iaW4vcGRzYWRtaW4uc2ggaHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL2JsdWVza3ktc29jaWFsL3Bkcy9tYWluL3Bkc2FkbWluLnNoXG4gICAgICAgIGNobW9kIDcwMCAvdXNyL2xvY2FsL2Jpbi9wZHNhZG1pbi5zaFxuICAgICAgICBsbiAtc2YgL3Vzci9sb2NhbC9iaW4vcGRzYWRtaW4uc2ggL3Vzci9sb2NhbC9iaW4vcGRzYWRtaW5cbiAgICAgICAgZWNobyBcIkNyZWF0aW5nIGFuIGVtcHR5IHBkcy5lbnYgZmlsZSBzbyBwZHNhZG1pbiB3b3Jrcy4uLlwiXG4gICAgICAgIHRvdWNoIC9wZHMvcGRzLmVudlxuICAgICAgICBlY2hvIFwiTGF1bmNoaW5nIFBEUywgZW5qb3khLi4uXCJcbiAgICAgICAgZXhlYyBub2RlIC0tZW5hYmxlLXNvdXJjZS1tYXBzIGluZGV4LmpzXG4gICAgICAnXG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OlxuICAgICAgICAtIENNRFxuICAgICAgICAtIHdnZXRcbiAgICAgICAgLSAnLS1zcGlkZXInXG4gICAgICAgIC0gJ2h0dHA6Ly8xMjcuMC4wLjE6MzAwMC94cnBjL19oZWFsdGgnXG4gICAgICBpbnRlcnZhbDogNXNcbiAgICAgIHRpbWVvdXQ6IDEwc1xuICAgICAgcmV0cmllczogMTBcbnZvbHVtZXM6IFxuICBwZHMtZGF0YToiLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuYWRtaW5fcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcbmp3dF9zZWNyZXQgPSBcIiR7and0OjMyfVwiXG5yb3RhdGlvbl9rZXkgPSBcIiR7and0OjMyfVwiXG5kYXRhX2RpcmVjdG9yeSA9IFwiL3Bkc1wiXG5ibG9iX3VwbG9hZF9saW1pdCA9IFwiMTA0ODU3NjAwXCJcbmxvZ19lbmFibGVkID0gXCJ0cnVlXCJcblxuW2NvbmZpZ11cbm1vdW50cyA9IFtdXG5lbnYgPSBbXG4gICAgXCJQRFNfQURNSU5fUEFTU1dPUkQ9JHthZG1pbl9wYXNzd29yZH1cIixcbiAgICBcIlBEU19IT1NUTkFNRT0ke21haW5fZG9tYWlufVwiLFxuICAgIFwiUERTX0pXVF9TRUNSRVQ9JHtqd3Rfc2VjcmV0fVwiLFxuICAgIFwiUERTX1BMQ19ST1RBVElPTl9LRVlfSzI1Nl9QUklWQVRFX0tFWV9IRVg9JHtyb3RhdGlvbl9rZXl9XCIsXG4gICAgXCJQRFNfQURNSU5fRU1BSUw9XCIsXG4gICAgXCJQRFNfRU1BSUxfRlJPTV9BRERSRVNTPVwiLFxuICAgIFwiUERTX0VNQUlMX1NNVFBfVVJMPVwiLFxuICAgIFwiUERTX0RBVEFfRElSRUNUT1JZPSR7ZGF0YV9kaXJlY3Rvcnl9XCIsXG4gICAgXCJQRFNfQkxPQlNUT1JFX0RJU0tfTE9DQVRJT049JHtkYXRhX2RpcmVjdG9yeX0vYmxvY2tzXCIsXG4gICAgXCJQRFNfQkxPQl9VUExPQURfTElNSVQ9JHtibG9iX3VwbG9hZF9saW1pdH1cIixcbiAgICBcIlBEU19ESURfUExDX1VSTD1odHRwczovL3BsYy5kaXJlY3RvcnlcIixcbiAgICBcIlBEU19CU0tZX0FQUF9WSUVXX1VSTD1odHRwczovL2FwaS5ic2t5LmFwcFwiLFxuICAgIFwiUERTX0JTS1lfQVBQX1ZJRVdfRElEPWRpZDp3ZWI6YXBpLmJza3kuYXBwXCIsXG4gICAgXCJQRFNfUkVQT1JUX1NFUlZJQ0VfVVJMPWh0dHBzOi8vbW9kLmJza3kuYXBwL3hycGMvY29tLmF0cHJvdG8ubW9kZXJhdGlvbi5jcmVhdGVSZXBvcnRcIixcbiAgICBcIlBEU19SRVBPUlRfU0VSVklDRV9ESUQ9ZGlkOnBsYzphcjdjNGJ5NDZxamR5ZGhkZXZ2cm5kYWNcIixcbiAgICBcIlBEU19DUkFXTEVSUz1odHRwczovL2Jza3kubmV0d29ya1wiLFxuICAgIFwiTE9HX0VOQUJMRUQ9JHtsb2dfZW5hYmxlZH1cIlxuXVxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJwZHNcIlxucG9ydCA9IDMwMDBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcbnBhdGggPSBcIi9cIiIKfQ==
```

## Links

`bluesky`,`pds`,`data`,`server`

---

Version:`0.4.182`

BlinkoBlinko is a modern web application for managing and organizing your digital content and workflows.

bolt.diyPrompt, run, edit, and deploy full-stack web applications using any LLM you want!

### On this page

ConfigurationBase64LinksTags