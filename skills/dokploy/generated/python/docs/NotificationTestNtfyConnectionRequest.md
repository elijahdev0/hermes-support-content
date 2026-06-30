# NotificationTestNtfyConnectionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_url** | **str** |  | 
**topic** | **str** |  | 
**access_token** | **str** |  | 
**priority** | **float** |  | 

## Example

```python
from dokploy_client.models.notification_test_ntfy_connection_request import NotificationTestNtfyConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationTestNtfyConnectionRequest from a JSON string
notification_test_ntfy_connection_request_instance = NotificationTestNtfyConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(NotificationTestNtfyConnectionRequest.to_json())

# convert the object into a dict
notification_test_ntfy_connection_request_dict = notification_test_ntfy_connection_request_instance.to_dict()
# create an instance of NotificationTestNtfyConnectionRequest from a dict
notification_test_ntfy_connection_request_from_dict = NotificationTestNtfyConnectionRequest.from_dict(notification_test_ntfy_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


