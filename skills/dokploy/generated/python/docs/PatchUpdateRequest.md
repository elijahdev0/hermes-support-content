# PatchUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**patch_id** | **str** |  | 
**type** | **str** |  | [optional] 
**file_path** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**content** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from dokploy_client.models.patch_update_request import PatchUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchUpdateRequest from a JSON string
patch_update_request_instance = PatchUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(PatchUpdateRequest.to_json())

# convert the object into a dict
patch_update_request_dict = patch_update_request_instance.to_dict()
# create an instance of PatchUpdateRequest from a dict
patch_update_request_from_dict = PatchUpdateRequest.from_dict(patch_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


