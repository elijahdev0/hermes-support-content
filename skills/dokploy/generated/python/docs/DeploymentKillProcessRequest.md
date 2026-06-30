# DeploymentKillProcessRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **str** |  | 

## Example

```python
from dokploy_client.models.deployment_kill_process_request import DeploymentKillProcessRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentKillProcessRequest from a JSON string
deployment_kill_process_request_instance = DeploymentKillProcessRequest.from_json(json)
# print the JSON string representation of the object
print(DeploymentKillProcessRequest.to_json())

# convert the object into a dict
deployment_kill_process_request_dict = deployment_kill_process_request_instance.to_dict()
# create an instance of DeploymentKillProcessRequest from a dict
deployment_kill_process_request_from_dict = DeploymentKillProcessRequest.from_dict(deployment_kill_process_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


