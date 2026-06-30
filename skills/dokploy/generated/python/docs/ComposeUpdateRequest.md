# ComposeUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compose_id** | **str** |  | 
**name** | **str** |  | [optional] 
**app_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**env** | **str** |  | [optional] 
**compose_file** | **str** |  | [optional] 
**refresh_token** | **str** |  | [optional] 
**source_type** | **str** |  | [optional] 
**compose_type** | **str** |  | [optional] 
**repository** | **str** |  | [optional] 
**owner** | **str** |  | [optional] 
**branch** | **str** |  | [optional] 
**auto_deploy** | **bool** |  | [optional] 
**gitlab_project_id** | **float** |  | [optional] 
**gitlab_repository** | **str** |  | [optional] 
**gitlab_owner** | **str** |  | [optional] 
**gitlab_branch** | **str** |  | [optional] 
**gitlab_path_namespace** | **str** |  | [optional] 
**bitbucket_repository** | **str** |  | [optional] 
**bitbucket_repository_slug** | **str** |  | [optional] 
**bitbucket_owner** | **str** |  | [optional] 
**bitbucket_branch** | **str** |  | [optional] 
**gitea_repository** | **str** |  | [optional] 
**gitea_owner** | **str** |  | [optional] 
**gitea_branch** | **str** |  | [optional] 
**custom_git_url** | **str** |  | [optional] 
**custom_git_branch** | **str** |  | [optional] 
**custom_git_ssh_key_id** | **str** |  | [optional] 
**command** | **str** |  | [optional] 
**enable_submodules** | **bool** |  | [optional] 
**compose_path** | **str** |  | [optional] 
**suffix** | **str** |  | [optional] 
**randomize** | **bool** |  | [optional] 
**isolated_deployment** | **bool** |  | [optional] 
**isolated_deployments_volume** | **bool** |  | [optional] 
**trigger_type** | **str** |  | [optional] 
**compose_status** | **str** |  | [optional] 
**environment_id** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**watch_paths** | **List[str]** |  | [optional] 
**github_id** | **str** |  | [optional] 
**gitlab_id** | **str** |  | [optional] 
**bitbucket_id** | **str** |  | [optional] 
**gitea_id** | **str** |  | [optional] 

## Example

```python
from dokploy_client.models.compose_update_request import ComposeUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ComposeUpdateRequest from a JSON string
compose_update_request_instance = ComposeUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(ComposeUpdateRequest.to_json())

# convert the object into a dict
compose_update_request_dict = compose_update_request_instance.to_dict()
# create an instance of ComposeUpdateRequest from a dict
compose_update_request_from_dict = ComposeUpdateRequest.from_dict(compose_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


