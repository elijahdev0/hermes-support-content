# NotificationUpdateTelegramRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_build_error** | **bool** |  | [optional] 
**database_backup** | **bool** |  | [optional] 
**dokploy_backup** | **bool** |  | [optional] 
**volume_backup** | **bool** |  | [optional] 
**dokploy_restart** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**app_deploy** | **bool** |  | [optional] 
**docker_cleanup** | **bool** |  | [optional] 
**server_threshold** | **bool** |  | [optional] 
**bot_token** | **str** |  | [optional] 
**chat_id** | **str** |  | [optional] 
**message_thread_id** | **str** |  | [optional] 
**notification_id** | **str** |  | 
**telegram_id** | **str** |  | 
**organization_id** | **str** |  | [optional] 

## Example

```python
from dokploy_client.models.notification_update_telegram_request import NotificationUpdateTelegramRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationUpdateTelegramRequest from a JSON string
notification_update_telegram_request_instance = NotificationUpdateTelegramRequest.from_json(json)
# print the JSON string representation of the object
print(NotificationUpdateTelegramRequest.to_json())

# convert the object into a dict
notification_update_telegram_request_dict = notification_update_telegram_request_instance.to_dict()
# create an instance of NotificationUpdateTelegramRequest from a dict
notification_update_telegram_request_from_dict = NotificationUpdateTelegramRequest.from_dict(notification_update_telegram_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


