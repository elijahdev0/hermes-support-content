# SsoUpdateRequestOidcConfigMapping


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
from dokploy_client.models.sso_update_request_oidc_config_mapping import SsoUpdateRequestOidcConfigMapping

# TODO update the JSON string below
json = "{}"
# create an instance of SsoUpdateRequestOidcConfigMapping from a JSON string
sso_update_request_oidc_config_mapping_instance = SsoUpdateRequestOidcConfigMapping.from_json(json)
# print the JSON string representation of the object
print(SsoUpdateRequestOidcConfigMapping.to_json())

# convert the object into a dict
sso_update_request_oidc_config_mapping_dict = sso_update_request_oidc_config_mapping_instance.to_dict()
# create an instance of SsoUpdateRequestOidcConfigMapping from a dict
sso_update_request_oidc_config_mapping_from_dict = SsoUpdateRequestOidcConfigMapping.from_dict(sso_update_request_oidc_config_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


