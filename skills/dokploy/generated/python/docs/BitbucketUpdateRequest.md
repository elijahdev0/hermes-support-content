# BitbucketUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bitbucket_id** | **str** |  | 
**bitbucket_username** | **str** |  | [optional] 
**bitbucket_email** | **str** |  | [optional] 
**app_password** | **str** |  | [optional] 
**api_token** | **str** |  | [optional] 
**bitbucket_workspace_name** | **str** |  | [optional] 
**git_provider_id** | **str** |  | 
**name** | **str** |  | 
**organization_id** | **str** |  | [optional] 

## Example

```python
from dokploy_client.models.bitbucket_update_request import BitbucketUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BitbucketUpdateRequest from a JSON string
bitbucket_update_request_instance = BitbucketUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(BitbucketUpdateRequest.to_json())

# convert the object into a dict
bitbucket_update_request_dict = bitbucket_update_request_instance.to_dict()
# create an instance of BitbucketUpdateRequest from a dict
bitbucket_update_request_from_dict = BitbucketUpdateRequest.from_dict(bitbucket_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


