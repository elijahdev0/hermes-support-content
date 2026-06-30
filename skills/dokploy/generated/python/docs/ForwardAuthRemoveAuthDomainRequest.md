# ForwardAuthRemoveAuthDomainRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_id** | **str** |  | 

## Example

```python
from dokploy_client.models.forward_auth_remove_auth_domain_request import ForwardAuthRemoveAuthDomainRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ForwardAuthRemoveAuthDomainRequest from a JSON string
forward_auth_remove_auth_domain_request_instance = ForwardAuthRemoveAuthDomainRequest.from_json(json)
# print the JSON string representation of the object
print(ForwardAuthRemoveAuthDomainRequest.to_json())

# convert the object into a dict
forward_auth_remove_auth_domain_request_dict = forward_auth_remove_auth_domain_request_instance.to_dict()
# create an instance of ForwardAuthRemoveAuthDomainRequest from a dict
forward_auth_remove_auth_domain_request_from_dict = ForwardAuthRemoveAuthDomainRequest.from_dict(forward_auth_remove_auth_domain_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


