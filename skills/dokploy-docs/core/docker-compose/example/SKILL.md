---
title: "Example | Dokploy"
source: "https://docs.dokploy.com/docs/core/docker-compose/example"
category: dokploy-docs
created: "2026-06-25T17:16:11.092Z"
---

Example | Dokploy

Docker Compose

# Example

Copy as Markdown

Learn how to use Docker Compose with Dokploy

## Tutorial

In this tutorial, we will create a simple application using Docker Compose and route the traffic to an accessible domain.

Note: There are two ways to configure domains for Docker Compose applications:

1. Using Dokploy Domains (Recommended): Configure domains directly in the Dokploy UI through the Domains tab. See the Domains guide for details.
2. Manual Configuration: Configure domains using Traefik labels in your Docker Compose file (shown in this tutorial).

This tutorial demonstrates the manual method. For most users, we recommend using the Dokploy Domains feature as it's simpler and doesn't require editing your Docker Compose file.

### Steps

1. Create a new project.
2. Create a new service`Compose` and select the Compose Type`Docker Compose`.
3. Fork this repository: Repo.
4. Select Provider type: GitHub or Git.
5. Select the repository:`Dokploy/docker-compose-test`.
6. Select the branch:`main`.
7. Set the Compose Path to`./docker-compose.yml` and save.

### Updating Your docker-compose.yml

Add the following to your existing`docker-compose.yml` file:

1. Add the network`dokploy-network` to each service.
2. Add labels for Traefik to make the service accessible through the domain.

Example:

Let's modify the following compose file to make it work with Dokploy:

```
version: "3"

services:
  next-app:
    build:
      context: ./next-app
      dockerfile: prod.Dockerfile
      args:
        ENV_VARIABLE: ${ENV_VARIABLE}
        NEXT_PUBLIC_ENV_VARIABLE: ${NEXT_PUBLIC_ENV_VARIABLE}
    restart: always
    ports:
      - 3000:3000
    networks:
      - my_network
networks:
  my_network:
    external: true
```

Updated version with dokploy-network and Traefik labels:

Don't set container_name property to the each service, it will cause issues with logs, metrics and other features

```
version: "3"

services:
  next-app:
    build:
      context: ./next-app
      dockerfile: prod.Dockerfile
      args:
        ENV_VARIABLE: ${ENV_VARIABLE}
        NEXT_PUBLIC_ENV_VARIABLE: ${NEXT_PUBLIC_ENV_VARIABLE}
    restart: always
    ports:
      - 3000
    networks:
      - dokploy-network
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.<unique-name>.rule=Host(`your-domain.com`)"
      - "traefik.http.routers.<unique-name>.entrypoints=websecure"
      - "traefik.http.routers.<unique-name>.tls.certResolver=letsencrypt"
      - "traefik.http.services.<unique-name>.loadbalancer.server.port=3000"
networks:
  dokploy-network:
    external: true
```

Make sure to point the A record to the domain you want to use for your service.

Deploy the application by clicking on "deploy" and wait for the deployment to complete. Then give Traefik about 10 seconds to generate the certificates. You can then access the application through the domain you have set.

Tips:

1. Set unique names for each router:`traefik.http.routers. `
2. Set unique names for each service:`traefik.http.services. `
3. Ensure the network is linked to the`dokploy-network`
4. Set the entry point to websecure and the certificate resolver to letsencrypt to generate certificates.
5. For Docker Stack: If you're using Docker Stack (Docker Swarm mode), place the labels under`deploy.labels` instead of directly under`labels`. See the Domains guide for the Docker Stack configuration example.

DomainsConfigure domains for your Docker Compose application.

UtilitiesUtilities for your Docker Compose application

### On this page

TutorialStepsUpdating Your`docker-compose.yml`