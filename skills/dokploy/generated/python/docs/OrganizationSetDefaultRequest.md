# OrganizationSetDefaultRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** |  | 

## Example

```python
from dokploy_client.models.organization_set_default_request import OrganizationSetDefaultRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationSetDefaultRequest from a JSON string
organization_set_default_request_instance = OrganizationSetDefaultRequest.from_json(json)
# print the JSON string representation of the object
print(OrganizationSetDefaultRequest.to_json())

# convert the object into a dict
organization_set_default_request_dict = organization_set_default_request_instance.to_dict()
# create an instance of OrganizationSetDefaultRequest from a dict
organization_set_default_request_from_dict = OrganizationSetDefaultRequest.from_dict(organization_set_default_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


