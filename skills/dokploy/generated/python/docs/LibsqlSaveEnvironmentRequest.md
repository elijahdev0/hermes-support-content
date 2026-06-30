# LibsqlSaveEnvironmentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**libsql_id** | **str** |  | 
**env** | **str** |  | 

## Example

```python
from dokploy_client.models.libsql_save_environment_request import LibsqlSaveEnvironmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LibsqlSaveEnvironmentRequest from a JSON string
libsql_save_environment_request_instance = LibsqlSaveEnvironmentRequest.from_json(json)
# print the JSON string representation of the object
print(LibsqlSaveEnvironmentRequest.to_json())

# convert the object into a dict
libsql_save_environment_request_dict = libsql_save_environment_request_instance.to_dict()
# create an instance of LibsqlSaveEnvironmentRequest from a dict
libsql_save_environment_request_from_dict = LibsqlSaveEnvironmentRequest.from_dict(libsql_save_environment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


