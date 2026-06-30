# LibsqlDeployRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**libsql_id** | **str** |  | 

## Example

```python
from dokploy_client.models.libsql_deploy_request import LibsqlDeployRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LibsqlDeployRequest from a JSON string
libsql_deploy_request_instance = LibsqlDeployRequest.from_json(json)
# print the JSON string representation of the object
print(LibsqlDeployRequest.to_json())

# convert the object into a dict
libsql_deploy_request_dict = libsql_deploy_request_instance.to_dict()
# create an instance of LibsqlDeployRequest from a dict
libsql_deploy_request_from_dict = LibsqlDeployRequest.from_dict(libsql_deploy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


