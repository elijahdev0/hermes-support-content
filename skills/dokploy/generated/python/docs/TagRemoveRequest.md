# TagRemoveRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag_id** | **str** |  | 

## Example

```python
from dokploy_client.models.tag_remove_request import TagRemoveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TagRemoveRequest from a JSON string
tag_remove_request_instance = TagRemoveRequest.from_json(json)
# print the JSON string representation of the object
print(TagRemoveRequest.to_json())

# convert the object into a dict
tag_remove_request_dict = tag_remove_request_instance.to_dict()
# create an instance of TagRemoveRequest from a dict
tag_remove_request_from_dict = TagRemoveRequest.from_dict(tag_remove_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


