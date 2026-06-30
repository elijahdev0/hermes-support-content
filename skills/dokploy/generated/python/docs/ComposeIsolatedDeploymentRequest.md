# ComposeIsolatedDeploymentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compose_id** | **str** |  | 
**suffix** | **str** |  | [optional] 

## Example

```python
from dokploy_client.models.compose_isolated_deployment_request import ComposeIsolatedDeploymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ComposeIsolatedDeploymentRequest from a JSON string
compose_isolated_deployment_request_instance = ComposeIsolatedDeploymentRequest.from_json(json)
# print the JSON string representation of the object
print(ComposeIsolatedDeploymentRequest.to_json())

# convert the object into a dict
compose_isolated_deployment_request_dict = compose_isolated_deployment_request_instance.to_dict()
# create an instance of ComposeIsolatedDeploymentRequest from a dict
compose_isolated_deployment_request_from_dict = ComposeIsolatedDeploymentRequest.from_dict(compose_isolated_deployment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


