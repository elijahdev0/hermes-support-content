# MariadbStopRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mariadb_id** | **str** |  | 

## Example

```python
from dokploy_client.models.mariadb_stop_request import MariadbStopRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MariadbStopRequest from a JSON string
mariadb_stop_request_instance = MariadbStopRequest.from_json(json)
# print the JSON string representation of the object
print(MariadbStopRequest.to_json())

# convert the object into a dict
mariadb_stop_request_dict = mariadb_stop_request_instance.to_dict()
# create an instance of MariadbStopRequest from a dict
mariadb_stop_request_from_dict = MariadbStopRequest.from_dict(mariadb_stop_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


