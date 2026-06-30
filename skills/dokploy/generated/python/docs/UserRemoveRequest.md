# UserRemoveRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 

## Example

```python
from dokploy_client.models.user_remove_request import UserRemoveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserRemoveRequest from a JSON string
user_remove_request_instance = UserRemoveRequest.from_json(json)
# print the JSON string representation of the object
print(UserRemoveRequest.to_json())

# convert the object into a dict
user_remove_request_dict = user_remove_request_instance.to_dict()
# create an instance of UserRemoveRequest from a dict
user_remove_request_from_dict = UserRemoveRequest.from_dict(user_remove_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


