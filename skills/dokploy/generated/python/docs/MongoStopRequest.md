# MongoStopRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mongo_id** | **str** |  | 

## Example

```python
from dokploy_client.models.mongo_stop_request import MongoStopRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MongoStopRequest from a JSON string
mongo_stop_request_instance = MongoStopRequest.from_json(json)
# print the JSON string representation of the object
print(MongoStopRequest.to_json())

# convert the object into a dict
mongo_stop_request_dict = mongo_stop_request_instance.to_dict()
# create an instance of MongoStopRequest from a dict
mongo_stop_request_from_dict = MongoStopRequest.from_dict(mongo_stop_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


