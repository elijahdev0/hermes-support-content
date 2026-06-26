---
title: "Directory Lister | Dokploy"
source: "https://docs.dokploy.com/docs/templates/directory-lister"
category: dokploy-docs
created: "2026-06-25T17:21:45.078Z"
---

Directory Lister | Dokploy

# Directory Lister

Copy as Markdown

Directory Lister is a simple PHP application that lists the contents of any web-accessible directory and allows navigation there within.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  directory-lister:
    image: directorylister/directorylister:latest
    restart: unless-stopped
    ports:
      # The internal port of the application.
      - 80
    volumes:
      # Mounts a persistent named volume to store directory data.
      - directory-lister-data:/data

volumes:
  # Defines the Docker-managed volume for data persistence.
  directory-lister-data: {}
```

```
[variables]
app_domain = "${domain}"

[config]
[[config.domains]]
serviceName = "directory-lister" # Must match the service name in docker-compose.yml
port = 80
host = "${app_domain}"

[config.env]
# See configuration docs for additional variables: https://www.directorylister.com/docs/configuration
APP_LANGUAGE = "en"
DISPLAY_READMES = "true"
READMES_FIRST = "false"
ZIP_DOWNLOADS = "true"
TIMEZONE = "UTC"

[[config.mounts]]
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBkaXJlY3RvcnktbGlzdGVyOlxuICAgIGltYWdlOiBkaXJlY3RvcnlsaXN0ZXIvZGlyZWN0b3J5bGlzdGVyOmxhdGVzdFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgcG9ydHM6XG4gICAgICAjIFRoZSBpbnRlcm5hbCBwb3J0IG9mIHRoZSBhcHBsaWNhdGlvbi5cbiAgICAgIC0gODBcbiAgICB2b2x1bWVzOlxuICAgICAgIyBNb3VudHMgYSBwZXJzaXN0ZW50IG5hbWVkIHZvbHVtZSB0byBzdG9yZSBkaXJlY3RvcnkgZGF0YS5cbiAgICAgIC0gZGlyZWN0b3J5LWxpc3Rlci1kYXRhOi9kYXRhXG5cbnZvbHVtZXM6XG4gICMgRGVmaW5lcyB0aGUgRG9ja2VyLW1hbmFnZWQgdm9sdW1lIGZvciBkYXRhIHBlcnNpc3RlbmNlLlxuICBkaXJlY3RvcnktbGlzdGVyLWRhdGE6IHt9XG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbmFwcF9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJkaXJlY3RvcnktbGlzdGVyXCIgIyBNdXN0IG1hdGNoIHRoZSBzZXJ2aWNlIG5hbWUgaW4gZG9ja2VyLWNvbXBvc2UueW1sXG5wb3J0ID0gODBcbmhvc3QgPSBcIiR7YXBwX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cbiMgU2VlIGNvbmZpZ3VyYXRpb24gZG9jcyBmb3IgYWRkaXRpb25hbCB2YXJpYWJsZXM6IGh0dHBzOi8vd3d3LmRpcmVjdG9yeWxpc3Rlci5jb20vZG9jcy9jb25maWd1cmF0aW9uXG5BUFBfTEFOR1VBR0UgPSBcImVuXCJcbkRJU1BMQVlfUkVBRE1FUyA9IFwidHJ1ZVwiXG5SRUFETUVTX0ZJUlNUID0gXCJmYWxzZVwiXG5aSVBfRE9XTkxPQURTID0gXCJ0cnVlXCJcblRJTUVaT05FID0gXCJVVENcIlxuXG5cbltbY29uZmlnLm1vdW50c11dXG4iCn0=
```

## Links

`file-manager`,`directory-listing`,`php`

---

Version:`latest`

DataLensA modern, scalable business intelligence and data visualization system.

DirectusDirectus is an open source headless CMS that provides an API-first solution for building custom backends.

### On this page

ConfigurationBase64LinksTags