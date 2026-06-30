# ApplicationUpdateRequestRollbackConfigSwarm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parallelism** | **float** |  | 
**delay** | **float** |  | [optional] 
**failure_action** | **str** |  | [optional] 
**monitor** | **float** |  | [optional] 
**max_failure_ratio** | **float** |  | [optional] 
**order** | **str** |  | 

## Example

```python
from dokploy_client.models.application_update_request_rollback_config_swarm import ApplicationUpdateRequestRollbackConfigSwarm

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationUpdateRequestRollbackConfigSwarm from a JSON string
application_update_request_rollback_config_swarm_instance = ApplicationUpdateRequestRollbackConfigSwarm.from_json(json)
# print the JSON string representation of the object
print(ApplicationUpdateRequestRollbackConfigSwarm.to_json())

# convert the object into a dict
application_update_request_rollback_config_swarm_dict = application_update_request_rollback_config_swarm_instance.to_dict()
# create an instance of ApplicationUpdateRequestRollbackConfigSwarm from a dict
application_update_request_rollback_config_swarm_from_dict = ApplicationUpdateRequestRollbackConfigSwarm.from_dict(application_update_request_rollback_config_swarm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


