# ApplicationUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **str** |  | 
**name** | **str** |  | [optional] 
**app_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**env** | **str** |  | [optional] 
**preview_env** | **str** |  | [optional] 
**watch_paths** | **List[str]** |  | [optional] 
**preview_build_args** | **str** |  | [optional] 
**preview_build_secrets** | **str** |  | [optional] 
**preview_labels** | **List[str]** |  | [optional] 
**preview_wildcard** | **str** |  | [optional] 
**preview_port** | **float** |  | [optional] 
**preview_https** | **bool** |  | [optional] 
**preview_path** | **str** |  | [optional] 
**preview_certificate_type** | **str** |  | [optional] 
**preview_custom_cert_resolver** | **str** |  | [optional] 
**preview_limit** | **float** |  | [optional] 
**is_preview_deployments_active** | **bool** |  | [optional] 
**preview_require_collaborator_permissions** | **bool** |  | [optional] 
**rollback_active** | **bool** |  | [optional] 
**build_args** | **str** |  | [optional] 
**build_secrets** | **str** |  | [optional] 
**memory_reservation** | **str** |  | [optional] 
**memory_limit** | **str** |  | [optional] 
**cpu_reservation** | **str** |  | [optional] 
**cpu_limit** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**subtitle** | **str** |  | [optional] 
**command** | **str** |  | [optional] 
**args** | **List[str]** |  | [optional] 
**icon** | **str** |  | [optional] 
**refresh_token** | **str** |  | [optional] 
**source_type** | **str** |  | [optional] 
**clean_cache** | **bool** |  | [optional] 
**repository** | **str** |  | [optional] 
**owner** | **str** |  | [optional] 
**branch** | **str** |  | [optional] 
**build_path** | **str** |  | [optional] 
**trigger_type** | **str** |  | [optional] 
**auto_deploy** | **bool** |  | [optional] 
**gitlab_project_id** | **float** |  | [optional] 
**gitlab_repository** | **str** |  | [optional] 
**gitlab_owner** | **str** |  | [optional] 
**gitlab_branch** | **str** |  | [optional] 
**gitlab_build_path** | **str** |  | [optional] 
**gitlab_path_namespace** | **str** |  | [optional] 
**gitea_repository** | **str** |  | [optional] 
**gitea_owner** | **str** |  | [optional] 
**gitea_branch** | **str** |  | [optional] 
**gitea_build_path** | **str** |  | [optional] 
**bitbucket_repository** | **str** |  | [optional] 
**bitbucket_repository_slug** | **str** |  | [optional] 
**bitbucket_owner** | **str** |  | [optional] 
**bitbucket_branch** | **str** |  | [optional] 
**bitbucket_build_path** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**docker_image** | **str** |  | [optional] 
**registry_url** | **str** |  | [optional] 
**custom_git_url** | **str** |  | [optional] 
**custom_git_branch** | **str** |  | [optional] 
**custom_git_build_path** | **str** |  | [optional] 
**custom_git_ssh_key_id** | **str** |  | [optional] 
**enable_submodules** | **bool** |  | [optional] 
**dockerfile** | **str** |  | [optional] 
**docker_context_path** | **str** |  | [optional] 
**docker_build_stage** | **str** |  | [optional] 
**drop_build_path** | **str** |  | [optional] 
**health_check_swarm** | [**ApplicationUpdateRequestHealthCheckSwarm**](ApplicationUpdateRequestHealthCheckSwarm.md) |  | [optional] 
**restart_policy_swarm** | [**ApplicationUpdateRequestRestartPolicySwarm**](ApplicationUpdateRequestRestartPolicySwarm.md) |  | [optional] 
**placement_swarm** | [**ApplicationUpdateRequestPlacementSwarm**](ApplicationUpdateRequestPlacementSwarm.md) |  | [optional] 
**update_config_swarm** | [**ApplicationUpdateRequestUpdateConfigSwarm**](ApplicationUpdateRequestUpdateConfigSwarm.md) |  | [optional] 
**rollback_config_swarm** | [**ApplicationUpdateRequestRollbackConfigSwarm**](ApplicationUpdateRequestRollbackConfigSwarm.md) |  | [optional] 
**mode_swarm** | [**ApplicationUpdateRequestModeSwarm**](ApplicationUpdateRequestModeSwarm.md) |  | [optional] 
**labels_swarm** | **Dict[str, Optional[str]]** |  | [optional] 
**network_swarm** | [**List[ApplicationUpdateRequestNetworkSwarmInner]**](ApplicationUpdateRequestNetworkSwarmInner.md) |  | [optional] 
**stop_grace_period_swarm** | **float** |  | [optional] 
**endpoint_spec_swarm** | [**ApplicationUpdateRequestEndpointSpecSwarm**](ApplicationUpdateRequestEndpointSpecSwarm.md) |  | [optional] 
**ulimits_swarm** | [**List[ApplicationUpdateRequestUlimitsSwarmInner]**](ApplicationUpdateRequestUlimitsSwarmInner.md) |  | [optional] 
**replicas** | **float** |  | [optional] 
**application_status** | **str** |  | [optional] 
**build_type** | **str** |  | [optional] 
**railpack_version** | **str** |  | [optional] 
**heroku_version** | **str** |  | [optional] 
**publish_directory** | **str** |  | [optional] 
**is_static_spa** | **bool** |  | [optional] 
**create_env_file** | **bool** |  | [optional] 
**created_at** | **str** |  | [optional] 
**registry_id** | **str** |  | [optional] 
**rollback_registry_id** | **str** |  | [optional] 
**environment_id** | **str** |  | [optional] 
**github_id** | **str** |  | [optional] 
**gitlab_id** | **str** |  | [optional] 
**gitea_id** | **str** |  | [optional] 
**bitbucket_id** | **str** |  | [optional] 
**build_server_id** | **str** |  | [optional] 
**build_registry_id** | **str** |  | [optional] 

## Example

```python
from dokploy_client.models.application_update_request import ApplicationUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationUpdateRequest from a JSON string
application_update_request_instance = ApplicationUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(ApplicationUpdateRequest.to_json())

# convert the object into a dict
application_update_request_dict = application_update_request_instance.to_dict()
# create an instance of ApplicationUpdateRequest from a dict
application_update_request_from_dict = ApplicationUpdateRequest.from_dict(application_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


