# SsoDeleteProviderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_id** | **str** |  | 

## Example

```python
from dokploy_client.models.sso_delete_provider_request import SsoDeleteProviderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SsoDeleteProviderRequest from a JSON string
sso_delete_provider_request_instance = SsoDeleteProviderRequest.from_json(json)
# print the JSON string representation of the object
print(SsoDeleteProviderRequest.to_json())

# convert the object into a dict
sso_delete_provider_request_dict = sso_delete_provider_request_instance.to_dict()
# create an instance of SsoDeleteProviderRequest from a dict
sso_delete_provider_request_from_dict = SsoDeleteProviderRequest.from_dict(sso_delete_provider_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


