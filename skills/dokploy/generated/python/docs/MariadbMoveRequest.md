# MariadbMoveRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mariadb_id** | **str** |  | 
**target_environment_id** | **str** |  | 

## Example

```python
from dokploy_client.models.mariadb_move_request import MariadbMoveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MariadbMoveRequest from a JSON string
mariadb_move_request_instance = MariadbMoveRequest.from_json(json)
# print the JSON string representation of the object
print(MariadbMoveRequest.to_json())

# convert the object into a dict
mariadb_move_request_dict = mariadb_move_request_instance.to_dict()
# create an instance of MariadbMoveRequest from a dict
mariadb_move_request_from_dict = MariadbMoveRequest.from_dict(mariadb_move_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


