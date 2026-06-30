# SsoAddTrustedOriginRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**origin** | **str** |  | 

## Example

```python
from dokploy_client.models.sso_add_trusted_origin_request import SsoAddTrustedOriginRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SsoAddTrustedOriginRequest from a JSON string
sso_add_trusted_origin_request_instance = SsoAddTrustedOriginRequest.from_json(json)
# print the JSON string representation of the object
print(SsoAddTrustedOriginRequest.to_json())

# convert the object into a dict
sso_add_trusted_origin_request_dict = sso_add_trusted_origin_request_instance.to_dict()
# create an instance of SsoAddTrustedOriginRequest from a dict
sso_add_trusted_origin_request_from_dict = SsoAddTrustedOriginRequest.from_dict(sso_add_trusted_origin_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


