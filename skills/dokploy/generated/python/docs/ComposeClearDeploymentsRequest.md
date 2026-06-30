# ComposeClearDeploymentsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compose_id** | **str** |  | 

## Example

```python
from dokploy_client.models.compose_clear_deployments_request import ComposeClearDeploymentsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ComposeClearDeploymentsRequest from a JSON string
compose_clear_deployments_request_instance = ComposeClearDeploymentsRequest.from_json(json)
# print the JSON string representation of the object
print(ComposeClearDeploymentsRequest.to_json())

# convert the object into a dict
compose_clear_deployments_request_dict = compose_clear_deployments_request_instance.to_dict()
# create an instance of ComposeClearDeploymentsRequest from a dict
compose_clear_deployments_request_from_dict = ComposeClearDeploymentsRequest.from_dict(compose_clear_deployments_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


