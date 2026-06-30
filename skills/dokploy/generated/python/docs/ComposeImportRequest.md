# ComposeImportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_base64** | **str** |  | 
**compose_id** | **str** |  | 

## Example

```python
from dokploy_client.models.compose_import_request import ComposeImportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ComposeImportRequest from a JSON string
compose_import_request_instance = ComposeImportRequest.from_json(json)
# print the JSON string representation of the object
print(ComposeImportRequest.to_json())

# convert the object into a dict
compose_import_request_dict = compose_import_request_instance.to_dict()
# create an instance of ComposeImportRequest from a dict
compose_import_request_from_dict = ComposeImportRequest.from_dict(compose_import_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


