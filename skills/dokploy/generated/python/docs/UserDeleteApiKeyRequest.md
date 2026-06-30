# UserDeleteApiKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key_id** | **str** |  | 

## Example

```python
from dokploy_client.models.user_delete_api_key_request import UserDeleteApiKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserDeleteApiKeyRequest from a JSON string
user_delete_api_key_request_instance = UserDeleteApiKeyRequest.from_json(json)
# print the JSON string representation of the object
print(UserDeleteApiKeyRequest.to_json())

# convert the object into a dict
user_delete_api_key_request_dict = user_delete_api_key_request_instance.to_dict()
# create an instance of UserDeleteApiKeyRequest from a dict
user_delete_api_key_request_from_dict = UserDeleteApiKeyRequest.from_dict(user_delete_api_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


