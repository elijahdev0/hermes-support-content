# MysqlDeployRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mysql_id** | **str** |  | 

## Example

```python
from dokploy_client.models.mysql_deploy_request import MysqlDeployRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MysqlDeployRequest from a JSON string
mysql_deploy_request_instance = MysqlDeployRequest.from_json(json)
# print the JSON string representation of the object
print(MysqlDeployRequest.to_json())

# convert the object into a dict
mysql_deploy_request_dict = mysql_deploy_request_instance.to_dict()
# create an instance of MysqlDeployRequest from a dict
mysql_deploy_request_from_dict = MysqlDeployRequest.from_dict(mysql_deploy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


