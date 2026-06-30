# LibsqlSaveExternalPortsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**libsql_id** | **str** |  | 
**external_port** | **float** |  | [optional] 
**external_grpc_port** | **float** |  | [optional] 
**external_admin_port** | **float** |  | [optional] 

## Example

```python
from dokploy_client.models.libsql_save_external_ports_request import LibsqlSaveExternalPortsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LibsqlSaveExternalPortsRequest from a JSON string
libsql_save_external_ports_request_instance = LibsqlSaveExternalPortsRequest.from_json(json)
# print the JSON string representation of the object
print(LibsqlSaveExternalPortsRequest.to_json())

# convert the object into a dict
libsql_save_external_ports_request_dict = libsql_save_external_ports_request_instance.to_dict()
# create an instance of LibsqlSaveExternalPortsRequest from a dict
libsql_save_external_ports_request_from_dict = LibsqlSaveExternalPortsRequest.from_dict(libsql_save_external_ports_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


