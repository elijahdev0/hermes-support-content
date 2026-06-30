# dokploy_client.ForwardAuthApi

All URIs are relative to *http://80.190.82.68:3001/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**forward_auth_deploy_on_server**](ForwardAuthApi.md#forward_auth_deploy_on_server) | **POST** /forwardAuth.deployOnServer | 
[**forward_auth_disable**](ForwardAuthApi.md#forward_auth_disable) | **POST** /forwardAuth.disable | 
[**forward_auth_enable**](ForwardAuthApi.md#forward_auth_enable) | **POST** /forwardAuth.enable | 
[**forward_auth_get_auth_domain**](ForwardAuthApi.md#forward_auth_get_auth_domain) | **GET** /forwardAuth.getAuthDomain | 
[**forward_auth_list_providers**](ForwardAuthApi.md#forward_auth_list_providers) | **GET** /forwardAuth.listProviders | 
[**forward_auth_remove_auth_domain**](ForwardAuthApi.md#forward_auth_remove_auth_domain) | **POST** /forwardAuth.removeAuthDomain | 
[**forward_auth_remove_on_server**](ForwardAuthApi.md#forward_auth_remove_on_server) | **POST** /forwardAuth.removeOnServer | 
[**forward_auth_server_status**](ForwardAuthApi.md#forward_auth_server_status) | **GET** /forwardAuth.serverStatus | 
[**forward_auth_set_auth_domain**](ForwardAuthApi.md#forward_auth_set_auth_domain) | **POST** /forwardAuth.setAuthDomain | 
[**forward_auth_status**](ForwardAuthApi.md#forward_auth_status) | **GET** /forwardAuth.status | 


# **forward_auth_deploy_on_server**
> object forward_auth_deploy_on_server(forward_auth_deploy_on_server_request)

### Example

* Api Key Authentication (apiKey):

```python
import dokploy_client
from dokploy_client.models.forward_auth_deploy_on_server_request import ForwardAuthDeployOnServerRequest
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
    api_instance = dokploy_client.ForwardAuthApi(api_client)
    forward_auth_deploy_on_server_request = dokploy_client.ForwardAuthDeployOnServerRequest() # ForwardAuthDeployOnServerRequest | 

    try:
        api_response = api_instance.forward_auth_deploy_on_server(forward_auth_deploy_on_server_request)
        print("The response of ForwardAuthApi->forward_auth_deploy_on_server:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ForwardAuthApi->forward_auth_deploy_on_server: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forward_auth_deploy_on_server_request** | [**ForwardAuthDeployOnServerRequest**](ForwardAuthDeployOnServerRequest.md)|  | 

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

# **forward_auth_disable**
> object forward_auth_disable(forward_auth_enable_request)

### Example

* Api Key Authentication (apiKey):

```python
import dokploy_client
from dokploy_client.models.forward_auth_enable_request import ForwardAuthEnableRequest
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
    api_instance = dokploy_client.ForwardAuthApi(api_client)
    forward_auth_enable_request = dokploy_client.ForwardAuthEnableRequest() # ForwardAuthEnableRequest | 

    try:
        api_response = api_instance.forward_auth_disable(forward_auth_enable_request)
        print("The response of ForwardAuthApi->forward_auth_disable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ForwardAuthApi->forward_auth_disable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forward_auth_enable_request** | [**ForwardAuthEnableRequest**](ForwardAuthEnableRequest.md)|  | 

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

# **forward_auth_enable**
> object forward_auth_enable(forward_auth_enable_request)

### Example

* Api Key Authentication (apiKey):

```python
import dokploy_client
from dokploy_client.models.forward_auth_enable_request import ForwardAuthEnableRequest
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
    api_instance = dokploy_client.ForwardAuthApi(api_client)
    forward_auth_enable_request = dokploy_client.ForwardAuthEnableRequest() # ForwardAuthEnableRequest | 

    try:
        api_response = api_instance.forward_auth_enable(forward_auth_enable_request)
        print("The response of ForwardAuthApi->forward_auth_enable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ForwardAuthApi->forward_auth_enable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forward_auth_enable_request** | [**ForwardAuthEnableRequest**](ForwardAuthEnableRequest.md)|  | 

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

# **forward_auth_get_auth_domain**
> object forward_auth_get_auth_domain(server_id)

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
    api_instance = dokploy_client.ForwardAuthApi(api_client)
    server_id = 'server_id_example' # str | 

    try:
        api_response = api_instance.forward_auth_get_auth_domain(server_id)
        print("The response of ForwardAuthApi->forward_auth_get_auth_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ForwardAuthApi->forward_auth_get_auth_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**|  | 

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

# **forward_auth_list_providers**
> object forward_auth_list_providers()

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
    api_instance = dokploy_client.ForwardAuthApi(api_client)

    try:
        api_response = api_instance.forward_auth_list_providers()
        print("The response of ForwardAuthApi->forward_auth_list_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ForwardAuthApi->forward_auth_list_providers: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

# **forward_auth_remove_auth_domain**
> object forward_auth_remove_auth_domain(forward_auth_remove_auth_domain_request)

### Example

* Api Key Authentication (apiKey):

```python
import dokploy_client
from dokploy_client.models.forward_auth_remove_auth_domain_request import ForwardAuthRemoveAuthDomainRequest
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
    api_instance = dokploy_client.ForwardAuthApi(api_client)
    forward_auth_remove_auth_domain_request = dokploy_client.ForwardAuthRemoveAuthDomainRequest() # ForwardAuthRemoveAuthDomainRequest | 

    try:
        api_response = api_instance.forward_auth_remove_auth_domain(forward_auth_remove_auth_domain_request)
        print("The response of ForwardAuthApi->forward_auth_remove_auth_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ForwardAuthApi->forward_auth_remove_auth_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forward_auth_remove_auth_domain_request** | [**ForwardAuthRemoveAuthDomainRequest**](ForwardAuthRemoveAuthDomainRequest.md)|  | 

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

# **forward_auth_remove_on_server**
> object forward_auth_remove_on_server(forward_auth_remove_auth_domain_request)

### Example

* Api Key Authentication (apiKey):

```python
import dokploy_client
from dokploy_client.models.forward_auth_remove_auth_domain_request import ForwardAuthRemoveAuthDomainRequest
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
    api_instance = dokploy_client.ForwardAuthApi(api_client)
    forward_auth_remove_auth_domain_request = dokploy_client.ForwardAuthRemoveAuthDomainRequest() # ForwardAuthRemoveAuthDomainRequest | 

    try:
        api_response = api_instance.forward_auth_remove_on_server(forward_auth_remove_auth_domain_request)
        print("The response of ForwardAuthApi->forward_auth_remove_on_server:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ForwardAuthApi->forward_auth_remove_on_server: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forward_auth_remove_auth_domain_request** | [**ForwardAuthRemoveAuthDomainRequest**](ForwardAuthRemoveAuthDomainRequest.md)|  | 

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

# **forward_auth_server_status**
> object forward_auth_server_status()

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
    api_instance = dokploy_client.ForwardAuthApi(api_client)

    try:
        api_response = api_instance.forward_auth_server_status()
        print("The response of ForwardAuthApi->forward_auth_server_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ForwardAuthApi->forward_auth_server_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

# **forward_auth_set_auth_domain**
> object forward_auth_set_auth_domain(forward_auth_set_auth_domain_request)

### Example

* Api Key Authentication (apiKey):

```python
import dokploy_client
from dokploy_client.models.forward_auth_set_auth_domain_request import ForwardAuthSetAuthDomainRequest
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
    api_instance = dokploy_client.ForwardAuthApi(api_client)
    forward_auth_set_auth_domain_request = dokploy_client.ForwardAuthSetAuthDomainRequest() # ForwardAuthSetAuthDomainRequest | 

    try:
        api_response = api_instance.forward_auth_set_auth_domain(forward_auth_set_auth_domain_request)
        print("The response of ForwardAuthApi->forward_auth_set_auth_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ForwardAuthApi->forward_auth_set_auth_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forward_auth_set_auth_domain_request** | [**ForwardAuthSetAuthDomainRequest**](ForwardAuthSetAuthDomainRequest.md)|  | 

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

# **forward_auth_status**
> object forward_auth_status(domain_id)

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
    api_instance = dokploy_client.ForwardAuthApi(api_client)
    domain_id = 'domain_id_example' # str | 

    try:
        api_response = api_instance.forward_auth_status(domain_id)
        print("The response of ForwardAuthApi->forward_auth_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ForwardAuthApi->forward_auth_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**|  | 

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

