# ApplicationSaveGiteaProviderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **str** |  | 
**gitea_build_path** | **str** |  | 
**gitea_owner** | **str** |  | 
**gitea_repository** | **str** |  | 
**gitea_id** | **str** |  | 
**gitea_branch** | **str** |  | 
**enable_submodules** | **bool** |  | [optional] 
**watch_paths** | **List[str]** |  | [optional] 

## Example

```python
from dokploy_client.models.application_save_gitea_provider_request import ApplicationSaveGiteaProviderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationSaveGiteaProviderRequest from a JSON string
application_save_gitea_provider_request_instance = ApplicationSaveGiteaProviderRequest.from_json(json)
# print the JSON string representation of the object
print(ApplicationSaveGiteaProviderRequest.to_json())

# convert the object into a dict
application_save_gitea_provider_request_dict = application_save_gitea_provider_request_instance.to_dict()
# create an instance of ApplicationSaveGiteaProviderRequest from a dict
application_save_gitea_provider_request_from_dict = ApplicationSaveGiteaProviderRequest.from_dict(application_save_gitea_provider_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


