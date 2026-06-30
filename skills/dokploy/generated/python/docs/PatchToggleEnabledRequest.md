# PatchToggleEnabledRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**patch_id** | **str** |  | 
**enabled** | **bool** |  | 

## Example

```python
from dokploy_client.models.patch_toggle_enabled_request import PatchToggleEnabledRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchToggleEnabledRequest from a JSON string
patch_toggle_enabled_request_instance = PatchToggleEnabledRequest.from_json(json)
# print the JSON string representation of the object
print(PatchToggleEnabledRequest.to_json())

# convert the object into a dict
patch_toggle_enabled_request_dict = patch_toggle_enabled_request_instance.to_dict()
# create an instance of PatchToggleEnabledRequest from a dict
patch_toggle_enabled_request_from_dict = PatchToggleEnabledRequest.from_dict(patch_toggle_enabled_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


