---
title: "Openinary | Dokploy"
source: "https://docs.dokploy.com/docs/templates/openinary"
category: dokploy-docs
created: "2026-06-25T17:21:55.476Z"
---

Openinary | Dokploy

# Openinary

Copy as Markdown

Openinary is a self-hosted Cloudinary alternative.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  openinary:
    image: openinary/openinary:${IMAGE_TAG:-latest}
    pull_policy: always
    restart: unless-stopped
    expose:
      - 3000
    environment:
      NODE_ENV: production
      MODE: fullstack
      NEXT_PUBLIC_API_BASE_URL: ${NEXT_PUBLIC_API_BASE_URL:-/api}
      BETTER_AUTH_SECRET: ${BETTER_AUTH_SECRET}
      BETTER_AUTH_URL: ${BETTER_AUTH_URL}
      ALLOWED_ORIGIN: ${ALLOWED_ORIGIN:-http://${domain}}
      DOCKER_CONTAINER: "true"
    volumes:
      - cache-data:/app/apps/api/cache
      - public-files:/app/apps/api/public
      - db-data:/app/data
      - db-data:/app/web-standalone/data

volumes:
  cache-data:
  public-files:
  db-data:
```

```
[variables]
main_domain = "${domain}"
image_tag = "latest"
better_auth_secret = "${password:64}"
better_auth_url = "http://${main_domain}"
allowed_origin = "http://${main_domain}"
next_public_api_base_url = "/api"

[config]
[[config.domains]]
serviceName = "openinary"
port = 3000
host = "${main_domain}"

[config.env]
IMAGE_TAG = "${image_tag}"
BETTER_AUTH_SECRET = "${better_auth_secret}"
BETTER_AUTH_URL = "${better_auth_url}"
ALLOWED_ORIGIN = "${allowed_origin}"
NEXT_PUBLIC_API_BASE_URL = "${next_public_api_base_url}"

[[config.mounts]]
serviceName = "openinary"
volumeName = "cache-data"
mountPath = "/app/apps/api/cache"

[[config.mounts]]
serviceName = "openinary"
volumeName = "public-files"
mountPath = "/app/apps/api/public"

[[config.mounts]]
serviceName = "openinary"
volumeName = "db-data"
mountPath = "/app/data"

[[config.mounts]]
serviceName = "openinary"
volumeName = "db-data"
mountPath = "/app/web-standalone/data"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBvcGVuaW5hcnk6XG4gICAgaW1hZ2U6IG9wZW5pbmFyeS9vcGVuaW5hcnk6JHtJTUFHRV9UQUc6LWxhdGVzdH1cbiAgICBwdWxsX3BvbGljeTogYWx3YXlzXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBleHBvc2U6XG4gICAgICAtIDMwMDBcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIE5PREVfRU5WOiBwcm9kdWN0aW9uXG4gICAgICBNT0RFOiBmdWxsc3RhY2tcbiAgICAgIE5FWFRfUFVCTElDX0FQSV9CQVNFX1VSTDogJHtORVhUX1BVQkxJQ19BUElfQkFTRV9VUkw6LS9hcGl9XG4gICAgICBCRVRURVJfQVVUSF9TRUNSRVQ6ICR7QkVUVEVSX0FVVEhfU0VDUkVUfVxuICAgICAgQkVUVEVSX0FVVEhfVVJMOiAke0JFVFRFUl9BVVRIX1VSTH1cbiAgICAgIEFMTE9XRURfT1JJR0lOOiAke0FMTE9XRURfT1JJR0lOOi1odHRwOi8vJHtkb21haW59fVxuICAgICAgRE9DS0VSX0NPTlRBSU5FUjogXCJ0cnVlXCJcbiAgICB2b2x1bWVzOlxuICAgICAgLSBjYWNoZS1kYXRhOi9hcHAvYXBwcy9hcGkvY2FjaGVcbiAgICAgIC0gcHVibGljLWZpbGVzOi9hcHAvYXBwcy9hcGkvcHVibGljXG4gICAgICAtIGRiLWRhdGE6L2FwcC9kYXRhXG4gICAgICAtIGRiLWRhdGE6L2FwcC93ZWItc3RhbmRhbG9uZS9kYXRhXG5cbnZvbHVtZXM6XG4gIGNhY2hlLWRhdGE6XG4gIHB1YmxpYy1maWxlczpcbiAgZGItZGF0YToiLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuaW1hZ2VfdGFnID0gXCJsYXRlc3RcIlxuYmV0dGVyX2F1dGhfc2VjcmV0ID0gXCIke3Bhc3N3b3JkOjY0fVwiXG5iZXR0ZXJfYXV0aF91cmwgPSBcImh0dHA6Ly8ke21haW5fZG9tYWlufVwiXG5hbGxvd2VkX29yaWdpbiA9IFwiaHR0cDovLyR7bWFpbl9kb21haW59XCJcbm5leHRfcHVibGljX2FwaV9iYXNlX3VybCA9IFwiL2FwaVwiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJvcGVuaW5hcnlcIlxucG9ydCA9IDMwMDBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5JTUFHRV9UQUcgPSBcIiR7aW1hZ2VfdGFnfVwiXG5CRVRURVJfQVVUSF9TRUNSRVQgPSBcIiR7YmV0dGVyX2F1dGhfc2VjcmV0fVwiXG5CRVRURVJfQVVUSF9VUkwgPSBcIiR7YmV0dGVyX2F1dGhfdXJsfVwiXG5BTExPV0VEX09SSUdJTiA9IFwiJHthbGxvd2VkX29yaWdpbn1cIlxuTkVYVF9QVUJMSUNfQVBJX0JBU0VfVVJMID0gXCIke25leHRfcHVibGljX2FwaV9iYXNlX3VybH1cIlxuXG5bW2NvbmZpZy5tb3VudHNdXVxuc2VydmljZU5hbWUgPSBcIm9wZW5pbmFyeVwiXG52b2x1bWVOYW1lID0gXCJjYWNoZS1kYXRhXCJcbm1vdW50UGF0aCA9IFwiL2FwcC9hcHBzL2FwaS9jYWNoZVwiXG5cbltbY29uZmlnLm1vdW50c11dXG5zZXJ2aWNlTmFtZSA9IFwib3BlbmluYXJ5XCJcbnZvbHVtZU5hbWUgPSBcInB1YmxpYy1maWxlc1wiXG5tb3VudFBhdGggPSBcIi9hcHAvYXBwcy9hcGkvcHVibGljXCJcblxuW1tjb25maWcubW91bnRzXV1cbnNlcnZpY2VOYW1lID0gXCJvcGVuaW5hcnlcIlxudm9sdW1lTmFtZSA9IFwiZGItZGF0YVwiXG5tb3VudFBhdGggPSBcIi9hcHAvZGF0YVwiXG5cbltbY29uZmlnLm1vdW50c11dXG5zZXJ2aWNlTmFtZSA9IFwib3BlbmluYXJ5XCJcbnZvbHVtZU5hbWUgPSBcImRiLWRhdGFcIlxubW91bnRQYXRoID0gXCIvYXBwL3dlYi1zdGFuZGFsb25lL2RhdGFcIiIKfQ==
```

## Links

`media`,`images`,`videos`,`cloudinary-alternative`,`developer-tools`

---

Version:`latest`

OpenHandsOpenHands is an open-source platform for running and managing AI agents.

OpenPanelAn open-source web and product analytics platform that combines the power of Mixpanel with the ease of Plausible and one of the best Google Analytics replacements.

### On this page

ConfigurationBase64LinksTags