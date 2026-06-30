# LibsqlStopRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**libsql_id** | **str** |  | 

## Example

```python
from dokploy_client.models.libsql_stop_request import LibsqlStopRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LibsqlStopRequest from a JSON string
libsql_stop_request_instance = LibsqlStopRequest.from_json(json)
# print the JSON string representation of the object
print(LibsqlStopRequest.to_json())

# convert the object into a dict
libsql_stop_request_dict = libsql_stop_request_instance.to_dict()
# create an instance of LibsqlStopRequest from a dict
libsql_stop_request_from_dict = LibsqlStopRequest.from_dict(libsql_stop_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


