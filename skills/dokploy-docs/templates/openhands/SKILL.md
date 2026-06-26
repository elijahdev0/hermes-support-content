---
title: "OpenHands | Dokploy"
source: "https://docs.dokploy.com/docs/templates/openhands"
category: dokploy-docs
created: "2026-06-25T17:21:55.476Z"
---

OpenHands | Dokploy

# OpenHands

Copy as Markdown

OpenHands is an open-source platform for running and managing AI agents.

## Configuration

docker-compose.ymltemplate.toml

```
# The 'version' attribute is obsolete and has been removed.
services:
  openhands:
    # Corrected the Docker image to what appears to be the official registry path.
    # This was the cause of the "pull access denied" error.
    image: docker.all-hands.dev/all-hands-ai/openhands:latest
    restart: unless-stopped

    # The port is exposed without mapping. Dokploy handles the routing via the domain.
    ports:
      - "3000"

    # Environment variables are sourced from the template.toml file.
    environment:
      - SANDBOX_RUNTIME_CONTAINER_IMAGE=${SANDBOX_RUNTIME_CONTAINER_IMAGE}
      - WORKSPACE_MOUNT_PATH=/opt/workspace_base

    # Allows the container to communicate with the host's Docker daemon.
    extra_hosts:
      - "host.docker.internal:host-gateway"

    # Volumes for persistent data. Named volumes are used instead of host mounts.
    # The docker socket is mounted to allow OpenHands to manage other containers.
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - openhands-config:/.openhands
      - openhands-workspace:/opt/workspace_base

    # These flags are necessary for the interactive shell functionality of OpenHands.
    stdin_open: true
    tty: true

# Named volumes are defined here to persist configuration and workspace data.
volumes:
  openhands-config: {}
  openhands-workspace: {}
```

```
[variables]
main_domain = "${domain}"
openhands_api_key = "${password:64}"

[config]
[[config.domains]]
serviceName = "openhands"
port = 3000
host = "${main_domain}"

[config.env]
SANDBOX_RUNTIME_CONTAINER_IMAGE="docker.all-hands.dev/all-hands-ai/runtime:0.50-nikolaik"

# Defines a file mount to create the OpenHands configuration file inside the container.
# The file will be placed within the 'openhands-config' volume.
[[config.mounts]]
filePath = "/.openhands/config.toml"
content = """
###################### OpenHands Configuration Example ######################
#
# All settings have default values, so you only need to uncomment and
# modify what you want to change
# The fields within each section are sorted in alphabetical order.
#
##############################################################################

#################################### Core ####################################
# General core configurations
##############################################################################
[core]
# workspace_base = "./workspace"
# cache_dir = "/tmp/cache"
# debug = false
# disable_color = false
# save_trajectory_path="./trajectories"
# save_screenshots_in_trajectory = false
# replay_trajectory_path = ""
# file_store_path = "/tmp/file_store"
# file_store = "memory"
# file_uploads_max_file_size_mb = 0
# enable_browser = true
# max_budget_per_task = 0.0
# max_iterations = 500
# workspace_mount_path_in_sandbox = "/workspace"
# workspace_mount_path = ""
# workspace_mount_rewrite = ""
# run_as_openhands = true
# runtime = "docker"
# default_agent = "CodeActAgent"
# jwt_secret = ""
# file_uploads_restrict_file_types = false
# file_uploads_allowed_extensions = [".*"]
# enable_default_condenser = true
# max_concurrent_conversations = 3
# conversation_max_age_seconds = 864000  # 10 days

#################################### LLM #####################################
# Configuration for LLM models (group name starts with 'llm')
##############################################################################
[llm]
# API key to use. It is being sourced from the Dokploy template variables.
api_key = "${openhands_api_key}" # API Key
# base_url = ""
# api_version = ""
# reasoning_effort = "medium"
# input_cost_per_token = 0.0
# output_cost_per_token = 0.0
# custom_llm_provider = ""
# max_message_chars = 10000
# max_input_tokens = 0
# max_output_tokens = 0
model = "gpt-4o"
# num_retries = 8
# retry_max_wait = 120
# retry_min_wait = 15
# retry_multiplier = 2.0
# drop_params = false
# modify_params = true
# caching_prompt = true
# ollama_base_url = ""
# temperature = 0.0
# timeout = 0
# top_p = 1.0
# disable_vision = true
# custom_tokenizer = ""
# native_tool_calling = None
# safety_settings = []

[llm.draft_editor]
# correct_num = 5

[llm.gpt4o-mini]
api_key = "${openhands_api_key}" # API Key
model = "gpt-4o"

#################################### Agent ###################################
# Configuration for agents
##############################################################################
[agent]
enable_Browse = true
# enable_llm_editor = false
enable_editor = true
enable_jupyter = true
enable_cmd = true
enable_think = true
enable_finish = true
# llm_config = 'your-llm-config-group'
# enable_prompt_extensions = true
# disabled_microagents = []
enable_history_truncation = true
# enable_condensation_request = false

#################################### Sandbox ###################################
# Configuration for the sandbox
##############################################################################
[sandbox]
# timeout = 120
# user_id = 1000
# base_container_image = "nikolaik/python-nodejs:python3.12-nodejs22"
# use_host_network = false
# runtime_extra_build_args = ["--network=host", "--add-host=host.docker.internal:host-gateway"]
# enable_auto_lint = false
# initialize_plugins = true
# runtime_extra_deps = ""
# runtime_startup_env_vars = {}
# browsergym_eval_env = ""
# platform = ""
# force_rebuild_runtime = false
# runtime_container_image = ""
# keep_runtime_alive = false
# pause_closed_runtimes = false
# close_delay = 300
# rm_all_containers = false
# enable_gpu = false
# cuda_visible_devices = ''
# docker_runtime_kwargs = {}
# vscode_port = 41234
# volumes = "/my/host/dir:/workspace:rw,/path2:/workspace/path2:ro"

#################################### Security ###################################
# Configuration for security features
##############################################################################
[security]
# confirmation_mode = false
# security_analyzer = ""
# enable_security_analyzer = false

#################################### Condenser #################################
# Condensers control how conversation history is managed
##############################################################################
[condenser]
type = "noop"
"""
```

