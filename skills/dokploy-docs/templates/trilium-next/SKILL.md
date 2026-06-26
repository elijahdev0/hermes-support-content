---
title: "TriliumNext | Dokploy"
source: "https://docs.dokploy.com/docs/templates/trilium-next"
category: dokploy-docs
created: "2026-06-25T17:22:00.275Z"
---

TriliumNext | Dokploy

# TriliumNext

Copy as Markdown

Is a free and open-source, cross-platform hierarchical note taking application with focus on building large personal knowledge bases.

## Configuration

docker-compose.ymltemplate.toml

```
# Running `docker-compose up` will create/use the "trilium-data" directory in the user home
services:
  trilium_next:
    # Optionally, replace `latest` with a version tag like `v0.110.3`
    # Using `latest` may cause unintended updates to the container
    image: triliumnext/trilium:v0.101.3
    # Restart the container unless it was stopped by the user
    restart: unless-stopped
    environment:
      - TRILIUM_DATA_DIR=/home/node/trilium-data
    ports:
      # By default, Trilium will be available at http://localhost:8080
      # It will also be accessible at http://<host-ip>:8080
      # You might want to limit this with something like Docker Networks, reverse proxies, or firewall rules,
      # however be aware that using UFW is known to not work with default Docker installations, see:
      # https://docs.docker.com/engine/network/packet-filtering-firewalls/#docker-and-ufw
      - "8080"
    volumes:
      # Unless TRILIUM_DATA_DIR is set, the data will be stored in the "trilium-data" directory in the home directory.
      # This can also be changed with by replacing the line below with `- /path/of/your/choice:/home/node/trilium-data
      - ${TRILIUM_DATA_DIR:-~/trilium-data}:/home/node/trilium-data
      - /etc/timezone:/etc/timezone:ro
      - /etc/localtime:/etc/localtime:ro
```

```
[variables]
main_domain = "${domain}"

[config]
env = [
"TRILIUM_DATA_DIR=/root"
]
mount = []

[[config.domains]]
serviceName = "trilium_next"
port = 8080
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogIiMgUnVubmluZyBgZG9ja2VyLWNvbXBvc2UgdXBgIHdpbGwgY3JlYXRlL3VzZSB0aGUgXCJ0cmlsaXVtLWRhdGFcIiBkaXJlY3RvcnkgaW4gdGhlIHVzZXIgaG9tZVxuc2VydmljZXM6XG4gIHRyaWxpdW1fbmV4dDpcbiAgICAjIE9wdGlvbmFsbHksIHJlcGxhY2UgYGxhdGVzdGAgd2l0aCBhIHZlcnNpb24gdGFnIGxpa2UgYHYwLjExMC4zYFxuICAgICMgVXNpbmcgYGxhdGVzdGAgbWF5IGNhdXNlIHVuaW50ZW5kZWQgdXBkYXRlcyB0byB0aGUgY29udGFpbmVyXG4gICAgaW1hZ2U6IHRyaWxpdW1uZXh0L3RyaWxpdW06djAuMTAxLjNcbiAgICAjIFJlc3RhcnQgdGhlIGNvbnRhaW5lciB1bmxlc3MgaXQgd2FzIHN0b3BwZWQgYnkgdGhlIHVzZXJcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBUUklMSVVNX0RBVEFfRElSPS9ob21lL25vZGUvdHJpbGl1bS1kYXRhXG4gICAgcG9ydHM6XG4gICAgICAjIEJ5IGRlZmF1bHQsIFRyaWxpdW0gd2lsbCBiZSBhdmFpbGFibGUgYXQgaHR0cDovL2xvY2FsaG9zdDo4MDgwXG4gICAgICAjIEl0IHdpbGwgYWxzbyBiZSBhY2Nlc3NpYmxlIGF0IGh0dHA6Ly88aG9zdC1pcD46ODA4MFxuICAgICAgIyBZb3UgbWlnaHQgd2FudCB0byBsaW1pdCB0aGlzIHdpdGggc29tZXRoaW5nIGxpa2UgRG9ja2VyIE5ldHdvcmtzLCByZXZlcnNlIHByb3hpZXMsIG9yIGZpcmV3YWxsIHJ1bGVzLFxuICAgICAgIyBob3dldmVyIGJlIGF3YXJlIHRoYXQgdXNpbmcgVUZXIGlzIGtub3duIHRvIG5vdCB3b3JrIHdpdGggZGVmYXVsdCBEb2NrZXIgaW5zdGFsbGF0aW9ucywgc2VlOlxuICAgICAgIyBodHRwczovL2RvY3MuZG9ja2VyLmNvbS9lbmdpbmUvbmV0d29yay9wYWNrZXQtZmlsdGVyaW5nLWZpcmV3YWxscy8jZG9ja2VyLWFuZC11ZndcbiAgICAgIC0gXCI4MDgwXCJcbiAgICB2b2x1bWVzOlxuICAgICAgIyBVbmxlc3MgVFJJTElVTV9EQVRBX0RJUiBpcyBzZXQsIHRoZSBkYXRhIHdpbGwgYmUgc3RvcmVkIGluIHRoZSBcInRyaWxpdW0tZGF0YVwiIGRpcmVjdG9yeSBpbiB0aGUgaG9tZSBkaXJlY3RvcnkuXG4gICAgICAjIFRoaXMgY2FuIGFsc28gYmUgY2hhbmdlZCB3aXRoIGJ5IHJlcGxhY2luZyB0aGUgbGluZSBiZWxvdyB3aXRoIGAtIC9wYXRoL29mL3lvdXIvY2hvaWNlOi9ob21lL25vZGUvdHJpbGl1bS1kYXRhXG4gICAgICAtICR7VFJJTElVTV9EQVRBX0RJUjotfi90cmlsaXVtLWRhdGF9Oi9ob21lL25vZGUvdHJpbGl1bS1kYXRhXG4gICAgICAtIC9ldGMvdGltZXpvbmU6L2V0Yy90aW1lem9uZTpyb1xuICAgICAgLSAvZXRjL2xvY2FsdGltZTovZXRjL2xvY2FsdGltZTpyb1xuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcblxuW2NvbmZpZ11cbmVudiA9IFtcblwiVFJJTElVTV9EQVRBX0RJUj0vcm9vdFwiXG5dXG5tb3VudCA9IFtdXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcInRyaWxpdW1fbmV4dFwiXG5wb3J0ID0gODA4MFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuIgp9
```

## Links

`self-hosted`,`productivity`,`personal-use`

---

Version:`latest`

TriliumTrilium Notes is a hierarchical note taking application with focus on building large personal knowledge bases.

TRMNL BYOS LaravelTRMNL BYOS Laravel is a self-hosted application to manage TRMNL e-ink devices.

### On this page

ConfigurationBase64LinksTags