# ForwardAuthDeployOnServerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_id** | **str** |  | 
**provider_id** | **str** |  | 

## Example

```python
from dokploy_client.models.forward_auth_deploy_on_server_request import ForwardAuthDeployOnServerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ForwardAuthDeployOnServerRequest from a JSON string
forward_auth_deploy_on_server_request_instance = ForwardAuthDeployOnServerRequest.from_json(json)
# print the JSON string representation of the object
print(ForwardAuthDeployOnServerRequest.to_json())

# convert the object into a dict
forward_auth_deploy_on_server_request_dict = forward_auth_deploy_on_server_request_instance.to_dict()
# create an instance of ForwardAuthDeployOnServerRequest from a dict
forward_auth_deploy_on_server_request_from_dict = ForwardAuthDeployOnServerRequest.from_dict(forward_auth_deploy_on_server_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


