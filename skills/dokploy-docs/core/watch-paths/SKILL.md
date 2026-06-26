---
title: "Watch Paths | Dokploy"
source: "https://docs.dokploy.com/docs/core/watch-paths"
category: dokploy-docs
created: "2026-06-25T17:21:39.217Z"
---

Watch Paths | Dokploy

# Watch Paths

Copy as Markdown

Learn how to use watch paths in your application or docker compose.

Watch paths are a feature that allows you to monitor specific directories or files for changes and automatically trigger actions when modifications occur.

## Overview

Watch paths functionality is available for both standalone applications and Docker Compose configurations. This feature helps automate deployments based on file changes in your repository.

## Supported Source Providers

The following source control providers are supported:

- GitHub
- GitLab
- Bitbucket
- Git (works with Bitbucket, Github, and GitLab repositories)

## Basic Usage

Let's say you have a project with the following directory structure:

```
my-app/	
├── src/	
│   ├── index.js	
├── public/	
```

By default, dokploy accepts an array of paths, allowing you to monitor multiple locations. For example:

- To trigger deployments when any file in the`src/` directory changes, use the pattern:`src/*`
- To monitor a specific file, simply specify its path:`src/index.js`

## Configuration

Watch Paths works out of the box with zero configuration when using GitHub as your provider. For other providers, you'll need to first set up auto-deploys as explained in:

- Auto Deploy
- Bitbucket Integration
- GitLab Integration
- GitHub Integration
- Gitea Integration

Note: When using the Git provider, the functionality will only work with GitHub, GitLab, Bitbucket, or Gitea repositories.

## Pattern Matching Features

We support a wide range of pattern matching features:

Wildcards:

- `**`(matches any number of directories)
- `*.js`(matches all JavaScript files)

Negation patterns:

- `!a/*.js`(excludes JavaScript files in directory 'a')
- `*!(b).js`(matches all JavaScript files except those ending with 'b')

Extended glob patterns:

- `+(x|y)`(matches 'x' or 'y' one or more times)
- `!(a|b)`(matches anything except 'a' or 'b')

POSIX character classes:

- `[[:alpha:][:digit:]]`(matches any letter or number)

Brace expansion:

- `foo/{1..5}.md`(matches foo/1.md through foo/5.md)
- `bar/{a,b,c}.js`(matches bar/a.js, bar/b.js, bar/c.js)

Regex character classes:

- `foo-[1-5].js`(matches foo-1.js through foo-5.js)

Regex logical "or":

- `foo/(abc|xyz).js`(matches foo/abc.js or foo/xyz.js)

Normal

ProvidersLearn how to use providers in your application or docker compose.

IntroductionDeploy your apps to multiple servers remotely.

### On this page

OverviewSupported Source ProvidersBasic UsageConfigurationPattern Matching Features