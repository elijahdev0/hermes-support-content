# ApplicationMoveRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **str** |  | 
**target_environment_id** | **str** |  | 

## Example

```python
from dokploy_client.models.application_move_request import ApplicationMoveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationMoveRequest from a JSON string
application_move_request_instance = ApplicationMoveRequest.from_json(json)
# print the JSON string representation of the object
print(ApplicationMoveRequest.to_json())

# convert the object into a dict
application_move_request_dict = application_move_request_instance.to_dict()
# create an instance of ApplicationMoveRequest from a dict
application_move_request_from_dict = ApplicationMoveRequest.from_dict(application_move_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


