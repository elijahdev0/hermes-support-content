# WhitelabelingUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**whitelabeling_config** | [**WhitelabelingUpdateRequestWhitelabelingConfig**](WhitelabelingUpdateRequestWhitelabelingConfig.md) |  | 

## Example

```python
from dokploy_client.models.whitelabeling_update_request import WhitelabelingUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WhitelabelingUpdateRequest from a JSON string
whitelabeling_update_request_instance = WhitelabelingUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(WhitelabelingUpdateRequest.to_json())

# convert the object into a dict
whitelabeling_update_request_dict = whitelabeling_update_request_instance.to_dict()
# create an instance of WhitelabelingUpdateRequest from a dict
whitelabeling_update_request_from_dict = WhitelabelingUpdateRequest.from_dict(whitelabeling_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


