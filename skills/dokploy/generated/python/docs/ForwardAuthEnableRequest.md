# ForwardAuthEnableRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_id** | **str** |  | 

## Example

```python
from dokploy_client.models.forward_auth_enable_request import ForwardAuthEnableRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ForwardAuthEnableRequest from a JSON string
forward_auth_enable_request_instance = ForwardAuthEnableRequest.from_json(json)
# print the JSON string representation of the object
print(ForwardAuthEnableRequest.to_json())

# convert the object into a dict
forward_auth_enable_request_dict = forward_auth_enable_request_instance.to_dict()
# create an instance of ForwardAuthEnableRequest from a dict
forward_auth_enable_request_from_dict = ForwardAuthEnableRequest.from_dict(forward_auth_enable_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


