# SettingsUpdateServerIpRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_ip** | **str** |  | 

## Example

```python
from dokploy_client.models.settings_update_server_ip_request import SettingsUpdateServerIpRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SettingsUpdateServerIpRequest from a JSON string
settings_update_server_ip_request_instance = SettingsUpdateServerIpRequest.from_json(json)
# print the JSON string representation of the object
print(SettingsUpdateServerIpRequest.to_json())

# convert the object into a dict
settings_update_server_ip_request_dict = settings_update_server_ip_request_instance.to_dict()
# create an instance of SettingsUpdateServerIpRequest from a dict
settings_update_server_ip_request_from_dict = SettingsUpdateServerIpRequest.from_dict(settings_update_server_ip_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


