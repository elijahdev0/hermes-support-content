# PatchDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**patch_id** | **str** |  | 

## Example

```python
from dokploy_client.models.patch_delete_request import PatchDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchDeleteRequest from a JSON string
patch_delete_request_instance = PatchDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(PatchDeleteRequest.to_json())

# convert the object into a dict
patch_delete_request_dict = patch_delete_request_instance.to_dict()
# create an instance of PatchDeleteRequest from a dict
patch_delete_request_from_dict = PatchDeleteRequest.from_dict(patch_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


