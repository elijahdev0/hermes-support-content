# ApplicationUpdateRequestEndpointSpecSwarm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** |  | [optional] 
**ports** | [**List[ApplicationUpdateRequestEndpointSpecSwarmPortsInner]**](ApplicationUpdateRequestEndpointSpecSwarmPortsInner.md) |  | [optional] 

## Example

```python
from dokploy_client.models.application_update_request_endpoint_spec_swarm import ApplicationUpdateRequestEndpointSpecSwarm

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationUpdateRequestEndpointSpecSwarm from a JSON string
application_update_request_endpoint_spec_swarm_instance = ApplicationUpdateRequestEndpointSpecSwarm.from_json(json)
# print the JSON string representation of the object
print(ApplicationUpdateRequestEndpointSpecSwarm.to_json())

# convert the object into a dict
application_update_request_endpoint_spec_swarm_dict = application_update_request_endpoint_spec_swarm_instance.to_dict()
# create an instance of ApplicationUpdateRequestEndpointSpecSwarm from a dict
application_update_request_endpoint_spec_swarm_from_dict = ApplicationUpdateRequestEndpointSpecSwarm.from_dict(application_update_request_endpoint_spec_swarm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


