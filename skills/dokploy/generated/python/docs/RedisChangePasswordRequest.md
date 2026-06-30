# RedisChangePasswordRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redis_id** | **str** |  | 
**password** | **str** |  | 

## Example

```python
from dokploy_client.models.redis_change_password_request import RedisChangePasswordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RedisChangePasswordRequest from a JSON string
redis_change_password_request_instance = RedisChangePasswordRequest.from_json(json)
# print the JSON string representation of the object
print(RedisChangePasswordRequest.to_json())

# convert the object into a dict
redis_change_password_request_dict = redis_change_password_request_instance.to_dict()
# create an instance of RedisChangePasswordRequest from a dict
redis_change_password_request_from_dict = RedisChangePasswordRequest.from_dict(redis_change_password_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


