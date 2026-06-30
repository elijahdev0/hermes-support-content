# SsoUpdateRequestOidcConfig


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
**mapping** | [**SsoUpdateRequestOidcConfigMapping**](SsoUpdateRequestOidcConfigMapping.md) |  | [optional] 

## Example

```python
from dokploy_client.models.sso_update_request_oidc_config import SsoUpdateRequestOidcConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SsoUpdateRequestOidcConfig from a JSON string
sso_update_request_oidc_config_instance = SsoUpdateRequestOidcConfig.from_json(json)
# print the JSON string representation of the object
print(SsoUpdateRequestOidcConfig.to_json())

# convert the object into a dict
sso_update_request_oidc_config_dict = sso_update_request_oidc_config_instance.to_dict()
# create an instance of SsoUpdateRequestOidcConfig from a dict
sso_update_request_oidc_config_from_dict = SsoUpdateRequestOidcConfig.from_dict(sso_update_request_oidc_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


