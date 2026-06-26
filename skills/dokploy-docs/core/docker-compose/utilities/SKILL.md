---
title: "Utilities | Dokploy"
source: "https://docs.dokploy.com/docs/core/docker-compose/utilities"
category: dokploy-docs
created: "2026-06-25T17:16:11.092Z"
---

Utilities | Dokploy

Docker Compose

# Utilities

Copy as Markdown

Utilities for your Docker Compose application

Dokploy provides a set of utilities to enhance your Docker Compose application deployment experience.

## Isolated Deployments

All open source templates come with this feature enabled by default.

This feature allows you to deploy your application in a separate network, isolated from other applications. This isolation is particularly useful when you need to deploy multiple instances of the same application.

For example, if you want to deploy two WordPress instances, you would typically encounter service naming conflicts since they share the same network (dokploy-network). Docker doesn't allow services with identical names in the same network. Consider this typical WordPress service:

```
services:
  wordpress:
    image: wordpress:latest
    ports:
      - "80"
```

When Isolated Deployments is enabled, Dokploy will:

1. Create a network based on your`appName` and associate it with each service in your compose file
2. Add the network to every service in your compose file
3. Connect the Traefik load balancer to this isolated network, maintaining service isolation while ensuring proper routing

When using this feature, you don't need to explicitly define dokploy-network in your networks section, as isolation is handled automatically.

Important: Installation Type Considerations

If you're using a custom installation that replaces the standalone Traefik container with a Docker service (see Manual Installation), be aware of the following risks:

System Restart Issues: If your system restarts, your services may lose their network references to Traefik. This happens because Docker Swarm changes network references after a restart, which can cause connectivity issues between your services and Traefik.

Manual Redeployment Required: After a system restart, you may need to manually redeploy your Docker Compose applications to restore network connectivity, which can be tedious and time-consuming.

Reference: For more details about this issue, see GitHub Issue #1004.

Recommended Approach: If you use the official installation or manual installation with the standalone Traefik container, you won't experience these issues. Your services should start normally after a system restart without requiring manual intervention.

ExampleLearn how to use Docker Compose with Dokploy

DatabasesDiscover how to create and backup databases easily with Dokploy, supporting a variety of database systems.

### On this page

Isolated Deployments