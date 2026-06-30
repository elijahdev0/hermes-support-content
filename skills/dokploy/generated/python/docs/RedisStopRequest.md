# RedisStopRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redis_id** | **str** |  | 

## Example

```python
from dokploy_client.models.redis_stop_request import RedisStopRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RedisStopRequest from a JSON string
redis_stop_request_instance = RedisStopRequest.from_json(json)
# print the JSON string representation of the object
print(RedisStopRequest.to_json())

# convert the object into a dict
redis_stop_request_dict = redis_stop_request_instance.to_dict()
# create an instance of RedisStopRequest from a dict
redis_stop_request_from_dict = RedisStopRequest.from_dict(redis_stop_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


