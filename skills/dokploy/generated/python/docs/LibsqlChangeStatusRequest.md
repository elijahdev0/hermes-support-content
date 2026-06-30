# LibsqlChangeStatusRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**libsql_id** | **str** |  | 
**application_status** | **str** |  | 

## Example

```python
from dokploy_client.models.libsql_change_status_request import LibsqlChangeStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LibsqlChangeStatusRequest from a JSON string
libsql_change_status_request_instance = LibsqlChangeStatusRequest.from_json(json)
# print the JSON string representation of the object
print(LibsqlChangeStatusRequest.to_json())

# convert the object into a dict
libsql_change_status_request_dict = libsql_change_status_request_instance.to_dict()
# create an instance of LibsqlChangeStatusRequest from a dict
libsql_change_status_request_from_dict = LibsqlChangeStatusRequest.from_dict(libsql_change_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


