# NotificationTestGotifyConnectionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_url** | **str** |  | 
**app_token** | **str** |  | 
**priority** | **float** |  | 
**decoration** | **bool** |  | [optional] 

## Example

```python
from dokploy_client.models.notification_test_gotify_connection_request import NotificationTestGotifyConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationTestGotifyConnectionRequest from a JSON string
notification_test_gotify_connection_request_instance = NotificationTestGotifyConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(NotificationTestGotifyConnectionRequest.to_json())

# convert the object into a dict
notification_test_gotify_connection_request_dict = notification_test_gotify_connection_request_instance.to_dict()
# create an instance of NotificationTestGotifyConnectionRequest from a dict
notification_test_gotify_connection_request_from_dict = NotificationTestGotifyConnectionRequest.from_dict(notification_test_gotify_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


