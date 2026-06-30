# LibsqlUpdateRequestEndpointSpecSwarm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** |  | [optional] 
**ports** | [**List[LibsqlUpdateRequestEndpointSpecSwarmPortsInner]**](LibsqlUpdateRequestEndpointSpecSwarmPortsInner.md) |  | [optional] 

## Example

```python
from dokploy_client.models.libsql_update_request_endpoint_spec_swarm import LibsqlUpdateRequestEndpointSpecSwarm

# TODO update the JSON string below
json = "{}"
# create an instance of LibsqlUpdateRequestEndpointSpecSwarm from a JSON string
libsql_update_request_endpoint_spec_swarm_instance = LibsqlUpdateRequestEndpointSpecSwarm.from_json(json)
# print the JSON string representation of the object
print(LibsqlUpdateRequestEndpointSpecSwarm.to_json())

# convert the object into a dict
libsql_update_request_endpoint_spec_swarm_dict = libsql_update_request_endpoint_spec_swarm_instance.to_dict()
# create an instance of LibsqlUpdateRequestEndpointSpecSwarm from a dict
libsql_update_request_endpoint_spec_swarm_from_dict = LibsqlUpdateRequestEndpointSpecSwarm.from_dict(libsql_update_request_endpoint_spec_swarm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


