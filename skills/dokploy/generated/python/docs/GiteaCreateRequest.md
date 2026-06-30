# GiteaCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gitea_id** | **str** |  | [optional] 
**gitea_url** | **str** |  | 
**gitea_internal_url** | **str** |  | [optional] 
**redirect_uri** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**git_provider_id** | **str** |  | [optional] 
**access_token** | **str** |  | [optional] 
**refresh_token** | **str** |  | [optional] 
**expires_at** | **float** |  | [optional] 
**scopes** | **str** |  | [optional] 
**last_authenticated_at** | **float** |  | [optional] 
**name** | **str** |  | 
**gitea_username** | **str** |  | [optional] 
**organization_name** | **str** |  | [optional] 

## Example

```python
from dokploy_client.models.gitea_create_request import GiteaCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GiteaCreateRequest from a JSON string
gitea_create_request_instance = GiteaCreateRequest.from_json(json)
# print the JSON string representation of the object
print(GiteaCreateRequest.to_json())

# convert the object into a dict
gitea_create_request_dict = gitea_create_request_instance.to_dict()
# create an instance of GiteaCreateRequest from a dict
gitea_create_request_from_dict = GiteaCreateRequest.from_dict(gitea_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


