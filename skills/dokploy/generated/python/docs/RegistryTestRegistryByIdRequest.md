# RegistryTestRegistryByIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**registry_id** | **str** |  | [optional] 
**server_id** | **str** |  | [optional] 

## Example

```python
from dokploy_client.models.registry_test_registry_by_id_request import RegistryTestRegistryByIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RegistryTestRegistryByIdRequest from a JSON string
registry_test_registry_by_id_request_instance = RegistryTestRegistryByIdRequest.from_json(json)
# print the JSON string representation of the object
print(RegistryTestRegistryByIdRequest.to_json())

# convert the object into a dict
registry_test_registry_by_id_request_dict = registry_test_registry_by_id_request_instance.to_dict()
# create an instance of RegistryTestRegistryByIdRequest from a dict
registry_test_registry_by_id_request_from_dict = RegistryTestRegistryByIdRequest.from_dict(registry_test_registry_by_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


