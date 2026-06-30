# AiAnalyzeLogsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ai_id** | **str** |  | 
**logs** | **str** |  | 
**context** | **str** |  | 

## Example

```python
from dokploy_client.models.ai_analyze_logs_request import AiAnalyzeLogsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiAnalyzeLogsRequest from a JSON string
ai_analyze_logs_request_instance = AiAnalyzeLogsRequest.from_json(json)
# print the JSON string representation of the object
print(AiAnalyzeLogsRequest.to_json())

# convert the object into a dict
ai_analyze_logs_request_dict = ai_analyze_logs_request_instance.to_dict()
# create an instance of AiAnalyzeLogsRequest from a dict
ai_analyze_logs_request_from_dict = AiAnalyzeLogsRequest.from_dict(ai_analyze_logs_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


