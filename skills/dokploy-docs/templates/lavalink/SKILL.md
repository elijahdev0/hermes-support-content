---
title: "Lavalink | Dokploy"
source: "https://docs.dokploy.com/docs/templates/lavalink"
category: dokploy-docs
created: "2026-06-25T17:21:52.045Z"
---

Lavalink | Dokploy

# Lavalink

Copy as Markdown

Lavalink is an open source standalone audio sending node based on Lavaplayer.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  fix-perms:
    image: busybox:1.36
    command: >
      sh -c "mkdir -p /opt/Lavalink/plugins &&
             chmod -R 0777 /opt/Lavalink/plugins || true &&
             chown -R 1000:1000 /opt/Lavalink/plugins || true &&
             echo perms-fixed && sleep 1"
    volumes:
      - "../files/plugins/:/opt/Lavalink/plugins/"
      - "../files/application.yml:/opt/Lavalink/application.yml"
    restart: "no"
  lavalink:
    image: ghcr.io/lavalink-devs/lavalink:4
    depends_on:
      - fix-perms
    restart: unless-stopped
    environment:
      _JAVA_OPTIONS: "${_JAVA_OPTIONS:--Xmx6G}"
      LAVALINK_SERVER_PASSWORD: "${LAVALINK_SERVER_PASSWORD:-youshallnotpass}"
      SERVER_PORT: "${SERVER_PORT:-2333}"
    volumes:
      - "../files/application.yml:/opt/Lavalink/application.yml:rw"
      - "../files/plugins/:/opt/Lavalink/plugins/:rw"
    ports:
      - ${SERVER_PORT}

    healthcheck:
      test: >
        sh -c 'wget --header="Authorization: ${LAVALINK_SERVER_PASSWORD}" -qO- http://127.0.0.1:${SERVER_PORT}/v4/info >/dev/null 2>&1 || exit 1'
      interval: 100s
      timeout: 5s
      retries: 5
      start_period: 30s

    entrypoint: >
      sh -c 'until [ -w /opt/Lavalink/plugins ] ; do
                echo "waiting for /opt/Lavalink/plugins to be writable";
                sleep 1;
             done;
             exec java -jar /opt/Lavalink/Lavalink.jar'
```

```
[variables]
main_domain = "${domain}"
server_port = "2333"
lavalink_server_password = "${password}"

[config]
[[config.mounts]]
filePath = "./application.yml"
content = """
server: # REST and WS server
  port: 2333
  address: 0.0.0.0
  http2:
    enabled: false
plugins:
#  name: # Name of the plugin
#    some_key: some_value # Some key-value pair for the plugin
#    another_key: another_value
lavalink:
  plugins:
    # - dependency: "com.github.username.pluginName:pluginName-plugin:x.y.z"
    #   snapshot: false
  # pluginsDir: "/opt/Lavalink/plugins"
  # defaultPluginRepository: "https://maven.lavalink.dev/releases"
  # defaultPluginSnapshotRepository: "https://maven.lavalink.dev/snapshots"
  server:
    password: "youshallnotpass"
    sources:
      # The default Youtube source is now deprecated and won't receive further updates. Please use https://github.com/lavalink-devs/youtube-source#plugin instead.
      youtube: true
      bandcamp: true
      soundcloud: true
      twitch: true
      vimeo: true
      nico: true
      http: true
      local: false
    filters:
      volume: true
      equalizer: true
      karaoke: true
      timescale: true
      tremolo: true
      vibrato: true
      distortion: true
      rotation: true
      channelMix: true
      lowPass: true
    nonAllocatingFrameBuffer: false
    bufferDurationMs: 400
    frameBufferDurationMs: 5000
    opusEncodingQuality: 10
    resamplingQuality: LOW
    trackStuckThresholdMs: 10000
    useSeekGhosting: true
    youtubePlaylistLoadLimit: 6
    playerUpdateInterval: 5
    youtubeSearchEnabled: true
    soundcloudSearchEnabled: true
    gc-warnings: true
    #ratelimit:
      #ipBlocks: ["1.0.0.0/8", "..."] # list of ip blocks
      #excludedIps: ["...", "..."] # ips which should be explicit excluded from usage by lavalink
      #strategy: "RotateOnBan" # RotateOnBan | LoadBalance | NanoSwitch | RotatingNanoSwitch
      #searchTriggersFail: true # Whether a search 429 should trigger marking the ip as failing
      #retryLimit: -1 # -1 = use default lavaplayer value | 0 = infinity | >0 = retry will happen this numbers times
    #youtubeConfig: # Required for avoiding all age restrictions by YouTube, some restricted videos still can be played without.
      #email: "" # Email of Google account
      #password: "" # Password of Google account
    #httpConfig: # Useful for blocking bad-actors from ip-grabbing your music node and attacking it, this way only the http proxy will be attacked
      #proxyHost: "localhost" # Hostname of the proxy, (ip or domain)
      #proxyPort: 3128 # Proxy port, 3128 is the default for squidProxy
      #proxyUser: "" # Optional user for basic authentication fields, leave blank if you don't use basic auth
      #proxyPassword: "" # Password for basic authentication
    timeouts:
      connectTimeoutMs: 3000
      connectionRequestTimeoutMs: 3000
      socketTimeoutMs: 3000

metrics:
  prometheus:
    enabled: false
    endpoint: /metrics

sentry:
  dsn: ""
  environment: ""
#  tags:
#    some_key: some_value
#    another_key: another_value

logging:
  file:
    path: ./logs/

  level:
    root: INFO
    lavalink: INFO

  request:
    enabled: true
    includeClientInfo: true
    includeHeaders: false
    includeQueryString: true
    includePayload: true
    maxPayloadLength: 10000

  logback:
    rollingpolicy:
      max-file-size: 1GB
      max-history: 30
"""

