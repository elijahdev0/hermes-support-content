# GithubTestConnectionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**github_id** | **str** |  | 

## Example

```python
from dokploy_client.models.github_test_connection_request import GithubTestConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GithubTestConnectionRequest from a JSON string
github_test_connection_request_instance = GithubTestConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(GithubTestConnectionRequest.to_json())

# convert the object into a dict
github_test_connection_request_dict = github_test_connection_request_instance.to_dict()
# create an instance of GithubTestConnectionRequest from a dict
github_test_connection_request_from_dict = GithubTestConnectionRequest.from_dict(github_test_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


