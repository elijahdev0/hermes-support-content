---
title: "Chibisafe | Dokploy"
source: "https://docs.dokploy.com/docs/templates/chibisafe"
category: dokploy-docs
created: "2026-06-25T17:21:43.962Z"
---

Chibisafe | Dokploy

# Chibisafe

Copy as Markdown

A beautiful and performant vault to save all your files in the cloud.

## Configuration

docker-compose.ymltemplate.toml

```
# https://chibisafe.app/docs/intro
#
# Default Credentials
#   USERNAME: admin
#   PASSWORD: admin
services:
  chibisafe:
    image: chibisafe/chibisafe:latest
    networks:
      - chibinet
    environment:
      - BASE_API_URL=http://chibisafe_server:8000
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "wget", "--spider", "--quiet", "http://127.0.0.1:8001"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 10s

  chibisafe_server:
    image: chibisafe/chibisafe-server:latest
    networks:
      - chibinet
    volumes:
      - database:/app/database:rw
      - uploads:/app/uploads:rw
      - logs:/app/logs:rw
    restart: unless-stopped
    healthcheck:
      test:
        [
          "CMD",
          "wget",
          "--spider",
          "--quiet",
          "http://127.0.0.1:8000/api/health",
        ]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 10s

  caddy:
    image: caddy:2-alpine
    networks:
      - chibinet
    volumes:
      - ../files/Caddyfile:/etc/caddy/Caddyfile:ro
      - uploads:/app/uploads:ro
    environment:
      - BASE_URL=":80"
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "wget", "--spider", "--quiet", "http://127.0.0.1:80"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 10s

volumes:
  database:
  uploads:
  logs:

networks:
  chibinet:
    driver: bridge
    internal: true
```

