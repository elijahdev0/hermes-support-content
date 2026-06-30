# TagBulkAssignRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 
**tag_ids** | **List[Optional[str]]** |  | 

## Example

```python
from dokploy_client.models.tag_bulk_assign_request import TagBulkAssignRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TagBulkAssignRequest from a JSON string
tag_bulk_assign_request_instance = TagBulkAssignRequest.from_json(json)
# print the JSON string representation of the object
print(TagBulkAssignRequest.to_json())

# convert the object into a dict
tag_bulk_assign_request_dict = tag_bulk_assign_request_instance.to_dict()
# create an instance of TagBulkAssignRequest from a dict
tag_bulk_assign_request_from_dict = TagBulkAssignRequest.from_dict(tag_bulk_assign_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


