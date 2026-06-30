# DomainCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** |  | 
**path** | **str** |  | [optional] 
**port** | **float** |  | [optional] 
**custom_entrypoint** | **str** |  | [optional] 
**https** | **bool** |  | [optional] 
**application_id** | **str** |  | [optional] 
**certificate_type** | **str** |  | [optional] 
**custom_cert_resolver** | **str** |  | [optional] 
**compose_id** | **str** |  | [optional] 
**service_name** | **str** |  | [optional] 
**domain_type** | **str** |  | [optional] 
**preview_deployment_id** | **str** |  | [optional] 
**internal_path** | **str** |  | [optional] 
**strip_path** | **bool** |  | [optional] 
**middlewares** | **List[str]** |  | [optional] 
**forward_auth_enabled** | **bool** |  | [optional] 

## Example

```python
from dokploy_client.models.domain_create_request import DomainCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DomainCreateRequest from a JSON string
domain_create_request_instance = DomainCreateRequest.from_json(json)
# print the JSON string representation of the object
print(DomainCreateRequest.to_json())

# convert the object into a dict
domain_create_request_dict = domain_create_request_instance.to_dict()
# create an instance of DomainCreateRequest from a dict
domain_create_request_from_dict = DomainCreateRequest.from_dict(domain_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


