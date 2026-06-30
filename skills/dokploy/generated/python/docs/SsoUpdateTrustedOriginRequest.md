# SsoUpdateTrustedOriginRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**old_origin** | **str** |  | 
**new_origin** | **str** |  | 

## Example

```python
from dokploy_client.models.sso_update_trusted_origin_request import SsoUpdateTrustedOriginRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SsoUpdateTrustedOriginRequest from a JSON string
sso_update_trusted_origin_request_instance = SsoUpdateTrustedOriginRequest.from_json(json)
# print the JSON string representation of the object
print(SsoUpdateTrustedOriginRequest.to_json())

# convert the object into a dict
sso_update_trusted_origin_request_dict = sso_update_trusted_origin_request_instance.to_dict()
# create an instance of SsoUpdateTrustedOriginRequest from a dict
sso_update_trusted_origin_request_from_dict = SsoUpdateTrustedOriginRequest.from_dict(sso_update_trusted_origin_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


