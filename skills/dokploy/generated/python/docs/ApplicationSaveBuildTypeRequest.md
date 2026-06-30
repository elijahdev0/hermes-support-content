# ApplicationSaveBuildTypeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **str** |  | 
**build_type** | **str** |  | 
**dockerfile** | **str** |  | 
**docker_context_path** | **str** |  | 
**docker_build_stage** | **str** |  | 
**heroku_version** | **str** |  | 
**railpack_version** | **str** |  | 
**publish_directory** | **str** |  | [optional] 
**is_static_spa** | **bool** |  | [optional] 

## Example

```python
from dokploy_client.models.application_save_build_type_request import ApplicationSaveBuildTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationSaveBuildTypeRequest from a JSON string
application_save_build_type_request_instance = ApplicationSaveBuildTypeRequest.from_json(json)
# print the JSON string representation of the object
print(ApplicationSaveBuildTypeRequest.to_json())

# convert the object into a dict
application_save_build_type_request_dict = application_save_build_type_request_instance.to_dict()
# create an instance of ApplicationSaveBuildTypeRequest from a dict
application_save_build_type_request_from_dict = ApplicationSaveBuildTypeRequest.from_dict(application_save_build_type_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


