# SettingsUpdateLogCleanupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cron_expression** | **str** |  | 

## Example

```python
from dokploy_client.models.settings_update_log_cleanup_request import SettingsUpdateLogCleanupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SettingsUpdateLogCleanupRequest from a JSON string
settings_update_log_cleanup_request_instance = SettingsUpdateLogCleanupRequest.from_json(json)
# print the JSON string representation of the object
print(SettingsUpdateLogCleanupRequest.to_json())

# convert the object into a dict
settings_update_log_cleanup_request_dict = settings_update_log_cleanup_request_instance.to_dict()
# create an instance of SettingsUpdateLogCleanupRequest from a dict
settings_update_log_cleanup_request_from_dict = SettingsUpdateLogCleanupRequest.from_dict(settings_update_log_cleanup_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


