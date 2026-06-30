# AiUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ai_id** | **str** |  | 
**name** | **str** |  | [optional] 
**api_url** | **str** |  | [optional] 
**api_key** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**is_enabled** | **bool** |  | [optional] 
**created_at** | **str** |  | [optional] 

## Example

```python
from dokploy_client.models.ai_update_request import AiUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiUpdateRequest from a JSON string
ai_update_request_instance = AiUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(AiUpdateRequest.to_json())

# convert the object into a dict
ai_update_request_dict = ai_update_request_instance.to_dict()
# create an instance of AiUpdateRequest from a dict
ai_update_request_from_dict = AiUpdateRequest.from_dict(ai_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


