# SsoRemoveTrustedOriginRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**origin** | **str** |  | 

## Example

```python
from dokploy_client.models.sso_remove_trusted_origin_request import SsoRemoveTrustedOriginRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SsoRemoveTrustedOriginRequest from a JSON string
sso_remove_trusted_origin_request_instance = SsoRemoveTrustedOriginRequest.from_json(json)
# print the JSON string representation of the object
print(SsoRemoveTrustedOriginRequest.to_json())

# convert the object into a dict
sso_remove_trusted_origin_request_dict = sso_remove_trusted_origin_request_instance.to_dict()
# create an instance of SsoRemoveTrustedOriginRequest from a dict
sso_remove_trusted_origin_request_from_dict = SsoRemoveTrustedOriginRequest.from_dict(sso_remove_trusted_origin_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


