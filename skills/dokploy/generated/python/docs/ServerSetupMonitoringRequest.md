# ServerSetupMonitoringRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_id** | **str** |  | 
**metrics_config** | [**AdminSetupMonitoringRequestMetricsConfig**](AdminSetupMonitoringRequestMetricsConfig.md) |  | 

## Example

```python
from dokploy_client.models.server_setup_monitoring_request import ServerSetupMonitoringRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServerSetupMonitoringRequest from a JSON string
server_setup_monitoring_request_instance = ServerSetupMonitoringRequest.from_json(json)
# print the JSON string representation of the object
print(ServerSetupMonitoringRequest.to_json())

# convert the object into a dict
server_setup_monitoring_request_dict = server_setup_monitoring_request_instance.to_dict()
# create an instance of ServerSetupMonitoringRequest from a dict
server_setup_monitoring_request_from_dict = ServerSetupMonitoringRequest.from_dict(server_setup_monitoring_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


