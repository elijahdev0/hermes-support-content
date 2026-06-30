# ScheduleRunManuallyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule_id** | **str** |  | 

## Example

```python
from dokploy_client.models.schedule_run_manually_request import ScheduleRunManuallyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleRunManuallyRequest from a JSON string
schedule_run_manually_request_instance = ScheduleRunManuallyRequest.from_json(json)
# print the JSON string representation of the object
print(ScheduleRunManuallyRequest.to_json())

# convert the object into a dict
schedule_run_manually_request_dict = schedule_run_manually_request_instance.to_dict()
# create an instance of ScheduleRunManuallyRequest from a dict
schedule_run_manually_request_from_dict = ScheduleRunManuallyRequest.from_dict(schedule_run_manually_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


