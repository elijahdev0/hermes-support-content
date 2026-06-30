# MysqlChangePasswordRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mysql_id** | **str** |  | 
**password** | **str** |  | 
**type** | **str** |  | [optional] [default to 'user']

## Example

```python
from dokploy_client.models.mysql_change_password_request import MysqlChangePasswordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MysqlChangePasswordRequest from a JSON string
mysql_change_password_request_instance = MysqlChangePasswordRequest.from_json(json)
# print the JSON string representation of the object
print(MysqlChangePasswordRequest.to_json())

# convert the object into a dict
mysql_change_password_request_dict = mysql_change_password_request_instance.to_dict()
# create an instance of MysqlChangePasswordRequest from a dict
mysql_change_password_request_from_dict = MysqlChangePasswordRequest.from_dict(mysql_change_password_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


