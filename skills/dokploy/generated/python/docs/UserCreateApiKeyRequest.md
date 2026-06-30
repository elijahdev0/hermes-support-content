# UserCreateApiKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**prefix** | **str** |  | [optional] 
**expires_in** | **float** |  | [optional] 
**metadata** | [**UserCreateApiKeyRequestMetadata**](UserCreateApiKeyRequestMetadata.md) |  | 
**rate_limit_enabled** | **bool** |  | [optional] 
**rate_limit_time_window** | **float** |  | [optional] 
**rate_limit_max** | **float** |  | [optional] 
**remaining** | **float** |  | [optional] 
**refill_amount** | **float** |  | [optional] 
**refill_interval** | **float** |  | [optional] 

## Example

```python
from dokploy_client.models.user_create_api_key_request import UserCreateApiKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserCreateApiKeyRequest from a JSON string
user_create_api_key_request_instance = UserCreateApiKeyRequest.from_json(json)
# print the JSON string representation of the object
print(UserCreateApiKeyRequest.to_json())

# convert the object into a dict
user_create_api_key_request_dict = user_create_api_key_request_instance.to_dict()
# create an instance of UserCreateApiKeyRequest from a dict
user_create_api_key_request_from_dict = UserCreateApiKeyRequest.from_dict(user_create_api_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


