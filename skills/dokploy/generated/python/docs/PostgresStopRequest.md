# PostgresStopRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**postgres_id** | **str** |  | 

## Example

```python
from dokploy_client.models.postgres_stop_request import PostgresStopRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostgresStopRequest from a JSON string
postgres_stop_request_instance = PostgresStopRequest.from_json(json)
# print the JSON string representation of the object
print(PostgresStopRequest.to_json())

# convert the object into a dict
postgres_stop_request_dict = postgres_stop_request_instance.to_dict()
# create an instance of PostgresStopRequest from a dict
postgres_stop_request_from_dict = PostgresStopRequest.from_dict(postgres_stop_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


