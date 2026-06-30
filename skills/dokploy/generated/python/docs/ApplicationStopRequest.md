# ApplicationStopRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **str** |  | 

## Example

```python
from dokploy_client.models.application_stop_request import ApplicationStopRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationStopRequest from a JSON string
application_stop_request_instance = ApplicationStopRequest.from_json(json)
# print the JSON string representation of the object
print(ApplicationStopRequest.to_json())

# convert the object into a dict
application_stop_request_dict = application_stop_request_instance.to_dict()
# create an instance of ApplicationStopRequest from a dict
application_stop_request_from_dict = ApplicationStopRequest.from_dict(application_stop_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


