# dokploy_client.RollbackApi

All URIs are relative to *http://80.190.82.68:3001/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rollback_delete**](RollbackApi.md#rollback_delete) | **POST** /rollback.delete | 
[**rollback_rollback**](RollbackApi.md#rollback_rollback) | **POST** /rollback.rollback | 


# **rollback_delete**
> object rollback_delete(rollback_delete_request)

### Example

* Api Key Authentication (apiKey):

```python
import dokploy_client
from dokploy_client.models.rollback_delete_request import RollbackDeleteRequest
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
    api_instance = dokploy_client.RollbackApi(api_client)
    rollback_delete_request = dokploy_client.RollbackDeleteRequest() # RollbackDeleteRequest | 

    try:
        api_response = api_instance.rollback_delete(rollback_delete_request)
        print("The response of RollbackApi->rollback_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RollbackApi->rollback_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rollback_delete_request** | [**RollbackDeleteRequest**](RollbackDeleteRequest.md)|  | 

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

# **rollback_rollback**
> object rollback_rollback(rollback_rollback_request)

### Example

* Api Key Authentication (apiKey):

```python
import dokploy_client
from dokploy_client.models.rollback_rollback_request import RollbackRollbackRequest
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
    api_instance = dokploy_client.RollbackApi(api_client)
    rollback_rollback_request = dokploy_client.RollbackRollbackRequest() # RollbackRollbackRequest | 

    try:
        api_response = api_instance.rollback_rollback(rollback_rollback_request)
        print("The response of RollbackApi->rollback_rollback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RollbackApi->rollback_rollback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rollback_rollback_request** | [**RollbackRollbackRequest**](RollbackRollbackRequest.md)|  | 

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

