# GiteaTestConnectionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gitea_id** | **str** |  | [optional] 
**organization_name** | **str** |  | [optional] 

## Example

```python
from dokploy_client.models.gitea_test_connection_request import GiteaTestConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GiteaTestConnectionRequest from a JSON string
gitea_test_connection_request_instance = GiteaTestConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(GiteaTestConnectionRequest.to_json())

# convert the object into a dict
gitea_test_connection_request_dict = gitea_test_connection_request_instance.to_dict()
# create an instance of GiteaTestConnectionRequest from a dict
gitea_test_connection_request_from_dict = GiteaTestConnectionRequest.from_dict(gitea_test_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


