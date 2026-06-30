# MariadbChangePasswordRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mariadb_id** | **str** |  | 
**password** | **str** |  | 
**type** | **str** |  | [optional] [default to 'user']

## Example

```python
from dokploy_client.models.mariadb_change_password_request import MariadbChangePasswordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MariadbChangePasswordRequest from a JSON string
mariadb_change_password_request_instance = MariadbChangePasswordRequest.from_json(json)
# print the JSON string representation of the object
print(MariadbChangePasswordRequest.to_json())

# convert the object into a dict
mariadb_change_password_request_dict = mariadb_change_password_request_instance.to_dict()
# create an instance of MariadbChangePasswordRequest from a dict
mariadb_change_password_request_from_dict = MariadbChangePasswordRequest.from_dict(mariadb_change_password_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


