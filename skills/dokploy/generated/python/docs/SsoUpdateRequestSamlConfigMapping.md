# SsoUpdateRequestSamlConfigMapping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**email** | **str** |  | 
**email_verified** | **str** |  | [optional] 
**name** | **str** |  | 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**extra_fields** | **Dict[str, object]** |  | [optional] 

## Example

```python
from dokploy_client.models.sso_update_request_saml_config_mapping import SsoUpdateRequestSamlConfigMapping

# TODO update the JSON string below
json = "{}"
# create an instance of SsoUpdateRequestSamlConfigMapping from a JSON string
sso_update_request_saml_config_mapping_instance = SsoUpdateRequestSamlConfigMapping.from_json(json)
# print the JSON string representation of the object
print(SsoUpdateRequestSamlConfigMapping.to_json())

# convert the object into a dict
sso_update_request_saml_config_mapping_dict = sso_update_request_saml_config_mapping_instance.to_dict()
# create an instance of SsoUpdateRequestSamlConfigMapping from a dict
sso_update_request_saml_config_mapping_from_dict = SsoUpdateRequestSamlConfigMapping.from_dict(sso_update_request_saml_config_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


