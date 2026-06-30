# OrganizationUpdateMemberRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_id** | **str** |  | 
**role** | **str** |  | 

## Example

```python
from dokploy_client.models.organization_update_member_role_request import OrganizationUpdateMemberRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationUpdateMemberRoleRequest from a JSON string
organization_update_member_role_request_instance = OrganizationUpdateMemberRoleRequest.from_json(json)
# print the JSON string representation of the object
print(OrganizationUpdateMemberRoleRequest.to_json())

# convert the object into a dict
organization_update_member_role_request_dict = organization_update_member_role_request_instance.to_dict()
# create an instance of OrganizationUpdateMemberRoleRequest from a dict
organization_update_member_role_request_from_dict = OrganizationUpdateMemberRoleRequest.from_dict(organization_update_member_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


