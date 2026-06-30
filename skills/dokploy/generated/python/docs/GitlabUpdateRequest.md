# GitlabUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **str** |  | [optional] 
**secret** | **str** |  | [optional] 
**group_name** | **str** |  | [optional] 
**redirect_uri** | **str** |  | [optional] 
**name** | **str** |  | 
**gitlab_id** | **str** |  | 
**gitlab_url** | **str** |  | 
**git_provider_id** | **str** |  | 
**gitlab_internal_url** | **str** |  | [optional] 

## Example

```python
from dokploy_client.models.gitlab_update_request import GitlabUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GitlabUpdateRequest from a JSON string
gitlab_update_request_instance = GitlabUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(GitlabUpdateRequest.to_json())

# convert the object into a dict
gitlab_update_request_dict = gitlab_update_request_instance.to_dict()
# create an instance of GitlabUpdateRequest from a dict
gitlab_update_request_from_dict = GitlabUpdateRequest.from_dict(gitlab_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


