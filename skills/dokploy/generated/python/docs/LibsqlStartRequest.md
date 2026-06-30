# LibsqlStartRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**libsql_id** | **str** |  | 

## Example

```python
from dokploy_client.models.libsql_start_request import LibsqlStartRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LibsqlStartRequest from a JSON string
libsql_start_request_instance = LibsqlStartRequest.from_json(json)
# print the JSON string representation of the object
print(LibsqlStartRequest.to_json())

# convert the object into a dict
libsql_start_request_dict = libsql_start_request_instance.to_dict()
# create an instance of LibsqlStartRequest from a dict
libsql_start_request_from_dict = LibsqlStartRequest.from_dict(libsql_start_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


