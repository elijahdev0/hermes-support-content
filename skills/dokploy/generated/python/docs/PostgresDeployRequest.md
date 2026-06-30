# PostgresDeployRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**postgres_id** | **str** |  | 

## Example

```python
from dokploy_client.models.postgres_deploy_request import PostgresDeployRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostgresDeployRequest from a JSON string
postgres_deploy_request_instance = PostgresDeployRequest.from_json(json)
# print the JSON string representation of the object
print(PostgresDeployRequest.to_json())

# convert the object into a dict
postgres_deploy_request_dict = postgres_deploy_request_instance.to_dict()
# create an instance of PostgresDeployRequest from a dict
postgres_deploy_request_from_dict = PostgresDeployRequest.from_dict(postgres_deploy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


