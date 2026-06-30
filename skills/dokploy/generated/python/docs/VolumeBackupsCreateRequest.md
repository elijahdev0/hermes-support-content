# VolumeBackupsCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**volume_name** | **str** |  | 
**prefix** | **str** |  | 
**service_type** | **str** |  | [optional] 
**app_name** | **str** |  | [optional] 
**service_name** | **str** |  | [optional] 
**turn_off** | **bool** |  | [optional] 
**cron_expression** | **str** |  | 
**keep_latest_count** | **float** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**application_id** | **str** |  | [optional] 
**postgres_id** | **str** |  | [optional] 
**mariadb_id** | **str** |  | [optional] 
**mongo_id** | **str** |  | [optional] 
**mysql_id** | **str** |  | [optional] 
**redis_id** | **str** |  | [optional] 
**libsql_id** | **str** |  | [optional] 
**compose_id** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**destination_id** | **str** |  | 

## Example

```python
from dokploy_client.models.volume_backups_create_request import VolumeBackupsCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VolumeBackupsCreateRequest from a JSON string
volume_backups_create_request_instance = VolumeBackupsCreateRequest.from_json(json)
# print the JSON string representation of the object
print(VolumeBackupsCreateRequest.to_json())

# convert the object into a dict
volume_backups_create_request_dict = volume_backups_create_request_instance.to_dict()
# create an instance of VolumeBackupsCreateRequest from a dict
volume_backups_create_request_from_dict = VolumeBackupsCreateRequest.from_dict(volume_backups_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


