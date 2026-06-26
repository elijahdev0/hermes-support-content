---
title: "Superset (Unofficial) | Dokploy"
source: "https://docs.dokploy.com/docs/templates/superset"
category: dokploy-docs
created: "2026-06-25T17:22:00.274Z"
---

Superset (Unofficial) | Dokploy

# Superset (Unofficial)

Copy as Markdown

Data visualization and data exploration platform.

## Configuration

docker-compose.ymltemplate.toml

```
# This is an UNOFFICIAL production docker image build for Superset:
# - https://github.com/amancevice/docker-superset
#
#
# ## SETUP INSTRUCTIONS
#
# After deploying this image, you will need to run one of the two
# commands below in a terminal within the superset container:
#      $ superset-demo     # Initialise database + load demo charts/datasets
#      $ superset-init     # Initialise database only
#
# You will be prompted to enter the credentials for the admin user.
#
#
# ## NETWORK INSTRUCTIONS
#
# If you want to connect superset with other internal databases managed by
# Dokploy using internal hostnames, you will need to connect the `superset`
# container to those networks.
#

services:
  superset:
    image: amancevice/superset:6.0.0
    restart: unless-stopped
    #networks:
    #  - dokploy-network
    depends_on:
      - superset_postgres
      - superset_redis
    volumes:
      # This superset_config.py can be edited in Dokploy's UI Advanced -> Volume Mount
      - ../files/superset/superset_config.py:/etc/superset/superset_config.py
    environment:
      SECRET_KEY: ${SECRET_KEY}
      MAPBOX_API_KEY: ${MAPBOX_API_KEY}
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: ${POSTGRES_DB}
      REDIS_PASSWORD: ${REDIS_PASSWORD}
      # Ensure the hosts matches your service names below.
      POSTGRES_HOST: superset_postgres
      REDIS_HOST: superset_redis

  superset_postgres:
    image: postgres:18
    restart: unless-stopped
    environment:
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: ${POSTGRES_DB}
    volumes:
      - superset_postgres_data:/var/lib/postgresql
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U $${POSTGRES_USER} -d $${POSTGRES_DB}"]
      interval: 30s
      timeout: 10s
      retries: 3

  superset_redis:
    image: redis:8
    restart: unless-stopped
    volumes:
      - superset_redis_data:/data
    command: redis-server --requirepass ${REDIS_PASSWORD}
    healthcheck:
      test: ["CMD-SHELL", "redis-cli -a $${REDIS_PASSWORD} ping"]
      interval: 30s
      timeout: 10s
      retries: 3

volumes:
  superset_postgres_data:
  superset_redis_data:
```

