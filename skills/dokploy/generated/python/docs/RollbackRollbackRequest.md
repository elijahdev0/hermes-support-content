# RollbackRollbackRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rollback_id** | **str** |  | 

## Example

```python
from dokploy_client.models.rollback_rollback_request import RollbackRollbackRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RollbackRollbackRequest from a JSON string
rollback_rollback_request_instance = RollbackRollbackRequest.from_json(json)
# print the JSON string representation of the object
print(RollbackRollbackRequest.to_json())

# convert the object into a dict
rollback_rollback_request_dict = rollback_rollback_request_instance.to_dict()
# create an instance of RollbackRollbackRequest from a dict
rollback_rollback_request_from_dict = RollbackRollbackRequest.from_dict(rollback_rollback_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


