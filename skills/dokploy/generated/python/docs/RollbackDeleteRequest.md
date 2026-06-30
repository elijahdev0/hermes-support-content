# RollbackDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rollback_id** | **str** |  | 

## Example

```python
from dokploy_client.models.rollback_delete_request import RollbackDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RollbackDeleteRequest from a JSON string
rollback_delete_request_instance = RollbackDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(RollbackDeleteRequest.to_json())

# convert the object into a dict
rollback_delete_request_dict = rollback_delete_request_instance.to_dict()
# create an instance of RollbackDeleteRequest from a dict
rollback_delete_request_from_dict = RollbackDeleteRequest.from_dict(rollback_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


