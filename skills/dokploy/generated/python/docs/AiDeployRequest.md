# AiDeployRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment_id** | **str** |  | 
**id** | **str** |  | 
**docker_compose** | **str** |  | 
**env_variables** | **str** |  | 
**server_id** | **str** |  | [optional] 
**name** | **str** |  | 
**description** | **str** |  | 
**domains** | [**List[AiDeployRequestDomainsInner]**](AiDeployRequestDomainsInner.md) |  | [optional] 
**config_files** | [**List[AiDeployRequestConfigFilesInner]**](AiDeployRequestConfigFilesInner.md) |  | [optional] 

## Example

```python
from dokploy_client.models.ai_deploy_request import AiDeployRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiDeployRequest from a JSON string
ai_deploy_request_instance = AiDeployRequest.from_json(json)
# print the JSON string representation of the object
print(AiDeployRequest.to_json())

# convert the object into a dict
ai_deploy_request_dict = ai_deploy_request_instance.to_dict()
# create an instance of AiDeployRequest from a dict
ai_deploy_request_from_dict = AiDeployRequest.from_dict(ai_deploy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