```
[variables]
main_domain = "${domain}"
secret_key = "${password:30}"
postgres_password = "${password:30}"
redis_password = "${password:30}"

[[config.domains]]
serviceName = "superset"
port = 8_088
host = "${main_domain}"

[config.env]
SECRET_KEY = "${secret_key}"
MAPBOX_API_KEY = ""
POSTGRES_DB = "superset"
POSTGRES_USER = "superset"
POSTGRES_PASSWORD = "${postgres_password}"
REDIS_PASSWORD = "${redis_password}"

[[config.mounts]]
filePath = "./superset/superset_config.py"
content = """
\"""
For more configuration options, see:
- https://superset.apache.org/docs/configuration/configuring-superset
\"""

import os

SECRET_KEY = os.getenv("SECRET_KEY")
MAPBOX_API_KEY = os.getenv("MAPBOX_API_KEY", "")

CACHE_CONFIG = {
  "CACHE_TYPE": "RedisCache",
  "CACHE_DEFAULT_TIMEOUT": 300,
  "CACHE_KEY_PREFIX": "superset_",
  "CACHE_REDIS_HOST": "redis",
  "CACHE_REDIS_PORT": 6379,
  "CACHE_REDIS_DB": 1,
  "CACHE_REDIS_URL": f"redis://:{os.getenv('REDIS_PASSWORD')}@{os.getenv('REDIS_HOST')}:6379/1",
}

FILTER_STATE_CACHE_CONFIG = {**CACHE_CONFIG, "CACHE_KEY_PREFIX": "superset_filter_"}
EXPLORE_FORM_DATA_CACHE_CONFIG = {**CACHE_CONFIG, "CACHE_KEY_PREFIX": "superset_explore_form_"}

SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST')}:5432/{os.getenv('POSTGRES_DB')}"

# Uncomment if you want to load example data (using "superset load_examples") at the
# same location as your metadata postgresql instance. Otherwise, the default sqlite
# will be used, which will not persist in volume when restarting superset by default.
#SQLALCHEMY_EXAMPLES_URI = SQLALCHEMY_DATABASE_URI
"""
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogIiMgVGhpcyBpcyBhbiBVTk9GRklDSUFMIHByb2R1Y3Rpb24gZG9ja2VyIGltYWdlIGJ1aWxkIGZvciBTdXBlcnNldDpcbiMgLSBodHRwczovL2dpdGh1Yi5jb20vYW1hbmNldmljZS9kb2NrZXItc3VwZXJzZXRcbiNcbiNcbiMgIyMgU0VUVVAgSU5TVFJVQ1RJT05TXG4jXG4jIEFmdGVyIGRlcGxveWluZyB0aGlzIGltYWdlLCB5b3Ugd2lsbCBuZWVkIHRvIHJ1biBvbmUgb2YgdGhlIHR3b1xuIyBjb21tYW5kcyBiZWxvdyBpbiBhIHRlcm1pbmFsIHdpdGhpbiB0aGUgc3VwZXJzZXQgY29udGFpbmVyOlxuIyAgICAgICQgc3VwZXJzZXQtZGVtbyAgICAgIyBJbml0aWFsaXNlIGRhdGFiYXNlICsgbG9hZCBkZW1vIGNoYXJ0cy9kYXRhc2V0c1xuIyAgICAgICQgc3VwZXJzZXQtaW5pdCAgICAgIyBJbml0aWFsaXNlIGRhdGFiYXNlIG9ubHlcbiNcbiMgWW91IHdpbGwgYmUgcHJvbXB0ZWQgdG8gZW50ZXIgdGhlIGNyZWRlbnRpYWxzIGZvciB0aGUgYWRtaW4gdXNlci5cbiNcbiNcbiMgIyMgTkVUV09SSyBJTlNUUlVDVElPTlNcbiNcbiMgSWYgeW91IHdhbnQgdG8gY29ubmVjdCBzdXBlcnNldCB3aXRoIG90aGVyIGludGVybmFsIGRhdGFiYXNlcyBtYW5hZ2VkIGJ5XG4jIERva3Bsb3kgdXNpbmcgaW50ZXJuYWwgaG9zdG5hbWVzLCB5b3Ugd2lsbCBuZWVkIHRvIGNvbm5lY3QgdGhlIGBzdXBlcnNldGBcbiMgY29udGFpbmVyIHRvIHRob3NlIG5ldHdvcmtzLlxuI1xuXG5zZXJ2aWNlczpcbiAgc3VwZXJzZXQ6XG4gICAgaW1hZ2U6IGFtYW5jZXZpY2Uvc3VwZXJzZXQ6Ni4wLjBcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgICNuZXR3b3JrczpcbiAgICAjICAtIGRva3Bsb3ktbmV0d29ya1xuICAgIGRlcGVuZHNfb246XG4gICAgICAtIHN1cGVyc2V0X3Bvc3RncmVzXG4gICAgICAtIHN1cGVyc2V0X3JlZGlzXG4gICAgdm9sdW1lczpcbiAgICAgICMgVGhpcyBzdXBlcnNldF9jb25maWcucHkgY2FuIGJlIGVkaXRlZCBpbiBEb2twbG95J3MgVUkgQWR2YW5jZWQgLT4gVm9sdW1lIE1vdW50XG4gICAgICAtIC4uL2ZpbGVzL3N1cGVyc2V0L3N1cGVyc2V0X2NvbmZpZy5weTovZXRjL3N1cGVyc2V0L3N1cGVyc2V0X2NvbmZpZy5weVxuICAgIGVudmlyb25tZW50OlxuICAgICAgU0VDUkVUX0tFWTogJHtTRUNSRVRfS0VZfVxuICAgICAgTUFQQk9YX0FQSV9LRVk6ICR7TUFQQk9YX0FQSV9LRVl9XG4gICAgICBQT1NUR1JFU19VU0VSOiAke1BPU1RHUkVTX1VTRVJ9XG4gICAgICBQT1NUR1JFU19QQVNTV09SRDogJHtQT1NUR1JFU19QQVNTV09SRH1cbiAgICAgIFBPU1RHUkVTX0RCOiAke1BPU1RHUkVTX0RCfVxuICAgICAgUkVESVNfUEFTU1dPUkQ6ICR7UkVESVNfUEFTU1dPUkR9XG4gICAgICAjIEVuc3VyZSB0aGUgaG9zdHMgbWF0Y2hlcyB5b3VyIHNlcnZpY2UgbmFtZXMgYmVsb3cuXG4gICAgICBQT1NUR1JFU19IT1NUOiBzdXBlcnNldF9wb3N0Z3Jlc1xuICAgICAgUkVESVNfSE9TVDogc3VwZXJzZXRfcmVkaXNcblxuICBzdXBlcnNldF9wb3N0Z3JlczpcbiAgICBpbWFnZTogcG9zdGdyZXM6MThcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGVudmlyb25tZW50OlxuICAgICAgUE9TVEdSRVNfVVNFUjogJHtQT1NUR1JFU19VU0VSfVxuICAgICAgUE9TVEdSRVNfUEFTU1dPUkQ6ICR7UE9TVEdSRVNfUEFTU1dPUkR9XG4gICAgICBQT1NUR1JFU19EQjogJHtQT1NUR1JFU19EQn1cbiAgICB2b2x1bWVzOlxuICAgICAgLSBzdXBlcnNldF9wb3N0Z3Jlc19kYXRhOi92YXIvbGliL3Bvc3RncmVzcWxcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6IFtcIkNNRC1TSEVMTFwiLCBcInBnX2lzcmVhZHkgLVUgJCR7UE9TVEdSRVNfVVNFUn0gLWQgJCR7UE9TVEdSRVNfREJ9XCJdXG4gICAgICBpbnRlcnZhbDogMzBzXG4gICAgICB0aW1lb3V0OiAxMHNcbiAgICAgIHJldHJpZXM6IDNcblxuICBzdXBlcnNldF9yZWRpczpcbiAgICBpbWFnZTogcmVkaXM6OFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgdm9sdW1lczpcbiAgICAgIC0gc3VwZXJzZXRfcmVkaXNfZGF0YTovZGF0YVxuICAgIGNvbW1hbmQ6IHJlZGlzLXNlcnZlciAtLXJlcXVpcmVwYXNzICR7UkVESVNfUEFTU1dPUkR9XG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OiBbXCJDTUQtU0hFTExcIiwgXCJyZWRpcy1jbGkgLWEgJCR7UkVESVNfUEFTU1dPUkR9IHBpbmdcIl1cbiAgICAgIGludGVydmFsOiAzMHNcbiAgICAgIHRpbWVvdXQ6IDEwc1xuICAgICAgcmV0cmllczogM1xuXG52b2x1bWVzOlxuICBzdXBlcnNldF9wb3N0Z3Jlc19kYXRhOlxuICBzdXBlcnNldF9yZWRpc19kYXRhOlxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbnNlY3JldF9rZXkgPSBcIiR7cGFzc3dvcmQ6MzB9XCJcbnBvc3RncmVzX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkOjMwfVwiXG5yZWRpc19wYXNzd29yZCA9IFwiJHtwYXNzd29yZDozMH1cIlxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJzdXBlcnNldFwiXG5wb3J0ID0gOF8wODhcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcblxuW2NvbmZpZy5lbnZdXG5TRUNSRVRfS0VZID0gXCIke3NlY3JldF9rZXl9XCJcbk1BUEJPWF9BUElfS0VZID0gXCJcIlxuUE9TVEdSRVNfREIgPSBcInN1cGVyc2V0XCJcblBPU1RHUkVTX1VTRVIgPSBcInN1cGVyc2V0XCJcblBPU1RHUkVTX1BBU1NXT1JEID0gXCIke3Bvc3RncmVzX3Bhc3N3b3JkfVwiXG5SRURJU19QQVNTV09SRCA9IFwiJHtyZWRpc19wYXNzd29yZH1cIlxuXG5bW2NvbmZpZy5tb3VudHNdXVxuZmlsZVBhdGggPSBcIi4vc3VwZXJzZXQvc3VwZXJzZXRfY29uZmlnLnB5XCJcbmNvbnRlbnQgPSBcIlwiXCJcblxcXCJcIlwiXG5Gb3IgbW9yZSBjb25maWd1cmF0aW9uIG9wdGlvbnMsIHNlZTpcbi0gaHR0cHM6Ly9zdXBlcnNldC5hcGFjaGUub3JnL2RvY3MvY29uZmlndXJhdGlvbi9jb25maWd1cmluZy1zdXBlcnNldFxuXFxcIlwiXCJcblxuaW1wb3J0IG9zXG5cblNFQ1JFVF9LRVkgPSBvcy5nZXRlbnYoXCJTRUNSRVRfS0VZXCIpXG5NQVBCT1hfQVBJX0tFWSA9IG9zLmdldGVudihcIk1BUEJPWF9BUElfS0VZXCIsIFwiXCIpXG5cbkNBQ0hFX0NPTkZJRyA9IHtcbiAgXCJDQUNIRV9UWVBFXCI6IFwiUmVkaXNDYWNoZVwiLFxuICBcIkNBQ0hFX0RFRkFVTFRfVElNRU9VVFwiOiAzMDAsXG4gIFwiQ0FDSEVfS0VZX1BSRUZJWFwiOiBcInN1cGVyc2V0X1wiLFxuICBcIkNBQ0hFX1JFRElTX0hPU1RcIjogXCJyZWRpc1wiLFxuICBcIkNBQ0hFX1JFRElTX1BPUlRcIjogNjM3OSxcbiAgXCJDQUNIRV9SRURJU19EQlwiOiAxLFxuICBcIkNBQ0hFX1JFRElTX1VSTFwiOiBmXCJyZWRpczovLzp7b3MuZ2V0ZW52KCdSRURJU19QQVNTV09SRCcpfUB7b3MuZ2V0ZW52KCdSRURJU19IT1NUJyl9OjYzNzkvMVwiLFxufVxuXG5GSUxURVJfU1RBVEVfQ0FDSEVfQ09ORklHID0geyoqQ0FDSEVfQ09ORklHLCBcIkNBQ0hFX0tFWV9QUkVGSVhcIjogXCJzdXBlcnNldF9maWx0ZXJfXCJ9XG5FWFBMT1JFX0ZPUk1fREFUQV9DQUNIRV9DT05GSUcgPSB7KipDQUNIRV9DT05GSUcsIFwiQ0FDSEVfS0VZX1BSRUZJWFwiOiBcInN1cGVyc2V0X2V4cGxvcmVfZm9ybV9cIn1cblxuU1FMQUxDSEVNWV9UUkFDS19NT0RJRklDQVRJT05TID0gVHJ1ZVxuU1FMQUxDSEVNWV9EQVRBQkFTRV9VUkkgPSBmXCJwb3N0Z3Jlc3FsK3BzeWNvcGcyOi8ve29zLmdldGVudignUE9TVEdSRVNfVVNFUicpfTp7b3MuZ2V0ZW52KCdQT1NUR1JFU19QQVNTV09SRCcpfUB7b3MuZ2V0ZW52KCdQT1NUR1JFU19IT1NUJyl9OjU0MzIve29zLmdldGVudignUE9TVEdSRVNfREInKX1cIlxuXG4jIFVuY29tbWVudCBpZiB5b3Ugd2FudCB0byBsb2FkIGV4YW1wbGUgZGF0YSAodXNpbmcgXCJzdXBlcnNldCBsb2FkX2V4YW1wbGVzXCIpIGF0IHRoZVxuIyBzYW1lIGxvY2F0aW9uIGFzIHlvdXIgbWV0YWRhdGEgcG9zdGdyZXNxbCBpbnN0YW5jZS4gT3RoZXJ3aXNlLCB0aGUgZGVmYXVsdCBzcWxpdGVcbiMgd2lsbCBiZSB1c2VkLCB3aGljaCB3aWxsIG5vdCBwZXJzaXN0IGluIHZvbHVtZSB3aGVuIHJlc3RhcnRpbmcgc3VwZXJzZXQgYnkgZGVmYXVsdC5cbiNTUUxBTENIRU1ZX0VYQU1QTEVTX1VSSSA9IFNRTEFMQ0hFTVlfREFUQUJBU0VfVVJJIFxuXCJcIlwiXG4iCn0=
```

## Links

`analytics`,`bi`,`dashboard`,`database`,`sql`

---

Version:`6.0.0`

SupaBaseThe open source Firebase alternative. Supabase gives you a dedicated Postgres database to build your web, mobile, and AI applications. This require at least version 0.22.5 of dokploy.

SurrealDBSurrealDB is a native, open-source, multi-model database that lets you store and manage data across relational, document, graph, time-series, vector & search, and geospatial models—all in one place.

### On this page

ConfigurationBase64LinksTags