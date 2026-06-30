# OrganizationDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** |  | 

## Example

```python
from dokploy_client.models.organization_delete_request import OrganizationDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationDeleteRequest from a JSON string
organization_delete_request_instance = OrganizationDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(OrganizationDeleteRequest.to_json())

# convert the object into a dict
organization_delete_request_dict = organization_delete_request_instance.to_dict()
# create an instance of OrganizationDeleteRequest from a dict
organization_delete_request_from_dict = OrganizationDeleteRequest.from_dict(organization_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


