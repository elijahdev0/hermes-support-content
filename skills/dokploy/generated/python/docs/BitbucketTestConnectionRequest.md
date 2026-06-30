# BitbucketTestConnectionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bitbucket_id** | **str** |  | 
**bitbucket_username** | **str** |  | [optional] 
**bitbucket_email** | **str** |  | [optional] 
**workspace_name** | **str** |  | [optional] 
**api_token** | **str** |  | [optional] 
**app_password** | **str** |  | [optional] 

## Example

```python
from dokploy_client.models.bitbucket_test_connection_request import BitbucketTestConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BitbucketTestConnectionRequest from a JSON string
bitbucket_test_connection_request_instance = BitbucketTestConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(BitbucketTestConnectionRequest.to_json())

# convert the object into a dict
bitbucket_test_connection_request_dict = bitbucket_test_connection_request_instance.to_dict()
# create an instance of BitbucketTestConnectionRequest from a dict
bitbucket_test_connection_request_from_dict = BitbucketTestConnectionRequest.from_dict(bitbucket_test_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


