# AiCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**api_url** | **str** |  | 
**api_key** | **str** |  | 
**model** | **str** |  | 
**is_enabled** | **bool** |  | 

## Example

```python
from dokploy_client.models.ai_create_request import AiCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiCreateRequest from a JSON string
ai_create_request_instance = AiCreateRequest.from_json(json)
# print the JSON string representation of the object
print(AiCreateRequest.to_json())

# convert the object into a dict
ai_create_request_dict = ai_create_request_instance.to_dict()
# create an instance of AiCreateRequest from a dict
ai_create_request_from_dict = AiCreateRequest.from_dict(ai_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


