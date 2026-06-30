# ComposeMoveRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compose_id** | **str** |  | 
**target_environment_id** | **str** |  | 

## Example

```python
from dokploy_client.models.compose_move_request import ComposeMoveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ComposeMoveRequest from a JSON string
compose_move_request_instance = ComposeMoveRequest.from_json(json)
# print the JSON string representation of the object
print(ComposeMoveRequest.to_json())

# convert the object into a dict
compose_move_request_dict = compose_move_request_instance.to_dict()
# create an instance of ComposeMoveRequest from a dict
compose_move_request_from_dict = ComposeMoveRequest.from_dict(compose_move_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


