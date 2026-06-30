# dokploy_client.RedirectsApi

All URIs are relative to *http://80.190.82.68:3001/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**redirects_create**](RedirectsApi.md#redirects_create) | **POST** /redirects.create | 
[**redirects_delete**](RedirectsApi.md#redirects_delete) | **POST** /redirects.delete | 
[**redirects_one**](RedirectsApi.md#redirects_one) | **GET** /redirects.one | 
[**redirects_update**](RedirectsApi.md#redirects_update) | **POST** /redirects.update | 


# **redirects_create**
> object redirects_create(redirects_create_request)

### Example

* Api Key Authentication (apiKey):

```python
import dokploy_client
from dokploy_client.models.redirects_create_request import RedirectsCreateRequest
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
    api_instance = dokploy_client.RedirectsApi(api_client)
    redirects_create_request = dokploy_client.RedirectsCreateRequest() # RedirectsCreateRequest | 

    try:
        api_response = api_instance.redirects_create(redirects_create_request)
        print("The response of RedirectsApi->redirects_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RedirectsApi->redirects_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **redirects_create_request** | [**RedirectsCreateRequest**](RedirectsCreateRequest.md)|  | 

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

# **redirects_delete**
> object redirects_delete(redirects_delete_request)

### Example

* Api Key Authentication (apiKey):

```python
import dokploy_client
from dokploy_client.models.redirects_delete_request import RedirectsDeleteRequest
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
    api_instance = dokploy_client.RedirectsApi(api_client)
    redirects_delete_request = dokploy_client.RedirectsDeleteRequest() # RedirectsDeleteRequest | 

    try:
        api_response = api_instance.redirects_delete(redirects_delete_request)
        print("The response of RedirectsApi->redirects_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RedirectsApi->redirects_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **redirects_delete_request** | [**RedirectsDeleteRequest**](RedirectsDeleteRequest.md)|  | 

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

# **redirects_one**
> object redirects_one(redirect_id)

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
    api_instance = dokploy_client.RedirectsApi(api_client)
    redirect_id = 'redirect_id_example' # str | 

    try:
        api_response = api_instance.redirects_one(redirect_id)
        print("The response of RedirectsApi->redirects_one:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RedirectsApi->redirects_one: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **redirect_id** | **str**|  | 

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

# **redirects_update**
> object redirects_update(redirects_update_request)

### Example

* Api Key Authentication (apiKey):

```python
import dokploy_client
from dokploy_client.models.redirects_update_request import RedirectsUpdateRequest
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
    api_instance = dokploy_client.RedirectsApi(api_client)
    redirects_update_request = dokploy_client.RedirectsUpdateRequest() # RedirectsUpdateRequest | 

    try:
        api_response = api_instance.redirects_update(redirects_update_request)
        print("The response of RedirectsApi->redirects_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RedirectsApi->redirects_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **redirects_update_request** | [**RedirectsUpdateRequest**](RedirectsUpdateRequest.md)|  | 

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

