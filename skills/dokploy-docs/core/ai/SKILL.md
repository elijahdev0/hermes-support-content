---
title: "AI Assistant | Dokploy"
source: "https://docs.dokploy.com/docs/core/ai"
category: dokploy-docs
created: "2026-06-25T17:16:08.647Z"
---

AI Assistant | Dokploy

# AI Assistant

Copy as Markdown

Use AI to generate Docker Compose templates in Dokploy.

Dokploy integrates with AI providers to let you generate Docker Compose templates from natural language. Describe what you want to deploy, and the AI generates the configuration for you.

Dokploy does not include its own AI model. You need to connect an external provider (like OpenAI, Anthropic, or any OpenAI-compatible API) with your own API key.

## Setting up an AI provider

1. Go to Settings.
2. Navigate to the AI section.
3. Click Add AI Provider.
4. Fill in the configuration:

| Field | Description |
| --- | --- |
| Name | A label for this provider (e.g., "OpenAI", "Claude", "Local LLM") |
| API URL | The API endpoint (e.g.,`https://api.openai.com/v1` for OpenAI) |
| API Key | Your API key for authentication |
| Model | The model to use (e.g.,`gpt-4o`,`claude-sonnet-4-20250514`) |

1. Click Save.

You can configure multiple providers and switch between them.

### Compatible providers

Any provider that exposes an OpenAI-compatible API works with Dokploy. Some examples:

| Provider | API URL | Models |
| --- | --- | --- |
| OpenAI | `https://api.openai.com/v1` | gpt-4o, gpt-4o-mini, o1, etc. |
| Anthropic | `https://api.anthropic.com/v1` | claude-sonnet-4-20250514, claude-haiku-4-5-20251001, etc. |
| Ollama (local) | `http://localhost:11434/v1` | llama3, mistral, codellama, etc. |
| OpenRouter | `https://openrouter.ai/api/v1` | Multiple providers through one API |
| Azure OpenAI | `https://{resource}.openai.azure.com/openai` | gpt-4o, gpt-4, etc. |

## Generating Docker Compose templates

Once you have a provider configured, you can use AI to generate Docker Compose templates when creating a new Compose service.

### How it works

The AI generates a complete`docker-compose.yml` with:

- Service definitions
- Environment variables with sensible defaults
- Volumes and networks
- Any additional config needed

### Example prompts

- Deploy.
- "A WordPress site with MySQL and Redis for caching"
- "Grafana with Prometheus for monitoring"
- "A Node.js API with MongoDB and Redis"
- "Plausible Analytics with PostgreSQL and ClickHouse"
- "Gitea with a PostgreSQL database"

Always review the generated configuration before deploying. The AI provides a starting point — you may need to adjust environment variables, resource limits, or volumes for your specific use case.

## Managing providers

You can manage your AI providers from Settings → AI:

- Add multiple providers for different use cases
- Edit existing provider configurations
- Delete providers you no longer need
- View available models for each provider
- Enable/Disable providers without deleting them

Cloud vs Self-HostedDetailed comparison between Dokploy Cloud and the Self-Hosted version.

### On this page

Setting up an AI providerCompatible providersGenerating Docker Compose templatesHow it worksExample promptsManaging providers