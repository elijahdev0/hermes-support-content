# WhitelabelingUpdateRequestWhitelabelingConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_name** | **str** |  | 
**app_description** | **str** |  | 
**logo_url** | **str** |  | 
**favicon_url** | **str** |  | 
**custom_css** | **str** |  | 
**login_logo_url** | **str** |  | 
**support_url** | **str** |  | 
**docs_url** | **str** |  | 
**error_page_title** | **str** |  | 
**error_page_description** | **str** |  | 
**meta_title** | **str** |  | 
**footer_text** | **str** |  | 

## Example

```python
from dokploy_client.models.whitelabeling_update_request_whitelabeling_config import WhitelabelingUpdateRequestWhitelabelingConfig

# TODO update the JSON string below
json = "{}"
# create an instance of WhitelabelingUpdateRequestWhitelabelingConfig from a JSON string
whitelabeling_update_request_whitelabeling_config_instance = WhitelabelingUpdateRequestWhitelabelingConfig.from_json(json)
# print the JSON string representation of the object
print(WhitelabelingUpdateRequestWhitelabelingConfig.to_json())

# convert the object into a dict
whitelabeling_update_request_whitelabeling_config_dict = whitelabeling_update_request_whitelabeling_config_instance.to_dict()
# create an instance of WhitelabelingUpdateRequestWhitelabelingConfig from a dict
whitelabeling_update_request_whitelabeling_config_from_dict = WhitelabelingUpdateRequestWhitelabelingConfig.from_dict(whitelabeling_update_request_whitelabeling_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


