---
title: "Nextcloud | Dokploy"
source: "https://docs.dokploy.com/docs/templates/nextcloud-aio"
category: dokploy-docs
created: "2026-06-25T17:21:54.354Z"
---

Nextcloud | Dokploy

# Nextcloud

Copy as Markdown

Nextcloud is a self-hosted file storage and sync platform with powerful collaboration capabilities. It integrates Files, Talk, Groupware, Office, Assistant and more into a single platform for remote work and data protection.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  nextcloud:
    image: nextcloud:stable
    restart: always
    volumes:
      - nextcloud_data:/var/www/html
      - ../files/fix-nextcloud.sh:/usr/local/bin/fix-nextcloud.sh:ro
    environment:
      - MYSQL_HOST=nextcloud_db
      - MYSQL_DATABASE=nextcloud
      - MYSQL_USER=nextcloud
      - MYSQL_PASSWORD=${MYSQL_PASSWORD}
    depends_on:
      - nextcloud_db
      - nextcloud_redis

  nextcloud_db:
    image: mariadb:10.11
    restart: always
    volumes:
      - nextcloud_db_data:/var/lib/mysql
    environment:
      - MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD}
      - MYSQL_DATABASE=nextcloud
      - MYSQL_USER=nextcloud
      - MYSQL_PASSWORD=${MYSQL_PASSWORD}

  nextcloud_redis:
    image: redis:alpine
    restart: always

volumes:
  nextcloud_data:
  nextcloud_db_data:
```

```
[variables]
  domain_name = "${domain}"
  db_password = "${password:32}"
  db_root_password = "${password:32}"
  region = "DE"

