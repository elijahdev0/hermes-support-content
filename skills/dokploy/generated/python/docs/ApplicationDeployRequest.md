# ApplicationDeployRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **str** |  | 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from dokploy_client.models.application_deploy_request import ApplicationDeployRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationDeployRequest from a JSON string
application_deploy_request_instance = ApplicationDeployRequest.from_json(json)
# print the JSON string representation of the object
print(ApplicationDeployRequest.to_json())

# convert the object into a dict
application_deploy_request_dict = application_deploy_request_instance.to_dict()
# create an instance of ApplicationDeployRequest from a dict
application_deploy_request_from_dict = ApplicationDeployRequest.from_dict(application_deploy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


