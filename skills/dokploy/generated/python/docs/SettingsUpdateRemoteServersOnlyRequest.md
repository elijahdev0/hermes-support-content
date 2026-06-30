# SettingsUpdateRemoteServersOnlyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remote_servers_only** | **bool** |  | 

## Example

```python
from dokploy_client.models.settings_update_remote_servers_only_request import SettingsUpdateRemoteServersOnlyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SettingsUpdateRemoteServersOnlyRequest from a JSON string
settings_update_remote_servers_only_request_instance = SettingsUpdateRemoteServersOnlyRequest.from_json(json)
# print the JSON string representation of the object
print(SettingsUpdateRemoteServersOnlyRequest.to_json())

# convert the object into a dict
settings_update_remote_servers_only_request_dict = settings_update_remote_servers_only_request_instance.to_dict()
# create an instance of SettingsUpdateRemoteServersOnlyRequest from a dict
settings_update_remote_servers_only_request_from_dict = SettingsUpdateRemoteServersOnlyRequest.from_dict(settings_update_remote_servers_only_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


