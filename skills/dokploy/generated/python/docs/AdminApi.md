# dokploy_client.AdminApi

All URIs are relative to *http://80.190.82.68:3001/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_setup_monitoring**](AdminApi.md#admin_setup_monitoring) | **POST** /admin.setupMonitoring | 


# **admin_setup_monitoring**
> object admin_setup_monitoring(admin_setup_monitoring_request)

### Example

* Api Key Authentication (apiKey):

```python
import dokploy_client
from dokploy_client.models.admin_setup_monitoring_request import AdminSetupMonitoringRequest
from dokploy_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://80.190.82.68:3001/api
# See configuration.py for a list of all supported configuration parameters.
configuration = dokploy_client.Configuration(
    host = "http://80.190.82.68:3001/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with dokploy_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dokploy_client.AdminApi(api_client)
    admin_setup_monitoring_request = dokploy_client.AdminSetupMonitoringRequest() # AdminSetupMonitoringRequest | 

    try:
        api_response = api_instance.admin_setup_monitoring(admin_setup_monitoring_request)
        print("The response of AdminApi->admin_setup_monitoring:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_setup_monitoring: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_setup_monitoring_request** | [**AdminSetupMonitoringRequest**](AdminSetupMonitoringRequest.md)|  | 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid input data |  -  |
**401** | Authorization not provided |  -  |
**403** | Insufficient access |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

