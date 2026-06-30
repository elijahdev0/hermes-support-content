# ApplicationSaveGitlabProviderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **str** |  | 
**gitlab_build_path** | **str** |  | 
**gitlab_owner** | **str** |  | 
**gitlab_repository** | **str** |  | 
**gitlab_id** | **str** |  | 
**gitlab_project_id** | **float** |  | 
**gitlab_path_namespace** | **str** |  | 
**gitlab_branch** | **str** |  | 
**enable_submodules** | **bool** |  | [optional] 
**watch_paths** | **List[str]** |  | [optional] 

## Example

```python
from dokploy_client.models.application_save_gitlab_provider_request import ApplicationSaveGitlabProviderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationSaveGitlabProviderRequest from a JSON string
application_save_gitlab_provider_request_instance = ApplicationSaveGitlabProviderRequest.from_json(json)
# print the JSON string representation of the object
print(ApplicationSaveGitlabProviderRequest.to_json())

# convert the object into a dict
application_save_gitlab_provider_request_dict = application_save_gitlab_provider_request_instance.to_dict()
# create an instance of ApplicationSaveGitlabProviderRequest from a dict
application_save_gitlab_provider_request_from_dict = ApplicationSaveGitlabProviderRequest.from_dict(application_save_gitlab_provider_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


