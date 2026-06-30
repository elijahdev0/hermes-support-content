# NotificationUpdateSlackRequest


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
**webhook_url** | **str** |  | [optional] 
**channel** | **str** |  | [optional] 
**notification_id** | **str** |  | 
**slack_id** | **str** |  | 
**organization_id** | **str** |  | [optional] 

## Example

```python
from dokploy_client.models.notification_update_slack_request import NotificationUpdateSlackRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationUpdateSlackRequest from a JSON string
notification_update_slack_request_instance = NotificationUpdateSlackRequest.from_json(json)
# print the JSON string representation of the object
print(NotificationUpdateSlackRequest.to_json())

# convert the object into a dict
notification_update_slack_request_dict = notification_update_slack_request_instance.to_dict()
# create an instance of NotificationUpdateSlackRequest from a dict
notification_update_slack_request_from_dict = NotificationUpdateSlackRequest.from_dict(notification_update_slack_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


