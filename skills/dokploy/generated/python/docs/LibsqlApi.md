# dokploy_client.LibsqlApi

All URIs are relative to *http://80.190.82.68:3001/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**libsql_change_status**](LibsqlApi.md#libsql_change_status) | **POST** /libsql.changeStatus | 
[**libsql_create**](LibsqlApi.md#libsql_create) | **POST** /libsql.create | 
[**libsql_deploy**](LibsqlApi.md#libsql_deploy) | **POST** /libsql.deploy | 
[**libsql_move**](LibsqlApi.md#libsql_move) | **POST** /libsql.move | 
[**libsql_one**](LibsqlApi.md#libsql_one) | **GET** /libsql.one | 
[**libsql_read_logs**](LibsqlApi.md#libsql_read_logs) | **GET** /libsql.readLogs | 
[**libsql_rebuild**](LibsqlApi.md#libsql_rebuild) | **POST** /libsql.rebuild | 
[**libsql_reload**](LibsqlApi.md#libsql_reload) | **POST** /libsql.reload | 
[**libsql_remove**](LibsqlApi.md#libsql_remove) | **POST** /libsql.remove | 
[**libsql_save_environment**](LibsqlApi.md#libsql_save_environment) | **POST** /libsql.saveEnvironment | 
[**libsql_save_external_ports**](LibsqlApi.md#libsql_save_external_ports) | **POST** /libsql.saveExternalPorts | 
[**libsql_start**](LibsqlApi.md#libsql_start) | **POST** /libsql.start | 
[**libsql_stop**](LibsqlApi.md#libsql_stop) | **POST** /libsql.stop | 
[**libsql_update**](LibsqlApi.md#libsql_update) | **POST** /libsql.update | 


# **libsql_change_status**
> object libsql_change_status(libsql_change_status_request)

### Example

* Api Key Authentication (apiKey):

```python
import dokploy_client
from dokploy_client.models.libsql_change_status_request import LibsqlChangeStatusRequest
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
    api_instance = dokploy_client.LibsqlApi(api_client)
    libsql_change_status_request = dokploy_client.LibsqlChangeStatusRequest() # LibsqlChangeStatusRequest | 

    try:
        api_response = api_instance.libsql_change_status(libsql_change_status_request)
        print("The response of LibsqlApi->libsql_change_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LibsqlApi->libsql_change_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **libsql_change_status_request** | [**LibsqlChangeStatusRequest**](LibsqlChangeStatusRequest.md)|  | 

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

# **libsql_create**
> object libsql_create(libsql_create_request)

### Example

* Api Key Authentication (apiKey):

```python
import dokploy_client
from dokploy_client.models.libsql_create_request import LibsqlCreateRequest
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
    api_instance = dokploy_client.LibsqlApi(api_client)
    libsql_create_request = dokploy_client.LibsqlCreateRequest() # LibsqlCreateRequest | 

    try:
        api_response = api_instance.libsql_create(libsql_create_request)
        print("The response of LibsqlApi->libsql_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LibsqlApi->libsql_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **libsql_create_request** | [**LibsqlCreateRequest**](LibsqlCreateRequest.md)|  | 

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

# **libsql_deploy**
> object libsql_deploy(libsql_deploy_request)

### Example

* Api Key Authentication (apiKey):

```python
import dokploy_client
from dokploy_client.models.libsql_deploy_request import LibsqlDeployRequest
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
    api_instance = dokploy_client.LibsqlApi(api_client)
    libsql_deploy_request = dokploy_client.LibsqlDeployRequest() # LibsqlDeployRequest | 

    try:
        api_response = api_instance.libsql_deploy(libsql_deploy_request)
        print("The response of LibsqlApi->libsql_deploy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LibsqlApi->libsql_deploy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **libsql_deploy_request** | [**LibsqlDeployRequest**](LibsqlDeployRequest.md)|  | 

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

# **libsql_move**
> object libsql_move(libsql_move_request)

### Example

* Api Key Authentication (apiKey):

```python
import dokploy_client
from dokploy_client.models.libsql_move_request import LibsqlMoveRequest
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
    api_instance = dokploy_client.LibsqlApi(api_client)
    libsql_move_request = dokploy_client.LibsqlMoveRequest() # LibsqlMoveRequest | 

    try:
        api_response = api_instance.libsql_move(libsql_move_request)
        print("The response of LibsqlApi->libsql_move:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LibsqlApi->libsql_move: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **libsql_move_request** | [**LibsqlMoveRequest**](LibsqlMoveRequest.md)|  | 

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

# **libsql_one**
> object libsql_one(libsql_id)

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
    api_instance = dokploy_client.LibsqlApi(api_client)
    libsql_id = 'libsql_id_example' # str | 

    try:
        api_response = api_instance.libsql_one(libsql_id)
        print("The response of LibsqlApi->libsql_one:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LibsqlApi->libsql_one: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **libsql_id** | **str**|  | 

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

# **libsql_read_logs**
> object libsql_read_logs(libsql_id, tail=tail, since=since, search=search)

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
    api_instance = dokploy_client.LibsqlApi(api_client)
    libsql_id = 'libsql_id_example' # str | 
    tail = 100 # int |  (optional) (default to 100)
    since = 'all' # str |  (optional) (default to 'all')
    search = 'search_example' # str |  (optional)

    try:
        api_response = api_instance.libsql_read_logs(libsql_id, tail=tail, since=since, search=search)
        print("The response of LibsqlApi->libsql_read_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LibsqlApi->libsql_read_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **libsql_id** | **str**|  | 
 **tail** | **int**|  | [optional] [default to 100]
 **since** | **str**|  | [optional] [default to &#39;all&#39;]
 **search** | **str**|  | [optional] 

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

# **libsql_rebuild**
> object libsql_rebuild(libsql_rebuild_request)

### Example

* Api Key Authentication (apiKey):

```python
import dokploy_client
from dokploy_client.models.libsql_rebuild_request import LibsqlRebuildRequest
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
    api_instance = dokploy_client.LibsqlApi(api_client)
    libsql_rebuild_request = dokploy_client.LibsqlRebuildRequest() # LibsqlRebuildRequest | 

    try:
        api_response = api_instance.libsql_rebuild(libsql_rebuild_request)
        print("The response of LibsqlApi->libsql_rebuild:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LibsqlApi->libsql_rebuild: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **libsql_rebuild_request** | [**LibsqlRebuildRequest**](LibsqlRebuildRequest.md)|  | 

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

# **libsql_reload**
> object libsql_reload(libsql_reload_request)

### Example

* Api Key Authentication (apiKey):

```python
import dokploy_client
from dokploy_client.models.libsql_reload_request import LibsqlReloadRequest
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
    api_instance = dokploy_client.LibsqlApi(api_client)
    libsql_reload_request = dokploy_client.LibsqlReloadRequest() # LibsqlReloadRequest | 

    try:
        api_response = api_instance.libsql_reload(libsql_reload_request)
        print("The response of LibsqlApi->libsql_reload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LibsqlApi->libsql_reload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **libsql_reload_request** | [**LibsqlReloadRequest**](LibsqlReloadRequest.md)|  | 

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

# **libsql_remove**
> object libsql_remove(libsql_stop_request)

### Example

* Api Key Authentication (apiKey):

```python
import dokploy_client
from dokploy_client.models.libsql_stop_request import LibsqlStopRequest
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
    api_instance = dokploy_client.LibsqlApi(api_client)
    libsql_stop_request = dokploy_client.LibsqlStopRequest() # LibsqlStopRequest | 

    try:
        api_response = api_instance.libsql_remove(libsql_stop_request)
        print("The response of LibsqlApi->libsql_remove:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LibsqlApi->libsql_remove: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **libsql_stop_request** | [**LibsqlStopRequest**](LibsqlStopRequest.md)|  | 

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

# **libsql_save_environment**
> object libsql_save_environment(libsql_save_environment_request)

### Example

* Api Key Authentication (apiKey):

```python
import dokploy_client
from dokploy_client.models.libsql_save_environment_request import LibsqlSaveEnvironmentRequest
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
    api_instance = dokploy_client.LibsqlApi(api_client)
    libsql_save_environment_request = dokploy_client.LibsqlSaveEnvironmentRequest() # LibsqlSaveEnvironmentRequest | 

    try:
        api_response = api_instance.libsql_save_environment(libsql_save_environment_request)
        print("The response of LibsqlApi->libsql_save_environment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LibsqlApi->libsql_save_environment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **libsql_save_environment_request** | [**LibsqlSaveEnvironmentRequest**](LibsqlSaveEnvironmentRequest.md)|  | 

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

# **libsql_save_external_ports**
> object libsql_save_external_ports(libsql_save_external_ports_request)

### Example

* Api Key Authentication (apiKey):

```python
import dokploy_client
from dokploy_client.models.libsql_save_external_ports_request import LibsqlSaveExternalPortsRequest
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
    api_instance = dokploy_client.LibsqlApi(api_client)
    libsql_save_external_ports_request = dokploy_client.LibsqlSaveExternalPortsRequest() # LibsqlSaveExternalPortsRequest | 

    try:
        api_response = api_instance.libsql_save_external_ports(libsql_save_external_ports_request)
        print("The response of LibsqlApi->libsql_save_external_ports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LibsqlApi->libsql_save_external_ports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **libsql_save_external_ports_request** | [**LibsqlSaveExternalPortsRequest**](LibsqlSaveExternalPortsRequest.md)|  | 

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

# **libsql_start**
> object libsql_start(libsql_start_request)

### Example

* Api Key Authentication (apiKey):

```python
import dokploy_client
from dokploy_client.models.libsql_start_request import LibsqlStartRequest
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
    api_instance = dokploy_client.LibsqlApi(api_client)
    libsql_start_request = dokploy_client.LibsqlStartRequest() # LibsqlStartRequest | 

    try:
        api_response = api_instance.libsql_start(libsql_start_request)
        print("The response of LibsqlApi->libsql_start:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LibsqlApi->libsql_start: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **libsql_start_request** | [**LibsqlStartRequest**](LibsqlStartRequest.md)|  | 

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

# **libsql_stop**
> object libsql_stop(libsql_stop_request)

### Example

* Api Key Authentication (apiKey):

```python
import dokploy_client
from dokploy_client.models.libsql_stop_request import LibsqlStopRequest
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
    api_instance = dokploy_client.LibsqlApi(api_client)
    libsql_stop_request = dokploy_client.LibsqlStopRequest() # LibsqlStopRequest | 

    try:
        api_response = api_instance.libsql_stop(libsql_stop_request)
        print("The response of LibsqlApi->libsql_stop:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LibsqlApi->libsql_stop: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **libsql_stop_request** | [**LibsqlStopRequest**](LibsqlStopRequest.md)|  | 

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

# **libsql_update**
> object libsql_update(libsql_update_request)

### Example

* Api Key Authentication (apiKey):

```python
import dokploy_client
from dokploy_client.models.libsql_update_request import LibsqlUpdateRequest
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
    api_instance = dokploy_client.LibsqlApi(api_client)
    libsql_update_request = dokploy_client.LibsqlUpdateRequest() # LibsqlUpdateRequest | 

    try:
        api_response = api_instance.libsql_update(libsql_update_request)
        print("The response of LibsqlApi->libsql_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LibsqlApi->libsql_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **libsql_update_request** | [**LibsqlUpdateRequest**](LibsqlUpdateRequest.md)|  | 

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

