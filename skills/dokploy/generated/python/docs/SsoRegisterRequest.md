# SsoRegisterRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_id** | **str** |  | 
**issuer** | **str** |  | 
**domains** | **List[str]** |  | 
**oidc_config** | [**SsoRegisterRequestOidcConfig**](SsoRegisterRequestOidcConfig.md) |  | [optional] 
**saml_config** | [**SsoRegisterRequestSamlConfig**](SsoRegisterRequestSamlConfig.md) |  | [optional] 
**organization_id** | **str** |  | [optional] 
**override_user_info** | **bool** |  | [optional] [default to False]

## Example

```python
from dokploy_client.models.sso_register_request import SsoRegisterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SsoRegisterRequest from a JSON string
sso_register_request_instance = SsoRegisterRequest.from_json(json)
# print the JSON string representation of the object
print(SsoRegisterRequest.to_json())

# convert the object into a dict
sso_register_request_dict = sso_register_request_instance.to_dict()
# create an instance of SsoRegisterRequest from a dict
sso_register_request_from_dict = SsoRegisterRequest.from_dict(sso_register_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


