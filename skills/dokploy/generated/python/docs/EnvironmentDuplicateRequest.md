# EnvironmentDuplicateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment_id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 

## Example

```python
from dokploy_client.models.environment_duplicate_request import EnvironmentDuplicateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentDuplicateRequest from a JSON string
environment_duplicate_request_instance = EnvironmentDuplicateRequest.from_json(json)
# print the JSON string representation of the object
print(EnvironmentDuplicateRequest.to_json())

# convert the object into a dict
environment_duplicate_request_dict = environment_duplicate_request_instance.to_dict()
# create an instance of EnvironmentDuplicateRequest from a dict
environment_duplicate_request_from_dict = EnvironmentDuplicateRequest.from_dict(environment_duplicate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


