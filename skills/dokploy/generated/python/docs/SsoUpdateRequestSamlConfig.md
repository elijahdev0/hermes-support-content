# SsoUpdateRequestSamlConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry_point** | **str** |  | 
**cert** | **str** |  | 
**callback_url** | **str** |  | 
**audience** | **str** |  | [optional] 
**idp_metadata** | [**SsoUpdateRequestSamlConfigIdpMetadata**](SsoUpdateRequestSamlConfigIdpMetadata.md) |  | [optional] 
**sp_metadata** | [**SsoUpdateRequestSamlConfigSpMetadata**](SsoUpdateRequestSamlConfigSpMetadata.md) |  | 
**want_assertions_signed** | **bool** |  | [optional] 
**authn_requests_signed** | **bool** |  | [optional] 
**signature_algorithm** | **str** |  | [optional] 
**digest_algorithm** | **str** |  | [optional] 
**identifier_format** | **str** |  | [optional] 
**private_key** | **str** |  | [optional] 
**decryption_pvk** | **str** |  | [optional] 
**additional_params** | **Dict[str, object]** |  | [optional] 
**mapping** | [**SsoUpdateRequestSamlConfigMapping**](SsoUpdateRequestSamlConfigMapping.md) |  | [optional] 

## Example

```python
from dokploy_client.models.sso_update_request_saml_config import SsoUpdateRequestSamlConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SsoUpdateRequestSamlConfig from a JSON string
sso_update_request_saml_config_instance = SsoUpdateRequestSamlConfig.from_json(json)
# print the JSON string representation of the object
print(SsoUpdateRequestSamlConfig.to_json())

# convert the object into a dict
sso_update_request_saml_config_dict = sso_update_request_saml_config_instance.to_dict()
# create an instance of SsoUpdateRequestSamlConfig from a dict
sso_update_request_saml_config_from_dict = SsoUpdateRequestSamlConfig.from_dict(sso_update_request_saml_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


