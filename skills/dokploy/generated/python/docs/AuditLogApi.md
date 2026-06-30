# dokploy_client.AuditLogApi

All URIs are relative to *http://80.190.82.68:3001/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**audit_log_all**](AuditLogApi.md#audit_log_all) | **GET** /auditLog.all | 


# **audit_log_all**
> object audit_log_all(user_id=user_id, user_email=user_email, resource_name=resource_name, action=action, resource_type=resource_type, var_from=var_from, to=to, limit=limit, offset=offset)

### Example

* Api Key Authentication (apiKey):

```python
import dokploy_client
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
    api_instance = dokploy_client.AuditLogApi(api_client)
    user_id = 'user_id_example' # str |  (optional)
    user_email = 'user_email_example' # str |  (optional)
    resource_name = 'resource_name_example' # str |  (optional)
    action = 'action_example' # str |  (optional)
    resource_type = 'resource_type_example' # str |  (optional)
    var_from = 'var_from_example' # str |  (optional)
    to = 'to_example' # str |  (optional)
    limit = 50 # float |  (optional) (default to 50)
    offset = 0 # float |  (optional) (default to 0)

    try:
        api_response = api_instance.audit_log_all(user_id=user_id, user_email=user_email, resource_name=resource_name, action=action, resource_type=resource_type, var_from=var_from, to=to, limit=limit, offset=offset)
        print("The response of AuditLogApi->audit_log_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditLogApi->audit_log_all: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | [optional] 
 **user_email** | **str**|  | [optional] 
 **resource_name** | **str**|  | [optional] 
 **action** | **str**|  | [optional] 
 **resource_type** | **str**|  | [optional] 
 **var_from** | **str**|  | [optional] 
 **to** | **str**|  | [optional] 
 **limit** | **float**|  | [optional] [default to 50]
 **offset** | **float**|  | [optional] [default to 0]

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid input data |  -  |
**401** | Authorization not provided |  -  |
**403** | Insufficient access |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

