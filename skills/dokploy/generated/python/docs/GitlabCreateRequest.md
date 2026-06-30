# GitlabCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **str** |  | [optional] 
**secret** | **str** |  | [optional] 
**group_name** | **str** |  | [optional] 
**git_provider_id** | **str** |  | [optional] 
**redirect_uri** | **str** |  | [optional] 
**auth_id** | **str** |  | 
**name** | **str** |  | 
**gitlab_url** | **str** |  | 
**gitlab_internal_url** | **str** |  | [optional] 

## Example

```python
from dokploy_client.models.gitlab_create_request import GitlabCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GitlabCreateRequest from a JSON string
gitlab_create_request_instance = GitlabCreateRequest.from_json(json)
# print the JSON string representation of the object
print(GitlabCreateRequest.to_json())

# convert the object into a dict
gitlab_create_request_dict = gitlab_create_request_instance.to_dict()
# create an instance of GitlabCreateRequest from a dict
gitlab_create_request_from_dict = GitlabCreateRequest.from_dict(gitlab_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


