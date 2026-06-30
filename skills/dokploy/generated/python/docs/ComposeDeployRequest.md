# ComposeDeployRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compose_id** | **str** |  | 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from dokploy_client.models.compose_deploy_request import ComposeDeployRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ComposeDeployRequest from a JSON string
compose_deploy_request_instance = ComposeDeployRequest.from_json(json)
# print the JSON string representation of the object
print(ComposeDeployRequest.to_json())

# convert the object into a dict
compose_deploy_request_dict = compose_deploy_request_instance.to_dict()
# create an instance of ComposeDeployRequest from a dict
compose_deploy_request_from_dict = ComposeDeployRequest.from_dict(compose_deploy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


