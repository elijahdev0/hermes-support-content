# SettingsUpdateWebServerTraefikConfigRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**traefik_config** | **str** |  | 

## Example

```python
from dokploy_client.models.settings_update_web_server_traefik_config_request import SettingsUpdateWebServerTraefikConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SettingsUpdateWebServerTraefikConfigRequest from a JSON string
settings_update_web_server_traefik_config_request_instance = SettingsUpdateWebServerTraefikConfigRequest.from_json(json)
# print the JSON string representation of the object
print(SettingsUpdateWebServerTraefikConfigRequest.to_json())

# convert the object into a dict
settings_update_web_server_traefik_config_request_dict = settings_update_web_server_traefik_config_request_instance.to_dict()
# create an instance of SettingsUpdateWebServerTraefikConfigRequest from a dict
settings_update_web_server_traefik_config_request_from_dict = SettingsUpdateWebServerTraefikConfigRequest.from_dict(settings_update_web_server_traefik_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


