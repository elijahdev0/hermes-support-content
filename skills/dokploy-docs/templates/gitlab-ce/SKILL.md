---
title: "GitLab CE | Dokploy"
source: "https://docs.dokploy.com/docs/templates/gitlab-ce"
category: dokploy-docs
created: "2026-06-25T17:21:48.522Z"
---

GitLab CE | Dokploy

# GitLab CE

Copy as Markdown

GitLab Community Edition is a free and open source platform for managing Git repositories, CI/CD pipelines, and project management.

## Configuration

docker-compose.ymltemplate.toml

```
services:
  gitlab:
    image: gitlab/gitlab-ce:latest
    restart: unless-stopped
    hostname: gitlab.example.com
    environment:
      GITLAB_OMNIBUS_CONFIG: |
        external_url 'http://${GITLAB_HOST}'
        gitlab_rails['gitlab_ssh_host'] = '${GITLAB_HOST}'
        gitlab_rails['gitlab_shell_ssh_port'] = 2224
        gitlab_rails['db_adapter'] = 'postgresql'
        gitlab_rails['db_host'] = 'postgresql'
        gitlab_rails['db_port'] = '5432'
        gitlab_rails['db_database'] = '${POSTGRES_DB}'
        gitlab_rails['db_username'] = '${POSTGRES_USER}'
        gitlab_rails['db_password'] = '${POSTGRES_PASSWORD}'
        # Redis config for external TCP connection
        gitlab_rails['redis_url'] = 'redis://redis:6379/0'
        gitlab_rails['redis_host'] = 'redis'
        gitlab_rails['redis_port'] = 6379
        gitlab_rails['redis_socket'] = nil
        gitlab_rails['gitlab_email_enabled'] = false
        gitlab_rails['gitlab_default_can_create_group'] = true
        gitlab_rails['gitlab_username_changing_enabled'] = false
        unicorn['worker_processes'] = 2
        unicorn['worker_timeout'] = 60
        postgresql['enable'] = false
        redis['enable'] = false
        nginx['enable'] = true
        nginx['listen_port'] = 80
        nginx['listen_https'] = false
        prometheus_monitoring['enable'] = false
    ports:
      - "80"
      - "2224"
    volumes:
      - gitlab_config:/etc/gitlab
      - gitlab_logs:/var/log/gitlab
      - gitlab_data:/var/opt/gitlab
    depends_on:
      - postgresql
      - redis

  postgresql:
    image: postgres:16-alpine
    restart: unless-stopped
    environment:
      POSTGRES_DB: ${POSTGRES_DB}
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    volumes:
      - postgresql_data:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine
    restart: unless-stopped
    volumes:
      - redis_data:/data

volumes:
  gitlab_config:
  gitlab_logs:
  gitlab_data:
  postgresql_data:
  redis_data:
```

