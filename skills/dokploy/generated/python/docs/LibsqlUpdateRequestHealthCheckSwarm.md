# LibsqlUpdateRequestHealthCheckSwarm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test** | **List[str]** |  | [optional] 
**interval** | **float** |  | [optional] 
**timeout** | **float** |  | [optional] 
**start_period** | **float** |  | [optional] 
**retries** | **float** |  | [optional] 

## Example

```python
from dokploy_client.models.libsql_update_request_health_check_swarm import LibsqlUpdateRequestHealthCheckSwarm

# TODO update the JSON string below
json = "{}"
# create an instance of LibsqlUpdateRequestHealthCheckSwarm from a JSON string
libsql_update_request_health_check_swarm_instance = LibsqlUpdateRequestHealthCheckSwarm.from_json(json)
# print the JSON string representation of the object
print(LibsqlUpdateRequestHealthCheckSwarm.to_json())

# convert the object into a dict
libsql_update_request_health_check_swarm_dict = libsql_update_request_health_check_swarm_instance.to_dict()
# create an instance of LibsqlUpdateRequestHealthCheckSwarm from a dict
libsql_update_request_health_check_swarm_from_dict = LibsqlUpdateRequestHealthCheckSwarm.from_dict(libsql_update_request_health_check_swarm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


