# ComposeRedeployRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compose_id** | **str** |  | 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from dokploy_client.models.compose_redeploy_request import ComposeRedeployRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ComposeRedeployRequest from a JSON string
compose_redeploy_request_instance = ComposeRedeployRequest.from_json(json)
# print the JSON string representation of the object
print(ComposeRedeployRequest.to_json())

# convert the object into a dict
compose_redeploy_request_dict = compose_redeploy_request_instance.to_dict()
# create an instance of ComposeRedeployRequest from a dict
compose_redeploy_request_from_dict = ComposeRedeployRequest.from_dict(compose_redeploy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


