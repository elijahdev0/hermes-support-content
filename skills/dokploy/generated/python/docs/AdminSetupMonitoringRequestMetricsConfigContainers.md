# AdminSetupMonitoringRequestMetricsConfigContainers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refresh_rate** | **float** |  | 
**services** | [**AdminSetupMonitoringRequestMetricsConfigContainersServices**](AdminSetupMonitoringRequestMetricsConfigContainersServices.md) |  | 

## Example

```python
from dokploy_client.models.admin_setup_monitoring_request_metrics_config_containers import AdminSetupMonitoringRequestMetricsConfigContainers

# TODO update the JSON string below
json = "{}"
# create an instance of AdminSetupMonitoringRequestMetricsConfigContainers from a JSON string
admin_setup_monitoring_request_metrics_config_containers_instance = AdminSetupMonitoringRequestMetricsConfigContainers.from_json(json)
# print the JSON string representation of the object
print(AdminSetupMonitoringRequestMetricsConfigContainers.to_json())

# convert the object into a dict
admin_setup_monitoring_request_metrics_config_containers_dict = admin_setup_monitoring_request_metrics_config_containers_instance.to_dict()
# create an instance of AdminSetupMonitoringRequestMetricsConfigContainers from a dict
admin_setup_monitoring_request_metrics_config_containers_from_dict = AdminSetupMonitoringRequestMetricsConfigContainers.from_dict(admin_setup_monitoring_request_metrics_config_containers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


