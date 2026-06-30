# UserCreateUserWithCredentialsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**password** | **str** |  | 
**role** | **str** |  | 

## Example

```python
from dokploy_client.models.user_create_user_with_credentials_request import UserCreateUserWithCredentialsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserCreateUserWithCredentialsRequest from a JSON string
user_create_user_with_credentials_request_instance = UserCreateUserWithCredentialsRequest.from_json(json)
# print the JSON string representation of the object
print(UserCreateUserWithCredentialsRequest.to_json())

# convert the object into a dict
user_create_user_with_credentials_request_dict = user_create_user_with_credentials_request_instance.to_dict()
# create an instance of UserCreateUserWithCredentialsRequest from a dict
user_create_user_with_credentials_request_from_dict = UserCreateUserWithCredentialsRequest.from_dict(user_create_user_with_credentials_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


