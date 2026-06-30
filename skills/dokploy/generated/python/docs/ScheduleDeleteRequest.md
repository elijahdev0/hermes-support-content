# ScheduleDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule_id** | **str** |  | 

## Example

```python
from dokploy_client.models.schedule_delete_request import ScheduleDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleDeleteRequest from a JSON string
schedule_delete_request_instance = ScheduleDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(ScheduleDeleteRequest.to_json())

# convert the object into a dict
schedule_delete_request_dict = schedule_delete_request_instance.to_dict()
# create an instance of ScheduleDeleteRequest from a dict
schedule_delete_request_from_dict = ScheduleDeleteRequest.from_dict(schedule_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


