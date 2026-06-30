# MongoDeployRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mongo_id** | **str** |  | 

## Example

```python
from dokploy_client.models.mongo_deploy_request import MongoDeployRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MongoDeployRequest from a JSON string
mongo_deploy_request_instance = MongoDeployRequest.from_json(json)
# print the JSON string representation of the object
print(MongoDeployRequest.to_json())

# convert the object into a dict
mongo_deploy_request_dict = mongo_deploy_request_instance.to_dict()
# create an instance of MongoDeployRequest from a dict
mongo_deploy_request_from_dict = MongoDeployRequest.from_dict(mongo_deploy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