[[config.domains]]
serviceName = "lavalink"
port = 2_333
host = "${main_domain}"

[config.env]
_JAVA_OPTIONS = "-Xmx6G"
LAVALINK_SERVER_PASSWORD = "${lavalink_server_password}"
SERVER_PORT = "${server_port}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBmaXgtcGVybXM6XG4gICAgaW1hZ2U6IGJ1c3lib3g6MS4zNlxuICAgIGNvbW1hbmQ6ID5cbiAgICAgIHNoIC1jIFwibWtkaXIgLXAgL29wdC9MYXZhbGluay9wbHVnaW5zICYmXG4gICAgICAgICAgICAgY2htb2QgLVIgMDc3NyAvb3B0L0xhdmFsaW5rL3BsdWdpbnMgfHwgdHJ1ZSAmJlxuICAgICAgICAgICAgIGNob3duIC1SIDEwMDA6MTAwMCAvb3B0L0xhdmFsaW5rL3BsdWdpbnMgfHwgdHJ1ZSAmJlxuICAgICAgICAgICAgIGVjaG8gcGVybXMtZml4ZWQgJiYgc2xlZXAgMVwiXG4gICAgdm9sdW1lczpcbiAgICAgIC0gXCIuLi9maWxlcy9wbHVnaW5zLzovb3B0L0xhdmFsaW5rL3BsdWdpbnMvXCJcbiAgICAgIC0gXCIuLi9maWxlcy9hcHBsaWNhdGlvbi55bWw6L29wdC9MYXZhbGluay9hcHBsaWNhdGlvbi55bWxcIlxuICAgIHJlc3RhcnQ6IFwibm9cIlxuICBsYXZhbGluazpcbiAgICBpbWFnZTogZ2hjci5pby9sYXZhbGluay1kZXZzL2xhdmFsaW5rOjRcbiAgICBkZXBlbmRzX29uOlxuICAgICAgLSBmaXgtcGVybXNcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGVudmlyb25tZW50OlxuICAgICAgX0pBVkFfT1BUSU9OUzogXCIke19KQVZBX09QVElPTlM6LS1YbXg2R31cIlxuICAgICAgTEFWQUxJTktfU0VSVkVSX1BBU1NXT1JEOiBcIiR7TEFWQUxJTktfU0VSVkVSX1BBU1NXT1JEOi15b3VzaGFsbG5vdHBhc3N9XCJcbiAgICAgIFNFUlZFUl9QT1JUOiBcIiR7U0VSVkVSX1BPUlQ6LTIzMzN9XCJcbiAgICB2b2x1bWVzOlxuICAgICAgLSBcIi4uL2ZpbGVzL2FwcGxpY2F0aW9uLnltbDovb3B0L0xhdmFsaW5rL2FwcGxpY2F0aW9uLnltbDpyd1wiXG4gICAgICAtIFwiLi4vZmlsZXMvcGx1Z2lucy86L29wdC9MYXZhbGluay9wbHVnaW5zLzpyd1wiXG4gICAgcG9ydHM6XG4gICAgICAtICR7U0VSVkVSX1BPUlR9XG5cbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6ID5cbiAgICAgICAgc2ggLWMgJ3dnZXQgLS1oZWFkZXI9XCJBdXRob3JpemF0aW9uOiAke0xBVkFMSU5LX1NFUlZFUl9QQVNTV09SRH1cIiAtcU8tIGh0dHA6Ly8xMjcuMC4wLjE6JHtTRVJWRVJfUE9SVH0vdjQvaW5mbyA+L2Rldi9udWxsIDI+JjEgfHwgZXhpdCAxJ1xuICAgICAgaW50ZXJ2YWw6IDEwMHNcbiAgICAgIHRpbWVvdXQ6IDVzXG4gICAgICByZXRyaWVzOiA1XG4gICAgICBzdGFydF9wZXJpb2Q6IDMwc1xuXG4gICAgZW50cnlwb2ludDogPlxuICAgICAgc2ggLWMgJ3VudGlsIFsgLXcgL29wdC9MYXZhbGluay9wbHVnaW5zIF0gOyBkb1xuICAgICAgICAgICAgICAgIGVjaG8gXCJ3YWl0aW5nIGZvciAvb3B0L0xhdmFsaW5rL3BsdWdpbnMgdG8gYmUgd3JpdGFibGVcIjtcbiAgICAgICAgICAgICAgICBzbGVlcCAxO1xuICAgICAgICAgICAgIGRvbmU7XG4gICAgICAgICAgICAgZXhlYyBqYXZhIC1qYXIgL29wdC9MYXZhbGluay9MYXZhbGluay5qYXInXG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxuc2VydmVyX3BvcnQgPSBcIjIzMzNcIlxubGF2YWxpbmtfc2VydmVyX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkfVwiXG5cbltjb25maWddXG5bW2NvbmZpZy5tb3VudHNdXVxuZmlsZVBhdGggPSBcIi4vYXBwbGljYXRpb24ueW1sXCJcbmNvbnRlbnQgPSBcIlwiXCJcbnNlcnZlcjogIyBSRVNUIGFuZCBXUyBzZXJ2ZXJcbiAgcG9ydDogMjMzM1xuICBhZGRyZXNzOiAwLjAuMC4wXG4gIGh0dHAyOlxuICAgIGVuYWJsZWQ6IGZhbHNlXG5wbHVnaW5zOlxuIyAgbmFtZTogIyBOYW1lIG9mIHRoZSBwbHVnaW5cbiMgICAgc29tZV9rZXk6IHNvbWVfdmFsdWUgIyBTb21lIGtleS12YWx1ZSBwYWlyIGZvciB0aGUgcGx1Z2luXG4jICAgIGFub3RoZXJfa2V5OiBhbm90aGVyX3ZhbHVlXG5sYXZhbGluazpcbiAgcGx1Z2luczpcbiAgICAjIC0gZGVwZW5kZW5jeTogXCJjb20uZ2l0aHViLnVzZXJuYW1lLnBsdWdpbk5hbWU6cGx1Z2luTmFtZS1wbHVnaW46eC55LnpcIlxuICAgICMgICBzbmFwc2hvdDogZmFsc2VcbiAgIyBwbHVnaW5zRGlyOiBcIi9vcHQvTGF2YWxpbmsvcGx1Z2luc1wiXG4gICMgZGVmYXVsdFBsdWdpblJlcG9zaXRvcnk6IFwiaHR0cHM6Ly9tYXZlbi5sYXZhbGluay5kZXYvcmVsZWFzZXNcIlxuICAjIGRlZmF1bHRQbHVnaW5TbmFwc2hvdFJlcG9zaXRvcnk6IFwiaHR0cHM6Ly9tYXZlbi5sYXZhbGluay5kZXYvc25hcHNob3RzXCJcbiAgc2VydmVyOlxuICAgIHBhc3N3b3JkOiBcInlvdXNoYWxsbm90cGFzc1wiXG4gICAgc291cmNlczpcbiAgICAgICMgVGhlIGRlZmF1bHQgWW91dHViZSBzb3VyY2UgaXMgbm93IGRlcHJlY2F0ZWQgYW5kIHdvbid0IHJlY2VpdmUgZnVydGhlciB1cGRhdGVzLiBQbGVhc2UgdXNlIGh0dHBzOi8vZ2l0aHViLmNvbS9sYXZhbGluay1kZXZzL3lvdXR1YmUtc291cmNlI3BsdWdpbiBpbnN0ZWFkLlxuICAgICAgeW91dHViZTogdHJ1ZVxuICAgICAgYmFuZGNhbXA6IHRydWVcbiAgICAgIHNvdW5kY2xvdWQ6IHRydWVcbiAgICAgIHR3aXRjaDogdHJ1ZVxuICAgICAgdmltZW86IHRydWVcbiAgICAgIG5pY286IHRydWVcbiAgICAgIGh0dHA6IHRydWVcbiAgICAgIGxvY2FsOiBmYWxzZVxuICAgIGZpbHRlcnM6XG4gICAgICB2b2x1bWU6IHRydWVcbiAgICAgIGVxdWFsaXplcjogdHJ1ZVxuICAgICAga2FyYW9rZTogdHJ1ZVxuICAgICAgdGltZXNjYWxlOiB0cnVlXG4gICAgICB0cmVtb2xvOiB0cnVlXG4gICAgICB2aWJyYXRvOiB0cnVlXG4gICAgICBkaXN0b3J0aW9uOiB0cnVlXG4gICAgICByb3RhdGlvbjogdHJ1ZVxuICAgICAgY2hhbm5lbE1peDogdHJ1ZVxuICAgICAgbG93UGFzczogdHJ1ZVxuICAgIG5vbkFsbG9jYXRpbmdGcmFtZUJ1ZmZlcjogZmFsc2VcbiAgICBidWZmZXJEdXJhdGlvbk1zOiA0MDBcbiAgICBmcmFtZUJ1ZmZlckR1cmF0aW9uTXM6IDUwMDBcbiAgICBvcHVzRW5jb2RpbmdRdWFsaXR5OiAxMFxuICAgIHJlc2FtcGxpbmdRdWFsaXR5OiBMT1dcbiAgICB0cmFja1N0dWNrVGhyZXNob2xkTXM6IDEwMDAwXG4gICAgdXNlU2Vla0dob3N0aW5nOiB0cnVlXG4gICAgeW91dHViZVBsYXlsaXN0TG9hZExpbWl0OiA2XG4gICAgcGxheWVyVXBkYXRlSW50ZXJ2YWw6IDVcbiAgICB5b3V0dWJlU2VhcmNoRW5hYmxlZDogdHJ1ZVxuICAgIHNvdW5kY2xvdWRTZWFyY2hFbmFibGVkOiB0cnVlXG4gICAgZ2Mtd2FybmluZ3M6IHRydWVcbiAgICAjcmF0ZWxpbWl0OlxuICAgICAgI2lwQmxvY2tzOiBbXCIxLjAuMC4wLzhcIiwgXCIuLi5cIl0gIyBsaXN0IG9mIGlwIGJsb2Nrc1xuICAgICAgI2V4Y2x1ZGVkSXBzOiBbXCIuLi5cIiwgXCIuLi5cIl0gIyBpcHMgd2hpY2ggc2hvdWxkIGJlIGV4cGxpY2l0IGV4Y2x1ZGVkIGZyb20gdXNhZ2UgYnkgbGF2YWxpbmtcbiAgICAgICNzdHJhdGVneTogXCJSb3RhdGVPbkJhblwiICMgUm90YXRlT25CYW4gfCBMb2FkQmFsYW5jZSB8IE5hbm9Td2l0Y2ggfCBSb3RhdGluZ05hbm9Td2l0Y2hcbiAgICAgICNzZWFyY2hUcmlnZ2Vyc0ZhaWw6IHRydWUgIyBXaGV0aGVyIGEgc2VhcmNoIDQyOSBzaG91bGQgdHJpZ2dlciBtYXJraW5nIHRoZSBpcCBhcyBmYWlsaW5nXG4gICAgICAjcmV0cnlMaW1pdDogLTEgIyAtMSA9IHVzZSBkZWZhdWx0IGxhdmFwbGF5ZXIgdmFsdWUgfCAwID0gaW5maW5pdHkgfCA+MCA9IHJldHJ5IHdpbGwgaGFwcGVuIHRoaXMgbnVtYmVycyB0aW1lc1xuICAgICN5b3V0dWJlQ29uZmlnOiAjIFJlcXVpcmVkIGZvciBhdm9pZGluZyBhbGwgYWdlIHJlc3RyaWN0aW9ucyBieSBZb3VUdWJlLCBzb21lIHJlc3RyaWN0ZWQgdmlkZW9zIHN0aWxsIGNhbiBiZSBwbGF5ZWQgd2l0aG91dC5cbiAgICAgICNlbWFpbDogXCJcIiAjIEVtYWlsIG9mIEdvb2dsZSBhY2NvdW50XG4gICAgICAjcGFzc3dvcmQ6IFwiXCIgIyBQYXNzd29yZCBvZiBHb29nbGUgYWNjb3VudFxuICAgICNodHRwQ29uZmlnOiAjIFVzZWZ1bCBmb3IgYmxvY2tpbmcgYmFkLWFjdG9ycyBmcm9tIGlwLWdyYWJiaW5nIHlvdXIgbXVzaWMgbm9kZSBhbmQgYXR0YWNraW5nIGl0LCB0aGlzIHdheSBvbmx5IHRoZSBodHRwIHByb3h5IHdpbGwgYmUgYXR0YWNrZWRcbiAgICAgICNwcm94eUhvc3Q6IFwibG9jYWxob3N0XCIgIyBIb3N0bmFtZSBvZiB0aGUgcHJveHksIChpcCBvciBkb21haW4pXG4gICAgICAjcHJveHlQb3J0OiAzMTI4ICMgUHJveHkgcG9ydCwgMzEyOCBpcyB0aGUgZGVmYXVsdCBmb3Igc3F1aWRQcm94eVxuICAgICAgI3Byb3h5VXNlcjogXCJcIiAjIE9wdGlvbmFsIHVzZXIgZm9yIGJhc2ljIGF1dGhlbnRpY2F0aW9uIGZpZWxkcywgbGVhdmUgYmxhbmsgaWYgeW91IGRvbid0IHVzZSBiYXNpYyBhdXRoXG4gICAgICAjcHJveHlQYXNzd29yZDogXCJcIiAjIFBhc3N3b3JkIGZvciBiYXNpYyBhdXRoZW50aWNhdGlvblxuICAgIHRpbWVvdXRzOlxuICAgICAgY29ubmVjdFRpbWVvdXRNczogMzAwMFxuICAgICAgY29ubmVjdGlvblJlcXVlc3RUaW1lb3V0TXM6IDMwMDBcbiAgICAgIHNvY2tldFRpbWVvdXRNczogMzAwMFxuXG5tZXRyaWNzOlxuICBwcm9tZXRoZXVzOlxuICAgIGVuYWJsZWQ6IGZhbHNlXG4gICAgZW5kcG9pbnQ6IC9tZXRyaWNzXG5cbnNlbnRyeTpcbiAgZHNuOiBcIlwiXG4gIGVudmlyb25tZW50OiBcIlwiXG4jICB0YWdzOlxuIyAgICBzb21lX2tleTogc29tZV92YWx1ZVxuIyAgICBhbm90aGVyX2tleTogYW5vdGhlcl92YWx1ZVxuXG5sb2dnaW5nOlxuICBmaWxlOlxuICAgIHBhdGg6IC4vbG9ncy9cblxuICBsZXZlbDpcbiAgICByb290OiBJTkZPXG4gICAgbGF2YWxpbms6IElORk9cblxuICByZXF1ZXN0OlxuICAgIGVuYWJsZWQ6IHRydWVcbiAgICBpbmNsdWRlQ2xpZW50SW5mbzogdHJ1ZVxuICAgIGluY2x1ZGVIZWFkZXJzOiBmYWxzZVxuICAgIGluY2x1ZGVRdWVyeVN0cmluZzogdHJ1ZVxuICAgIGluY2x1ZGVQYXlsb2FkOiB0cnVlXG4gICAgbWF4UGF5bG9hZExlbmd0aDogMTAwMDBcblxuXG4gIGxvZ2JhY2s6XG4gICAgcm9sbGluZ3BvbGljeTpcbiAgICAgIG1heC1maWxlLXNpemU6IDFHQlxuICAgICAgbWF4LWhpc3Rvcnk6IDMwXG5cIlwiXCJcblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwibGF2YWxpbmtcIlxucG9ydCA9IDJfMzMzXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuX0pBVkFfT1BUSU9OUyA9IFwiLVhteDZHXCJcbkxBVkFMSU5LX1NFUlZFUl9QQVNTV09SRCA9IFwiJHtsYXZhbGlua19zZXJ2ZXJfcGFzc3dvcmR9XCJcblNFUlZFUl9QT1JUID0gXCIke3NlcnZlcl9wb3J0fVwiXG4iCn0=
```

## Links

`voice`,`discord`

---

Version:`4.1.1`

LangflowLangflow is a low-code app builder for RAG and multi-agent AI applications. It's Python-based and agnostic to any model, API, or database.

LetterfeedConvert email newsletters into RSS feeds

### On this page

ConfigurationBase64LinksTags