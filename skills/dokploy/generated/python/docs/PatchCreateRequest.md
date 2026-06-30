# PatchCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_path** | **str** |  | 
**content** | **str** |  | 
**type** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**application_id** | **str** |  | [optional] 
**compose_id** | **str** |  | [optional] 

## Example

```python
from dokploy_client.models.patch_create_request import PatchCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchCreateRequest from a JSON string
patch_create_request_instance = PatchCreateRequest.from_json(json)
# print the JSON string representation of the object
print(PatchCreateRequest.to_json())

# convert the object into a dict
patch_create_request_dict = patch_create_request_instance.to_dict()
# create an instance of PatchCreateRequest from a dict
patch_create_request_from_dict = PatchCreateRequest.from_dict(patch_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


