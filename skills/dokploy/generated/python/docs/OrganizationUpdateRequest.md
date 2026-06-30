# OrganizationUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** |  | 
**name** | **str** |  | 
**logo** | **str** |  | [optional] 

## Example

```python
from dokploy_client.models.organization_update_request import OrganizationUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationUpdateRequest from a JSON string
organization_update_request_instance = OrganizationUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(OrganizationUpdateRequest.to_json())

# convert the object into a dict
organization_update_request_dict = organization_update_request_instance.to_dict()
# create an instance of OrganizationUpdateRequest from a dict
organization_update_request_from_dict = OrganizationUpdateRequest.from_dict(organization_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