```
[variables]
main_domain = "${domain}"

[[config.domains]]
serviceName = "caddy"
port = 80
host = "${main_domain}"

[[config.mounts]]
filePath = "./Caddyfile"
content = """
# chibisafe/Caddyfile
# https://chibisafe.app/docs/installation/running-with-docker
{$BASE_URL} {
	route {
		file_server * {
				root /app/uploads
				pass_thru
		}

		@api path /api/*
		reverse_proxy @api http://chibisafe_server:8000 {
				header_up Host {http.reverse_proxy.upstream.hostport}
				header_up X-Real-IP {http.request.header.X-Real-IP}
		}

		@docs path /docs*
		reverse_proxy @docs http://chibisafe_server:8000 {
				header_up Host {http.reverse_proxy.upstream.hostport}
				header_up X-Real-IP {http.request.header.X-Real-IP}
		}

		reverse_proxy http://chibisafe:8001 {
				header_up Host {http.reverse_proxy.upstream.hostport}
				header_up X-Real-IP {http.request.header.X-Real-IP}
		}
	}
}
"""
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogIiMgaHR0cHM6Ly9jaGliaXNhZmUuYXBwL2RvY3MvaW50cm9cbiNcbiMgRGVmYXVsdCBDcmVkZW50aWFsc1xuIyAgIFVTRVJOQU1FOiBhZG1pblxuIyAgIFBBU1NXT1JEOiBhZG1pblxuc2VydmljZXM6XG4gIGNoaWJpc2FmZTpcbiAgICBpbWFnZTogY2hpYmlzYWZlL2NoaWJpc2FmZTpsYXRlc3RcbiAgICBuZXR3b3JrczpcbiAgICAgIC0gY2hpYmluZXRcbiAgICBlbnZpcm9ubWVudDpcbiAgICAgIC0gQkFTRV9BUElfVVJMPWh0dHA6Ly9jaGliaXNhZmVfc2VydmVyOjgwMDBcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDogW1wiQ01EXCIsIFwid2dldFwiLCBcIi0tc3BpZGVyXCIsIFwiLS1xdWlldFwiLCBcImh0dHA6Ly8xMjcuMC4wLjE6ODAwMVwiXVxuICAgICAgaW50ZXJ2YWw6IDMwc1xuICAgICAgdGltZW91dDogMTBzXG4gICAgICByZXRyaWVzOiAzXG4gICAgICBzdGFydF9wZXJpb2Q6IDEwc1xuXG4gIGNoaWJpc2FmZV9zZXJ2ZXI6XG4gICAgaW1hZ2U6IGNoaWJpc2FmZS9jaGliaXNhZmUtc2VydmVyOmxhdGVzdFxuICAgIG5ldHdvcmtzOlxuICAgICAgLSBjaGliaW5ldFxuICAgIHZvbHVtZXM6XG4gICAgICAtIGRhdGFiYXNlOi9hcHAvZGF0YWJhc2U6cndcbiAgICAgIC0gdXBsb2FkczovYXBwL3VwbG9hZHM6cndcbiAgICAgIC0gbG9nczovYXBwL2xvZ3M6cndcbiAgICByZXN0YXJ0OiB1bmxlc3Mtc3RvcHBlZFxuICAgIGhlYWx0aGNoZWNrOlxuICAgICAgdGVzdDpcbiAgICAgICAgW1xuICAgICAgICAgIFwiQ01EXCIsXG4gICAgICAgICAgXCJ3Z2V0XCIsXG4gICAgICAgICAgXCItLXNwaWRlclwiLFxuICAgICAgICAgIFwiLS1xdWlldFwiLFxuICAgICAgICAgIFwiaHR0cDovLzEyNy4wLjAuMTo4MDAwL2FwaS9oZWFsdGhcIixcbiAgICAgICAgXVxuICAgICAgaW50ZXJ2YWw6IDMwc1xuICAgICAgdGltZW91dDogMTBzXG4gICAgICByZXRyaWVzOiAzXG4gICAgICBzdGFydF9wZXJpb2Q6IDEwc1xuXG4gIGNhZGR5OlxuICAgIGltYWdlOiBjYWRkeToyLWFscGluZVxuICAgIG5ldHdvcmtzOlxuICAgICAgLSBjaGliaW5ldFxuICAgIHZvbHVtZXM6XG4gICAgICAtIC4uL2ZpbGVzL0NhZGR5ZmlsZTovZXRjL2NhZGR5L0NhZGR5ZmlsZTpyb1xuICAgICAgLSB1cGxvYWRzOi9hcHAvdXBsb2Fkczpyb1xuICAgIGVudmlyb25tZW50OlxuICAgICAgLSBCQVNFX1VSTD1cIjo4MFwiXG4gICAgcmVzdGFydDogdW5sZXNzLXN0b3BwZWRcbiAgICBoZWFsdGhjaGVjazpcbiAgICAgIHRlc3Q6IFtcIkNNRFwiLCBcIndnZXRcIiwgXCItLXNwaWRlclwiLCBcIi0tcXVpZXRcIiwgXCJodHRwOi8vMTI3LjAuMC4xOjgwXCJdXG4gICAgICBpbnRlcnZhbDogMzBzXG4gICAgICB0aW1lb3V0OiAxMHNcbiAgICAgIHJldHJpZXM6IDNcbiAgICAgIHN0YXJ0X3BlcmlvZDogMTBzXG5cbnZvbHVtZXM6XG4gIGRhdGFiYXNlOlxuICB1cGxvYWRzOlxuICBsb2dzOlxuXG5uZXR3b3JrczpcbiAgY2hpYmluZXQ6XG4gICAgZHJpdmVyOiBicmlkZ2VcbiAgICBpbnRlcm5hbDogdHJ1ZVxuIiwKICAiY29uZmlnIjogIlt2YXJpYWJsZXNdXG5tYWluX2RvbWFpbiA9IFwiJHtkb21haW59XCJcblxuW1tjb25maWcuZG9tYWluc11dXG5zZXJ2aWNlTmFtZSA9IFwiY2FkZHlcIlxucG9ydCA9IDgwXG5ob3N0ID0gXCIke21haW5fZG9tYWlufVwiXG5cblxuW1tjb25maWcubW91bnRzXV1cbmZpbGVQYXRoID0gXCIuL0NhZGR5ZmlsZVwiXG5jb250ZW50ID0gXCJcIlwiXG4jIGNoaWJpc2FmZS9DYWRkeWZpbGVcbiMgaHR0cHM6Ly9jaGliaXNhZmUuYXBwL2RvY3MvaW5zdGFsbGF0aW9uL3J1bm5pbmctd2l0aC1kb2NrZXJcbnskQkFTRV9VUkx9IHtcblx0cm91dGUge1xuXHRcdGZpbGVfc2VydmVyICoge1xuXHRcdFx0XHRyb290IC9hcHAvdXBsb2Fkc1xuXHRcdFx0XHRwYXNzX3RocnVcblx0XHR9XG5cblx0XHRAYXBpIHBhdGggL2FwaS8qXG5cdFx0cmV2ZXJzZV9wcm94eSBAYXBpIGh0dHA6Ly9jaGliaXNhZmVfc2VydmVyOjgwMDAge1xuXHRcdFx0XHRoZWFkZXJfdXAgSG9zdCB7aHR0cC5yZXZlcnNlX3Byb3h5LnVwc3RyZWFtLmhvc3Rwb3J0fVxuXHRcdFx0XHRoZWFkZXJfdXAgWC1SZWFsLUlQIHtodHRwLnJlcXVlc3QuaGVhZGVyLlgtUmVhbC1JUH1cblx0XHR9XG5cblx0XHRAZG9jcyBwYXRoIC9kb2NzKlxuXHRcdHJldmVyc2VfcHJveHkgQGRvY3MgaHR0cDovL2NoaWJpc2FmZV9zZXJ2ZXI6ODAwMCB7XG5cdFx0XHRcdGhlYWRlcl91cCBIb3N0IHtodHRwLnJldmVyc2VfcHJveHkudXBzdHJlYW0uaG9zdHBvcnR9XG5cdFx0XHRcdGhlYWRlcl91cCBYLVJlYWwtSVAge2h0dHAucmVxdWVzdC5oZWFkZXIuWC1SZWFsLUlQfVxuXHRcdH1cblxuXHRcdHJldmVyc2VfcHJveHkgaHR0cDovL2NoaWJpc2FmZTo4MDAxIHtcblx0XHRcdFx0aGVhZGVyX3VwIEhvc3Qge2h0dHAucmV2ZXJzZV9wcm94eS51cHN0cmVhbS5ob3N0cG9ydH1cblx0XHRcdFx0aGVhZGVyX3VwIFgtUmVhbC1JUCB7aHR0cC5yZXF1ZXN0LmhlYWRlci5YLVJlYWwtSVB9XG5cdFx0fVxuXHR9XG59XG5cIlwiXCJcbiIKfQ==
```

## Links

`media system`,`storage`,`file-sharing`

---

Version:`latest`

CheveretoChevereto is a powerful, self-hosted image and video hosting platform designed for individuals, communities, and businesses. It allows users to upload, organize, and share media effortlessly.

Chief-OnboardingChief-Onboarding is a comprehensive, self-hosted onboarding and employee management platform designed for businesses to streamline their onboarding processes.

### On this page

ConfigurationBase64LinksTags