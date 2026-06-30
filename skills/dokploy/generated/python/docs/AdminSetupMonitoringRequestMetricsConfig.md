# AdminSetupMonitoringRequestMetricsConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server** | [**AdminSetupMonitoringRequestMetricsConfigServer**](AdminSetupMonitoringRequestMetricsConfigServer.md) |  | 
**containers** | [**AdminSetupMonitoringRequestMetricsConfigContainers**](AdminSetupMonitoringRequestMetricsConfigContainers.md) |  | 

## Example

```python
from dokploy_client.models.admin_setup_monitoring_request_metrics_config import AdminSetupMonitoringRequestMetricsConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AdminSetupMonitoringRequestMetricsConfig from a JSON string
admin_setup_monitoring_request_metrics_config_instance = AdminSetupMonitoringRequestMetricsConfig.from_json(json)
# print the JSON string representation of the object
print(AdminSetupMonitoringRequestMetricsConfig.to_json())

# convert the object into a dict
admin_setup_monitoring_request_metrics_config_dict = admin_setup_monitoring_request_metrics_config_instance.to_dict()
# create an instance of AdminSetupMonitoringRequestMetricsConfig from a dict
admin_setup_monitoring_request_metrics_config_from_dict = AdminSetupMonitoringRequestMetricsConfig.from_dict(admin_setup_monitoring_request_metrics_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


