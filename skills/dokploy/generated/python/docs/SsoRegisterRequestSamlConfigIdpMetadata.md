# SsoRegisterRequestSamlConfigIdpMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **str** |  | [optional] 
**entity_id** | **str** |  | [optional] 
**cert** | **str** |  | [optional] 
**private_key** | **str** |  | [optional] 
**private_key_pass** | **str** |  | [optional] 
**is_assertion_encrypted** | **bool** |  | [optional] 
**enc_private_key** | **str** |  | [optional] 
**enc_private_key_pass** | **str** |  | [optional] 
**single_sign_on_service** | [**List[SsoRegisterRequestSamlConfigIdpMetadataSingleSignOnServiceInner]**](SsoRegisterRequestSamlConfigIdpMetadataSingleSignOnServiceInner.md) |  | [optional] 

## Example

```python
from dokploy_client.models.sso_register_request_saml_config_idp_metadata import SsoRegisterRequestSamlConfigIdpMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of SsoRegisterRequestSamlConfigIdpMetadata from a JSON string
sso_register_request_saml_config_idp_metadata_instance = SsoRegisterRequestSamlConfigIdpMetadata.from_json(json)
# print the JSON string representation of the object
print(SsoRegisterRequestSamlConfigIdpMetadata.to_json())

# convert the object into a dict
sso_register_request_saml_config_idp_metadata_dict = sso_register_request_saml_config_idp_metadata_instance.to_dict()
# create an instance of SsoRegisterRequestSamlConfigIdpMetadata from a dict
sso_register_request_saml_config_idp_metadata_from_dict = SsoRegisterRequestSamlConfigIdpMetadata.from_dict(sso_register_request_saml_config_idp_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


