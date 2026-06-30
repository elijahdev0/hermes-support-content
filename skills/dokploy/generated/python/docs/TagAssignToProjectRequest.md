# TagAssignToProjectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 
**tag_id** | **str** |  | 

## Example

```python
from dokploy_client.models.tag_assign_to_project_request import TagAssignToProjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TagAssignToProjectRequest from a JSON string
tag_assign_to_project_request_instance = TagAssignToProjectRequest.from_json(json)
# print the JSON string representation of the object
print(TagAssignToProjectRequest.to_json())

# convert the object into a dict
tag_assign_to_project_request_dict = tag_assign_to_project_request_instance.to_dict()
# create an instance of TagAssignToProjectRequest from a dict
tag_assign_to_project_request_from_dict = TagAssignToProjectRequest.from_dict(tag_assign_to_project_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


