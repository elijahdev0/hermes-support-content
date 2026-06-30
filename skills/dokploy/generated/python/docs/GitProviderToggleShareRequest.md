# GitProviderToggleShareRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**git_provider_id** | **str** |  | 
**shared_with_organization** | **bool** |  | 

## Example

```python
from dokploy_client.models.git_provider_toggle_share_request import GitProviderToggleShareRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GitProviderToggleShareRequest from a JSON string
git_provider_toggle_share_request_instance = GitProviderToggleShareRequest.from_json(json)
# print the JSON string representation of the object
print(GitProviderToggleShareRequest.to_json())

# convert the object into a dict
git_provider_toggle_share_request_dict = git_provider_toggle_share_request_instance.to_dict()
# create an instance of GitProviderToggleShareRequest from a dict
git_provider_toggle_share_request_from_dict = GitProviderToggleShareRequest.from_dict(git_provider_toggle_share_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


