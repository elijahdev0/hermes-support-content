# SettingsUpdateTraefikPortsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_id** | **str** |  | [optional] 
**additional_ports** | [**List[SettingsUpdateTraefikPortsRequestAdditionalPortsInner]**](SettingsUpdateTraefikPortsRequestAdditionalPortsInner.md) |  | 

## Example

```python
from dokploy_client.models.settings_update_traefik_ports_request import SettingsUpdateTraefikPortsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SettingsUpdateTraefikPortsRequest from a JSON string
settings_update_traefik_ports_request_instance = SettingsUpdateTraefikPortsRequest.from_json(json)
# print the JSON string representation of the object
print(SettingsUpdateTraefikPortsRequest.to_json())

# convert the object into a dict
settings_update_traefik_ports_request_dict = settings_update_traefik_ports_request_instance.to_dict()
# create an instance of SettingsUpdateTraefikPortsRequest from a dict
settings_update_traefik_ports_request_from_dict = SettingsUpdateTraefikPortsRequest.from_dict(settings_update_traefik_ports_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


