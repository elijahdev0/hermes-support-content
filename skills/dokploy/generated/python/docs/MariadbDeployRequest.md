# MariadbDeployRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mariadb_id** | **str** |  | 

## Example

```python
from dokploy_client.models.mariadb_deploy_request import MariadbDeployRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MariadbDeployRequest from a JSON string
mariadb_deploy_request_instance = MariadbDeployRequest.from_json(json)
# print the JSON string representation of the object
print(MariadbDeployRequest.to_json())

# convert the object into a dict
mariadb_deploy_request_dict = mariadb_deploy_request_instance.to_dict()
# create an instance of MariadbDeployRequest from a dict
mariadb_deploy_request_from_dict = MariadbDeployRequest.from_dict(mariadb_deploy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