```
[variables]
main_domain = "${domain}"
postgres_db = "gitlab"
postgres_user = "gitlab"
postgres_password = "${password:32}"

[config]
env = [
  "GITLAB_HOST=${main_domain}",
  "POSTGRES_DB=${postgres_db}",
  "POSTGRES_USER=${postgres_user}",
  "POSTGRES_PASSWORD=${postgres_password}",
]

[[config.domains]]
serviceName = "gitlab"
port = 80
host = "${main_domain}"
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogInNlcnZpY2VzOlxuICBnaXRsYWI6XG4gICAgaW1hZ2U6IGdpdGxhYi9naXRsYWItY2U6bGF0ZXN0XG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBob3N0bmFtZTogZ2l0bGFiLmV4YW1wbGUuY29tXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICBHSVRMQUJfT01OSUJVU19DT05GSUc6IHxcbiAgICAgICAgZXh0ZXJuYWxfdXJsICdodHRwOi8vJHtHSVRMQUJfSE9TVH0nXG4gICAgICAgIGdpdGxhYl9yYWlsc1snZ2l0bGFiX3NzaF9ob3N0J10gPSAnJHtHSVRMQUJfSE9TVH0nXG4gICAgICAgIGdpdGxhYl9yYWlsc1snZ2l0bGFiX3NoZWxsX3NzaF9wb3J0J10gPSAyMjI0XG4gICAgICAgIGdpdGxhYl9yYWlsc1snZGJfYWRhcHRlciddID0gJ3Bvc3RncmVzcWwnXG4gICAgICAgIGdpdGxhYl9yYWlsc1snZGJfaG9zdCddID0gJ3Bvc3RncmVzcWwnXG4gICAgICAgIGdpdGxhYl9yYWlsc1snZGJfcG9ydCddID0gJzU0MzInXG4gICAgICAgIGdpdGxhYl9yYWlsc1snZGJfZGF0YWJhc2UnXSA9ICcke1BPU1RHUkVTX0RCfSdcbiAgICAgICAgZ2l0bGFiX3JhaWxzWydkYl91c2VybmFtZSddID0gJyR7UE9TVEdSRVNfVVNFUn0nXG4gICAgICAgIGdpdGxhYl9yYWlsc1snZGJfcGFzc3dvcmQnXSA9ICcke1BPU1RHUkVTX1BBU1NXT1JEfSdcbiAgICAgICAgIyBSZWRpcyBjb25maWcgZm9yIGV4dGVybmFsIFRDUCBjb25uZWN0aW9uXG4gICAgICAgIGdpdGxhYl9yYWlsc1sncmVkaXNfdXJsJ10gPSAncmVkaXM6Ly9yZWRpczo2Mzc5LzAnXG4gICAgICAgIGdpdGxhYl9yYWlsc1sncmVkaXNfaG9zdCddID0gJ3JlZGlzJ1xuICAgICAgICBnaXRsYWJfcmFpbHNbJ3JlZGlzX3BvcnQnXSA9IDYzNzlcbiAgICAgICAgZ2l0bGFiX3JhaWxzWydyZWRpc19zb2NrZXQnXSA9IG5pbFxuICAgICAgICBnaXRsYWJfcmFpbHNbJ2dpdGxhYl9lbWFpbF9lbmFibGVkJ10gPSBmYWxzZVxuICAgICAgICBnaXRsYWJfcmFpbHNbJ2dpdGxhYl9kZWZhdWx0X2Nhbl9jcmVhdGVfZ3JvdXAnXSA9IHRydWVcbiAgICAgICAgZ2l0bGFiX3JhaWxzWydnaXRsYWJfdXNlcm5hbWVfY2hhbmdpbmdfZW5hYmxlZCddID0gZmFsc2VcbiAgICAgICAgdW5pY29yblsnd29ya2VyX3Byb2Nlc3NlcyddID0gMlxuICAgICAgICB1bmljb3JuWyd3b3JrZXJfdGltZW91dCddID0gNjBcbiAgICAgICAgcG9zdGdyZXNxbFsnZW5hYmxlJ10gPSBmYWxzZVxuICAgICAgICByZWRpc1snZW5hYmxlJ10gPSBmYWxzZVxuICAgICAgICBuZ2lueFsnZW5hYmxlJ10gPSB0cnVlXG4gICAgICAgIG5naW54WydsaXN0ZW5fcG9ydCddID0gODBcbiAgICAgICAgbmdpbnhbJ2xpc3Rlbl9odHRwcyddID0gZmFsc2VcbiAgICAgICAgcHJvbWV0aGV1c19tb25pdG9yaW5nWydlbmFibGUnXSA9IGZhbHNlXG4gICAgcG9ydHM6XG4gICAgICAtIFwiODBcIlxuICAgICAgLSBcIjIyMjRcIlxuICAgIHZvbHVtZXM6XG4gICAgICAtIGdpdGxhYl9jb25maWc6L2V0Yy9naXRsYWJcbiAgICAgIC0gZ2l0bGFiX2xvZ3M6L3Zhci9sb2cvZ2l0bGFiXG4gICAgICAtIGdpdGxhYl9kYXRhOi92YXIvb3B0L2dpdGxhYlxuICAgIGRlcGVuZHNfb246XG4gICAgICAtIHBvc3RncmVzcWxcbiAgICAgIC0gcmVkaXNcblxuICBwb3N0Z3Jlc3FsOlxuICAgIGltYWdlOiBwb3N0Z3JlczoxNi1hbHBpbmVcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGVudmlyb25tZW50OlxuICAgICAgUE9TVEdSRVNfREI6ICR7UE9TVEdSRVNfREJ9XG4gICAgICBQT1NUR1JFU19VU0VSOiAke1BPU1RHUkVTX1VTRVJ9XG4gICAgICBQT1NUR1JFU19QQVNTV09SRDogJHtQT1NUR1JFU19QQVNTV09SRH1cbiAgICB2b2x1bWVzOlxuICAgICAgLSBwb3N0Z3Jlc3FsX2RhdGE6L3Zhci9saWIvcG9zdGdyZXNxbC9kYXRhXG5cbiAgcmVkaXM6XG4gICAgaW1hZ2U6IHJlZGlzOjctYWxwaW5lXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICB2b2x1bWVzOlxuICAgICAgLSByZWRpc19kYXRhOi9kYXRhXG5cbnZvbHVtZXM6XG4gIGdpdGxhYl9jb25maWc6XG4gIGdpdGxhYl9sb2dzOlxuICBnaXRsYWJfZGF0YTpcbiAgcG9zdGdyZXNxbF9kYXRhOlxuICByZWRpc19kYXRhOlxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcbnBvc3RncmVzX2RiID0gXCJnaXRsYWJcIlxucG9zdGdyZXNfdXNlciA9IFwiZ2l0bGFiXCJcbnBvc3RncmVzX3Bhc3N3b3JkID0gXCIke3Bhc3N3b3JkOjMyfVwiXG5cbltjb25maWddXG5lbnYgPSBbXG4gIFwiR0lUTEFCX0hPU1Q9JHttYWluX2RvbWFpbn1cIixcbiAgXCJQT1NUR1JFU19EQj0ke3Bvc3RncmVzX2RifVwiLFxuICBcIlBPU1RHUkVTX1VTRVI9JHtwb3N0Z3Jlc191c2VyfVwiLFxuICBcIlBPU1RHUkVTX1BBU1NXT1JEPSR7cG9zdGdyZXNfcGFzc3dvcmR9XCIsXG5dXG5cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcImdpdGxhYlwiXG5wb3J0ID0gODBcbmhvc3QgPSBcIiR7bWFpbl9kb21haW59XCJcbiIKfQ==
```

## Links

`git`,`ci-cd`,`version-control`,`project-management`

---

Version:`latest`

GitingestGitingest is an application that supports Prometheus metrics, Sentry integration, and S3-backed storage.

GlanceA self-hosted dashboard that puts all your feeds in one place. Features RSS feeds, weather, bookmarks, site monitoring, and more in a minimal, fast interface.

### On this page

ConfigurationBase64LinksTags