# SsoUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_id** | **str** |  | 
**issuer** | **str** |  | 
**domains** | **List[str]** |  | 
**oidc_config** | [**SsoUpdateRequestOidcConfig**](SsoUpdateRequestOidcConfig.md) |  | [optional] 
**saml_config** | [**SsoUpdateRequestSamlConfig**](SsoUpdateRequestSamlConfig.md) |  | [optional] 
**organization_id** | **str** |  | [optional] 
**override_user_info** | **bool** |  | [optional] [default to False]

## Example

```python
from dokploy_client.models.sso_update_request import SsoUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SsoUpdateRequest from a JSON string
sso_update_request_instance = SsoUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(SsoUpdateRequest.to_json())

# convert the object into a dict
sso_update_request_dict = sso_update_request_instance.to_dict()
# create an instance of SsoUpdateRequest from a dict
sso_update_request_from_dict = SsoUpdateRequest.from_dict(sso_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


