# GithubUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**github_id** | **str** |  | 
**name** | **str** |  | 
**git_provider_id** | **str** |  | 
**github_app_name** | **str** |  | 

## Example

```python
from dokploy_client.models.github_update_request import GithubUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GithubUpdateRequest from a JSON string
github_update_request_instance = GithubUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(GithubUpdateRequest.to_json())

# convert the object into a dict
github_update_request_dict = github_update_request_instance.to_dict()
# create an instance of GithubUpdateRequest from a dict
github_update_request_from_dict = GithubUpdateRequest.from_dict(github_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


