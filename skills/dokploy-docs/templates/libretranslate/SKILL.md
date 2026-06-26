---
title: "LibreTranslate | Dokploy"
source: "https://docs.dokploy.com/docs/templates/libretranslate"
category: dokploy-docs
created: "2026-06-25T17:21:52.046Z"
---

LibreTranslate | Dokploy

# LibreTranslate

Copy as Markdown

LibreTranslate is a free and open-source machine translation API, powered by Argos Translate. Self-hosted, no external dependencies, and supports multiple languages.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  libretranslate:
    image: libretranslate/libretranslate:latest
    restart: unless-stopped
    ports:
      - "5000"
    environment:
      # Enables the API key system
      - LT_API_KEYS=true
      # Defines the path for the API keys database INSIDE the container
      - LT_API_KEYS_DB_PATH=/app/db/api_keys.db
      # Optional: Load only the languages you need to save RAM (Spanish, English, Chinese)
      # - LT_LOAD_ONLY=en,es,zh-Hans
      # This ensures the API is not public and does not accept requests when api_key is ""
      # - LT_REQ_LIMIT=0
      # This disables the web UI so it doesn’t show on the link
      # - LT_DISABLE_WEB_UI=true
      # This only allows requests from a specific origin page
      # - LT_REQUIRE_API_KEY_ORIGIN=webthat.canuse.translate.com
    volumes:
      # Volume to store downloaded language models
      - libretranslate_models:/home/libretranslate/.local
      # Volume to store the API keys database
      - libretranslate_api_keys:/app/db

volumes:
  libretranslate_models:
  libretranslate_api_keys:
  # TO GET AN API KEY YOU MUST GO TO THE TERMINAL AND RUN -> ltmanage keys add 1000000
  # To make it work only with an API key, you need to use LT_REQ_LIMIT=0 so it isn’t open to other users
  # For more information, see https://docs.libretranslate.com/guides/manage_api_keys/
```

```
[variables]
main_domain = "${domain}"

[config]
[[config.domains]]
serviceName = "libretranslate"
port = 5000
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIGxpYnJldHJhbnNsYXRlOlxuICAgIGltYWdlOiBsaWJyZXRyYW5zbGF0ZS9saWJyZXRyYW5zbGF0ZTpsYXRlc3RcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIHBvcnRzOlxuICAgICAgLSBcIjUwMDBcIlxuICAgIGVudmlyb25tZW50OlxuICAgICAgIyBFbmFibGVzIHRoZSBBUEkga2V5IHN5c3RlbVxuICAgICAgLSBMVF9BUElfS0VZUz10cnVlXG4gICAgICAjIERlZmluZXMgdGhlIHBhdGggZm9yIHRoZSBBUEkga2V5cyBkYXRhYmFzZSBJTlNJREUgdGhlIGNvbnRhaW5lclxuICAgICAgLSBMVF9BUElfS0VZU19EQl9QQVRIPS9hcHAvZGIvYXBpX2tleXMuZGJcbiAgICAgICMgT3B0aW9uYWw6IExvYWQgb25seSB0aGUgbGFuZ3VhZ2VzIHlvdSBuZWVkIHRvIHNhdmUgUkFNIChTcGFuaXNoLCBFbmdsaXNoLCBDaGluZXNlKVxuICAgICAgIyAtIExUX0xPQURfT05MWT1lbixlcyx6aC1IYW5zXG4gICAgICAjIFRoaXMgZW5zdXJlcyB0aGUgQVBJIGlzIG5vdCBwdWJsaWMgYW5kIGRvZXMgbm90IGFjY2VwdCByZXF1ZXN0cyB3aGVuIGFwaV9rZXkgaXMgXCJcIlxuICAgICAgIyAtIExUX1JFUV9MSU1JVD0wXG4gICAgICAjIFRoaXMgZGlzYWJsZXMgdGhlIHdlYiBVSSBzbyBpdCBkb2VzbuKAmXQgc2hvdyBvbiB0aGUgbGlua1xuICAgICAgIyAtIExUX0RJU0FCTEVfV0VCX1VJPXRydWVcbiAgICAgICMgVGhpcyBvbmx5IGFsbG93cyByZXF1ZXN0cyBmcm9tIGEgc3BlY2lmaWMgb3JpZ2luIHBhZ2VcbiAgICAgICMgLSBMVF9SRVFVSVJFX0FQSV9LRVlfT1JJR0lOPXdlYnRoYXQuY2FudXNlLnRyYW5zbGF0ZS5jb21cbiAgICB2b2x1bWVzOlxuICAgICAgIyBWb2x1bWUgdG8gc3RvcmUgZG93bmxvYWRlZCBsYW5ndWFnZSBtb2RlbHNcbiAgICAgIC0gbGlicmV0cmFuc2xhdGVfbW9kZWxzOi9ob21lL2xpYnJldHJhbnNsYXRlLy5sb2NhbFxuICAgICAgIyBWb2x1bWUgdG8gc3RvcmUgdGhlIEFQSSBrZXlzIGRhdGFiYXNlXG4gICAgICAtIGxpYnJldHJhbnNsYXRlX2FwaV9rZXlzOi9hcHAvZGJcblxudm9sdW1lczpcbiAgbGlicmV0cmFuc2xhdGVfbW9kZWxzOlxuICBsaWJyZXRyYW5zbGF0ZV9hcGlfa2V5czpcbiAgIyBUTyBHRVQgQU4gQVBJIEtFWSBZT1UgTVVTVCBHTyBUTyBUSEUgVEVSTUlOQUwgQU5EIFJVTiAtPiBsdG1hbmFnZSBrZXlzIGFkZCAxMDAwMDAwXG4gICMgVG8gbWFrZSBpdCB3b3JrIG9ubHkgd2l0aCBhbiBBUEkga2V5LCB5b3UgbmVlZCB0byB1c2UgTFRfUkVRX0xJTUlUPTAgc28gaXQgaXNu4oCZdCBvcGVuIHRvIG90aGVyIHVzZXJzXG4gICMgRm9yIG1vcmUgaW5mb3JtYXRpb24sIHNlZSBodHRwczovL2RvY3MubGlicmV0cmFuc2xhdGUuY29tL2d1aWRlcy9tYW5hZ2VfYXBpX2tleXMvXG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuXG5bY29uZmlnXVxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwibGlicmV0cmFuc2xhdGVcIlxucG9ydCA9IDUwMDBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCIiCn0=
```

## Links

`translation`,`api`,`nlp`,`language`

---

Version:`1.7.3`

LibredeskOpen source, self-hosted customer support desk. Single binary app.

LinkdingLinkding is a self-hosted bookmark manager with a clean and simple interface.

### On this page

ConfigurationBase64LinksTags