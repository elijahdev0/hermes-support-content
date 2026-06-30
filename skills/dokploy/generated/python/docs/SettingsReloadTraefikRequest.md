# SettingsReloadTraefikRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_id** | **str** |  | [optional] 

## Example

```python
from dokploy_client.models.settings_reload_traefik_request import SettingsReloadTraefikRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SettingsReloadTraefikRequest from a JSON string
settings_reload_traefik_request_instance = SettingsReloadTraefikRequest.from_json(json)
# print the JSON string representation of the object
print(SettingsReloadTraefikRequest.to_json())

# convert the object into a dict
settings_reload_traefik_request_dict = settings_reload_traefik_request_instance.to_dict()
# create an instance of SettingsReloadTraefikRequest from a dict
settings_reload_traefik_request_from_dict = SettingsReloadTraefikRequest.from_dict(settings_reload_traefik_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


