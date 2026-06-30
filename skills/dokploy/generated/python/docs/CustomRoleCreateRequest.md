# CustomRoleCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_name** | **str** |  | 
**permissions** | **Dict[str, List[str]]** |  | 

## Example

```python
from dokploy_client.models.custom_role_create_request import CustomRoleCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomRoleCreateRequest from a JSON string
custom_role_create_request_instance = CustomRoleCreateRequest.from_json(json)
# print the JSON string representation of the object
print(CustomRoleCreateRequest.to_json())

# convert the object into a dict
custom_role_create_request_dict = custom_role_create_request_instance.to_dict()
# create an instance of CustomRoleCreateRequest from a dict
custom_role_create_request_from_dict = CustomRoleCreateRequest.from_dict(custom_role_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


