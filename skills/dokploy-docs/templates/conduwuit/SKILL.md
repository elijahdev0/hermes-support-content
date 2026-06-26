---
title: "Conduwuit | Dokploy"
source: "https://docs.dokploy.com/docs/templates/conduwuit"
category: dokploy-docs
created: "2026-06-25T17:21:45.077Z"
---

Conduwuit | Dokploy

# Conduwuit

Copy as Markdown

Well-maintained, featureful Matrix chat homeserver (fork of Conduit)

## Configuration

docker-compose.ymltemplate.toml

```
# conduwuit
# https://conduwuit.puppyirl.gay/deploying/docker-compose.yml

services:
  homeserver:
    image: girlbossceo/conduwuit:latest
    restart: unless-stopped
    ports:
      - 8448:6167
    volumes:
      - db:/var/lib/conduwuit
      #- ./conduwuit.toml:/etc/conduwuit.toml
    environment:
      # Edit this in your Dokploy Environment
      CONDUWUIT_SERVER_NAME: ${CONDUWUIT_SERVER_NAME}

      CONDUWUIT_DATABASE_PATH: /var/lib/conduwuit
      CONDUWUIT_PORT: 6167
      CONDUWUIT_MAX_REQUEST_SIZE: 20000000 # in bytes, ~20 MB

      CONDUWUIT_ALLOW_REGISTRATION: 'true'
      CONDUWUIT_REGISTRATION_TOKEN: ${CONDUWUIT_REGISTRATION_TOKEN}

      CONDUWUIT_ALLOW_FEDERATION: 'true'
      CONDUWUIT_ALLOW_CHECK_FOR_UPDATES: 'true'
      CONDUWUIT_TRUSTED_SERVERS: '["matrix.org"]'
      #CONDUWUIT_LOG: warn,state_res=warn
      CONDUWUIT_ADDRESS: 0.0.0.0

      # Uncomment if you mapped config toml in volumes
      #CONDUWUIT_CONFIG: '/etc/conduwuit.toml'

  ### Uncomment if you want to use your own Element-Web App.
  ### Note: You need to provide a config.json for Element and you also need a second
  ###     Domain or Subdomain for the communication between Element and conduwuit
  ### Config-Docs: https://github.com/vector-im/element-web/blob/develop/docs/config.md
  # element-web:
  #   image: vectorim/element-web:latest
  #   restart: unless-stopped
  #   ports:
  #     - 8009:80
  #   volumes:
  #     - ./element_config.json:/app/config.json
  #   depends_on:
  #     - homeserver

volumes:
  db:
```

