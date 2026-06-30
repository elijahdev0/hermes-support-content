# DomainValidateDomainRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** |  | 
**server_ip** | **str** |  | [optional] 

## Example

```python
from dokploy_client.models.domain_validate_domain_request import DomainValidateDomainRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DomainValidateDomainRequest from a JSON string
domain_validate_domain_request_instance = DomainValidateDomainRequest.from_json(json)
# print the JSON string representation of the object
print(DomainValidateDomainRequest.to_json())

# convert the object into a dict
domain_validate_domain_request_dict = domain_validate_domain_request_instance.to_dict()
# create an instance of DomainValidateDomainRequest from a dict
domain_validate_domain_request_from_dict = DomainValidateDomainRequest.from_dict(domain_validate_domain_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


