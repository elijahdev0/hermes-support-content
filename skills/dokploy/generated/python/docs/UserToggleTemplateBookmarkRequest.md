# UserToggleTemplateBookmarkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **str** |  | 

## Example

```python
from dokploy_client.models.user_toggle_template_bookmark_request import UserToggleTemplateBookmarkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserToggleTemplateBookmarkRequest from a JSON string
user_toggle_template_bookmark_request_instance = UserToggleTemplateBookmarkRequest.from_json(json)
# print the JSON string representation of the object
print(UserToggleTemplateBookmarkRequest.to_json())

# convert the object into a dict
user_toggle_template_bookmark_request_dict = user_toggle_template_bookmark_request_instance.to_dict()
# create an instance of UserToggleTemplateBookmarkRequest from a dict
user_toggle_template_bookmark_request_from_dict = UserToggleTemplateBookmarkRequest.from_dict(user_toggle_template_bookmark_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