```
[variables]
main_domain = "${domain}"
registration_token = "${password:20}"

[config]
env = [
  "CONDUWUIT_SERVER_NAME=${main_domain}",
  "CONDUWUIT_REGISTRATION_TOKEN=${registration_token}",
]
mounts = []

[[config.domains]]
serviceName = "homeserver"
port = 6_167
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogIiMgY29uZHV3dWl0XG4jIGh0dHBzOi8vY29uZHV3dWl0LnB1cHB5aXJsLmdheS9kZXBsb3lpbmcvZG9ja2VyLWNvbXBvc2UueW1sXG5cbnNlcnZpY2VzOlxuICBob21lc2VydmVyOlxuICAgIGltYWdlOiBnaXJsYm9zc2Nlby9jb25kdXd1aXQ6bGF0ZXN0XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBwb3J0czpcbiAgICAgIC0gODQ0ODo2MTY3XG4gICAgdm9sdW1lczpcbiAgICAgIC0gZGI6L3Zhci9saWIvY29uZHV3dWl0XG4gICAgICAjLSAuL2NvbmR1d3VpdC50b21sOi9ldGMvY29uZHV3dWl0LnRvbWxcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgICMgRWRpdCB0aGlzIGluIHlvdXIgRG9rcGxveSBFbnZpcm9ubWVudFxuICAgICAgQ09ORFVXVUlUX1NFUlZFUl9OQU1FOiAke0NPTkRVV1VJVF9TRVJWRVJfTkFNRX1cblxuICAgICAgQ09ORFVXVUlUX0RBVEFCQVNFX1BBVEg6IC92YXIvbGliL2NvbmR1d3VpdFxuICAgICAgQ09ORFVXVUlUX1BPUlQ6IDYxNjdcbiAgICAgIENPTkRVV1VJVF9NQVhfUkVRVUVTVF9TSVpFOiAyMDAwMDAwMCAjIGluIGJ5dGVzLCB+MjAgTUJcblxuICAgICAgQ09ORFVXVUlUX0FMTE9XX1JFR0lTVFJBVElPTjogJ3RydWUnXG4gICAgICBDT05EVVdVSVRfUkVHSVNUUkFUSU9OX1RPS0VOOiAke0NPTkRVV1VJVF9SRUdJU1RSQVRJT05fVE9LRU59XG5cbiAgICAgIENPTkRVV1VJVF9BTExPV19GRURFUkFUSU9OOiAndHJ1ZSdcbiAgICAgIENPTkRVV1VJVF9BTExPV19DSEVDS19GT1JfVVBEQVRFUzogJ3RydWUnXG4gICAgICBDT05EVVdVSVRfVFJVU1RFRF9TRVJWRVJTOiAnW1wibWF0cml4Lm9yZ1wiXSdcbiAgICAgICNDT05EVVdVSVRfTE9HOiB3YXJuLHN0YXRlX3Jlcz13YXJuXG4gICAgICBDT05EVVdVSVRfQUREUkVTUzogMC4wLjAuMFxuXG4gICAgICAjIFVuY29tbWVudCBpZiB5b3UgbWFwcGVkIGNvbmZpZyB0b21sIGluIHZvbHVtZXNcbiAgICAgICNDT05EVVdVSVRfQ09ORklHOiAnL2V0Yy9jb25kdXd1aXQudG9tbCdcblxuICAjIyMgVW5jb21tZW50IGlmIHlvdSB3YW50IHRvIHVzZSB5b3VyIG93biBFbGVtZW50LVdlYiBBcHAuXG4gICMjIyBOb3RlOiBZb3UgbmVlZCB0byBwcm92aWRlIGEgY29uZmlnLmpzb24gZm9yIEVsZW1lbnQgYW5kIHlvdSBhbHNvIG5lZWQgYSBzZWNvbmRcbiAgIyMjICAgICBEb21haW4gb3IgU3ViZG9tYWluIGZvciB0aGUgY29tbXVuaWNhdGlvbiBiZXR3ZWVuIEVsZW1lbnQgYW5kIGNvbmR1d3VpdFxuICAjIyMgQ29uZmlnLURvY3M6IGh0dHBzOi8vZ2l0aHViLmNvbS92ZWN0b3ItaW0vZWxlbWVudC13ZWIvYmxvYi9kZXZlbG9wL2RvY3MvY29uZmlnLm1kXG4gICMgZWxlbWVudC13ZWI6XG4gICMgICBpbWFnZTogdmVjdG9yaW0vZWxlbWVudC13ZWI6bGF0ZXN0XG4gICMgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAjICAgcG9ydHM6XG4gICMgICAgIC0gODAwOTo4MFxuICAjICAgdm9sdW1lczpcbiAgIyAgICAgLSAuL2VsZW1lbnRfY29uZmlnLmpzb246L2FwcC9jb25maWcuanNvblxuICAjICAgZGVwZW5kc19vbjpcbiAgIyAgICAgLSBob21lc2VydmVyXG5cbnZvbHVtZXM6XG4gIGRiOlxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbnJlZ2lzdHJhdGlvbl90b2tlbiA9IFwiJHtwYXNzd29yZDoyMH1cIlxuXG5bY29uZmlnXVxuZW52ID0gW1xuICBcIkNPTkRVV1VJVF9TRVJWRVJfTkFNRT0ke21haW5fZG9tYWlufVwiLFxuICBcIkNPTkRVV1VJVF9SRUdJU1RSQVRJT05fVE9LRU49JHtyZWdpc3RyYXRpb25fdG9rZW59XCIsXG5dXG5tb3VudHMgPSBbXVxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJob21lc2VydmVyXCJcbnBvcnQgPSA2XzE2N1xuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuIgp9
```

## Links

`backend`,`chat`,`communication`,`matrix`,`server`

---

Version:`latest`

ConduitConduit is a simple, fast and reliable chat server powered by Matrix

ConfluenceConfluence is a powerful team collaboration and knowledge-sharing tool. It allows you to create, organize, and collaborate on content in a centralized space. Designed for project management, documentation, and team communication, Confluence helps streamline workflows and enhances productivity.

### On this page

ConfigurationBase64LinksTags