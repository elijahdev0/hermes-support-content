# dokploy_client.DomainApi

All URIs are relative to *http://80.190.82.68:3001/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**domain_by_application_id**](DomainApi.md#domain_by_application_id) | **GET** /domain.byApplicationId | 
[**domain_by_compose_id**](DomainApi.md#domain_by_compose_id) | **GET** /domain.byComposeId | 
[**domain_can_generate_traefik_me_domains**](DomainApi.md#domain_can_generate_traefik_me_domains) | **GET** /domain.canGenerateTraefikMeDomains | 
[**domain_create**](DomainApi.md#domain_create) | **POST** /domain.create | 
[**domain_delete**](DomainApi.md#domain_delete) | **POST** /domain.delete | 
[**domain_generate_domain**](DomainApi.md#domain_generate_domain) | **POST** /domain.generateDomain | 
[**domain_one**](DomainApi.md#domain_one) | **GET** /domain.one | 
[**domain_update**](DomainApi.md#domain_update) | **POST** /domain.update | 
[**domain_validate_domain**](DomainApi.md#domain_validate_domain) | **POST** /domain.validateDomain | 


# **domain_by_application_id**
> object domain_by_application_id(application_id)

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
    api_instance = dokploy_client.DomainApi(api_client)
    application_id = 'application_id_example' # str | 

    try:
        api_response = api_instance.domain_by_application_id(application_id)
        print("The response of DomainApi->domain_by_application_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainApi->domain_by_application_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**|  | 

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

# **domain_by_compose_id**
> object domain_by_compose_id(compose_id)

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
    api_instance = dokploy_client.DomainApi(api_client)
    compose_id = 'compose_id_example' # str | 

    try:
        api_response = api_instance.domain_by_compose_id(compose_id)
        print("The response of DomainApi->domain_by_compose_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainApi->domain_by_compose_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compose_id** | **str**|  | 

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

# **domain_can_generate_traefik_me_domains**
> object domain_can_generate_traefik_me_domains(server_id)

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
    api_instance = dokploy_client.DomainApi(api_client)
    server_id = 'server_id_example' # str | 

    try:
        api_response = api_instance.domain_can_generate_traefik_me_domains(server_id)
        print("The response of DomainApi->domain_can_generate_traefik_me_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainApi->domain_can_generate_traefik_me_domains: %s\n" % e)
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

# **domain_create**
> object domain_create(domain_create_request)

### Example

* Api Key Authentication (apiKey):

```python
import dokploy_client
from dokploy_client.models.domain_create_request import DomainCreateRequest
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
    api_instance = dokploy_client.DomainApi(api_client)
    domain_create_request = dokploy_client.DomainCreateRequest() # DomainCreateRequest | 

    try:
        api_response = api_instance.domain_create(domain_create_request)
        print("The response of DomainApi->domain_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainApi->domain_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_create_request** | [**DomainCreateRequest**](DomainCreateRequest.md)|  | 

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

# **domain_delete**
> object domain_delete(domain_delete_request)

### Example

* Api Key Authentication (apiKey):

```python
import dokploy_client
from dokploy_client.models.domain_delete_request import DomainDeleteRequest
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
    api_instance = dokploy_client.DomainApi(api_client)
    domain_delete_request = dokploy_client.DomainDeleteRequest() # DomainDeleteRequest | 

    try:
        api_response = api_instance.domain_delete(domain_delete_request)
        print("The response of DomainApi->domain_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainApi->domain_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_delete_request** | [**DomainDeleteRequest**](DomainDeleteRequest.md)|  | 

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

# **domain_generate_domain**
> object domain_generate_domain(domain_generate_domain_request)

### Example

* Api Key Authentication (apiKey):

```python
import dokploy_client
from dokploy_client.models.domain_generate_domain_request import DomainGenerateDomainRequest
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
    api_instance = dokploy_client.DomainApi(api_client)
    domain_generate_domain_request = dokploy_client.DomainGenerateDomainRequest() # DomainGenerateDomainRequest | 

    try:
        api_response = api_instance.domain_generate_domain(domain_generate_domain_request)
        print("The response of DomainApi->domain_generate_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainApi->domain_generate_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_generate_domain_request** | [**DomainGenerateDomainRequest**](DomainGenerateDomainRequest.md)|  | 

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

# **domain_one**
> object domain_one(domain_id)

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
    api_instance = dokploy_client.DomainApi(api_client)
    domain_id = 'domain_id_example' # str | 

    try:
        api_response = api_instance.domain_one(domain_id)
        print("The response of DomainApi->domain_one:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainApi->domain_one: %s\n" % e)
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

# **domain_update**
> object domain_update(domain_update_request)

### Example

* Api Key Authentication (apiKey):

```python
import dokploy_client
from dokploy_client.models.domain_update_request import DomainUpdateRequest
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
    api_instance = dokploy_client.DomainApi(api_client)
    domain_update_request = dokploy_client.DomainUpdateRequest() # DomainUpdateRequest | 

    try:
        api_response = api_instance.domain_update(domain_update_request)
        print("The response of DomainApi->domain_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainApi->domain_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_update_request** | [**DomainUpdateRequest**](DomainUpdateRequest.md)|  | 

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

# **domain_validate_domain**
> object domain_validate_domain(domain_validate_domain_request)

### Example

* Api Key Authentication (apiKey):

```python
import dokploy_client
from dokploy_client.models.domain_validate_domain_request import DomainValidateDomainRequest
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
    api_instance = dokploy_client.DomainApi(api_client)
    domain_validate_domain_request = dokploy_client.DomainValidateDomainRequest() # DomainValidateDomainRequest | 

    try:
        api_response = api_instance.domain_validate_domain(domain_validate_domain_request)
        print("The response of DomainApi->domain_validate_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainApi->domain_validate_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_validate_domain_request** | [**DomainValidateDomainRequest**](DomainValidateDomainRequest.md)|  | 

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

