# SettingsUpdateTraefikPortsRequestAdditionalPortsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_port** | **float** |  | 
**published_port** | **float** |  | 
**protocol** | **str** |  | 

## Example

```python
from dokploy_client.models.settings_update_traefik_ports_request_additional_ports_inner import SettingsUpdateTraefikPortsRequestAdditionalPortsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SettingsUpdateTraefikPortsRequestAdditionalPortsInner from a JSON string
settings_update_traefik_ports_request_additional_ports_inner_instance = SettingsUpdateTraefikPortsRequestAdditionalPortsInner.from_json(json)
# print the JSON string representation of the object
print(SettingsUpdateTraefikPortsRequestAdditionalPortsInner.to_json())

# convert the object into a dict
settings_update_traefik_ports_request_additional_ports_inner_dict = settings_update_traefik_ports_request_additional_ports_inner_instance.to_dict()
# create an instance of SettingsUpdateTraefikPortsRequestAdditionalPortsInner from a dict
settings_update_traefik_ports_request_additional_ports_inner_from_dict = SettingsUpdateTraefikPortsRequestAdditionalPortsInner.from_dict(settings_update_traefik_ports_request_additional_ports_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


