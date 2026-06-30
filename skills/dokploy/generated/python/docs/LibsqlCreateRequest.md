# LibsqlCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**app_name** | **str** |  | 
**docker_image** | **str** |  | [default to 'ghcr.io/tursodatabase/libsql-server:v0.24.32']
**environment_id** | **str** |  | 
**description** | **str** |  | 
**database_user** | **str** |  | 
**database_password** | **str** |  | 
**sqld_node** | **str** |  | 
**sqld_primary_url** | **str** |  | 
**enable_namespaces** | **bool** |  | [default to False]
**server_id** | **str** |  | 

## Example

```python
from dokploy_client.models.libsql_create_request import LibsqlCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LibsqlCreateRequest from a JSON string
libsql_create_request_instance = LibsqlCreateRequest.from_json(json)
# print the JSON string representation of the object
print(LibsqlCreateRequest.to_json())

# convert the object into a dict
libsql_create_request_dict = libsql_create_request_instance.to_dict()
# create an instance of LibsqlCreateRequest from a dict
libsql_create_request_from_dict = LibsqlCreateRequest.from_dict(libsql_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


