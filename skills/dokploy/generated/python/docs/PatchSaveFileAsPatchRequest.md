# PatchSaveFileAsPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** |  | 
**file_path** | **str** |  | 
**content** | **str** |  | 
**patch_type** | **str** |  | [optional] [default to 'update']

## Example

```python
from dokploy_client.models.patch_save_file_as_patch_request import PatchSaveFileAsPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchSaveFileAsPatchRequest from a JSON string
patch_save_file_as_patch_request_instance = PatchSaveFileAsPatchRequest.from_json(json)
# print the JSON string representation of the object
print(PatchSaveFileAsPatchRequest.to_json())

# convert the object into a dict
patch_save_file_as_patch_request_dict = patch_save_file_as_patch_request_instance.to_dict()
# create an instance of PatchSaveFileAsPatchRequest from a dict
patch_save_file_as_patch_request_from_dict = PatchSaveFileAsPatchRequest.from_dict(patch_save_file_as_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


