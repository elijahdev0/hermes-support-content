# NotificationCreatePushoverRequest


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
**user_key** | **str** |  | 
**api_token** | **str** |  | 
**priority** | **float** |  | [optional] [default to 0]
**retry** | **float** |  | [optional] 
**expire** | **float** |  | [optional] 

## Example

```python
from dokploy_client.models.notification_create_pushover_request import NotificationCreatePushoverRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationCreatePushoverRequest from a JSON string
notification_create_pushover_request_instance = NotificationCreatePushoverRequest.from_json(json)
# print the JSON string representation of the object
print(NotificationCreatePushoverRequest.to_json())

# convert the object into a dict
notification_create_pushover_request_dict = notification_create_pushover_request_instance.to_dict()
# create an instance of NotificationCreatePushoverRequest from a dict
notification_create_pushover_request_from_dict = NotificationCreatePushoverRequest.from_dict(notification_create_pushover_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


