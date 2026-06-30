# EnvironmentCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**project_id** | **str** |  | 

## Example

```python
from dokploy_client.models.environment_create_request import EnvironmentCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentCreateRequest from a JSON string
environment_create_request_instance = EnvironmentCreateRequest.from_json(json)
# print the JSON string representation of the object
print(EnvironmentCreateRequest.to_json())

# convert the object into a dict
environment_create_request_dict = environment_create_request_instance.to_dict()
# create an instance of EnvironmentCreateRequest from a dict
environment_create_request_from_dict = EnvironmentCreateRequest.from_dict(environment_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


