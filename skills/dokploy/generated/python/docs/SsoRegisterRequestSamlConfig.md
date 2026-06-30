# SsoRegisterRequestSamlConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry_point** | **str** |  | 
**cert** | **str** |  | 
**callback_url** | **str** |  | 
**audience** | **str** |  | [optional] 
**idp_metadata** | [**SsoRegisterRequestSamlConfigIdpMetadata**](SsoRegisterRequestSamlConfigIdpMetadata.md) |  | [optional] 
**sp_metadata** | [**SsoRegisterRequestSamlConfigSpMetadata**](SsoRegisterRequestSamlConfigSpMetadata.md) |  | 
**want_assertions_signed** | **bool** |  | [optional] 
**authn_requests_signed** | **bool** |  | [optional] 
**signature_algorithm** | **str** |  | [optional] 
**digest_algorithm** | **str** |  | [optional] 
**identifier_format** | **str** |  | [optional] 
**private_key** | **str** |  | [optional] 
**decryption_pvk** | **str** |  | [optional] 
**additional_params** | **Dict[str, object]** |  | [optional] 
**mapping** | [**SsoRegisterRequestSamlConfigMapping**](SsoRegisterRequestSamlConfigMapping.md) |  | [optional] 

## Example

```python
from dokploy_client.models.sso_register_request_saml_config import SsoRegisterRequestSamlConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SsoRegisterRequestSamlConfig from a JSON string
sso_register_request_saml_config_instance = SsoRegisterRequestSamlConfig.from_json(json)
# print the JSON string representation of the object
print(SsoRegisterRequestSamlConfig.to_json())

# convert the object into a dict
sso_register_request_saml_config_dict = sso_register_request_saml_config_instance.to_dict()
# create an instance of SsoRegisterRequestSamlConfig from a dict
sso_register_request_saml_config_from_dict = SsoRegisterRequestSamlConfig.from_dict(sso_register_request_saml_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


