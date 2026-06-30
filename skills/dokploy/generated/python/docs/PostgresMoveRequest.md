# PostgresMoveRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**postgres_id** | **str** |  | 
**target_environment_id** | **str** |  | 

## Example

```python
from dokploy_client.models.postgres_move_request import PostgresMoveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostgresMoveRequest from a JSON string
postgres_move_request_instance = PostgresMoveRequest.from_json(json)
# print the JSON string representation of the object
print(PostgresMoveRequest.to_json())

# convert the object into a dict
postgres_move_request_dict = postgres_move_request_instance.to_dict()
# create an instance of PostgresMoveRequest from a dict
postgres_move_request_from_dict = PostgresMoveRequest.from_dict(postgres_move_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


