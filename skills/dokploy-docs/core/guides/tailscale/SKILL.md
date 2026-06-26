---
title: "Tailscale | Dokploy"
source: "https://docs.dokploy.com/docs/core/guides/tailscale"
category: dokploy-docs
created: "2026-06-25T17:21:36.902Z"
---

Tailscale | Dokploy

# Tailscale

Copy as Markdown

Learn how to use Tailscale to securely access your Dokploy applications and servers through a private network without opening ports.

Tailscale creates a secure, private network that connects your devices and servers using WireGuard. This allows you to access your Dokploy applications and servers securely without opening ports on your firewall or exposing services to the public internet.

Tailscale is particularly useful for preventing unauthorized access to your services. By keeping your Dokploy instance and applications on a private network, only devices that are explicitly added to your Tailscale network can access them. This means your services remain completely private and invisible to the public internet, significantly reducing the attack surface and preventing unauthorized users from discovering or accessing your infrastructure.

## What is Tailscale?

Tailscale is a zero-config VPN that creates a mesh network between your devices and servers. It uses the WireGuard protocol to establish encrypted connections, making it easy to access your infrastructure securely from anywhere.

### Benefits

- Zero-Config VPN: Automatic key management and network setup
- No Port Forwarding: Access services without opening firewall ports
- Secure by Default: All traffic is encrypted end-to-end
- Private Services: Keep your services completely private and prevent unauthorized access
- Easy Access: Connect from any device with Tailscale installed
- Private IPs: Each device gets a private IP address (100.x.x.x)
- Free Tier Available: Up to 100 devices for personal use
- ACLs: Fine-grained access control lists for security

## Prerequisites

Before setting up Tailscale with Dokploy, ensure you have:

- A Tailscale account (free tier works)
- Dokploy installed and running
- Access to your server via SSH or console
- Tailscale installed on your client devices (optional, for accessing services)

Tailscale works great for accessing Dokploy's admin interface and your applications from anywhere, without exposing them to the public internet. This keeps your services private and prevents unauthorized users from discovering or accessing them.

## Tailscale Setup

This guide will walk you through setting up Tailscale to securely access your Dokploy server and applications through a private network.

### Step 1: Prerequisites

Before starting, ensure you have:

1. Dokploy installed and running - Follow the installation guide if needed
2. A Tailscale account - Create one at tailscale.com(free tier works)

### Step 2: Get Docker Network Subnet

First, we need to identify the Docker network subnet that Dokploy uses. This will be advertised to the Tailscale network to allow access to your containers.

Run the following command on your Dokploy server:

```
docker network inspect dokploy-network | grep Subnet
```

You should see output like this:

```
"Subnet": "10.254.0.0/24",
```

Copy the subnet value (e.g.,`10.254.0.0/24`) - you'll need it in the next step.

### Step 3: Configure Tailscale Server

Now we'll set up Tailscale on your Dokploy server with subnet routing enabled.

#### 3.1: Create Server in Tailscale Admin

1. Go to Tailscale Admin Console
2. Click Add a device → Linux
3. Scroll down and click Generate install script

You'll see a script like this:

```
curl -fsSL https://tailscale.com/install.sh | sh && sudo tailscale up --auth-key=tskey-auth-something-random
```

#### 3.2: Modify the Install Command

We need to modify this command to:

- Enable SSH access with the`--ssh` flag
- Advertise the Docker subnet with`--advertise-routes` flag

Replace`subnet-of-docker` with the subnet you copied in Step 2:

```
curl -fsSL https://tailscale.com/install.sh | sh && sudo tailscale up --ssh --advertise-routes=10.254.0.0/24 --auth-key=tskey-auth-something-random
```

Replace`10.254.0.0/24` with your actual Docker network subnet from Step 2.

#### 3.3: Run the Command

Execute the modified command on your Dokploy server terminal.

#### 3.4: Approve Subnet Routes

After running the command, you need to approve the subnet routes in Tailscale:

1. Go to Tailscale Admin Console
2. Find your server and approve the advertised routes

#### 3.5: Verify Server Connection

Verify that your server is connected to Tailscale:

```
sudo tailscale status
```

