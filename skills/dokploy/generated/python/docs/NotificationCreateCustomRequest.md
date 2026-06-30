# NotificationCreateCustomRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_build_error** | **bool** |  | [optional] 
**database_backup** | **bool** |  | [optional] 
**dokploy_backup** | **bool** |  | [optional] 
**volume_backup** | **bool** |  | [optional] 
**dokploy_restart** | **bool** |  | [optional] 
**name** | **str** |  | 
**app_deploy** | **bool** |  | [optional] 
**docker_cleanup** | **bool** |  | [optional] 
**server_threshold** | **bool** |  | [optional] 
**endpoint** | **str** |  | 
**headers** | **Dict[str, str]** |  | [optional] 

## Example

```python
from dokploy_client.models.notification_create_custom_request import NotificationCreateCustomRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationCreateCustomRequest from a JSON string
notification_create_custom_request_instance = NotificationCreateCustomRequest.from_json(json)
# print the JSON string representation of the object
print(NotificationCreateCustomRequest.to_json())

# convert the object into a dict
notification_create_custom_request_dict = notification_create_custom_request_instance.to_dict()
# create an instance of NotificationCreateCustomRequest from a dict
notification_create_custom_request_from_dict = NotificationCreateCustomRequest.from_dict(notification_create_custom_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


