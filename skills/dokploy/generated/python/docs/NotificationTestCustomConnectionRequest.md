# NotificationTestCustomConnectionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint** | **str** |  | 
**headers** | **Dict[str, str]** |  | [optional] 

## Example

```python
from dokploy_client.models.notification_test_custom_connection_request import NotificationTestCustomConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationTestCustomConnectionRequest from a JSON string
notification_test_custom_connection_request_instance = NotificationTestCustomConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(NotificationTestCustomConnectionRequest.to_json())

# convert the object into a dict
notification_test_custom_connection_request_dict = notification_test_custom_connection_request_instance.to_dict()
# create an instance of NotificationTestCustomConnectionRequest from a dict
notification_test_custom_connection_request_from_dict = NotificationTestCustomConnectionRequest.from_dict(notification_test_custom_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


