# TagRemoveFromProjectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 
**tag_id** | **str** |  | 

## Example

```python
from dokploy_client.models.tag_remove_from_project_request import TagRemoveFromProjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TagRemoveFromProjectRequest from a JSON string
tag_remove_from_project_request_instance = TagRemoveFromProjectRequest.from_json(json)
# print the JSON string representation of the object
print(TagRemoveFromProjectRequest.to_json())

# convert the object into a dict
tag_remove_from_project_request_dict = tag_remove_from_project_request_instance.to_dict()
# create an instance of TagRemoveFromProjectRequest from a dict
tag_remove_from_project_request_from_dict = TagRemoveFromProjectRequest.from_dict(tag_remove_from_project_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