You should see your server listed. Get the server's Tailscale IP address:

```
sudo tailscale ip -4
```

This will return something like:

```
100.100.100.100
```

Copy this IPv4 address - you'll use it to access your server and Dokploy.

### Step 4: Configure Client Devices

Now you'll set up client devices (your computer, phone, etc.) to connect to the Tailscale network.

#### 4.1: Add Client Device

Select your device type:

- Windows
- macOS
- Linux
- Android
- iPhone & iPad
- Synology

#### 4.2: Install Tailscale on Client

For macOS:

- Download the native app from tailscale.com/download/macos
- Install and authenticate with your Tailscale account

For other platforms:

- Visit tailscale.com/download for your specific platform
- Follow the installation instructions

Login to your Tailscale account and you should see both your server and client device connected to the network it will also display in the tailscale dashboard.

### Step 5: Access Dokploy via Tailscale

Now you can access Dokploy and your applications through the Tailscale network.

#### Access Dokploy Dashboard

Use your server's Tailscale IP address (from Step 3.5):

```
http://100.100.100.100:3000
```

Replace`100.100.100.100` with your actual Tailscale IP.

Or use the Tailscale hostname (if MagicDNS is enabled):

```
http://your-server-name.tailscale.ts.net:3000
```

#### Access via SSH

You can also SSH into your server using the Tailscale IP:

```
ssh [email protected]
```

https://docs.dokploy.com/cdn-cgi/l/email-protection

Replace`100.100.100.100` with your server's Tailscale IP address.

With this setup, you can access Dokploy and your applications without any port forwarding or exposing services to the public internet. Only devices in your Tailscale network can access these services, ensuring they remain private and protected from unauthorized access.

## Configuring Applications

### Accessing Applications via Tailscale

Once Tailscale is set up, you can access your Dokploy applications through the Tailscale network:

1. Using Tailscale IP: Access applications directly using your server's Tailscale IP and the port configured in Dokploy
2. Using Tailscale DNS: Use your server's Tailscale hostname (e.g.,`your-server.tailscale.ts.net`)

### Example: Accessing an Application

If you have an application running on port`8080`:

Get your server's Tailscale IP:

```
sudo tailscale ip -4
```

Access your application your application/compose should expose the port:

```
http://YOUR_TAILSCALE_IP:8080
```

You can access from your client device or any device in the Tailscale network.

## Advanced Configuration

### Enabling MagicDNS

MagicDNS provides automatic DNS resolution for devices in your Tailscale network:

1. Go to Tailscale Admin Console
2. Enable MagicDNS
3. Optionally add custom DNS names for your devices

With MagicDNS enabled, you can access your server using its hostname.

For example, to access the Dokploy dashboard (which runs on port 3000):

```
http://your-server-name.tailscale.ts.net:3000
```

### Using Custom Domains with MagicDNS

If you want to use a custom domain for your Dokploy server, you'll need to find the Full Domain assigned by Tailscale:

1. Go to Tailscale Admin Console
2. Navigate to Machines and search for your server
3. Scroll down to find the Full Domain field
4. The Full Domain will look something like:`ubuntu-2gb-ash-4.tail1ff529.ts.net`

Once you have the Full Domain, you can use it to access your Dokploy server:

```
http://ubuntu-2gb-ash-4.tail1ff529.ts.net:3000
```

Replace`ubuntu-2gb-ash-4.tail1ff529.ts.net` with your actual server's Full Domain from the Tailscale admin console.

## Securing Your Server with UFW

Once Tailscale is configured, you can further enhance your server's security by using UFW (Uncomplicated Firewall) to block all public internet traffic and only allow connections through Tailscale. This prevents unauthorized access attempts and bot attacks that are common on public-facing servers.

Important: Before proceeding, ensure you can SSH into your server using the Tailscale IP address (from Step 3.5). If you lock down SSH access and lose Tailscale connectivity, you may need console access to your server to regain access.

### Why Use UFW with Tailscale?

Servers on the public internet are constantly scanned and attacked by bots looking for vulnerabilities. By using UFW to block all public traffic and only allowing Tailscale connections, you:

