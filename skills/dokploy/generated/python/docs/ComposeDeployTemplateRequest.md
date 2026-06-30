# ComposeDeployTemplateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment_id** | **str** |  | 
**server_id** | **str** |  | [optional] 
**id** | **str** |  | 
**base_url** | **str** |  | [optional] 

## Example

```python
from dokploy_client.models.compose_deploy_template_request import ComposeDeployTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ComposeDeployTemplateRequest from a JSON string
compose_deploy_template_request_instance = ComposeDeployTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(ComposeDeployTemplateRequest.to_json())

# convert the object into a dict
compose_deploy_template_request_dict = compose_deploy_template_request_instance.to_dict()
# create an instance of ComposeDeployTemplateRequest from a dict
compose_deploy_template_request_from_dict = ComposeDeployTemplateRequest.from_dict(compose_deploy_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


