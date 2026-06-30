# NotificationTestResendConnectionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** |  | 
**from_address** | **str** |  | 
**to_addresses** | **List[str]** |  | 

## Example

```python
from dokploy_client.models.notification_test_resend_connection_request import NotificationTestResendConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationTestResendConnectionRequest from a JSON string
notification_test_resend_connection_request_instance = NotificationTestResendConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(NotificationTestResendConnectionRequest.to_json())

# convert the object into a dict
notification_test_resend_connection_request_dict = notification_test_resend_connection_request_instance.to_dict()
# create an instance of NotificationTestResendConnectionRequest from a dict
notification_test_resend_connection_request_from_dict = NotificationTestResendConnectionRequest.from_dict(notification_test_resend_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


