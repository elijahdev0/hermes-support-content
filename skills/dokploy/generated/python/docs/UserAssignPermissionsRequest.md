# UserAssignPermissionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**accessed_projects** | **List[str]** |  | 
**accessed_environments** | **List[str]** |  | 
**accessed_services** | **List[str]** |  | 
**accessed_git_providers** | **List[str]** |  | 
**accessed_servers** | **List[str]** |  | 
**can_create_projects** | **bool** |  | 
**can_create_services** | **bool** |  | 
**can_delete_projects** | **bool** |  | 
**can_delete_services** | **bool** |  | 
**can_access_to_docker** | **bool** |  | 
**can_access_to_traefik_files** | **bool** |  | 
**can_access_to_api** | **bool** |  | 
**can_access_to_ssh_keys** | **bool** |  | 
**can_access_to_git_providers** | **bool** |  | 
**can_delete_environments** | **bool** |  | 
**can_create_environments** | **bool** |  | 

## Example

```python
from dokploy_client.models.user_assign_permissions_request import UserAssignPermissionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserAssignPermissionsRequest from a JSON string
user_assign_permissions_request_instance = UserAssignPermissionsRequest.from_json(json)
# print the JSON string representation of the object
print(UserAssignPermissionsRequest.to_json())

# convert the object into a dict
user_assign_permissions_request_dict = user_assign_permissions_request_instance.to_dict()
# create an instance of UserAssignPermissionsRequest from a dict
user_assign_permissions_request_from_dict = UserAssignPermissionsRequest.from_dict(user_assign_permissions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


