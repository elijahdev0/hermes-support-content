---
title: "Discord Tickets | Dokploy"
source: "https://docs.dokploy.com/docs/templates/discord-tickets"
category: dokploy-docs
created: "2026-06-25T17:21:46.245Z"
---

Discord Tickets | Dokploy

# Discord Tickets

Copy as Markdown

An open-source Discord bot for creating and managing support ticket channels.

## Configuration

docker-compose.ymltemplate.toml

```
version: "3.8"

services:
  tickets-postgres:
    image: mysql:8
    restart: unless-stopped

    volumes:
      - tickets-mysql-data:/var/lib/mysql
    environment:
      MYSQL_DATABASE: ${MYSQL_DATABASE}
      MYSQL_PASSWORD: ${MYSQL_PASSWORD}
      MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD}
      MYSQL_USER: ${MYSQL_USER}
    healthcheck:
      test: ["CMD", "mysqladmin", "ping", "-h", "localhost", "-u${MYSQL_USER}", "-p${MYSQL_PASSWORD}"]
      interval: 10s
      timeout: 5s
      retries: 5

  tickets-app:
    image: eartharoid/discord-tickets:4.0.21
    depends_on:
      tickets-postgres:
        condition: service_healthy
    restart: unless-stopped

    volumes:
      - tickets-app-data:/home/container/user
      - /etc/timezone:/etc/timezone:ro
      - /etc/localtime:/etc/localtime:ro
    tty: true
    stdin_open: true
    environment:
      DB_CONNECTION_URL: mysql://${MYSQL_USER}:${MYSQL_PASSWORD}@tickets-postgres/${MYSQL_DATABASE}
      DISCORD_SECRET: ${DISCORD_SECRET}
      DISCORD_TOKEN: ${DISCORD_TOKEN}
      ENCRYPTION_KEY: ${ENCRYPTION_KEY}
      DB_PROVIDER: mysql
      HTTP_EXTERNAL: https://${TICKETS_HOST}
      HTTP_HOST: 0.0.0.0
      HTTP_PORT: 8169
      HTTP_TRUST_PROXY: "true"
      PUBLIC_BOT: "false"
      PUBLISH_COMMANDS: "true"
      SUPER: ${SUPER_USERS}

volumes:
  tickets-mysql-data:
  tickets-app-data:
```

