# PatchEnsureRepoRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from dokploy_client.models.patch_ensure_repo_request import PatchEnsureRepoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchEnsureRepoRequest from a JSON string
patch_ensure_repo_request_instance = PatchEnsureRepoRequest.from_json(json)
# print the JSON string representation of the object
print(PatchEnsureRepoRequest.to_json())

# convert the object into a dict
patch_ensure_repo_request_dict = patch_ensure_repo_request_instance.to_dict()
# create an instance of PatchEnsureRepoRequest from a dict
patch_ensure_repo_request_from_dict = PatchEnsureRepoRequest.from_dict(patch_ensure_repo_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


