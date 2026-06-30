# SsoRegisterRequestOidcConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** |  | 
**client_secret** | **str** |  | 
**authorization_endpoint** | **str** |  | [optional] 
**token_endpoint** | **str** |  | [optional] 
**user_info_endpoint** | **str** |  | [optional] 
**token_endpoint_authentication** | **str** |  | [optional] 
**jwks_endpoint** | **str** |  | [optional] 
**discovery_endpoint** | **str** |  | [optional] 
**skip_discovery** | **bool** |  | [optional] 
**scopes** | **List[str]** |  | [optional] 
**pkce** | **bool** |  | [optional] [default to True]
**mapping** | [**SsoRegisterRequestOidcConfigMapping**](SsoRegisterRequestOidcConfigMapping.md) |  | [optional] 

## Example

```python
from dokploy_client.models.sso_register_request_oidc_config import SsoRegisterRequestOidcConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SsoRegisterRequestOidcConfig from a JSON string
sso_register_request_oidc_config_instance = SsoRegisterRequestOidcConfig.from_json(json)
# print the JSON string representation of the object
print(SsoRegisterRequestOidcConfig.to_json())

# convert the object into a dict
sso_register_request_oidc_config_dict = sso_register_request_oidc_config_instance.to_dict()
# create an instance of SsoRegisterRequestOidcConfig from a dict
sso_register_request_oidc_config_from_dict = SsoRegisterRequestOidcConfig.from_dict(sso_register_request_oidc_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