```
[variables]
main_domain = "${domain}"
mysql_password = "${password}"
mysql_root_password = "${password}"
mysql_user = "tickets"
mysql_database = "tickets"
encryption_key = "${password:48}"

[config]
env = [
  "TICKETS_HOST=${main_domain}",
  "MYSQL_DATABASE=${mysql_database}",
  "MYSQL_PASSWORD=${mysql_password}",
  "MYSQL_ROOT_PASSWORD=${mysql_root_password}",
  "MYSQL_USER=${mysql_user}",
  "ENCRYPTION_KEY=${encryption_key}",
  "# Follow the guide at: https://discordtickets.app/self-hosting/installation/docker/#creating-the-discord-application",
  "DISCORD_SECRET=",
  "DISCORD_TOKEN=",
  "SUPER_USERS=YOUR_DISCORD_USER_ID",
]
mounts = []

[[config.domains]]
serviceName = "tickets-app"
port = 8_169
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInZlcnNpb246IFwiMy44XCJcblxuc2VydmljZXM6XG4gIHRpY2tldHMtcG9zdGdyZXM6XG4gICAgaW1hZ2U6IG15c3FsOjhcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuXG4gICAgdm9sdW1lczpcbiAgICAgIC0gdGlja2V0cy1teXNxbC1kYXRhOi92YXIvbGliL215c3FsXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBNWVNRTF9EQVRBQkFTRTogJHtNWVNRTF9EQVRBQkFTRX1cbiAgICAgIE1ZU1FMX1BBU1NXT1JEOiAke01ZU1FMX1BBU1NXT1JEfVxuICAgICAgTVlTUUxfUk9PVF9QQVNTV09SRDogJHtNWVNRTF9ST09UX1BBU1NXT1JEfVxuICAgICAgTVlTUUxfVVNFUjogJHtNWVNRTF9VU0VSfVxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDogW1wiQ01EXCIsIFwibXlzcWxhZG1pblwiLCBcInBpbmdcIiwgXCItaFwiLCBcImxvY2FsaG9zdFwiLCBcIi11JHtNWVNRTF9VU0VSfVwiLCBcIi1wJHtNWVNRTF9QQVNTV09SRH1cIl1cbiAgICAgIGludGVydmFsOiAxMHNcbiAgICAgIHRpbWVvdXQ6IDVzXG4gICAgICByZXRyaWVzOiA1XG5cbiAgdGlja2V0cy1hcHA6XG4gICAgaW1hZ2U6IGVhcnRoYXJvaWQvZGlzY29yZC10aWNrZXRzOjQuMC4yMVxuICAgIGRlcGVuZHNfb246XG4gICAgICB0aWNrZXRzLXBvc3RncmVzOlxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2VfaGVhbHRoeVxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG5cbiAgICB2b2x1bWVzOlxuICAgICAgLSB0aWNrZXRzLWFwcC1kYXRhOi9ob21lL2NvbnRhaW5lci91c2VyXG4gICAgICAtIC9ldGMvdGltZXpvbmU6L2V0Yy90aW1lem9uZTpyb1xuICAgICAgLSAvZXRjL2xvY2FsdGltZTovZXRjL2xvY2FsdGltZTpyb1xuICAgIHR0eTogdHJ1ZVxuICAgIHN0ZGluX29wZW46IHRydWVcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIERCX0NPTk5FQ1RJT05fVVJMOiBteXNxbDovLyR7TVlTUUxfVVNFUn06JHtNWVNRTF9QQVNTV09SRH1AdGlja2V0cy1wb3N0Z3Jlcy8ke01ZU1FMX0RBVEFCQVNFfVxuICAgICAgRElTQ09SRF9TRUNSRVQ6ICR7RElTQ09SRF9TRUNSRVR9XG4gICAgICBESVNDT1JEX1RPS0VOOiAke0RJU0NPUkRfVE9LRU59XG4gICAgICBFTkNSWVBUSU9OX0tFWTogJHtFTkNSWVBUSU9OX0tFWX1cbiAgICAgIERCX1BST1ZJREVSOiBteXNxbFxuICAgICAgSFRUUF9FWFRFUk5BTDogaHR0cHM6Ly8ke1RJQ0tFVFNfSE9TVH1cbiAgICAgIEhUVFBfSE9TVDogMC4wLjAuMFxuICAgICAgSFRUUF9QT1JUOiA4MTY5XG4gICAgICBIVFRQX1RSVVNUX1BST1hZOiBcInRydWVcIlxuICAgICAgUFVCTElDX0JPVDogXCJmYWxzZVwiXG4gICAgICBQVUJMSVNIX0NPTU1BTkRTOiBcInRydWVcIlxuICAgICAgU1VQRVI6ICR7U1VQRVJfVVNFUlN9XG5cbnZvbHVtZXM6XG4gIHRpY2tldHMtbXlzcWwtZGF0YTpcbiAgdGlja2V0cy1hcHAtZGF0YTogIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbm15c3FsX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkfVwiXG5teXNxbF9yb290X3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkfVwiXG5teXNxbF91c2VyID0gXCJ0aWNrZXRzXCJcbm15c3FsX2RhdGFiYXNlID0gXCJ0aWNrZXRzXCJcbmVuY3J5cHRpb25fa2V5ID0gXCIke3Bhc3N3b3JkOjQ4fVwiXG5cbltjb25maWddXG5lbnYgPSBbXG4gIFwiVElDS0VUU19IT1NUPSR7bWFpbl9kb21haW59XCIsXG4gIFwiTVlTUUxfREFUQUJBU0U9JHtteXNxbF9kYXRhYmFzZX1cIixcbiAgXCJNWVNRTF9QQVNTV09SRD0ke215c3FsX3Bhc3N3b3JkfVwiLFxuICBcIk1ZU1FMX1JPT1RfUEFTU1dPUkQ9JHtteXNxbF9yb290X3Bhc3N3b3JkfVwiLFxuICBcIk1ZU1FMX1VTRVI9JHtteXNxbF91c2VyfVwiLFxuICBcIkVOQ1JZUFRJT05fS0VZPSR7ZW5jcnlwdGlvbl9rZXl9XCIsXG4gIFwiIyBGb2xsb3cgdGhlIGd1aWRlIGF0OiBodHRwczovL2Rpc2NvcmR0aWNrZXRzLmFwcC9zZWxmLWhvc3RpbmcvaW5zdGFsbGF0aW9uL2RvY2tlci8jY3JlYXRpbmctdGhlLWRpc2NvcmQtYXBwbGljYXRpb25cIixcbiAgXCJESVNDT1JEX1NFQ1JFVD1cIixcbiAgXCJESVNDT1JEX1RPS0VOPVwiLFxuICBcIlNVUEVSX1VTRVJTPVlPVVJfRElTQ09SRF9VU0VSX0lEXCIsXG5dXG5tb3VudHMgPSBbXVxuXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJ0aWNrZXRzLWFwcFwiXG5wb3J0ID0gOF8xNjlcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcbiIKfQ==
```

## Links

`discord`,`tickets`,`support`

---

Version:`4.0.21`

DirectusDirectus is an open source headless CMS that provides an API-first solution for building custom backends.

DiscourseDiscourse is a modern forum software for your community. Use it as a mailing list, discussion forum, or long-form chat room.

### On this page

ConfigurationBase64LinksTags