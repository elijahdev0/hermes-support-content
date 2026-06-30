# MariadbUpdateRequestUlimitsSwarmInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**soft** | **int** |  | 
**hard** | **int** |  | 

## Example

```python
from dokploy_client.models.mariadb_update_request_ulimits_swarm_inner import MariadbUpdateRequestUlimitsSwarmInner

# TODO update the JSON string below
json = "{}"
# create an instance of MariadbUpdateRequestUlimitsSwarmInner from a JSON string
mariadb_update_request_ulimits_swarm_inner_instance = MariadbUpdateRequestUlimitsSwarmInner.from_json(json)
# print the JSON string representation of the object
print(MariadbUpdateRequestUlimitsSwarmInner.to_json())

# convert the object into a dict
mariadb_update_request_ulimits_swarm_inner_dict = mariadb_update_request_ulimits_swarm_inner_instance.to_dict()
# create an instance of MariadbUpdateRequestUlimitsSwarmInner from a dict
mariadb_update_request_ulimits_swarm_inner_from_dict = MariadbUpdateRequestUlimitsSwarmInner.from_dict(mariadb_update_request_ulimits_swarm_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


