# CustomRoleRemoveRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_name** | **str** |  | 

## Example

```python
from dokploy_client.models.custom_role_remove_request import CustomRoleRemoveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomRoleRemoveRequest from a JSON string
custom_role_remove_request_instance = CustomRoleRemoveRequest.from_json(json)
# print the JSON string representation of the object
print(CustomRoleRemoveRequest.to_json())

# convert the object into a dict
custom_role_remove_request_dict = custom_role_remove_request_instance.to_dict()
# create an instance of CustomRoleRemoveRequest from a dict
custom_role_remove_request_from_dict = CustomRoleRemoveRequest.from_dict(custom_role_remove_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


