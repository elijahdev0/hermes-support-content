# EnvironmentRemoveRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment_id** | **str** |  | 

## Example

```python
from dokploy_client.models.environment_remove_request import EnvironmentRemoveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentRemoveRequest from a JSON string
environment_remove_request_instance = EnvironmentRemoveRequest.from_json(json)
# print the JSON string representation of the object
print(EnvironmentRemoveRequest.to_json())

# convert the object into a dict
environment_remove_request_dict = environment_remove_request_instance.to_dict()
# create an instance of EnvironmentRemoveRequest from a dict
environment_remove_request_from_dict = EnvironmentRemoveRequest.from_dict(environment_remove_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


