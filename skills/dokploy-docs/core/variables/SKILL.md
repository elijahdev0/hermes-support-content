---
title: "Environment Variables | Dokploy"
source: "https://docs.dokploy.com/docs/core/variables"
category: dokploy-docs
created: "2026-06-25T17:21:39.216Z"
---

Environment Variables | Dokploy

# Environment Variables

Copy as Markdown

Dokploy allows you to create and manage shared and service-level environment variables for your projects and environments.

## Overview

Environment variables in Dokploy allow you to:

- Define configuration once and reuse it
- Share values across multiple services
- Reference values from within the same service
- Centrally manage sensitive information

## Defining Variables

You can declare environment variables either:

- Project-level (shared) — available across all services in the project
- Environment-level — specific to a single environment
- Service-level — specific to a single service

## Project-Level Variables

### Practical Example

Let's consider a common scenario where you have:

- A PostgreSQL database
- Two services that need to connect to this database

### 1. Define Shared Variable

In the project's shared variables section, define:

```
DATABASE_URL=postgresql://postgres:postgres@database:5432/postgres
```

### 2. Use the Variable in Services

In each service's environment variables tab, reference the shared variable:

```
DATABASE_URL=${{project.DATABASE_URL}}
```

Dokploy will automatically replace`${{project.DATABASE_URL}}` with the value defined in the project's shared variables.

You can use shared environment variables in all the services available in dokploy.

## Environment-Level Variables

### Practical Example

Let's consider a scenario where you have:

- A staging environment with different database credentials
- Multiple services that need environment-specific configurations

### 1. Define Environment Variable

In the environment's variables section, define:

```
DATABASE_PASSWORD=staging_secret_password
API_KEY=staging_api_key_12345
```

### 2. Use the Variable in Services

In each service's environment variables tab, reference the environment variable:

```
DATABASE_URL=postgresql://postgres:${{environment.DATABASE_PASSWORD}}@staging-db:5432/postgres
EXTERNAL_API_KEY=${{environment.API_KEY}}
```

Dokploy will automatically replace`${{environment.VARIABLE_NAME}}` with the value defined in the environment's variables.

You can use environment variables in all the services available in that specific environment.

## Service-Level Variables

Service-level variables are specific to a single service and can be used to override shared variables or define service-specific configurations.

### Practical Example

Let's say you have a service that requires a different database user. You can define a service-level variable:

```
DATABASE_USER=service_user
DATABASE_PASSWORD=service_password
DATABASE_URL=postgresql://${{DATABASE_USER}}:${{DATABASE_PASSWORD}}@service-database:5432/postgres
```

Preview Deployments environments also include a service-level variable called`DOKPLOY_DEPLOY_URL`, which points to the deployment URL of the service. It can be used as`${{DOKPLOY_DEPLOY_URL}}` for variables like`APP_URL=https://${{DOKPLOY_DEPLOY_URL}}`.

### Best Practices

- Use shared variables for credentials and configurations that repeat across services
- Keep descriptive variable names
- Document the purpose of each variable for easier maintenance

BackupsLearn how to create and restore backups of your Dokploy applications and services.

DomainsThis section outlines how to configure domains for your applications in Dokploy, ensuring that your applications are accessible via custom URLs.

### On this page

OverviewDefining VariablesProject-Level VariablesPractical Example1. Define Shared Variable2. Use the Variable in ServicesEnvironment-Level VariablesPractical Example1. Define Environment Variable2. Use the Variable in ServicesService-Level VariablesPractical ExampleBest Practices