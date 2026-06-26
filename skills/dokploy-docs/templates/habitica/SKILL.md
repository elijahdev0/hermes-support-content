---
title: "Habitica | Dokploy"
source: "https://docs.dokploy.com/docs/templates/habitica"
category: dokploy-docs
created: "2026-06-25T17:21:49.750Z"
---

Habitica | Dokploy

# Habitica

Habitica is a free habit and productivity app that treats your real life like a game. With in-game rewards and punishments to motivate you and a strong social network to inspire you, Habitica can help you achieve your goals to become healthy and hard-working.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  server:
    image: docker.io/awinterstein/habitica-server:latest
    restart: unless-stopped
    depends_on:
      mongo:
        condition: service_healthy
    environment:
      NODE_DB_URI: "mongodb://${MONGO_HABITICA_USER}:${MONGO_HABITICA_PASSWORD}@mongo/habitica?authSource=habitica"
      INVITE_ONLY: "${INVITE_ONLY}"
      EMAIL_SERVER_URL: "${EMAIL_SERVER_URL}"
      EMAIL_SERVER_PORT: "${EMAIL_SERVER_PORT}"
      EMAIL_SERVER_AUTH_USER: "${EMAIL_SERVER_AUTH_USER}"
      EMAIL_SERVER_AUTH_PASSWORD: "${EMAIL_SERVER_AUTH_PASSWORD}"
      ADMIN_EMAIL: "${ADMIN_EMAIL}"

  client:
    image: docker.io/awinterstein/habitica-client:latest
    restart: unless-stopped
    depends_on:
      - server
    ports:
      - "80"

  mongo:
    image: docker.io/mongo:latest
    restart: unless-stopped
    command: >
      bash -c "
        echo \"${MONGO_KEYFILE_CONTENT}\" > /etc/mongo-keyfile &&
        chown 999:999 /etc/mongo-keyfile &&
        chmod 400 /etc/mongo-keyfile &&
        exec docker-entrypoint.sh mongod --replSet rs --bind_ip_all --port 27017 --keyFile /etc/mongo-keyfile
      "
    environment:
      MONGO_INITDB_ROOT_USERNAME: ${MONGO_ADMIN_USER}
      MONGO_INITDB_ROOT_PASSWORD: ${MONGO_ADMIN_PASSWORD}
      MONGO_KEYFILE_CONTENT: ${MONGO_KEYFILE_CONTENT}
      MONGO_HABITICA_USER: ${MONGO_HABITICA_USER}
      MONGO_HABITICA_PASSWORD: ${MONGO_HABITICA_PASSWORD}
    # ---------------------------------------------------------
    # SMART HEALTHCHECK: Auto-fixes Hostname Mismatches for replicaSet
    # ---------------------------------------------------------
    healthcheck:
      test: |
        mongosh --port 27017 --quiet -u "${MONGO_ADMIN_USER}" -p "${MONGO_ADMIN_PASSWORD}" --authenticationDatabase admin --eval "
          try {
            // 1. Hostname Fix
            const config = rs.conf();
            const currentHost = require('os').hostname() + ':27017';
            if (config.members[0].host !== currentHost) {
              config.members[0].host = currentHost;
              rs.reconfig(config, { force: true });
            }

            // 2. User Creation Logic
            const targetDb = db.getSiblingDB('habitica');
            const hUser = process.env.MONGO_HABITICA_USER;
            const hPass = process.env.MONGO_HABITICA_PASSWORD;

            // We can only check/create users if we are Primary
            if (rs.isMaster().ismaster) {
              if (!targetDb.getUser(hUser)) {
                print('Creating missing user ' + hUser + '...');
                targetDb.createUser({ user: hUser, pwd: hPass, roles: ['readWrite'] });
              }
              // SUCCESS: User exists and we are Primary
              quit(0);
            } else {
              // We are not Primary yet (still electing), so we cannot confirm user exists.
              // Fail the check so the dependent app waits.
              print('Waiting for Primary state...');
              quit(1);
            }
          } catch (err) {
            // If not initialized, initiate and FAIL this check so we wait for the next cycle
            try {
              rs.initiate({ _id: 'rs', members: [{ _id: 0, host: require('os').hostname() + ':27017' }] });
            } catch (e) {}
            quit(1);
          }
        "
      interval: 5s
      timeout: 10s
      retries: 20
    volumes:
      - habitica-mongo-data:/data/db

volumes:
  habitica-mongo-data: {}
```

```
[variables]
main_domain = "${domain}"
mail_password = "${password:32}"
mongo_key = "${base64:756}"
mongo_admin_password = "${password}"
mongo_habitica_password = "${password}"

[config]
[[config.domains]]
serviceName = "client"
port = 80
host = "habitica.${main_domain}"

