# OrganizationRemoveInvitationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invitation_id** | **str** |  | 

## Example

```python
from dokploy_client.models.organization_remove_invitation_request import OrganizationRemoveInvitationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationRemoveInvitationRequest from a JSON string
organization_remove_invitation_request_instance = OrganizationRemoveInvitationRequest.from_json(json)
# print the JSON string representation of the object
print(OrganizationRemoveInvitationRequest.to_json())

# convert the object into a dict
organization_remove_invitation_request_dict = organization_remove_invitation_request_instance.to_dict()
# create an instance of OrganizationRemoveInvitationRequest from a dict
organization_remove_invitation_request_from_dict = OrganizationRemoveInvitationRequest.from_dict(organization_remove_invitation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


