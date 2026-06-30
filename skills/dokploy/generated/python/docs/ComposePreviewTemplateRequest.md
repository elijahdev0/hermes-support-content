# ComposePreviewTemplateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_base64** | **str** |  | 
**app_name** | **str** |  | 
**server_id** | **str** |  | [optional] 

## Example

```python
from dokploy_client.models.compose_preview_template_request import ComposePreviewTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ComposePreviewTemplateRequest from a JSON string
compose_preview_template_request_instance = ComposePreviewTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(ComposePreviewTemplateRequest.to_json())

# convert the object into a dict
compose_preview_template_request_dict = compose_preview_template_request_instance.to_dict()
# create an instance of ComposePreviewTemplateRequest from a dict
compose_preview_template_request_from_dict = ComposePreviewTemplateRequest.from_dict(compose_preview_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


