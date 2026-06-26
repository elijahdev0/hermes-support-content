---
title: "Cloudflare Tunnels | Dokploy"
source: "https://docs.dokploy.com/docs/core/guides/cloudflare-tunnels"
category: dokploy-docs
created: "2026-06-25T17:21:36.901Z"
---

Cloudflare Tunnels | Dokploy

# Cloudflare Tunnels

Copy as Markdown

Learn how to use Cloudflare Tunnels to securely expose your Dokploy applications without opening ports on your server.

Cloudflare Tunnels provide a secure way to connect your applications to the internet without exposing ports on your server. This is particularly useful for home servers or networks where you can't easily configure port forwarding or want enhanced security.

## What are Cloudflare Tunnels?

Cloudflare Tunnels (formerly Argo Tunnels) create an encrypted tunnel between your origin server and Cloudflare's global network. Instead of opening ports 80 and 443 on your server, the tunnel establishes an outbound-only connection to Cloudflare, which then routes traffic to your applications.

### Benefits

- Enhanced Security: No need to open inbound ports on your firewall
- Simple Setup: Works behind NAT and restrictive firewalls
- DDoS Protection: Traffic is routed through Cloudflare's network
- Free Tier Available: Included with free Cloudflare accounts
- Wildcard Support: Route multiple subdomains through a single tunnel

## Prerequisites

Before setting up Cloudflare Tunnels with Dokploy, ensure you have:

- A domain managed by Cloudflare (free tier works)
- Dokploy installed and running
- Access to Cloudflare dashboard

When using Cloudflare Tunnels, you should disable Let's Encrypt in Dokploy and use HTTP instead of HTTPS for internal connections. Cloudflare handles SSL/TLS termination at their edge.

## Cloudflare Tunnel Setup

### Step 1: Create a Tunnel in Cloudflare

- Log in to your Cloudflare Dashboard
- Navigate to Zero Trust (or Access in older dashboards)
- Go to Networks → Connectors
- Click Create a tunnel
- Choose Cloudflared as the connector type
- Give your tunnel a name (e.g.,`dokploy-tunnel`)
- Copy the Tunnel Token that's generated (you'll need this later)

Keep your tunnel token secure! It provides access to route traffic to your server.

### Step 2: Configure SSL/TLS Settings

For Cloudflare Tunnels to work properly with Dokploy:

- In Cloudflare Dashboard, go to SSL/TLS
- Set the encryption mode to Full or Full (Strict)

Do not use "Flexible" mode as it may cause redirect loops with Traefik.

### Step 3: Create Cloudflare Service in Dokploy

1. Create a new application
2. Select Docker Provider and set the Image name as`cloudflare/cloudflared`
3. Go to the Environments tab and add the token you copied:`TUNNEL_TOKEN="TOKEN-YOU-COPIED"`
4. Go to the Advanced tab, in the Arguments field add 2 entries: first`tunnel`, second`run`, then click save
5. Deploy the application. You should see the container in healthy status in the logs section

### Step 4: Configuring Public Hostnames (Domains)

After deploying cloudflared, you need to configure which domains route through the tunnel.

#### Understanding Traefik Routing vs Direct Access

Dokploy uses Traefik as its reverse proxy to route traffic to your applications. When configuring Cloudflare Tunnels, you have two options:

Option 1: Route through Traefik (Recommended)

Benefits:

- Support for multiple applications with a single tunnel (wildcard domains)
- Leverage all Dokploy domain configurations (redirects, path rewrites, etc.)
- Traefik automatically routes based on the domain you configured in Dokploy
- Configure once, works for all apps

Option 2: Direct Container Access

Benefits:

- Simpler setup for single applications
- Slightly lower latency (one less hop)

#### For Applications (via Traefik)

Configure:

Service:

- Type: HTTP
- URL:`dokploy-traefik:80`

With this setup, Traefik will route the request to the correct application based on the domain you configured in Dokploy's domain settings.

Example:

To test this, let's create a minimal app:

