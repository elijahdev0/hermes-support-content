# ComposeProcessTemplateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_base64** | **str** |  | 
**compose_id** | **str** |  | 

## Example

```python
from dokploy_client.models.compose_process_template_request import ComposeProcessTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ComposeProcessTemplateRequest from a JSON string
compose_process_template_request_instance = ComposeProcessTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(ComposeProcessTemplateRequest.to_json())

# convert the object into a dict
compose_process_template_request_dict = compose_process_template_request_instance.to_dict()
# create an instance of ComposeProcessTemplateRequest from a dict
compose_process_template_request_from_dict = ComposeProcessTemplateRequest.from_dict(compose_process_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


