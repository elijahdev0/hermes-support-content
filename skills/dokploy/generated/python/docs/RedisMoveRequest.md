# RedisMoveRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redis_id** | **str** |  | 
**target_environment_id** | **str** |  | 

## Example

```python
from dokploy_client.models.redis_move_request import RedisMoveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RedisMoveRequest from a JSON string
redis_move_request_instance = RedisMoveRequest.from_json(json)
# print the JSON string representation of the object
print(RedisMoveRequest.to_json())

# convert the object into a dict
redis_move_request_dict = redis_move_request_instance.to_dict()
# create an instance of RedisMoveRequest from a dict
redis_move_request_from_dict = RedisMoveRequest.from_dict(redis_move_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