1. Click Save
2. Create a simple application
3. Select Docker Provider and set the image name to`nginx`
4. Click on Deploy
5. Go to the Domains tab
6. Create a new domain (Important: make sure to use the same domain you created in Cloudflare dashboard under`Published application routes`)
7. Set the correct port where your application is running (nginx runs on port`80` by default)
8. Don't enable HTTPS toggle or select any certificate provider (this can cause conflicts with Cloudflare SSL)

#### For Direct Container Access

If you prefer to bypass Traefik and connect directly to a container:

Configure the public hostname with:

Service:

- Type: HTTP
- URL:`appName:port`(e.g.,`dokploy:3000`,`my-app:8080`)

Note: The app name in Dokploy is shown under the service name, usually formatted as`project-serviceName-hash`

When using direct access, you bypass Traefik completely. Domain configurations in Dokploy won't apply, and you'll need to configure each container separately in Cloudflare.

### For Wildcard Subdomains (Multiple Apps)

To support multiple applications/subdomains with a single tunnel configuration:

Note: You need to create a manual CNAME wildcard record in your Cloudflare DNS configuration.

Create a new record:

- Type: CNAME
- Name:`*`
- Content:`your-tunnel-id.cfargotunnel.com`(replace`your-tunnel-id` with the ID you copied)

Then, go to the configuration of your tunnel under Published application routes:

Add a public hostname with:

Service:

- Type: HTTP
- URL:`dokploy-traefik:80`

This allows all subdomains (`app1.example.com`,`app2.example.com`, etc.) to route through Traefik, which then directs traffic to the appropriate container based on your Dokploy domain configurations.

With wildcard routing, you only need ONE public hostname in Cloudflare Tunnel. Traefik handles routing to different apps based on the domain configured in Dokploy.

## Using Cloudflare Access (Zero Trust) with Dokploy

If you protect your Dokploy dashboard with Cloudflare Access (Zero Trust), there are a few extra steps required to make login work correctly.

### Why login hangs behind Cloudflare Access

When Cloudflare Access sits in front of Dokploy, the login request (`POST /api/auth/sign-in/email`) may appear to hang indefinitely even with valid credentials. Invalid credentials still return a`401` immediately, which makes it easy to miss this issue.

The root cause is that Better Auth (Dokploy's auth library) validates the`Origin` header of every request. When the request comes through Cloudflare Access, the origin may not match any of the trusted origins Dokploy knows about, so the request is silently dropped.

### Required configuration

You need to configure three things:

1. Set a stable`BETTER_AUTH_SECRET`

Make sure this value is set and does not change between restarts. If it is missing or rotates, sessions are invalidated and auth flows may break.

```
BETTER_AUTH_SECRET=your-random-secret-here
```

Generate a secure value with:

```
openssl rand -hex 32
```

2. Add your domain to trusted origins

Set the`BETTER_AUTH_TRUSTED_ORIGINS` environment variable to include all origins that can reach Dokploy:

```
BETTER_AUTH_TRUSTED_ORIGINS=http://localhost:3000,http://<internal-ip>:3000,https://dokploy.example.com
```

Replace`dokploy.example.com` with your actual public domain.

3. Configure Web Server settings in the Dokploy UI

Go to Settings → Server and set:

- Host:`dokploy.example.com`(your public domain)
- HTTPS: enabled

This ensures Dokploy includes your domain as a trusted origin automatically.

After applying these changes, redeploy the Dokploy service so the new environment variables take effect.

If you access Dokploy through multiple origins (public domain, internal IP, Tailscale), make sure all of them are listed in`BETTER_AUTH_TRUSTED_ORIGINS`.

Audit LogsTrack all actions performed by members in your organization

TailscaleLearn how to use Tailscale to securely access your Dokploy applications and servers through a private network without opening ports.

### On this page

What are Cloudflare Tunnels?BenefitsPrerequisitesCloudflare Tunnel SetupStep 1: Create a Tunnel in CloudflareStep 2: Configure SSL/TLS SettingsStep 3: Create Cloudflare Service in DokployStep 4: Configuring Public Hostnames (Domains)Understanding Traefik Routing vs Direct AccessFor Applications (via Traefik)For Direct Container AccessFor Wildcard Subdomains (Multiple Apps)Using Cloudflare Access (Zero Trust) with DokployWhy login hangs behind Cloudflare AccessRequired configuration