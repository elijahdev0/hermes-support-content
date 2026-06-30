# DeploymentRemoveDeploymentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **str** |  | 

## Example

```python
from dokploy_client.models.deployment_remove_deployment_request import DeploymentRemoveDeploymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentRemoveDeploymentRequest from a JSON string
deployment_remove_deployment_request_instance = DeploymentRemoveDeploymentRequest.from_json(json)
# print the JSON string representation of the object
print(DeploymentRemoveDeploymentRequest.to_json())

# convert the object into a dict
deployment_remove_deployment_request_dict = deployment_remove_deployment_request_instance.to_dict()
# create an instance of DeploymentRemoveDeploymentRequest from a dict
deployment_remove_deployment_request_from_dict = DeploymentRemoveDeploymentRequest.from_dict(deployment_remove_deployment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


