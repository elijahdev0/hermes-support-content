# LibsqlReloadRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**libsql_id** | **str** |  | 
**app_name** | **str** |  | 

## Example

```python
from dokploy_client.models.libsql_reload_request import LibsqlReloadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LibsqlReloadRequest from a JSON string
libsql_reload_request_instance = LibsqlReloadRequest.from_json(json)
# print the JSON string representation of the object
print(LibsqlReloadRequest.to_json())

# convert the object into a dict
libsql_reload_request_dict = libsql_reload_request_instance.to_dict()
# create an instance of LibsqlReloadRequest from a dict
libsql_reload_request_from_dict = LibsqlReloadRequest.from_dict(libsql_reload_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


