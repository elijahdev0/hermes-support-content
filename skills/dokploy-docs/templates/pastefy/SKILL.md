---
title: "Pastefy | Dokploy"
source: "https://docs.dokploy.com/docs/templates/pastefy"
category: dokploy-docs
created: "2026-06-25T17:21:55.477Z"
---

Pastefy | Dokploy

# Pastefy

Copy as Markdown

Pastefy is an open-source pastebin with support for syntax highlighting and OAuth2 authentication.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"
services:
  db:
    image: mariadb:10.11
    restart: unless-stopped
    volumes:
      - "../files/db:/var/lib/mysql"
    environment:
      MYSQL_ROOT_PASSWORD: ${DB_ROOT_PASSWORD}
      MYSQL_DATABASE: ${DB_NAME}
      MYSQL_USER: ${DB_USER}
      MYSQL_PASSWORD: ${DB_PASSWORD}
  pastefy:
    image: interaapps/pastefy:latest
    restart: unless-stopped
    depends_on:
      - db
    expose:
      - "80"
    environment:
      HTTP_SERVER_PORT: 80
      HTTP_SERVER_CORS: ${HTTP_SERVER_CORS}
      DATABASE_DRIVER: mysql
      DATABASE_NAME: ${DB_NAME}
      DATABASE_USER: ${DB_USER}
      DATABASE_PASSWORD: ${DB_PASSWORD}
      DATABASE_HOST: db
      DATABASE_PORT: 3306
      SERVER_NAME: ${SERVER_NAME}
      OAUTH2_INTERAAPPS_CLIENT_ID: ${OAUTH2_INTERAAPPS_CLIENT_ID}
      OAUTH2_INTERAAPPS_CLIENT_SECRET: ${OAUTH2_INTERAAPPS_CLIENT_SECRET}
      OAUTH2_GITHUB_CLIENT_ID: ${OAUTH2_GITHUB_CLIENT_ID}
      OAUTH2_GITHUB_CLIENT_SECRET: ${OAUTH2_GITHUB_CLIENT_SECRET}
      OAUTH2_GOOGLE_CLIENT_ID: ${OAUTH2_GOOGLE_CLIENT_ID}
      OAUTH2_GOOGLE_CLIENT_SECRET: ${OAUTH2_GOOGLE_CLIENT_SECRET}
      OAUTH2_DISCORD_CLIENT_ID: ${OAUTH2_DISCORD_CLIENT_ID}
      OAUTH2_DISCORD_CLIENT_SECRET: ${OAUTH2_DISCORD_CLIENT_SECRET}
      OAUTH2_TWITCH_CLIENT_ID: ${OAUTH2_TWITCH_CLIENT_ID}
      OAUTH2_TWITCH_CLIENT_SECRET: ${OAUTH2_TWITCH_CLIENT_SECRET}
```

```
[variables]
main_domain = "${domain}"
db_root_password = "${password:32}"
db_password = "${password:32}"
db_user = "pastefy"
db_name = "pastefy"
http_server_cors = "*"
server_name = "https://${main_domain}"
oauth2_interaapps_client_id = "NONE"
oauth2_interaapps_client_secret = ""
oauth2_github_client_id = "NONE"
oauth2_github_client_secret = ""
oauth2_google_client_id = "NONE"
oauth2_google_client_secret = ""
oauth2_discord_client_id = "NONE"
oauth2_discord_client_secret = ""
oauth2_twitch_client_id = "NONE"
oauth2_twitch_client_secret = ""

[[config.domains]]
serviceName = "pastefy"
port = 80
host = "${main_domain}"

