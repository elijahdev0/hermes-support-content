# MysqlRebuildRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mysql_id** | **str** |  | 

## Example

```python
from dokploy_client.models.mysql_rebuild_request import MysqlRebuildRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MysqlRebuildRequest from a JSON string
mysql_rebuild_request_instance = MysqlRebuildRequest.from_json(json)
# print the JSON string representation of the object
print(MysqlRebuildRequest.to_json())

# convert the object into a dict
mysql_rebuild_request_dict = mysql_rebuild_request_instance.to_dict()
# create an instance of MysqlRebuildRequest from a dict
mysql_rebuild_request_from_dict = MysqlRebuildRequest.from_dict(mysql_rebuild_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


