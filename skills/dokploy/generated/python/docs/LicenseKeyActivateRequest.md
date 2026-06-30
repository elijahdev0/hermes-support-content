# LicenseKeyActivateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**license_key** | **str** |  | 

## Example

```python
from dokploy_client.models.license_key_activate_request import LicenseKeyActivateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseKeyActivateRequest from a JSON string
license_key_activate_request_instance = LicenseKeyActivateRequest.from_json(json)
# print the JSON string representation of the object
print(LicenseKeyActivateRequest.to_json())

# convert the object into a dict
license_key_activate_request_dict = license_key_activate_request_instance.to_dict()
# create an instance of LicenseKeyActivateRequest from a dict
license_key_activate_request_from_dict = LicenseKeyActivateRequest.from_dict(license_key_activate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


