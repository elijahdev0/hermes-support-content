# SsoUpdateRequestSamlConfigIdpMetadata


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
**single_sign_on_service** | [**List[SsoUpdateRequestSamlConfigIdpMetadataSingleSignOnServiceInner]**](SsoUpdateRequestSamlConfigIdpMetadataSingleSignOnServiceInner.md) |  | [optional] 

## Example

```python
from dokploy_client.models.sso_update_request_saml_config_idp_metadata import SsoUpdateRequestSamlConfigIdpMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of SsoUpdateRequestSamlConfigIdpMetadata from a JSON string
sso_update_request_saml_config_idp_metadata_instance = SsoUpdateRequestSamlConfigIdpMetadata.from_json(json)
# print the JSON string representation of the object
print(SsoUpdateRequestSamlConfigIdpMetadata.to_json())

# convert the object into a dict
sso_update_request_saml_config_idp_metadata_dict = sso_update_request_saml_config_idp_metadata_instance.to_dict()
# create an instance of SsoUpdateRequestSamlConfigIdpMetadata from a dict
sso_update_request_saml_config_idp_metadata_from_dict = SsoUpdateRequestSamlConfigIdpMetadata.from_dict(sso_update_request_saml_config_idp_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


