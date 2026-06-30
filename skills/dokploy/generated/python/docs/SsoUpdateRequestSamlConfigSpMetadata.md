# SsoUpdateRequestSamlConfigSpMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **str** |  | [optional] 
**entity_id** | **str** |  | [optional] 
**binding** | **str** |  | [optional] 
**private_key** | **str** |  | [optional] 
**private_key_pass** | **str** |  | [optional] 
**is_assertion_encrypted** | **bool** |  | [optional] 
**enc_private_key** | **str** |  | [optional] 
**enc_private_key_pass** | **str** |  | [optional] 

## Example

```python
from dokploy_client.models.sso_update_request_saml_config_sp_metadata import SsoUpdateRequestSamlConfigSpMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of SsoUpdateRequestSamlConfigSpMetadata from a JSON string
sso_update_request_saml_config_sp_metadata_instance = SsoUpdateRequestSamlConfigSpMetadata.from_json(json)
# print the JSON string representation of the object
print(SsoUpdateRequestSamlConfigSpMetadata.to_json())

# convert the object into a dict
sso_update_request_saml_config_sp_metadata_dict = sso_update_request_saml_config_sp_metadata_instance.to_dict()
# create an instance of SsoUpdateRequestSamlConfigSpMetadata from a dict
sso_update_request_saml_config_sp_metadata_from_dict = SsoUpdateRequestSamlConfigSpMetadata.from_dict(sso_update_request_saml_config_sp_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


