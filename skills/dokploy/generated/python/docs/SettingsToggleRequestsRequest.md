# SettingsToggleRequestsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** |  | 

## Example

```python
from dokploy_client.models.settings_toggle_requests_request import SettingsToggleRequestsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SettingsToggleRequestsRequest from a JSON string
settings_toggle_requests_request_instance = SettingsToggleRequestsRequest.from_json(json)
# print the JSON string representation of the object
print(SettingsToggleRequestsRequest.to_json())

# convert the object into a dict
settings_toggle_requests_request_dict = settings_toggle_requests_request_instance.to_dict()
# create an instance of SettingsToggleRequestsRequest from a dict
settings_toggle_requests_request_from_dict = SettingsToggleRequestsRequest.from_dict(settings_toggle_requests_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


