# ApplicationRedeployRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **str** |  | 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from dokploy_client.models.application_redeploy_request import ApplicationRedeployRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationRedeployRequest from a JSON string
application_redeploy_request_instance = ApplicationRedeployRequest.from_json(json)
# print the JSON string representation of the object
print(ApplicationRedeployRequest.to_json())

# convert the object into a dict
application_redeploy_request_dict = application_redeploy_request_instance.to_dict()
# create an instance of ApplicationRedeployRequest from a dict
application_redeploy_request_from_dict = ApplicationRedeployRequest.from_dict(application_redeploy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