[config]
  env = [
    "MYSQL_PASSWORD=${db_password}",
    "MYSQL_ROOT_PASSWORD=${db_root_password}",
    "DEFAULT_PHONE_REGION=${region}",
    "NEXTCLOUD_DOMAIN=${domain_name}",
    "OVERWRITEPROTOCOL=https",
    "TRUSTED_PROXIES=10.0.0.0/8 172.16.0.0/12",
    "REDIS_HOST=nextcloud_redis",
    "MYSQL_DATABASE=nextcloud",
    "MYSQL_USER=nextcloud"
  ]

  [[config.domains]]
    serviceName = "nextcloud"
    port = 80
    host = "${domain_name}"

  [[config.mounts]]
    filePath = "fix-nextcloud.sh"
    content = """#!/bin/sh
#
# Nextcloud Optimization Script
# ==============================
# This script applies production-ready optimizations to Nextcloud.
#
# MANUAL EXECUTION REQUIRED
# -------------------------
# After Nextcloud completes its initial setup (create admin account, etc.),
# run this script manually:
#
# Option 1 (From Dokploy UI):
#   1. Go to your Nextcloud service in Dokploy
#   2. Open the Terminal tab
#   3. Run: su -s /bin/sh www-data -c "/bin/sh /usr/local/bin/fix-nextcloud.sh"
#
# Option 2 (From command line):
#   docker exec -u www-data <container-name> /bin/sh /usr/local/bin/fix-nextcloud.sh
#
# Optimizations include:
# - Trusted proxy configuration for reverse proxy support
# - HTTPS protocol override
# - Regional settings (phone region, maintenance window)
# - Performance optimizations (database repair, missing indices)
# - Redis caching configuration (APCu, distributed, locking)
#
# The script is idempotent - it creates a marker file to prevent re-running.
# To re-run manually: delete /var/www/html/data/.nextcloud-optimized and restart container
#

MARKER_FILE="/var/www/html/data/.nextcloud-optimized"
OCC="php /var/www/html/occ"

# Check if already run
if [ -f "$MARKER_FILE" ]; then
  echo "Optimizations already applied (marker file exists)."
  exit 0
fi

echo "=========================================="
echo "  Nextcloud Optimization Script"
echo "=========================================="
echo ""

# Check if running as www-data
CURRENT_USER=$(whoami)
if [ "$CURRENT_USER" = "www-data" ]; then
  RUN_AS_WWWDATA=""
else
  RUN_AS_WWWDATA="su -s /bin/sh www-data -c"
fi

# Function to run occ command with error handling
run_occ() {
  description="$1"
  shift
  printf "  - %s... " "$description"
  if [ -z "$RUN_AS_WWWDATA" ]; then
    # Already running as www-data
    if $OCC "$@" >/dev/null 2>&1; then
      echo "✓"
      return 0
    else
      echo "✗ (failed, but continuing)"
      return 1
    fi
  else
    # Need to switch to www-data
    if $RUN_AS_WWWDATA "$OCC $*" >/dev/null 2>&1; then
      echo "✓"
      return 0
    else
      echo "✗ (failed, but continuing)"
      return 1
    fi
  fi
}

# Test database connectivity
echo "[1/5] Testing database connectivity..."
if [ -z "$RUN_AS_WWWDATA" ]; then
  if $OCC status >/dev/null 2>&1; then
    echo "  ✓ Database is accessible"
  else
    echo "  ✗ Database not accessible"
    exit 1
  fi
else
  if $RUN_AS_WWWDATA "$OCC status" >/dev/null 2>&1; then
    echo "  ✓ Database is accessible"
  else
    echo "  ✗ Database not accessible"
    exit 1
  fi
fi

# Configure trusted proxies
echo "[2/5] Configuring trusted proxies..."
run_occ "Set trusted proxy 10.0.0.0/8" config:system:set trusted_proxies 0 --value='10.0.0.0/8'
run_occ "Set trusted proxy 172.16.0.0/12" config:system:set trusted_proxies 1 --value='172.16.0.0/12'
run_occ "Set trusted proxy 192.168.0.0/16" config:system:set trusted_proxies 2 --value='192.168.0.0/16'
run_occ "Set HTTPS protocol override" config:system:set overwriteprotocol --value='https'

# Configure regional settings
echo "[3/5] Configuring regional settings..."
run_occ "Set phone region to DE" config:system:set default_phone_region --value='DE'
run_occ "Set maintenance window start" config:system:set maintenance_window_start --value=1 --type=integer

# Run performance optimizations
echo "[4/5] Running performance optimizations..."
echo "  - Running maintenance repair (this may take a while)..."
if [ -z "$RUN_AS_WWWDATA" ]; then
  if $OCC maintenance:repair --include-expensive 2>&1 | grep -q "No repair steps available"; then
    echo "    ✓ No repairs needed"
  else
    echo "    ✓ Repair completed"
  fi
else
  if $RUN_AS_WWWDATA "$OCC maintenance:repair --include-expensive" 2>&1 | grep -q "No repair steps available"; then
    echo "    ✓ No repairs needed"
  else
    echo "    ✓ Repair completed"
  fi
fi
run_occ "Add missing database indices" db:add-missing-indices

# Configure Redis caching
echo "[5/5] Configuring Redis caching..."
run_occ "Set APCu for local cache" config:system:set memcache.local --value='\\OC\\Memcache\\APCu'
run_occ "Set Redis for distributed cache" config:system:set memcache.distributed --value='\\OC\\Memcache\\Redis'
run_occ "Set Redis for locking" config:system:set memcache.locking --value='\\OC\\Memcache\\Redis'
run_occ "Set Redis host" config:system:set redis host --value='nextcloud_redis'
run_occ "Set Redis port" config:system:set redis port --value=6379 --type=integer

# Create marker file
touch "$MARKER_FILE"

echo ""
echo "=========================================="
echo "  Optimization Complete!"
echo "=========================================="
echo "All optimizations have been applied."
echo "Marker file created at: $MARKER_FILE"
echo ""
"""
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBuZXh0Y2xvdWQ6XG4gICAgaW1hZ2U6IG5leHRjbG91ZDpzdGFibGVcbiAgICByZXN0YXJ0OiBhbHdheXNcbiAgICB2b2x1bWVzOlxuICAgICAgLSBuZXh0Y2xvdWRfZGF0YTovdmFyL3d3dy9odG1sXG4gICAgICAtIC4uL2ZpbGVzL2ZpeC1uZXh0Y2xvdWQuc2g6L3Vzci9sb2NhbC9iaW4vZml4LW5leHRjbG91ZC5zaDpyb1xuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBNWVNRTF9IT1NUPW5leHRjbG91ZF9kYlxuICAgICAgLSBNWVNRTF9EQVRBQkFTRT1uZXh0Y2xvdWRcbiAgICAgIC0gTVlTUUxfVVNFUj1uZXh0Y2xvdWRcbiAgICAgIC0gTVlTUUxfUEFTU1dPUkQ9JHtNWVNRTF9QQVNTV09SRH1cbiAgICBkZXBlbmRzX29uOlxuICAgICAgLSBuZXh0Y2xvdWRfZGJcbiAgICAgIC0gbmV4dGNsb3VkX3JlZGlzXG5cbiAgbmV4dGNsb3VkX2RiOlxuICAgIGltYWdlOiBtYXJpYWRiOjEwLjExXG4gICAgcmVzdGFydDogYWx3YXlzXG4gICAgdm9sdW1lczpcbiAgICAgIC0gbmV4dGNsb3VkX2RiX2RhdGE6L3Zhci9saWIvbXlzcWxcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gTVlTUUxfUk9PVF9QQVNTV09SRD0ke01ZU1FMX1JPT1RfUEFTU1dPUkR9XG4gICAgICAtIE1ZU1FMX0RBVEFCQVNFPW5leHRjbG91ZFxuICAgICAgLSBNWVNRTF9VU0VSPW5leHRjbG91ZFxuICAgICAgLSBNWVNRTF9QQVNTV09SRD0ke01ZU1FMX1BBU1NXT1JEfVxuXG4gIG5leHRjbG91ZF9yZWRpczpcbiAgICBpbWFnZTogcmVkaXM6YWxwaW5lXG4gICAgcmVzdGFydDogYWx3YXlzXG5cbnZvbHVtZXM6XG4gIG5leHRjbG91ZF9kYXRhOlxuICBuZXh0Y2xvdWRfZGJfZGF0YToiLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbiAgZG9tYWluX25hbWUgPSBcIiR7ZG9tYWlufVwiXG4gIGRiX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkOjMyfVwiXG4gIGRiX3Jvb3RfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcbiAgcmVnaW9uID0gXCJERVwiXG5cbltjb25maWddXG4gIGVudiA9IFtcbiAgICBcIk1ZU1FMX1BBU1NXT1JEPSR7ZGJfcGFzc3dvcmR9XCIsXG4gICAgXCJNWVNRTF9ST09UX1BBU1NXT1JEPSR7ZGJfcm9vdF9wYXNzd29yZH1cIixcbiAgICBcIkRFRkFVTFRfUEhPTkVfUkVHSU9OPSR7cmVnaW9ufVwiLFxuICAgIFwiTkVYVENMT1VEX0RPTUFJTj0ke2RvbWFpbl9uYW1lfVwiLFxuICAgIFwiT1ZFUldSSVRFUFJPVE9DT0w9aHR0cHNcIixcbiAgICBcIlRSVVNURURfUFJPWElFUz0xMC4wLjAuMC84IDE3Mi4xNi4wLjAvMTJcIixcbiAgICBcIlJFRElTX0hPU1Q9bmV4dGNsb3VkX3JlZGlzXCIsXG4gICAgXCJNWVNRTF9EQVRBQkFTRT1uZXh0Y2xvdWRcIixcbiAgICBcIk1ZU1FMX1VTRVI9bmV4dGNsb3VkXCJcbiAgXVxuXG4gIFtbY29uZmlnLmRvbWFpbnNdXVxuICAgIHNlcnZpY2VOYW1lID0gXCJuZXh0Y2xvdWRcIlxuICAgIHBvcnQgPSA4MFxuICAgIGhvc3QgPSBcIiR7ZG9tYWluX25hbWV9XCJcblxuICBbW2NvbmZpZy5tb3VudHNdXVxuICAgIGZpbGVQYXRoID0gXCJmaXgtbmV4dGNsb3VkLnNoXCJcbiAgICBjb250ZW50ID0gXCJcIlwiIyEvYmluL3NoXG4jXG4jIE5leHRjbG91ZCBPcHRpbWl6YXRpb24gU2NyaXB0XG4jID09PT09PT09PT09PT09PT09PT09PT09PT09PT09PVxuIyBUaGlzIHNjcmlwdCBhcHBsaWVzIHByb2R1Y3Rpb24tcmVhZHkgb3B0aW1pemF0aW9ucyB0byBOZXh0Y2xvdWQuXG4jXG4jIE1BTlVBTCBFWEVDVVRJT04gUkVRVUlSRURcbiMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuIyBBZnRlciBOZXh0Y2xvdWQgY29tcGxldGVzIGl0cyBpbml0aWFsIHNldHVwIChjcmVhdGUgYWRtaW4gYWNjb3VudCwgZXRjLiksXG4jIHJ1biB0aGlzIHNjcmlwdCBtYW51YWxseTpcbiNcbiMgT3B0aW9uIDEgKEZyb20gRG9rcGxveSBVSSk6XG4jICAgMS4gR28gdG8geW91ciBOZXh0Y2xvdWQgc2VydmljZSBpbiBEb2twbG95XG4jICAgMi4gT3BlbiB0aGUgVGVybWluYWwgdGFiXG4jICAgMy4gUnVuOiBzdSAtcyAvYmluL3NoIHd3dy1kYXRhIC1jIFwiL2Jpbi9zaCAvdXNyL2xvY2FsL2Jpbi9maXgtbmV4dGNsb3VkLnNoXCJcbiNcbiMgT3B0aW9uIDIgKEZyb20gY29tbWFuZCBsaW5lKTpcbiMgICBkb2NrZXIgZXhlYyAtdSB3d3ctZGF0YSA8Y29udGFpbmVyLW5hbWU+IC9iaW4vc2ggL3Vzci9sb2NhbC9iaW4vZml4LW5leHRjbG91ZC5zaFxuI1xuIyBPcHRpbWl6YXRpb25zIGluY2x1ZGU6XG4jIC0gVHJ1c3RlZCBwcm94eSBjb25maWd1cmF0aW9uIGZvciByZXZlcnNlIHByb3h5IHN1cHBvcnRcbiMgLSBIVFRQUyBwcm90b2NvbCBvdmVycmlkZVxuIyAtIFJlZ2lvbmFsIHNldHRpbmdzIChwaG9uZSByZWdpb24sIG1haW50ZW5hbmNlIHdpbmRvdylcbiMgLSBQZXJmb3JtYW5jZSBvcHRpbWl6YXRpb25zIChkYXRhYmFzZSByZXBhaXIsIG1pc3NpbmcgaW5kaWNlcylcbiMgLSBSZWRpcyBjYWNoaW5nIGNvbmZpZ3VyYXRpb24gKEFQQ3UsIGRpc3RyaWJ1dGVkLCBsb2NraW5nKVxuI1xuIyBUaGUgc2NyaXB0IGlzIGlkZW1wb3RlbnQgLSBpdCBjcmVhdGVzIGEgbWFya2VyIGZpbGUgdG8gcHJldmVudCByZS1ydW5uaW5nLlxuIyBUbyByZS1ydW4gbWFudWFsbHk6IGRlbGV0ZSAvdmFyL3d3dy9odG1sL2RhdGEvLm5leHRjbG91ZC1vcHRpbWl6ZWQgYW5kIHJlc3RhcnQgY29udGFpbmVyXG4jXG5cbk1BUktFUl9GSUxFPVwiL3Zhci93d3cvaHRtbC9kYXRhLy5uZXh0Y2xvdWQtb3B0aW1pemVkXCJcbk9DQz1cInBocCAvdmFyL3d3dy9odG1sL29jY1wiXG5cbiMgQ2hlY2sgaWYgYWxyZWFkeSBydW5cbmlmIFsgLWYgXCIkTUFSS0VSX0ZJTEVcIiBdOyB0aGVuXG4gIGVjaG8gXCJPcHRpbWl6YXRpb25zIGFscmVhZHkgYXBwbGllZCAobWFya2VyIGZpbGUgZXhpc3RzKS5cIlxuICBleGl0IDBcbmZpXG5cbmVjaG8gXCI9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT1cIlxuZWNobyBcIiAgTmV4dGNsb3VkIE9wdGltaXphdGlvbiBTY3JpcHRcIlxuZWNobyBcIj09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PVwiXG5lY2hvIFwiXCJcblxuIyBDaGVjayBpZiBydW5uaW5nIGFzIHd3dy1kYXRhXG5DVVJSRU5UX1VTRVI9JCh3aG9hbWkpXG5pZiBbIFwiJENVUlJFTlRfVVNFUlwiID0gXCJ3d3ctZGF0YVwiIF07IHRoZW5cbiAgUlVOX0FTX1dXV0RBVEE9XCJcIlxuZWxzZVxuICBSVU5fQVNfV1dXREFUQT1cInN1IC1zIC9iaW4vc2ggd3d3LWRhdGEgLWNcIlxuZmlcblxuIyBGdW5jdGlvbiB0byBydW4gb2NjIGNvbW1hbmQgd2l0aCBlcnJvciBoYW5kbGluZ1xucnVuX29jYygpIHtcbiAgZGVzY3JpcHRpb249XCIkMVwiXG4gIHNoaWZ0XG4gIHByaW50ZiBcIiAgLSAlcy4uLiBcIiBcIiRkZXNjcmlwdGlvblwiXG4gIGlmIFsgLXogXCIkUlVOX0FTX1dXV0RBVEFcIiBdOyB0aGVuXG4gICAgIyBBbHJlYWR5IHJ1bm5pbmcgYXMgd3d3LWRhdGFcbiAgICBpZiAkT0NDIFwiJEBcIiA+L2Rldi9udWxsIDI+JjE7IHRoZW5cbiAgICAgIGVjaG8gXCLinJNcIlxuICAgICAgcmV0dXJuIDBcbiAgICBlbHNlXG4gICAgICBlY2hvIFwi4pyXIChmYWlsZWQsIGJ1dCBjb250aW51aW5nKVwiXG4gICAgICByZXR1cm4gMVxuICAgIGZpXG4gIGVsc2VcbiAgICAjIE5lZWQgdG8gc3dpdGNoIHRvIHd3dy1kYXRhXG4gICAgaWYgJFJVTl9BU19XV1dEQVRBIFwiJE9DQyAkKlwiID4vZGV2L251bGwgMj4mMTsgdGhlblxuICAgICAgZWNobyBcIuKck1wiXG4gICAgICByZXR1cm4gMFxuICAgIGVsc2VcbiAgICAgIGVjaG8gXCLinJcgKGZhaWxlZCwgYnV0IGNvbnRpbnVpbmcpXCJcbiAgICAgIHJldHVybiAxXG4gICAgZmlcbiAgZmlcbn1cblxuIyBUZXN0IGRhdGFiYXNlIGNvbm5lY3Rpdml0eVxuZWNobyBcIlsxLzVdIFRlc3RpbmcgZGF0YWJhc2UgY29ubmVjdGl2aXR5Li4uXCJcbmlmIFsgLXogXCIkUlVOX0FTX1dXV0RBVEFcIiBdOyB0aGVuXG4gIGlmICRPQ0Mgc3RhdHVzID4vZGV2L251bGwgMj4mMTsgdGhlblxuICAgIGVjaG8gXCIgIOKckyBEYXRhYmFzZSBpcyBhY2Nlc3NpYmxlXCJcbiAgZWxzZVxuICAgIGVjaG8gXCIgIOKclyBEYXRhYmFzZSBub3QgYWNjZXNzaWJsZVwiXG4gICAgZXhpdCAxXG4gIGZpXG5lbHNlXG4gIGlmICRSVU5fQVNfV1dXREFUQSBcIiRPQ0Mgc3RhdHVzXCIgPi9kZXYvbnVsbCAyPiYxOyB0aGVuXG4gICAgZWNobyBcIiAg4pyTIERhdGFiYXNlIGlzIGFjY2Vzc2libGVcIlxuICBlbHNlXG4gICAgZWNobyBcIiAg4pyXIERhdGFiYXNlIG5vdCBhY2Nlc3NpYmxlXCJcbiAgICBleGl0IDFcbiAgZmlcbmZpXG5cbiMgQ29uZmlndXJlIHRydXN0ZWQgcHJveGllc1xuZWNobyBcIlsyLzVdIENvbmZpZ3VyaW5nIHRydXN0ZWQgcHJveGllcy4uLlwiXG5ydW5fb2NjIFwiU2V0IHRydXN0ZWQgcHJveHkgMTAuMC4wLjAvOFwiIGNvbmZpZzpzeXN0ZW06c2V0IHRydXN0ZWRfcHJveGllcyAwIC0tdmFsdWU9JzEwLjAuMC4wLzgnXG5ydW5fb2NjIFwiU2V0IHRydXN0ZWQgcHJveHkgMTcyLjE2LjAuMC8xMlwiIGNvbmZpZzpzeXN0ZW06c2V0IHRydXN0ZWRfcHJveGllcyAxIC0tdmFsdWU9JzE3Mi4xNi4wLjAvMTInXG5ydW5fb2NjIFwiU2V0IHRydXN0ZWQgcHJveHkgMTkyLjE2OC4wLjAvMTZcIiBjb25maWc6c3lzdGVtOnNldCB0cnVzdGVkX3Byb3hpZXMgMiAtLXZhbHVlPScxOTIuMTY4LjAuMC8xNidcbnJ1bl9vY2MgXCJTZXQgSFRUUFMgcHJvdG9jb2wgb3ZlcnJpZGVcIiBjb25maWc6c3lzdGVtOnNldCBvdmVyd3JpdGVwcm90b2NvbCAtLXZhbHVlPSdodHRwcydcblxuIyBDb25maWd1cmUgcmVnaW9uYWwgc2V0dGluZ3NcbmVjaG8gXCJbMy81XSBDb25maWd1cmluZyByZWdpb25hbCBzZXR0aW5ncy4uLlwiXG5ydW5fb2NjIFwiU2V0IHBob25lIHJlZ2lvbiB0byBERVwiIGNvbmZpZzpzeXN0ZW06c2V0IGRlZmF1bHRfcGhvbmVfcmVnaW9uIC0tdmFsdWU9J0RFJ1xucnVuX29jYyBcIlNldCBtYWludGVuYW5jZSB3aW5kb3cgc3RhcnRcIiBjb25maWc6c3lzdGVtOnNldCBtYWludGVuYW5jZV93aW5kb3dfc3RhcnQgLS12YWx1ZT0xIC0tdHlwZT1pbnRlZ2VyXG5cbiMgUnVuIHBlcmZvcm1hbmNlIG9wdGltaXphdGlvbnNcbmVjaG8gXCJbNC81XSBSdW5uaW5nIHBlcmZvcm1hbmNlIG9wdGltaXphdGlvbnMuLi5cIlxuZWNobyBcIiAgLSBSdW5uaW5nIG1haW50ZW5hbmNlIHJlcGFpciAodGhpcyBtYXkgdGFrZSBhIHdoaWxlKS4uLlwiXG5pZiBbIC16IFwiJFJVTl9BU19XV1dEQVRBXCIgXTsgdGhlblxuICBpZiAkT0NDIG1haW50ZW5hbmNlOnJlcGFpciAtLWluY2x1ZGUtZXhwZW5zaXZlIDI+JjEgfCBncmVwIC1xIFwiTm8gcmVwYWlyIHN0ZXBzIGF2YWlsYWJsZVwiOyB0aGVuXG4gICAgZWNobyBcIiAgICDinJMgTm8gcmVwYWlycyBuZWVkZWRcIlxuICBlbHNlXG4gICAgZWNobyBcIiAgICDinJMgUmVwYWlyIGNvbXBsZXRlZFwiXG4gIGZpXG5lbHNlXG4gIGlmICRSVU5fQVNfV1dXREFUQSBcIiRPQ0MgbWFpbnRlbmFuY2U6cmVwYWlyIC0taW5jbHVkZS1leHBlbnNpdmVcIiAyPiYxIHwgZ3JlcCAtcSBcIk5vIHJlcGFpciBzdGVwcyBhdmFpbGFibGVcIjsgdGhlblxuICAgIGVjaG8gXCIgICAg4pyTIE5vIHJlcGFpcnMgbmVlZGVkXCJcbiAgZWxzZVxuICAgIGVjaG8gXCIgICAg4pyTIFJlcGFpciBjb21wbGV0ZWRcIlxuICBmaVxuZmlcbnJ1bl9vY2MgXCJBZGQgbWlzc2luZyBkYXRhYmFzZSBpbmRpY2VzXCIgZGI6YWRkLW1pc3NpbmctaW5kaWNlc1xuXG4jIENvbmZpZ3VyZSBSZWRpcyBjYWNoaW5nXG5lY2hvIFwiWzUvNV0gQ29uZmlndXJpbmcgUmVkaXMgY2FjaGluZy4uLlwiXG5ydW5fb2NjIFwiU2V0IEFQQ3UgZm9yIGxvY2FsIGNhY2hlXCIgY29uZmlnOnN5c3RlbTpzZXQgbWVtY2FjaGUubG9jYWwgLS12YWx1ZT0nXFxcXE9DXFxcXE1lbWNhY2hlXFxcXEFQQ3UnXG5ydW5fb2NjIFwiU2V0IFJlZGlzIGZvciBkaXN0cmlidXRlZCBjYWNoZVwiIGNvbmZpZzpzeXN0ZW06c2V0IG1lbWNhY2hlLmRpc3RyaWJ1dGVkIC0tdmFsdWU9J1xcXFxPQ1xcXFxNZW1jYWNoZVxcXFxSZWRpcydcbnJ1bl9vY2MgXCJTZXQgUmVkaXMgZm9yIGxvY2tpbmdcIiBjb25maWc6c3lzdGVtOnNldCBtZW1jYWNoZS5sb2NraW5nIC0tdmFsdWU9J1xcXFxPQ1xcXFxNZW1jYWNoZVxcXFxSZWRpcydcbnJ1bl9vY2MgXCJTZXQgUmVkaXMgaG9zdFwiIGNvbmZpZzpzeXN0ZW06c2V0IHJlZGlzIGhvc3QgLS12YWx1ZT0nbmV4dGNsb3VkX3JlZGlzJ1xucnVuX29jYyBcIlNldCBSZWRpcyBwb3J0XCIgY29uZmlnOnN5c3RlbTpzZXQgcmVkaXMgcG9ydCAtLXZhbHVlPTYzNzkgLS10eXBlPWludGVnZXJcblxuIyBDcmVhdGUgbWFya2VyIGZpbGVcbnRvdWNoIFwiJE1BUktFUl9GSUxFXCJcblxuZWNobyBcIlwiXG5lY2hvIFwiPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09XCJcbmVjaG8gXCIgIE9wdGltaXphdGlvbiBDb21wbGV0ZSFcIlxuZWNobyBcIj09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PVwiXG5lY2hvIFwiQWxsIG9wdGltaXphdGlvbnMgaGF2ZSBiZWVuIGFwcGxpZWQuXCJcbmVjaG8gXCJNYXJrZXIgZmlsZSBjcmVhdGVkIGF0OiAkTUFSS0VSX0ZJTEVcIlxuZWNobyBcIlwiXG5cIlwiXCIiCn0=
```

## Links

`file-manager`,`sync`

---

Version:`stable`

Networking ToolboxA collection of handy networking utilities by Lissy93, packaged as a self-hostable web app.

NginxNginx is an High performance web server

### On this page

ConfigurationBase64LinksTags