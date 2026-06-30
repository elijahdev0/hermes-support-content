# ServerCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | 
**ip_address** | **str** |  | 
**port** | **float** |  | 
**username** | **str** |  | 
**ssh_key_id** | **str** |  | 
**server_type** | **str** |  | 
**enable_docker_cleanup** | **bool** |  | [optional] [default to True]

## Example

```python
from dokploy_client.models.server_create_request import ServerCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServerCreateRequest from a JSON string
server_create_request_instance = ServerCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ServerCreateRequest.to_json())

# convert the object into a dict
server_create_request_dict = server_create_request_instance.to_dict()
# create an instance of ServerCreateRequest from a dict
server_create_request_from_dict = ServerCreateRequest.from_dict(server_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


