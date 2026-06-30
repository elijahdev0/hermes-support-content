# AdminSetupMonitoringRequestMetricsConfigServer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refresh_rate** | **float** |  | 
**port** | **float** |  | 
**token** | **str** |  | 
**url_callback** | **str** |  | 
**retention_days** | **float** |  | 
**cron_job** | **str** |  | 
**thresholds** | [**AdminSetupMonitoringRequestMetricsConfigServerThresholds**](AdminSetupMonitoringRequestMetricsConfigServerThresholds.md) |  | 

## Example

```python
from dokploy_client.models.admin_setup_monitoring_request_metrics_config_server import AdminSetupMonitoringRequestMetricsConfigServer

# TODO update the JSON string below
json = "{}"
# create an instance of AdminSetupMonitoringRequestMetricsConfigServer from a JSON string
admin_setup_monitoring_request_metrics_config_server_instance = AdminSetupMonitoringRequestMetricsConfigServer.from_json(json)
# print the JSON string representation of the object
print(AdminSetupMonitoringRequestMetricsConfigServer.to_json())

# convert the object into a dict
admin_setup_monitoring_request_metrics_config_server_dict = admin_setup_monitoring_request_metrics_config_server_instance.to_dict()
# create an instance of AdminSetupMonitoringRequestMetricsConfigServer from a dict
admin_setup_monitoring_request_metrics_config_server_from_dict = AdminSetupMonitoringRequestMetricsConfigServer.from_dict(admin_setup_monitoring_request_metrics_config_server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


