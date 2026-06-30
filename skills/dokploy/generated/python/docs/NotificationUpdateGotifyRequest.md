# NotificationUpdateGotifyRequest


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
**server_url** | **str** |  | [optional] 
**app_token** | **str** |  | [optional] 
**priority** | **float** |  | [optional] 
**decoration** | **bool** |  | [optional] 
**notification_id** | **str** |  | 
**gotify_id** | **str** |  | 
**organization_id** | **str** |  | [optional] 

## Example

```python
from dokploy_client.models.notification_update_gotify_request import NotificationUpdateGotifyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationUpdateGotifyRequest from a JSON string
notification_update_gotify_request_instance = NotificationUpdateGotifyRequest.from_json(json)
# print the JSON string representation of the object
print(NotificationUpdateGotifyRequest.to_json())

# convert the object into a dict
notification_update_gotify_request_dict = notification_update_gotify_request_instance.to_dict()
# create an instance of NotificationUpdateGotifyRequest from a dict
notification_update_gotify_request_from_dict = NotificationUpdateGotifyRequest.from_dict(notification_update_gotify_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


