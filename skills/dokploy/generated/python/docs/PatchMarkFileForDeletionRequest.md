# PatchMarkFileForDeletionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** |  | 
**file_path** | **str** |  | 

## Example

```python
from dokploy_client.models.patch_mark_file_for_deletion_request import PatchMarkFileForDeletionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchMarkFileForDeletionRequest from a JSON string
patch_mark_file_for_deletion_request_instance = PatchMarkFileForDeletionRequest.from_json(json)
# print the JSON string representation of the object
print(PatchMarkFileForDeletionRequest.to_json())

# convert the object into a dict
patch_mark_file_for_deletion_request_dict = patch_mark_file_for_deletion_request_instance.to_dict()
# create an instance of PatchMarkFileForDeletionRequest from a dict
patch_mark_file_for_deletion_request_from_dict = PatchMarkFileForDeletionRequest.from_dict(patch_mark_file_for_deletion_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


