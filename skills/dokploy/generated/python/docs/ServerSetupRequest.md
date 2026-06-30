# ServerSetupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_id** | **str** |  | 

## Example

```python
from dokploy_client.models.server_setup_request import ServerSetupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServerSetupRequest from a JSON string
server_setup_request_instance = ServerSetupRequest.from_json(json)
# print the JSON string representation of the object
print(ServerSetupRequest.to_json())

# convert the object into a dict
server_setup_request_dict = server_setup_request_instance.to_dict()
# create an instance of ServerSetupRequest from a dict
server_setup_request_from_dict = ServerSetupRequest.from_dict(server_setup_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


