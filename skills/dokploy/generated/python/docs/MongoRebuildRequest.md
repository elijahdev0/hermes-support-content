# MongoRebuildRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mongo_id** | **str** |  | 

## Example

```python
from dokploy_client.models.mongo_rebuild_request import MongoRebuildRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MongoRebuildRequest from a JSON string
mongo_rebuild_request_instance = MongoRebuildRequest.from_json(json)
# print the JSON string representation of the object
print(MongoRebuildRequest.to_json())

# convert the object into a dict
mongo_rebuild_request_dict = mongo_rebuild_request_instance.to_dict()
# create an instance of MongoRebuildRequest from a dict
mongo_rebuild_request_from_dict = MongoRebuildRequest.from_dict(mongo_rebuild_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


