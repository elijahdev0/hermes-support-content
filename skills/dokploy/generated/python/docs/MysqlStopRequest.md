# MysqlStopRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mysql_id** | **str** |  | 

## Example

```python
from dokploy_client.models.mysql_stop_request import MysqlStopRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MysqlStopRequest from a JSON string
mysql_stop_request_instance = MysqlStopRequest.from_json(json)
# print the JSON string representation of the object
print(MysqlStopRequest.to_json())

# convert the object into a dict
mysql_stop_request_dict = mysql_stop_request_instance.to_dict()
# create an instance of MysqlStopRequest from a dict
mysql_stop_request_from_dict = MysqlStopRequest.from_dict(mysql_stop_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


