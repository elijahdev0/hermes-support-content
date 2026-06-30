# PostgresChangePasswordRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**postgres_id** | **str** |  | 
**password** | **str** |  | 

## Example

```python
from dokploy_client.models.postgres_change_password_request import PostgresChangePasswordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostgresChangePasswordRequest from a JSON string
postgres_change_password_request_instance = PostgresChangePasswordRequest.from_json(json)
# print the JSON string representation of the object
print(PostgresChangePasswordRequest.to_json())

# convert the object into a dict
postgres_change_password_request_dict = postgres_change_password_request_instance.to_dict()
# create an instance of PostgresChangePasswordRequest from a dict
postgres_change_password_request_from_dict = PostgresChangePasswordRequest.from_dict(postgres_change_password_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


