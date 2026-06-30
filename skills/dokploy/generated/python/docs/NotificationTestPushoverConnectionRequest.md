# NotificationTestPushoverConnectionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_key** | **str** |  | 
**api_token** | **str** |  | 
**priority** | **float** |  | 
**retry** | **float** |  | [optional] 
**expire** | **float** |  | [optional] 

## Example

```python
from dokploy_client.models.notification_test_pushover_connection_request import NotificationTestPushoverConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationTestPushoverConnectionRequest from a JSON string
notification_test_pushover_connection_request_instance = NotificationTestPushoverConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(NotificationTestPushoverConnectionRequest.to_json())

# convert the object into a dict
notification_test_pushover_connection_request_dict = notification_test_pushover_connection_request_instance.to_dict()
# create an instance of NotificationTestPushoverConnectionRequest from a dict
notification_test_pushover_connection_request_from_dict = NotificationTestPushoverConnectionRequest.from_dict(notification_test_pushover_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


