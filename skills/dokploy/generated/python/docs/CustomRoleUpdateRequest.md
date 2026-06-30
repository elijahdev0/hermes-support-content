# CustomRoleUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_name** | **str** |  | 
**new_role_name** | **str** |  | [optional] 
**permissions** | **Dict[str, List[str]]** |  | 

## Example

```python
from dokploy_client.models.custom_role_update_request import CustomRoleUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomRoleUpdateRequest from a JSON string
custom_role_update_request_instance = CustomRoleUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(CustomRoleUpdateRequest.to_json())

# convert the object into a dict
custom_role_update_request_dict = custom_role_update_request_instance.to_dict()
# create an instance of CustomRoleUpdateRequest from a dict
custom_role_update_request_from_dict = CustomRoleUpdateRequest.from_dict(custom_role_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


