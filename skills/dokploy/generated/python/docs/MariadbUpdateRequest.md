# MariadbUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mariadb_id** | **str** |  | 
**name** | **str** |  | [optional] 
**app_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**database_name** | **str** |  | [optional] 
**database_user** | **str** |  | [optional] 
**database_password** | **str** |  | [optional] 
**database_root_password** | **str** |  | [optional] 
**docker_image** | **str** |  | [optional] 
**command** | **str** |  | [optional] 
**args** | **List[str]** |  | [optional] 
**env** | **str** |  | [optional] 
**memory_reservation** | **str** |  | [optional] 
**memory_limit** | **str** |  | [optional] 
**cpu_reservation** | **str** |  | [optional] 
**cpu_limit** | **str** |  | [optional] 
**external_port** | **float** |  | [optional] 
**application_status** | **str** |  | [optional] 
**health_check_swarm** | [**LibsqlUpdateRequestHealthCheckSwarm**](LibsqlUpdateRequestHealthCheckSwarm.md) |  | [optional] 
**restart_policy_swarm** | [**LibsqlUpdateRequestRestartPolicySwarm**](LibsqlUpdateRequestRestartPolicySwarm.md) |  | [optional] 
**placement_swarm** | [**LibsqlUpdateRequestPlacementSwarm**](LibsqlUpdateRequestPlacementSwarm.md) |  | [optional] 
**update_config_swarm** | [**ApplicationUpdateRequestRollbackConfigSwarm**](ApplicationUpdateRequestRollbackConfigSwarm.md) |  | [optional] 
**rollback_config_swarm** | [**ApplicationUpdateRequestRollbackConfigSwarm**](ApplicationUpdateRequestRollbackConfigSwarm.md) |  | [optional] 
**mode_swarm** | [**LibsqlUpdateRequestModeSwarm**](LibsqlUpdateRequestModeSwarm.md) |  | [optional] 
**labels_swarm** | **Dict[str, str]** |  | [optional] 
**network_swarm** | [**List[LibsqlUpdateRequestNetworkSwarmInner]**](LibsqlUpdateRequestNetworkSwarmInner.md) |  | [optional] 
**stop_grace_period_swarm** | **float** |  | [optional] 
**endpoint_spec_swarm** | [**LibsqlUpdateRequestEndpointSpecSwarm**](LibsqlUpdateRequestEndpointSpecSwarm.md) |  | [optional] 
**ulimits_swarm** | [**List[MariadbUpdateRequestUlimitsSwarmInner]**](MariadbUpdateRequestUlimitsSwarmInner.md) |  | [optional] 
**replicas** | **float** |  | [optional] 
**created_at** | **str** |  | [optional] 
**environment_id** | **str** |  | [optional] 

## Example

```python
from dokploy_client.models.mariadb_update_request import MariadbUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MariadbUpdateRequest from a JSON string
mariadb_update_request_instance = MariadbUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(MariadbUpdateRequest.to_json())

# convert the object into a dict
mariadb_update_request_dict = mariadb_update_request_instance.to_dict()
# create an instance of MariadbUpdateRequest from a dict
mariadb_update_request_from_dict = MariadbUpdateRequest.from_dict(mariadb_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


