# RedisRebuildRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redis_id** | **str** |  | 

## Example

```python
from dokploy_client.models.redis_rebuild_request import RedisRebuildRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RedisRebuildRequest from a JSON string
redis_rebuild_request_instance = RedisRebuildRequest.from_json(json)
# print the JSON string representation of the object
print(RedisRebuildRequest.to_json())

# convert the object into a dict
redis_rebuild_request_dict = redis_rebuild_request_instance.to_dict()
# create an instance of RedisRebuildRequest from a dict
redis_rebuild_request_from_dict = RedisRebuildRequest.from_dict(redis_rebuild_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


