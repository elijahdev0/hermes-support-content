# UserCreateApiKeyRequestMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** |  | 

## Example

```python
from dokploy_client.models.user_create_api_key_request_metadata import UserCreateApiKeyRequestMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of UserCreateApiKeyRequestMetadata from a JSON string
user_create_api_key_request_metadata_instance = UserCreateApiKeyRequestMetadata.from_json(json)
# print the JSON string representation of the object
print(UserCreateApiKeyRequestMetadata.to_json())

# convert the object into a dict
user_create_api_key_request_metadata_dict = user_create_api_key_request_metadata_instance.to_dict()
# create an instance of UserCreateApiKeyRequestMetadata from a dict
user_create_api_key_request_metadata_from_dict = UserCreateApiKeyRequestMetadata.from_dict(user_create_api_key_request_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


