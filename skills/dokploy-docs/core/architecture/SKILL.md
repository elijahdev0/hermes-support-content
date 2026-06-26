---
title: "Architecture of Dokploy | Dokploy"
source: "https://docs.dokploy.com/docs/core/architecture"
category: dokploy-docs
created: "2026-06-25T17:16:11.090Z"
---

Architecture of Dokploy | Dokploy

# Architecture of Dokploy

Copy as Markdown

Overview of the core architecture components of Dokploy.

Understanding the architecture of Dokploy is crucial for both deploying and scaling applications. Below is a diagram illustrating the core components:

## Installation Process

When Dokploy is installed, it automatically sets up the following components:

1. Next.js Application: Serves as the frontend interface. Utilizing Next.js allows for an integrated server-side rendering experience, streamlining the UI and backend into a single cohesive application.
2. PostgreSQL Database: Acts as the primary database for Dokploy, chosen for its robustness and widespread adoption. It stores all the configuration and operational data.
3. Redis Database: Employed for managing deployment queues. This ensures that multiple deployments do not trigger simultaneously, which could lead to high server load and potential freezing.
4. Traefik: Used as a reverse proxy and load balancer. Traefik facilitates dynamic routing and service discovery which simplifies the configuration process by allowing declarative setup through the UI.

## Purpose and Functionality

Each component in the Dokploy architecture plays a vital role:

- Next.js: Provides a scalable and easy-to-manage frontend framework, encapsulating both server and client-side logic in one platform. This simplifies deployment and development workflows.
- PostgreSQL: Delivers reliable and secure data storage capabilities. Its use within Dokploy ensures consistency and high performance for all database operations.
- Redis: Handles concurrency and job scheduling. By using Redis, Dokploy can efficiently manage deployment tasks, avoiding collisions and server overload during simultaneous operations.
- Traefik: Enhances Docker integration. Its ability to read from and write to Docker configurations declaratively allows Dokploy to automate and streamline network traffic management and service discovery.

This structure ensures that Dokploy is not only efficient in deploying applications but also robust in handling traffic and data at scale.

Welcome to DokployDokploy is a open source alternative to Heroku, Vercel, and Netlify.

FeaturesExplore the comprehensive suite of features available in Dokploy for optimized application deployment and management.

### On this page

Installation ProcessPurpose and Functionality