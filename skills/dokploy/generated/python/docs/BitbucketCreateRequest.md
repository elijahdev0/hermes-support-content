# BitbucketCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bitbucket_id** | **str** |  | [optional] 
**bitbucket_username** | **str** |  | [optional] 
**bitbucket_email** | **str** |  | [optional] 
**app_password** | **str** |  | [optional] 
**api_token** | **str** |  | [optional] 
**bitbucket_workspace_name** | **str** |  | [optional] 
**git_provider_id** | **str** |  | [optional] 
**auth_id** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from dokploy_client.models.bitbucket_create_request import BitbucketCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BitbucketCreateRequest from a JSON string
bitbucket_create_request_instance = BitbucketCreateRequest.from_json(json)
# print the JSON string representation of the object
print(BitbucketCreateRequest.to_json())

# convert the object into a dict
bitbucket_create_request_dict = bitbucket_create_request_instance.to_dict()
# create an instance of BitbucketCreateRequest from a dict
bitbucket_create_request_from_dict = BitbucketCreateRequest.from_dict(bitbucket_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


