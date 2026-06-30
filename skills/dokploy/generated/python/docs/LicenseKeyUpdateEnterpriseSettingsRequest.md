# LicenseKeyUpdateEnterpriseSettingsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_enterprise_features** | **bool** |  | [optional] 

## Example

```python
from dokploy_client.models.license_key_update_enterprise_settings_request import LicenseKeyUpdateEnterpriseSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseKeyUpdateEnterpriseSettingsRequest from a JSON string
license_key_update_enterprise_settings_request_instance = LicenseKeyUpdateEnterpriseSettingsRequest.from_json(json)
# print the JSON string representation of the object
print(LicenseKeyUpdateEnterpriseSettingsRequest.to_json())

# convert the object into a dict
license_key_update_enterprise_settings_request_dict = license_key_update_enterprise_settings_request_instance.to_dict()
# create an instance of LicenseKeyUpdateEnterpriseSettingsRequest from a dict
license_key_update_enterprise_settings_request_from_dict = LicenseKeyUpdateEnterpriseSettingsRequest.from_dict(license_key_update_enterprise_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


