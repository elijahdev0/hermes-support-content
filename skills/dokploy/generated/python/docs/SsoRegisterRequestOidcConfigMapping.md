# SsoRegisterRequestOidcConfigMapping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**email** | **str** |  | 
**email_verified** | **str** |  | [optional] 
**name** | **str** |  | 
**image** | **str** |  | [optional] 
**extra_fields** | **Dict[str, object]** |  | [optional] 

## Example

```python
from dokploy_client.models.sso_register_request_oidc_config_mapping import SsoRegisterRequestOidcConfigMapping

# TODO update the JSON string below
json = "{}"
# create an instance of SsoRegisterRequestOidcConfigMapping from a JSON string
sso_register_request_oidc_config_mapping_instance = SsoRegisterRequestOidcConfigMapping.from_json(json)
# print the JSON string representation of the object
print(SsoRegisterRequestOidcConfigMapping.to_json())

# convert the object into a dict
sso_register_request_oidc_config_mapping_dict = sso_register_request_oidc_config_mapping_instance.to_dict()
# create an instance of SsoRegisterRequestOidcConfigMapping from a dict
sso_register_request_oidc_config_mapping_from_dict = SsoRegisterRequestOidcConfigMapping.from_dict(sso_register_request_oidc_config_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


