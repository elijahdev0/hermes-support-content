---
title: "Pulse | Dokploy"
source: "https://docs.dokploy.com/docs/templates/pulse"
category: dokploy-docs
created: "2026-06-25T17:21:57.937Z"
---

Pulse | Dokploy

# Pulse

Copy as Markdown

A responsive monitoring platform for Proxmox VE, PBS, and Docker with real-time metrics across nodes and containers.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  pulse:
    image: rcourtman/pulse:5.1
    restart: always
    expose:
      - 7655
    volumes:
      - pulse_data:/data
      - /var/run/docker.sock:/var/run/docker.sock
    environment:
      - PULSE_AUTH_USER=${PULSE_AUTH_USER}
      - PULSE_AUTH_PASS=${PULSE_AUTH_PASS}
    healthcheck:
      test: ["CMD", "wget", "--no-verbose", "--tries=1", "--spider", "http://localhost:7655/api/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s

volumes:
  pulse_data:
```

```
[variables]
main_domain = "${domain}"
pulse_auth_user = "${username}"
pulse_auth_pass = "${password:32}"

[config]
env = ["PULSE_AUTH_USER=${pulse_auth_user}", "PULSE_AUTH_PASS=${pulse_auth_pass}"]
mounts = []

[[config.domains]]
serviceName = "pulse"
port = 7_655
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBwdWxzZTpcbiAgICBpbWFnZTogcmNvdXJ0bWFuL3B1bHNlOjUuMVxuICAgIHJlc3RhcnQ6IGFsd2F5c1xuICAgIGV4cG9zZTpcbiAgICAgIC0gNzY1NVxuICAgIHZvbHVtZXM6XG4gICAgICAtIHB1bHNlX2RhdGE6L2RhdGFcbiAgICAgIC0gL3Zhci9ydW4vZG9ja2VyLnNvY2s6L3Zhci9ydW4vZG9ja2VyLnNvY2tcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gUFVMU0VfQVVUSF9VU0VSPSR7UFVMU0VfQVVUSF9VU0VSfVxuICAgICAgLSBQVUxTRV9BVVRIX1BBU1M9JHtQVUxTRV9BVVRIX1BBU1N9XG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OiBbXCJDTURcIiwgXCJ3Z2V0XCIsIFwiLS1uby12ZXJib3NlXCIsIFwiLS10cmllcz0xXCIsIFwiLS1zcGlkZXJcIiwgXCJodHRwOi8vbG9jYWxob3N0Ojc2NTUvYXBpL2hlYWx0aFwiXVxuICAgICAgaW50ZXJ2YWw6IDMwc1xuICAgICAgdGltZW91dDogMTBzXG4gICAgICByZXRyaWVzOiAzXG4gICAgICBzdGFydF9wZXJpb2Q6IDQwc1xuXG52b2x1bWVzOlxuICBwdWxzZV9kYXRhOiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5wdWxzZV9hdXRoX3VzZXIgPSBcIiR7dXNlcm5hbWV9XCJcbnB1bHNlX2F1dGhfcGFzcyA9IFwiJHtwYXNzd29yZDozMn1cIlxuXG5bY29uZmlnXVxuZW52ID0gW1wiUFVMU0VfQVVUSF9VU0VSPSR7cHVsc2VfYXV0aF91c2VyfVwiLCBcIlBVTFNFX0FVVEhfUEFTUz0ke3B1bHNlX2F1dGhfcGFzc31cIl1cbm1vdW50cyA9IFtdXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcInB1bHNlXCJcbnBvcnQgPSA3XzY1NVxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIiIKfQ==
```

## Links

`monitoring`,`proxmox`,`docker`,`metrics`

---

Version:`latest`

PterodactylA free, open-source game server management panel.

PyrodactylPyrodactyl is the Pterodactyl-based game server panel that's faster, smaller, safer, and more accessible than Pelican.

### On this page

ConfigurationBase64LinksTags