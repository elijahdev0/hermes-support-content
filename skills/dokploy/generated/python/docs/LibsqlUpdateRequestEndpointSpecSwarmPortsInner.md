# LibsqlUpdateRequestEndpointSpecSwarmPortsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocol** | **str** |  | [optional] 
**target_port** | **float** |  | [optional] 
**published_port** | **float** |  | [optional] 
**publish_mode** | **str** |  | [optional] 

## Example

```python
from dokploy_client.models.libsql_update_request_endpoint_spec_swarm_ports_inner import LibsqlUpdateRequestEndpointSpecSwarmPortsInner

# TODO update the JSON string below
json = "{}"
# create an instance of LibsqlUpdateRequestEndpointSpecSwarmPortsInner from a JSON string
libsql_update_request_endpoint_spec_swarm_ports_inner_instance = LibsqlUpdateRequestEndpointSpecSwarmPortsInner.from_json(json)
# print the JSON string representation of the object
print(LibsqlUpdateRequestEndpointSpecSwarmPortsInner.to_json())

# convert the object into a dict
libsql_update_request_endpoint_spec_swarm_ports_inner_dict = libsql_update_request_endpoint_spec_swarm_ports_inner_instance.to_dict()
# create an instance of LibsqlUpdateRequestEndpointSpecSwarmPortsInner from a dict
libsql_update_request_endpoint_spec_swarm_ports_inner_from_dict = LibsqlUpdateRequestEndpointSpecSwarmPortsInner.from_dict(libsql_update_request_endpoint_spec_swarm_ports_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


