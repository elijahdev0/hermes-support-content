# NotificationUpdateNtfyRequest


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
**topic** | **str** |  | [optional] 
**access_token** | **str** |  | [optional] 
**priority** | **float** |  | [optional] 
**notification_id** | **str** |  | 
**ntfy_id** | **str** |  | 
**organization_id** | **str** |  | [optional] 

## Example

```python
from dokploy_client.models.notification_update_ntfy_request import NotificationUpdateNtfyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationUpdateNtfyRequest from a JSON string
notification_update_ntfy_request_instance = NotificationUpdateNtfyRequest.from_json(json)
# print the JSON string representation of the object
print(NotificationUpdateNtfyRequest.to_json())

# convert the object into a dict
notification_update_ntfy_request_dict = notification_update_ntfy_request_instance.to_dict()
# create an instance of NotificationUpdateNtfyRequest from a dict
notification_update_ntfy_request_from_dict = NotificationUpdateNtfyRequest.from_dict(notification_update_ntfy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


