# RedisUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redis_id** | **str** |  | 
**name** | **str** |  | [optional] 
**app_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**database_password** | **str** |  | [optional] 
**docker_image** | **str** |  | [optional] 
**command** | **str** |  | [optional] 
**args** | **List[str]** |  | [optional] 
**env** | **str** |  | [optional] 
**memory_reservation** | **str** |  | [optional] 
**memory_limit** | **str** |  | [optional] 
**cpu_reservation** | **str** |  | [optional] 
**cpu_limit** | **str** |  | [optional] 
**external_port** | **float** |  | [optional] 
**created_at** | **str** |  | [optional] 
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
**environment_id** | **str** |  | [optional] 

## Example

```python
from dokploy_client.models.redis_update_request import RedisUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RedisUpdateRequest from a JSON string
redis_update_request_instance = RedisUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(RedisUpdateRequest.to_json())

# convert the object into a dict
redis_update_request_dict = redis_update_request_instance.to_dict()
# create an instance of RedisUpdateRequest from a dict
redis_update_request_from_dict = RedisUpdateRequest.from_dict(redis_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


