# MongoMoveRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mongo_id** | **str** |  | 
**target_environment_id** | **str** |  | 

## Example

```python
from dokploy_client.models.mongo_move_request import MongoMoveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MongoMoveRequest from a JSON string
mongo_move_request_instance = MongoMoveRequest.from_json(json)
# print the JSON string representation of the object
print(MongoMoveRequest.to_json())

# convert the object into a dict
mongo_move_request_dict = mongo_move_request_instance.to_dict()
# create an instance of MongoMoveRequest from a dict
mongo_move_request_from_dict = MongoMoveRequest.from_dict(mongo_move_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