## Base64

To import this template in Dokploy: create a Compose service → Advanced → Base64 import and paste the content below:

```
ewogICJjb21wb3NlIjogIiMgVGhlICd2ZXJzaW9uJyBhdHRyaWJ1dGUgaXMgb2Jzb2xldGUgYW5kIGhhcyBiZWVuIHJlbW92ZWQuXG5zZXJ2aWNlczpcbiAgb3BlbmhhbmRzOlxuICAgICMgQ29ycmVjdGVkIHRoZSBEb2NrZXIgaW1hZ2UgdG8gd2hhdCBhcHBlYXJzIHRvIGJlIHRoZSBvZmZpY2lhbCByZWdpc3RyeSBwYXRoLlxuICAgICMgVGhpcyB3YXMgdGhlIGNhdXNlIG9mIHRoZSBcInB1bGwgYWNjZXNzIGRlbmllZFwiIGVycm9yLlxuICAgIGltYWdlOiBkb2NrZXIuYWxsLWhhbmRzLmRldi9hbGwtaGFuZHMtYWkvb3BlbmhhbmRzOmxhdGVzdFxuICAgIHJlc3RhcnQ6IHVubGVzcy1zdG9wcGVkXG5cbiAgICAjIFRoZSBwb3J0IGlzIGV4cG9zZWQgd2l0aG91dCBtYXBwaW5nLiBEb2twbG95IGhhbmRsZXMgdGhlIHJvdXRpbmcgdmlhIHRoZSBkb21haW4uXG4gICAgcG9ydHM6XG4gICAgICAtIFwiMzAwMFwiXG5cbiAgICAjIEVudmlyb25tZW50IHZhcmlhYmxlcyBhcmUgc291cmNlZCBmcm9tIHRoZSB0ZW1wbGF0ZS50b21sIGZpbGUuXG4gICAgZW52aXJvbm1lbnQ6XG4gICAgICAtIFNBTkRCT1hfUlVOVElNRV9DT05UQUlORVJfSU1BR0U9JHtTQU5EQk9YX1JVTlRJTUVfQ09OVEFJTkVSX0lNQUdFfVxuICAgICAgLSBXT1JLU1BBQ0VfTU9VTlRfUEFUSD0vb3B0L3dvcmtzcGFjZV9iYXNlXG5cbiAgICAjIEFsbG93cyB0aGUgY29udGFpbmVyIHRvIGNvbW11bmljYXRlIHdpdGggdGhlIGhvc3QncyBEb2NrZXIgZGFlbW9uLlxuICAgIGV4dHJhX2hvc3RzOlxuICAgICAgLSBcImhvc3QuZG9ja2VyLmludGVybmFsOmhvc3QtZ2F0ZXdheVwiXG5cbiAgICAjIFZvbHVtZXMgZm9yIHBlcnNpc3RlbnQgZGF0YS4gTmFtZWQgdm9sdW1lcyBhcmUgdXNlZCBpbnN0ZWFkIG9mIGhvc3QgbW91bnRzLlxuICAgICMgVGhlIGRvY2tlciBzb2NrZXQgaXMgbW91bnRlZCB0byBhbGxvdyBPcGVuSGFuZHMgdG8gbWFuYWdlIG90aGVyIGNvbnRhaW5lcnMuXG4gICAgdm9sdW1lczpcbiAgICAgIC0gL3Zhci9ydW4vZG9ja2VyLnNvY2s6L3Zhci9ydW4vZG9ja2VyLnNvY2tcbiAgICAgIC0gb3BlbmhhbmRzLWNvbmZpZzovLm9wZW5oYW5kc1xuICAgICAgLSBvcGVuaGFuZHMtd29ya3NwYWNlOi9vcHQvd29ya3NwYWNlX2Jhc2VcblxuICAgICMgVGhlc2UgZmxhZ3MgYXJlIG5lY2Vzc2FyeSBmb3IgdGhlIGludGVyYWN0aXZlIHNoZWxsIGZ1bmN0aW9uYWxpdHkgb2YgT3BlbkhhbmRzLlxuICAgIHN0ZGluX29wZW46IHRydWVcbiAgICB0dHk6IHRydWVcblxuIyBOYW1lZCB2b2x1bWVzIGFyZSBkZWZpbmVkIGhlcmUgdG8gcGVyc2lzdCBjb25maWd1cmF0aW9uIGFuZCB3b3Jrc3BhY2UgZGF0YS5cbnZvbHVtZXM6XG4gIG9wZW5oYW5kcy1jb25maWc6IHt9XG4gIG9wZW5oYW5kcy13b3Jrc3BhY2U6IHt9XG4iLAogICJjb25maWciOiAiW3ZhcmlhYmxlc11cbm1haW5fZG9tYWluID0gXCIke2RvbWFpbn1cIlxub3BlbmhhbmRzX2FwaV9rZXkgPSBcIiR7cGFzc3dvcmQ6NjR9XCJcblxuW2NvbmZpZ11cbltbY29uZmlnLmRvbWFpbnNdXVxuc2VydmljZU5hbWUgPSBcIm9wZW5oYW5kc1wiXG5wb3J0ID0gMzAwMFxuaG9zdCA9IFwiJHttYWluX2RvbWFpbn1cIlxuXG5bY29uZmlnLmVudl1cblNBTkRCT1hfUlVOVElNRV9DT05UQUlORVJfSU1BR0U9XCJkb2NrZXIuYWxsLWhhbmRzLmRldi9hbGwtaGFuZHMtYWkvcnVudGltZTowLjUwLW5pa29sYWlrXCJcblxuIyBEZWZpbmVzIGEgZmlsZSBtb3VudCB0byBjcmVhdGUgdGhlIE9wZW5IYW5kcyBjb25maWd1cmF0aW9uIGZpbGUgaW5zaWRlIHRoZSBjb250YWluZXIuXG4jIFRoZSBmaWxlIHdpbGwgYmUgcGxhY2VkIHdpdGhpbiB0aGUgJ29wZW5oYW5kcy1jb25maWcnIHZvbHVtZS5cbltbY29uZmlnLm1vdW50c11dXG5maWxlUGF0aCA9IFwiLy5vcGVuaGFuZHMvY29uZmlnLnRvbWxcIlxuY29udGVudCA9IFwiXCJcIlxuIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyBPcGVuSGFuZHMgQ29uZmlndXJhdGlvbiBFeGFtcGxlICMjIyMjIyMjIyMjIyMjIyMjIyMjIyNcbiNcbiMgQWxsIHNldHRpbmdzIGhhdmUgZGVmYXVsdCB2YWx1ZXMsIHNvIHlvdSBvbmx5IG5lZWQgdG8gdW5jb21tZW50IGFuZFxuIyBtb2RpZnkgd2hhdCB5b3Ugd2FudCB0byBjaGFuZ2VcbiMgVGhlIGZpZWxkcyB3aXRoaW4gZWFjaCBzZWN0aW9uIGFyZSBzb3J0ZWQgaW4gYWxwaGFiZXRpY2FsIG9yZGVyLlxuI1xuIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjXG5cbiMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyBDb3JlICMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjI1xuIyBHZW5lcmFsIGNvcmUgY29uZmlndXJhdGlvbnNcbiMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjI1xuW2NvcmVdXG4jIHdvcmtzcGFjZV9iYXNlID0gXCIuL3dvcmtzcGFjZVwiXG4jIGNhY2hlX2RpciA9IFwiL3RtcC9jYWNoZVwiXG4jIGRlYnVnID0gZmFsc2VcbiMgZGlzYWJsZV9jb2xvciA9IGZhbHNlXG4jIHNhdmVfdHJhamVjdG9yeV9wYXRoPVwiLi90cmFqZWN0b3JpZXNcIlxuIyBzYXZlX3NjcmVlbnNob3RzX2luX3RyYWplY3RvcnkgPSBmYWxzZVxuIyByZXBsYXlfdHJhamVjdG9yeV9wYXRoID0gXCJcIlxuIyBmaWxlX3N0b3JlX3BhdGggPSBcIi90bXAvZmlsZV9zdG9yZVwiXG4jIGZpbGVfc3RvcmUgPSBcIm1lbW9yeVwiXG4jIGZpbGVfdXBsb2Fkc19tYXhfZmlsZV9zaXplX21iID0gMFxuIyBlbmFibGVfYnJvd3NlciA9IHRydWVcbiMgbWF4X2J1ZGdldF9wZXJfdGFzayA9IDAuMFxuIyBtYXhfaXRlcmF0aW9ucyA9IDUwMFxuIyB3b3Jrc3BhY2VfbW91bnRfcGF0aF9pbl9zYW5kYm94ID0gXCIvd29ya3NwYWNlXCJcbiMgd29ya3NwYWNlX21vdW50X3BhdGggPSBcIlwiXG4jIHdvcmtzcGFjZV9tb3VudF9yZXdyaXRlID0gXCJcIlxuIyBydW5fYXNfb3BlbmhhbmRzID0gdHJ1ZVxuIyBydW50aW1lID0gXCJkb2NrZXJcIlxuIyBkZWZhdWx0X2FnZW50ID0gXCJDb2RlQWN0QWdlbnRcIlxuIyBqd3Rfc2VjcmV0ID0gXCJcIlxuIyBmaWxlX3VwbG9hZHNfcmVzdHJpY3RfZmlsZV90eXBlcyA9IGZhbHNlXG4jIGZpbGVfdXBsb2Fkc19hbGxvd2VkX2V4dGVuc2lvbnMgPSBbXCIuKlwiXVxuIyBlbmFibGVfZGVmYXVsdF9jb25kZW5zZXIgPSB0cnVlXG4jIG1heF9jb25jdXJyZW50X2NvbnZlcnNhdGlvbnMgPSAzXG4jIGNvbnZlcnNhdGlvbl9tYXhfYWdlX3NlY29uZHMgPSA4NjQwMDDCoCAjIDEwIGRheXNcblxuIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIExMTSAjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjXG4jIENvbmZpZ3VyYXRpb24gZm9yIExMTSBtb2RlbHMgKGdyb3VwIG5hbWUgc3RhcnRzIHdpdGggJ2xsbScpXG4jIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyNcbltsbG1dXG4jIEFQSSBrZXkgdG8gdXNlLiBJdCBpcyBiZWluZyBzb3VyY2VkIGZyb20gdGhlIERva3Bsb3kgdGVtcGxhdGUgdmFyaWFibGVzLlxuYXBpX2tleSA9IFwiJHtvcGVuaGFuZHNfYXBpX2tleX1cIiAjIEFQSSBLZXlcbiMgYmFzZV91cmwgPSBcIlwiXG4jIGFwaV92ZXJzaW9uID0gXCJcIlxuIyByZWFzb25pbmdfZWZmb3J0ID0gXCJtZWRpdW1cIlxuIyBpbnB1dF9jb3N0X3Blcl90b2tlbiA9IDAuMFxuIyBvdXRwdXRfY29zdF9wZXJfdG9rZW4gPSAwLjBcbiMgY3VzdG9tX2xsbV9wcm92aWRlciA9IFwiXCJcbiMgbWF4X21lc3NhZ2VfY2hhcnMgPSAxMDAwMFxuIyBtYXhfaW5wdXRfdG9rZW5zID0gMFxuIyBtYXhfb3V0cHV0X3Rva2VucyA9IDBcbm1vZGVsID0gXCJncHQtNG9cIlxuIyBudW1fcmV0cmllcyA9IDhcbiMgcmV0cnlfbWF4X3dhaXQgPSAxMjBcbiMgcmV0cnlfbWluX3dhaXQgPSAxNVxuIyByZXRyeV9tdWx0aXBsaWVyID0gMi4wXG4jIGRyb3BfcGFyYW1zID0gZmFsc2VcbiMgbW9kaWZ5X3BhcmFtcyA9IHRydWVcbiMgY2FjaGluZ19wcm9tcHQgPSB0cnVlXG4jIG9sbGFtYV9iYXNlX3VybCA9IFwiXCJcbiMgdGVtcGVyYXR1cmUgPSAwLjBcbiMgdGltZW91dCA9IDBcbiMgdG9wX3AgPSAxLjBcbiMgZGlzYWJsZV92aXNpb24gPSB0cnVlXG4jIGN1c3RvbV90b2tlbml6ZXIgPSBcIlwiXG4jIG5hdGl2ZV90b29sX2NhbGxpbmcgPSBOb25lXG4jIHNhZmV0eV9zZXR0aW5ncyA9IFtdXG5cbltsbG0uZHJhZnRfZWRpdG9yXVxuIyBjb3JyZWN0X251bSA9IDVcblxuW2xsbS5ncHQ0by1taW5pXVxuYXBpX2tleSA9IFwiJHtvcGVuaGFuZHNfYXBpX2tleX1cIiAjIEFQSSBLZXlcbm1vZGVsID0gXCJncHQtNG9cIlxuXG4jIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMgQWdlbnQgIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyNcbiMgQ29uZmlndXJhdGlvbiBmb3IgYWdlbnRzXG4jIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyNcblthZ2VudF1cbmVuYWJsZV9Ccm93c2UgPSB0cnVlXG4jIGVuYWJsZV9sbG1fZWRpdG9yID0gZmFsc2VcbmVuYWJsZV9lZGl0b3IgPSB0cnVlXG5lbmFibGVfanVweXRlciA9IHRydWVcbmVuYWJsZV9jbWQgPSB0cnVlXG5lbmFibGVfdGhpbmsgPSB0cnVlXG5lbmFibGVfZmluaXNoID0gdHJ1ZVxuIyBsbG1fY29uZmlnID0gJ3lvdXItbGxtLWNvbmZpZy1ncm91cCdcbiMgZW5hYmxlX3Byb21wdF9leHRlbnNpb25zID0gdHJ1ZVxuIyBkaXNhYmxlZF9taWNyb2FnZW50cyA9IFtdXG5lbmFibGVfaGlzdG9yeV90cnVuY2F0aW9uID0gdHJ1ZVxuIyBlbmFibGVfY29uZGVuc2F0aW9uX3JlcXVlc3QgPSBmYWxzZVxuXG4jIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMgU2FuZGJveCAjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjI1xuIyBDb25maWd1cmF0aW9uIGZvciB0aGUgc2FuZGJveFxuIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjXG5bc2FuZGJveF1cbiMgdGltZW91dCA9IDEyMFxuIyB1c2VyX2lkID0gMTAwMFxuIyBiYXNlX2NvbnRhaW5lcl9pbWFnZSA9IFwibmlrb2xhaWsvcHl0aG9uLW5vZGVqczpweXRob24zLjEyLW5vZGVqczIyXCJcbiMgdXNlX2hvc3RfbmV0d29yayA9IGZhbHNlXG4jIHJ1bnRpbWVfZXh0cmFfYnVpbGRfYXJncyA9IFtcIi0tbmV0d29yaz1ob3N0XCIsIFwiLS1hZGQtaG9zdD1ob3N0LmRvY2tlci5pbnRlcm5hbDpob3N0LWdhdGV3YXlcIl1cbiMgZW5hYmxlX2F1dG9fbGludCA9IGZhbHNlXG4jIGluaXRpYWxpemVfcGx1Z2lucyA9IHRydWVcbiMgcnVudGltZV9leHRyYV9kZXBzID0gXCJcIlxuIyBydW50aW1lX3N0YXJ0dXBfZW52X3ZhcnMgPSB7fVxuIyBicm93c2VyZ3ltX2V2YWxfZW52ID0gXCJcIlxuIyBwbGF0Zm9ybSA9IFwiXCJcbiMgZm9yY2VfcmVidWlsZF9ydW50aW1lID0gZmFsc2VcbiMgcnVudGltZV9jb250YWluZXJfaW1hZ2UgPSBcIlwiXG4jIGtlZXBfcnVudGltZV9hbGl2ZSA9IGZhbHNlXG4jIHBhdXNlX2Nsb3NlZF9ydW50aW1lcyA9IGZhbHNlXG4jIGNsb3NlX2RlbGF5ID0gMzAwXG4jIHJtX2FsbF9jb250YWluZXJzID0gZmFsc2VcbiMgZW5hYmxlX2dwdSA9IGZhbHNlXG4jIGN1ZGFfdmlzaWJsZV9kZXZpY2VzID0gJydcbiMgZG9ja2VyX3J1bnRpbWVfa3dhcmdzID0ge31cbiMgdnNjb2RlX3BvcnQgPSA0MTIzNFxuIyB2b2x1bWVzID0gXCIvbXkvaG9zdC9kaXI6L3dvcmtzcGFjZTpydywvcGF0aDI6L3dvcmtzcGFjZS9wYXRoMjpyb1wiXG5cbiMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyBTZWN1cml0eSAjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjI1xuIyBDb25maWd1cmF0aW9uIGZvciBzZWN1cml0eSBmZWF0dXJlc1xuIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjXG5bc2VjdXJpdHldXG4jIGNvbmZpcm1hdGlvbl9tb2RlID0gZmFsc2VcbiMgc2VjdXJpdHlfYW5hbHl6ZXIgPSBcIlwiXG4jIGVuYWJsZV9zZWN1cml0eV9hbmFseXplciA9IGZhbHNlXG5cbiMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyBDb25kZW5zZXIgIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjXG4jIENvbmRlbnNlcnMgY29udHJvbCBob3cgY29udmVyc2F0aW9uIGhpc3RvcnkgaXMgbWFuYWdlZFxuIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjXG5bY29uZGVuc2VyXVxudHlwZSA9IFwibm9vcFwiXG5cIlwiXCIiCn0=
```

## Links

`ai`,`agents`,`llm`,`openai`

---

Version:`0.1.1`

OpenGistOpenGist is a self-hosted pastebin alternative.

OpeninaryOpeninary is a self-hosted Cloudinary alternative.

### On this page

ConfigurationBase64LinksTags