# AiTestConnectionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_url** | **str** |  | 
**api_key** | **str** |  | 
**model** | **str** |  | 

## Example

```python
from dokploy_client.models.ai_test_connection_request import AiTestConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiTestConnectionRequest from a JSON string
ai_test_connection_request_instance = AiTestConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(AiTestConnectionRequest.to_json())

# convert the object into a dict
ai_test_connection_request_dict = ai_test_connection_request_instance.to_dict()
# create an instance of AiTestConnectionRequest from a dict
ai_test_connection_request_from_dict = AiTestConnectionRequest.from_dict(ai_test_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


