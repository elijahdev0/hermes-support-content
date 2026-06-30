# PostgresRebuildRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**postgres_id** | **str** |  | 

## Example

```python
from dokploy_client.models.postgres_rebuild_request import PostgresRebuildRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostgresRebuildRequest from a JSON string
postgres_rebuild_request_instance = PostgresRebuildRequest.from_json(json)
# print the JSON string representation of the object
print(PostgresRebuildRequest.to_json())

# convert the object into a dict
postgres_rebuild_request_dict = postgres_rebuild_request_instance.to_dict()
# create an instance of PostgresRebuildRequest from a dict
postgres_rebuild_request_from_dict = PostgresRebuildRequest.from_dict(postgres_rebuild_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


