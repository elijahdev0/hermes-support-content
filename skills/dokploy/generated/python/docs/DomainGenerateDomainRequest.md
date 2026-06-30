# DomainGenerateDomainRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_name** | **str** |  | 
**server_id** | **str** |  | [optional] 

## Example

```python
from dokploy_client.models.domain_generate_domain_request import DomainGenerateDomainRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DomainGenerateDomainRequest from a JSON string
domain_generate_domain_request_instance = DomainGenerateDomainRequest.from_json(json)
# print the JSON string representation of the object
print(DomainGenerateDomainRequest.to_json())

# convert the object into a dict
domain_generate_domain_request_dict = domain_generate_domain_request_instance.to_dict()
# create an instance of DomainGenerateDomainRequest from a dict
domain_generate_domain_request_from_dict = DomainGenerateDomainRequest.from_dict(domain_generate_domain_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


