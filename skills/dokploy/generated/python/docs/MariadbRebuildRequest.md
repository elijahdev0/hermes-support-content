# MariadbRebuildRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mariadb_id** | **str** |  | 

## Example

```python
from dokploy_client.models.mariadb_rebuild_request import MariadbRebuildRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MariadbRebuildRequest from a JSON string
mariadb_rebuild_request_instance = MariadbRebuildRequest.from_json(json)
# print the JSON string representation of the object
print(MariadbRebuildRequest.to_json())

# convert the object into a dict
mariadb_rebuild_request_dict = mariadb_rebuild_request_instance.to_dict()
# create an instance of MariadbRebuildRequest from a dict
mariadb_rebuild_request_from_dict = MariadbRebuildRequest.from_dict(mariadb_rebuild_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


