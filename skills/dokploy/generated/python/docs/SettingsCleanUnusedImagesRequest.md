# SettingsCleanUnusedImagesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_id** | **str** |  | [optional] 

## Example

```python
from dokploy_client.models.settings_clean_unused_images_request import SettingsCleanUnusedImagesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SettingsCleanUnusedImagesRequest from a JSON string
settings_clean_unused_images_request_instance = SettingsCleanUnusedImagesRequest.from_json(json)
# print the JSON string representation of the object
print(SettingsCleanUnusedImagesRequest.to_json())

# convert the object into a dict
settings_clean_unused_images_request_dict = settings_clean_unused_images_request_instance.to_dict()
# create an instance of SettingsCleanUnusedImagesRequest from a dict
settings_clean_unused_images_request_from_dict = SettingsCleanUnusedImagesRequest.from_dict(settings_clean_unused_images_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


