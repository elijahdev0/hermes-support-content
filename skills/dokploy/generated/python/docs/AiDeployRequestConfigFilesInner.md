# AiDeployRequestConfigFilesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_path** | **str** |  | 
**content** | **str** |  | 

## Example

```python
from dokploy_client.models.ai_deploy_request_config_files_inner import AiDeployRequestConfigFilesInner

# TODO update the JSON string below
json = "{}"
# create an instance of AiDeployRequestConfigFilesInner from a JSON string
ai_deploy_request_config_files_inner_instance = AiDeployRequestConfigFilesInner.from_json(json)
# print the JSON string representation of the object
print(AiDeployRequestConfigFilesInner.to_json())

# convert the object into a dict
ai_deploy_request_config_files_inner_dict = ai_deploy_request_config_files_inner_instance.to_dict()
# create an instance of AiDeployRequestConfigFilesInner from a dict
ai_deploy_request_config_files_inner_from_dict = AiDeployRequestConfigFilesInner.from_dict(ai_deploy_request_config_files_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


