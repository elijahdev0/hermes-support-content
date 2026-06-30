# LibsqlMoveRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**libsql_id** | **str** |  | 
**target_environment_id** | **str** |  | 

## Example

```python
from dokploy_client.models.libsql_move_request import LibsqlMoveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LibsqlMoveRequest from a JSON string
libsql_move_request_instance = LibsqlMoveRequest.from_json(json)
# print the JSON string representation of the object
print(LibsqlMoveRequest.to_json())

# convert the object into a dict
libsql_move_request_dict = libsql_move_request_instance.to_dict()
# create an instance of LibsqlMoveRequest from a dict
libsql_move_request_from_dict = LibsqlMoveRequest.from_dict(libsql_move_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


