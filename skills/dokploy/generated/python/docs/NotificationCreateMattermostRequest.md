# NotificationCreateMattermostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_build_error** | **bool** |  | 
**database_backup** | **bool** |  | 
**dokploy_backup** | **bool** |  | 
**volume_backup** | **bool** |  | 
**dokploy_restart** | **bool** |  | 
**name** | **str** |  | 
**app_deploy** | **bool** |  | 
**docker_cleanup** | **bool** |  | 
**server_threshold** | **bool** |  | 
**webhook_url** | **str** |  | 
**channel** | **str** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from dokploy_client.models.notification_create_mattermost_request import NotificationCreateMattermostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationCreateMattermostRequest from a JSON string
notification_create_mattermost_request_instance = NotificationCreateMattermostRequest.from_json(json)
# print the JSON string representation of the object
print(NotificationCreateMattermostRequest.to_json())

# convert the object into a dict
notification_create_mattermost_request_dict = notification_create_mattermost_request_instance.to_dict()
# create an instance of NotificationCreateMattermostRequest from a dict
notification_create_mattermost_request_from_dict = NotificationCreateMattermostRequest.from_dict(notification_create_mattermost_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


