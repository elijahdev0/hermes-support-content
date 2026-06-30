# RedisDeployRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redis_id** | **str** |  | 

## Example

```python
from dokploy_client.models.redis_deploy_request import RedisDeployRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RedisDeployRequest from a JSON string
redis_deploy_request_instance = RedisDeployRequest.from_json(json)
# print the JSON string representation of the object
print(RedisDeployRequest.to_json())

# convert the object into a dict
redis_deploy_request_dict = redis_deploy_request_instance.to_dict()
# create an instance of RedisDeployRequest from a dict
redis_deploy_request_from_dict = RedisDeployRequest.from_dict(redis_deploy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


