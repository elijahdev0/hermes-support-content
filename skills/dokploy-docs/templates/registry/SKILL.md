---
title: "Docker Registry | Dokploy"
source: "https://docs.dokploy.com/docs/templates/registry"
category: dokploy-docs
created: "2026-06-25T17:21:57.938Z"
---

Docker Registry | Dokploy

# Docker Registry

Copy as Markdown

Distribution implementation for storing and distributing of Docker container images and artifacts.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  registry:
    restart: always
    image: registry:2
    ports:
      - 5000
    volumes:
      - ../files/auth/registry.password:/auth/registry.password
      - registry-data:/var/lib/registry
    environment:
      REGISTRY_STORAGE_DELETE_ENABLED: true
      REGISTRY_HEALTH_STORAGEDRIVER_ENABLED: false
      REGISTRY_HTTP_SECRET: ${REGISTRY_HTTP_SECRET}
      REGISTRY_AUTH: htpasswd
      REGISTRY_AUTH_HTPASSWD_REALM: Registry Realm
      REGISTRY_AUTH_HTPASSWD_PATH: /auth/registry.password

volumes:
  registry-data:
```

```
[variables]
main_domain = "${domain}"
registry_http_secret = "${password:30}"

[[config.domains]]
serviceName = "registry"
port = 5_000
host = "${main_domain}"

[config.env]
REGISTRY_HTTP_SECRET = "${registry_http_secret}"

[[config.mounts]]
filePath = "/auth/registry.password"
content = """
# from: docker run --rm --entrypoint htpasswd httpd:2 -Bbn docker password
docker:$2y$10$qWZoWev/u5PV7WneFoRAMuoGpRcAQOgUuIIdLnU7pJXogrBSY23/2
"""
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICByZWdpc3RyeTpcbiAgICByZXN0YXJ0OiBhbHdheXNcbiAgICBpbWFnZTogcmVnaXN0cnk6MlxuICAgIHBvcnRzOlxuICAgICAgLSA1MDAwXG4gICAgdm9sdW1lczpcbiAgICAgIC0gLi4vZmlsZXMvYXV0aC9yZWdpc3RyeS5wYXNzd29yZDovYXV0aC9yZWdpc3RyeS5wYXNzd29yZFxuICAgICAgLSByZWdpc3RyeS1kYXRhOi92YXIvbGliL3JlZ2lzdHJ5XG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBSRUdJU1RSWV9TVE9SQUdFX0RFTEVURV9FTkFCTEVEOiB0cnVlXG4gICAgICBSRUdJU1RSWV9IRUFMVEhfU1RPUkFHRURSSVZFUl9FTkFCTEVEOiBmYWxzZVxuICAgICAgUkVHSVNUUllfSFRUUF9TRUNSRVQ6ICR7UkVHSVNUUllfSFRUUF9TRUNSRVR9XG4gICAgICBSRUdJU1RSWV9BVVRIOiBodHBhc3N3ZFxuICAgICAgUkVHSVNUUllfQVVUSF9IVFBBU1NXRF9SRUFMTTogUmVnaXN0cnkgUmVhbG1cbiAgICAgIFJFR0lTVFJZX0FVVEhfSFRQQVNTV0RfUEFUSDogL2F1dGgvcmVnaXN0cnkucGFzc3dvcmRcblxudm9sdW1lczpcbiAgcmVnaXN0cnktZGF0YToiLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxucmVnaXN0cnlfaHR0cF9zZWNyZXQgPSBcIiR7cGFzc3dvcmQ6MzB9XCJcblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwicmVnaXN0cnlcIlxucG9ydCA9IDVfMDAwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuUkVHSVNUUllfSFRUUF9TRUNSRVQgPSBcIiR7cmVnaXN0cnlfaHR0cF9zZWNyZXR9XCJcblxuW1tjb25maWcubW91bnRzXV1cbmZpbGVQYXRoID0gXCIvYXV0aC9yZWdpc3RyeS5wYXNzd29yZFwiXG5jb250ZW50ID0gXCJcIlwiXG4jIGZyb206IGRvY2tlciBydW4gLS1ybSAtLWVudHJ5cG9pbnQgaHRwYXNzd2QgaHR0cGQ6MiAtQmJuIGRvY2tlciBwYXNzd29yZFxuZG9ja2VyOiQyeSQxMCRxV1pvV2V2L3U1UFY3V25lRm9SQU11b0dwUmNBUU9nVXVJSWRMblU3cEpYb2dyQlNZMjMvMiBcblwiXCJcIlxuIgp9
```

## Links

`registry`,`docker`,`self-hosted`

---

Version:`2`

Reactive ResumeA free and open-source resume builder that simplifies the process of creating, updating, and sharing your resume.

RocketchatRocket.Chat is a free and open-source web chat platform that allows you to build and manage your own chat applications.

### On this page

ConfigurationBase64LinksTags