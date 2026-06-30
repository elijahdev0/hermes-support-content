# PreviewDeploymentDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preview_deployment_id** | **str** |  | 

## Example

```python
from dokploy_client.models.preview_deployment_delete_request import PreviewDeploymentDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewDeploymentDeleteRequest from a JSON string
preview_deployment_delete_request_instance = PreviewDeploymentDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(PreviewDeploymentDeleteRequest.to_json())

# convert the object into a dict
preview_deployment_delete_request_dict = preview_deployment_delete_request_instance.to_dict()
# create an instance of PreviewDeploymentDeleteRequest from a dict
preview_deployment_delete_request_from_dict = PreviewDeploymentDeleteRequest.from_dict(preview_deployment_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


