# ApplicationUpdateRequestEndpointSpecSwarmPortsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocol** | **str** |  | [optional] 
**target_port** | **float** |  | [optional] 
**published_port** | **float** |  | [optional] 
**publish_mode** | **str** |  | [optional] 

## Example

```python
from dokploy_client.models.application_update_request_endpoint_spec_swarm_ports_inner import ApplicationUpdateRequestEndpointSpecSwarmPortsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationUpdateRequestEndpointSpecSwarmPortsInner from a JSON string
application_update_request_endpoint_spec_swarm_ports_inner_instance = ApplicationUpdateRequestEndpointSpecSwarmPortsInner.from_json(json)
# print the JSON string representation of the object
print(ApplicationUpdateRequestEndpointSpecSwarmPortsInner.to_json())

# convert the object into a dict
application_update_request_endpoint_spec_swarm_ports_inner_dict = application_update_request_endpoint_spec_swarm_ports_inner_instance.to_dict()
# create an instance of ApplicationUpdateRequestEndpointSpecSwarmPortsInner from a dict
application_update_request_endpoint_spec_swarm_ports_inner_from_dict = ApplicationUpdateRequestEndpointSpecSwarmPortsInner.from_dict(application_update_request_endpoint_spec_swarm_ports_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


