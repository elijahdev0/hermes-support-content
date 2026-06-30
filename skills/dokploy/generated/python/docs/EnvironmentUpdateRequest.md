# EnvironmentUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment_id** | **str** |  | 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**project_id** | **str** |  | [optional] 
**env** | **str** |  | [optional] 

## Example

```python
from dokploy_client.models.environment_update_request import EnvironmentUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentUpdateRequest from a JSON string
environment_update_request_instance = EnvironmentUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(EnvironmentUpdateRequest.to_json())

# convert the object into a dict
environment_update_request_dict = environment_update_request_instance.to_dict()
# create an instance of EnvironmentUpdateRequest from a dict
environment_update_request_from_dict = EnvironmentUpdateRequest.from_dict(environment_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


