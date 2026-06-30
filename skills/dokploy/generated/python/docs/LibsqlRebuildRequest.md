# LibsqlRebuildRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**libsql_id** | **str** |  | 

## Example

```python
from dokploy_client.models.libsql_rebuild_request import LibsqlRebuildRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LibsqlRebuildRequest from a JSON string
libsql_rebuild_request_instance = LibsqlRebuildRequest.from_json(json)
# print the JSON string representation of the object
print(LibsqlRebuildRequest.to_json())

# convert the object into a dict
libsql_rebuild_request_dict = libsql_rebuild_request_instance.to_dict()
# create an instance of LibsqlRebuildRequest from a dict
libsql_rebuild_request_from_dict = LibsqlRebuildRequest.from_dict(libsql_rebuild_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


