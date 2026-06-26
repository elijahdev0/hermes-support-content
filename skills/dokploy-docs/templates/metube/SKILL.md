---
title: "MeTube | Dokploy"
source: "https://docs.dokploy.com/docs/templates/metube"
category: dokploy-docs
created: "2026-06-25T17:21:53.155Z"
---

MeTube | Dokploy

# MeTube

Copy as Markdown

MeTube is a web-based YouTube downloader that allows downloading videos and audio using yt-dlp.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  metube:
    image: ghcr.io/alexta69/metube
    restart: unless-stopped
    ports:
      - 8081
    volumes:
      - ../files/downloads:/downloads
```

```
[variables]
main_domain = "${domain}"

[config]
[[config.domains]]
serviceName = "metube"
port = 8081
host = "${main_domain}"

[config.env]
UID = "1000"
GID = "1000"
UMASK = "022"
DEFAULT_THEME = "auto"
DOWNLOAD_DIR = "/downloads"
AUDIO_DOWNLOAD_DIR = "/downloads"
DOWNLOAD_DIRS_INDEXABLE = "false"
CUSTOM_DIRS = "true"
CREATE_CUSTOM_DIRS = "true"
CUSTOM_DIRS_EXCLUDE_REGEX = "(^|/)[.@].*$" # Regex to exclude certain directories
STATE_DIR = "/downloads/.metube"
TEMP_DIR = "/downloads"
DELETE_FILE_ON_TRASHCAN = "false" # Delete files when trashed from UI
URL_PREFIX = "/"
PUBLIC_HOST_URL = "" # Base URL for download links (optional)
HTTPS = "false" # Use HTTPS (requires CERTFILE and KEYFILE)
CERTFILE = ""
KEYFILE = ""
PUBLIC_HOST_AUDIO_URL = ""
OUTPUT_TEMPLATE = "%(title)s.%(ext)s" # Filename template for videos
OUTPUT_TEMPLATE_CHAPTER = "%(title)s - %(section_number)s %(section_title)s.%(ext)s"
OUTPUT_TEMPLATE_PLAYLIST = "%(playlist_title)s/%(title)s.%(ext)s"
DEFAULT_OPTION_PLAYLIST_STRICT_MODE = "false"
DEFAULT_OPTION_PLAYLIST_ITEM_LIMIT = "0"
YTDL_OPTIONS = "{}" # Additional yt-dlp options in JSON format
YTDL_OPTIONS_FILE = ""
ROBOTS_TXT = ""
DOWNLOAD_MODE = "limited"
MAX_CONCURRENT_DOWNLOADS = "3"
LOGLEVEL = "INFO"
ENABLE_ACCESSLOG = "false"

[[config.mounts]]
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBtZXR1YmU6XG4gICAgaW1hZ2U6IGdoY3IuaW8vYWxleHRhNjkvbWV0dWJlXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBwb3J0czpcbiAgICAgIC0gODA4MVxuICAgIHZvbHVtZXM6XG4gICAgICAtIC4uL2ZpbGVzL2Rvd25sb2FkczovZG93bmxvYWRzXG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuXG5bY29uZmlnXVxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwibWV0dWJlXCJcbnBvcnQgPSA4MDgxXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuVUlEID0gXCIxMDAwXCIgXG5HSUQgPSBcIjEwMDBcIiBcblVNQVNLID0gXCIwMjJcIlxuREVGQVVMVF9USEVNRSA9IFwiYXV0b1wiIFxuRE9XTkxPQURfRElSID0gXCIvZG93bmxvYWRzXCIgXG5BVURJT19ET1dOTE9BRF9ESVIgPSBcIi9kb3dubG9hZHNcIiBcbkRPV05MT0FEX0RJUlNfSU5ERVhBQkxFID0gXCJmYWxzZVwiIFxuQ1VTVE9NX0RJUlMgPSBcInRydWVcIiBcbkNSRUFURV9DVVNUT01fRElSUyA9IFwidHJ1ZVwiXG5DVVNUT01fRElSU19FWENMVURFX1JFR0VYID0gXCIoXnwvKVsuQF0uKiRcIiAjIFJlZ2V4IHRvIGV4Y2x1ZGUgY2VydGFpbiBkaXJlY3Rvcmllc1xuU1RBVEVfRElSID0gXCIvZG93bmxvYWRzLy5tZXR1YmVcIiBcblRFTVBfRElSID0gXCIvZG93bmxvYWRzXCIgXG5ERUxFVEVfRklMRV9PTl9UUkFTSENBTiA9IFwiZmFsc2VcIiAjIERlbGV0ZSBmaWxlcyB3aGVuIHRyYXNoZWQgZnJvbSBVSVxuVVJMX1BSRUZJWCA9IFwiL1wiIFxuUFVCTElDX0hPU1RfVVJMID0gXCJcIiAjIEJhc2UgVVJMIGZvciBkb3dubG9hZCBsaW5rcyAob3B0aW9uYWwpXG5IVFRQUyA9IFwiZmFsc2VcIiAjIFVzZSBIVFRQUyAocmVxdWlyZXMgQ0VSVEZJTEUgYW5kIEtFWUZJTEUpXG5DRVJURklMRSA9IFwiXCIgXG5LRVlGSUxFID0gXCJcIlxuUFVCTElDX0hPU1RfQVVESU9fVVJMID0gXCJcIiBcbk9VVFBVVF9URU1QTEFURSA9IFwiJSh0aXRsZSlzLiUoZXh0KXNcIiAjIEZpbGVuYW1lIHRlbXBsYXRlIGZvciB2aWRlb3Ncbk9VVFBVVF9URU1QTEFURV9DSEFQVEVSID0gXCIlKHRpdGxlKXMgLSAlKHNlY3Rpb25fbnVtYmVyKXMgJShzZWN0aW9uX3RpdGxlKXMuJShleHQpc1wiIFxuT1VUUFVUX1RFTVBMQVRFX1BMQVlMSVNUID0gXCIlKHBsYXlsaXN0X3RpdGxlKXMvJSh0aXRsZSlzLiUoZXh0KXNcIiBcbkRFRkFVTFRfT1BUSU9OX1BMQVlMSVNUX1NUUklDVF9NT0RFID0gXCJmYWxzZVwiIFxuREVGQVVMVF9PUFRJT05fUExBWUxJU1RfSVRFTV9MSU1JVCA9IFwiMFwiIFxuWVRETF9PUFRJT05TID0gXCJ7fVwiICMgQWRkaXRpb25hbCB5dC1kbHAgb3B0aW9ucyBpbiBKU09OIGZvcm1hdFxuWVRETF9PUFRJT05TX0ZJTEUgPSBcIlwiIFxuUk9CT1RTX1RYVCA9IFwiXCIgXG5ET1dOTE9BRF9NT0RFID0gXCJsaW1pdGVkXCIgXG5NQVhfQ09OQ1VSUkVOVF9ET1dOTE9BRFMgPSBcIjNcIiBcbkxPR0xFVkVMID0gXCJJTkZPXCIgXG5FTkFCTEVfQUNDRVNTTE9HID0gXCJmYWxzZVwiIFxuXG5bW2NvbmZpZy5tb3VudHNdXVxuIgp9
```

## Links

`downloader`,`youtube`,`media`

---

Version:`latest`

MetabaseMetabase is an open source business intelligence tool that allows you to ask questions and visualize data.

MinepanelWeb panel for managing Minecraft servers with Docker. Create, configure, start/stop, and monitor multiple instances from a modern UI.

### On this page

ConfigurationBase64LinksTags