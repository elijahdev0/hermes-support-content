# GitlabTestConnectionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gitlab_id** | **str** |  | 
**group_name** | **str** |  | [optional] 

## Example

```python
from dokploy_client.models.gitlab_test_connection_request import GitlabTestConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GitlabTestConnectionRequest from a JSON string
gitlab_test_connection_request_instance = GitlabTestConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(GitlabTestConnectionRequest.to_json())

# convert the object into a dict
gitlab_test_connection_request_dict = gitlab_test_connection_request_instance.to_dict()
# create an instance of GitlabTestConnectionRequest from a dict
gitlab_test_connection_request_from_dict = GitlabTestConnectionRequest.from_dict(gitlab_test_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


