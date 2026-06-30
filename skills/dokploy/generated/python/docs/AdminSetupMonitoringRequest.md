# AdminSetupMonitoringRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metrics_config** | [**AdminSetupMonitoringRequestMetricsConfig**](AdminSetupMonitoringRequestMetricsConfig.md) |  | 

## Example

```python
from dokploy_client.models.admin_setup_monitoring_request import AdminSetupMonitoringRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AdminSetupMonitoringRequest from a JSON string
admin_setup_monitoring_request_instance = AdminSetupMonitoringRequest.from_json(json)
# print the JSON string representation of the object
print(AdminSetupMonitoringRequest.to_json())

# convert the object into a dict
admin_setup_monitoring_request_dict = admin_setup_monitoring_request_instance.to_dict()
# create an instance of AdminSetupMonitoringRequest from a dict
admin_setup_monitoring_request_from_dict = AdminSetupMonitoringRequest.from_dict(admin_setup_monitoring_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


