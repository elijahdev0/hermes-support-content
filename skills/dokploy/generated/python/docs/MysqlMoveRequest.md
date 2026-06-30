# MysqlMoveRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mysql_id** | **str** |  | 
**target_environment_id** | **str** |  | 

## Example

```python
from dokploy_client.models.mysql_move_request import MysqlMoveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MysqlMoveRequest from a JSON string
mysql_move_request_instance = MysqlMoveRequest.from_json(json)
# print the JSON string representation of the object
print(MysqlMoveRequest.to_json())

# convert the object into a dict
mysql_move_request_dict = mysql_move_request_instance.to_dict()
# create an instance of MysqlMoveRequest from a dict
mysql_move_request_from_dict = MysqlMoveRequest.from_dict(mysql_move_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


