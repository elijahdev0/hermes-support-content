# PreviewDeploymentRedeployRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preview_deployment_id** | **str** |  | 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from dokploy_client.models.preview_deployment_redeploy_request import PreviewDeploymentRedeployRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewDeploymentRedeployRequest from a JSON string
preview_deployment_redeploy_request_instance = PreviewDeploymentRedeployRequest.from_json(json)
# print the JSON string representation of the object
print(PreviewDeploymentRedeployRequest.to_json())

# convert the object into a dict
preview_deployment_redeploy_request_dict = preview_deployment_redeploy_request_instance.to_dict()
# create an instance of PreviewDeploymentRedeployRequest from a dict
preview_deployment_redeploy_request_from_dict = PreviewDeploymentRedeployRequest.from_dict(preview_deployment_redeploy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


