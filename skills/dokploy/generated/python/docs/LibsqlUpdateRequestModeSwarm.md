# LibsqlUpdateRequestModeSwarm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replicated** | [**LibsqlUpdateRequestModeSwarmReplicated**](LibsqlUpdateRequestModeSwarmReplicated.md) |  | [optional] 
**var_global** | **object** |  | [optional] 
**replicated_job** | [**LibsqlUpdateRequestModeSwarmReplicatedJob**](LibsqlUpdateRequestModeSwarmReplicatedJob.md) |  | [optional] 
**global_job** | **object** |  | [optional] 

## Example

```python
from dokploy_client.models.libsql_update_request_mode_swarm import LibsqlUpdateRequestModeSwarm

# TODO update the JSON string below
json = "{}"
# create an instance of LibsqlUpdateRequestModeSwarm from a JSON string
libsql_update_request_mode_swarm_instance = LibsqlUpdateRequestModeSwarm.from_json(json)
# print the JSON string representation of the object
print(LibsqlUpdateRequestModeSwarm.to_json())

# convert the object into a dict
libsql_update_request_mode_swarm_dict = libsql_update_request_mode_swarm_instance.to_dict()
# create an instance of LibsqlUpdateRequestModeSwarm from a dict
libsql_update_request_mode_swarm_from_dict = LibsqlUpdateRequestModeSwarm.from_dict(libsql_update_request_mode_swarm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


