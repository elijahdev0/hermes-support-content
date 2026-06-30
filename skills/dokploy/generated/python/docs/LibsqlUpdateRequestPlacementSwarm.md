# LibsqlUpdateRequestPlacementSwarm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**constraints** | **List[str]** |  | [optional] 
**preferences** | [**List[LibsqlUpdateRequestPlacementSwarmPreferencesInner]**](LibsqlUpdateRequestPlacementSwarmPreferencesInner.md) |  | [optional] 
**max_replicas** | **float** |  | [optional] 
**platforms** | [**List[LibsqlUpdateRequestPlacementSwarmPlatformsInner]**](LibsqlUpdateRequestPlacementSwarmPlatformsInner.md) |  | [optional] 

## Example

```python
from dokploy_client.models.libsql_update_request_placement_swarm import LibsqlUpdateRequestPlacementSwarm

# TODO update the JSON string below
json = "{}"
# create an instance of LibsqlUpdateRequestPlacementSwarm from a JSON string
libsql_update_request_placement_swarm_instance = LibsqlUpdateRequestPlacementSwarm.from_json(json)
# print the JSON string representation of the object
print(LibsqlUpdateRequestPlacementSwarm.to_json())

# convert the object into a dict
libsql_update_request_placement_swarm_dict = libsql_update_request_placement_swarm_instance.to_dict()
# create an instance of LibsqlUpdateRequestPlacementSwarm from a dict
libsql_update_request_placement_swarm_from_dict = LibsqlUpdateRequestPlacementSwarm.from_dict(libsql_update_request_placement_swarm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


