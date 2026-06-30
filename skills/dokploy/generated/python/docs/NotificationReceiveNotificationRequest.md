# NotificationReceiveNotificationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_type** | **str** |  | [optional] [default to 'Dokploy']
**type** | **str** |  | 
**value** | **float** |  | 
**threshold** | **float** |  | 
**message** | **str** |  | 
**timestamp** | **str** |  | 
**token** | **str** |  | 

## Example

```python
from dokploy_client.models.notification_receive_notification_request import NotificationReceiveNotificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationReceiveNotificationRequest from a JSON string
notification_receive_notification_request_instance = NotificationReceiveNotificationRequest.from_json(json)
# print the JSON string representation of the object
print(NotificationReceiveNotificationRequest.to_json())

# convert the object into a dict
notification_receive_notification_request_dict = notification_receive_notification_request_instance.to_dict()
# create an instance of NotificationReceiveNotificationRequest from a dict
notification_receive_notification_request_from_dict = NotificationReceiveNotificationRequest.from_dict(notification_receive_notification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


