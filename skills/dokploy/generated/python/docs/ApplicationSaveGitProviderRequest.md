# ApplicationSaveGitProviderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **str** |  | 
**custom_git_build_path** | **str** |  | 
**custom_git_url** | **str** |  | 
**watch_paths** | **List[str]** |  | 
**enable_submodules** | **bool** |  | [optional] 
**custom_git_branch** | **str** |  | 
**custom_git_ssh_key_id** | **str** |  | [optional] 

## Example

```python
from dokploy_client.models.application_save_git_provider_request import ApplicationSaveGitProviderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationSaveGitProviderRequest from a JSON string
application_save_git_provider_request_instance = ApplicationSaveGitProviderRequest.from_json(json)
# print the JSON string representation of the object
print(ApplicationSaveGitProviderRequest.to_json())

# convert the object into a dict
application_save_git_provider_request_dict = application_save_git_provider_request_instance.to_dict()
# create an instance of ApplicationSaveGitProviderRequest from a dict
application_save_git_provider_request_from_dict = ApplicationSaveGitProviderRequest.from_dict(application_save_git_provider_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


