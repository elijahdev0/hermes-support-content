# ForwardAuthSetAuthDomainRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_id** | **str** |  | 
**auth_domain** | **str** |  | 
**https** | **bool** |  | [optional] [default to True]
**certificate_type** | **str** |  | [optional] [default to 'letsencrypt']
**custom_cert_resolver** | **str** |  | [optional] 

## Example

```python
from dokploy_client.models.forward_auth_set_auth_domain_request import ForwardAuthSetAuthDomainRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ForwardAuthSetAuthDomainRequest from a JSON string
forward_auth_set_auth_domain_request_instance = ForwardAuthSetAuthDomainRequest.from_json(json)
# print the JSON string representation of the object
print(ForwardAuthSetAuthDomainRequest.to_json())

# convert the object into a dict
forward_auth_set_auth_domain_request_dict = forward_auth_set_auth_domain_request_instance.to_dict()
# create an instance of ForwardAuthSetAuthDomainRequest from a dict
forward_auth_set_auth_domain_request_from_dict = ForwardAuthSetAuthDomainRequest.from_dict(forward_auth_set_auth_domain_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


