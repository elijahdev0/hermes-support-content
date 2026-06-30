# UserSendInvitationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invitation_id** | **str** |  | 
**notification_id** | **str** |  | 

## Example

```python
from dokploy_client.models.user_send_invitation_request import UserSendInvitationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserSendInvitationRequest from a JSON string
user_send_invitation_request_instance = UserSendInvitationRequest.from_json(json)
# print the JSON string representation of the object
print(UserSendInvitationRequest.to_json())

# convert the object into a dict
user_send_invitation_request_dict = user_send_invitation_request_instance.to_dict()
# create an instance of UserSendInvitationRequest from a dict
user_send_invitation_request_from_dict = UserSendInvitationRequest.from_dict(user_send_invitation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


