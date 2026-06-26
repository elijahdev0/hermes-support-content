---
title: "Shlink | Dokploy"
source: "https://docs.dokploy.com/docs/templates/shlink"
category: dokploy-docs
created: "2026-06-25T17:21:59.113Z"
---

Shlink | Dokploy

# Shlink

Copy as Markdown

URL shortener that can be used to serve shortened URLs under your own domain.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  shlink:
    image: shlinkio/shlink:stable
    environment:
      - INITIAL_API_KEY=${INITIAL_API_KEY}
      - DEFAULT_DOMAIN=${DEFAULT_DOMAIN}
      # Note: you should also update SHLINK_SERVER_URL in the shlink-web service.
      - IS_HTTPS_ENABLED=false
    volumes:
      - shlink-data:/etc/shlink/data
    healthcheck:
      test: ["CMD", "curl", "-f", "http://127.0.0.1:8080/rest/v3/health"]
      interval: 30s
      timeout: 10s
      retries: 3
  shlink-web:
    image: shlinkio/shlink-web-client
    environment:
      - SHLINK_SERVER_API_KEY=${INITIAL_API_KEY}
      # Note: if you've set IS_HTTPS_ENABLED=true, change http to https.
      - SHLINK_SERVER_URL=http://${DEFAULT_DOMAIN}
    healthcheck:
      test: ["CMD", "curl", "-f", "http://127.0.0.1:8080"]
      interval: 30s
      timeout: 10s
      retries: 3

volumes:
  shlink-data:
```

```
[variables]
main_domain = "${domain}"
initial_api_key = "${password:30}"

[config]
mounts = []

[[config.domains]]
serviceName = "shlink-web"
port = 8_080
host = "web-${main_domain}"

[[config.domains]]
serviceName = "shlink"
port = 8_080
host = "${main_domain}"

[config.env]
INITIAL_API_KEY = "${initial_api_key}"
DEFAULT_DOMAIN = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBzaGxpbms6XG4gICAgaW1hZ2U6IHNobGlua2lvL3NobGluazpzdGFibGVcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gSU5JVElBTF9BUElfS0VZPSR7SU5JVElBTF9BUElfS0VZfVxuICAgICAgLSBERUZBVUxUX0RPTUFJTj0ke0RFRkFVTFRfRE9NQUlOfVxuICAgICAgIyBOb3RlOiB5b3Ugc2hvdWxkIGFsc28gdXBkYXRlIFNITElOS19TRVJWRVJfVVJMIGluIHRoZSBzaGxpbmstd2ViIHNlcnZpY2UuXG4gICAgICAtIElTX0hUVFBTX0VOQUJMRUQ9ZmFsc2VcbiAgICB2b2x1bWVzOlxuICAgICAgLSBzaGxpbmstZGF0YTovZXRjL3NobGluay9kYXRhXG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OiBbXCJDTURcIiwgXCJjdXJsXCIsIFwiLWZcIiwgXCJodHRwOi8vMTI3LjAuMC4xOjgwODAvcmVzdC92My9oZWFsdGhcIl1cbiAgICAgIGludGVydmFsOiAzMHNcbiAgICAgIHRpbWVvdXQ6IDEwc1xuICAgICAgcmV0cmllczogM1xuICBzaGxpbmstd2ViOlxuICAgIGltYWdlOiBzaGxpbmtpby9zaGxpbmstd2ViLWNsaWVudFxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBTSExJTktfU0VSVkVSX0FQSV9LRVk9JHtJTklUSUFMX0FQSV9LRVl9XG4gICAgICAjIE5vdGU6IGlmIHlvdSd2ZSBzZXQgSVNfSFRUUFNfRU5BQkxFRD10cnVlLCBjaGFuZ2UgaHR0cCB0byBodHRwcy5cbiAgICAgIC0gU0hMSU5LX1NFUlZFUl9VUkw9aHR0cDovLyR7REVGQVVMVF9ET01BSU59XG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OiBbXCJDTURcIiwgXCJjdXJsXCIsIFwiLWZcIiwgXCJodHRwOi8vMTI3LjAuMC4xOjgwODBcIl1cbiAgICAgIGludGVydmFsOiAzMHNcbiAgICAgIHRpbWVvdXQ6IDEwc1xuICAgICAgcmV0cmllczogM1xuXG52b2x1bWVzOlxuICBzaGxpbmstZGF0YTpcbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5pbml0aWFsX2FwaV9rZXkgPSBcIiR7cGFzc3dvcmQ6MzB9XCJcblxuW2NvbmZpZ11cbm1vdW50cyA9IFtdXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcInNobGluay13ZWJcIlxucG9ydCA9IDhfMDgwXG5ob3N0ID0gXCJ3ZWItJHttYWluX2RvbWFpbn1cIlxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJzaGxpbmtcIlxucG9ydCA9IDhfMDgwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuSU5JVElBTF9BUElfS0VZID0gXCIke2luaXRpYWxfYXBpX2tleX1cIlxuREVGQVVMVF9ET01BSU4gPSBcIiR7bWFpbl9kb21haW59XCJcbiIKfQ==
```

## Links

`sharing`,`shortener`,`url`

---

Version:`stable`

SeaweedFSSeaweedFS is a fast distributed storage system for blobs, objects, and files. Features S3-compatible API, POSIX FUSE mount, and WebDAV support.

SigNozSigNoz is an open-source Datadog or New Relic alternative. Get APM, logs,traces, metrics, exceptions, & alerts in a single tool.

### On this page

ConfigurationBase64LinksTags