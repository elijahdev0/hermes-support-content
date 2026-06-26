---
title: "Installation | Dokploy"
source: "https://docs.dokploy.com/docs/core/installation"
category: dokploy-docs
created: "2026-06-25T17:21:36.902Z"
---

Installation | Dokploy

# Installation

Copy as Markdown

Get Dokploy up and running on your server within minutes with this easy-to-follow installation guide.

Follow these steps in order to set up Dokploy locally and deploy it to your server, effectively managing Docker containers and applications:

You need to follow this steps in the same order:

1. Virtual Private Server (VPS)

## Virtual Private Server (VPS)

There are multiple VPS providers to choose from:

We have tested on the following Linux Distros:

- Ubuntu 24.04 LTS
- Ubuntu 23.10
- Ubuntu 22.04 LTS
- Ubuntu 20.04 LTS
- Ubuntu 18.04 LTS
- Debian 12
- Debian 11
- Debian 10
- Fedora 40
- Centos 9
- Centos 8

### Providers

### Requirements

To ensure a smooth experience with Dokploy, your server should have at least 2GB of RAM and 30GB of disk space. This specification helps to handle the resources consumed by Docker during builds and prevents system freezes.

Suggestion: For cost efficiency with reliable service, we recommend Hetzner as the best value-for-money VPS provider.

### Port Requirements

Before installing Dokploy, ensure the following ports are available on your server:

- Port 80: HTTP traffic (used by Traefik)
- Port 443: HTTPS traffic (used by Traefik)
- Port 3000: Dokploy web interface

Important: The installation will fail if any of these ports are already in use. Make sure to stop any services using these ports before running the installation script.

### Docker

Dokploy utilizes Docker, so it is essential to have Docker installed on your server. If Docker is not already installed, Dokploy's installation script will install it automatically. Use the following command to install Dokploy:

Dokploy Cloud: Use Dokploy directly without worrying about maintenance or updates. Enjoy a hassle-free experience with Dokploy Cloud. Sign up

```
curl -sSL https://dokploy.com/install.sh | sh
```

See Manual Installation if you want to customize your Dokploy installation.

### Advanced Installation Options

The installation script automatically detects and installs the latest stable version from GitHub. However, you can customize the installation using environment variables:

#### Install Specific Versions

Install Canary Version (Development):

```
export DOKPLOY_VERSION=canary && curl -sSL https://dokploy.com/install.sh | sh
```

Install Latest Stable:

```
export DOKPLOY_VERSION=latest && curl -sSL https://dokploy.com/install.sh | sh
```

Install Specific Version:

```
export DOKPLOY_VERSION=v0.26.6 && curl -sSL https://dokploy.com/install.sh | sh
```

#### Custom Network Configuration

If you need to customize the Docker Swarm network configuration (useful to avoid CIDR conflicts with cloud provider VPCs):

```
export DOCKER_SWARM_INIT_ARGS="--default-addr-pool 172.20.0.0/16 --default-addr-pool-mask-length 24"
curl -sSL https://dokploy.com/install.sh | sh
```

If the script cannot detect your server's IP automatically, specify it manually:

```
export ADVERTISE_ADDR=192.168.1.100
curl -sSL https://dokploy.com/install.sh | sh
```

### Proxmox LXC Support

The installation script automatically detects Proxmox LXC containers and applies the necessary configurations (`--endpoint-mode dnsrr`) for compatibility.

### Updating Dokploy

To update your Dokploy installation to the latest version:

```
curl -sSL https://dokploy.com/install.sh | sh -s update
```

Update to Specific Version:

```
export DOKPLOY_VERSION=v0.26.6 && curl -sSL https://dokploy.com/install.sh | sh -s update
```

## Completing the Setup

After running the installation script, Dokploy and its dependencies will be set up on your server. Here's how to finalize the setup and start using Dokploy:

### Accessing Dokploy

Open your web browser and navigate to`http://your-ip-from-your-vps:3000`. You will be directed to the initial setup page where you can configure the administrative account for Dokploy.

Important: Ensure that your server's firewall allows traffic on port 3000 to access the Dokploy web interface.

### Initial Configuration

1. Create an Admin Account: Fill in the necessary details to set up your administrator account. This account will be the admin account for Dokploy.

### Secure Your Installation

After setting up your admin account, it's crucial to secure your Dokploy installation by enabling HTTPS.

To configure a domain with SSL/TLS certificates for your Dokploy panel, please refer to the Domains section where you'll find detailed instructions for different SSL configurations including Let's Encrypt, Cloudflare, and custom certificates.

### Disable access via ip:port (Optional but Recommended)

To enhance security, it's advisable to restrict access to Dokploy via the server's IP address and port.

Important: Before disabling IP:port access, make sure you have configured a domain with HTTPS working properly. Otherwise, you will lose access to your Dokploy installation. See the Domains section to set this up first.

Once you have verified that your domain is working correctly, you can disable IP:port access by running this command on the server:

```
docker service update --publish-rm "published=3000,target=3000,mode=host" dokploy
```

To further secure your installation, consider reading the Security recommendations section.

ComparisonA comparison of Dokploy, CapRover, Dokku, and Coolify

Manual InstallationLearn how to manually install Dokploy on your server.

### On this page

Virtual Private Server (VPS)ProvidersRequirementsPort RequirementsDockerAdvanced Installation OptionsInstall Specific VersionsCustom Network ConfigurationManual Advertise AddressProxmox LXC SupportUpdating DokployCompleting the SetupAccessing DokployInitial ConfigurationSecure Your InstallationDisable access via ip:port (Optional but Recommended)