[config]
env = [
  "DB_ROOT_PASSWORD=${db_root_password}",
  "DB_NAME=${db_name}",
  "DB_USER=${db_user}",
  "DB_PASSWORD=${db_password}",
  "HTTP_SERVER_CORS=${http_server_cors}",
  "SERVER_NAME=${server_name}",
  "OAUTH2_INTERAAPPS_CLIENT_ID=${oauth2_interaapps_client_id} # Interaapps API Key (optional)",
  "OAUTH2_INTERAAPPS_CLIENT_SECRET=${oauth2_interaapps_client_secret} # Interaapps API Secret (optional)",
  "OAUTH2_GITHUB_CLIENT_ID=${oauth2_github_client_id} # GitHub API Key (optional)",
  "OAUTH2_GITHUB_CLIENT_SECRET=${oauth2_github_client_secret} # GitHub API Secret (optional)",
  "OAUTH2_GOOGLE_CLIENT_ID=${oauth2_google_client_id} # Google API Key (optional)",
  "OAUTH2_GOOGLE_CLIENT_SECRET=${oauth2_google_client_secret} # Google API Secret (optional)",
  "OAUTH2_DISCORD_CLIENT_ID=${oauth2_discord_client_id} # Discord API Key (optional)",
  "OAUTH2_DISCORD_CLIENT_SECRET=${oauth2_discord_client_secret} # Discord API Secret (optional)",
  "OAUTH2_TWITCH_CLIENT_ID=${oauth2_twitch_client_id} # Twitch API Key (optional)",
  "OAUTH2_TWITCH_CLIENT_SECRET=${oauth2_twitch_client_secret} # Twitch API Secret (optional)"
]
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcbnNlcnZpY2VzOlxuICBkYjpcbiAgICBpbWFnZTogbWFyaWFkYjoxMC4xMVxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgdm9sdW1lczpcbiAgICAgIC0gXCIuLi9maWxlcy9kYjovdmFyL2xpYi9teXNxbFwiXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBNWVNRTF9ST09UX1BBU1NXT1JEOiAke0RCX1JPT1RfUEFTU1dPUkR9XG4gICAgICBNWVNRTF9EQVRBQkFTRTogJHtEQl9OQU1FfVxuICAgICAgTVlTUUxfVVNFUjogJHtEQl9VU0VSfVxuICAgICAgTVlTUUxfUEFTU1dPUkQ6ICR7REJfUEFTU1dPUkR9XG4gIHBhc3RlZnk6XG4gICAgaW1hZ2U6IGludGVyYWFwcHMvcGFzdGVmeTpsYXRlc3RcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGRlcGVuZHNfb246XG4gICAgICAtIGRiXG4gICAgZXhwb3NlOlxuICAgICAgLSBcIjgwXCJcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIEhUVFBfU0VSVkVSX1BPUlQ6IDgwXG4gICAgICBIVFRQX1NFUlZFUl9DT1JTOiAke0hUVFBfU0VSVkVSX0NPUlN9XG4gICAgICBEQVRBQkFTRV9EUklWRVI6IG15c3FsXG4gICAgICBEQVRBQkFTRV9OQU1FOiAke0RCX05BTUV9XG4gICAgICBEQVRBQkFTRV9VU0VSOiAke0RCX1VTRVJ9XG4gICAgICBEQVRBQkFTRV9QQVNTV09SRDogJHtEQl9QQVNTV09SRH1cbiAgICAgIERBVEFCQVNFX0hPU1Q6IGRiXG4gICAgICBEQVRBQkFTRV9QT1JUOiAzMzA2XG4gICAgICBTRVJWRVJfTkFNRTogJHtTRVJWRVJfTkFNRX1cbiAgICAgIE9BVVRIMl9JTlRFUkFBUFBTX0NMSUVOVF9JRDogJHtPQVVUSDJfSU5URVJBQVBQU19DTElFTlRfSUR9XG4gICAgICBPQVVUSDJfSU5URVJBQVBQU19DTElFTlRfU0VDUkVUOiAke09BVVRIMl9JTlRFUkFBUFBTX0NMSUVOVF9TRUNSRVR9XG4gICAgICBPQVVUSDJfR0lUSFVCX0NMSUVOVF9JRDogJHtPQVVUSDJfR0lUSFVCX0NMSUVOVF9JRH1cbiAgICAgIE9BVVRIMl9HSVRIVUJfQ0xJRU5UX1NFQ1JFVDogJHtPQVVUSDJfR0lUSFVCX0NMSUVOVF9TRUNSRVR9XG4gICAgICBPQVVUSDJfR09PR0xFX0NMSUVOVF9JRDogJHtPQVVUSDJfR09PR0xFX0NMSUVOVF9JRH1cbiAgICAgIE9BVVRIMl9HT09HTEVfQ0xJRU5UX1NFQ1JFVDogJHtPQVVUSDJfR09PR0xFX0NMSUVOVF9TRUNSRVR9XG4gICAgICBPQVVUSDJfRElTQ09SRF9DTElFTlRfSUQ6ICR7T0FVVEgyX0RJU0NPUkRfQ0xJRU5UX0lEfVxuICAgICAgT0FVVEgyX0RJU0NPUkRfQ0xJRU5UX1NFQ1JFVDogJHtPQVVUSDJfRElTQ09SRF9DTElFTlRfU0VDUkVUfVxuICAgICAgT0FVVEgyX1RXSVRDSF9DTElFTlRfSUQ6ICR7T0FVVEgyX1RXSVRDSF9DTElFTlRfSUR9XG4gICAgICBPQVVUSDJfVFdJVENIX0NMSUVOVF9TRUNSRVQ6ICR7T0FVVEgyX1RXSVRDSF9DTElFTlRfU0VDUkVUfVxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbmRiX3Jvb3RfcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmQ6MzJ9XCJcbmRiX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5kYl91c2VyID0gXCJwYXN0ZWZ5XCJcbmRiX25hbWUgPSBcInBhc3RlZnlcIlxuaHR0cF9zZXJ2ZXJfY29ycyA9IFwiKlwiXG5zZXJ2ZXJfbmFtZSA9IFwiaHR0cHM6Ly8ke21haW5fZG9tYWlufVwiXG5vYXV0aDJfaW50ZXJhYXBwc19jbGllbnRfaWQgPSBcIk5PTkVcIlxub2F1dGgyX2ludGVyYWFwcHNfY2xpZW50X3NlY3JldCA9IFwiXCJcbm9hdXRoMl9naXRodWJfY2xpZW50X2lkID0gXCJOT05FXCJcbm9hdXRoMl9naXRodWJfY2xpZW50X3NlY3JldCA9IFwiXCJcbm9hdXRoMl9nb29nbGVfY2xpZW50X2lkID0gXCJOT05FXCJcbm9hdXRoMl9nb29nbGVfY2xpZW50X3NlY3JldCA9IFwiXCJcbm9hdXRoMl9kaXNjb3JkX2NsaWVudF9pZCA9IFwiTk9ORVwiXG5vYXV0aDJfZGlzY29yZF9jbGllbnRfc2VjcmV0ID0gXCJcIlxub2F1dGgyX3R3aXRjaF9jbGllbnRfaWQgPSBcIk5PTkVcIlxub2F1dGgyX3R3aXRjaF9jbGllbnRfc2VjcmV0ID0gXCJcIlxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJwYXN0ZWZ5XCJcbnBvcnQgPSA4MFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnXVxuZW52ID0gW1xuICBcIkRCX1JPT1RfUEFTU1dPUkQ9JHtkYl9yb290X3Bhc3N3b3JkfVwiLFxuICBcIkRCX05BTUU9JHtkYl9uYW1lfVwiLFxuICBcIkRCX1VTRVI9JHtkYl91c2VyfVwiLFxuICBcIkRCX1BBU1NXT1JEPSR7ZGJfcGFzc3dvcmR9XCIsXG4gIFwiSFRUUF9TRVJWRVJfQ09SUz0ke2h0dHBfc2VydmVyX2NvcnN9XCIsXG4gIFwiU0VSVkVSX05BTUU9JHtzZXJ2ZXJfbmFtZX1cIixcbiAgXCJPQVVUSDJfSU5URVJBQVBQU19DTElFTlRfSUQ9JHtvYXV0aDJfaW50ZXJhYXBwc19jbGllbnRfaWR9ICMgSW50ZXJhYXBwcyBBUEkgS2V5IChvcHRpb25hbClcIixcbiAgXCJPQVVUSDJfSU5URVJBQVBQU19DTElFTlRfU0VDUkVUPSR7b2F1dGgyX2ludGVyYWFwcHNfY2xpZW50X3NlY3JldH0gIyBJbnRlcmFhcHBzIEFQSSBTZWNyZXQgKG9wdGlvbmFsKVwiLFxuICBcIk9BVVRIMl9HSVRIVUJfQ0xJRU5UX0lEPSR7b2F1dGgyX2dpdGh1Yl9jbGllbnRfaWR9ICMgR2l0SHViIEFQSSBLZXkgKG9wdGlvbmFsKVwiLFxuICBcIk9BVVRIMl9HSVRIVUJfQ0xJRU5UX1NFQ1JFVD0ke29hdXRoMl9naXRodWJfY2xpZW50X3NlY3JldH0gIyBHaXRIdWIgQVBJIFNlY3JldCAob3B0aW9uYWwpXCIsXG4gIFwiT0FVVEgyX0dPT0dMRV9DTElFTlRfSUQ9JHtvYXV0aDJfZ29vZ2xlX2NsaWVudF9pZH0gIyBHb29nbGUgQVBJIEtleSAob3B0aW9uYWwpXCIsXG4gIFwiT0FVVEgyX0dPT0dMRV9DTElFTlRfU0VDUkVUPSR7b2F1dGgyX2dvb2dsZV9jbGllbnRfc2VjcmV0fSAjIEdvb2dsZSBBUEkgU2VjcmV0IChvcHRpb25hbClcIixcbiAgXCJPQVVUSDJfRElTQ09SRF9DTElFTlRfSUQ9JHtvYXV0aDJfZGlzY29yZF9jbGllbnRfaWR9ICMgRGlzY29yZCBBUEkgS2V5IChvcHRpb25hbClcIixcbiAgXCJPQVVUSDJfRElTQ09SRF9DTElFTlRfU0VDUkVUPSR7b2F1dGgyX2Rpc2NvcmRfY2xpZW50X3NlY3JldH0gIyBEaXNjb3JkIEFQSSBTZWNyZXQgKG9wdGlvbmFsKVwiLFxuICBcIk9BVVRIMl9UV0lUQ0hfQ0xJRU5UX0lEPSR7b2F1dGgyX3R3aXRjaF9jbGllbnRfaWR9ICMgVHdpdGNoIEFQSSBLZXkgKG9wdGlvbmFsKVwiLFxuICBcIk9BVVRIMl9UV0lUQ0hfQ0xJRU5UX1NFQ1JFVD0ke29hdXRoMl90d2l0Y2hfY2xpZW50X3NlY3JldH0gIyBUd2l0Y2ggQVBJIFNlY3JldCAob3B0aW9uYWwpXCJcbl0iCn0=
```

## Links

`pastebin`,`text-sharing`,`collaboration`,`oauth2`

---

Version:`latest`

PassboltPassbolt is an open source credential platform for modern teams. A versatile, battle-tested solution to manage and collaborate on passwords, accesses, and secrets. All in one.

PaymenterPaymenter is a modern billing and payment management system for hosting providers, with automation, invoicing, and client management features.

### On this page

ConfigurationBase64LinksTags