[config.env]
BASE_URL = "https://habitica.${main_domain}"
INVITE_ONLY = "false"
EMAIL_SERVER_URL = "mail.example.com"
EMAIL_SERVER_PORT = "587"
EMAIL_SERVER_AUTH_USER = "mail_user"
EMAIL_SERVER_AUTH_PASSWORD = "${mail_password}"
MONGO_KEYFILE_CONTENT = "${mongo_key}"
MONGO_ADMIN_USER = "admin"
MONGO_ADMIN_PASSWORD = "${mongo_admin_password}"
MONGO_HABITICA_USER = "habitica"
MONGO_HABITICA_PASSWORD = "${mongo_habitica_password}"
ADMIN_EMAIL = "no-reply@${main_domain}"

[[config.mounts]]
serviceName = "mongo"
type = "volume"
source = "habitica-mongo-data"
target = "/data/db"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBzZXJ2ZXI6XG4gICAgaW1hZ2U6IGRvY2tlci5pby9hd2ludGVyc3RlaW4vaGFiaXRpY2Etc2VydmVyOmxhdGVzdFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIG1vbmdvOlxuICAgICAgICBjb25kaXRpb246IHNlcnZpY2VfaGVhbHRoeVxuICAgIGVudmlyb25tZW50OlxuICAgICAgTk9ERV9EQl9VUkk6IFwibW9uZ29kYjovLyR7TU9OR09fSEFCSVRJQ0FfVVNFUn06JHtNT05HT19IQUJJVElDQV9QQVNTV09SRH1AbW9uZ28vaGFiaXRpY2E/YXV0aFNvdXJjZT1oYWJpdGljYVwiXG4gICAgICBJTlZJVEVfT05MWTogXCIke0lOVklURV9PTkxZfVwiXG4gICAgICBFTUFJTF9TRVJWRVJfVVJMOiBcIiR7RU1BSUxfU0VSVkVSX1VSTH1cIlxuICAgICAgRU1BSUxfU0VSVkVSX1BPUlQ6IFwiJHtFTUFJTF9TRVJWRVJfUE9SVH1cIlxuICAgICAgRU1BSUxfU0VSVkVSX0FVVEhfVVNFUjogXCIke0VNQUlMX1NFUlZFUl9BVVRIX1VTRVJ9XCJcbiAgICAgIEVNQUlMX1NFUlZFUl9BVVRIX1BBU1NXT1JEOiBcIiR7RU1BSUxfU0VSVkVSX0FVVEhfUEFTU1dPUkR9XCJcbiAgICAgIEFETUlOX0VNQUlMOiBcIiR7QURNSU5fRU1BSUx9XCJcblxuICBjbGllbnQ6XG4gICAgaW1hZ2U6IGRvY2tlci5pby9hd2ludGVyc3RlaW4vaGFiaXRpY2EtY2xpZW50OmxhdGVzdFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG4gICAgZGVwZW5kc19vbjpcbiAgICAgIC0gc2VydmVyXG4gICAgcG9ydHM6XG4gICAgICAtIFwiODBcIlxuXG4gIG1vbmdvOlxuICAgIGltYWdlOiBkb2NrZXIuaW8vbW9uZ286bGF0ZXN0XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBjb21tYW5kOiA+XG4gICAgICBiYXNoIC1jIFwiXG4gICAgICAgIGVjaG8gXFxcIiR7TU9OR09fS0VZRklMRV9DT05URU5UfVxcXCIgPiAvZXRjL21vbmdvLWtleWZpbGUgJiZcbiAgICAgICAgY2hvd24gOTk5Ojk5OSAvZXRjL21vbmdvLWtleWZpbGUgJiZcbiAgICAgICAgY2htb2QgNDAwIC9ldGMvbW9uZ28ta2V5ZmlsZSAmJlxuICAgICAgICBleGVjIGRvY2tlci1lbnRyeXBvaW50LnNoIG1vbmdvZCAtLXJlcGxTZXQgcnMgLS1iaW5kX2lwX2FsbCAtLXBvcnQgMjcwMTcgLS1rZXlGaWxlIC9ldGMvbW9uZ28ta2V5ZmlsZVxuICAgICAgXCJcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIE1PTkdPX0lOSVREQl9ST09UX1VTRVJOQU1FOiAke01PTkdPX0FETUlOX1VTRVJ9XG4gICAgICBNT05HT19JTklUREJfUk9PVF9QQVNTV09SRDogJHtNT05HT19BRE1JTl9QQVNTV09SRH1cbiAgICAgIE1PTkdPX0tFWUZJTEVfQ09OVEVOVDogJHtNT05HT19LRVlGSUxFX0NPTlRFTlR9XG4gICAgICBNT05HT19IQUJJVElDQV9VU0VSOiAke01PTkdPX0hBQklUSUNBX1VTRVJ9XG4gICAgICBNT05HT19IQUJJVElDQV9QQVNTV09SRDogJHtNT05HT19IQUJJVElDQV9QQVNTV09SRH1cbiAgICAjIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuICAgICMgU01BUlQgSEVBTFRIQ0hFQ0s6IEF1dG8tZml4ZXMgSG9zdG5hbWUgTWlzbWF0Y2hlcyBmb3IgcmVwbGljYVNldFxuICAgICMgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG4gICAgaGVhbHRoY2hlY2s6XG4gICAgICB0ZXN0OiB8XG4gICAgICAgIG1vbmdvc2ggLS1wb3J0IDI3MDE3IC0tcXVpZXQgLXUgXCIke01PTkdPX0FETUlOX1VTRVJ9XCIgLXAgXCIke01PTkdPX0FETUlOX1BBU1NXT1JEfVwiIC0tYXV0aGVudGljYXRpb25EYXRhYmFzZSBhZG1pbiAtLWV2YWwgXCJcbiAgICAgICAgICB0cnkge1xuICAgICAgICAgICAgLy8gMS4gSG9zdG5hbWUgRml4XG4gICAgICAgICAgICBjb25zdCBjb25maWcgPSBycy5jb25mKCk7XG4gICAgICAgICAgICBjb25zdCBjdXJyZW50SG9zdCA9IHJlcXVpcmUoJ29zJykuaG9zdG5hbWUoKSArICc6MjcwMTcnO1xuICAgICAgICAgICAgaWYgKGNvbmZpZy5tZW1iZXJzWzBdLmhvc3QgIT09IGN1cnJlbnRIb3N0KSB7XG4gICAgICAgICAgICAgIGNvbmZpZy5tZW1iZXJzWzBdLmhvc3QgPSBjdXJyZW50SG9zdDtcbiAgICAgICAgICAgICAgcnMucmVjb25maWcoY29uZmlnLCB7IGZvcmNlOiB0cnVlIH0pO1xuICAgICAgICAgICAgfVxuXG4gICAgICAgICAgICAvLyAyLiBVc2VyIENyZWF0aW9uIExvZ2ljXG4gICAgICAgICAgICBjb25zdCB0YXJnZXREYiA9IGRiLmdldFNpYmxpbmdEQignaGFiaXRpY2EnKTtcbiAgICAgICAgICAgIGNvbnN0IGhVc2VyID0gcHJvY2Vzcy5lbnYuTU9OR09fSEFCSVRJQ0FfVVNFUjtcbiAgICAgICAgICAgIGNvbnN0IGhQYXNzID0gcHJvY2Vzcy5lbnYuTU9OR09fSEFCSVRJQ0FfUEFTU1dPUkQ7XG5cbiAgICAgICAgICAgIC8vIFdlIGNhbiBvbmx5IGNoZWNrL2NyZWF0ZSB1c2VycyBpZiB3ZSBhcmUgUHJpbWFyeVxuICAgICAgICAgICAgaWYgKHJzLmlzTWFzdGVyKCkuaXNtYXN0ZXIpIHtcbiAgICAgICAgICAgICAgaWYgKCF0YXJnZXREYi5nZXRVc2VyKGhVc2VyKSkge1xuICAgICAgICAgICAgICAgIHByaW50KCdDcmVhdGluZyBtaXNzaW5nIHVzZXIgJyArIGhVc2VyICsgJy4uLicpO1xuICAgICAgICAgICAgICAgIHRhcmdldERiLmNyZWF0ZVVzZXIoeyB1c2VyOiBoVXNlciwgcHdkOiBoUGFzcywgcm9sZXM6IFsncmVhZFdyaXRlJ10gfSk7XG4gICAgICAgICAgICAgIH1cbiAgICAgICAgICAgICAgLy8gU1VDQ0VTUzogVXNlciBleGlzdHMgYW5kIHdlIGFyZSBQcmltYXJ5XG4gICAgICAgICAgICAgIHF1aXQoMCk7XG4gICAgICAgICAgICB9IGVsc2Uge1xuICAgICAgICAgICAgICAvLyBXZSBhcmUgbm90IFByaW1hcnkgeWV0IChzdGlsbCBlbGVjdGluZyksIHNvIHdlIGNhbm5vdCBjb25maXJtIHVzZXIgZXhpc3RzLlxuICAgICAgICAgICAgICAvLyBGYWlsIHRoZSBjaGVjayBzbyB0aGUgZGVwZW5kZW50IGFwcCB3YWl0cy5cbiAgICAgICAgICAgICAgcHJpbnQoJ1dhaXRpbmcgZm9yIFByaW1hcnkgc3RhdGUuLi4nKTtcbiAgICAgICAgICAgICAgcXVpdCgxKTtcbiAgICAgICAgICAgIH1cbiAgICAgICAgICB9IGNhdGNoIChlcnIpIHtcbiAgICAgICAgICAgIC8vIElmIG5vdCBpbml0aWFsaXplZCwgaW5pdGlhdGUgYW5kIEZBSUwgdGhpcyBjaGVjayBzbyB3ZSB3YWl0IGZvciB0aGUgbmV4dCBjeWNsZVxuICAgICAgICAgICAgdHJ5IHsgXG4gICAgICAgICAgICAgIHJzLmluaXRpYXRlKHsgX2lkOiAncnMnLCBtZW1iZXJzOiBbeyBfaWQ6IDAsIGhvc3Q6IHJlcXVpcmUoJ29zJykuaG9zdG5hbWUoKSArICc6MjcwMTcnIH1dIH0pOyBcbiAgICAgICAgICAgIH0gY2F0Y2ggKGUpIHt9XG4gICAgICAgICAgICBxdWl0KDEpO1xuICAgICAgICAgIH1cbiAgICAgICAgXCJcbiAgICAgIGludGVydmFsOiA1c1xuICAgICAgdGltZW91dDogMTBzXG4gICAgICByZXRyaWVzOiAyMFxuICAgIHZvbHVtZXM6XG4gICAgICAtIGhhYml0aWNhLW1vbmdvLWRhdGE6L2RhdGEvZGJcblxudm9sdW1lczpcbiAgaGFiaXRpY2EtbW9uZ28tZGF0YToge31cbiIsCiAgImNvbmZpZyI6ICJbdmFyaWFibGVzXVxubWFpbl9kb21haW4gPSBcIiR7ZG9tYWlufVwiXG5tYWlsX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5tb25nb19rZXkgPSBcIiR7YmFzZTY0Ojc1Nn1cIlxubW9uZ29fYWRtaW5fcGFzc3dvcmQgPSBcIiR7cGFzc3dvcmR9XCJcbm1vbmdvX2hhYml0aWNhX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkfVwiXG5cbltjb25maWddXG5bW2NvbmZpZy5kb21haW5zXV1cbnNlcnZpY2VOYW1lID0gXCJjbGllbnRcIlxucG9ydCA9IDgwXG5ob3N0ID0gXCJoYWJpdGljYS4ke21haW5fZG9tYWlufVwiXG5cbltjb25maWcuZW52XVxuQkFTRV9VUkwgPSBcImh0dHBzOi8vaGFiaXRpY2EuJHttYWluX2RvbWFpbn1cIlxuSU5WSVRFX09OTFkgPSBcImZhbHNlXCJcbkVNQUlMX1NFUlZFUl9VUkwgPSBcIm1haWwuZXhhbXBsZS5jb21cIlxuRU1BSUxfU0VSVkVSX1BPUlQgPSBcIjU4N1wiXG5FTUFJTF9TRVJWRVJfQVVUSF9VU0VSID0gXCJtYWlsX3VzZXJcIlxuRU1BSUxfU0VSVkVSX0FVVEhfUEFTU1dPUkQgPSBcIiR7bWFpbF9wYXNzd29yZH1cIlxuTU9OR09fS0VZRklMRV9DT05URU5UID0gXCIke21vbmdvX2tleX1cIlxuTU9OR09fQURNSU5fVVNFUiA9IFwiYWRtaW5cIlxuTU9OR09fQURNSU5fUEFTU1dPUkQgPSBcIiR7bW9uZ29fYWRtaW5fcGFzc3dvcmR9XCJcbk1PTkdPX0hBQklUSUNBX1VTRVIgPSBcImhhYml0aWNhXCJcbk1PTkdPX0hBQklUSUNBX1BBU1NXT1JEID0gXCIke21vbmdvX2hhYml0aWNhX3Bhc3N3b3JkfVwiXG5BRE1JTl9FTUFJTCA9IFwibm8tcmVwbHlAJHttYWluX2RvbWFpbn1cIlxuXG5bW2NvbmZpZy5tb3VudHNdXVxuc2VydmljZU5hbWUgPSBcIm1vbmdvXCJcbnR5cGUgPSBcInZvbHVtZVwiXG5zb3VyY2UgPSBcImhhYml0aWNhLW1vbmdvLWRhdGFcIlxudGFyZ2V0ID0gXCIvZGF0YS9kYlwiXG4iCn0=
```

## Links

- Website
- Github
- Documentation

`productivity`,`gamification`,`habits`,`self-hosted`

---

Version:`latest`

GristGrist is an open-source spreadsheet and database alternative that combines the flexibility of spreadsheets with the power of databases.

HeyFormAllows anyone to create engaging conversational forms for surveys, questionnaires, quizzes, and polls. No coding skills required.

### On this page

ConfigurationBase64LinksTags

