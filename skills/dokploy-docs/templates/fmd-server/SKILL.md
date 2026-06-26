---
title: "FMD Server | Dokploy"
source: "https://docs.dokploy.com/docs/templates/fmd-server"
category: dokploy-docs
created: "2026-06-25T17:21:48.520Z"
---

FMD Server | Dokploy

# FMD Server

Copy as Markdown

A server to communicate with the FMD Android app, to locate and control your devices.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  fmd-server:
    image: registry.gitlab.com/fmd-foss/fmd-server:v0.11.0
    ports:
     - 8080
    environment:
      # View all configurations at:
      #     - https://gitlab.com/fmd-foss/fmd-server/-/blob/master/config.example.yml
      #
      # Config fields can be converted to environment variables as per the documentation
      #     - https://gitlab.com/fmd-foss/fmd-server#via-environment-variables
      # e.g. RegistrationToken -> FMD_REGISTRATIONTOKEN
      #
      - FMD_REGISTRATIONTOKEN=${FMD_REGISTRATIONTOKEN}
      - FMD_USERIDLENGTH=${FMD_USERIDLENGTH}
      - FMD_MAXSAVEDLOC=${FMD_MAXSAVEDLOC}
      - FMD_MAXSAVEDPIC=${FMD_MAXSAVEDPIC}
    volumes:
      - fmd-server-data:/var/lib/fmd-server/db/
    restart: unless-stopped
    healthcheck:
      test: ["CMD-SHELL", "timeout 10s bash -c ':> /dev/tcp/127.0.0.1/8080'"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 5s
      start_interval: 3s

volumes:
  fmd-server-data:
```

```
[variables]
main_domain = "${domain}"
registration_token = "${password:32}"

[[config.domains]]
serviceName = "fmd-server"
port = 8080
host = "${main_domain}"

[config.env]
FMD_REGISTRATIONTOKEN = "${registration_token}"
FMD_USERIDLENGTH=5
FMD_MAXSAVEDLOC=1000
FMD_MAXSAVEDPIC=10
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBmbWQtc2VydmVyOlxuICAgIGltYWdlOiByZWdpc3RyeS5naXRsYWIuY29tL2ZtZC1mb3NzL2ZtZC1zZXJ2ZXI6djAuMTEuMFxuICAgIHBvcnRzOlxuICAgICAtIDgwODBcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgICMgVmlldyBhbGwgY29uZmlndXJhdGlvbnMgYXQ6XG4gICAgICAjICAgICAtIGh0dHBzOi8vZ2l0bGFiLmNvbS9mbWQtZm9zcy9mbWQtc2VydmVyLy0vYmxvYi9tYXN0ZXIvY29uZmlnLmV4YW1wbGUueW1sXG4gICAgICAjXG4gICAgICAjIENvbmZpZyBmaWVsZHMgY2FuIGJlIGNvbnZlcnRlZCB0byBlbnZpcm9ubWVudCB2YXJpYWJsZXMgYXMgcGVyIHRoZSBkb2N1bWVudGF0aW9uXG4gICAgICAjICAgICAtIGh0dHBzOi8vZ2l0bGFiLmNvbS9mbWQtZm9zcy9mbWQtc2VydmVyI3ZpYS1lbnZpcm9ubWVudC12YXJpYWJsZXNcbiAgICAgICMgZS5nLiBSZWdpc3RyYXRpb25Ub2tlbiAtPiBGTURfUkVHSVNUUkFUSU9OVE9LRU5cbiAgICAgICNcbiAgICAgIC0gRk1EX1JFR0lTVFJBVElPTlRPS0VOPSR7Rk1EX1JFR0lTVFJBVElPTlRPS0VOfVxuICAgICAgLSBGTURfVVNFUklETEVOR1RIPSR7Rk1EX1VTRVJJRExFTkdUSH1cbiAgICAgIC0gRk1EX01BWFNBVkVETE9DPSR7Rk1EX01BWFNBVkVETE9DfVxuICAgICAgLSBGTURfTUFYU0FWRURQSUM9JHtGTURfTUFYU0FWRURQSUN9XG4gICAgdm9sdW1lczpcbiAgICAgIC0gZm1kLXNlcnZlci1kYXRhOi92YXIvbGliL2ZtZC1zZXJ2ZXIvZGIvXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6IFtcIkNNRC1TSEVMTFwiLCBcInRpbWVvdXQgMTBzIGJhc2ggLWMgJzo+IC9kZXYvdGNwLzEyNy4wLjAuMS84MDgwJ1wiXVxuICAgICAgaW50ZXJ2YWw6IDMwc1xuICAgICAgdGltZW91dDogMTBzXG4gICAgICByZXRyaWVzOiAzXG4gICAgICBzdGFydF9wZXJpb2Q6IDVzXG4gICAgICBzdGFydF9pbnRlcnZhbDogM3Ncblxudm9sdW1lczpcbiAgZm1kLXNlcnZlci1kYXRhOlxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbnJlZ2lzdHJhdGlvbl90b2tlbiA9IFwiJHtwYXNzd29yZDozMn1cIlxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJmbWQtc2VydmVyXCJcbnBvcnQgPSA4MDgwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuRk1EX1JFR0lTVFJBVElPTlRPS0VOID0gXCIke3JlZ2lzdHJhdGlvbl90b2tlbn1cIlxuRk1EX1VTRVJJRExFTkdUSD01XG5GTURfTUFYU0FWRURMT0M9MTAwMFxuRk1EX01BWFNBVkVEUElDPTEwXG4iCn0=
```

## Links

`phone`,`security`,`gps`,`location`

---

Version:`0.11.0`

FlowiseFlowise is an open-source UI visual tool to build and run LLM-powered applications.

FocalboardOpen source project management for technical teams

### On this page

ConfigurationBase64LinksTags