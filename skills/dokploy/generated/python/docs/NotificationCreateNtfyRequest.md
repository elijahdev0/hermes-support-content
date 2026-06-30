# NotificationCreateNtfyRequest


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
**server_url** | **str** |  | 
**topic** | **str** |  | 
**access_token** | **str** |  | 
**priority** | **float** |  | 

## Example

```python
from dokploy_client.models.notification_create_ntfy_request import NotificationCreateNtfyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationCreateNtfyRequest from a JSON string
notification_create_ntfy_request_instance = NotificationCreateNtfyRequest.from_json(json)
# print the JSON string representation of the object
print(NotificationCreateNtfyRequest.to_json())

# convert the object into a dict
notification_create_ntfy_request_dict = notification_create_ntfy_request_instance.to_dict()
# create an instance of NotificationCreateNtfyRequest from a dict
notification_create_ntfy_request_from_dict = NotificationCreateNtfyRequest.from_dict(notification_create_ntfy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


