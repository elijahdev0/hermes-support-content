# ServerRemoveRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_id** | **str** |  | 

## Example

```python
from dokploy_client.models.server_remove_request import ServerRemoveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServerRemoveRequest from a JSON string
server_remove_request_instance = ServerRemoveRequest.from_json(json)
# print the JSON string representation of the object
print(ServerRemoveRequest.to_json())

# convert the object into a dict
server_remove_request_dict = server_remove_request_instance.to_dict()
# create an instance of ServerRemoveRequest from a dict
server_remove_request_from_dict = ServerRemoveRequest.from_dict(server_remove_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


