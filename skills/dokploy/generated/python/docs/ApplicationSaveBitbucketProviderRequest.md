# ApplicationSaveBitbucketProviderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bitbucket_build_path** | **str** |  | 
**bitbucket_owner** | **str** |  | 
**bitbucket_repository** | **str** |  | 
**bitbucket_repository_slug** | **str** |  | 
**bitbucket_id** | **str** |  | 
**application_id** | **str** |  | 
**bitbucket_branch** | **str** |  | 
**enable_submodules** | **bool** |  | [optional] 
**watch_paths** | **List[str]** |  | [optional] 

## Example

```python
from dokploy_client.models.application_save_bitbucket_provider_request import ApplicationSaveBitbucketProviderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationSaveBitbucketProviderRequest from a JSON string
application_save_bitbucket_provider_request_instance = ApplicationSaveBitbucketProviderRequest.from_json(json)
# print the JSON string representation of the object
print(ApplicationSaveBitbucketProviderRequest.to_json())

# convert the object into a dict
application_save_bitbucket_provider_request_dict = application_save_bitbucket_provider_request_instance.to_dict()
# create an instance of ApplicationSaveBitbucketProviderRequest from a dict
application_save_bitbucket_provider_request_from_dict = ApplicationSaveBitbucketProviderRequest.from_dict(application_save_bitbucket_provider_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


