# GitProviderRemoveRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**git_provider_id** | **str** |  | 

## Example

```python
from dokploy_client.models.git_provider_remove_request import GitProviderRemoveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GitProviderRemoveRequest from a JSON string
git_provider_remove_request_instance = GitProviderRemoveRequest.from_json(json)
# print the JSON string representation of the object
print(GitProviderRemoveRequest.to_json())

# convert the object into a dict
git_provider_remove_request_dict = git_provider_remove_request_instance.to_dict()
# create an instance of GitProviderRemoveRequest from a dict
git_provider_remove_request_from_dict = GitProviderRemoveRequest.from_dict(git_provider_remove_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


