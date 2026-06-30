# AiSuggestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ai_id** | **str** |  | 
**input** | **str** |  | 
**server_id** | **str** |  | [optional] 

## Example

```python
from dokploy_client.models.ai_suggest_request import AiSuggestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiSuggestRequest from a JSON string
ai_suggest_request_instance = AiSuggestRequest.from_json(json)
# print the JSON string representation of the object
print(AiSuggestRequest.to_json())

# convert the object into a dict
ai_suggest_request_dict = ai_suggest_request_instance.to_dict()
# create an instance of AiSuggestRequest from a dict
ai_suggest_request_from_dict = AiSuggestRequest.from_dict(ai_suggest_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


