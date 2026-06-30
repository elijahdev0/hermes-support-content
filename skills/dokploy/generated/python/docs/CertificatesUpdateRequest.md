# CertificatesUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_id** | **str** |  | 
**name** | **str** |  | [optional] 
**certificate_data** | **str** |  | [optional] 
**private_key** | **str** |  | [optional] 

## Example

```python
from dokploy_client.models.certificates_update_request import CertificatesUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CertificatesUpdateRequest from a JSON string
certificates_update_request_instance = CertificatesUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(CertificatesUpdateRequest.to_json())

# convert the object into a dict
certificates_update_request_dict = certificates_update_request_instance.to_dict()
# create an instance of CertificatesUpdateRequest from a dict
certificates_update_request_from_dict = CertificatesUpdateRequest.from_dict(certificates_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


