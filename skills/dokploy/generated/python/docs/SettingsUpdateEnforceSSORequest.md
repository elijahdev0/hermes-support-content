# SettingsUpdateEnforceSSORequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enforce_sso** | **bool** |  | 

## Example

```python
from dokploy_client.models.settings_update_enforce_sso_request import SettingsUpdateEnforceSSORequest

# TODO update the JSON string below
json = "{}"
# create an instance of SettingsUpdateEnforceSSORequest from a JSON string
settings_update_enforce_sso_request_instance = SettingsUpdateEnforceSSORequest.from_json(json)
# print the JSON string representation of the object
print(SettingsUpdateEnforceSSORequest.to_json())

# convert the object into a dict
settings_update_enforce_sso_request_dict = settings_update_enforce_sso_request_instance.to_dict()
# create an instance of SettingsUpdateEnforceSSORequest from a dict
settings_update_enforce_sso_request_from_dict = SettingsUpdateEnforceSSORequest.from_dict(settings_update_enforce_sso_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


