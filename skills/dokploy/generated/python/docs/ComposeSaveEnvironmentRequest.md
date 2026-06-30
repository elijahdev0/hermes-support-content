# ComposeSaveEnvironmentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compose_id** | **str** |  | 
**env** | **str** |  | 

## Example

```python
from dokploy_client.models.compose_save_environment_request import ComposeSaveEnvironmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ComposeSaveEnvironmentRequest from a JSON string
compose_save_environment_request_instance = ComposeSaveEnvironmentRequest.from_json(json)
# print the JSON string representation of the object
print(ComposeSaveEnvironmentRequest.to_json())

# convert the object into a dict
compose_save_environment_request_dict = compose_save_environment_request_instance.to_dict()
# create an instance of ComposeSaveEnvironmentRequest from a dict
compose_save_environment_request_from_dict = ComposeSaveEnvironmentRequest.from_dict(compose_save_environment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


