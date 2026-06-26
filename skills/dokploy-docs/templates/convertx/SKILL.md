---
title: "ConvertX | Dokploy"
source: "https://docs.dokploy.com/docs/templates/convertx"
category: dokploy-docs
created: "2026-06-25T17:21:45.077Z"
---

ConvertX | Dokploy

# ConvertX

Copy as Markdown

ConvertX is a service for converting media files, with optional user registration and file management features.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  convertx:
    image: ghcr.io/c4illin/convertx
    restart: unless-stopped
    ports:
      - 3000
    environment:
      - JWT_SECRET=${JWT_SECRET}
      - ACCOUNT_REGISTRATION=${ACCOUNT_REGISTRATION}
      - HTTP_ALLOWED=${HTTP_ALLOWED}
      - ALLOW_UNAUTHENTICATED=${ALLOW_UNAUTHENTICATED}
      - AUTO_DELETE_EVERY_N_HOURS=${AUTO_DELETE_EVERY_N_HOURS}
      - WEBROOT=${WEBROOT}
      - FFMPEG_ARGS=${FFMPEG_ARGS}
      - HIDE_HISTORY=${HIDE_HISTORY}
      - LANGUAGE=${LANGUAGE}
    volumes:
      - ../files/data:/app/data
```

```
[variables]
main_domain = "${domain}"
jwt_secret = "${jwt:32}"
account_registration = "false"
http_allowed = "true"
allow_unauthenticated = "false"
auto_delete_every_n_hours = "24"
webroot = ""
ffmpeg_args = ""
hide_history = "false"
language = "en"

[config]
[[config.domains]]
serviceName = "convertx"
port = 3000
host = "${main_domain}"

[config.env]
JWT_SECRET = "${jwt_secret}"
ACCOUNT_REGISTRATION = "${account_registration}"
HTTP_ALLOWED = "${http_allowed}"
ALLOW_UNAUTHENTICATED = "${allow_unauthenticated}"
AUTO_DELETE_EVERY_N_HOURS = "${auto_delete_every_n_hours}"
WEBROOT = "${webroot}"
FFMPEG_ARGS = "${ffmpeg_args}"
HIDE_HISTORY = "${hide_history}"
LANGUAGE = "${language}"

[[config.mounts]]
source = "../files/data"
target = "/app/data"
type = "bind"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBjb252ZXJ0eDpcbiAgICBpbWFnZTogZ2hjci5pby9jNGlsbGluL2NvbnZlcnR4XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBwb3J0czpcbiAgICAgIC0gMzAwMFxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBKV1RfU0VDUkVUPSR7SldUX1NFQ1JFVH1cbiAgICAgIC0gQUNDT1VOVF9SRUdJU1RSQVRJT049JHtBQ0NPVU5UX1JFR0lTVFJBVElPTn1cbiAgICAgIC0gSFRUUF9BTExPV0VEPSR7SFRUUF9BTExPV0VEfVxuICAgICAgLSBBTExPV19VTkFVVEhFTlRJQ0FURUQ9JHtBTExPV19VTkFVVEhFTlRJQ0FURUR9XG4gICAgICAtIEFVVE9fREVMRVRFX0VWRVJZX05fSE9VUlM9JHtBVVRPX0RFTEVURV9FVkVSWV9OX0hPVVJTfVxuICAgICAgLSBXRUJST09UPSR7V0VCUk9PVH1cbiAgICAgIC0gRkZNUEVHX0FSR1M9JHtGRk1QRUdfQVJHU31cbiAgICAgIC0gSElERV9ISVNUT1JZPSR7SElERV9ISVNUT1JZfVxuICAgICAgLSBMQU5HVUFHRT0ke0xBTkdVQUdFfVxuICAgIHZvbHVtZXM6XG4gICAgICAtIC4uL2ZpbGVzL2RhdGE6L2FwcC9kYXRhXG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuand0X3NlY3JldCA9IFwiJHtqd3Q6MzJ9XCJcbmFjY291bnRfcmVnaXN0cmF0aW9uID0gXCJmYWxzZVwiXG5odHRwX2FsbG93ZWQgPSBcInRydWVcIlxuYWxsb3dfdW5hdXRoZW50aWNhdGVkID0gXCJmYWxzZVwiXG5hdXRvX2RlbGV0ZV9ldmVyeV9uX2hvdXJzID0gXCIyNFwiXG53ZWJyb290ID0gXCJcIlxuZmZtcGVnX2FyZ3MgPSBcIlwiXG5oaWRlX2hpc3RvcnkgPSBcImZhbHNlXCJcbmxhbmd1YWdlID0gXCJlblwiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJjb252ZXJ0eFwiIFxucG9ydCA9IDMwMDBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5KV1RfU0VDUkVUID0gXCIke2p3dF9zZWNyZXR9XCJcbkFDQ09VTlRfUkVHSVNUUkFUSU9OID0gXCIke2FjY291bnRfcmVnaXN0cmF0aW9ufVwiXG5IVFRQX0FMTE9XRUQgPSBcIiR7aHR0cF9hbGxvd2VkfVwiXG5BTExPV19VTkFVVEhFTlRJQ0FURUQgPSBcIiR7YWxsb3dfdW5hdXRoZW50aWNhdGVkfVwiXG5BVVRPX0RFTEVURV9FVkVSWV9OX0hPVVJTID0gXCIke2F1dG9fZGVsZXRlX2V2ZXJ5X25faG91cnN9XCJcbldFQlJPT1QgPSBcIiR7d2Vicm9vdH1cIlxuRkZNUEVHX0FSR1MgPSBcIiR7ZmZtcGVnX2FyZ3N9XCJcbkhJREVfSElTVE9SWSA9IFwiJHtoaWRlX2hpc3Rvcnl9XCJcbkxBTkdVQUdFID0gXCIke2xhbmd1YWdlfVwiXG5cbltbY29uZmlnLm1vdW50c11dXG5zb3VyY2UgPSBcIi4uL2ZpbGVzL2RhdGFcIlxudGFyZ2V0ID0gXCIvYXBwL2RhdGFcIlxudHlwZSA9IFwiYmluZFwiIgp9
```

## Links

`media`,`converter`,`ffmpeg`

---

Version:`latest`

ConfluenceConfluence is a powerful team collaboration and knowledge-sharing tool. It allows you to create, organize, and collaborate on content in a centralized space. Designed for project management, documentation, and team communication, Confluence helps streamline workflows and enhances productivity.

ConvexConvex is an open-source reactive database designed to make life easy for web app developers.

### On this page

ConfigurationBase64LinksTags