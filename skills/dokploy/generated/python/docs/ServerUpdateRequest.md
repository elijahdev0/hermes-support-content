# ServerUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | 
**server_id** | **str** |  | 
**ip_address** | **str** |  | 
**port** | **float** |  | 
**username** | **str** |  | 
**ssh_key_id** | **str** |  | 
**server_type** | **str** |  | 
**enable_docker_cleanup** | **bool** |  | [optional] [default to True]
**command** | **str** |  | [optional] 

## Example

```python
from dokploy_client.models.server_update_request import ServerUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServerUpdateRequest from a JSON string
server_update_request_instance = ServerUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(ServerUpdateRequest.to_json())

# convert the object into a dict
server_update_request_dict = server_update_request_instance.to_dict()
# create an instance of ServerUpdateRequest from a dict
server_update_request_from_dict = ServerUpdateRequest.from_dict(server_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


