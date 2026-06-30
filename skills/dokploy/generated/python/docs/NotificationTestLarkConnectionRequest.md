# NotificationTestLarkConnectionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_url** | **str** |  | 

## Example

```python
from dokploy_client.models.notification_test_lark_connection_request import NotificationTestLarkConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationTestLarkConnectionRequest from a JSON string
notification_test_lark_connection_request_instance = NotificationTestLarkConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(NotificationTestLarkConnectionRequest.to_json())

# convert the object into a dict
notification_test_lark_connection_request_dict = notification_test_lark_connection_request_instance.to_dict()
# create an instance of NotificationTestLarkConnectionRequest from a dict
notification_test_lark_connection_request_from_dict = NotificationTestLarkConnectionRequest.from_dict(notification_test_lark_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


