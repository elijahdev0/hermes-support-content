# ScheduleUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule_id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**cron_expression** | **str** |  | 
**app_name** | **str** |  | [optional] 
**service_name** | **str** |  | [optional] 
**shell_type** | **str** |  | [optional] 
**schedule_type** | **str** |  | [optional] 
**command** | **str** |  | 
**script** | **str** |  | [optional] 
**application_id** | **str** |  | [optional] 
**compose_id** | **str** |  | [optional] 
**server_id** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**timezone** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 

## Example

```python
from dokploy_client.models.schedule_update_request import ScheduleUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleUpdateRequest from a JSON string
schedule_update_request_instance = ScheduleUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(ScheduleUpdateRequest.to_json())

# convert the object into a dict
schedule_update_request_dict = schedule_update_request_instance.to_dict()
# create an instance of ScheduleUpdateRequest from a dict
schedule_update_request_from_dict = ScheduleUpdateRequest.from_dict(schedule_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


