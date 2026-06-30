# OrganizationInviteMemberRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**role** | **str** |  | 

## Example

```python
from dokploy_client.models.organization_invite_member_request import OrganizationInviteMemberRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationInviteMemberRequest from a JSON string
organization_invite_member_request_instance = OrganizationInviteMemberRequest.from_json(json)
# print the JSON string representation of the object
print(OrganizationInviteMemberRequest.to_json())

# convert the object into a dict
organization_invite_member_request_dict = organization_invite_member_request_instance.to_dict()
# create an instance of OrganizationInviteMemberRequest from a dict
organization_invite_member_request_from_dict = OrganizationInviteMemberRequest.from_dict(organization_invite_member_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


