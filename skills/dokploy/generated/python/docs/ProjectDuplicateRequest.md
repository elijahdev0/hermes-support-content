# ProjectDuplicateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_environment_id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**include_services** | **bool** |  | [optional] [default to True]
**selected_services** | [**List[ProjectDuplicateRequestSelectedServicesInner]**](ProjectDuplicateRequestSelectedServicesInner.md) |  | [optional] 
**duplicate_in_same_project** | **bool** |  | [optional] [default to False]

## Example

```python
from dokploy_client.models.project_duplicate_request import ProjectDuplicateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectDuplicateRequest from a JSON string
project_duplicate_request_instance = ProjectDuplicateRequest.from_json(json)
# print the JSON string representation of the object
print(ProjectDuplicateRequest.to_json())

# convert the object into a dict
project_duplicate_request_dict = project_duplicate_request_instance.to_dict()
# create an instance of ProjectDuplicateRequest from a dict
project_duplicate_request_from_dict = ProjectDuplicateRequest.from_dict(project_duplicate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


