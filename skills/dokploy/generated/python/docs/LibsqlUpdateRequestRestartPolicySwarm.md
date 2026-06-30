# LibsqlUpdateRequestRestartPolicySwarm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**condition** | **str** |  | [optional] 
**delay** | **float** |  | [optional] 
**max_attempts** | **float** |  | [optional] 
**window** | **float** |  | [optional] 

## Example

```python
from dokploy_client.models.libsql_update_request_restart_policy_swarm import LibsqlUpdateRequestRestartPolicySwarm

# TODO update the JSON string below
json = "{}"
# create an instance of LibsqlUpdateRequestRestartPolicySwarm from a JSON string
libsql_update_request_restart_policy_swarm_instance = LibsqlUpdateRequestRestartPolicySwarm.from_json(json)
# print the JSON string representation of the object
print(LibsqlUpdateRequestRestartPolicySwarm.to_json())

# convert the object into a dict
libsql_update_request_restart_policy_swarm_dict = libsql_update_request_restart_policy_swarm_instance.to_dict()
# create an instance of LibsqlUpdateRequestRestartPolicySwarm from a dict
libsql_update_request_restart_policy_swarm_from_dict = LibsqlUpdateRequestRestartPolicySwarm.from_dict(libsql_update_request_restart_policy_swarm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