- Eliminate attack surface: Your server becomes invisible to attackers on the public internet
- Prevent bot scans: No more failed login attempts in your logs
- Maintain easy access: You can still access everything through your private Tailscale network
- Keep services private: Dokploy (port 3000) and Traefik (ports 80/443) are only accessible through Tailscale

### Step 1: SSH Over Tailscale

Before locking down public access, verify you can SSH using your Tailscale IP:

Get your server's Tailscale IP:

```
sudo tailscale ip -4
```

Exit your current SSH session and reconnect using the Tailscale IP:

```
exit
ssh <username>@<tailscale-ip>
```

If you can successfully connect, you're ready to proceed.

### Step 2: Enable UFW

UFW comes pre-installed on Ubuntu. Enable it:

```
sudo ufw enable
```

### Step 3: Configure Default Rules

Set UFW to deny all incoming traffic by default, but allow all outgoing traffic:

```
sudo ufw default deny incoming
sudo ufw default allow outgoing
```

### Step 4: Allow Tailscale Traffic

Allow all traffic on the Tailscale interface (`tailscale0`):

```
sudo ufw allow in on tailscale0
```

This ensures all Tailscale connections work properly, including:

- SSH access
- Dokploy dashboard (port 3000)
- Traefik (ports 80/443)
- All your applications

### Step 5: Review and Remove Public Access Rules

Check your current firewall rules:

```
sudo ufw status verbose
```

You might see rules like:

```
To                          Action      From
--                         ------      ----
Anywhere on tailscale0     ALLOW       Anywhere                  
Anywhere (v6) on tailscale0 ALLOW       Anywhere (v6)       
```

Since we're using Tailscale for all access, your server is now configured to only accept connections through the Tailscale network. This means:

- ✅ SSH access: Only available via Tailscale IP
- ✅ Dokploy dashboard: Only accessible via Tailscale IP
- ✅ Traefik: Only accessible via Tailscale IP
- ✅ All applications: Only accessible via Tailscale IP

Important Note About Docker and UFW: Docker directly manipulates`iptables`, which can bypass UFW rules. This means Docker-published ports (like Dokploy on port 3000 or Traefik on ports 80/443) might still be accessible from the public internet even with UFW configured.

Solutions:

Use your VPS provider's firewall (recommended): Configure your cloud provider's firewall to block public access to ports 22, 80, 443, and 3000. This operates before Docker's iptables rules.

Use ufw-docker utility: This tool integrates Docker with UFW properly. However, with Tailscale and subnet routing, this is usually not necessary since all access goes through Tailscale.

Bind Docker ports to localhost: Modify Docker services to bind to`127.0.0.1` instead of`0.0.0.0`, but this may break Tailscale access unless configured carefully.

For Dokploy with Tailscale, the recommended approach is to use your VPS provider's firewall to block public access, as this provides the most reliable protection.

With this configuration, your server is now protected from public internet access. All services (SSH, Dokploy, Traefik, and applications) are only accessible through your private Tailscale network, ensuring they remain secure and invisible to unauthorized users.

Cloudflare TunnelsLearn how to use Cloudflare Tunnels to securely expose your Dokploy applications without opening ports on your server.

EC2 InstructionsInstructions for setting up a remote server on EC2

### On this page

What is Tailscale?BenefitsPrerequisitesTailscale SetupStep 1: PrerequisitesStep 2: Get Docker Network SubnetStep 3: Configure Tailscale Server3.1: Create Server in Tailscale Admin3.2: Modify the Install Command3.3: Run the Command3.4: Approve Subnet Routes3.5: Verify Server ConnectionStep 4: Configure Client Devices4.1: Add Client Device4.2: Install Tailscale on ClientStep 5: Access Dokploy via TailscaleAccess Dokploy DashboardAccess via SSHConfiguring ApplicationsAccessing Applications via TailscaleExample: Accessing an ApplicationAdvanced ConfigurationEnabling MagicDNSUsing Custom Domains with MagicDNSSecuring Your Server with UFWWhy Use UFW with Tailscale?Step 1: SSH Over TailscaleStep 2: Enable UFWStep 3: Configure Default RulesStep 4: Allow Tailscale TrafficStep 5: Review and Remove Public Access Rules